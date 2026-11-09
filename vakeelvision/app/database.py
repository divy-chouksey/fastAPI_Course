from pymongo import MongoClient
from config import MONGODB_URI


client = MongoClient(MONGODB_URI)
db = client["mydb"]

#collections
contracts_collection  = db["contracts"]
analysis_collection = db["analysis"]

def init_db():
    # Create collections if they don't exist
    contracts_collection.create_index("filename", unique=True)
    analysis_collection.create_index("contract_id", unique=True)


