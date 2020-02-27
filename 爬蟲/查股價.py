import tkinter as tk
import time
import pandas as pd
from bs4 import BeautifulSoup
import requests
window = tk.Tk()
window.title('get stock')
window.geometry('400x600')          #定義窗口

def add_stkno():                    #定義「把輸入的證券代碼加入listbox」
    stkno = e.get()
    lb.insert('end',stkno)
l = tk.Label(window, text='請輸入證券代碼')
l.pack()

e = tk.Entry(window)                #證券代碼輸入位置
e.pack()

b = tk.Button(window, text='add',command=add_stkno)   #按鈕，用於啟用「把輸入的證券代碼加入listbox」
b.pack()

lb = tk.Listbox(window, width=20, height=22)  #listbox
lb.pack()

def del_stk():                          #定義「刪除所選證券代碼」
    lb.delete(lb.curselection()[0])
b2 = tk.Button(window, text='delete',command=del_stk)      #按鈕，使用「刪除所選證券代碼」
b2.pack()

var = tk.StringVar()
var.set('')
l2 = tk.Label(window, textvariable=var, bg='yellow',width=15,height=2)            #用於顯示更新時間
l2.pack()

def update():                   #定義「主程序」，說明如下：
    for i in range(lb.size()):      #對於listbox裡面每一個證券代碼 的索引 的操作
        stkno = lb.get(i)           #依索引找到對應的證券代碼
        data = {'stkNo':stkno}      #把證券代碼寫成字典形式，用於post指定網站
        try:
            df_=pd.read_csv(stkno+'.csv')  #這邊嘗試尋找 已儲存的記錄，如果有，則調用（不報錯）；
        except:
            df_=0                          #如果沒有（報錯），則令df_為0，用於下面引發報錯
        html = requests.post('https://www.twse.com.tw/zh/stockSearch/stockSearch',data=data)    #連到台灣證券交易所，post證券代碼，取得回應
        soup = BeautifulSoup(html.text, features='lxml')            #用BeautifulSoup解析
        table = soup.find_all('table')                          #找到所有的表格
        try:                                        #這邊的情形比較特殊，有的股票顯示在第二個表格，有的顯示在第一個，且後者的網頁只有一個表格
            df = pd.read_html(str(table[1]))        #對於前者，能順利爬取[1]，對於後者，會報錯
        except:
            df = pd.read_html(str(table[0]))        #則後者會爬取[0]
                                                    #然後再用pandas把這段html吃掉，換成表格
        df = df[0]
        df['證券代碼'] = stkno                       #新增一列(axis=1)，標注證券代碼
        df['time'] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())   #新增一列，標註更新時間
        try:                                                    #39~42行：如果已經有紀錄的，則df_為一表格，如果沒有，則df_為0
            df_= df_.append(df,ignore_index=True,sort=True)     #對於前者，可新增 此次爬到的數據 到 之前的紀錄（因為不報錯）
            df_= df_.dropna(axis=1,how='any')                   #但實際使用發現 自動加入的index會造成多出的列，且這些列中有NaN，所以drop掉任何有NaN的列
            df_.to_csv(stkno+'.csv')                            #儲存
        except:
            df_=df                                              #對於後者，則將df_ 定義為爬到的資訊（因為 df_為0時，執行上面的指令會報錯）
            df_.to_csv(stkno+'.csv')                            #儲存
        var.set(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) #更新窗口上「顯示更新時間」
        time.sleep(1)                               #對於爬取多隻股票，設定時間間隔使伺服器回應
    
def r_update():                     #定義「regular update」：定時更新
    update()                        #執行主程序
    window.after(1000*60, r_update)   #執行後過 60秒（100000毫秒)，執行「regular update」

r_update()      #執行「regular update」

b3 = tk.Button(window, text='update', command=update)       #按鈕，執行「主程序」，手動更新
b3.pack()

window.mainloop()