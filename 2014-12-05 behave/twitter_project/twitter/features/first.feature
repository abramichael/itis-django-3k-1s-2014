Feature: First feature of project
  
  Scenario Outline: anonimous user have access to login page
    Given an anonimous user
	Then he has access to <page>/
	
  Examples: urls
  |page			  |
  |/twitter/login |
  |/analytics	  |

  Scenario: logging in user
    Given a new user
     When he is logged in
     Then he has access to /twitter/