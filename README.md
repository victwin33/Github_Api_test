# Github_Api_test

## **Описание:**

Этот скрипт написан на Python и выполняет следующие тесты с помощью GitHub API:

#### Test_create_repository

   Проверку создания нового публичного репозитория:
   с помощью requests.post() отправляется запрос на создание публичного репозитория.

#### Test_get_list_repos

   Получение списка репозиториев пользователя для подтверждения создания нового репозитория: 
   запрос requests.get() возвращает список репозиториев, который проверяется на наличие созданного.

#### Test_delete_repo

   Удаление репозитория:
   с помощью requests.delete() выполняется удаление репозитория.

### Инструкция как установить зависимости, настроить переменные окружения и запустить тест.

#### Клонируйте репозиторий:
1. git clone https://github.com/victwin33/Github_Api_test.git
2. cd github-api-test

##### Установите зависимости:
pip install -r requirements.txt

#### Создайте файл .env в корне проекта и добавьте ваши данные
1. GITHUB_USERNAME=your_github_username
2. GITHUB_TOKEN=your_github_token
3. REPO_NAME=repo_name_to_create

#### Запустите скрипт
* Установите зависимости
``` shell
pip3 install -r requirements.txt
```
* Запустить тесты находящиеся в файле test_api.py
```shell
$ pytest test_api.py --alluredir=allure_results
```
* Посмотреть отчет в веб версии пройденного прогона
``` shell
allure serve allure_results

