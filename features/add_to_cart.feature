Feature: Adding products to cart

    Scenario: Adding products from homepage featured products
        Given the user is at the homepage
        When the user clicks on the "Add to Cart" button
        Then the product will be added to cart
        And the total price of products in cart will be updated

    Scenario: Adding products from search page
        Given the user has searched for a product
        And the user is at the search results page
        And at least one product is displayed
        When the user clicks on the "Add to Cart" button
        Then the product will be added to the cart
        And the total price of products in the cart will be updated

    Scenario: Adding products from product page
        Given the user is at the product page
        When the user sets the quantity to desired amount
        And click on the "Add to Cart" button
        Then the desired quantity of product will be added to the cart
        And the total price of products in the cart will be updated