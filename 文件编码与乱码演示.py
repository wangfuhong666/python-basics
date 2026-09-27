with open("a.txt", "w", encoding="GBK") as f_write:
    f_write.write(
        "几块好滴好滴机顶盒你肯定郭德纲的故事哥哥如何厚度对还一副我回复是沙发客是客户端会发给对不过宁可很难看距离不应该已经女法好烦好烦好烦好烦发货部分恢复好官一"
        "恐怖谷不敢哭UV个人他没能力反反复复反反复复反反复复反反复复反反复复反反复复反反复复"
        "放风”哭唧唧是看过回去不买3226556355465454545555"
        "11qaaaaaaa")

with open("a.txt", "r", encoding="UTF-8", errors="replace") as f_read:
    garbled_content = f_read.read()
print("UTF-8读取的乱码：", garbled_content)
with open("a.txt", "w", encoding="UTF-8") as f_save:
    f_save.write(garbled_content)
with open("a.txt", "r", encoding="GBK", errors="replace") as f_final:
    final_garbled = f_final.read()
print("GBK打开UTF-8乱码文件的结果：", final_garbled)
