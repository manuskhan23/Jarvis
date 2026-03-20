from groq import Groq

# pip install groq
client = Groq(
  api_key="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"
)

completion = client.chat.completions.create(
  model="llama-3.3-70b-versatile",
  messages=[
    {"role": "system", "content": "You are a virtual assistant named jarvis skilled in general tasks like Alexa and Google Cloud"},
    {"role": "user", "content": "what is coding"}
  ]
)

print(completion.choices[0].message.content)