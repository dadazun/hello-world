#coding:utf-8 
from pyecharts import options as opts
from pyecharts.charts import Page, WordCloud
from pyecharts.globals import SymbolType
from pyecharts.charts import Page, ThemeRiver
from collections import Counter
import string
def ciyun_en(movie_name):
	#读取数据
	filename=movie_name+'\\'+movie_name+'Dreview.txt'
	with open(filename,'r+',encoding='utf-8') as f:
		rev_1 = f.read()
		#处理标点
		for i in rev_1:
			if i in string.punctuation:
				rev_1=rev_1.replace(i," ")
		#分词+统计
		words=rev_1.split()
		words_dic=Counter(words)
	#删除一些高频词
	file_del='ban.txt'
	with open(file_del,'r+',encoding='utf-8') as d:
		del_1=d.read()
		Ban_list = del_1.split('\n')
	#处理数据
	words_list=[]
	for word,time in words_dic.items():
		if word.lower() in Ban_list or time < 35:
			continue
		else:
			a_word=(word.title(),time)
			words_list.append(a_word)
	#出图
	words_cloud=(
             WordCloud()
             .add("", words_list, word_size_range=[20, 100],shape="diamond")
             .set_global_opts(title_opts=opts.TitleOpts(title=movie_name+" WordCloud",subtitle=None)
             ,toolbox_opts=opts.ToolboxOpts(is_show=True))
             )
	words_cloud.render(movie_name+'\\'+movie_name+'wordcloud.html')

if __name__ == '__main__':
	ciyun_en('复仇者联盟4')

	
	




