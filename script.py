import os
import openai
openai.api_key = "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"

completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "user", "content": "Hello!"}
  ]
)

print(completion.choices[0].message)