#-*-coding:utf-8-*-

#注意：请按照中文模板对照中文释义进行翻译
def Chinese():
    global home, home_go, home_welcome, \
        last_page, next_page, error1, error3, \
        error, error2, sen_end, language, setting, lists, \
            error4,software_name,error5
    home = '阅读器主页'
    software_name = '阅读器'
    home_go = '选择文件（仅支持txt）'
    home_welcome = '欢迎使用基于tkinter制作的阅读器。中文原生语言包由 whtry陈 制作。'
    last_page = '上一页'
    next_page = '下一页'
    error1 = '请重新启动软件 :( \n找不到根目录下的fonts.txt字体参数配置文件，已将字体默认为'
    error = '错误'
    error2 = '不能为空'
    error3 = '已经是第一页了！'
    error4 = '已经是最后一页了！'
    error5 = '当前语言不是中文，进行设置更改可能出现未知错误！'
    sen_end = '。'
    language = '语言'
    setting = '设置'
    lists = '目录'


# 尚未翻译全
def English():
    global home, last_page, \
        next_page, error, sen_end, \
            home_go,software_name
    Chinese()
    home = 'RS Home'
    home_go = 'choose'
    last_page = 'Last Page'
    next_page = 'Next Page'
    error = 'error'
    sen_end = '.'
    software_name = 'RS'
