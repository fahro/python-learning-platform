import { useState, useEffect } from 'react'
import { useParams, Link, useNavigate } from 'react-router-dom'
import { ArrowLeft, ArrowRight, Play, CheckCircle, Loader2, BookOpen, Code, Lightbulb, HelpCircle, Check, X } from 'lucide-react'
import ReactMarkdown from 'react-markdown'
import { Prism as SyntaxHighlighter } from 'react-syntax-highlighter'
import { oneDark } from 'react-syntax-highlighter/dist/esm/styles/prism'
import { fetchLesson, fetchNextLesson, executeCode, updateProgress, getUserId } from '../api'

export default function LessonView() {
  const { lessonId } = useParams()
  const navigate = useNavigate()
  const [lesson, setLesson] = useState(null)
  const [nextLessonInfo, setNextLessonInfo] = useState(null)
  const [loading, setLoading] = useState(true)
  const [code, setCode] = useState('')
  const [output, setOutput] = useState('')
  const [running, setRunning] = useState(false)
  const [activeTab, setActiveTab] = useState('content')
  const [completed, setCompleted] = useState(false)
  const [quizAnswers, setQuizAnswers] = useState({})
  const [quizSubmitted, setQuizSubmitted] = useState(false)
  const [showSolution, setShowSolution] = useState(false)
  const userId = getUserId()

  useEffect(() => {
    async function loadLesson() {
      setLoading(true)
      try {
        const data = await fetchLesson(lessonId)
        setLesson(data)
        setCode(data.code_example || '')
        
        const next = await fetchNextLesson(lessonId)
        setNextLessonInfo(next)
      } catch (e) {
        console.error('Error loading lesson:', e)
      } finally {
        setLoading(false)
      }
    }
    loadLesson()
    setOutput('')
    setCompleted(false)
    setActiveTab('content')
    setQuizAnswers({})
    setQuizSubmitted(false)
    setShowSolution(false)
  }, [lessonId])

  // Parse quiz from lesson
  const parseQuiz = () => {
    if (!lesson?.quiz) return []
    try {
      return JSON.parse(lesson.quiz)
    } catch (e) {
      return []
    }
  }

  const quizQuestions = lesson ? parseQuiz() : []

  const handleQuizAnswer = (questionIndex, answerIndex) => {
    if (quizSubmitted) return
    setQuizAnswers(prev => ({ ...prev, [questionIndex]: answerIndex }))
  }

  const submitQuiz = () => {
    setQuizSubmitted(true)
  }

  const resetQuiz = () => {
    setQuizAnswers({})
    setQuizSubmitted(false)
  }

  const getQuizScore = () => {
    let correct = 0
    quizQuestions.forEach((q, i) => {
      if (quizAnswers[i] === q.correct) correct++
    })
    return correct
  }

  // Parse exercises from markdown
  const parseExercises = () => {
    if (!lesson?.exercise) return []
    const text = lesson.exercise
    const exercises = []
    const regex = /###\s*Vježba\s*(\d+)[:\s]*([^\n]+)\n([^#]*?)(?=###|$)/gi
    let match
    while ((match = regex.exec(text)) !== null) {
      exercises.push({
        number: match[1],
        title: match[2].trim(),
        description: match[3].trim()
      })
    }
    if (exercises.length === 0 && text.trim()) {
      exercises.push({ number: '1', title: 'Vježba', description: text })
    }
    return exercises
  }

  const exercises = lesson ? parseExercises() : []

  const runCode = async () => {
    setRunning(true)
    setOutput('')
    try {
      const result = await executeCode(code, parseInt(lessonId), userId)
      let outputText = result.output || ''
      if (result.error) {
        outputText += '\n❌ Error: ' + result.error
      }
      outputText += `\n\n⏱️ Vrijeme izvršavanja: ${result.execution_time}s`
      setOutput(outputText)
    } catch (e) {
      setOutput('❌ Greška pri izvršavanju koda: ' + e.message)
    } finally {
      setRunning(false)
    }
  }

  const markComplete = async () => {
    try {
      await updateProgress(userId, parseInt(lessonId), true, code)
      setCompleted(true)
    } catch (e) {
      console.error('Error updating progress:', e)
    }
  }

  const loadExercise = () => {
    if (lesson?.exercise_solution) {
      setCode(lesson.exercise_solution)
    }
  }

  if (loading) {
    return (
      <div className="flex items-center justify-center min-h-[400px]">
        <Loader2 className="animate-spin text-python-blue" size={40} />
      </div>
    )
  }

  if (!lesson) {
    return (
      <div className="max-w-4xl mx-auto px-4 py-8 text-center">
        <h1 className="text-2xl font-bold">Lekcija nije pronađena</h1>
        <Link to="/modules" className="text-python-blue hover:underline mt-4 inline-block">
          ← Nazad na module
        </Link>
      </div>
    )
  }

  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-6">
      {/* Header */}
      <div className="flex items-center justify-between mb-6">
        <Link 
          to={`/modules/${lesson.module_id}`}
          className="inline-flex items-center text-gray-600 hover:text-python-blue"
        >
          <ArrowLeft size={20} className="mr-2" />
          Nazad na modul
        </Link>
        
        {completed && (
          <span className="flex items-center text-green-600">
            <CheckCircle size={20} className="mr-2" />
            Završeno!
          </span>
        )}
      </div>

      {/* Lesson Title */}
      <h1 className="text-2xl md:text-3xl font-bold mb-6">{lesson.title}</h1>

      {/* Tabs */}
      <div className="flex border-b mb-6 overflow-x-auto">
        {[
          { id: 'content', label: 'Sadržaj', icon: BookOpen },
          { id: 'code', label: 'Code Editor', icon: Code },
          { id: 'exercise', label: 'Vježbe', icon: Lightbulb },
          { id: 'quiz', label: 'Kviz', icon: HelpCircle, badge: quizQuestions.length },
        ].map(tab => (
          <button
            key={tab.id}
            onClick={() => setActiveTab(tab.id)}
            className={`flex items-center px-4 py-3 border-b-2 transition-colors whitespace-nowrap ${
              activeTab === tab.id
                ? 'border-python-blue text-python-blue'
                : 'border-transparent text-gray-500 hover:text-gray-700'
            }`}
          >
            <tab.icon size={18} className="mr-2" />
            {tab.label}
            {tab.badge > 0 && (
              <span className="ml-2 bg-purple-100 text-purple-700 text-xs px-2 py-0.5 rounded-full">
                {tab.badge}
              </span>
            )}
          </button>
        ))}
      </div>

      {/* Content Tab */}
      {activeTab === 'content' && (
        <div className="prose max-w-none lesson-content bg-white rounded-xl p-6 shadow-sm">
          <ReactMarkdown
            components={{
              code({ node, inline, className, children, ...props }) {
                const match = /language-(\w+)/.exec(className || '')
                return !inline && match ? (
                  <SyntaxHighlighter
                    style={oneDark}
                    language={match[1]}
                    PreTag="div"
                    {...props}
                  >
                    {String(children).replace(/\n$/, '')}
                  </SyntaxHighlighter>
                ) : (
                  <code className={className} {...props}>
                    {children}
                  </code>
                )
              }
            }}
          >
            {lesson.content || 'Sadržaj nije dostupan.'}
          </ReactMarkdown>
        </div>
      )}

      {/* Code Editor Tab */}
      {activeTab === 'code' && (
        <div className="grid lg:grid-cols-2 gap-6">
          {/* Editor */}
          <div className="bg-gray-900 rounded-xl overflow-hidden">
            <div className="flex items-center justify-between px-4 py-2 bg-gray-800">
              <span className="text-gray-400 text-sm">Python Editor</span>
              <button
                onClick={runCode}
                disabled={running}
                className="flex items-center bg-green-600 text-white px-4 py-1.5 rounded-lg text-sm hover:bg-green-700 disabled:opacity-50"
              >
                {running ? (
                  <Loader2 size={16} className="mr-2 animate-spin" />
                ) : (
                  <Play size={16} className="mr-2" />
                )}
                {running ? 'Izvršavam...' : 'Pokreni'}
              </button>
            </div>
            <textarea
              value={code}
              onChange={(e) => setCode(e.target.value)}
              className="w-full h-80 bg-gray-900 text-gray-100 font-mono text-sm p-4 resize-none focus:outline-none"
              placeholder="# Upiši Python kod ovdje..."
              spellCheck={false}
            />
          </div>

          {/* Output */}
          <div className="bg-white rounded-xl shadow-sm overflow-hidden">
            <div className="px-4 py-2 bg-gray-100 border-b">
              <span className="text-gray-600 text-sm font-medium">Output</span>
            </div>
            <pre className="p-4 h-80 overflow-auto text-sm font-mono whitespace-pre-wrap">
              {output || 'Klikni "Pokreni" da vidiš output...'}
            </pre>
          </div>
        </div>
      )}

      {/* Exercise Tab */}
      {activeTab === 'exercise' && (
        <div className="bg-white rounded-xl p-6 shadow-sm">
          <h3 className="text-xl font-semibold mb-6 flex items-center">
            <Lightbulb className="mr-2 text-yellow-500" />
            Vježbe
          </h3>
          
          {exercises.length > 0 ? (
            <>
              <div className="grid gap-4 mb-6">
                {exercises.map((ex, i) => (
                  <div key={i} className="border border-gray-200 rounded-xl p-5 hover:border-blue-300 hover:shadow-md transition-all">
                    <div className="flex items-start gap-4">
                      <div className="flex-shrink-0 w-10 h-10 bg-gradient-to-br from-blue-500 to-blue-600 text-white rounded-lg flex items-center justify-center font-bold text-lg">
                        {ex.number}
                      </div>
                      <div className="flex-1">
                        <h4 className="font-semibold text-gray-800 mb-2">{ex.title}</h4>
                        <p className="text-gray-600 text-sm leading-relaxed">{ex.description}</p>
                      </div>
                    </div>
                  </div>
                ))}
              </div>
              
              <div className="border-t pt-6">
                <div className="flex flex-wrap gap-3">
                  <button
                    onClick={() => setActiveTab('code')}
                    className="btn-primary"
                  >
                    <Code size={18} className="mr-2 inline" />
                    Otvori Editor
                  </button>
                  {lesson.exercise_solution && (
                    <button
                      onClick={() => setShowSolution(!showSolution)}
                      className="btn-secondary"
                    >
                      {showSolution ? 'Sakrij Rješenje' : 'Prikaži Rješenje'}
                    </button>
                  )}
                </div>
                
                {showSolution && lesson.exercise_solution && (
                  <div className="mt-6">
                    <h4 className="font-semibold text-gray-700 mb-3">Rješenja:</h4>
                    <div className="bg-gray-900 rounded-xl overflow-hidden">
                      <SyntaxHighlighter
                        style={oneDark}
                        language="python"
                        customStyle={{ margin: 0, padding: '1rem', fontSize: '0.875rem' }}
                      >
                        {lesson.exercise_solution}
                      </SyntaxHighlighter>
                    </div>
                  </div>
                )}
              </div>
            </>
          ) : (
            <p className="text-gray-500">Nema vježbi za ovu lekciju.</p>
          )}
        </div>
      )}

      {/* Quiz Tab */}
      {activeTab === 'quiz' && (
        <div className="bg-white rounded-xl p-6 shadow-sm">
          <h3 className="text-xl font-semibold mb-6 flex items-center">
            <HelpCircle className="mr-2 text-purple-500" />
            Kviz - Testiraj svoje znanje
          </h3>
          
          {quizQuestions.length > 0 ? (
            <>
              {quizSubmitted && (
                <div className={`mb-6 p-4 rounded-xl ${
                  getQuizScore() === quizQuestions.length 
                    ? 'bg-green-50 border border-green-200' 
                    : getQuizScore() >= quizQuestions.length / 2 
                      ? 'bg-yellow-50 border border-yellow-200'
                      : 'bg-red-50 border border-red-200'
                }`}>
                  <div className="flex items-center justify-between">
                    <div>
                      <span className="font-semibold text-lg">
                        Rezultat: {getQuizScore()}/{quizQuestions.length}
                      </span>
                      <span className="ml-3 text-gray-600">
                        ({Math.round(getQuizScore() / quizQuestions.length * 100)}%)
                      </span>
                    </div>
                    {getQuizScore() === quizQuestions.length && (
                      <span className="text-green-600 font-medium">Odlično! 🎉</span>
                    )}
                  </div>
                </div>
              )}
              
              <div className="space-y-6">
                {quizQuestions.map((q, qIndex) => (
                  <div key={qIndex} className="border border-gray-200 rounded-xl p-5">
                    <div className="flex items-start gap-3 mb-4">
                      <span className="flex-shrink-0 w-8 h-8 bg-purple-100 text-purple-700 rounded-lg flex items-center justify-center font-semibold text-sm">
                        {qIndex + 1}
                      </span>
                      <p className="font-medium text-gray-800 pt-1">{q.question}</p>
                    </div>
                    
                    <div className="grid gap-2 ml-11">
                      {q.options.map((option, oIndex) => {
                        const isSelected = quizAnswers[qIndex] === oIndex
                        const isCorrect = q.correct === oIndex
                        const showResult = quizSubmitted
                        
                        let bgClass = 'bg-gray-50 hover:bg-gray-100 border-gray-200'
                        if (showResult) {
                          if (isCorrect) {
                            bgClass = 'bg-green-50 border-green-400'
                          } else if (isSelected && !isCorrect) {
                            bgClass = 'bg-red-50 border-red-400'
                          }
                        } else if (isSelected) {
                          bgClass = 'bg-blue-50 border-blue-400'
                        }
                        
                        return (
                          <button
                            key={oIndex}
                            onClick={() => handleQuizAnswer(qIndex, oIndex)}
                            disabled={quizSubmitted}
                            className={`flex items-center gap-3 p-3 rounded-lg border text-left transition-all ${bgClass} ${!quizSubmitted && 'cursor-pointer'}`}
                          >
                            <span className={`w-6 h-6 rounded-full border-2 flex items-center justify-center text-xs ${
                              isSelected ? 'border-blue-500 bg-blue-500 text-white' : 'border-gray-300'
                            }`}>
                              {showResult && isCorrect && <Check size={14} />}
                              {showResult && isSelected && !isCorrect && <X size={14} />}
                              {!showResult && isSelected && '●'}
                            </span>
                            <span className="text-gray-700">{option}</span>
                          </button>
                        )
                      })}
                    </div>
                  </div>
                ))}
              </div>
              
              <div className="mt-6 flex gap-3">
                {!quizSubmitted ? (
                  <button
                    onClick={submitQuiz}
                    disabled={Object.keys(quizAnswers).length < quizQuestions.length}
                    className="btn-primary disabled:opacity-50 disabled:cursor-not-allowed"
                  >
                    <CheckCircle size={18} className="mr-2 inline" />
                    Provjeri Odgovore
                  </button>
                ) : (
                  <button onClick={resetQuiz} className="btn-secondary">
                    Pokušaj Ponovo
                  </button>
                )}
              </div>
            </>
          ) : (
            <p className="text-gray-500">Nema kviza za ovu lekciju.</p>
          )}
        </div>
      )}

      {/* Navigation Footer */}
      <div className="mt-8 flex items-center justify-between border-t pt-6">
        <Link
          to={`/modules/${lesson.module_id}`}
          className="btn-secondary"
        >
          <ArrowLeft size={18} className="mr-2 inline" />
          Sve lekcije
        </Link>

        <div className="flex gap-3">
          {!completed && (
            <button onClick={markComplete} className="btn-success">
              <CheckCircle size={18} className="mr-2 inline" />
              Označi kao završeno
            </button>
          )}
          
          {nextLessonInfo?.next_lesson_id && (
            <button
              onClick={() => navigate(`/lessons/${nextLessonInfo.next_lesson_id}`)}
              className="btn-primary"
            >
              Sljedeća lekcija
              <ArrowRight size={18} className="ml-2 inline" />
            </button>
          )}
        </div>
      </div>
    </div>
  )
}
