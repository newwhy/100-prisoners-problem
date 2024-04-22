import random

n_prisoners = 100  
prisoners = list(range(n_prisoners))  
boxes = []  
failures = 0 
attempts = 1000 


for i in range(attempts):
    boxes = list(prisoners)  
    random.shuffle(boxes)

    for prisoner in prisoners:  
        box_nr = prisoner
        for turn in range(n_prisoners // 2):  
            if boxes[box_nr] == prisoner:  
                break
            box_nr = boxes[box_nr]  
        else:  
            failures += 1  
            break  

print(f'{failures / attempts * 100}% 의 시도가 실패했습니다. ')

