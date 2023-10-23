website_url_txt = "https://react-shopping-cart-67954.firebaseapp.com/"
size_s_m_list = ['Black Tule Oversized', 'Black Batman T-shirt', 'Blue Sweatshirt']
checkout_items_list = ['Cropped Stay Groovy off white', 'Basic Cactus White T-shirt', 'Skater Black Sweatshirt', 'Black Batman T-shirt']
size_txt = "//*[text()='Sizes:']"
size_xs_txt = "//*[text() = 'XS']"
size_s_txt = "//*[text() = 'S']"
size_m_txt = "//*[text() = 'M']"
fetch_item_name_filed = '//*[@class="sc-uhudcz-0 iZZGui"]/div/p'
fetch_checkout_item_list = "//p[@class='sc-11uohgb-2 elbkhN']"
fetch_no_of_items_cart = "//div[@class='sc-1h98xa9-3 VLMSP']"
add_to_cart_txt = "(//*[contains(text(),'Add to cart')])[{}]"
increase_item_no_checkout = "//button[@class='sc-11uohgb-6 cgtUCJ' and text()='+']"
remove_item_cart = '//button[@title="remove product from cart"]'
fetch_total_amount = '//p[@class="sc-1h98xa9-9 jzywDV"]'
checkout_btn_txt = "//button[text()='Checkout']"
