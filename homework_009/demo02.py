import matplotlib.pyplot as plt

#x_values=[1,2,3,4,5]
#y_values=[1,4,9,16,25]
x_values=list(range(1,1001))
y_values=[x**2 for x in x_values]

#plt.scatter(2,4, s=200)
#plt.scatter(x_values,y_values,s=100)
#plt.scatter(x_values,y_values,s=40)

#edgecolor default is 'none'
#plt.scatter(x_values,y_values,c='red',edgecolor='none',s=40)
#plt.scatter(x_values,y_values,c=(0,0,0.8),edgecolor='none',s=40)
plt.scatter(x_values,y_values,c=y_values,cmap=plt.cm.Blues,edgecolor='none',s=40)

plt.title('Square Numbers',fontsize=24)
plt.xlabel('Value',fontsize=14)
plt.ylabel('Square of Value',fontsize=14)

#set tick size
plt.tick_params(axis='both',which='major',labelsize=14)

#
plt.axis([0,1100,0,1100000])
#plt.show()
plt.savefig('square_plot.png',bbox_inches='tight')
