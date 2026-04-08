📧 **AI Email Assistant (OpenEnv)**

An AI-powered Email Triage system that automatically classifies emails, assigns priority, and generates summaries using an OpenEnv-based environment.

🚀 **Features**

*   📥 Accepts multiple email inputs
    
*   🧠 Classifies emails into:
    
    *   🔥 Important
        
    *   📩 Normal
        
    *   🚫 Spam
        
*   ⚡ Assigns priority:
    
    *   High / Medium / Low
        
*   📝 Generates smart summary
    
*   🎯 Produces reward score (0.0 → 1.0)
    
*   🌐 REST API (OpenEnv compliant)
    
*   🎨 Interactive UI with live results
    

🏗️ **Project Structure**

email-env/

*   app.py → FastAPI server (UI + API)
    
*   environment.py → RL/OpenEnv logic
    
*   tasks.py → Email tasks
    
*   grader.py → Reward calculation
    
*   inference.py → Evaluation script
    
*   openenv.yaml → API specification
    
*   Dockerfile → Deployment setup
    
*   .env → Config variables
    

⚙️ **Setup & Run**

1️⃣ Install dependenciespip install fastapi uvicorn python-dotenv

2️⃣ Run serverpython -m uvicorn app:app --reload

🌐 Open in browser:[http://127.0.0.1:8000](http://127.0.0.1:8000/)

🧪 **Run Inference**

python inference.py

✅ Expected output:\[START\]\[STEP\]\[END\]

🔌 **API Endpoints**

*   /reset → Reset environment 🔄
    
*   /step → Submit action ▶️
    
*   /state → Get current state 📊
    
*   /tasks → View tasks 📋
    

📥 **Example Input**

Job alert: Sales Intern - ChennaiBank alert: INR 3000 debitedQuora digest: Are PhDs a scam?

📤 **Example Output**

*   Classification → important, important, normal
    
*   Priority → high, medium, low
    
*   Reward → 0.6
    

📊 **Reward System**

*   🟢 1.0 → Perfect classification
    
*   🟡 0.5–0.8 → Good
    
*   🔴 <0.5 → Needs improvement
    

🔑 **Environment Variables (.env)**

API\_BASE\_URL=[http://127.0.0.1:8000](http://127.0.0.1:8000/)MODEL\_NAME=dummy-modelHF\_TOKEN=your\_token

🐳 **Docker (Optional)**

docker build -t email-env .docker run -p 7860:7860 email-env

📦 **OpenEnv Compliance**

✔ Implements: reset(), step(), state()✔ Uses: openenv.yaml, tasks, grader

🎯 **Use Cases**

*   📧 Smart email filtering
    
*   🤖 AI assistants
    
*   ⚡ Productivity tools
    
*   🎮 RL-based decision systems
    

🏁 **Status**

✅ Fully functional✅ Ready for evaluation✅ Meets hackathon requirements

👨‍💻 **Author**

Logesh

📄 **License**

MIT License
