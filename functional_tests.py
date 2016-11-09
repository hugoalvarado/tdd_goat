from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome("D:\python\chromedriver_win32\chromedriver.exe")
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_questions_and_retrieve_later(self):
        # The user Anne opens browser
        self.browser.get("http://localhost:8000")

        # The page title needs to mention the site http://decisionsdecisions.com/
        self.assertIn('You tell me!', self.browser.title)

        # There is a label in the page "Should I (do|wear|eat|buy|other) this or that?

        # The site shows a gui to enter 2 short 150 char phrases
        inputbox1 = self.browser.find_element_by_id('id_new_question1')
        self.assertEqual(
            inputbox1.get_attribute('placeholder'),
            'Enter your question'
        )

        inputbox2 = self.browser.find_element_by_id('id_new_question2')
        self.assertEqual(
            inputbox2.get_attribute('placeholder'),
            'Enter your question'
        )

        # User enters "buy a rolex" in the first box
        inputbox1.send_keys('Buy a rolex')

        # Then user enters "buy a car" in the second box
        inputbox2.send_keys('Buy a car')

        # When Anne preses enter or clicks the save button she is asked for her email in a popup
        inputbox2.send_keys(Keys.ENTER)

        # She enters her email
        inputboxemail = self.browser.find_element_by_id('id_email')
        inputboxemail.send_keys('user@test.com')
        inputboxemail.send_keys(Keys.ENTER)


        # A url is generated where she can see
        # the results of the answers from other people helping her decide
        # the url is automatically emailed to her

        # The page refreshes and she sees her questions and counters/stats for her questions
        questiondiv1 = self.browser.find_element_by_id("question_1")
        questiondiv2 = self.browser.find_element_by_id("question_2")

        self.assertTrue(questiondiv1.text == "Buy a rolex")
        self.assertTrue(questiondiv2.text == "Buy a car")

        # None has voted on her questions, so there are no stats, they are all 0
        countsyesquestion1div = self.browser.find_element_by_id("question_1_answer_count")
        countsyesquestion2div = self.browser.find_element_by_id("question_1_answer_count")

        self.assertTrue(countsyesquestion1div.text == "0")
        self.assertTrue(countsyesquestion2div.text == "0")



        # end

if __name__ == '__main__':
    unittest.main(warnings='ignore')





