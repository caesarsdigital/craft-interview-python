## Prerequisites
* chromedriver [Installation Instructions](https://til.simonwillison.net/selenium/selenium-python-macos)
* Python 3.8.6
* Virtual Env with Requirements in requirements.txt

## Questions!
* Can you explain why you came to this file first? Or why not?
* Can you explain the basic structure of the project without reading this file? What are your expectations?
* Can you explain what the root level files might be for?

## Steps needed to add new tests
* If the new tests fit into any of the test files in the test folder, please add in there,
otherwise create a new test file in an existing or new directory as appropriate.
* Then, implement the marker and the test function

## Running tests locally:
Run the tests locally with: pytest -m "login"

## Where do I start?
1. Hit the URL (https://caesarspalaceonline.com/us/nj/casino)
2. Click on Log in button
3. Enter incorrect email and password
4. Click on Log In button
5. Verify "You have entered an incorrect email or password." message is displayed
6. Click on Close button
7. Enter "Caesars Palace Frenzy" in the search bar
8. Click on the "Caesars Palace Frenzy"
9. Verify Game info page is displayed for "Caesars Palace Frenzy"
