Feature: Viewing order

    Background:
        Given the user has placed an order

    Scenario: Viewing order history
        Given user clicked on My account button
        When user clicks on Order History in the dropdown menu
        Then his order history will be displayed

    Scenario: Viewing order details
        Given the order history is displayed
        When the user clicks on the red button with eye
        Then order details will be displayed