from ollama import chat

bad ="Tell me about cats."
good ="List 3 cat breeds that are suitable for a penthouse. 2 lines about each."

responseB = chat(
    model="llama3.2",
    messages=[
        {
            "role" : "user",
            "content" : bad
        }
    ]
)
responseG = chat(
    model="llama3.2",
    messages=[
        {
            "role" : "user",
            "content" : bad
        }
    ]
)
for t in [0,0.7,1.5]:
