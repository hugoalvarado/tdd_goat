from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome("D:\python\chromedriver_win32\chromedriver.exe")
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test(self):
        # The user Anne opens browser
        self.browser.get("http://localhost:8000")

        # The page title needs to mention the site http://decisionsdecisions.com/
        self.assertIn('You tell me!', self.browser.title)

        self.fail("Finish this")

        # There is a label in the page "Should I (do|wear|eat|buy|other) this or that?

        # The site shows a gui to enter 2 short 150 char phrases

        # User enters "buy a rolex" in the first box

        # Then user enters "buy a car" in the second box

        # When Anne preses enter or clicks the save button she is asked for her email in a popup


        # She enters her email

        # A url is generated where she can see
        # the results of the answers from other people helping her decide
        # the url is automatically emailed to her

        # When she clicks the close buttons on the popup the page refreshes and all inputs are cleared

        # When she clicks the url from the email she's taken to a page with stats on her question

        # end

if __name__ == '__main__':
    unittest.main(warnings='ignore')





