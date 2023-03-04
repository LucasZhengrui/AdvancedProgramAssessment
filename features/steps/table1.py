from behave import given, when, then

@given(u'I navigate to main page')
def nav(content):
    """
    Navigate to main page
    """
    content.browser.get('https://human-animal-b0nh.onrender.com/')

@when(u'I click the Chinese Animal link to table1 details')
def click(content):
    """
    Find the link
    """
    content.browser.find_element_by_partial_link_text('Chinese Animal').click()

@then(u'I should see all of details from table1')
def details(content):
    """
    Successful, can visit data
    """
    print(content.browser.page_source)
    assert content.browser.current_url == "https://human-animal-b0nh.onrender.com/table1"
    assert '1 China 1733 elephant Male Tongan' in content.browser.page_source