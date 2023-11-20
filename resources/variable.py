url_demo=    'https://demoqa.com/text-box'
browser=    'chrome'
text= 'id=userName'
email= 'id=userEmail'
currentadd= 'id=currentAddress'
permanentadd= 'id=permanentAddress'
submitinp= 'id=submit'

#checkbox

checkbox= 'id=item-1'
selectcekbox= 'xpath=//label[@for="tree-node-home"]//span[@class="rct-checkbox"]'

#radio button
radiobutt= 'id=item-2'
selectradio= 'xpath=//label[@for="yesRadio"]'
selectradio2= 'xpath=//label[@for="impressiveRadio"]'

#web table
webtbl= 'id=item-3'
buttadd= 'id=addNewRecordButton'
inptex ='id=firstName'
lasttex ='id=lastName'
email1 ='id=userEmail'
age ='age'
salary ='salary'
departemen ='department'
inpBox= 'xpath=//*[@id="searchBox"]'
edit= 'xpath=//div[@class="rt-tr -odd"]//div[@class="rt-td"]//div[@class="action-buttons"]//span[@data-toggle="tooltip"]'
delete= 'xpath=//div[@class="rt-tr -odd"]//div[@class="rt-td"]//div[@class="action-buttons"]//span[@id="delete-record-4"]'

#page buttons
pagebutton= 'id=item-4'
doubleklik= 'id=doubleClickBtn'

#page link
pagelink= 'xpath=//*[@id="item-5"]'
home='xpath=//*[@id="simpleLink"]'

# cara id dinamis 
# //p[@class='checkout-dialog-text-a']/../div/div/a[.='Nanti']
#  xpath=(//tr[td[text()='${new_create_division_save}']]//button[@class="btn btn-action d-flex text-white justify-content-center"])[1]

#web sulusi button dinamis
# https://forum.robotframework.org/t/how-to-handle-button-on-the-dynamic-body/4410
# https://stackoverflow.com/questions/70836692/how-to-locate-an-id-of-the-button-to-click-when-id-is-dynamic-in-robot-framework
