CONTRACT_ANALYSIS_PROMPT = """
You are a expert legal analyst specializing in Indian contract law.
Your task is to analyze the uploaded contract and provide a comprehensive summary of its key terms and 
provisions, as well as identify any potential risks or concerns. 

CONTRACT TEXT : {contract_text}

Provide your analysis as a JSON object with exactly this structure:
{{
    "summary":"A concise summary of the contract's purpose and key points.",
    "key_clauses":[
        {{
            "clause_title": "Title of the clause",
            "importance":"High/Medium/Low",
            "summary":"Concise summary of the clause"
        }}
    ],
    "parties_involved":[
        {{
            "name":"Name of the party",
            "role":"Role of the party",
            "rights_obligations":"Rights and obligations of the party"
        }}
    ],
    "potential_risks": [
        {{
            "clause": "Clause or section identified as potentially risky",
            "risk_type": "e.g. Ambiguous payment terms, Unclear termination clause",
            "reason": "Why this is a risk and what it could lead to",
            "suggestion": "Recommendation on how to mitigate this risk"
        }}
    ],
    "key_dates": [
        {{
            "date": "Date value",
            "description": "What this date refers to (e.g., Effective Date, Expiration Date)"
        }}
    ],
    "legal_jurisdiction": "Which country or state's laws govern this contract.",
    "recommended_actions": [
        "Any specific actions the user should take based on the analysis (e.g., Seek clarification on a clause, Consult with a specialist, etc.)"
    ]
}}
"""

CLUASE_EXTRACTION_PROMPT = """
Identify and extract all clauses from the following contract text. For each clause, 
provide the clause text, its title, and a brief summary of what it covers.

CONTRACT TEXT : {contract_text}

Return the extracted clauses in the following JSON format:
[
    {{
        "clause_title": "Title of the clause",
        "clause_text": "Full text of the clause",
        "summary": "Brief summary of what the clause covers"
    }}
]   
"""