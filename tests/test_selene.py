from selene import by, browser, be, have, query
from selene.support.shared.jquery_style import s


def test_github():

    browser.open("https://github.com")
    s('button[aria-label="Search or jump to…"]').click()
    s('#query-builder-test').should(be.visible).type('YuryKambur/python_autotests_hw9').press_enter()

    s(by.link_text("YuryKambur/python_autotests_hw9")).click()

    s("#issues-tab").click()

    s('body').should(have.text('No results'))


