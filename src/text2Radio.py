import pyttsx3
import re

def readBook(filepath):
    filename = filepath.replace("\\", '/').split("/")[-1].split(".")[0]
    i=1
    str=""
    with open(filepath,'r', encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            # x = re.findall(r"^第\d+章\.*?", line)  # 使用findall()获取所有匹配
            x = re.findall(r"^第[\u4e00-\u9fa5a-zA-Z0-9]{1,7}[章节卷集部回]\.*", line)  # 使用findall()获取所有匹配
            if x != [] :
                if str != "":
                    transText(str,"第"+i.__str__()+"章")
                    i += 1
                str = "" + line
            else:
                str += line
        transText(str,filename,i)




def transText(str,chara) :
    chara = chara.__str__()
    engine = pyttsx3.init()
    engine.setProperty('rate', 200)  # 设置语速
    engine.setProperty('volume', 1)  # 设置音量
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[5].id)  # 设置第一个语音合成器
    engine.save_to_file(str,chara+'.mp3','test')
    engine.runAndWait()
    engine.stop()



    # Press the green button in the gutter to run the script.
if __name__ == '__main__':
    filepath = input("请输入文件路径：")
    readBook(filepath)
    # readBook("C:\\Users\\user\\Desktop\\他与它.txt")
