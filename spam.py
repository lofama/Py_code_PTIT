import pyautogui, pyperclip, random,time
print(pyautogui.size())
print ("Tool spam tin nhan")
mgs = input("Nhập nội dung chia bằng dấu '//' : ").split(" // ")
n = int(input("Nhập số lần: "))
m = float(input("Thời gian nghỉ: "))
for i in range (100):
    print("Loading.....%d%",i)
    time.sleep(1)
for i in range(5,0,-1):
    print(i,end="...",flush = 'True')
    time.sleep(0.01)
print("Start")

for i in range(n):
    pyperclip.copy(random.choice(mgs))
    pyautogui.hotkey("ctrl","v")
    pyautogui.press("enter")
    time.sleep(m)
