#从source.html文件中分析网页结构，此文件是网页源文件
from bs4 import BeautifulSoup
soup = BeautifulSoup(open("source.html", "r", encoding='utf-8'), 'lxml')

def getContentOfTag(tag):
    '''获取一个Tag对象的内容'''
    content = ''
    if tag != None:
        for line in tag.stripped_strings:
            content += line + '\n'
    return content
        
#问题标题
question_title = getContentOfTag(soup.find("h1", class_="QuestionHeader-title"))
#问题描述
question_desc = getContentOfTag(soup.find("span",class_="RichText ztext"))
#总共有的回答数量
all_answer_count = getContentOfTag(soup.find("h4",class_="List-headerText"))
#所有回答信息，包含作者用户名头像、作者个性签名、回答被点赞数、答案等。
answers = soup.find_all("div",class_="List-item")
#当前获取到的回答数量
current_answer_count = len(answers)

#############下面针对每个回答进行分别提取信息#############
answers_map_list = [] #存储所有答案的信息
for answer in answers:
    answers_map = {} #存储每一个答案的信息
    #获取答案内容
    answer_tag = answer.find("span",class_="RichText ztext CopyrightRichText-richText")
    answer_content = getContentOfTag(answer_tag)
        
    #获取用户名
    username_tag = answer.find("span",class_="UserLink AuthorInfo-name")
    username = getContentOfTag(username_tag)
        
    #获取用户个性签名
    userdesc_tag = answer.find("div",class_="RichText ztext AuthorInfo-badgeText")
    userdesc = getContentOfTag(userdesc_tag)

    #获取答案获赞数
    voter_tag = answer.find("span",class_="Voters")
    voter = getContentOfTag(voter_tag)
        
    answers_map["answer_content"] = answer_content
    answers_map["username"] = username
    answers_map["userdesc"] = userdesc
    answers_map["voter"] = voter
    answers_map_list.append(answers_map)

#对结果按照点赞数进行排序
def vo(mp):
    if not 'voter' in mp:
        return 0
    s = mp['voter']
    if s == None:
        return 0
    s = s.replace('\n', ' ')
    for e in s.split(' ')[::-1]:
        e = e.replace(',', '')
        if(e.isdigit()):
            return int(e)
    return 0

answers_map_list.sort(key = vo, reverse = True)

#将提取的问题和答案信息保存到文件
sep = "-*-"

#文件名不能出现的字符
no_file_name = ["\\", "/", ":", "*", "?", "\"", "<", ">", "|"]
file_name = question_title.strip()
for c in no_file_name:
    file_name = file_name.replace(c, "")

with open(file_name + ".txt", "w", encoding='utf-8') as file:
    file.write(question_title)
    file.write(question_desc)
    file.write(all_answer_count)
    file.write("#"*10 + "当前获取回答数：" + str(current_answer_count) + "#"*10 + '\n\n\n')
    for am in answers_map_list:
        file.write(am["username"])
        file.write(am["userdesc"])
        file.write(am["voter"])
        file.write("【answer.begin】" + sep*7 + "\n")
        file.write(am["answer_content"])
        file.write(sep*8 + "【answer.end】\n\n")
    file.close()
    
print("done....")