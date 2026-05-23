from config.llm_config import llm

response = llm.invoke("Bonjour, présente-toi en une phrase.")

print(response.content)