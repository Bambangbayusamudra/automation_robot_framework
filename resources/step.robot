*** Settings ***
Library    SeleniumLibrary
Library    BuiltIn
Variables   variable.py
# Library    SeleniumLibrary    selenium_log_level=INFO

# *** Variables ***
# ${url}         https://google.com
# ${url_demo}    https://demoqa.com/text-box

*** Keywords ***
Input text in field Name
    #demoQA
    # Open Browser    ${url_demo}    ${browser}
    Open Browser    about:blank    browser=chrome    options=add_argument("--incognito")
    Go To 	 ${url_demo}
    Maximize Browser Window
    input Text      ${text}    uno
    input Text      ${email}    test@gmail.com
    input Text      ${currentadd}    yahhaha testing
    input Text      ${permanentadd}    permanent testing
    Click Element 	${submitinp}
    # sleep   2s
Checkbox
    Click Element 	${checkbox} 
    Click Element 	${selectcekbox}
    # Sleep  2s   
    Wait Until Element Is Visible 	${selectcekbox}	
Radio button 
    Click Element 	 ${radiobutt}
    Click Element 	 ${selectradio}
    # Sleep   1s
    Click Element 	 ${selectradio2}
    # sleep   4s
Web tables
    Click Element   ${webtbl}
    Click Element   ${buttadd}
    Input Text      ${inptex}   coba testing 
    Input Text      ${lasttex}   yahaha hayyukk  
    Input Text      ${email1}   yahahahayyukk@gmail.com  
    Input Text      ${age}   20  
    Input Text      ${salary}   20  
    Input Text      ${departemen}   CGW 
    Click Element 	${submitinp} 
    # sleep   30s
    Input Text      ${inpBox}   CGW 
    ${text}=    Get Text    xpath=//div[@class="rt-tbody"]
    Log To Console  ${text}
    sleep   1s
    Click Element 	 ${edit}
    Input Text      ${inptex}   coba testing update 
    Input Text      ${lasttex}   yahaha hayyukk  update
    Input Text      ${email1}   yahahahayyukkupdate@gmail.com  
    Input Text      ${age}   30  
    Input Text      ${salary}   20  
    Input Text      ${departemen}   Quality 
    Click Element 	${submitinp} 
    Input Text      ${inpBox}   Quality 
    sleep   3s
    Click Element 	${delete} 
    sleep   3s
Page Buttons
    #Clear Chache
    # Execute JavaScript    location.reload(true)
    # Execute JavaScript    window.localStorage.clear()
    # Execute JavaScript    window.sessionStorage.clear()
    # sleep   2s
    
    Click Element   ${pagebutton}
    Doubleclick Element 	 ${doubleklik}	 	 
    Click Element 	 (//div[button[text()='Click Me']]//button[@class="btn btn-primary"])[1]
    sleep   3s
Page Link
    Click Element   ${pagelink}
    ${new_tab_window} = Click Element 	${home}
    Log To Console ${new_tab_window.title}
    # Switch Window  ${main_window}
    # Close Window  ${new_tab_window}
    sleep   2s
    