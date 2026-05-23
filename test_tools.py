from tools.hr_tools import search_telework_policy

result = search_telework_policy.invoke(
    "Combien de jours de télétravail sont autorisés par semaine ?"
)

print(result)