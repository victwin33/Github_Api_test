import requests
import os
from dotenv import load_dotenv, find_dotenv

# Загружаем переменные окружения
load_dotenv(find_dotenv())


GITHUB_USERNAME = os.getenv("GITHUB_USERNAME")
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
REPOSITORY_NAME = os.getenv("REPO_NAME")


class TestGitHubAPI:
    """Создание нового публичного репозитория на GitHub."""
    def test_create_repository(repo_name):
        headers = {
            "Authorization": f"token {GITHUB_TOKEN}",  # Заголовок авторизации с токеном(токен указан в переменной
            # окружения)
            "Accept": "application/vnd.github.v3+json",  # Указываем в headers версию API GitHub
        }
        data = {
            "name": REPOSITORY_NAME,  # Имя репозитория(указано в переменной окружения)
            "description": "This is a from API call",
            "private": False,  # Указываем что репозиторий публичный
        }
        CREATE_REPO_URL = "https://api.github.com/user/repos"
        r = requests.post(CREATE_REPO_URL, json=data, headers=headers)
        if r.status_code == 201:
            print(f"Новый репозиторий '{REPOSITORY_NAME}' создан.")
        else:
            print(f"Не удалось создать новый репозиторий: {r.status_code}, {r.json()}")


    """ Получение списка репозиториев пользователя для подтверждения создания нового репозитория."""
    def test_get_list_repos(self):
        headers = {
            "Authorization": f"token {GITHUB_TOKEN}",  # Заголовок авторизации с токеном(токен указан в переменной
            # окружения)
            "Accept": "application/vnd.github.v3+json",  # Указываем в headers  версию API GitHub
        }
        GET_LIST_REPO_URL = f"https://api.github.com/users/{GITHUB_USERNAME}/repos"
        r = requests.get(GET_LIST_REPO_URL, headers=headers)
        if r.status_code == 200:
            repos = r.json()
            return [repo['name'] for repo in repos]  # Возвращаем список c именами репозиториев
        else:
            print(f"Не удалось получить список репозиториев: {r.status_code}, {r.json()}")
            return []

    """Удаление репозитория с GitHub."""
    def test_delete_repo(repo_name):
        headers = {
            "Authorization": f"token {GITHUB_TOKEN}",  # Заголовок авторизации с токеном
            "Accept": "application/vnd.github.v3+json",  # Указываем версию API GitHub
        }
        DELETE_REPO_URL = f"https://api.github.com/repos/{GITHUB_USERNAME}/{repo_name}"
        r = requests.delete(DELETE_REPO_URL, headers=headers)
        if r.status_code == 204:
            print(f"Репозиторий '{repo_name}' успешно удален.")
        else:
            print(f"Не удалось удалить репозиторий: {r.status_code}, {r.json()}")

    if __name__ == "__main__":
        # Создаем репозиторий
        create_repo(REPO_NAME)

        # Проверяем его наличие в списке репозиториев
        repos = list_repos()
        if REPO_NAME in repos:
            print(f"Репозиторий '{REPO_NAME}' присутствует в списке репозиториев.")
        else:
            print(f"Репозиторий '{REPO_NAME}' не найден.")

        # Удаляем репозиторий
        delete_repo(REPO_NAME)