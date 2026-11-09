from dotenv import load_dotenv
import os

load_dotenv()

MONGODB_URI = os.getenv("MONGODB_URI")
ALLOWED_EXTENSIONS = [".pdf", ".txt"]
MAX_FILE_SIZE_MB = 10  # Maximum file size in megabytes
UPLOADS_DIR = "uploads" # Default to "uploads" if not set
GEMINI_API_KEY = os.getenv("GOOGLE_AI_API_KEY")