import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "26551994")

API_HASH = os.environ.get("API_HASH", "80bb600d382bb46ce394c2808e1ef2ac")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6237341566:AAENXTuZecPPduK5ZvJIiKIJTYUeMCzSH7U") 

FORCE_SUB = os.environ.get("FORCE_SUB", "botosteeve") 

DB_NAME = os.environ.get("DB_NAME","Cluster0")     

DB_URL = os.environ.get("DB_URL","mongodb+srv://Renamebotv1:Renamebotv1@cluster0.nz721xb.mongodb.net/?retryWrites=true&w=majority")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://images.app.goo.gl/623TXcmCEsGtvuPL7")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '1591539219').split()]

PORT = os.environ.get("PORT", "8080")
