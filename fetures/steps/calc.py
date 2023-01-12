from behave import *

from src.calc import Somator, Subtractor, Multiplier, Divider


@given("that the user inserted {operator1}")
def step_impl(context, operator1):
    context.op1 = int(operator1)


@step("that also inserted {operator2}")
def step_impl(context, operator2):
    context.op2 = int(operator2)


@when("the user run the sum operation")
def step_impl(context):
    somator = Somator()
    context.result = somator.sum(context.op1, context.op2)


@when("the user run the sub operation")
def step_impl(context):
    subtractor = Subtractor()
    context.result = subtractor.sub(context.op1, context.op2)


@when("the user run the mult operation")
def step_impl(context):
    multiplier = Multiplier()
    context.result = multiplier.mult(context.op1, context.op2)


@when("the user run the div operation")
def step_impl(context):
    divider = Divider()
    context.result = divider.div(context.op1, context.op2)


@then("the result shall be {result}")
def step_impl(context, result):
    context.result = int(result)
