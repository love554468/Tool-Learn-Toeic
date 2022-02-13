# with open('readme.txt') as f:
#     lines = f.readlines()

with open('unit1.txt', encoding="utf-8") as f:
    line = f.readlines()

list_cac_phan = ("".join(line)).split("====\n") # list_cac_phan
print(list_cac_phan[0])

for l in list_cac_phan[1:]:
    l = l.split("\n")
    print("Phần: ",l[0])
    #luyen tung cau trong tung phan 
    list_cac_cau = l[1:]
    