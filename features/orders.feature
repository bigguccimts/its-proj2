Feature: Administrating orders

    Background:
        Given the admin is logged in the administration page

    Scenario: Listing orders as admin
        Given the main dashboard page is displayed
        When the admin clicks on the view more button on the total orders image
        Then list of all orders will be displayed

    Scenario: Viewing order details as admin
        Given the list of orders is displayed
        When the admin clicks on the blue button with eye
        Then the order details will be displayed

    Scenario: Editing order
        Given the order details page is displayed
        And the admin changes details of the order
        When the admin clicks on the "Confirm" button
        Then the order details will be updated
