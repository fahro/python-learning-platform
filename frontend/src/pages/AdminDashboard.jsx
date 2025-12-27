import { useState, useEffect } from 'react'
import { useNavigate } from 'react-router-dom'
import { Users, BookOpen, Unlock, Lock, ChevronDown, ChevronUp, CheckCircle, XCircle, Eye } from 'lucide-react'
import { fetchAllUsers, fetchUserProgressAdmin, fetchAllModulesAdmin, unlockModule } from '../api'

export default function AdminDashboard({ user }) {
  const [users, setUsers] = useState([])
  const [modules, setModules] = useState([])
  const [selectedUser, setSelectedUser] = useState(null)
  const [userProgress, setUserProgress] = useState(null)
  const [loading, setLoading] = useState(true)
  const [expandedUser, setExpandedUser] = useState(null)
  const navigate = useNavigate()

  useEffect(() => {
    if (!user?.is_admin) {
      navigate('/')
      return
    }
    loadData()
  }, [user])

  const loadData = async () => {
    try {
      const [usersData, modulesData] = await Promise.all([
        fetchAllUsers(),
        fetchAllModulesAdmin()
      ])
      setUsers(usersData)
      setModules(modulesData)
    } catch (err) {
      console.error(err)
    } finally {
      setLoading(false)
    }
  }

  const loadUserProgress = async (userId) => {
    if (expandedUser === userId) {
      setExpandedUser(null)
      setUserProgress(null)
      return
    }
    try {
      const progress = await fetchUserProgressAdmin(userId)
      setUserProgress(progress)
      setExpandedUser(userId)
    } catch (err) {
      console.error(err)
    }
  }

  const handleUnlockModule = async (userId, moduleId, currentlyUnlocked) => {
    try {
      await unlockModule(userId, moduleId, !currentlyUnlocked)
      // Reload user progress
      const progress = await fetchUserProgressAdmin(userId)
      setUserProgress(progress)
    } catch (err) {
      console.error(err)
    }
  }

  if (loading) {
    return (
      <div className="flex items-center justify-center min-h-screen">
        <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-blue-500"></div>
      </div>
    )
  }

  return (
    <div className="max-w-6xl mx-auto p-6">
      <div className="mb-8">
        <h1 className="text-3xl font-bold text-white flex items-center gap-3">
          <Users className="w-8 h-8 text-blue-400" />
          Admin Dashboard
        </h1>
        <p className="text-slate-400 mt-2">Upravljanje korisnicima i modulima</p>
      </div>

      {/* Stats */}
      <div className="grid grid-cols-1 md:grid-cols-3 gap-4 mb-8">
        <div className="bg-slate-800 rounded-xl p-6 border border-slate-700">
          <div className="text-3xl font-bold text-blue-400">{users.length}</div>
          <div className="text-slate-400">Registrovanih korisnika</div>
        </div>
        <div className="bg-slate-800 rounded-xl p-6 border border-slate-700">
          <div className="text-3xl font-bold text-green-400">{modules.length}</div>
          <div className="text-slate-400">Modula</div>
        </div>
        <div className="bg-slate-800 rounded-xl p-6 border border-slate-700">
          <div className="text-3xl font-bold text-purple-400">70%</div>
          <div className="text-slate-400">Prag za prolaz kviza</div>
        </div>
      </div>

      {/* Users List */}
      <div className="bg-slate-800 rounded-xl border border-slate-700 overflow-hidden">
        <div className="p-4 border-b border-slate-700">
          <h2 className="text-xl font-semibold text-white">Korisnici</h2>
        </div>
        
        {users.length === 0 ? (
          <div className="p-8 text-center text-slate-400">
            Nema registrovanih korisnika
          </div>
        ) : (
          <div className="divide-y divide-slate-700">
            {users.map((u) => (
              <div key={u.id} className="bg-slate-800">
                <div 
                  className="p-4 flex items-center justify-between cursor-pointer hover:bg-slate-700/50 transition-colors"
                  onClick={() => loadUserProgress(u.id)}
                >
                  <div className="flex items-center gap-4">
                    <div className="w-10 h-10 rounded-full bg-blue-600 flex items-center justify-center text-white font-bold">
                      {u.username[0].toUpperCase()}
                    </div>
                    <div>
                      <div className="font-medium text-white">{u.username}</div>
                      <div className="text-sm text-slate-400">
                        Registrovan: {new Date(u.created_at).toLocaleDateString('bs')}
                      </div>
                    </div>
                  </div>
                  <div className="flex items-center gap-2">
                    <button className="p-2 hover:bg-slate-600 rounded-lg transition-colors">
                      {expandedUser === u.id ? (
                        <ChevronUp className="w-5 h-5 text-slate-400" />
                      ) : (
                        <ChevronDown className="w-5 h-5 text-slate-400" />
                      )}
                    </button>
                  </div>
                </div>

                {/* Expanded User Progress */}
                {expandedUser === u.id && userProgress && (
                  <div className="px-4 pb-4 bg-slate-900/50">
                    <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-3 mt-2">
                      {userProgress.map((module) => (
                        <div 
                          key={module.module_id}
                          className={`p-4 rounded-lg border ${
                            module.unlocked 
                              ? 'bg-slate-800 border-green-600/50' 
                              : 'bg-slate-800/50 border-slate-700'
                          }`}
                        >
                          <div className="flex items-center justify-between mb-2">
                            <span className="font-medium text-white">
                              Modul {module.module_number}
                            </span>
                            <button
                              onClick={(e) => {
                                e.stopPropagation()
                                handleUnlockModule(u.id, module.module_id, module.unlocked)
                              }}
                              className={`p-2 rounded-lg transition-colors ${
                                module.unlocked
                                  ? 'bg-green-600 hover:bg-green-700'
                                  : 'bg-slate-600 hover:bg-slate-500'
                              }`}
                            >
                              {module.unlocked ? (
                                <Unlock className="w-4 h-4 text-white" />
                              ) : (
                                <Lock className="w-4 h-4 text-white" />
                              )}
                            </button>
                          </div>
                          <div className="text-sm text-slate-400 mb-2">{module.title}</div>
                          
                          {module.unlocked && (
                            <div className="space-y-1 mt-3 border-t border-slate-700 pt-3">
                              {module.lessons.map((lesson) => (
                                <div 
                                  key={lesson.lesson_id}
                                  className="flex items-center justify-between text-sm"
                                >
                                  <span className="text-slate-300 truncate flex-1">
                                    {lesson.title}
                                  </span>
                                  <div className="flex items-center gap-2 ml-2">
                                    {lesson.exercise_passed ? (
                                      <CheckCircle className="w-4 h-4 text-green-500" />
                                    ) : (
                                      <XCircle className="w-4 h-4 text-slate-600" />
                                    )}
                                    {lesson.quiz_passed ? (
                                      <span className="text-xs bg-green-600 px-1.5 py-0.5 rounded">
                                        {lesson.quiz_score?.toFixed(0)}%
                                      </span>
                                    ) : lesson.quiz_score !== null ? (
                                      <span className="text-xs bg-red-600 px-1.5 py-0.5 rounded">
                                        {lesson.quiz_score?.toFixed(0)}%
                                      </span>
                                    ) : (
                                      <span className="text-xs bg-slate-600 px-1.5 py-0.5 rounded">-</span>
                                    )}
                                  </div>
                                </div>
                              ))}
                            </div>
                          )}
                        </div>
                      ))}
                    </div>
                  </div>
                )}
              </div>
            ))}
          </div>
        )}
      </div>
    </div>
  )
}
