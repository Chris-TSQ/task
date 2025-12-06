import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns
import io

class PlotService:
    
    @staticmethod
    def create_bar_chart(data, title, ylabel, color):
        fig, ax = plt.subplots(figsize=(14, 8))
        ax.bar(range(len(data)), data.values, color=color, 
               edgecolor='black', alpha=0.7)
        ax.set_xticks(range(len(data)))
        ax.set_xticklabels(data.index, rotation=45, ha='right')
        ax.set_ylabel(ylabel, fontsize=12)
        ax.set_xlabel('Genre', fontsize=12)
        ax.set_title(title, fontsize=14, fontweight='bold')
        ax.grid(axis='y', alpha=0.3, linestyle='--')
        plt.tight_layout()
        return PlotService._fig_to_bytes(fig)
    
    @staticmethod
    def create_boxplot(df_ex):
        genre_order = df_ex['genres_en'].value_counts().index.tolist()
        fig, ax = plt.subplots(figsize=(16, 8))
        sns.boxplot(data=df_ex, x='genres_en', y='rating', 
                   order=genre_order, hue='genres_en', 
                   palette='Set2', legend=False, ax=ax)
        ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right')
        ax.set_ylabel('Rating', fontsize=12)
        ax.set_xlabel('Genre', fontsize=12)
        ax.set_title('Rating Distribution by Genre', 
                    fontsize=14, fontweight='bold')
        ax.set_ylim(6, 10)
        ax.grid(axis='y', alpha=0.3, linestyle='--')
        plt.tight_layout()
        return PlotService._fig_to_bytes(fig)
    
    @staticmethod
    def create_heatmap(df_ex):
        pivot = df_ex.pivot_table(index='genres_en', columns='region_en',
                                  values='rating', aggfunc='mean')
        fig = plt.figure(figsize=(16, 10))
        sns.heatmap(pivot, annot=True, fmt='.1f', cmap='YlGnBu',
                   cbar_kws={'label': 'Avg Rating'})
        plt.title('Average Rating by Genre and Region', 
                 fontsize=14, fontweight='bold')
        plt.ylabel('Genre', fontsize=12)
        plt.xlabel('Region', fontsize=12)
        plt.tight_layout()
        return PlotService._fig_to_bytes(fig)
    
    @staticmethod
    def _fig_to_bytes(fig):
        buf = io.BytesIO()
        fig.savefig(buf, format='png', dpi=100, bbox_inches='tight')
        plt.close(fig)
        buf.seek(0)
        return buf