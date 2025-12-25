import { Link } from 'react-router-dom'
import { BookOpen, Code, Database, Globe, Zap, Clock, CheckCircle } from 'lucide-react'

const curriculum = [
  {
    part: 1,
    title: 'DIO 1: Početni Nivo',
    hours: 20,
    color: 'blue',
    modules: [
      { num: 1, title: 'Python Osnove', hours: 5, icon: Code },
      { num: 2, title: 'Strukture Podataka', hours: 5, icon: Database },
      { num: 3, title: 'Kontrola Toka i Petlje', hours: 5, icon: Zap },
      { num: 4, title: 'Funkcije', hours: 5, icon: BookOpen },
    ]
  },
  {
    part: 2,
    title: 'DIO 2: Srednji Nivo',
    hours: 24,
    color: 'green',
    modules: [
      { num: 5, title: 'OOP Osnove', hours: 6, icon: Code },
      { num: 6, title: 'Rad sa Fajlovima', hours: 6, icon: BookOpen },
      { num: 7, title: 'Moduli i Paketi', hours: 6, icon: Database },
      { num: 8, title: 'Error Handling', hours: 6, icon: Zap },
    ]
  },
  {
    part: 3,
    title: 'DIO 3: Napredni Nivo',
    hours: 28,
    color: 'purple',
    modules: [
      { num: 9, title: 'Napredni OOP', hours: 7, icon: Code },
      { num: 10, title: 'Generatori i Iteratori', hours: 7, icon: Zap },
      { num: 11, title: 'Konkurentnost', hours: 7, icon: Globe },
      { num: 12, title: 'Testiranje i Best Practices', hours: 7, icon: CheckCircle },
    ]
  }
]

export default function Home() {
  return (
    <div>
      {/* Hero Section */}
      <section className="bg-gradient-to-br from-python-blue via-blue-600 to-blue-800 text-white py-16">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center">
            <h1 className="text-4xl md:text-5xl font-bold mb-4">
              Python za IT Profesionalce
            </h1>
            <p className="text-xl text-blue-100 mb-8 max-w-2xl mx-auto">
              Naučite Python kroz praktične primjere prilagođene sistem administratorima, 
              DevOps inženjerima i IT support stručnjacima.
            </p>
            <div className="flex flex-wrap justify-center gap-4">
              <Link to="/modules" className="bg-python-yellow text-gray-900 px-8 py-3 rounded-lg font-bold hover:bg-yellow-300 transition-colors">
                Započni Učenje
              </Link>
              <Link to="/progress" className="bg-white/20 text-white px-8 py-3 rounded-lg font-medium hover:bg-white/30 transition-colors">
                Moj Napredak
              </Link>
            </div>
          </div>

          {/* Stats */}
          <div className="mt-12 grid grid-cols-2 md:grid-cols-4 gap-4 max-w-3xl mx-auto">
            {[
              { value: '72', label: 'Časova' },
              { value: '12', label: 'Modula' },
              { value: '54', label: 'Lekcija' },
              { value: '∞', label: 'Vježbi' },
            ].map((stat, i) => (
              <div key={i} className="bg-white/10 rounded-lg p-4 text-center">
                <div className="text-3xl font-bold text-python-yellow">{stat.value}</div>
                <div className="text-blue-200">{stat.label}</div>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Curriculum Overview */}
      <section className="py-16 bg-gray-50">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <h2 className="text-3xl font-bold text-center mb-12">Pregled Silabusa</h2>
          
          <div className="grid md:grid-cols-3 gap-6">
            {curriculum.map((part) => {
              const colors = {
                blue: { bg: 'bg-blue-600', light: 'bg-blue-100 text-blue-600' },
                green: { bg: 'bg-green-600', light: 'bg-green-100 text-green-600' },
                purple: { bg: 'bg-purple-600', light: 'bg-purple-100 text-purple-600' }
              }
              const c = colors[part.color]
              return (
              <div key={part.part} className="bg-white rounded-xl shadow-lg overflow-hidden">
                <div className={`p-4 ${c.bg} text-white`}>
                  <div className="flex items-center justify-between">
                    <h3 className="text-lg font-bold">{part.title}</h3>
                    <span className="flex items-center text-sm">
                      <Clock size={16} className="mr-1" />
                      {part.hours}h
                    </span>
                  </div>
                </div>
                <div className="p-3">
                  {part.modules.map((mod) => (
                    <Link
                      key={mod.num}
                      to={`/modules/${mod.num}`}
                      className="flex items-center p-2 hover:bg-gray-50 rounded-lg transition-colors group"
                    >
                      <div className={`w-9 h-9 rounded-lg flex items-center justify-center mr-2 ${c.light}`}>
                        <mod.icon size={18} />
                      </div>
                      <div className="flex-1 min-w-0">
                        <div className="font-medium text-sm group-hover:text-python-blue truncate">
                          {mod.num}. {mod.title}
                        </div>
                        <div className="text-xs text-gray-500">{mod.hours}h</div>
                      </div>
                    </Link>
                  ))}
                </div>
              </div>
            )})}
          </div>
        </div>
      </section>

      {/* Features */}
      <section className="py-16">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <h2 className="text-3xl font-bold text-center mb-12">Zašto Ovaj Kurs?</h2>
          
          <div className="grid md:grid-cols-3 gap-8">
            {[
              {
                icon: Code,
                title: 'Interaktivni Code Editor',
                description: 'Pišite i izvršavajte Python kod direktno u browseru. Instant feedback za svaku vježbu.'
              },
              {
                icon: CheckCircle,
                title: 'Praćenje Napretka',
                description: 'Pratite svoj napredak kroz module i lekcije. Nikad ne gubite gdje ste stali.'
              },
              {
                icon: Zap,
                title: 'Fokus na Praktično',
                description: 'Primjeri iz stvarnog svijeta IT-a: automatizacija, API-ji, baze podataka, DevOps.'
              }
            ].map((feature, i) => (
              <div key={i} className="text-center p-6">
                <div className="w-16 h-16 bg-python-blue/10 rounded-xl flex items-center justify-center mx-auto mb-4">
                  <feature.icon size={32} className="text-python-blue" />
                </div>
                <h3 className="text-xl font-semibold mb-2">{feature.title}</h3>
                <p className="text-gray-600">{feature.description}</p>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* CTA */}
      <section className="py-16 bg-gray-900 text-white">
        <div className="max-w-4xl mx-auto px-4 text-center">
          <h2 className="text-3xl font-bold mb-4">Spreman za Početak?</h2>
          <p className="text-gray-400 mb-8">
            Započnite sa Modulom 1 i naučite Python kroz praktične primjere.
          </p>
          <Link 
            to="/modules/1" 
            className="inline-flex items-center bg-python-yellow text-gray-900 px-8 py-3 rounded-lg font-bold hover:bg-yellow-300 transition-colors"
          >
            <BookOpen className="mr-2" size={20} />
            Kreni sa Modulom 1
          </Link>
        </div>
      </section>
    </div>
  )
}
