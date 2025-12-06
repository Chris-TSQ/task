import mysql.connector
import pandas as pd
from config import Config

class Database:
    def __init__(self):
        self.config = Config.get_db_config()
    
    def get_connection(self):
        return mysql.connector.connect(
            **self.config,
            charset="utf8mb4",
            ssl_disabled=True
        )
    
    def execute_query(self, query, params=None):
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute(query, params or ())
        results = cursor.fetchall()
        cursor.close()
        conn.close()
        return results
    
    def fetch_dataframe(self, query):
        conn = self.get_connection()
        df = pd.read_sql(query, conn)
        conn.close()
        return df