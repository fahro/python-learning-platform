import { useState, useEffect } from 'react'
import { Link } from 'react-router-dom'
import { Clock, BookOpen, ChevronRight, Loader2 } from 'lucide-react'
import { fetchModules, fetchModuleProgress, getUserId } from '../api'

export default function ModuleList() {
  const [modules, setModules] = useState([])
  const [loading, setLoading] = useState(true)
  const [progress, setProgress] = useState({})
  const userId = getUserId()

  useEffect(() => {
    async function loadData() {
      try {
        const mods = await fetchModules()
        setModules(mods)
        
        const progressData = {}
        for (const mod of mods) {
          try {
            const p = await fetchModuleProgress(userId, mod.id)
            progressData[mod.id] = p
          } catch (e) {
            progressData[mod.id] = { progress_percentage: 0 }
          }
        }
        setProgress(progressData)
      } catch (e) {
        console.error('Error loading modules:', e)
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

  const part1 = modules.filter(m => m.part === 1)
  const part2 = modules.filter(m => m.part === 2)
  const part3 = modules.filter(m => m.part === 3)

  const getPartColors = (part) => {
    switch(part) {
      case 1: return { bg: 'bg-blue-100', text: 'text-blue-600', bar: 'bg-blue-500' }
      case 2: return { bg: 'bg-green-100', text: 'text-green-600', bar: 'bg-green-500' }
      case 3: return { bg: 'bg-purple-100', text: 'text-purple-600', bar: 'bg-purple-500' }
      default: return { bg: 'bg-gray-100', text: 'text-gray-600', bar: 'bg-gray-500' }
    }
  }

  const ModuleCard = ({ module }) => {
    const prog = progress[module.id] || { progress_percentage: 0 }
    const colors = getPartColors(module.part)
    
    return (
      <Link
        to={`/modules/${module.id}`}
        className="module-card p-6 block group"
      >
        <div className="flex items-start justify-between mb-4">
          <div className={`w-12 h-12 rounded-xl flex items-center justify-center text-xl font-bold ${colors.bg} ${colors.text}`}>
            {module.number}
          </div>
          <ChevronRight className="text-gray-400 group-hover:text-python-blue transition-colors" />
        </div>
        
        <h3 className="text-lg font-semibold mb-2 group-hover:text-python-blue transition-colors">
          {module.title}
        </h3>
        
        <div className="flex items-center text-sm text-gray-500 mb-4">
          <Clock size={16} className="mr-1" />
          <span>{module.duration_hours} časa</span>
          <span className="mx-2">•</span>
          <BookOpen size={16} className="mr-1" />
          <span>{module.lesson_count} lekcija</span>
        </div>
        
        {/* Progress bar */}
        <div className="mt-auto">
          <div className="flex justify-between text-sm mb-1">
            <span className="text-gray-500">Napredak</span>
            <span className="font-medium">{prog.progress_percentage}%</span>
          </div>
          <div className="h-2 bg-gray-100 rounded-full overflow-hidden">
            <div 
              className={`h-full rounded-full transition-all ${colors.bar}`}
              style={{ width: `${prog.progress_percentage}%` }}
            />
          </div>
        </div>
      </Link>
    )
  }

  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
      <h1 className="text-3xl font-bold mb-2">Moduli</h1>
      <p className="text-gray-600 mb-8">Izaberite modul za početak učenja</p>

      {/* Part 1 - Početni */}
      <div className="mb-12">
        <div className="flex items-center mb-6">
          <div className="bg-blue-600 text-white px-4 py-2 rounded-lg font-medium">
            DIO 1: Početni Nivo
          </div>
          <div className="ml-4 text-gray-500">20 sati</div>
        </div>
        <div className="grid md:grid-cols-2 lg:grid-cols-4 gap-6">
          {part1.map(mod => (
            <ModuleCard key={mod.id} module={mod} />
          ))}
        </div>
      </div>

      {/* Part 2 - Srednji */}
      <div className="mb-12">
        <div className="flex items-center mb-6">
          <div className="bg-green-600 text-white px-4 py-2 rounded-lg font-medium">
            DIO 2: Srednji Nivo
          </div>
          <div className="ml-4 text-gray-500">24 sata</div>
        </div>
        <div className="grid md:grid-cols-2 lg:grid-cols-4 gap-6">
          {part2.map(mod => (
            <ModuleCard key={mod.id} module={mod} />
          ))}
        </div>
      </div>

      {/* Part 3 - Napredni */}
      <div>
        <div className="flex items-center mb-6">
          <div className="bg-purple-600 text-white px-4 py-2 rounded-lg font-medium">
            DIO 3: Napredni Nivo
          </div>
          <div className="ml-4 text-gray-500">28 sati</div>
        </div>
        <div className="grid md:grid-cols-2 lg:grid-cols-4 gap-6">
          {part3.map(mod => (
            <ModuleCard key={mod.id} module={mod} />
          ))}
        </div>
      </div>
    </div>
  )
}
