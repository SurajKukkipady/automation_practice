Feature: Order Transaction
    Tests related to Order Transaction functionality

    Scenario: Place an order and verify transaction
        Given User is on the order page
        And the user is on login page
        When User logs in with valid credentials
        And User adds a product to the cart
        And User proceeds to checkout
        And User places the order
        Then Verify the order is placed successfully