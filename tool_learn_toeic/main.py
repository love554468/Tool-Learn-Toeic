# tool luyen cac part trong toeic
import numpy, os

def check_int(s):
    return True if s.isdigit() else False

def check_chuoi(s):
    print(s)
    iik = ""
    while 1:
        if iik == s:
            print("Correct ! +1")
            return
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

def write_file_luyen_tap(l):
    namel = input("lưu file luyện tập với tên: ")
    namell = 'unit' + namel + '.txt'
    with open(namell, encoding = 'utf-8', mode='w') as f:
        f.write("Phần luyện tập \n====\n01\n")
        f.writelines(l)
    print("đã viết file luyện tập!")
    
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
    option = input("chọn chế độ luyện tập cường độ cao(h): ")  
    print_equal()
    unit = "unit" + num_unit +".txt"
    # check_chuoi("Life is what happens when you're busy making other plans.")
    with open(unit, encoding="utf-8") as f:
        line = f.readlines()

    list_cac_phan = ("".join(line)).split("====\n") # list_cac_phan
    print(list_cac_phan[0])

    l_save = [] # luu trữ các câu để luyện sau này

    for l in list_cac_phan[1:]:
        l = l.split("\n")
        print("Phần: ",l[0])
        #luyen tung cau trong tung phan 
        list_cac_cau = l[1:]
        print('Có {} câu.\n'.format(len(list_cac_cau)))
        for i in list_cac_cau:
            i = i.strip()
            check_chuoi(i)
            # lưu câu để luyện tập vào 1 cái list
            if(option != 'h'):
                option_save = input("Lưu câu (s) or next: ")
                if option_save == "s":
                    l_save.append(i+"\n")
                    # print(l_save)
            # strip để lọc các dấu cách không cần thiết dẫn
            #  đến việc so sánh chuỗi bị lỗi vd : "hello " và "hello" là tương tự nhau
        print_equal()
        print('Keep learning! Try your best!!!')
    if(option != 'h'):
        write_file_luyen_tap(l_save)