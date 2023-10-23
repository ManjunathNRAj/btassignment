@btassignment_add_items_to_cart
Feature: British Telecom Assignment for checking demo website add items to cart feature [ https://react-shopping-cart-67954.firebaseapp.com/ ]

  @btassignment_02_Test1
  Scenario: Verify items are listed in cart in the order as added to cart with price
    Given launch browser and open "website_url_txt"
    And wait for xpath "add_to_cart_txt.format(1)" for validation with timeout "10"
    When I add first "3" items to cart
    And I Click "another item" with xpath "add_to_cart_txt.format(5)"
    Then I verify items list "checkout_items_list" added in checkout panel
    And close browser

  @btassignment_02_Test2
  Scenario: Verify user is able to add same items as desired
    Given launch browser and open "website_url_txt"
    And wait for xpath "add_to_cart_txt.format(1)" for validation with timeout "10"
    When I Click "an item" with xpath "add_to_cart_txt.format(1)"
    And I Click "same item" with xpath "add_to_cart_txt.format(1)"
    Then Validate value "$ 21.80" of "str" from xpath "fetch_total_amount"
    And Validate value "2" of "str" from xpath "fetch_no_of_items_cart"
    When I Click "increase item number in checkout" with xpath "increase_item_no_checkout"
    Then Validate value "$ 32.70" of "str" from xpath "fetch_total_amount"
    And Validate value "3" of "str" from xpath "fetch_no_of_items_cart"
    And close browser
