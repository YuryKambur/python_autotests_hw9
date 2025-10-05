import allure
from allure_commons.types import Severity
from selene.support.shared.jquery_style import s
from selene import by, browser, be, have
from users import users



def test_github():
    allure.dynamic.tag("web", "ui", "smoke")
    allure.dynamic.severity(Severity.CRITICAL)
    allure.dynamic.feature("GitHub репозитории")
    allure.dynamic.story("Поиск репозитория без issues")
    allure.dynamic.link("https://github.com", name="Репозиторий")

    repo = users.yurykambur_repo.repo

    with allure.step('Открыть главую страницу GitHub'):
        browser.open("https://github.com")
        allure.attach(
            browser.driver.current_url,
            name="URL после открытия",
            attachment_type=allure.attachment_type.TEXT
        )

    with allure.step('Нажать кнопку "Поиск" на главной странице GitHub'):
        s('button[aria-label="Search or jump to…"]').click()

    with allure.step(f'Ввести в поисковую строку {repo}'):
        s('#query-builder-test').should(be.visible).type(repo).press_enter()

    with allure.step(f'Кликнуть на {repo} в поисковой выдаче'):
        s(by.link_text(repo)).click()
        allure.attach(
            f"Искомый репозиторий: {repo}",
            name="Параметры поиска",
            attachment_type=allure.attachment_type.TEXT
        )

    with allure.step('Кликнуть на вкладку "Issues"'):
        s("#issues-tab").click()

    with allure.step('Проверить, что на странице есть текст "No results"'):
        s('body').should(have.text('No results'))
        allure.attach(
            "Итоговая проверка: текст 'No results' найден.",
            name="Результат проверки",
            attachment_type=allure.attachment_type.TEXT
        )


