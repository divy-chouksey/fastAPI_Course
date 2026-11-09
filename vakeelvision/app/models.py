from pydantic import BaseModel , Field
from typing import Optional
from datetime import datetime



class Contract(BaseModel):
    id:Optional[str] = None
    filename : str
    original_name : str
    upload_date : str = ""
    text_content: str = ""
    page_count : int = 0
    word_count : int = 0
    status : str = "uploaded"

    def model_post_init(self, __context):
        if not self.upload_date:
            self.upload_date = datetime.now().isoformat()

class ClauseAnalysis(BaseModel):
    clause_title: str
    importance:str
    summary:str

class PartyInvolved(BaseModel):
    name: str
    role: str
    rights_obligations: str
    
class RiskFlag(BaseModel):
    clause: str
    risk_type: str
    reason: str
    suggestion: str

class AnalysisResult(BaseModel):
    id: Optional[str] = None
    summary: str
    key_clauses: list[ClauseAnalysis]
    parties_involved: list[PartyInvolved]
    potential_risks: list[RiskFlag]
    legal_jurisdiction: str
    recommended_actions: list[str]

    
