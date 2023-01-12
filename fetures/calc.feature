# Created by Paulo at 12/01/2023
Feature: Calculator
  Will receive two natural numbers by the user and operate them

  Scenario Outline: Sum two numbers inserted by the user
    Receive two numbers from the user and sum them
    Given that the user inserted <operator1>
    And that also inserted <operator2>
    When the user run the sum operation
    Then the result shall be <result>

    Examples:
      | operator1 | operator2 | result    |
      | 10        | 20        | 30        |
      | 3         | 4         | 7         |

  Scenario Outline: Subtract two numbers inserted by the user
    Receive two numbers from the user and subtract them
    Given that the user inserted <operator1>
    And that also inserted <operator2>
    When the user run the sub operation
    Then the result shall be <result>

    Examples:
      | operator1 | operator2 | result    |
      | 20        | 10        | 10        |
      | 5         | 4         | 1         |

  Scenario Outline: Multiply two numbers inserted by the user
    Receive two numbers from the user and multiply them
    Given that the user inserted <operator1>
    And that also inserted <operator2>
    When the user run the mult operation
    Then the result shall be <result>

    Examples:
      | operator1 | operator2 | result    |
      | 20        | 10        | 200       |
      | 5         | 7         | 35        |

  Scenario Outline: Divide two numbers inserted by the user
    Receive two numbers from the user and divide them
    Given that the user inserted <operator1>
    And that also inserted <operator2>
    When the user run the div operation
    Then the result shall be <result>

    Examples:
      | operator1 | operator2 | result    |
      | 20        | 10        | 200       |
      | 5         | 7         | 35        |
