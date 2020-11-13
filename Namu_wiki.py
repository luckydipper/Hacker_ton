import wikipediaapi
import json
wiki=wikipediaapi.Wikipedia('ko')

search = str(input())
page_py = wiki.page(search)
if page_py.exists():
#      print("Page - Summary: %s" % page_py.summary[0:100])

    search_dict = {'tag': search,
                    "patterns":[search],
                    "responses":[page_py.summary]}
else :
    print("이해하지 못했습니다")


def toJson(search_dict):
    with open('search.json', 'w', encoding='utf-8') as file :
        json.dump(search_dict, file, ensure_ascii=False, indent='\t')

toJson(search_dict)