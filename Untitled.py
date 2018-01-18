#Translation
translations = [("早上好","Good morning"),("再见","Good bye"),("谢谢","Thank you"),("晚安","Goodnight"),("太好了","Wonderful!"),("多亏有你帮忙","Thanks for your help!"),("太奇妙了","that's amazing"),("你学得真快","you are learning so fast"),("你真棒","You are great!"),("你真能干","you are pretty talented"),("我真为你高兴","I'm happy for you"),("我好羡慕你","I envy you so much"),("你好可爱","you’re so cute"),("我妈说我很特别","moms says i'm special")]
#translations = [("Good morning",""), ("Goodnight",""),("Thank you",""),("You are so cute",""),("You are so sexy",""),("Can I get your number",""),("Can I g

def intochinese():
    a = input("Translation: ")
    for i in translations:
        if i[0] == a:
            print(i[1])
        else:
            llama()


def intoenglish():
    a = input("Translation: ")
    for i in translations:
        if i[1] == a:
            print(i[0])
        else:
            llama()
          
def llama():
       print("llama ate the word")
       print("┏┛┻━━━┛┻┓")
       print("┃｜｜｜｜｜｜｜┃")
       print("┃　　　━　　　┃")
       print("┃ ┳┛ 　┗┳ ┃")
       print("┃　　　　　　　┃")
       print("┃　　　┻　　　┃")
       print("┃　　　P 　　　┃")
       print("┗━┓　a  ┏━┛")
       print("　　┃　t  ┃　　")
       print("　　┃  r  ┃　　")
       print("　　┃　i  ┃　　")
       print("　　┃　c  ┃")
       print("　　┃　h  ┗━━━┓")
       print("　　┃ o         ┣┓")
       print("　　┃ r         ┃")
       print("　　┗┓┓┏━┳┓┏┛")
       print("　　　┃┫┫　┃┫┫")
       print("　　　┗┻┛　┗┻┛")
            
print("Welcome to use 'how to get a girl TRANSLATION'")
print("Notice: ")
print(" English to Chinese or Chinese to English?")
print("    No Capital or quotation mark")


language = input("English or Chinese")
if language == "English":
    intochinese()
else:
    intoenglish()

