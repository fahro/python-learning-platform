import { useState, useEffect } from 'react'
import { useParams, Link, useNavigate } from 'react-router-dom'
import { ArrowLeft, ArrowRight, Play, CheckCircle, Loader2, BookOpen, Code, Lightbulb, HelpCircle, Check, X, Send, Trophy, AlertCircle } from 'lucide-react'
import ReactMarkdown from 'react-markdown'
import { Prism as SyntaxHighlighter } from 'react-syntax-highlighter'
import { oneDark } from 'react-syntax-highlighter/dist/esm/styles/prism'
import { fetchLesson, fetchNextLesson, executeCode, submitExercise, submitQuiz, getExerciseStatus, getQuizStatus } from '../api'

export default function LessonView({ user }) {
  const { lessonId } = useParams()
  const navigate = useNavigate()
  const [lesson, setLesson] = useState(null)
  const [nextLessonInfo, setNextLessonInfo] = useState(null)
  const [loading, setLoading] = useState(true)
  const [code, setCode] = useState('')
  const [exerciseCodes, setExerciseCodes] = useState({})
  const [output, setOutput] = useState('')
  const [exerciseResults, setExerciseResults] = useState({})
  const [running, setRunning] = useState(false)
  const [submittingExercise, setSubmittingExercise] = useState({})
  const [submittingQuiz, setSubmittingQuiz] = useState(false)
  const [activeTab, setActiveTab] = useState('content')
  const [quizAnswers, setQuizAnswers] = useState({})
  const [quizResult, setQuizResult] = useState(null)
  const [exerciseResult, setExerciseResult] = useState(null)
  const [showSolution, setShowSolution] = useState(false)
  const [exerciseStatus, setExerciseStatus] = useState(null)
  const [quizStatus, setQuizStatus] = useState(null)

  useEffect(() => {
    async function loadLesson() {
      setLoading(true)
      try {
        const data = await fetchLesson(lessonId)
        setLesson(data)
        setCode(data.code_example || '')
        setExerciseCodes({})
        setExerciseResults({})
        
        const next = await fetchNextLesson(lessonId)
        setNextLessonInfo(next)
        
        // Load exercise and quiz status
        try {
          const [exStatus, qzStatus] = await Promise.all([
            getExerciseStatus(lessonId),
            getQuizStatus(lessonId)
          ])
          setExerciseStatus(exStatus)
          setQuizStatus(qzStatus)
        } catch (e) {
          // User might not have access
        }
      } catch (e) {
        console.error('Error loading lesson:', e)
      } finally {
        setLoading(false)
      }
    }
    loadLesson()
    setOutput('')
    setActiveTab('content')
    setQuizAnswers({})
    setQuizResult(null)
    setShowSolution(false)
    setSubmittingExercise({})
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
    if (quizResult) return
    setQuizAnswers(prev => ({ ...prev, [questionIndex]: answerIndex }))
  }

  const handleSubmitQuiz = async () => {
    if (Object.keys(quizAnswers).length < quizQuestions.length) return
    setSubmittingQuiz(true)
    try {
      const answers = quizQuestions.map((_, i) => quizAnswers[i])
      const result = await submitQuiz(parseInt(lessonId), answers)
      setQuizResult(result)
      // Refresh quiz status
      const status = await getQuizStatus(lessonId)
      setQuizStatus(status)
    } catch (e) {
      console.error('Error submitting quiz:', e)
      alert(e.message)
    } finally {
      setSubmittingQuiz(false)
    }
  }

  const resetQuiz = () => {
    setQuizAnswers({})
    setQuizResult(null)
  }

  const handleSubmitExercise = async (exerciseIndex) => {
    const code = exerciseCodes[exerciseIndex] || ''
    if (!code.trim()) return
    
    setSubmittingExercise(prev => ({ ...prev, [exerciseIndex]: true }))
    try {
      const result = await submitExercise(parseInt(lessonId), exerciseIndex, code)
      setExerciseResults(prev => ({ ...prev, [exerciseIndex]: result }))
      // Refresh exercise status
      const status = await getExerciseStatus(lessonId)
      setExerciseStatus(status)
    } catch (e) {
      console.error('Error submitting exercise:', e)
      setExerciseResults(prev => ({ ...prev, [exerciseIndex]: { passed: false, error: e.message } }))
    } finally {
      setSubmittingExercise(prev => ({ ...prev, [exerciseIndex]: false }))
    }
  }

  const updateExerciseCode = (exerciseIndex, code) => {
    setExerciseCodes(prev => ({ ...prev, [exerciseIndex]: code }))
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
      const result = await executeCode(code, parseInt(lessonId), null)
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
        
        {(exerciseStatus?.completed || quizStatus?.passed) && (
          <span className="flex items-center text-green-600">
            <CheckCircle size={20} className="mr-2" />
            Napredak zabilježen
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
        <div className="space-y-6">
          {/* Exercise Status Banner */}
          {exerciseStatus?.completed && (
            <div className="bg-green-50 border border-green-200 rounded-xl p-4 flex items-center gap-3">
              <Trophy className="w-6 h-6 text-green-600" />
              <span className="text-green-700 font-medium">Sve vježbe uspješno završene!</span>
            </div>
          )}

          <h3 className="text-xl font-semibold flex items-center">
            <Lightbulb className="mr-2 text-yellow-500" />
            Vježbe ({exercises.length})
          </h3>

          {exercises.length > 0 ? (
            <div className="space-y-8">
              {exercises.map((ex, i) => {
                const exCode = exerciseCodes[i] || ''
                const exResult = exerciseResults[i]
                const isSubmitting = submittingExercise[i]
                
                return (
                  <div key={i} className="bg-white rounded-xl shadow-sm overflow-hidden border border-gray-200">
                    {/* Exercise Header */}
                    <div className="bg-gradient-to-r from-blue-600 to-blue-700 text-white p-4">
                      <div className="flex items-center justify-between">
                        <h4 className="font-semibold text-lg flex items-center gap-2">
                          <span className="w-8 h-8 bg-white/20 rounded-lg flex items-center justify-center">
                            {ex.number}
                          </span>
                          {ex.title}
                        </h4>
                        {exResult?.passed && (
                          <span className="bg-green-500 text-white px-3 py-1 rounded-full text-sm flex items-center gap-1">
                            <CheckCircle size={14} /> Riješeno
                          </span>
                        )}
                      </div>
                    </div>
                    
                    {/* Exercise Description */}
                    <div className="p-4 bg-blue-50 border-b border-blue-100">
                      <p className="text-gray-700">{ex.description}</p>
                    </div>
                    
                    {/* Editor and Result */}
                    <div className="grid lg:grid-cols-2 gap-0">
                      {/* Code Editor */}
                      <div className="bg-gray-900">
                        <div className="flex items-center justify-between px-4 py-2 bg-gray-800 border-b border-gray-700">
                          <span className="text-gray-400 text-sm">Tvoje Rješenje</span>
                          <button
                            onClick={() => handleSubmitExercise(i)}
                            disabled={isSubmitting || !exCode.trim()}
                            className="flex items-center bg-green-600 text-white px-3 py-1.5 rounded-lg text-sm hover:bg-green-700 disabled:opacity-50 transition-colors"
                          >
                            {isSubmitting ? (
                              <Loader2 size={14} className="mr-1.5 animate-spin" />
                            ) : (
                              <Send size={14} className="mr-1.5" />
                            )}
                            {isSubmitting ? 'Testiram...' : 'Predaj'}
                          </button>
                        </div>
                        <textarea
                          value={exCode}
                          onChange={(e) => updateExerciseCode(i, e.target.value)}
                          className="w-full h-48 bg-gray-900 text-gray-100 font-mono text-sm p-4 resize-none focus:outline-none"
                          placeholder={`# Vježba ${ex.number}: Napiši rješenje ovdje...`}
                          spellCheck={false}
                        />
                      </div>
                      
                      {/* Result Panel */}
                      <div className="bg-gray-50 border-l border-gray-200">
                        <div className="px-4 py-2 bg-gray-100 border-b flex items-center justify-between">
                          <span className="text-gray-600 text-sm font-medium">Rezultat</span>
                          {exResult && (
                            <span className={`text-xs font-medium px-2 py-1 rounded ${
                              exResult.passed ? 'bg-green-100 text-green-700' : 'bg-red-100 text-red-700'
                            }`}>
                              {exResult.passed ? '✓ Tačno!' : '✗ Netačno'}
                            </span>
                          )}
                        </div>
                        <div className="p-4 h-48 overflow-auto">
                          {exResult ? (
                            <div className="space-y-3">
                              {exResult.passed ? (
                                <div className="flex items-center gap-2 text-green-600">
                                  <CheckCircle size={18} />
                                  <span className="font-medium text-sm">Bravo! Rješenje je tačno!</span>
                                </div>
                              ) : (
                                <div className="flex items-center gap-2 text-red-600">
                                  <AlertCircle size={18} />
                                  <span className="font-medium text-sm">Pokušaj ponovo!</span>
                                </div>
                              )}
                              {exResult.output && (
                                <div>
                                  <span className="text-xs text-gray-500">Output:</span>
                                  <pre className="mt-1 text-xs font-mono bg-white p-2 rounded border">{exResult.output}</pre>
                                </div>
                              )}
                              {exResult.error && (
                                <div className="text-red-600 text-xs">
                                  <span className="font-medium">Greška:</span> {exResult.error}
                                </div>
                              )}
                            </div>
                          ) : (
                            <p className="text-gray-400 text-sm">Predaj rješenje da vidiš rezultat...</p>
                          )}
                        </div>
                      </div>
                    </div>
                  </div>
                )
              })}
            </div>
          ) : (
            <div className="bg-white rounded-xl p-6 shadow-sm">
              <p className="text-gray-500">Nema vježbi za ovu lekciju.</p>
            </div>
          )}

          {/* Show Solution Toggle */}
          {lesson.exercise_solution && (
            <div className="bg-white rounded-xl p-6 shadow-sm">
              <button
                onClick={() => setShowSolution(!showSolution)}
                className="btn-secondary"
              >
                {showSolution ? 'Sakrij Rješenja' : 'Prikaži Rješenja'}
              </button>
              {showSolution && (
                <div className="mt-4">
                  <SyntaxHighlighter style={oneDark} language="python" customStyle={{ borderRadius: '0.75rem' }}>
                    {lesson.exercise_solution}
                  </SyntaxHighlighter>
                </div>
              )}
            </div>
          )}
        </div>
      )}

      {/* Quiz Tab */}
      {activeTab === 'quiz' && (
        <div className="bg-white rounded-xl p-6 shadow-sm">
          <div className="flex items-center justify-between mb-6">
            <h3 className="text-xl font-semibold flex items-center">
              <HelpCircle className="mr-2 text-purple-500" />
              Kviz - Testiraj svoje znanje
            </h3>
            <div className="flex items-center gap-3">
              <span className="text-sm text-gray-500">Potrebno za prolaz: <strong>70%</strong></span>
              {quizStatus?.passed && (
                <span className="bg-green-100 text-green-700 text-sm px-3 py-1 rounded-full flex items-center gap-1">
                  <Trophy size={14} /> Položeno ({quizStatus.best_score?.toFixed(0)}%)
                </span>
              )}
            </div>
          </div>
          
          {quizQuestions.length > 0 ? (
            <>
              {/* Quiz Result Banner */}
              {quizResult && (
                <div className={`mb-6 p-4 rounded-xl ${
                  quizResult.passed 
                    ? 'bg-green-50 border border-green-200' 
                    : 'bg-red-50 border border-red-200'
                }`}>
                  <div className="flex items-center justify-between">
                    <div className="flex items-center gap-3">
                      {quizResult.passed ? (
                        <Trophy className="w-8 h-8 text-green-600" />
                      ) : (
                        <AlertCircle className="w-8 h-8 text-red-600" />
                      )}
                      <div>
                        <span className="font-semibold text-lg">
                          Rezultat: {quizResult.correct_count}/{quizResult.total_count}
                        </span>
                        <span className={`ml-3 font-bold ${quizResult.passed ? 'text-green-600' : 'text-red-600'}`}>
                          ({quizResult.score.toFixed(0)}%)
                        </span>
                      </div>
                    </div>
                    <span className={`font-medium ${quizResult.passed ? 'text-green-600' : 'text-red-600'}`}>
                      {quizResult.passed ? 'Čestitamo! Položili ste kviz! 🎉' : 'Niste položili. Potrebno je 70%.'}
                    </span>
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
                        const showResult = quizResult !== null
                        
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
                            disabled={quizResult !== null}
                            className={`flex items-center gap-3 p-3 rounded-lg border text-left transition-all ${bgClass} ${!quizResult && 'cursor-pointer'}`}
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
                {!quizResult ? (
                  <button
                    onClick={handleSubmitQuiz}
                    disabled={submittingQuiz || Object.keys(quizAnswers).length < quizQuestions.length}
                    className="btn-primary disabled:opacity-50 disabled:cursor-not-allowed"
                  >
                    {submittingQuiz ? (
                      <Loader2 size={18} className="mr-2 inline animate-spin" />
                    ) : (
                      <Send size={18} className="mr-2 inline" />
                    )}
                    {submittingQuiz ? 'Provjeravam...' : 'Predaj Kviz'}
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

        <div className="flex gap-3 items-center">
          {/* Progress indicators */}
          {exerciseStatus?.completed && (
            <span className="text-green-600 text-sm flex items-center gap-1">
              <CheckCircle size={16} /> Vježba
            </span>
          )}
          {quizStatus?.passed && (
            <span className="text-green-600 text-sm flex items-center gap-1">
              <CheckCircle size={16} /> Kviz
            </span>
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
