*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  Graham 
    Set Password  Chappyman
    Set Password Confirmation  Chappyman
    Click  button >> text=Register
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  g 
    Set Password  Chappyman
    Set Password Confirmation  Chappyman
    Click  button >> text=Register
    Register Should Fail With Message  Username must be at least 4 characters long

Register With Valid Username And Too Short Password
    Set Username  Graham
    Set Password  C
    Set Password Confirmation  C
    Click  button >> text=Register
    Register Should Fail With Message  Password must be at least 8 characters long

Register With Username That Is Already In Use
    Set Username  kalle
    Set Password  Chappyman
    Set Password Confirmation  Chappyman
    Click  button >> text=Register
    Register Should Fail With Message  User with username kalle already exists

*** Keywords ***
Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Get Text  body  *=  ${message}

Set Username
    [Arguments]  ${username}
    Fill Text  id=username  ${username}

Set Password
    [Arguments]  ${password}
    Fill Secret  id=password  $password

Set Password Confirmation
    [Arguments]  ${password}
    Fill Secret  id=password_confirmation  $password

Reset Application Create User And Go To Register Page
    Reset Application
    Create User  kalle  kalle123
    Go To Register Page