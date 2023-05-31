Feature: Administrating products

    Background:
        Given the admin is logged in the administration page

    Scenario: Listing all products
        Given the admin has clicked on the Catalog item in the navigation menu
        When the admin clicks on the Products item in the dropdown menu
        Then list of all products will be displayed

    Scenario: Editing product
        Given the list of all products is displayed
        And the list is not empty
        When the admin clicks on the blue edit button with the pencil
        Then the admin will be able to edit the product

    Scenario: Changing the quantity of product
        Given the product edit page is displayed
        When the user clicks on Data
        And changes the quantity of the product
        And saves the changes
        And returns to the product list page
        Then the updated quantity will be displayed


