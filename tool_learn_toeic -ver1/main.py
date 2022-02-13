# tool luyen cac part trong toeic
import numpy, os
#  I give you small advice before the workout put in
#  a paper what you have to do so you dont stop,
#  you check you do it you check you do it. 
def check_int(s):
    return True if s.isdigit() else False

def check_chuoi(s):
    print(s)
    iik = ""
    while 1:
        if iik == s:
            print("Correct ! +1")
            return
        # print
        iik = input("Again hay bỏ cuộc (2): ") # iik input in keyboard
        if check_int(iik):
            if int(iik) == 2:
                print_equal()
                print("Chưa chi gì đã bỏ cuộc rồi! -__ Thất vọng về mày vl")
                my_quit_fn()

def print_equal():
    print("=================================")

def my_quit_fn():
   raise SystemExit

# function random cau va random cac phan
# function chon cac part hoac unit de lam
# function dem so cau dung

# def invalid():
#    print ("INVALID CHOICE!")

# def menu(chuoi_s):
#     menu = {"1":("Again",check_chuoi(chuoi_s)),
#             "2":("Bỏ cuộc",my_quit_fn)
#         }
#     for key in sorted(menu.keys()):
#         print( key+":" + menu[key][0])

#     ans = input("Make A Choice")
#     menu.get(ans,[None,invalid])[1]()

if __name__ == '__main__':

    os.system('cls')
    os.system('color %s' % numpy.random.randint(9))
# mở đầu
    print('Practise make perfect!')
    print_equal()
    print()
# chọn unit để học
    unit = ""
    num_unit = input("Chọn unit để học 1 2 3 4: ") # mặc định là nhập đúng    
    print_equal()
    unit = "unit" + num_unit +".txt"
    # check_chuoi("Life is what happens when you're busy making other plans.")
    with open(unit, encoding="utf-8") as f:
        line = f.readlines()

    list_cac_phan = ("".join(line)).split("====\n") # list_cac_phan
    print(list_cac_phan[0])

    for l in list_cac_phan[1:]:
        l = l.split("\n")
        print("Phần: ",l[0])
        #luyen tung cau trong tung phan 
        list_cac_cau = l[1:]
        print('Có {} câu.\n'.format(len(list_cac_cau)))
        for i in list_cac_cau:
            check_chuoi(i.strip())
            # strip để lọc các dấu cách không cần thiết dẫn
            #  đến việc so sánh chuỗi bị lỗi vd : "hello " và "hello" là tương tự nhau
        print_equal()
        print('Keep learning! Try your best!!!')