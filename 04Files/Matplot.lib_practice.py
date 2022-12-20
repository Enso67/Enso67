#Kyle Metcalf 11/15/22
# import matplotlib.pyplot
import matplotlib.pyplot as plt
#Professor Parsons File
        
#---------LINE------------
# Create x and y coordinates
y = []
x = ["July","August","September","October","November"]




for i in range(5):
    data = int(input("Please enter your data for x-axis"))
    y.append(data)
   
    
# Line plot
#plt.plot(x,y)           #marker = 'o' 'v' 'D'= diamonds
plt.plot(x,y,marker = 'D')


#How to label
plt.title("Profits over time")
plt.ylabel("Profit")
plt.xlabel("Months")


# Customize plot axes
plt.xlim(xmin=0, xmax=len(x))
plt.ylim(ymin=0, ymax= 55000)

##plt.xticks(ticks=range(0,5))
##plt.yticks(ticks=range(0,5))

#Customize tick marks
##plt.xticks([0, 1, 2, 3, 4],
##           ['2016', '2017', '2018', '2019', '2020'])
##plt.yticks([0, 1, 2, 3, 4, 5],
##           ['$0m', '$1m', '$2m', '$3m', '$4m', '$5m'])

'''
#---------BAR------------
# Bar coordinates
left_edges = [0, 10, 20, 30, 40]
heights = [100, 200, 300, 400, 500]
bar_width = 5

# Bar plot
plt.bar(left_edges, heights, bar_width)


#---------PIE------------
plt.pie(y)
'''

# Show plot
plt.show()
#commment out plt.show() or it wont save
#plt.savefig("Matplot_Metcalf_CIS-115.png")
#to save to specific directory
#plt.savefig("r'C:\User\test.png")
