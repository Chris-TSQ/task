from models.database import Database
from utils.translators import Translator

class DataService:
    def __init__(self):
        self.db = Database()
        self.translator = Translator()
    
    def get_all_movies(self):
        query = """
            SELECT id, title, url, genres, region, rating 
            FROM douban_top100_movies 
            ORDER BY id
        """
        rows = self.db.execute_query(query)
        return [{
            "id": r[0], "title": r[1], "url": r[2],
            "genres": r[3], "region": r[4],
            "rating": float(r[5]) if r[5] else None
        } for r in rows]
    
    def get_genres_data(self):
        query = """
            SELECT genres, rating 
            FROM douban_top100_movies 
            WHERE genres IS NOT NULL AND rating IS NOT NULL
        """
        return self.db.fetch_dataframe(query)
    
    def get_full_data(self):
        query = """
            SELECT genres, region, rating 
            FROM douban_top100_movies 
            WHERE genres IS NOT NULL 
            AND region IS NOT NULL 
            AND rating IS NOT NULL
        """
        return self.db.fetch_dataframe(query)
    
    def prepare_genre_data(self, df, include_region=False):
        df["genres_en"] = df["genres"].apply(self.translator.translate_genres)
        if include_region:
            df["region_en"] = df["region"].apply(self.translator.translate_regions)
        return self._explode_genres(df)
    
    def _explode_genres(self, df):
        df_ex = df.assign(genres_en=df["genres_en"].str.split(r'\s*/\s*')).explode("genres_en")
        df_ex["genres_en"] = df_ex["genres_en"].str.strip()
        return df_ex[df_ex["genres_en"] != ""]