## 0x01 FNT-GH
> 渔网工具集第一个工具

**基于GoogleSearch的谷歌发现工具：**[FNT-GH](https://github.com/austfish/FNT-GH "FNT-GH")
是一款针对资产列表的快速敏感信息收集工具，通过调用Google配合敏感信息的语法集合，快速查询资产信息并检索相关泄露的文件、页面、错误提示、github、Pastebin、stackoverflow等网站泄露信息。

## 0x02 Google Hacking
Google Hack是google提供的搜索语法，如果熟练掌握，我们可以搜到许多意想不到的东西!

**googlesearch**是一个Python库，可轻松爬取Google搜索结果。googlesearch使用requests和
BeautifulSoup4抓取Google，[详细介绍地址](https://www.xugj520.cn/archives/googlesearch.html "详细介绍地址")。


**googlehack 常用语法**
- site       指定域名
- intext   正文中存在关键字的网页
- intitle   标题中存在关键字的网页
- info      一些基本信息
- inurl    URL存在关键字的网页
- filetype 搜索指定文件类型
![image](https://github.com/austfish/FNT-GH/blob/main/images/banner.png)

### 0x03 功能介绍
![image](https://github.com/austfish/FNT-GH/blob/main/images/run.png)
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

### 0x04 使用指南
#### 敏感文件探测
`python3 FntGoogleHack.py example.com -i `

#### 敏感信息全探测
`python3 FntGoogleHack.py example.com -i -f -e -g -p -s`
