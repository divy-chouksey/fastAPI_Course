from google import genai
import base64
from os import getenv
from dotenv import load_dotenv
import json

load_dotenv()

client = genai.Client(api_key=getenv("GEMINI_API_KEY"))


CROP_ANALYSIS_PROMPT = """
You are an expert agricultural scientist specializing in crop disease detection 
analyze this image of a crop/plant and provide a detailed disease assessment .
Provide your analysis as a JSON object with exactly this structure:
{ 
    "crop_detected":"Name of the crop or plant visible in the image",
    "severity":"healthy" or "mild" or "moderate" or "severe" or "critical","is_disease_detected": true or false,
    "dieseases":[
    {
        "name" : "Disease name",
        "confidence" : 0.0 to 1.0 ,
        "description" : "Brief description of the disease and visible symptoms"
    }],
    "treatments":[
        {
        "treatment_name":"Name of treatment",
        "treatment_type":"organic" or "chemical" or "preventive",
        "instructions" : "Step by step treatment instructions",
        "urgency":"immediate" or "within_week" or "seasonal"
        }
    ],
    "overall_health":"One sentence summary of the plant health",
    "additional_notes":"Any other observations or recommendations" 

}
 """

async def analyze_image(image_content:bytes , content_type :str):


    interaction = client.interactions.create(
        model = "gemini-3.5-flash",
        input=[
            {"type":"text" , "text":CROP_ANALYSIS_PROMPT},
            {
                "type" : "image",
                "data" : base64.b64encode(image_content).decode('utf-8'),
                "mime_type":content_type
            }
        ]
    )
    #return as JSON parsed data
    #write the code to clean the output text
    output_text = interaction.output_text
    output_text = output_text.replace("```json", "")
    output_text = output_text.replace("```", "")
    output_text = output_text.strip()
    return json.loads(output_text)
