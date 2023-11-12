from selene.support.shared import browser
from selene import be, have


def test_google_should_find_selene():
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))


def test_google_should_not_find_selene():
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('hjkjkmmuikhkjjllo;').press_enter()
    browser.element('#botstuff').should(have.text('По запросу hjkjkmmuikhkjjllo; ничего не найдено.'))
