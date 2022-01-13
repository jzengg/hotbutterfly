from flask import Flask
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine

load_dotenv()

app = Flask(__name__)

DB_HOSTNAME = os.getenv('DB_HOSTNAME')
DB_USER = os.environ.get('DB_USER')
DB_PASSWORD = os.environ.get('DB_PASSWORD')
DB_PORT = os.environ.get('DB_PORT')
DB_NAME = os.environ.get('DB_NAME')

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

# if __name__ == '__main__':
  # print('hello')
  # app.run(host='0.0.0.0', port=30006, debug=True)

engine = create_engine(f'mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOSTNAME}:{DB_PORT}/{DB_NAME}', echo=True, future=True)
with engine.connect() as conn:
  result = conn.execute(text("select 'hello world'"))
  print(result.all())
