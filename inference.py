from dotenv import load_dotenv
import requests
import os

load_dotenv()

API = os.getenv("API_BASE_URL", "http://localhost:8000")

print("[START] Email AI Agent started")

# Reset env
requests.get(f"{API}/reset")

emails = [
    "Job alert: Sales Intern - Chennai",
    "Bank alert: INR 3000 debited from your account",
    "Quora digest: Are PhDs a scam?"
]

print(f"[STEP] Emails: {emails}")

# 🔥 SMART CLASSIFIER
def auto_classify(email):
    email = email.lower()

    if any(w in email for w in ["bank", "debit", "upi", "transaction"]):
        return ("important", "high")

    if any(w in email for w in ["job", "intern", "hiring"]):
        return ("important", "high")

    if any(w in email for w in ["otp", "alert", "security"]):
        return ("important", "high")

    if any(w in email for w in ["sale", "offer", "discount"]):
        return ("spam", "low")

    if any(w in email for w in ["quora", "digest", "newsletter"]):
        return ("normal", "low")

    return ("normal", "medium")


classification = []
priority = []

for e in emails:
    c, p = auto_classify(e)
    classification.append(c)
    priority.append(p)

# 🔥 SMART SUMMARY
summary = " | ".join([
    f"{c.upper()}-{p.upper()}: {e[:30]}"
    for c, p, e in zip(classification, priority, emails)
])

action = {
    "classification": classification,
    "priority": priority,
    "summary": summary
}

print(f"[STEP] Action: {action}")

res = requests.post(f"{API}/step", json=action)
data = res.json()

print(f"[STEP] Reward: {data['reward']}")

print("[END] Completed")