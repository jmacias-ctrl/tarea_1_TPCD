def save_edit(text, filename):
    with open(filename, 'w', encoding="UTF-8") as file_text:
        file_text.write(text)

def replacing_substring(content, filename, s_find, s_replace):
    index = content.lower().find(s_find.lower())
    new_content = content[:index] + s_replace + content[index+len(s_find):]
    save_edit(new_content, filename)
    return True

def check_if_exist(content, s_find, case_sensitive):
    if(case_sensitive):
        index = content.find(s_find)
    else:
        index = content.lower().find(s_find.lower())
    if(index == -1):
        return False
    return True