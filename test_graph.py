from graph.workflow import app

result = app.invoke(
    {
        "question": "Puis-je bénéficier de trois jours de télétravail par semaine ?"
    }
)

print("\n===== RESULTAT FINAL =====\n")

print(result)