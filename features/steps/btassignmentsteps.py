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
    '''
    Function to launch chrome browser and load url
    :param context: behave context variable to get data from feature file
    :param website: parameter to specify url to open in chrome browser
    :return: selenium object
    '''
    try:
        website_url = eval(website)
        service = Service(executable_path=f"{base_folder_path}drivers\chromedriver.exe")
        options = webdriver.ChromeOptions()

        # open chrome in maximized mode
        options.add_argument("--start-maximized")
        context.driver = webdriver.Chrome(service=service, options=options)

        # open website url
        context.driver.get(website_url)

    except Exception as error:
        assert False, f"Error occured: {error}"


@step('wait for xpath "{element_xpath}" for validation with timeout "{timeout}"')
def wait_for_xpath(context, element_xpath, timeout="10"):
    '''
    Function to wait from element in website opened
    :param context: behave context variable to get data from feature file
    :param element_xpath: xpath of element to wait to get displayed
    :param timeout: timeout in seconds to wait for element to appear
    '''
    try:
        element_xpath = eval(element_xpath)
        WebDriverWait(context.driver, int(timeout)).until(EC.element_to_be_clickable((By.XPATH, element_xpath)))

    except Exception as error:
        assert False, f"Error occured: {error}"

@step('I check if element "{element_name}" with xpath "{element_xpath}" is displayed')
def verify_load_url(context, element_name, element_xpath):
    '''
    Function to check if element is displayed in website opened
    :param context: behave context variable to get data from feature file
    :param element_name: Name of element or string data representing element name
    :param element_xpath: xpath of element to wait to get displayed
    :return: True/False
    '''
    try:
        element_xpath = eval(element_xpath)
        print(f"Validating {element_name} is present")
        status = context.driver.find_element(By.XPATH, element_xpath).is_displayed()
        assert status is True
    except Exception as error:
        assert False, f"Error occured: {error}"


@step('I Click "{element_name}" with xpath "{element_xpath}"')
def click_xpath(context, element_name, element_xpath):
    '''
    Function to click element present in website opened
    :param context: behave context variable to get data from feature file
    :param element_name: Name of element or string data representing element name
    :param element_xpath: xpath of element to wait to click
    '''
    try:
        element_xpath = eval(element_xpath)
        print(f"Clicking on element {element_name} with {element_xpath}")
        context.driver.find_element(By.XPATH, element_xpath).click()
        context.driver.implicitly_wait(5)

    except Exception as error:
        assert False, f"Error occured 111: {error}"


@step('Validate value "{val_string}" of "{val_datatype}" from xpath "{fetch_elements_xpath}"')
def validate_fetch_list(context, val_datatype, val_string, fetch_elements_xpath):
    '''
    Function to validate text of specified datatype for xpath specified
    :param context: behave context variable to get data from feature file
    :param val_datatype: datatype of text to compare and validate
    :param val_string: string value to validate against result value
    :param fetch_elements_xpath: xpath of element to fetch data
    :return: True/False
    '''
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
    '''
    Function to validate list data with list fetched from xpath elements
    :param context: behave context variable to get data from feature file
    :param val_list: list value to validate against result value
    :param fetch_elements_xpath: xpath of elements to fetch data
    :return: True/False
    '''
    try:
        result_list = []
        fetch_elements_xpath = eval(fetch_elements_xpath)
        print(f"Validate string {val_list} with xpath {fetch_elements_xpath}")
        text_data_list = context.driver.find_elements(By.XPATH, fetch_elements_xpath)

        # get text from selenium object and save in list
        for text_data in text_data_list:
            result_list.append(text_data.text)

        status = True if val_list.sort()==result_list.sort() else False
        assert status

    except Exception as error:
        assert False, f"Error occured: {error}"

@step('I verify "{item_count}" for selected size')
def verify_size_item(context,item_count):
    '''
    Function to verify number of items for selected size items
    :param context: behave context variable to get data from feature file
    :param item_count: number of items count in "int" format
    :return: True/False
    '''
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
    '''
    Function to verify list of items for selected size in website
    :param context: behave context variable to get data from feature file
    :param selected_items: list of items to validate against fetched list from website
    :return: True/False
    '''
    try:
        output_list = []
        selected_items = eval(selected_items)

        print(f"Validating item count {selected_items}")

        # context.driver.implicitly_wait(5)
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
    '''
    Function to add n number of items in serial order
    :param context: behave context variable to get data from feature file
    :param select_no_of_items: number of items to select in website in "int" format
    '''
    try:
        total_items = int(select_no_of_items)
        for item_num in range(1,(total_items+1)):
            sleep(2)
            context.driver.find_element(By.XPATH, add_to_cart_txt.format(item_num)).click()

    except Exception as error:
        assert False, f"Error occured: {error}"

@step(u'I clear "{select_no_of_items}" items from cart')
def remove_no_of_items_cart(context,select_no_of_items):
    '''
    Function to remove n number of items from cart
    :param context: behave context variable to get data from feature file
    :param select_no_of_items: number of items to remove from cart in website in "int" format
    '''
    try:
        print(f"Remove {select_no_of_items} items from cart")
        for item_num in range(0,int(select_no_of_items)):
            sleep(2)
            context.driver.find_element(By.XPATH, remove_item_cart).click()

    except Exception as error:
        assert False, f"Error occured: {error}"

@step(u'I verify "{total_amount}" is correct in alert message')
def verfiy_alert(context,total_amount):
    '''
    Function to verify alert data from alert message in website after checkout
    :param context: behave context variable to get data from feature file
    :param total_amount: items price in alert message to validate
    :return: True/False
    '''
    try:
        sleep(2)
        # create alert message object
        alert_obj = context.driver.switch_to.alert
        alert_txt = alert_obj.text
        print(f"Ouptput from alert: {alert_txt}")
        sleep(2)
        status = True if (total_amount in alert_txt) else False

        #press accept in alert
        alert_obj.accept()
        assert status

    except Exception as error:
        assert False, f"Error occured: {error}"

@step(u'I verify items list "{item_list}" added in checkout panel')
def verify_checkout_item(context,item_list):
    '''
    Function to verify list of items added in check panel
    :param context: behave context variable to get data from feature file
    :param item_list: list of items to verify against fetch list of items in checkout items
    :return: True/False
    '''
    try:
        output_list = []
        selected_items = eval(item_list)

        print(f"Validating item count {selected_items}")

        # context.driver.implicitly_wait(5)
        sleep(5)

        # validate items listed
        return_text_data = context.driver.find_elements(By.XPATH, fetch_checkout_item_list)
        for text_data in return_text_data:
            output_list.append(text_data.text)

        print(f"Output after selecting size: {output_list}")
        status = True if (selected_items == output_list) else False
        assert status

    except Exception as error:
        assert False, f"Error occured: {error}"

@step(u'close browser')
def close_browser(context):
    '''
    Function to close Chrome browser
    :param context: behave context variable to get data from feature file
    '''
    try:
        sleep(5)
        context.driver.close()

    except Exception as error:
        assert False, f"Error occured: {error}"

if __name__ == "__main__":
    pass
