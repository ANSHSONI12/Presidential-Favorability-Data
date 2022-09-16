import csv
import matplotlib.pyplot as plt

file = open("data.csv")
csvreader = csv.reader(file)
header = next(csvreader)
#print(header)
data = []
for row in csvreader:
    data.append(row)
#print(data)
file.close()
#step 1---------------------------------------------------------------
poll_names = []
names = []


for i in range(len(data)):#it looping to data
  names.append([data[i][0]])#its appending i in data
for i in range(len(names)):#its looping to names
  if names[i] not in poll_names:#the name i is not in poll name
    poll_names.append(names[i])#is appending i in poll name
print()#it prints it    
print(poll_names)#it prints it

#step 2--------------------------------------------------------------------------

polls_dict = {}#printing dictionary
for i in range(len(poll_names)):#loop to poll name in i
  polls_dict.update({poll_names[i][0]:[]})#its adding [] at the end of the line
print(polls_dict)#its printing 
#step 3----------------------------------------------------------------------------
for i in range(len(data)):#loops to poll dict
  for key in polls_dict:#looping to data
    if data[i][0] == key:#data
      values = data[i][1:]#its value in i
      polls_dict[key].append(values)#its appending value in dict


print(polls_dict)#its printing
#step4------------------------------------------------------------------------------
for key in polls_dict:
  polls_dict[key].sort()
  holder = []#empty list called holder
  for i in range(len(polls_dict[key])): #loop inse poll dict for key i
    if polls_dict[key][i][0][1].isnumeric(): #find if the key i inside polls dict numeric
      holder.append(polls_dict[key][i])#if is numeric add holder to polls dict
  for j in range(len(holder) ):#new for loop but inside the holder
    if holder[j] in polls_dict[key]:#check if the value inside holder is in polls dict
      polls_dict[key].remove(holder[j])#if is inside remove
  for h in range(len(holder) ):#new for loop for holder
    polls_dict[key].append(holder[h])#add polls dict to holder
print(polls_dict)
#---------------------------------------------------------------------------------
#step 6
for key in polls_dict:#for loop for key inside polls dict
  plt.subplot(2,1,1)
  plt.title('Favorability')#add title to the output
  for i in range(len(polls_dict[key])):#for loop inside polls dict
    plt.bar(polls_dict[key][i][0],polls_dict[key][i][1],color='blue')#define the color
  plt.xticks(rotation=90)#rotate the ticks in 90 degrees
  plt.grid()
  plt.ylabel('percentage of population')#tittle of y label
  plt.subplot(2,1,1)
  plt.title('unfavorability')#title of another output
  for i in range(len(polls_dict[key])):#for loop inside pol dict
    plt.bar(polls_dict[key][i][0],polls_dict[key][i][2],color='red')#difine the color
plt.xticks(rotation=90)#rotate the ticks in 90 degrees
plt.grid()
plt.ylabel('percentage of population')
plt.suptitle(key)
plt.show(block=False)
plt.pause(5)
plt.close()