Feature: Checking out
    Background:
        Given products are in shopping cart
        And the user is at the Checkout page


    Scenario: Checkout with being logged in without prior order
        Given the user is logged in
        When the user inputs address
        And selects the flat rate
        And selects the payment method
        And the user clicks on confirm order button
        Then his order will be placed
        And the user will be redirected to a site telling him so

    Scenario: Checkout as a guest
        Given the user is logged out
        When the user selects guest checkout
        * the user fills in the details
        * the user selects the flat rate
        * the user selects the payment method
        * the user clicks on confirm order button
        Then his order will be placed
        And the user will be redirected to a site telling him so

    Scenario: Checkout and registering new account
        Given the user is logged out
        When the user selects register account
        * the user fills in the details
        * the user checks that he read and agrees to the Privacy Policy checkbox
        * the user clicks on continue button
        Then he can not proceed the checkout
        But his account will be created
