import os
from dotenv import load_dotenv
load_dotenv()

# 환경 변수 가져오기
client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")



# 환경 변수 가져오기
base_path = os.getenv("BASE")
processed_path = os.getenv("PROCESSED")
report_path = os.getenv("REPORT")
image_path =os.getenv("IMAGE")
trans_image_path =os.getenv("TRANSIMAGE")
