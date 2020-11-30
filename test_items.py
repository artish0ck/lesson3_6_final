# import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_basket_button(browser_with_language):
    browser_with_language.get(link)
    # time.sleep(30)
    button_basket = browser_with_language.find_element_by_class_name("btn-add-to-basket")
    assert button_basket, "Button not found"
