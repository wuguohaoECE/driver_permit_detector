# driver_permit_detector

This program is used to detect the vacancy of driver permit for duke student.

### sender email configuration

please refer to [使用python给自己邮箱发邮件](https://blog.csdn.net/weixin_40475396/article/details/78693408)

### cookie configuration

The detector rely on the the correctness of cookie, which means you need to copy the cookie from your browser. You can do it in the following instructions.

* go to [DMV](https://skiptheline.ncdot.gov/Webapp/WizardAppt/Unit) and click your favourate location.
* enter "F12". refresh the webpage and click "DateandTime" section. 
* copy the cookie from the header to your python file.


### future work

The cookie is likely to expire when detecing, crashing the program. It is possible to add an reminder via email before the program crash.


### star star star

please