## 0x00 FNT
**渔网工具集第一个工具**

## 0x01 Google Hacking
![](http://10.0.36.99/server/index.php?s=/api/attachment/visitFile/sign/ede8ef7f37048e6ab311dd3275dfc9d1&showdoc=.jpg)

基于GoogleSearch的谷歌发现工具

## 0x02 功能介绍
![](http://10.0.36.99/server/index.php?s=/api/attachment/visitFile/sign/7d7a7f30a1f9bdf9fad5fabb494b0e01&showdoc=.jpg)

- file
	- 公开披露的文件
	- 目录列表漏洞
	- 暴露的配置文件
	- 暴露的数据库文件
	- 暴露的日志文件
	- 备份和旧文件
- info
	- 登录页面
	- 注册页面
	- phpinfo（）
- error
	- SQL错误
	- PHP错误/警告
- pastebin
	- 搜索Pastebin.com网站/粘贴网站
- github
	- 搜索Github.com网站以及Gitlab.com网站
- stackoverflow
	- 搜索Stackoverflow.com网站

## 0x03 使用指南
#### 敏感文件探测
`python3 FntGoogleHack.py example.com -i `

#### 敏感信息全探测
`python3 FntGoogleHack.py example.com -i -f -e -g -p -s`
