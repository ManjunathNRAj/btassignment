from behave import *

def before_step(context,step):
    context.step_name = step.name