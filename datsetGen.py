import csv

# open a file containg the user id and their ratings
file1 = open('u1.base','r')

people = list() # to store user id
rating= dict()  # to store user id with ratings


movieName = {} # dictonary to svae move  id and its name
moviefactor= {} # dictionar to save movie id and its factor/score. such as , romatinc, action , thriller ... etc

reader = csv.reader(file1,delimiter='	')

#adding user and rating to list and dictionary
for row in reader :
        l = row
        if l[0] not in people :
                people.append(l[0])
                rating[int(l[0])] ={}
        rating[int(l[0])][int(l[1])] = float(l[2])


# open a file containing the move detais and its scores
file2 = open('u.item','r')

reader = csv.reader(file2,delimiter='|')

for row in reader :
        l = row
        movieName[int(l[0])] = l[1] 
        fact = []
        fact.append(1) # x_0 is one for any value
        for x in l[5:] :
             fact.append(float(x))
        moviefactor[int(l[0])] = fact      



