from typing import List

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select

from locators.quote_page_locators import QuotesPageLocator
from parsers.quote import QuoteParser


class QuotePage:
    def __init__(self, browser):
        self.browser = browser

    @property
    def quotes(self) -> List[QuoteParser]:
        return [
            QuoteParser(e)
            for e in self.browser.find_elements_by_css_selector(
                QuotesPageLocator.QUOTE
            )
        ]

    @property
    def author_dropdown(self) -> Select:
        element = self.browser.find_element_by_css_selector(
            QuotesPageLocator.AUTHOR_DROPDOWN
        )
        return Select(element)

    @property
    def tag_dropdown(self) -> Select:
        element = self.browser.find_element_by_css_selector(
            QuotesPageLocator.TAG_DROPDOWN
        )
        return Select(element)

    @property
    def search_button(self):
        return self.browser.find_element_by_css_selector(
            QuotesPageLocator.SEARCH_BUTTON
        )

    def select_author(self, author_name: str):
        self.author_dropdown.select_by_visible_text(author_name)

    def get_available_tags(self) -> List[str]:
        return [option.text.strip() for option in self.tag_dropdown.options[1:]]  # [1:]

    def select_tag(self, tag_name: str):
        self.tag_dropdown.select_by_visible_text(tag_name)

    def search_for_quotes(self, author_name: str, tag_name: str) -> List[QuoteParser]:
        self.select_author(author_name)
        try:
            self.select_tag(tag_name)
        except NoSuchElementException:
            raise InvalidTagForAuthorError(
                f"Author '{author_name}' does not have the given tag: '{tag_name}'."
            )
        self.search_button.click()
        return self.quotes


class InvalidTagForAuthorError(ValueError):
    pass

