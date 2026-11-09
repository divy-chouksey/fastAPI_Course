from models import ClauseAnalysis, RiskFlag, PartyInvolved, AnalysisResult
from services.prompt import CONTRACT_ANALYSIS_PROMPT, CLUASE_EXTRACTION_PROMPT
from config import GEMINI_API_KEY
from google import genai
from google.genai import types
import json
from asyncio import timeout

client = genai.Client(api_key=GEMINI_API_KEY)


async def analyze_contract_gemini(text_content: str) -> AnalysisResult:
    prompt = CONTRACT_ANALYSIS_PROMPT.format(contract_text=text_content[:15000])

    async with timeout(60):
        response = await client.aio.models.generate_content(
        model="models/gemini-3.5-flash-lite",
        contents=prompt,
        config=types.GenerateContentConfig(
            temperature=0.3,
            max_output_tokens=4096,
            response_mime_type="application/json",
        ),
        )
    


        raw_text = response.text.strip()
        if raw_text.startswith("```json"):
            raw_text = raw_text[7:]
        if raw_text.startswith("```"):
            raw_text = raw_text[3:]
        if raw_text.endswith("```"):
            raw_text = raw_text[:-3]
        raw_text = raw_text.strip()

        analysis_data = json.loads(raw_text)

        key_clauses = [
            ClauseAnalysis(**clause) for clause in analysis_data.get("key_clauses", [])
        ]
        risk_flags = [
            RiskFlag(**risk) for risk in analysis_data.get("potential_risks", [])
        ]
        parties_involved = [
            PartyInvolved(**party) for party in analysis_data.get("parties_involved", [])
        ]

        return AnalysisResult(
            summary=analysis_data.get("summary", ""),
            key_clauses=key_clauses,
            parties_involved=parties_involved,
            potential_risks=risk_flags,
            legal_jurisdiction=analysis_data.get("legal_jurisdiction", ""),
            recommended_actions=analysis_data.get("recommended_actions", []),
        )