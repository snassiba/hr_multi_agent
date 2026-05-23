from config.llm_config import llm

from tools.hr_tools import (
    search_telework_policy,
    search_leave_policy,
    search_training_policy,
    search_mobility_policy
)


def select_tool(question: str):
    question_lower = question.lower()

    if "télétravail" in question_lower or "teletravail" in question_lower:
        return search_telework_policy

    if "congé" in question_lower or "absence" in question_lower or "maladie" in question_lower:
        return search_leave_policy

    if "formation" in question_lower or "certification" in question_lower:
        return search_training_policy

    if "mobilité" in question_lower or "poste" in question_lower or "carrière" in question_lower:
        return search_mobility_policy

    return search_telework_policy


def answer_hr_question(question: str) -> str:
    selected_tool = select_tool(question)

    context = selected_tool.invoke(question)

    prompt = f"""
Tu es un assistant RH professionnel.

Question du collaborateur :
{question}

Informations trouvées dans les politiques RH :
{context}

Consigne :
Réponds en français.
Utilise uniquement les informations fournies.
Si une validation RH ou manager est nécessaire, indique-le clairement.
Réponds de manière simple, professionnelle et prudente.
"""

    response = llm.invoke(prompt)

    return response.content