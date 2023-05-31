Feature: Logging in as a returning customer

    Background:
        Given the user has created an account before with "<email>" and "<password>"
        * the user is currently not logged in
        * the user clicked on My Account button
        * the user selected Login from the dropdown menu


    Scenario: Logging in with unknown credentials
        Given the user filled in the email and password fields
        When the user clicks on the Continue button
        Then a warning will be displayed
        And the user will not be logged in

    Scenario Outline: Logging in with known credentials
        Given the user filled in the email and password fields with "<email>" and "<password>"
        When the user clicks on the Continue button
        Then the user will be logged in

        Examples: Known credentials
            | email         | password |
            | test@test.com | test     |
