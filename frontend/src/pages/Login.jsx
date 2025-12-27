import { useState } from 'react'
import { useNavigate, Link } from 'react-router-dom'
import { User, Lock, LogIn, UserPlus } from 'lucide-react'
import { login, register } from '../api'

export default function Login({ onLogin }) {
  const [isRegister, setIsRegister] = useState(false)
  const [username, setUsername] = useState('')
  const [password, setPassword] = useState('')
  const [error, setError] = useState('')
  const [loading, setLoading] = useState(false)
  const navigate = useNavigate()

  const handleSubmit = async (e) => {
    e.preventDefault()
    setError('')
    setLoading(true)

    try {
      if (isRegister) {
        if (password.length < 4) {
          throw new Error('Lozinka mora imati najmanje 4 karaktera')
        }
        await register(username, password)
      } else {
        await login(username, password)
      }
      onLogin()
      navigate('/')
    } catch (err) {
      setError(err.message)
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-900 via-blue-900 to-slate-900 flex items-center justify-center p-4">
      <div className="w-full max-w-md">
        <div className="text-center mb-8">
          <h1 className="text-4xl font-bold text-white mb-2">🐍 Python Learning</h1>
          <p className="text-blue-200">Platforma za učenje Pythona</p>
        </div>

        <div className="bg-slate-800 rounded-2xl shadow-2xl p-8 border border-slate-700">
          <div className="flex mb-6 bg-slate-700 rounded-lg p-1">
            <button
              className={`flex-1 py-2 px-4 rounded-md transition-all flex items-center justify-center gap-2 ${
                !isRegister ? 'bg-blue-600 text-white' : 'text-slate-300 hover:text-white'
              }`}
              onClick={() => setIsRegister(false)}
            >
              <LogIn className="w-4 h-4" />
              Prijava
            </button>
            <button
              className={`flex-1 py-2 px-4 rounded-md transition-all flex items-center justify-center gap-2 ${
                isRegister ? 'bg-green-600 text-white' : 'text-slate-300 hover:text-white'
              }`}
              onClick={() => setIsRegister(true)}
            >
              <UserPlus className="w-4 h-4" />
              Registracija
            </button>
          </div>

          <form onSubmit={handleSubmit} className="space-y-4">
            <div>
              <label className="block text-sm font-medium text-slate-300 mb-2">
                Korisničko ime
              </label>
              <div className="relative">
                <User className="absolute left-3 top-1/2 -translate-y-1/2 w-5 h-5 text-slate-400" />
                <input
                  type="text"
                  value={username}
                  onChange={(e) => setUsername(e.target.value)}
                  className="w-full pl-10 pr-4 py-3 bg-slate-700 border border-slate-600 rounded-lg text-white placeholder-slate-400 focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                  placeholder="Unesite korisničko ime"
                  required
                />
              </div>
            </div>

            <div>
              <label className="block text-sm font-medium text-slate-300 mb-2">
                Lozinka
              </label>
              <div className="relative">
                <Lock className="absolute left-3 top-1/2 -translate-y-1/2 w-5 h-5 text-slate-400" />
                <input
                  type="password"
                  value={password}
                  onChange={(e) => setPassword(e.target.value)}
                  className="w-full pl-10 pr-4 py-3 bg-slate-700 border border-slate-600 rounded-lg text-white placeholder-slate-400 focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                  placeholder="Unesite lozinku"
                  required
                />
              </div>
            </div>

            {error && (
              <div className="bg-red-500/20 border border-red-500 text-red-300 px-4 py-3 rounded-lg text-sm">
                {error}
              </div>
            )}

            <button
              type="submit"
              disabled={loading}
              className={`w-full py-3 rounded-lg font-semibold text-white transition-all ${
                isRegister
                  ? 'bg-green-600 hover:bg-green-700'
                  : 'bg-blue-600 hover:bg-blue-700'
              } ${loading ? 'opacity-50 cursor-not-allowed' : ''}`}
            >
              {loading ? 'Učitavanje...' : isRegister ? 'Registruj se' : 'Prijavi se'}
            </button>
          </form>

          {!isRegister && (
            <p className="mt-4 text-center text-slate-400 text-sm">
              Admin pristup: <span className="text-blue-400">admin / admin123</span>
            </p>
          )}
        </div>
      </div>
    </div>
  )
}
