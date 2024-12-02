
inputs = []

with open('input1.txt', 'r') as fichier:
    for ligne in fichier:
        valeurs = ligne.split(" ")
        report = []
        report = [int(v) for v in valeurs]
        inputs.append(report)

def isSafe(report):
    is_safe = True
    is_increasing = report[0] < report[1]
    i = 0
    n = len(report)

    while is_safe and i < n - 1:
        if abs(report[i] - report[i+1]) == 0 or abs(report[i] - report[i+1]) > 3 or is_increasing != (report[i] < report[i+1]):
            return False
        i += 1
    return True


#Challenge 1
count1 = 0
for report in inputs :
    if isSafe(report):
        count1 +=1
print("Réponse Challenge 1:",count1)

#Challenge 2
count2 = 0
for report in inputs :
    n = len(report)
    if isSafe(report):
       count2 += 1
    else:
        for i in range(n):
            new_report = [report[j] for j in range(n) if j != i]
            if isSafe(new_report):
                count2 +=1
                break

print("Réponse Challenge 2:",count2)




