*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
    Set Username  mertsikka
    Set Password  ValidPass123
    Set Password Confirmation  ValidPass123
    Click Button  Register
    Registration Should Succeed

Register With Too Short Username And Valid Password
    Set Username  me
    Set Password  ValidPass123
    Set Password Confirmation  ValidPass123
    Click Button  Register
    Registration Should Fail With Message  Username too short

Register With Valid Username And Too Short Password
    Set Username  mertsikka2
    Set Password  V1a
    Set Password Confirmation  V1a
    Click Button  Register
    Registration Should Fail With Message  Password too short

Register With Valid Username And Invalid Password
    Set Username  mertsikka3
    Set Password  password
    Set Password Confirmation  password
    Click Button  Register
    Registration Should Fail With Message  Password should contain at least one number

Register With Nonmatching Password And Password Confirmation
    Set Username  mertsikka4
    Set Password  ValidPass123
    Set Password Confirmation  DifferentPass123
    Click Button  Register
    Registration Should Fail With Message  Password and password confirmation do not match

Register With Username That Is Already In Use
    Set Username  existinguser
    Set Password  ValidPass123
    Set Password Confirmation  ValidPass123
    Click Button  Register
    Registration Should Fail With Message  Username already taken

*** Keywords ***
Reset Application Create User And Go To Register Page
    Reset Application
    Create User  existinguser  ValidPass123
    Go To  ${REGISTER_URL}

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Text  password  ${password}

Set Password Confirmation
    [Arguments]  ${password_confirmation}
    Input Text  password_confirmation  ${password_confirmation}

Registration Should Fail With Message
    [Arguments]  ${message}
    Page Should Contain  ${message}

Registration Should Succeed
    Page Should Contain  Welcome to Ohtu Application!

