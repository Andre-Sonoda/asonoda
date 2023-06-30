Feature: Teste Site Advantage

  Scenario: Test
    Given I ON THE <SITE>
    When  I click on the top menu magnifying glass
    And   I type <PRODUTO>
    And   press search/enter
    Then  the product page is displayed
