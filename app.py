from flask import Flask
from datetime import datetime, timedelta
import requests, json

# For our api documentation using swagger
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)

def get_repos():
    '''
    this function will return the first 100 repositories ordered by stars.
    '''
    # start date of the last 30 days from now
    date = (datetime.now() - timedelta(30)).date()

    url = f'https://api.github.com/search/repositories?q=created:>{date}&sort=stars&order=desc&page=1&per_page=100'
    response = requests.get(url)
    repos = response.json()
    return repos

def list_of_lang():
    '''
    this function will return an object contains on the list of languages
    and number and list of repositories for each language.
    '''
    repos = get_repos()
    languages = {}
    for repo in repos['items']:
        lang = repo['language']
        if lang != None:
            if lang in languages :
                languages[lang]["repositories_count"] +=1
                languages[lang]["repositories"].append({'repository_name': repo['name'],
                                                        'repository_url': repo['html_url']
                                                        })
            else:
                languages[lang] = {}
                languages[lang]["repositories_count"] = 1
                languages[lang]["repositories"] = []
                languages[lang]["repositories"].append({'repository_name': repo['name'],
                                                        'repository_url': repo['html_url']
                                                        })
    languages = json.dumps(languages)
    return languages

@app.route('/trending_languages', methods=['GET'])
def get_lang():
    '''
    this is an endpoint to return the list of trending languages that
    including the count and list of repositories for each language.
    '''
    return list_of_lang()

# API Documentation config
SWAGGER_URL = '/docs'
API_URL = '/static/swagger.json'
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name' : "Github_Trendings"
    }
)

app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)