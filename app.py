from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from environment import EmailEnv

app = FastAPI()
env = EmailEnv()

@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <html>
    <head>
        <title>AI Email Assistant</title>

        <style>
            body {
                font-family: 'Segoe UI';
                background: linear-gradient(135deg, #0f172a, #1e293b);
                color: white;
                text-align: center;
            }

            h1 { color: #38bdf8; }

            textarea {
                width: 400px;
                height: 100px;
                border-radius: 10px;
                padding: 10px;
                border: none;
            }

            button {
                padding: 12px 25px;
                margin: 15px;
                border-radius: 10px;
                border: none;
                background: #38bdf8;
                color: black;
                font-weight: bold;
                cursor: pointer;
            }

            button:hover {
                background: #0ea5e9;
                transform: scale(1.05);
            }

            .container {
                display: flex;
                justify-content: center;
                flex-wrap: wrap;
            }

            .card {
                background: #1e293b;
                padding: 15px;
                margin: 10px;
                border-radius: 12px;
                width: 260px;
            }

            .tag {
                margin-top: 10px;
                padding: 5px 10px;
                border-radius: 8px;
                display: inline-block;
                font-weight: bold;
                color: white;
            }

            .result {
                background: #1e293b;
                padding: 20px;
                margin: 20px;
                border-radius: 12px;
            }
        </style>
    </head>

    <body>

        <h1>📩 AI Email Assistant</h1>

        <h3>Paste Emails (one per line)</h3>
        <textarea id="inputEmails"></textarea><br>

        <button onclick="loadEmails()">Load Emails</button>

        <div class="container" id="emails"></div>

        <button onclick="submitAction()">Run AI</button>

        <div class="result" id="result"></div>

        <script>
            let currentEmails = [];

            function loadEmails() {

                let input = document.getElementById("inputEmails").value;
                let emails = input.split("\\n").filter(e => e.trim() !== "");

                currentEmails = emails;

                let html = "";

                emails.forEach((email, i) => {

                    let reason = "";

                    if (email.toLowerCase().includes("bank")) 
                        reason = "💳 Bank alert";
                    else if (email.toLowerCase().includes("job")) 
                        reason = "💼 Job related";
                    else if (email.toLowerCase().includes("sale")) 
                        reason = "🛒 Promotion";
                    else 
                        reason = "📩 General";

                    html += `
                    <div class="card">
                        <p>${email}</p>
                        <div id="tag${i}" class="tag">Waiting...</div>
                        <p style="font-size:12px;color:gray;">${reason}</p>
                    </div>
                    `;
                });

                document.getElementById("emails").innerHTML = html;
            }

            function autoClassify(email) {

                email = email.toLowerCase();

                if (email.includes("bank") || email.includes("otp") || email.includes("alert"))
                    return {c:"important", p:"high"};

                if (email.includes("job") || email.includes("intern"))
                    return {c:"important", p:"medium"};

                if (email.includes("offer") || email.includes("sale"))
                    return {c:"spam", p:"low"};

                return {c:"normal", p:"low"};
            }

            async function submitAction() {

                await fetch('/reset');

                let classification = [];
                let priority = [];

                currentEmails.forEach((email, i) => {

                    let result = autoClassify(email);

                    classification.push(result.c);
                    priority.push(result.p);

                    let tag = document.getElementById("tag"+i);

                    if(result.c === "important") {
                        tag.innerHTML = "🔥 Important";
                        tag.style.background = "#16a34a";
                    } 
                    else if(result.c === "spam") {
                        tag.innerHTML = "🚫 Spam";
                        tag.style.background = "#dc2626";
                    } 
                    else {
                        tag.innerHTML = "📩 Normal";
                        tag.style.background = "#eab308";
                    }
                });

                let summary = currentEmails.length > 0
                    ? "Focus on: " + currentEmails[0]
                    : "No emails";

                let action = {
                    classification: classification,
                    priority: priority,
                    summary: summary
                };

                let res = await fetch('/step', {
                    method: "POST",
                    headers: {"Content-Type": "application/json"},
                    body: JSON.stringify(action)
                });

                let data = await res.json();

                document.getElementById("result").innerHTML =
                    `<h2>Score: ${data.reward.toFixed(2)}</h2>
                     <p>${data.feedback}</p>`;
            }
        </script>

    </body>
    </html>
    """

@app.get("/reset")
def reset():
    return env.reset()

@app.post("/step")
def step(action: dict):

    if env.task is None:
        env.reset()

    try:
        _, reward, done, _ = env.step(action)
    except Exception as e:
        return {
            "reward": 0.0,
            "done": True,
            "feedback": f"Error: {str(e)}"
        }

    if reward > 0.8:
        feedback = "Excellent! Almost perfect."
    elif reward > 0.5:
        feedback = "Good, but can improve."
    else:
        feedback = "Needs improvement."

    return {
        "reward": reward,
        "done": done,
        "feedback": feedback
    }

@app.get("/state")
def state():
    return env.state()

@app.get("/tasks")
def tasks():
    return {"message": "Email tasks"}