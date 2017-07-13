# coding: utf-8
  
class Util():


    @staticmethod	
    def content_format(content,content_fnt,max_content_w):
        lines = content.split('\n')
        content_formated = ''
        single_content_w,single_content_h = content_fnt.getsize("已")
        for line in lines:
            temp = ''
            line_formated = ''
            words = line.split(' ')
            for _word in words:
                pure_word = _word.replace(',','').replace('.','').replace('!','').replace('?','')
                if pure_word.isalpha():
                    if temp !='':
                        append = _word+' '
                    else:
                        append = _word+' '
                    #print(_word)
                    #print(append)    
                    temp_w,temp_h = content_fnt.getsize(temp + append)                      
                    if temp_w > max_content_w:
                        line_formated = line_formated + '\n' +append
                        temp = append
                    else:
                        temp += append
                        line_formated += append   
                else:                  
                    contents = list(_word)                  
                    for word in contents:
                        temp += word
                        temp_w,temp_h = content_fnt.getsize(temp)
                        line_formated += word
                        if temp_w + single_content_w > max_content_w:
                            line_formated += '\n'
                            temp = ''
            if temp != '':
                line_formated += '\n'
            content_formated += line_formated
    
        return content_formated


  
if __name__ == "__main__":
    from PIL import ImageFont
    content = 'The deepest love I think, later than apart, I will live as you like. 我所认为最深沉的爱,莫过于分开以后,我将自己活成了你的样子。'
    max_content_w = 710
    content_font = ImageFont.truetype('font/zh/PingFang.ttf',40)
    content_formated = Util.content_format(content,content_font,max_content_w)
    print(content_formated)
