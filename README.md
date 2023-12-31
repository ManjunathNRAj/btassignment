Project btassignment is tested using BDD behave framework with selenium for testing demo website:
 https://react-shopping-cart-67954.firebaseapp.com/

# Required Pre-requisites :
1. Install python on windows platform.
2. Add python path to environment variables system variables path
3. Install selenium [command: pip install -U selenium]
4. Install behave [command: "pip install behave"]
5. Install allure-behave [command: "pip install allure-behave"]
5. Clone code from: 
6. Copy btassignment to c:\ folder 
7. Open command prompt and cwd to c:\btassignment\features [command: "cd c:\btassignment\features\" ]

# How to Run Testscenarios :

Below are the test scenarios proposed and command to run from cmd prompt:

Note: change working directory to "c:\btassignment\features\". [command: cd c:\btassignment\features\]

## 1. Feature : Filter validations [ feature file name: btassignment_filter_validation.feature ]
### command to run feature file in cmd: behave --no-capture --tags @btassignment_filter_validation
- Test 1: Verify user is able to filter items using different size filters XS, S, M, etc. and can see the results as expected

#### command to run test scenario 1 in cmd: "behave --no-capture --tags @btassignment_01_Test1" 
 

Test 2: Verify user is able to apply multiple filters (S, M) at once and can see the results as expected. 
- Apply filter S,M separately and then apply both filters S, M at the same time - verify the results are correct

#### command to run test scenario 2 in cmd: "behave --no-capture --tags @btassignment_01_Test2"  

## 2. Feature : Add items to cart feature [Feature file name: btassignment_add_items_to_cart.feature ]
### command to run feature file in cmd: behave --no-capture --tags @btassignment_add_items_to_cart
Test 1: Verify items are listed in cart in the order as added to cart with price

- Add random 4 items with free shipping (items labelled as Free shipping)

- Add 1 item without free shipping (items without Free shipping label)

- Verify the order of items in cart and the price

#### command to run test scenario 1 in cmd: "behave --no-capture --tags @btassignment_02_Test1" 

Test2: Verify user is able to add same items as desired

- Add a same item one or more times using ‘Add to cart’ button and verify the count & price is increased in cart accordingly

- Add an item which is already present in the cart using ‘+’ button and verify the count & price is increased in cart accordingly

#### command to run test scenario 2 in cmd: "behave --no-capture --tags @btassignment_02_Test2"  

## 3. Feature : Update and checkout to complete order feature [Feature file name: btassignment_update_checkout.feature ]
### command to run feature file in cmd: behave --no-capture --tags @btassignment_update_checkout
Test 1: Verify user can delete items in cart

- Add few items to cart and verify the total count and price is displayed correctly

- Clear all items in cart and verify price & count is reset to 0

 #### command to run test scenario 1 in cmd: "behave --no-capture --tags @btassignment_03_Test1"  

Test 2: Verify user is able to place order

- Add few items to cart and click on “checkout” and verify alert message is displayed with correct price same as cart

- Verify items in cart is reset on refreshing the page

#### command to run test scenario 2 in cmd: "behave --no-capture --tags @btassignment_03_Test2"  


# Generate Report :
Note: change working directory to "c:\btassignment\features\". [command: cd c:\btassignment\features\]

## 1. Generate report for all features

#### command to generate json report library in cmd: "behave -f allure_behave.formatter:AllureFormatter -o reports"

## 2. Generate report for one feature file

#### command to generate json report library in cmd: "behave -f allure_behave.formatter:AllureFormatter -o reports feature_file_name.feature"
