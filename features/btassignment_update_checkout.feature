@btassignment_update_checkout
Feature: Update and checkout to complete order in demo website [ https://react-shopping-cart-67954.firebaseapp.com/ ]

  @btassignment_03_Test1
  Scenario: Verify user can delete items in cart
    Given launch browser and open "website_url_txt"
    And wait for xpath "add_to_cart_txt.format(1)" for validation with timeout "10"
    When I add first "3" items to cart
    Then Validate value "$ 50.05" of "str" from xpath "fetch_total_amount"
    And wait for xpath "remove_item_cart" for validation with timeout "10"
    And I clear "3" items from cart
    Then Validate value "$ 0.00" of "str" from xpath "fetch_total_amount"
    And close browser

  @btassignment_03_Test2
  Scenario: Verify user is able to place order
    Given launch browser and open "website_url_txt"
    And wait for xpath "add_to_cart_txt.format(1)" for validation with timeout "10"
    When I add first "3" items to cart
    And wait for xpath "checkout_btn_txt" for validation with timeout "10"
    Then I Click "checkout button" with xpath "checkout_btn_txt"
    Then I verify "$ 50.05" is correct in alert message
    And close browser
