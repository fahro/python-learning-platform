import { useState, useEffect } from 'react'
import { useParams, Link } from 'react-router-dom'
import { Clock, CheckCircle, Circle, ArrowLeft, Play, Loader2 } from 'lucide-react'
import { fetchModule, fetchLessonsByModule, fetchUserProgress, getUserId } from '../api'

export default function ModuleDetail() {
  const { moduleId } = useParams()
  const [module, setModule] = useState(null)
  const [lessons, setLessons] = useState([])
  const [completedLessons, setCompletedLessons] = useState(new Set())
  const [loading, setLoading] = useState(true)
  const userId = getUserId()

  useEffect(() => {
    async function loadData() {
      try {
        const mod = await fetchModule(moduleId)
        setModule(mod)
        
        const lessonList = await fetchLessonsByModule(moduleId)
        setLessons(lessonList)
        
        const progress = await fetchUserProgress(userId)
        const completed = new Set(
          progress.filter(p => p.completed).map(p => p.lesson_id)
        )
        setCompletedLessons(completed)
      } catch (e) {
        console.error('Error loading module:', e)
      } finally {
        setLoading(false)
      }
    }
    loadData()
  }, [moduleId, userId])

  if (loading) {
    return (
      <div className="flex items-center justify-center min-h-[400px]">
        <Loader2 className="animate-spin text-python-blue" size={40} />
      </div>
    )
  }

  if (!module) {
    return (
      <div className="max-w-4xl mx-auto px-4 py-8 text-center">
        <h1 className="text-2xl font-bold text-gray-900">Modul nije pronađen</h1>
        <Link to="/modules" className="text-python-blue hover:underline mt-4 inline-block">
          ← Nazad na module
        </Link>
      </div>
    )
  }

  const completedCount = lessons.filter(l => completedLessons.has(l.id)).length
  const progressPercent = lessons.length > 0 ? Math.round((completedCount / lessons.length) * 100) : 0

  return (
    <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
      {/* Back link */}
      <Link to="/modules" className="inline-flex items-center text-gray-600 hover:text-python-blue mb-6">
        <ArrowLeft size={20} className="mr-2" />
        Svi moduli
      </Link>

      {/* Module Header */}
      <div className={`rounded-xl p-6 mb-8 ${module.part === 1 ? 'bg-blue-600' : 'bg-green-600'} text-white`}>
        <div className="flex items-center mb-2">
          <span className="bg-white/20 px-3 py-1 rounded-full text-sm">
            Modul {module.number}
          </span>
          <span className="ml-3 flex items-center">
            <Clock size={16} className="mr-1" />
            {module.duration_hours} časa
          </span>
        </div>
        <h1 className="text-2xl md:text-3xl font-bold mb-2">{module.title}</h1>
        <p className="text-white/80">{module.description}</p>
        
        {/* Progress */}
        <div className="mt-6">
          <div className="flex justify-between text-sm mb-2">
            <span>Napredak</span>
            <span>{completedCount} / {lessons.length} lekcija ({progressPercent}%)</span>
          </div>
          <div className="h-3 bg-white/20 rounded-full overflow-hidden">
            <div 
              className="h-full bg-white rounded-full transition-all"
              style={{ width: `${progressPercent}%` }}
            />
          </div>
        </div>
      </div>

      {/* Lessons List */}
      <h2 className="text-xl font-semibold mb-4">Lekcije</h2>
      <div className="space-y-3">
        {lessons.map((lesson, index) => {
          const isCompleted = completedLessons.has(lesson.id)
          
          return (
            <Link
              key={lesson.id}
              to={`/lessons/${lesson.id}`}
              className={`block p-4 rounded-lg border transition-all hover:shadow-md ${
                isCompleted 
                  ? 'bg-green-50 border-green-200' 
                  : 'bg-white border-gray-200 hover:border-python-blue'
              }`}
            >
              <div className="flex items-center">
                <div className={`w-10 h-10 rounded-full flex items-center justify-center mr-4 ${
                  isCompleted ? 'bg-green-500 text-white' : 'bg-gray-100 text-gray-500'
                }`}>
                  {isCompleted ? <CheckCircle size={20} /> : <span>{index + 1}</span>}
                </div>
                
                <div className="flex-1">
                  <h3 className="font-medium">{lesson.title}</h3>
                  <div className="text-sm text-gray-500 flex items-center mt-1">
                    <Clock size={14} className="mr-1" />
                    {lesson.duration_hours} čas
                  </div>
                </div>
                
                <div className={`px-3 py-1 rounded-full text-sm ${
                  isCompleted 
                    ? 'bg-green-100 text-green-700' 
                    : 'bg-gray-100 text-gray-600'
                }`}>
                  {isCompleted ? 'Završeno' : 'Započni'}
                </div>
              </div>
            </Link>
          )
        })}
      </div>

      {/* Start Button */}
      {lessons.length > 0 && (
        <div className="mt-8 text-center">
          <Link
            to={`/lessons/${lessons.find(l => !completedLessons.has(l.id))?.id || lessons[0].id}`}
            className="inline-flex items-center btn-primary px-8 py-3"
          >
            <Play size={20} className="mr-2" />
            {completedCount === 0 ? 'Započni Modul' : completedCount === lessons.length ? 'Ponovi' : 'Nastavi'}
          </Link>
        </div>
      )}
    </div>
  )
}
