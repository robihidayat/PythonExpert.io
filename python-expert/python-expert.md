# Python Expert from book Expert Python Programming 

## low level class 

    a. List comperhension 
    b. Iterator and generator
    c. Descriptor and properties
    d. Decorators
    d. with and contextlib
    
    
    kemampuan kita untuk menulis sytax dengan effisien datang secara alami oleh waktu. 
    jika kamu mencari kembali program yang pertama kamu buat, pasti kamu setuju, ya pasti lah. 
    code yang benar akan terlihat indah dimatamu, sementara syntax yang salah akan terlihat sesuatu menjijikan. 


# List Comprehensions 

    >> numers = range(10)
    >> size = len(number)
    >> event = []
    >> i = 0
    >> while i <size:
    >>    if i%2 ==0:
    >>        event.append(i)
    
    kode diatas kurang baik, karena :
        1. itu akan membuat interpreter bekerja setiap kali penghitungan looping yang mana bagian dari sequance dari perubahan. 
        2. itu membuat kamu akan menyimpan penghitung untuk mengetrack element apa. 
        
    list comperhension is adalah jawaban yang tepat untuk menjawan pattern jenis ini. 
    
    >> [i for i in range(10) if i%2 ==0 ]
    
    selain, code diatas lebih effisien, kemudian lebih pendek. saat code itu menjadi besar, itu artinya lebih mudah dibaca dan dipahami. 

# ENUMERATE
    >> i = 0
    >> seq = ['one','two,'three']
    >> for element in seq:
        seq[i] = '%d: %s' (i, seq[i])
        i += 1
    
    code in above is not efficient, so we can use enumerate:
    
    >> seq = ["one","twi","three"]
    >> for i, element in enumeate(seq):
        seq[i] = '%d: %s' $(i, seq[i)
        
# Itterator 
     next. --> which return the next item of the container
     __iter__ --> which return the iterator itself.
    

# Generator 
    simple way to return a list from element
    
    
 



    
    
    
    
    
   