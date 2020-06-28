import os
 
class aladin:

    def menu1(self,dictionary):
        print(">>> 추가를 원하는 책 정보를 입력하세요.")
        print("ex) 제목 저자 발행년도 출판사 카테고리")
        self.pbook = str(input("입력 : "))
        self.plus_book = self.pbook.split()
        print(self.plus_book)
        print("제목 : %s 저자 : %s 발행년도 : %s 출판사 : %s 카테고리 : %s" %(self.plus_book[0],[1],[2],[3],[4]))
        check = int(input(">>> 저장하시겠습니까?(yes -> 1 / no -> 2)"))
        if check == 1:
            dictionary.append(self.pbook+'\n')
            print("추가되었습니다.")
        
        elif check == 2:
            print("메인으로 돌아갑니다.")
        return dictionary

    def menu2(self,dictionary):
        fbook = str(input(">>> 검색어를 입력 하세요"))
        for i in range(0,len(dictionary),1):
            if fbook in dictionary[i]:
                print(dictionary[i])
        print("검색완료")

    def menu3(self,dictionary):
        for i in range(len(dictionary)):
            print(i)
            print(dictionary[i])
        num = int(input(">>> 대상 번호를 입력하세요"))
        dictionary[num] = str(input("수정할 책정보를 입력하세요.\n ex) 제목 저자 발행년도 출판사 카테고리 순서로 입력하세요.\n 입력 :"))
        print("수정되었습니다.")
        return dictionary


    def menu4(self,dictionary):
        for i in range(len(dictionary)):
            print(i)
            print(dictionary[i])
        nbook = int(input(">>> 삭제할 책 번호를 입력하세요"))
        dictionary.pop(nbook)
        print("삭제되었습니다.")
        return dictionary

    def menu5(self,dictionary):
        print (">>> 현재 책 목록은 다음과 같습니다.")
        print (dictionary)
    
    def menu6(self,dictionary):
        sbook = ''.join(dictionary)
        this_folder = os.path.dirname(os.path.abspath(__file__))
        my_file = os.path.join(this_folder,'input.txt')
        wfolder = open(my_file,'w')
        wfolder.write(sbook)
        wfolder.close
        print("저장되었습니다.")

    def menu7(self,dictionary):
        lbook = ''.join(dictionary)
        this_folder = os.path.dirname(os.path.abspath(__file__))
        my_file = os.path.join(this_folder,'input.txt')
        wfolder = open(my_file,'w')
        wfolder.write(lbook)
        wfolder.close 
        print("자동저장")