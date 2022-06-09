#!/usr/bin/env python
# coding: utf-8

# Họ và tên: Nguyễn Thanh Huy
# MSSV: 19120532

# In[18]:


import copy

# Hàm đọc file txt
def read_File(fName):
    with open(fName, 'r') as fRead:
        alpha = fRead.readline().strip("\n")
        quantity = fRead.readline().strip("\n")
        arr_Clauses = []
        for i in range(int(quantity)):
            clause = fRead.readline().strip("\n").split(' ')
            for i in range(len(clause)):
                clause[i] = clause[i].strip(' ')

            clause = set(filter(lambda x: x!="OR", clause))
            arr_Clauses.append(clause)
        
        return alpha, quantity, arr_Clauses


# In[19]:


# Hàm chuyển đổi literal thành literal đối
def swap_Negative(a):
    if a[0] == "-":
        return a[1:]
    else:
        return "-"+a

# Hàm kiểm tra xem a, b có phải là 2 literal đối nhau không
def check_Is_Negative(a, b):
    if a == swap_Negative(b):
        return True
    return False


# In[20]:


# Hàm kiểm tra tập dư thừa
def check_Is_Clause_Redundancy(clause):
    if len(clause) <= 1:
        return False
    for i in clause:
        if swap_Negative(i) in clause:
            return True
    return False


# In[21]:


# Hàm PL_Resolve dùng để hợp giải 2 mênh đề 
def PL_Resolve(ci, cj):
    arr_Clauses = []
    for di in ci:
        for dj in cj:
            if check_Is_Negative(di, dj):
                try:
                    diNew = copy.deepcopy(ci)
                    diNew.remove(di)
                    djNew = copy.deepcopy(cj)
                    djNew.remove(dj)
                    arr_Clauses.append(set(sorted(djNew.union(diNew))))
                except:
                    pass

    if arr_Clauses:
        list_remove = []
        for i in range(len(arr_Clauses)):
            if check_Is_Clause_Redundancy(arr_Clauses[i]):
                list_remove.append(arr_Clauses[i])

        for i in list_remove:
            arr_Clauses.remove(i)

        return arr_Clauses
    return None


# In[22]:


# Hàm kiểm tra xem list1 có phải con là con list2
def check_Is_SubList(list1, list2):
    for element in list1:
        if element not in list2:
            return False
    return True


# In[23]:


# Hàm ghi kết quả vào file output
def write_File(data, fName, result):
    with open(fName, 'w') as fWrite:
        count = 0
        for i in range(len(data)):
            fWrite.write(str(len(data[i])))
            fWrite.write("\n")
            for j in data[i]:
                fWrite.write(str(j))
                fWrite.write("\n")
        fWrite.write(result)


# In[24]:


# Hàm thực thi giải thuật PL-Resolution
def PL_Resolution(arr_Clauses, alpha):
    dWrite = []
    arr_Clauses.append(set([swap_Negative(alpha)]))
    arr_Temp = []

    while True:
        data = []
        n = len(arr_Clauses)
        p = [(arr_Clauses[i], arr_Clauses[j]) for i in range(n) for j in range(i+1, n)]
        for ci, cj in p:
            resolution = PL_Resolve(ci, cj)

            if resolution != None:
                for temp in resolution:
                    if temp not in arr_Temp and temp not in arr_Clauses:
                        data.append(temp)
                        arr_Temp.append(temp)
        dWrite.append(data)

        if check_Is_SubList(arr_Temp, arr_Clauses):
            write_File(dWrite, "Output.txt", "NO")
            return "NO"        
        
        for cc in arr_Temp:
            if not cc in arr_Clauses:
                arr_Clauses.append(cc)

        if set() in arr_Temp:
            write_File(dWrite, "Output.txt", 'YES')
            return "YES"


# In[30]:


# Hàm main
def main(fName):
    alpha, quality, arr_Clauses = read_File(fName)   
    print(PL_Resolution(arr_Clauses, alpha))
    
    
if __name__ == "__main__":
    main("Input1.txt")


# In[ ]:




