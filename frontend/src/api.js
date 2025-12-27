const API_BASE = import.meta.env.VITE_API_URL || '/api'

export async function fetchModules() {
  const res = await fetch(`${API_BASE}/modules/`)
  if (!res.ok) throw new Error('Failed to fetch modules')
  return res.json()
}

export async function fetchModule(moduleId) {
  const res = await fetch(`${API_BASE}/modules/${moduleId}`)
  if (!res.ok) throw new Error('Failed to fetch module')
  return res.json()
}

export async function fetchModuleByNumber(number) {
  const res = await fetch(`${API_BASE}/modules/number/${number}`)
  if (!res.ok) throw new Error('Failed to fetch module')
  return res.json()
}

export async function fetchLesson(lessonId) {
  const res = await fetch(`${API_BASE}/lessons/${lessonId}`)
  if (!res.ok) throw new Error('Failed to fetch lesson')
  return res.json()
}

export async function fetchLessonsByModule(moduleId) {
  const res = await fetch(`${API_BASE}/lessons/module/${moduleId}`)
  if (!res.ok) throw new Error('Failed to fetch lessons')
  return res.json()
}

export async function fetchNextLesson(lessonId) {
  const res = await fetch(`${API_BASE}/lessons/${lessonId}/next`)
  if (!res.ok) throw new Error('Failed to fetch next lesson')
  return res.json()
}

export async function executeCode(code, lessonId = null, userId = null) {
  const res = await fetch(`${API_BASE}/code/execute`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ code, lesson_id: lessonId, user_id: userId })
  })
  if (!res.ok) throw new Error('Failed to execute code')
  return res.json()
}

export async function updateProgress(userId, lessonId, completed, codeSubmission = null) {
  const res = await fetch(`${API_BASE}/progress/update`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      user_id: userId,
      lesson_id: lessonId,
      completed,
      code_submission: codeSubmission
    })
  })
  if (!res.ok) throw new Error('Failed to update progress')
  return res.json()
}

export async function fetchUserProgress(userId) {
  const res = await fetch(`${API_BASE}/progress/user/${userId}`)
  if (!res.ok) throw new Error('Failed to fetch progress')
  return res.json()
}

export async function fetchUserStats(userId) {
  const res = await fetch(`${API_BASE}/progress/user/${userId}/stats`)
  if (!res.ok) throw new Error('Failed to fetch stats')
  return res.json()
}

export async function fetchModuleProgress(userId, moduleId) {
  const res = await fetch(`${API_BASE}/progress/user/${userId}/module/${moduleId}`)
  if (!res.ok) throw new Error('Failed to fetch module progress')
  return res.json()
}

export function getUserId() {
  let userId = localStorage.getItem('python_learning_user_id')
  if (!userId) {
    userId = 'user_' + Math.random().toString(36).substr(2, 9)
    localStorage.setItem('python_learning_user_id', userId)
  }
  return userId
}

// Auth API
export async function register(username, password) {
  const res = await fetch(`${API_BASE}/auth/register`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    credentials: 'include',
    body: JSON.stringify({ username, password })
  })
  if (!res.ok) {
    const data = await res.json()
    throw new Error(data.detail || 'Registracija nije uspjela')
  }
  return res.json()
}

export async function login(username, password) {
  const res = await fetch(`${API_BASE}/auth/login`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    credentials: 'include',
    body: JSON.stringify({ username, password })
  })
  if (!res.ok) {
    const data = await res.json()
    throw new Error(data.detail || 'Prijava nije uspjela')
  }
  return res.json()
}

export async function logout() {
  const res = await fetch(`${API_BASE}/auth/logout`, {
    method: 'POST',
    credentials: 'include'
  })
  return res.json()
}

export async function checkAuth() {
  const res = await fetch(`${API_BASE}/auth/check`, {
    credentials: 'include'
  })
  return res.json()
}

// Module Access
export async function fetchUserModuleAccess() {
  const res = await fetch(`${API_BASE}/modules/user-access`, {
    credentials: 'include'
  })
  return res.json()
}

// Exercise API
export async function submitExercise(lessonId, exerciseIndex, code) {
  const res = await fetch(`${API_BASE}/exercises/submit`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    credentials: 'include',
    body: JSON.stringify({ lesson_id: lessonId, exercise_index: exerciseIndex, code })
  })
  if (!res.ok) {
    const data = await res.json()
    throw new Error(data.detail || 'Greška pri slanju vježbe')
  }
  return res.json()
}

export async function getExerciseStatus(lessonId) {
  const res = await fetch(`${API_BASE}/exercises/status/${lessonId}`, {
    credentials: 'include'
  })
  return res.json()
}

// Quiz API
export async function submitQuiz(lessonId, answers) {
  const res = await fetch(`${API_BASE}/quiz/submit`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    credentials: 'include',
    body: JSON.stringify({ lesson_id: lessonId, answers })
  })
  if (!res.ok) {
    const data = await res.json()
    throw new Error(data.detail || 'Greška pri slanju kviza')
  }
  return res.json()
}

export async function getQuizStatus(lessonId) {
  const res = await fetch(`${API_BASE}/quiz/status/${lessonId}`, {
    credentials: 'include'
  })
  return res.json()
}

// Admin API
export async function fetchAllUsers() {
  const res = await fetch(`${API_BASE}/admin/users`, {
    credentials: 'include'
  })
  if (!res.ok) throw new Error('Nemate pristup')
  return res.json()
}

export async function fetchUserStatsAdmin(userId) {
  const res = await fetch(`${API_BASE}/admin/users/${userId}/stats`, {
    credentials: 'include'
  })
  return res.json()
}

export async function fetchUserProgressAdmin(userId) {
  const res = await fetch(`${API_BASE}/admin/users/${userId}/progress`, {
    credentials: 'include'
  })
  return res.json()
}

export async function unlockModule(userId, moduleId, unlocked) {
  const res = await fetch(`${API_BASE}/admin/unlock-module`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    credentials: 'include',
    body: JSON.stringify({ user_id: userId, module_id: moduleId, unlocked })
  })
  return res.json()
}

export async function fetchAllModulesAdmin() {
  const res = await fetch(`${API_BASE}/admin/modules`, {
    credentials: 'include'
  })
  return res.json()
}
