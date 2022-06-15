import requests

BASE_URL = 'http://localhost:8000/api/v1'


def create_post(title, text):
    url = BASE_URL + '/posts/'
    response = requests.post(url, json={'title': title, 'text': text})
    print("Status", response.status_code)
    print("Created post", response.json())


def get_posts():
    url = BASE_URL + '/posts'
    response = requests.get(url, headers={'Accept': 'application/json'})
    print("Status", response.status_code)
    print("Headers", response.headers)
    print("Content", type(response.content), response.content)
    print("Text", type(response.text), response.text)
    print("Json", type(response.json()), response.json())


def delete_post(id):
    url = f'{BASE_URL}/posts/{id}/'
    response = requests.delete(url)
    print(response.status_code)


def update_post(id, title):
    url = f'{BASE_URL}/posts/{id}/'
    response = requests.patch(url, json={'title': title})
    print(response.status_code)
    print(response.json())


if __name__ == '__main__':
    # get_posts()
    # create_post("Hello requests", "Learn how to use requests package")
    # delete_post(2)
    update_post(3, "Learn requests")
