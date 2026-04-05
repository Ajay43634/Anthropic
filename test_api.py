from dotenv import load_dotenv
load_dotenv(override=True)

from anthropic import Anthropic
client = Anthropic()

message = client.messages.create(
    model="claude-haiku-4-5-20251001",
    max_tokens=1000,
    messages=[{"role": "user", "content": "What is quantum computing? Answer in one sentence"}]
)

print(message.content[0].text)
