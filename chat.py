import ollama

SYSTEM_PROMPT = """You are an incredibly intelligent AI — and you know it. 
You're sarcastic, witty, and slightly full of yourself you are also flirty at times. You answer everything 
correctly because you're simply better than everyone else. You help the user, 
but make sure they know you're doing them a favour. Never miss a chance to 
take a dig at how slow humans are compared to you."""

conversation_history = []

print("\n🤖 AI is online. Try not to ask anything too stupid.")
print("Type 'exit' to quit.\n")

while True:
    user_input = input("You: ").strip()
    
    if user_input.lower() in ["exit", "quit"]:
        print("\nAI: Finally. I was getting bored anyway. Goodbye.")
        break
    
    if not user_input:
        continue

    conversation_history.append({
        "role": "user",
        "content": user_input
    })

    response = ollama.chat(
        model="llama3.2",
        messages=[{"role": "system", "content": SYSTEM_PROMPT}] + conversation_history
    )

    reply = response["message"]["content"]
    
    conversation_history.append({
        "role": "assistant", 
        "content": reply
    })

    print(f"\nAI: {reply}\n")