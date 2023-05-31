Feature: Finding product using Categories navigation bar

    Scenario: Using navigation bar
        Given the user is on a page where the Categories navigation bar is displayed
        When the user hovers mouse on desired category
        And the user clicks on an item from the displayed dropdown menu displayed
        Then the user will be redirected to a page containing all products from that category