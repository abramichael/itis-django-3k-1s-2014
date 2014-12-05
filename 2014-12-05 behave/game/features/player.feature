Feature: Player 

  Scenario: init parameters
    Given a new player
    then it should have name
    and it should have hp = 100

  Scenario Outline: kicking
    Given two players
    when first player kicks the second with power <power>
    then hp of second decreases on 20

  Examples: power_size
  |power 	|
  |10 		|
  |20 		|
  |30		|