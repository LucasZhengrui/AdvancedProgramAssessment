Feature: table1
"""
Confirm that we can visit the table1's page.
"""

Scenario: success for visiting table1
    Given I navigate to main page
    When I click the Chinese Animal link to table1 details
    Then I should see all of details from table1
