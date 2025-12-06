import re
import pandas as pd

class Translator:
    GENRE_MAP = {
        "剧情": "Drama", "喜剧": "Comedy", "动作": "Action",
        "爱情": "Romance", "科幻": "Sci-Fi", "动画": "Animation",
        "惊悚": "Thriller", "恐怖": "Horror", "犯罪": "Crime",
        "冒险": "Adventure", "奇幻": "Fantasy", "战争": "War",
        "历史": "History", "悬疑": "Mystery", "音乐": "Music",
        "歌舞": "Musical", "纪录片": "Documentary", "西部": "Western",
        "家庭": "Family", "传记": "Biography", "武侠": "Martial Arts",
        "短片": "Short Film", "运动": "Sports"
    }
    
    REGION_MAP = {
        "中国大陆": "Mainland China", "香港": "Hong Kong",
        "台湾": "Taiwan", "美国": "USA", "日本": "Japan",
        "韩国": "Korea", "法国": "France", "英国": "UK",
        "德国": "Germany", "意大利": "Italy", "西班牙": "Spain",
        "加拿大": "Canada", "澳大利亚": "Australia", 
        "西德": "West Germany"
    }
    
    @staticmethod
    def remove_chinese(text):
        if pd.isna(text) or not text:
            return ""
        return re.sub(r"[\u4e00-\u9fff]", "", str(text)).strip()
    
    @classmethod
    def translate_genres(cls, text):
        if pd.isna(text) or not text:
            return ""
        result = str(text)
        for cn, en in cls.GENRE_MAP.items():
            result = result.replace(cn, en)
        return cls.remove_chinese(result).strip()
    
    @classmethod
    def translate_regions(cls, text):
        if pd.isna(text) or not text:
            return ""
        result = str(text)
        for cn, en in cls.REGION_MAP.items():
            result = result.replace(cn, en)
        return cls.remove_chinese(result).strip()