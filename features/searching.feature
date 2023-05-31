Feature: Searching products

    Background:
        Given application is at a page where search bar is displayed

    Scenario Outline: Searching for existing products using the search bar
        When the user enters <query> into the search bar
        Then products that match the searched <query> are displayed

        Examples: Products
            | query  |
            | mac    |
            | canon  |
            | iphone |

    Scenario Outline: Searching for nonexisting products using the search bar
        When the user enters <query> into the search bar
        Then no products matching the criteria will be shown

        Examples: Products
            | query     |
            | laptop    |
            | asus      |
            | panasonic |
