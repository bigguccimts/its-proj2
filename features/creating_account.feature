
Feature: Creating new account

    Background:
        Given the user clicked on My Account button
        And the user selected Register from the dropdown menu

    Scenario: Creating new account and not agreeing to the Privacy Policy
        Given the user filled in all blank fields
        And the user has not checked the agreement to the Privacy Policy
        When the user clicks on the Continue button
        Then a warning will be displayed
        And the user can not continue with the account creation


    Scenario: Creating new account with email address already in use
        Given account with credentials already exists
        Given the user filled in all blank fields
        And the user has checked the agreement to the Privacy Policy
        When the user clicks on the Continue button
        Then a warning will be displayed
        And the user can not continue with the account creation

    Scenario: Creating new account with email address not already in use
        Given the user filled in all blank fields
        And the user has checked the agreement to the Privacy Policy
        When the user clicks on the Continue button
        Then new account will be created

