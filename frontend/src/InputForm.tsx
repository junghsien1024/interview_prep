import { useState, ChangeEvent, FormEvent } from 'react'
import './InputForm.css'

interface FormData {
    name: string
    email: string
    phone: string
}

interface FormErrors {
    name?: string
    email?: string
    phone?: string
}

function InputForm() {
    const [formData, setFormData] = useState<FormData>({
        name: '',
        email: '',
        phone: ''
    })

    const [errors, setErrors] = useState<FormErrors>({})
    const [submitted, setSubmitted] = useState<boolean>(false)

    const validateInput = (): boolean => {
        const newErrors: FormErrors = {}

        // Validate name
        if (!formData.name.trim()) {
            newErrors.name = 'Name is required'
        } else if (formData.name.trim().length < 2) {
            newErrors.name = 'Name must be at least 2 characters'
        }

        // Validate email
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/
        if (!formData.email.trim()) {
            newErrors.email = 'Email is required'
        } else if (!emailRegex.test(formData.email)) {
            newErrors.email = 'Please enter a valid email address'
        }

        // Validate phone
        const phoneRegex = /^[\d\s\-\+\(\)]+$/
        if (!formData.phone.trim()) {
            newErrors.phone = 'Phone is required'
        } else if (!phoneRegex.test(formData.phone)) {
            newErrors.phone = 'Please enter a valid phone number'
        } else if (formData.phone.replace(/\D/g, '').length < 10) {
            newErrors.phone = 'Phone number must be at least 10 digits'
        }

        setErrors(newErrors)
        return Object.keys(newErrors).length === 0
    }

    const handleChange = (e: ChangeEvent<HTMLInputElement>) => {
        const { name, value } = e.target
        setFormData(prev => ({
            ...prev,
            [name]: value
        }))
        // Clear error when user starts typing
        if (errors[name as keyof FormErrors]) {
            setErrors(prev => ({
                ...prev,
                [name]: undefined
            }))
        }
    }

    const handleSubmit = (e: FormEvent<HTMLFormElement>) => {
        e.preventDefault()

        if (validateInput()) {
            console.log('Form submitted:', formData)
            setSubmitted(true)
            // Here you could send data to your backend API
            // Example: await fetch('/api/users', { method: 'POST', body: JSON.stringify(formData) })

            // Reset form after 3 seconds
            setTimeout(() => {
                setFormData({ name: '', email: '', phone: '' })
                setSubmitted(false)
            }, 3000)
        }
    }

    return (
        <div className="input-form-container">
            <h1>User Input Form</h1>

            {submitted && (
                <div className="success-message">
                    ✓ Form submitted successfully!
                </div>
            )}

            <form onSubmit={handleSubmit} className="input-form">
                <div className="form-group">
                    <label htmlFor="name">Name:</label>
                    <input
                        type="text"
                        id="name"
                        name="name"
                        value={formData.name}
                        onChange={handleChange}
                        className={errors.name ? 'error' : ''}
                        placeholder="Enter your name"
                    />
                    {errors.name && <span className="error-message">{errors.name}</span>}
                </div>

                <div className="form-group">
                    <label htmlFor="email">Email:</label>
                    <input
                        type="email"
                        id="email"
                        name="email"
                        value={formData.email}
                        onChange={handleChange}
                        className={errors.email ? 'error' : ''}
                        placeholder="Enter your email"
                    />
                    {errors.email && <span className="error-message">{errors.email}</span>}
                </div>

                <div className="form-group">
                    <label htmlFor="phone">Phone:</label>
                    <input
                        type="tel"
                        id="phone"
                        name="phone"
                        value={formData.phone}
                        onChange={handleChange}
                        className={errors.phone ? 'error' : ''}
                        placeholder="Enter your phone number"
                    />
                    {errors.phone && <span className="error-message">{errors.phone}</span>}
                </div>

                <button type="submit" className="submit-button">
                    Submit
                </button>
            </form>
        </div>
    )
}

export default InputForm