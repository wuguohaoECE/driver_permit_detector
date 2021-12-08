# driver_permit_detector

This program is used to detect the vacancy of driver permit for duke student.
脚本可以实现刷permit和刷road test的功能，并在刷到时发邮件提醒。
新版更新会在cookie失效时发邮件提醒换cookie

### sender email configuration

代码中需要修改 mail_user, mail_pass, sender 三个变量实现发邮件提醒功能，具体方式参考下面链接
please refer to [使用python给自己邮箱发邮件](https://blog.csdn.net/weixin_40475396/article/details/78693408)

### cookie configuration

代码需要修改 cities_list 变量的值，来实现地点选择。想抢几个地点就搞几个cookie（推荐只放一个）
The detector rely on the the correctness of cookie, which means you need to copy the cookie from your browser. You can do it in the following instructions.

* go to [DMV](https://skiptheline.ncdot.gov/Webapp/WizardAppt/Unit) and click your favourate location.
* enter "F12". refresh the webpage and click "DateandTime" section. 其实就是chrome浏览器->开发者选项->network 中找到 DateandTime并刷新
* copy the cookie from the header to your python file. 将cookie复制到cities_list，比如将'a cookie'换成真正的cookie




### star star star

please


### 各位老板觉得好用的话可以给我打赏
[image](./weixin.jpg)
[image](./zhifubao.jpg)
