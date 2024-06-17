from selenium.webdriver.common.by import By


class LoginScreen:
    LOG_IN_BUTTON = (By.ID, 'submit')

    def __init__(self, app):
        self.app = app

    def login_with_incorrent_creds(self):
        # TO DO: ADD Click on Account BTN and Send Keys to Email and Password Fields
        # TO DO: ADD Error Verification

        self.app.click_element(self.LOG_IN_BUTTON)

    # add additional method to check error visibility
