import pytest


@pytest.mark.login
def test_login_incorrect_credentials(login_screen):
    """
    Given the app on the account login screen
    When I Enter Incorrect Credential and try to Login
    Then Incorrect credential error should be visible
    """
    # Login with incorrect credentials
    login_screen.login_with_incorrent_creds()
    # Verify incorrect Credentials msg appears
