question=input("Δώσε τις λέξεις: ")    #δινει τις λεξεις
words=question.split()                 #αποθηκευει στην μεταβλητη 'words' τις λεξεις χωρισμενες αμα ειναι
list=[]                                #αρχιοθετω μια κενη λιστα
for word in words:
    list.append(word)                   #βαζω τις λεξεις στην λιστα 'list'
print (max(list))                       #βγαζω στην οθονη την λεξη με το μεγαλυτερο μηκος
