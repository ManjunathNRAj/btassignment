@btassignment_filter_validation
Feature: British Telecom Assignment for checking demo website [ https://react-shopping-cart-67954.firebaseapp.com/ ]

  @btassignment_01_Test1
  Scenario Outline: Verify user is able to filter items using different size filters XS, S, M, etc
    Given launch browser and open "website_url_txt"
    And wait for xpath "size_txt" for validation with timeout "10"
    When I Click "<size>" with xpath "<size_xpath>"
    And wait for xpath "fetch_item_name_filed" for validation with timeout "10"
    Then I verify "<item_count>" for selected size
    And close browser

  Examples:
    | size   |  size_xpath  | item_count  |
    | XS     |  size_xs_txt | 1           |
    | S      |  size_s_txt  | 2           |
    | M      |  size_m_txt  | 1           |

  @btassignment_01_Test2
  Scenario Outline: Verify user is able to apply multiple filters (S, M) at once and can see the results as expected,
    - Apply filter S,M separately and then apply both filters S, M at the same time - verify the results are correct
    Given launch browser and open "website_url_txt"
    And wait for xpath "size_txt" for validation with timeout "10"
    When I Click "<size>" with xpath "<size_xpath>"
    Then I verify "<item_count>" for selected size
    And I Click "additional size" with xpath "<add_size_xpath>"
    Then I verify list "size_s_m_list" for selected size
    And close browser

  Examples:
    | size   |  size_xpath  | item_count  | add_size_xpath  |
    | S      |  size_s_txt  | 2           | size_m_txt      |
    | M      |  size_m_txt  | 1           | size_s_txt      |
