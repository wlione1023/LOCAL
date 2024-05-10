from skpy import Skype, SkypeChats
import time

sk = Skype("帳號", "密碼")
skc = SkypeChats(sk)
ct_name = ["群組名稱", "群組名稱", "群組名稱"]


def print_recent_chats(skc):
    chats = skc.recent()
    
    for chat in chats.values():
        # 取得群組名稱
        group_name = getattr(chat, 'topic', 'no attr')

            # 取得群組 ID
        group_id = getattr(chat, 'id', 'no id')

        if group_name != 'no attr':
                # 如果抓得到群組名稱的話就印出名稱和 ID
            print('Group Name:', group_name, ', Group Id:', group_id)
    chats = skc.recent()

def print_recent_chats(skc):
    chats = skc.recent()
    chat_info = {}  # 创建一个字典用于存储群组信息
    for chat in chats.values():
        group_name = getattr(chat, 'topic', 'no attr')
        group_id = getattr(chat, 'id', 'no id')
        if group_name != 'no attr':
            chat_info[group_name] = group_id  # 将群组名和ID存储在字典中
    return chat_info

# 获取最近的聊天列表信息
chat_info = print_recent_chats(skc)

# 打印每个群组的名称和对应的ID
#for group_name, group_id in chat_info.items():
#    print('Group Name:', group_name, ', Group Id:', group_id)

# 定义一个函数用来检查给定的群组名称是否存在于 chat_info 字典中，并打印对应的群组名称和ID
def print_group_info(group_name, chat_info):
    if group_name in chat_info:
        group_id = chat_info[group_name]
        print(f'Group Name: {group_name}, Group Id: {group_id}')
    else:
        print(f"Group '{group_name}' not found.")
for name in ct_name:
    #print_group_info(name, chat_info)
    if name in chat_info:
        ch = sk.chats[chat_info[name]]  # 根据群组名称从chat_info字典中获取对应的ID
        msg = ch.sendMsg("Skype API testing success !")
        time.sleep(15)
    else:
        print(f"Chat room '{name}' not found.")
