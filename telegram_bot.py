TELEGRAM_TOKEN = "6715995399:AAGdCFwCqbnX_etoQ5p7uc9MVqiLiRqouxY"

import openai

openai.api_key = "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"

response = openai.Completion.create(
    model = "text-davinci-003",
    prompt = "Hello, I am Davinci!",
    temperature = 0.5,
    max_tokens = 1024,
    top_p = 1,
    frequency_penalty = 0.0,
    presence_penalty = 0.0,
)

print(response.choices[0].text)