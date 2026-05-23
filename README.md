# HR Policy Assistant

Système multi-agent RH basé sur LangChain, LangGraph et RAG multi-corpus.

## Objectif

Ce projet implémente un système multi-agent capable de :

- analyser une demande RH ;
- sélectionner le bon corpus documentaire ;
- rechercher des informations via RAG ;
- générer une réponse contextualisée ;
- intégrer une validation humaine (Human-in-the-loop).

Le système utilise LangGraph pour orchestrer le workflow agentique.

---

# Architecture

## Workflow global

Utilisateur
↓
Router Node
↓
Retriever Tool
↓
Generator Node
↓
Human Validation Node
↓
Réponse finale

---

## Agents et composants

### Router Node
Analyse la question RH et sélectionne le bon corpus documentaire.

### Retriever Tools
Effectuent la recherche sémantique dans les politiques RH.

### Generator Node
Génère une réponse RH contextualisée à partir des documents récupérés.

### Human Validation Node
Permet à un humain de valider ou rejeter la réponse générée.

---

# RAG Multi-Corpus

Le système utilise plusieurs corpus RH :

- Télétravail
- Congés et absences
- Formation
- Mobilité interne

Chaque corpus possède son propre retriever.

---

# Technologies utilisées

- Python
- LangChain
- LangGraph
- Ollama
- ChromaDB
- RAG
- uv

---

# Structure du projet

```text
hr_multi_agent/
│
├── agents/
├── tools/
├── graph/
├── config/
├── data/
├── vectordb/
│
├── ingest.py
├── human_validation.py
├── test_agent.py
├── test_graph.py
├── README.md