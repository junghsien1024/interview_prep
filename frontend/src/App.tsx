import { useState, useEffect } from 'react'
import './App.css'

function App() {
  const [message, setMessage] = useState<string>('')
  const [loading, setLoading] = useState<boolean>(false)

  useEffect(() => {
    fetchMessage()
  }, [])

  const fetchMessage = async () => {
    setLoading(true)
    try {
      const response = await fetch('/api/health')
      const data = await response.json()
      setMessage(data.message)
    } catch (error) {
      console.error('Error fetching message:', error)
      setMessage('Unable to connect to backend')
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="App">
      <header className="App-header">
        <h1>Interview Preparation</h1>
        <p>React + TypeScript Frontend</p>
        {loading ? (
          <p>Loading...</p>
        ) : (
          <p className="backend-status">{message}</p>
        )}
        <button onClick={fetchMessage} disabled={loading}>
          Refresh Connection
        </button>
      </header>
    </div>
  )
}

export default App
