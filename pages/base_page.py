class BasePage:
    def __init__(self, page):
        self.page = page

    def click(self, selector):
        self.page.wait_for_selector(selector)
        self.page.click(selector)

    def fill(self, selector, value):
        self.page.wait_for_selector(selector)
        self.page.fill(selector, value)

    def get_text(self, selector):
        self.page.wait_for_selector(selector)
        return self.page.inner_text(selector)
