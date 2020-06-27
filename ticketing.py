import sys
import copy


f = open("C:/users/안호영/desktop/jh/TrainList.txt",'r') 
ticket = []
ticket_list = []
while True:
    line = f.readline()
    if not line: break
    train_r = line.split()
    ticket.append(train_r)
ticket.pop(0)
       

ticket_list = copy.deepcopy(ticket)
treservation = []
ttreservation = []
ticket_list1 = [605, 635, 715, 842]
ticket_list2 = [365, 395, 435, 522]
for i in range(20): 
    del ticket_list[i][2]
    ticket_list[i][0] = ticket_list[i][0].replace(":", "")
    ticket_list[i][0] = int(ticket_list[i][0])
           
class travel:

    def res_menu(self):
        while True:
            print("1. 기차 예약하기")
            print("2. 전체 기차 시간대")
            print("3. 예약 현황, 예약 취소하기 ")
            print("4. 프로그램 종료 ")
            try:
                menu = int(input("메뉴를 입력해주세요 : "))
            except:
                print("숫자를 입력하세요")
                self.res_menu()
            if menu == 1:
                self.menu1()
            elif menu == 2:
                self.menu2()
            elif menu == 3:
                self.menu3()
            elif menu == 4:
                print("프로그램을 종료합니다.")
                break
            else:
                print ("다시 번호를 입력해주세요.")
                return self.res_menu()
    def menu1(self):
        
        ttime = []
        abstime = []
        
        
        
        print(">>>예약 시, 예약 분, 출발역, 도착역, 열차종류를 입력해주세요.")
        
        print(">>>ex) h mm 서울 부산 KTX")
        
        ticketing = list(input("입력 : ").split())
        thour = int(ticketing[0])
        tminute = int(ticketing[1])
        ttime = thour * 60 + tminute
        for i in range(4):
            abstime.append(abs(ttime-ticket_list2[i]))
        find_ind = abstime.index(min(abstime))
        if tminute // 10 == 0:
            ttime1 = str(thour)+"0"+str(tminute)
        else:
            ttime1 = str(thour)+str(tminute)
        
        
        for j in range(20):
            if int(ttime1) == ticket_list1[find_ind] == int(ticket_list[j][0]) and ticketing[2] == ticket_list[j][1] and ticketing[3] == ticket_list[j][2] and ticketing[4] == ticket_list[j][3]:
                print(ticket[j])
                
                while True:
                    print(">>>해당 기차표를 예매하시겠습니까? [Y/N]")
                    reservation = input("입력 : ")
                    
                    if reservation == "Y":
                        if ticket[j][5] != "매진":
                            treservation.append(ticket[j])
                            ticket[j][5] = int(ticket[j][5]) - 1 
                            
                            ttreservation.append(j)
                            print("\n예매가 완료되었습니다.")
                            self.res_menu()
                            if ticket[j][5] == 0:
                                ticket[j][5] = "매진"
                        
                        else:
                            print("매진")
                        
                        
                    elif reservation == "N":
                        self.res_menu()
                return treservation
                    
    def menu2(self):
        print(">>>전체 기차 시간표를 출력합니다 1번을 눌러주세요.")
        alltime = int(input("입력 : "))
        if alltime == 1:
            i = 0
            while i < len(ticket):
                a, b, c, d, e, f = ticket[i]
                print(a, b, c, d, e, f)
                i += 1
            print("\n")
        
            
        else:
            self.res_menu()
    
    def menu3(self):
        print(">>>1. 예매확인 2. 예매취소 ")
        check_and_cancel = int(input("입력 : "))
        if check_and_cancel == 1:
            print(">> 예매확인")
            print(treservation)
        elif check_and_cancel == 2:
            if ticket[ttreservation[len(ttreservation) - 1]][5] == '매진':
                ticket[ttreservation[len(ttreservation) - 1]][5] = 1
                treservation.pop()
            else:
                ticket[ttreservation[len(ttreservation) - 1]][5] = ticket[ttreservation[len(ttreservation) - 1]][5] + 1
                treservation.pop()
                ttreservation.pop()
                print("예약이 취소되었습니다.")  
        else :
            self.res_menu()


if __name__ == "__main__":
    program = travel()
    print(program.res_menu())
    

            

                

    
        
        
