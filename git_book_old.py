with open("html_text.txt",'r') as f:
    text = f.read()



def find_name(text):
    pos = text.find("readbefore_cover")
    next_pos = text.find("h3",pos)
    next_pos = text.find("href",next_pos)
    next_pos = text.find('">',next_pos)
    start_pos = next_pos + 2
    end_pos = text.find('</', start_pos)
    name = text[start_pos : end_pos]
    return name


def find_author():
    pos = text.find("readbefore_box")
    next_pos = text.find("author",pos)
    next_pos = text.find(">",next_pos)
    start_pos = next_pos + 2
    end_pos = text.find("</p>", start_pos)

