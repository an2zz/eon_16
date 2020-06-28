import os
import book 

this_folder = os.path.dirname(os.path.abspath(__file__))
my_file = os.path.join(this_folder,'input.txt')
f = open(my_file,'r')
dictionary = f.readlines()

class yes24:
    
    def __init__(self):
        self.aladin_clss = book.funtion()
    
    def Menu_List(self):
        print("1. 도서추가")
        print("2. 도서검색")
        print("3. 도서 정보 수정")
        print("4. 도서삭제")
        print("5. 도서 목록 출력")
        print("6. 저장")
        print("7. 종료")

    def Menu (self,dictionary):
        self.Menu_List()
        select = int(input(">>> 메뉴를 선택하세요"))

        if select ==1:
            self.aladin_clss.menu1(dictionary)
            self.Menu(dictionary)
        
        elif select ==2:
            self.aladin_clss.menu2(dictionary)
            self.Menu(dictionary)
        
        elif select ==3:
            self.aladin_clss.menu3(dictionary)
            self.Menu(dictionary)
        
        elif select ==4:
            self.aladin_clss.menu4(dictionary)
            self.Menu(dictionary)
        
        elif select ==5:
            self.aladin_clss.menu5(dictionary)
            self.Menu(dictionary)
        
        elif select ==6:
            self.aladin_clss.menu6(dictionary)                  
            self.Menu(dictionary)
        
        elif select ==7:
            self.aladin_clss.menu7(dictionary)         
            print(">>> 프로그램을 마칩니다.")

b=yes24()
b.Menu(dictionary)