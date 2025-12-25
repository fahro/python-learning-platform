import { useState, useEffect } from 'react'
import { Link } from 'react-router-dom'
import { Clock, BookOpen, CheckCircle, Trophy, Loader2, BarChart3 } from 'lucide-react'
import { fetchModules, fetchUserStats, fetchModuleProgress, getUserId } from '../api'

export default function Progress() {
  const [modules, setModules] = useState([])
  const [stats, setStats] = useState(null)
  const [moduleProgress, setModuleProgress] = useState({})
  const [loading, setLoading] = useState(true)
  const userId = getUserId()

  useEffect(() => {
    async function loadData() {
      try {
        const [mods, userStats] = await Promise.all([
          fetchModules(),
          fetchUserStats(userId)
        ])
        
        setModules(mods)
        setStats(userStats)
        
        const progress = {}
        for (const mod of mods) {
          try {
            const p = await fetchModuleProgress(userId, mod.id)
            progress[mod.id] = p
          } catch {
            progress[mod.id] = { progress_percentage: 0, completed_lessons: 0, total_lessons: 0 }
          }
        }
        setModuleProgress(progress)
      } catch (e) {
        console.error('Error loading progress:', e)
      } finally {
        setLoading(false)
      }
    }
    loadData()
  }, [userId])

  if (loading) {
    return (
      <div className="flex items-center justify-center min-h-[400px]">
        <Loader2 className="animate-spin text-python-blue" size={40} />
      </div>
    )
  }

  return (
    <div className="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
      <h1 className="text-3xl font-bold mb-2">Moj Napredak</h1>
      <p className="text-gray-600 mb-8">Pratite svoj put kroz Python kurs</p>

      {/* Stats Cards */}
      {stats && (
        <div className="grid grid-cols-2 md:grid-cols-4 gap-4 mb-10">
          <div className="bg-white rounded-xl p-5 shadow-sm border">
            <div className="flex items-center justify-between mb-2">
              <span className="text-gray-500 text-sm">Ukupno lekcija</span>
              <BookOpen size={20} className="text-blue-500" />
            </div>
            <div className="text-2xl font-bold">{stats.completed_lessons} / {stats.total_lessons}</div>
          </div>
          
          <div className="bg-white rounded-xl p-5 shadow-sm border">
            <div className="flex items-center justify-between mb-2">
              <span className="text-gray-500 text-sm">Napredak</span>
              <BarChart3 size={20} className="text-green-500" />
            </div>
            <div className="text-2xl font-bold">{stats.progress_percentage}%</div>
          </div>
          
          <div className="bg-white rounded-xl p-5 shadow-sm border">
            <div className="flex items-center justify-between mb-2">
              <span className="text-gray-500 text-sm">Sati učenja</span>
              <Clock size={20} className="text-purple-500" />
            </div>
            <div className="text-2xl font-bold">{stats.completed_hours} / {stats.total_hours}h</div>
          </div>
          
          <div className="bg-white rounded-xl p-5 shadow-sm border">
            <div className="flex items-center justify-between mb-2">
              <span className="text-gray-500 text-sm">Status</span>
              <Trophy size={20} className="text-yellow-500" />
            </div>
            <div className="text-2xl font-bold">
              {stats.progress_percentage === 100 ? '🏆' : stats.progress_percentage > 50 ? '🚀' : '📚'}
            </div>
          </div>
        </div>
      )}

      {/* Overall Progress Bar */}
      {stats && (
        <div className="bg-white rounded-xl p-6 shadow-sm border mb-10">
          <h2 className="text-lg font-semibold mb-4">Ukupni napredak</h2>
          <div className="h-4 bg-gray-100 rounded-full overflow-hidden">
            <div 
              className="h-full bg-gradient-to-r from-python-blue to-blue-400 rounded-full transition-all duration-500"
              style={{ width: `${stats.progress_percentage}%` }}
            />
          </div>
          <div className="flex justify-between mt-2 text-sm text-gray-500">
            <span>0%</span>
            <span className="font-medium text-python-blue">{stats.progress_percentage}% završeno</span>
            <span>100%</span>
          </div>
        </div>
      )}

      {/* Module Progress */}
      <h2 className="text-xl font-semibold mb-4">Napredak po modulima</h2>
      <div className="space-y-4">
        {modules.map(mod => {
          const prog = moduleProgress[mod.id] || { progress_percentage: 0, completed_lessons: 0, total_lessons: mod.lesson_count }
          const isComplete = prog.progress_percentage === 100
          
          return (
            <Link
              key={mod.id}
              to={`/modules/${mod.id}`}
              className={`block bg-white rounded-xl p-5 shadow-sm border hover:shadow-md transition-shadow ${
                isComplete ? 'border-green-200 bg-green-50/50' : ''
              }`}
            >
              <div className="flex items-center justify-between mb-3">
                <div className="flex items-center">
                  <div className={`w-10 h-10 rounded-lg flex items-center justify-center mr-3 ${
                    isComplete 
                      ? 'bg-green-100 text-green-600' 
                      : mod.part === 1 
                        ? 'bg-blue-100 text-blue-600' 
                        : 'bg-green-100 text-green-600'
                  }`}>
                    {isComplete ? <CheckCircle size={20} /> : mod.number}
                  </div>
                  <div>
                    <h3 className="font-medium">{mod.title}</h3>
                    <div className="text-sm text-gray-500">
                      {prog.completed_lessons} / {prog.total_lessons} lekcija • {mod.duration_hours}h
                    </div>
                  </div>
                </div>
                <div className={`text-lg font-bold ${
                  isComplete ? 'text-green-600' : 'text-gray-600'
                }`}>
                  {prog.progress_percentage}%
                </div>
              </div>
              
              <div className="h-2 bg-gray-100 rounded-full overflow-hidden">
                <div 
                  className={`h-full rounded-full transition-all ${
                    isComplete 
                      ? 'bg-green-500' 
                      : mod.part === 1 
                        ? 'bg-blue-500' 
                        : 'bg-green-500'
                  }`}
                  style={{ width: `${prog.progress_percentage}%` }}
                />
              </div>
            </Link>
          )
        })}
      </div>

      {/* Motivation Message */}
      {stats && stats.progress_percentage < 100 && (
        <div className="mt-10 bg-gradient-to-r from-python-blue to-blue-600 rounded-xl p-6 text-white text-center">
          <h3 className="text-xl font-bold mb-2">
            {stats.progress_percentage === 0 
              ? 'Spremni za početak?' 
              : stats.progress_percentage < 25 
                ? 'Odličan početak!' 
                : stats.progress_percentage < 50 
                  ? 'Nastavite tako!' 
                  : stats.progress_percentage < 75 
                    ? 'Već ste na pola puta!' 
                    : 'Skoro ste završili!'}
          </h3>
          <p className="text-blue-100 mb-4">
            {stats.total_lessons - stats.completed_lessons} lekcija do kraja kursa
          </p>
          <Link to="/modules" className="inline-block bg-white text-python-blue px-6 py-2 rounded-lg font-medium hover:bg-blue-50">
            Nastavi učenje
          </Link>
        </div>
      )}

      {/* Completed Message */}
      {stats && stats.progress_percentage === 100 && (
        <div className="mt-10 bg-gradient-to-r from-green-500 to-emerald-600 rounded-xl p-8 text-white text-center">
          <Trophy size={48} className="mx-auto mb-4" />
          <h3 className="text-2xl font-bold mb-2">Čestitamo! 🎉</h3>
          <p className="text-green-100">
            Završili ste sve lekcije Python kursa. Sada ste spremni za stvarne projekte!
          </p>
        </div>
      )}
    </div>
  )
}
