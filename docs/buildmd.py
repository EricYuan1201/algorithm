# * [day04 24. 两两交换链表中的节点，19.删除链表的倒数第N个节点， 链表相交，142.环形链表II ](chapter2/section2.2.md)

import os


def mkdir(path):
    folder = os.path.exists(path)
    if not folder:  # 判断是否存在文件夹如果不存在则创建为文件夹
        os.makedirs(path)  # makedirs 创建文件时如果路径不存在会创建这个路径
    else:
        print("---  There is this folder!  ---")


def get_last_line():
    f = open("SUMMARY.md", "r")
    lines = f.readlines()  # 读取全部内容 ，并以列表方式返回
    lastLine = ''
    for line in lines:
        if len(str(line).strip()) > 3:
            lastLine = line
    print(lastLine)
    return lastLine


if __name__ == '__main__':
    last_line = get_last_line()
    file_name = last_line[last_line.index('](') + 2:last_line.index(')')]
    print(file_name)
    content = last_line[last_line.index('[day') + 6: last_line.index('(chapter') - 2].strip()
    print(content)
    mkdir(file_name[0:file_name.index('/')])
    f = open(os.path.abspath(os.path.dirname(__file__)) + '/' + file_name, 'w')
    f.write('#' + content + '\n\n')
    items = content.split('，')
    for item in items:
        print(item)
        f.write("##" + item.strip() + '\n')
        f.write('\n\n\n')
        f.write('```java' + '\n\n\n')
        f.write('```' + '\n')
