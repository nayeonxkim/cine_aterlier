import googletrans

def to_english(title):
    translator = googletrans.Translator()
    translator.raise_Exception = True
    eng_title = translator.translate(title, dest='en', src='auto')
    return eng_title.text

print(to_english('nayeon'))


# my_dict = [{"model": "movies.movie",
#             "pk": 3,
#             "fields": {
#                 "original_title": "ant",
#                 "title": "개미",
#                 "overview": "개미개믹매ㅣ",
#                 "release_date": "2023-05-18",
#                 "poster_path": "/asdjahkdhaksd.jpg",
#                 "genre_id": 4,
#                 "adult": True,
#                 "popularity": "-0.04"
#                 }
#             }, {
#     "model": "movies.movie",
#     "pk": 8,
#     "fields": {
#         "original_title": "BBU",
#         "title": "뿌",
#         "overview": "뿌어ㅏㅂ너ㅓ와와벚ㅇㅂㅈㅇㅈ",
#         "release_date": "2023-05-09",
#         "poster_path": "/asdjahkdhaksd.jpg",
#         "genre_id": 7,
#         "adult": False,
#         "popularity": "0.05"
#     }
# }
# ]


# with open('temp.json', "w", encoding='utf-8') as f:
#     json.dump(my_dict,f, ensure_ascii=False,indent=4)