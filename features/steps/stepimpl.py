import requests
from behave import *


#from features.payLoad import addBookPayload


def getConfig():
    pass


class ApiResources:
    pass


@given('the Book details which needs to be added to Library')
def step_impl(context):
    #context.url = getConfig()['API']['endpoint'] + ApiResources.addBook
    #context.headers = {"Content-Type": "application/json"}
    #context.payLoad = addBookPayload("manfdfppt","4373")
    pass


@when('we execute the AddBook PostAPI method')
def step_impl(context):
    #context.response = requests.post(context.url, json=context.payLoad , headers=context.headers, )
    pass

@then('book is successfully added')
def step_impl(context):
    #print(context.response.json())
    #response_json = context.response.json()
    #context.bookId = response_json['ID']
    #print(context.bookId)
    #assert response_json["Msg"] == "successfully added"
    pass

@given('the Book details with {isbn} and {aisle}')
def step_impl(context,isbn,aisle):
    context.url = getConfig()['API']['endpoint'] + ApiResources.addBook
    context.headers = {"Content-Type": "application/json"}
    context.payLoad = addBookPayload(isbn, aisle);


@given('I have github auth credentials')
def step_impl(context):

    context.se = requests.session()
    context.se.auth = auth = ('rahulshettyacademy', getPassword())


@when(u'I hit getRepo API of github')
def step_impl(context):
    context.response = context.se.get(ApiResources.githubRepo)


@then(u'status code of response should be {statusCode:d}')
def step_impl(context,statusCode):
    print(context.response.status_code)
    assert context.response.status_code == statusCode






