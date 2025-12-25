import { Routes, Route } from 'react-router-dom'
import Layout from './components/Layout'
import Home from './pages/Home'
import ModuleList from './pages/ModuleList'
import ModuleDetail from './pages/ModuleDetail'
import LessonView from './pages/LessonView'
import Progress from './pages/Progress'

function App() {
  return (
    <Layout>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/modules" element={<ModuleList />} />
        <Route path="/modules/:moduleId" element={<ModuleDetail />} />
        <Route path="/lessons/:lessonId" element={<LessonView />} />
        <Route path="/progress" element={<Progress />} />
      </Routes>
    </Layout>
  )
}

export default App
