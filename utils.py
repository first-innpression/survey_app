import csv
from model import Result
from flask import current_app

def add_results_to_csvfile():
    with current_app.app_context():
        results = Result.query.all()
        with open('results.csv', 'w', newline='', encoding='utf-8-sig') as csvfile:
            fieldnames = ['Email', 'Favorite Time', 'Favorite Season', 'Favorite Actor', 'Favorite Genres']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for r in results:
                writer.writerow({
                    'Email': r.email,
                    'Favorite Time': r.favorite_time,
                    'Favorite Season': r.favorite_season,
                    'Favorite Actor': r.favorite_actor,
                    'Favorite Genres': r.favorite_genres
                })