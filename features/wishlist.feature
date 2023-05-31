Feature: Adding products to the Wish List

    Background:
        Given the application is at the homepage


    Scenario: User not being logged in
        Given the user is not logged in
        When the user clicks on Add to Wish List button
        Then he will be prompted to create an account or log in

    Scenario: User being logged in
        Given the user is logged in
        When the user clicks on Add to Wish List button
        Then the item will be added to his Wish List

    Scenario: Adding products from Wishlist to cart
        Given the user is in their Wishlist page
        And the user has items in their Wishlist
        When the user clicks on the Add to cart button
        Then the product will be added to the cart
        And the total price of products in cart will be updated

    Scenario: Removing products from Wishlist
        Given the user is in their Wishlist page
        And the user has items in their Wishlist
        When the user clicks on the Remove button
        Then the products will be removed from the Wishlist


