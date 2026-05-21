import { useState } from "react"

function StudentForm({ onPredict }) {

    const [formData, setFormData] = useState({
        gender: "",
        race_ethnicity: "",
        parental_level_of_education: "",
        lunch: "",
        test_preparation_course: "",
        reading_score: "",
        writing_score: ""
    })

    const handleChange = (e) => {
        setFormData({
            ...formData,
            [e.target.name]: e.target.value
        })
    }

    const handleSubmit = (e) => {
        e.preventDefault()
        onPredict(formData)
    }

    return (

        <form className="student-form" onSubmit={handleSubmit}>
            <div className="form-group">
                <label>Gender</label>
                <select
                    name="gender"
                    onChange={handleChange}
                    required
                >
                    <option value="">Select Gender</option>
                    <option value="male">Male</option>
                    <option value="female">Female</option>
                </select>
            </div>

            <div className="form-group">
                <label>Race / Ethnicity</label>
                <select
                    name="race_ethnicity"
                    onChange={handleChange}
                    required
                >
                    <option value="">Select Group</option>
                    <option value="group A">Group A</option>
                    <option value="group B">Group B</option>
                    <option value="group C">Group C</option>
                    <option value="group D">Group D</option>
                    <option value="group E">Group E</option>
                </select>
            </div>

            <div className="form-group">
                <label>Parental Education</label>
                <select
                    name="parental_level_of_education"
                    onChange={handleChange}
                    required
                >
                    <option value="">Select Education</option>
                    <option value="some high school">Some High School</option>
                    <option value="high school">High School</option>
                    <option value="some college">Some College</option>
                    <option value="associate's degree">Associate Degree</option>
                    <option value="bachelor's degree">Bachelor Degree</option>
                    <option value="master's degree">Master Degree</option>
                </select>
            </div>

            <div className="form-group">
                <label>Lunch Type</label>
                <select
                    name="lunch"
                    onChange={handleChange}
                    required
                >
                    <option value="">Select Lunch Type</option>
                    <option value="standard">Standard</option>
                    <option value="free/reduced">Free/Reduced</option>
                </select>
            </div>

            <div className="form-group">
                <label>Test Preparation Course</label>
                <select
                    name="test_preparation_course"
                    onChange={handleChange}
                    required
                >
                    <option value="">Select Option</option>
                    <option value="completed">Completed</option>
                    <option value="none">None</option>
                </select>
            </div>

            <div className="form-group">
                <label>Reading Score</label>
                <input
                    type="number"
                    name="reading_score"
                    placeholder="Enter Reading Score"
                    onChange={handleChange}
                    required
                />
            </div>

            <div className="form-group">
                <label>Writing Score</label>
                <input
                    type="number"
                    name="writing_score"
                    placeholder="Enter Writing Score"
                    onChange={handleChange}
                    required
                />

            </div>
            <button type="submit">
                Predict Math Score
            </button>
        </form>
    )
}

export default StudentForm