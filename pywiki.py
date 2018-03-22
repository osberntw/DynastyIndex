import re
import wikipedia


wiki= open("name08.txt",'r', encoding = 'utf8')

input_line = wiki.read().split(',')
wikipedia.set_lang('zh')

#a = ['吳思瑤','姚文智']

#with open('wiki_page_ext.txt', 'w') as output_file1:
with open('wiki_extract08.txt', 'w', encoding = 'utf8') as output_file1:
		for i in input_line:
			print ('--- Now Get {'+str(i)+'} ---')
			target = []
			get_wiki = wikipedia.page(str(i))
			name = get_wiki.title
			summary = get_wiki.summary
			content = get_wiki.content
			target.append([name, summary, content])
			for j in target:
				output_file1.write(str(j)+'\n')
			print ('--- Now {'+str(i)+'} GOT---')

print ('--- PROCESSING OVER---')