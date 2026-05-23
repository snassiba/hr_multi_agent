from agents.hr_agent import answer_hr_question

question = input("Posez votre question RH : ")

response = answer_hr_question(question)

print("\n===== REPONSE PROPOSEE PAR L'AGENT =====\n")
print(response)

validation = input("\nValider cette réponse ? oui/non : ")

if validation.lower() == "oui":
    print("\n===== REPONSE VALIDEE =====\n")
    print(response)
else:
    correction = input("\nExpliquez la correction souhaitée : ")

    print("\n===== REPONSE A CORRIGER =====\n")
    print("Correction demandée par l'humain :")
    print(correction)