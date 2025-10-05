
import allure
from allure_commons.types import Severity
from selene import browser, be, have, by
from selene.support.shared.jquery_style import s
from users import users

@allure.tag("web", "ui", "smoke")
@allure.severity(Severity.CRITICAL)
@allure.feature("GitHub репозитории")
@allure.story("Поиск репозитория с issues")
@allure.label("owner", "YuryKambur")
@allure.link("https://github.com", name="Тестируемый сайт")

def test_github():
    github_main_open()
    search_for_repository(users.yurykambur_repo.repo)
    go_to_repository(users.yurykambur_repo.repo)
    search_issues()
    search_no_results()

@allure.step('Открыть главую страницу GitHub')
def github_main_open():
    browser.open("https://github.com")
    allure.attach(
        browser.driver.current_url,
        name="URL после открытия",
        attachment_type=allure.attachment_type.TEXT
    )

@allure.step('Нажать кнопку "Поиск" на главной странице GitHub')
def search_for_repository(repo):
    s('button[aria-label="Search or jump to…"]').click()
    s('#query-builder-test').should(be.visible).type(repo).press_enter()
    allure.attach(
        f"Искомый репозиторий: {repo}",
        name="Параметры поиска",
        attachment_type=allure.attachment_type.TEXT
    )

@allure.step('Кликнуть на {repo} в поисковой выдаче')
def go_to_repository(repo):
    s(by.link_text(repo)).click()

@allure.step('Кликнуть на вкладку "Issues"')
def search_issues():
    s("#issues-tab").click()

@allure.step('Проверить, что на странице есть текст "No results"')
def search_no_results():
    s('body').should(have.text('No results'))
    allure.attach(
        "Итоговая проверка: текст 'No results' найден.",
        name="Результат проверки",
        attachment_type=allure.attachment_type.TEXT
    )