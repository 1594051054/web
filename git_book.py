with open("html_text.txt",'r') as f:
    text = f.read()


# Get The Book Name
pos = text.find("readbefore_cover")
next_pos = text.find("h3",pos)
next_pos = text.find("href",next_pos)
next_pos = text.find('">',next_pos)
start_pos = next_pos + 2
end_pos = text.find('</', start_pos)
name = text[start_pos : end_pos]

# Get The Author
pos = text.find("readbefore_box", end_pos)
next_pos = text.find("author",pos)
next_pos = text.find(">",next_pos)
start_pos = next_pos + 2
end_pos = text.find("</p>", start_pos)

author= text[start_pos:end_pos]
print(name, author)