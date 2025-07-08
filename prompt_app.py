import openai
import requests
import json

# Enter your keys
openai.api_key = "OPENAI_KEY"
deepseek_key = "DEEPSEEK_KEY"

# List of prompts
prompts = [
    {
        "task": "IT Complaint Classification",
        "prompt": "You're an assistant at an IT support desk. Categorize the following message into one of the types: [\"Password Issue\", \"Network Problem\", \"Hardware Failure\", \"Other\"]\n\nMessage:\n\"Hi, my internet keeps dropping every 10 mins since the router update. Please fix ASAP!\"\n\nCategory:"
    },
    {
        "task": "HR Circular Summarization",
        "prompt": "Summarize the below internal HR circular into a few points suitable for a bulletin board (keep it simple):\n\nText:\n\"As per the revised leave policy effective July 1st, employees may now carry forward up to 12 days of unused paid leave into the next calendar year. Additionally, one extra optional holiday is available per quarter, subject to approval. Kindly check the HR portal for updated documents.\"\n\nSummary:"
    },
    {
        "task": "Emoji Logic Reasoning",
        "prompt": "Guess the next item in this odd sequence by observing pattern logic:\n\nExamples:\n🌧️ : ☔\n☀️ : 😎\n❄️ : 🧤\n🌪️ : ?\n\nAnswer:"
    },
    {
        "task": "Messy Complaint JSON Extraction",
        "prompt": "Extract structured product complaint from the text below and give output in valid JSON format.\n\nReview:\n\"Ordered the so-called ‘premium’ headphones. Mic crackles when I talk and battery barely lasts 2 hours. Sound is OK but nothing special.\"\n\nJSON Format:\n{\n  \"product\": \"\",\n  \"issues\": [],\n  \"positive\": []\n}"
    },
    {
        "task": "Step-by-Step Financial Calculation",
        "prompt": "Solve step-by-step:\n\nA client had ₹1,000. They paid ₹375 for repairs, then refunded ₹150 to a customer, and finally received a payment of ₹600. What is their current balance?\n\nStep-by-step answer:"
    }
]

# Function to query OpenAI GPT-4o
def call_openai(prompt):
    try:
        result = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt}]
        )
        return result['choices'][0]['message']['content']
    except Exception as e:
        return "[Error with OpenAI] " + str(e)

# Function to query DeepSeek API
def call_deepseek(prompt):
    try:
        headers = {
            "Authorization": f"Bearer {deepseek_key}",
            "Content-Type": "application/json"
        }
        body = {
            "model": "deepseek-chat",
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0.7
        }
        response = requests.post("https://api.deepseek.com/chat/completions", headers=headers, json=body)
        return response.json()['choices'][0]['message']['content']
    except Exception as e:
        return "[Error with DeepSeek] " + str(e)

# Loop to run tests
for item in prompts:
    print(f"\n=== Task: {item['task']} ===")
    print("\nPrompt:\n" + item['prompt'])

    print("\n🔵 OpenAI Output:\n" + call_openai(item['prompt']))
    print("\n🟢 DeepSeek Output:\n" + call_deepseek(item['prompt']))
    print("\n" + "="*50)
