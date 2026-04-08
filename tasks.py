TASKS = [

    {
        "emails": [
            "Meeting at 10 AM",
            "Spotify autopay tomorrow",
            "50% OFF sale!!!"
        ],
        "context": {
            "time_now": "9:30 AM",
            "user_goal": "prepare for interview"
        },
        "answer": {
            "classification": ["important", "normal", "spam"],
            "priority": ["high", "medium", "low"],
            "summary": "Meeting at 10 AM soon. Focus on interview."
        }
    },

    {
        "emails": [
            "Bank alert: INR 5000 debited",
            "OTP for login",
            "Amazon sale 50% off"
        ],
        "context": {},
        "answer": {
            "classification": ["important", "important", "spam"],
            "priority": ["high", "high", "low"],
            "summary": "Bank and OTP alerts are critical."
        }
    },

    {
        "emails": [
            "Job opening: Software Intern",
            "LinkedIn message",
            "Discount offer today"
        ],
        "context": {},
        "answer": {
            "classification": ["important", "normal", "spam"],
            "priority": ["high", "medium", "low"],
            "summary": "Focus on job opportunity."
        }
    },

    {
        "emails": [
            "Security alert",
            "Meeting reminder",
            "Newsletter digest"
        ],
        "context": {},
        "answer": {
            "classification": ["important", "important", "normal"],
            "priority": ["high", "high", "low"],
            "summary": "Security and meeting are important."
        }
    }

]