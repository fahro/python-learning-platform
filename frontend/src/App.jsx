import { useState, useEffect } from 'react'
import { Routes, Route, Navigate } from 'react-router-dom'
import Layout from './components/Layout'
import Home from './pages/Home'
import ModuleList from './pages/ModuleList'
import ModuleDetail from './pages/ModuleDetail'
import LessonView from './pages/LessonView'
import Progress from './pages/Progress'
import Login from './pages/Login'
import AdminDashboard from './pages/AdminDashboard'
import { checkAuth, logout } from './api'

function App() {
  const [user, setUser] = useState(null)
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    checkAuthStatus()
  }, [])

  const checkAuthStatus = async () => {
    try {
      const data = await checkAuth()
      if (data.authenticated) {
        setUser(data.user)
      }
    } catch (err) {
      console.error(err)
    } finally {
      setLoading(false)
    }
  }

  const handleLogin = () => {
    checkAuthStatus()
  }

  const handleLogout = async () => {
    await logout()
    setUser(null)
  }

  if (loading) {
    return (
      <div className="min-h-screen bg-slate-900 flex items-center justify-center">
        <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-blue-500"></div>
      </div>
    )
  }

  if (!user) {
    return <Login onLogin={handleLogin} />
  }

  return (
    <Layout user={user} onLogout={handleLogout}>
      <Routes>
        <Route path="/" element={<Home user={user} />} />
        <Route path="/modules" element={<ModuleList user={user} />} />
        <Route path="/modules/:moduleId" element={<ModuleDetail user={user} />} />
        <Route path="/lessons/:lessonId" element={<LessonView user={user} />} />
        <Route path="/progress" element={<Progress user={user} />} />
        <Route path="/admin" element={<AdminDashboard user={user} />} />
        <Route path="/login" element={<Navigate to="/" />} />
      </Routes>
    </Layout>
  )
}

export default App
