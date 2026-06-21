email_content = input("Enter the email content: ")

risk_score = 0
suspicious_keywords = [
    "urgent",
    "immediately",
    "suspended",
    "verify your password",
    "otp",
    "bank account",
    "credit card",
    "click here"
]

for keyword in suspicious_keywords:
    if keyword.lower() in email_content.lower():
        risk_score += 1

if "http://" in email_content or "https://" in email_content:
    risk_score += 1
if risk_score >= 5:
    risk_level = "HIGH RISK"
elif risk_score >= 3:
    risk_level = "MEDIUM RISK"
else:
    risk_level = "LOW RISK"

print("\nEmail Risk Analysis")
print("-------------------")
print("Risk Score:", risk_score)
print("Risk Level:", risk_level)

if risk_level != "LOW RISK":
    print("Warning: This email may be unsafe.")
else:
    print("This email appears safe.")