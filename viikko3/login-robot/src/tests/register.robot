*** Settings ***
Resource  resource.robot
Test Setup  Create User And Input New Command

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  sammu  sammu123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  kalle  kalle123
    Output Should Contain  Username taken

Register With Too Short Username And Valid Password
    Input Credentials  sa  sammu123
    Output Should Contain  Username too short

Register With Valid Username And Too Short Password
    Input Credentials  sammu  sammu12
    Output Should Contain  Password too short

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  sammu  sammuuuuu
    Output Should Contain  Password consists of only letters

*** Keywords ***

Create User And Input New Command
    Create User  kalle  kalle123
    Input New Command