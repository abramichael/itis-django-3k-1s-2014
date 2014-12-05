from behave import *
from game import Game

@Given("a new game")
def step_impl(context):
    context.game = Game()
	
@then("it should have 2 players")
def step_impl(context):
	assert hasattr(context.game, "player1")
	assert hasattr(context.game, "player2")
	assert context.game.player1 is not None
	assert context.game.player1 is not None
