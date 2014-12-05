from behave import *
from player import Player

@Given("a new player")
def step(context):
	context.player = Player("player")

@then("it should have name")
def step(context):
	assert context.player.name is not None

@then("it should have hp = 100")
def step(context):
	assert context.player.hp is not None
	assert context.player.hp == 100


@Given("two players")
def step(context):
	context.player1 = Player("1")
	context.player2 = Player("2")

@when("first player kicks the second with power {d}")
def step(context, d):
	context.old_hp = context.player2.hp
	context.player1.kicks(context.player2, int(d))

@then("hp of second decreases on {d}")
def step(context, d):
	assert context.old_hp == context.player2.hp + int(d)

