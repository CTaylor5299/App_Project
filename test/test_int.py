import unittest
import time
from flask import url_for
from urllib.request import urlopen

from flask_testing import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from application import app, db
from application.models import Teams, Players

class TestBase(LiveServerTestCase):

    def create_app(self):
        """
        Configure the Flask app before every test.
        """
        app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:root@35.242.182.10/fpl"
        app.config['SECRET_KEY'] = "aodjiwjdoiwja"
        return app

    def setUp(self):
        """
        Setup the test driver and create table schema before every test.
        You can populate the table with some test tasks here if you want to
        test read/update/delete functionality.
        """
        print("--------------------------NEXT-TEST----------------------------------------------")
        chrome_options = Options()
        chrome_options.binary_location = "/usr/bin/chromium-browser"
        chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(executable_path="/home/Conno/chromedriver", chrome_options=chrome_options)
        self.driver.get("http://localhost:5000")
        db.drop_all()
        db.create_all()

    def tearDown(self):
        """
        Stop the driver after every test.
        """
        self.driver.quit()
        print("--------------------------END-OF-TEST----------------------------------------------\n\n\n-------------------------UNIT-AND-SELENIUM-TESTS----------------------------------------------")

    def test_server_is_up_and_running(self):
        """
        Test that the server is running before each test.
        """
        response = urlopen("http://localhost:5000")
        self.assertEqual(response.code, 200)

class TestTaskCreation(TestBase):
    def test_task_creation(self):
        """
        Test that a user can navigate to the Create Task page,
        enter the description for the task and check to see if
        it redirects to the home page
        """

        # Navigate to the Create Task page
        self.driver.find_element_by_xpath('/html/body/a[2]').click()
        time.sleep(1)

        # Input the task description into the form field
        self.driver.find_element_by_xpath('//*[@id="team_name"]').send_keys('Integration Test')
        self.driver.find_element_by_xpath('//*[@id="owner"]').send_keys('Test Integration')
        self.driver.find_element_by_xpath('//*[@id="submit"]').click()
        time.sleep(1)

        # Assert that browser redirects to home page
        assert url_for('home') in self.driver.current_url

if __name__ == '__main__':
    unittest.main(port=5000)
