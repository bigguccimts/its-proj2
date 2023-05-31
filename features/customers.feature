Feature: Administrating customers

    Background:
        Given the admin is logged in the administration page

    Scenario: Listing all customers from the main dashboard page
        Given the admin is at the dashboard page
        When the admin clicks the View more button on the total customers image
        Then the list of all customers will be displayed

    Scenario: Editing customer data
        Given the list of all customers is displayed
        When the admin clicks on the Edit button
        Then the admin will be able to edit the customer data