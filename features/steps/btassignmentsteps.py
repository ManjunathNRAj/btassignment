import os
import sys
import logging
from behave import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep
base_folder_path = (os.path.realpath(".").split("features"))[0]
sys.path.append(base_folder_path)
from xpaths.btassignment_xpaths import *


@step('launch browser and open "{website}"')
def launch_browser(context, website):
    try:
        website_url = eval(website)
        service = Service(executable_path=f"{base_folder_path}drivers\chromedriver.exe")
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        context.driver = webdriver.Chrome(service=service, options=options)
        context.driver.get(website_url)
        context.driver.refresh()

    except Exception as error:
        assert False, f"Error occured: {error}"


@step('wait for xpath "{element_xpath}" for validation with timeout "{timeout}"')
def wait_for_xpath(context, element_xpath, timeout="10"):
    try:
        element_xpath = eval(element_xpath)
        WebDriverWait(context.driver, int(timeout)).until(EC.element_to_be_clickable((By.XPATH, element_xpath)))

    except Exception as error:
        assert False, f"Error occured: {error}"


@step('I check if element "{element_name}" with xpath "{element_xpath}" is displayed')
def verify_load_url(context, element_name, element_xpath):
    try:
        element_xpath = eval(element_xpath)
        print(f"=======Validating {element_name} is present")
        logging.info(f"Validating {element_name} is present")
        status = context.driver.find_element(By.XPATH, element_xpath).is_displayed()
        assert status is True
    except Exception as error:
        assert False, f"Error occured: {error}"


@step('I Click "{element_name}" with xpath "{element_xpath}"')
def click_xpath(context, element_name, element_xpath):
    try:
        element_xpath = eval(element_xpath)
        print(f"Clicking on element {element_name} with {element_xpath}")
        context.driver.find_element(By.XPATH, element_xpath).click()
        context.driver.implicitly_wait(5)

    except Exception as error:
        assert False, f"Error occured 111: {error}"


@step('Validate value "{val_string}" of "{val_datatype}" from xpath "{fetch_elements_xpath}"')
def validate_fetch_list(context, val_datatype, val_string, fetch_elements_xpath):
    try:
        fetch_elements_xpath = eval(fetch_elements_xpath)
        print(f"Validate value {val_string} with xpath {fetch_elements_xpath}")
        sleep(5)
        output_value = context.driver.find_element(By.XPATH, fetch_elements_xpath).text
        if str(val_datatype) == "str":
            status = True if (str(output_value) == str(val_string)) else False
        elif str(val_datatype) == "int":
            status = True if (int(output_value) == int(val_string)) else False
        assert status
    except Exception as error:
        assert False, f"Error occured: {error}"


@step('Validate list "{val_list}" from xpath "{fetch_elements_xpath}"')
def validate_fetch_list(context, val_list, fetch_elements_xpath):
    try:
        fetch_elements_xpath = eval(fetch_elements_xpath)
        print(f"Validate string {val_list} with xpath {fetch_elements_xpath}")
        text_data = context.driver.find_elements(By.XPATH, fetch_elements_xpath).text()
    except Exception as error:
        assert False, f"Error occured: {error}"

@step('I verify "{item_count}" for selected size')
def verify_size_item(context,item_count):
    try:
        output_list = []
        item_count = eval(item_count)

        print(f"Validating item count {item_count}")

        context.driver.implicitly_wait(5)
        sleep(5)

        # validate items listed
        return_text_data = context.driver.find_elements(By.XPATH, fetch_item_name_filed)
        for text_data in return_text_data:
            output_list.append(text_data.text)
        print(f"Output after selecting size: {output_list}")
        status = True if len(output_list) == int(item_count) else False
        assert status

    except Exception as error:
        assert False, f"Error occured: {error}"

@step('I verify list "{selected_items}" for selected size')
def verify_size_item(context,selected_items):
    try:
        output_list = []
        selected_items = eval(selected_items)

        print(f"Validating item count {selected_items}")

        context.driver.implicitly_wait(5)
        sleep(5)

        # validate items listed
        return_text_data = context.driver.find_elements(By.XPATH, fetch_item_name_filed)
        for text_data in return_text_data:
            output_list.append(text_data.text)

        print(f"Output after selecting size: {output_list}")
        status = True if (selected_items.sort() == output_list.sort()) else False
        assert status

    except Exception as error:
        assert False, f"Error occured: {error}"

@step(u'I add first "{select_no_of_items}" items to cart')
def add_no_of_items_cart(context,select_no_of_items):
    try:
        total_items = int(select_no_of_items)
        for item_num in range(1,(total_items+1)):
            sleep(2)
            context.driver.find_element(By.XPATH, add_to_cart_txt.format(item_num)).click()

    except Exception as error:
        assert False, f"Error occured: {error}"

@step(u'I clear "{select_no_of_items}" items from cart')
def remove_no_of_items_cart(context,select_no_of_items):
    try:
        print(f"Remove {select_no_of_items} items from cart")
        for item_num in range(0,int(select_no_of_items)):
            sleep(2)
            context.driver.find_element(By.XPATH, remove_item_cart).click()

    except Exception as error:
        assert False, f"Error occured: {error}"

@step(u'I verify "{total_amount}" is correct in alert message')
def verfiy_alert(context,total_amount):
    try:
        sleep(2)
        alert_obj = context.driver.switch_to.alert
        alert_txt = alert_obj.text
        print(f"Ouptput from alert: {alert_txt}")
        sleep(2)
        status = True if (total_amount in alert_txt) else False
        assert status

    except Exception as error:
        assert False, f"Error occured: {error}"


@step(u'close browser')
def close_browser(context):
    try:
        sleep(5)
        context.driver.close()

    except Exception as error:
        assert False, f"Error occured: {error}"


if __name__ == "__main__":
    # launch_browser()
    pass
