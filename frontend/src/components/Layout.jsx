import { Link, useLocation } from 'react-router-dom'
import { BookOpen, Home, BarChart3, Menu, X } from 'lucide-react'
import { useState } from 'react'

export default function Layout({ children }) {
  const location = useLocation()
  const [mobileMenuOpen, setMobileMenuOpen] = useState(false)

  const navItems = [
    { path: '/', icon: Home, label: 'Početna' },
    { path: '/modules', icon: BookOpen, label: 'Moduli' },
    { path: '/progress', icon: BarChart3, label: 'Napredak' },
  ]

  const isActive = (path) => location.pathname === path

  return (
    <div className="min-h-screen flex flex-col">
      {/* Header */}
      <header className="bg-gradient-to-r from-python-blue to-blue-700 text-white shadow-lg">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex items-center justify-between h-16">
            {/* Logo */}
            <Link to="/" className="flex items-center space-x-3">
              <img src="/python.svg" alt="Python" className="h-10 w-10" />
              <div>
                <h1 className="text-xl font-bold">Python Learning</h1>
                <p className="text-xs text-blue-200">40 časova • 7 modula</p>
              </div>
            </Link>

            {/* Desktop Navigation */}
            <nav className="hidden md:flex space-x-1">
              {navItems.map(({ path, icon: Icon, label }) => (
                <Link
                  key={path}
                  to={path}
                  className={`flex items-center space-x-2 px-4 py-2 rounded-lg transition-colors ${
                    isActive(path)
                      ? 'bg-white/20 text-white'
                      : 'text-blue-100 hover:bg-white/10'
                  }`}
                >
                  <Icon size={18} />
                  <span>{label}</span>
                </Link>
              ))}
            </nav>

            {/* Mobile menu button */}
            <button
              className="md:hidden p-2"
              onClick={() => setMobileMenuOpen(!mobileMenuOpen)}
            >
              {mobileMenuOpen ? <X size={24} /> : <Menu size={24} />}
            </button>
          </div>
        </div>

        {/* Mobile Navigation */}
        {mobileMenuOpen && (
          <nav className="md:hidden border-t border-white/20 py-2">
            {navItems.map(({ path, icon: Icon, label }) => (
              <Link
                key={path}
                to={path}
                onClick={() => setMobileMenuOpen(false)}
                className={`flex items-center space-x-3 px-6 py-3 ${
                  isActive(path) ? 'bg-white/20' : 'hover:bg-white/10'
                }`}
              >
                <Icon size={20} />
                <span>{label}</span>
              </Link>
            ))}
          </nav>
        )}
      </header>

      {/* Main Content */}
      <main className="flex-1">
        {children}
      </main>

      {/* Footer */}
      <footer className="bg-gray-800 text-gray-400 py-6">
        <div className="max-w-7xl mx-auto px-4 text-center">
          <p>Python Learning Platform • IT Profesionalci</p>
          <p className="text-sm mt-1">DIO 1: Osnove i Skripting (18h) • DIO 2: Struktura i Napredne Tehnike (22h)</p>
        </div>
      </footer>
    </div>
  )
}
