# import csv
#
#
# from main import app, Result
#
# def add_results_to_csvfile():
#     with app.app_context():
#         results = Result.query.all()
#         with open('results.csv', 'w', newline ='', encoding='utf-8') as csvfile:
#
#             fieldnames = ['Email', 'Favorite Time', 'Favorite Season', 'Favorite Actor', 'Favorite Genres']
#             writer = csv.DictWriter(csvfile, fieldnames= fieldnames)
#
#             writer.writeheader()
#
#             for r in results:
#                 print(r.email, r.favorite_time, r.favorite_season,  r.favorite_actor, r.favorite_genres)
#                 writer.writerow({
#                     'Email': r.email,
#                     'Favorite Time': r.favorite_time,
#                     'Favorite Season': r.favorite_season,
#                     'Favorite Actor': r.favorite_actor,
#                     'Favorite Genres': r.favorite_genres
#                 })
#
#
#






