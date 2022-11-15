*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Create User And Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
    Set Username  sammu
    Set Password  sammu123
    Set Password Confirmation  sammu123
    Submit Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  sa
    Set Password  sammu123
    Set Password Confirmation  sammu123
    Submit Credentials
    Register Should Fail With Message  Username too short

Register With Valid Username And Too Short Password
    Set Username  sammu
    Set Password  sammu12
    Set Password Confirmation  sammu12
    Submit Credentials
    Register Should Fail With Message  Password too short

Register With Nonmatching Password And Password Confirmation
    Set Username  sammu
    Set Password  sammu123
    Set Password Confirmation  sammu12
    Submit Credentials
    Register Should Fail With Message  Passwords do not match

Login After Successful Registration
    Go To Login Page
    Set Username  kalle
    Set Password  kalle123
    Submit Login Credentials
    Login Should Succeed

Login After Failed Registration
    Set Username  sa
    Set Password  sammu123
    Set Password Confirmation  sammu123
    Submit Credentials
    Go To Login Page
    Set Username  sa
    Set Password  sammu123
    Submit Login Credentials
    Login Should Fail With Message  Invalid username or password

*** Keywords ***
Register Should Succeed
    Welcome Page Should Be Open

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password_confirmation}
    Input Password  password_confirmation  ${password_confirmation}

Submit Credentials
    Click Button  Register

Submit Login Credentials
    Click Button  Login

Create User And Go To Register Page
    Create User  kalle  kalle123
    Go To Register Page
    Register Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}

Login Should Succeed
    Main Page Should Be Open