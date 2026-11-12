import matplotlib.pyplot as plt

# data
months=["jan","feb","mar","apr","may"] # x direction
revenue=[20000,45000,44000,23000,87000] # y direction

plt.plot(months,revenue)

plt.show()



#--bar chart --
months=["jan","feb","mar","apr","may"]
revenue=[20000,45000,44000,23000,87000]

plt.bar(months,revenue,color="red")
plt.show()


#--barh--
months=["jan","feb","mar","apr","may"]
revenue=[20000,45000,44000,23000,87000]

plt.barh(months,revenue)
plt.show()



#--pie chart--
months=["jan","feb","mar","apr","may"]
revenue=[20000,45000,44000,23000,87000]

plt.pie(revenue,labels=months,autopct="%1.1f%%")
plt.show()



#--scatter plot--
months=["jan","feb","mar","apr","may"]
revenue=[20000,45000,44000,23000,87000]

plt.scatter(months,revenue,color='red',marker="v",s=10,edgecolor="black")
plt.show()


#multiple plot lines--
months=["jan","feb","mar","apr","may"]

dairymilk=[10000,140000,120000,80000,950000]
kitkat=[10000,140000,140000,90000,105000]
fivestar=[50000,80000,1120000,180000,1950000]

plt.plot(months,dairymilk,color="green",marker="*",label="dairymilk")
plt.plot(months,kitkat,color="red",marker="s",label="kitkat")
plt.plot(months,fivestar,color="orange",marker="o",label="fivestar")

plt.legend()
plt.show()