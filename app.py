from flask import Flask

app = Flask(__name__)

def get_repos():
    '''
    this function will return the first 100 repositories ordered by stars.
    '''

def list_of_lang():
    '''
    this function will return an object contains on the list of languages
    and number and list of repositories for each language.
    '''
    pass

@app.route('/trending_languages', methods=['GET'])
def get_lang():
    '''
    this is an endpoint to return the list of trending languages that
    including the count and list of repositories for each language.
    '''
    pass

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)