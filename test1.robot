*** Settings ***
Library    SeleniumLibrary
Library    BuiltIn
Resource    resources/step.robot

*** Test Cases ***
DemoQA input text
    Input text in field Name
    checkbox
    Radio button
    Web tables
    Page Buttons
    Page Link
    Close Browser
    