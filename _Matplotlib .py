#!/usr/bin/env python
# coding: utf-8

# In[239]:


import matplotlib as pl
import numpy as np


# In[241]:


print(pl.__version__)


# In[12]:


np.__version__


# In[13]:


import matplotlib.pyplot as plt


# In[14]:


x=np.array([0,6])


# In[15]:


x


# In[16]:


y=np.array([0,250] )


# In[17]:


y


# In[18]:


plt.plot(x,y)


# In[19]:


plt.plot(y,x)


# In[20]:


plt.plot(y,x,"o")


# In[21]:


x1=np.array([1,2,3,5,6])
y1=np.array([23,26,34,32,20])


# In[22]:


plt.plot(x1,y1)


# In[63]:


p=np.array([2,4,5,12,23,43])


# In[69]:


plt.plot(p)


# In[23]:


plt.plot(x1,y1,"o")


# In[24]:


plt.plot(x1,y1,marker='o')


# In[25]:


plt.plot(x1,y1,marker='*')

 **Markers**

=============   ===============================
character       description
=============   ===============================
``'.'``         point marker
``','``         pixel marker
``'o'``         circle marker
``'v'``         triangle_down marker
``'^'``         triangle_up marker
``'<'``         triangle_left marker
``'>'``         triangle_right marker
``'1'``         tri_down marker
``'2'``         tri_up marker
``'3'``         tri_left marker
``'4'``         tri_right marker
``'8'``         octagon marker
``'s'``         square marker
``'p'``         pentagon marker
``'P'``         plus (filled) marker
``'*'``         star marker
``'h'``         hexagon1 marker
``'H'``         hexagon2 marker
``'+'``         plus marker
``'x'``         x marker
``'X'``         x (filled) marker
``'D'``         diamond marker
``'d'``         thin_diamond marker
``'|'``         vline marker
``'_'``         hline marker
=============   ===============================

# In[26]:


plt.plot(x1,y1,marker='o',color='red')


# In[27]:


plt.plot(x1,y1,marker='o',color='m')


# In[28]:


plt.plot(x1,y1,'*''y')

The supported color abbreviations are the single letter codes

=============    ===============================
character        color
=============    ===============================
``'b'``          blue
``'g'``          green
``'r'``          red
``'c'``          cyan
``'m'``          magenta
``'y'``          yellow
``'k'``          black
``'w'``          white
=============    ===============================
# In[29]:


plt.plot(x1,y1,marker='o',color='red',linestyle='--')


# In[30]:


plt.plot(x1,y1,marker="*",color="c",linestyle='-.')


# In[31]:


plt.plot(x1,y1,'*:c')

**Line Styles**

=============    ===============================
character        description
=============    ===============================
``'-'``          solid line style
``'--'``         dashed line style
``'-.'``         dash-dot line style
``':'``          dotted line style
=============    ===============================
# In[33]:


plt.plot(x1,y1,'*',ms=10) #marker size(ms)


# In[34]:


plt.plot(x1,y1,'*',ms=30)


# In[35]:


plt.plot(x1,y1,'o--g',ms=15)


# In[36]:


plt.plot(x1,y1,'o--g',ms=15,mec='r')# marker edge color-mec


# In[37]:


plt.plot(x1,y1,'o--g',ms=15,mec='k')


# In[38]:


plt.plot(x1,y1,'o--g',ms=15,mfc='y') #marker face color (mfc)


# In[39]:


plt.plot(x1,y1,'*:g',ms=14,mfc='k')


# In[40]:


plt.plot(x1,y1,'o:y',ms=18,mec='k',mfc='g')


# # linestyle or ls
# - is used to change the style of the plotted line

# In[41]:


plt.plot(x1,y1,ls=':') #linestyle(ls)


# In[42]:


plt.plot(x1,y1,ls='--')


# # line width

# In[43]:


plt.plot(x1,y1)


# In[44]:


plt.plot(x1,y1,linewidth='10')


# In[45]:


plt.plot(x1,y1,'g',linewidth="5.5")


# # Create labels for a plot

# In[46]:


x2=np.array([30,35,40,45,50,55,60,65,70,75])
y2=np.array([100,105,110,115,120,125,130,135,140,145])


# In[47]:


plt.plot(x2,y2)


# In[48]:


plt.xlabel('oxygen')
plt.ylabel('water')


# In[49]:


plt.plot(x2,y2)
plt.xlabel('oxygen')
plt.ylabel('water')


# ### Title for the plot

# In[50]:


plt.title('Earth')


# In[51]:


plt.plot(x2,y2)
plt.title('Earth')
plt.xlabel('oxygen')
plt.ylabel('water')


# #### Font property for title and labels

# In[52]:


f1={'family':'serif','color':'pink','size':20}
f2={'family':'serif','color':'darkred','size':25}


# In[53]:


plt.plot(x2,y2)
plt.title('Earth',f2)
plt.xlabel('oxygen',f1)
plt.ylabel('water',f1)


# ## Change the location of title

# In[54]:


plt.plot(x2,y2)
plt.title('Earth',f2)
plt.xlabel('oxygen',f1)
plt.ylabel('water',f1)


# In[55]:


plt.plot(x2,y2)
plt.title('Earth',f2,loc='left')# location (loc)
plt.xlabel('oxygen',f1)
plt.ylabel('water',f1)


# In[56]:


plt.plot(x2,y2)
plt.title('Earth',f2,loc='right')
plt.xlabel('oxygen',f1)
plt.ylabel('water',f1)


# # Adding the grid lines to a plot

# In[57]:


plt.grid()


# In[58]:


plt.plot(x2,y2)
plt.title('Earth',f2)
plt.xlabel('oxygen',f1)
plt.ylabel('water',f1)
plt.grid()


# <h5>Now we will specify which grid line to display 
#                  
#     x axis or y axis

# In[59]:


plt.grid(axis='x')


# In[60]:


plt.grid(axis='y')


# <h5>line properties for the grid<h5>

# In[61]:


plt.plot(x2,y2)
plt.title('Earth',f2)
plt.xlabel('oxygen',f1)
plt.ylabel('water',f1)
plt.grid(color='pink',ls='--',linewidth=1)


# In[62]:


plt.plot(x2,y2)
plt.title('Earth',f2)
plt.xlabel('oxygen',f1)
plt.ylabel('water',f1)
plt.grid(color='orange',ls='--',linewidth=1)


# # Display the multiple plots
# 

# In[113]:


x3=np.array([0,2,4,6,8])
y3=np.array([5,3,6,3,12])
plt.subplot(1,2,1) # (rows, columns, panel number)
x4=np.array([1,2,3,4,5,6])
y4=np.array([0,30,24,35,43,29])
plt.subplot(1,2,2) # (rows, columns, panel number)


# In[125]:


x3=np.array([0,2,4,6,8])
y3=np.array([5,3,6,3,12])          
plt.subplot(1,2,1) # (rows, columns, panel number)
plt.plot(x3,y3) 
plt.title('1st plot')


x4=np.array([1,2,3,4,5,6])
y4=np.array([0,30,24,35,43,29])
plt.subplot(1,2,2) # (rows, columns, panel number)
plt.plot(x4,y4)
plt.title('2nd plot')


# In[129]:


x3=np.array([0,2,4,6,8])
y3=np.array([5,3,6,3,12])          
plt.subplot(2,1,1) # (rows, columns, panel number)
plt.plot(x3,y3) 
plt.title('1st plot')




x4=np.array([1,2,3,4,5,6])
y4=np.array([0,30,24,35,43,29])
plt.subplot(2,1,2) # (rows, columns, panel number)
plt.plot(x4,y4)
plt.title('2nd plot')


# In[146]:


x3=np.array([0,2,4,6,8])
y3=np.array([5,3,6,3,12])          
plt.subplot(2,2,1) # (rows, columns, panel number)
plt.plot(x3,y3) 
plt.title('1st plot')


x4=np.array([1,2,3,4,5,6])
y4=np.array([0,30,24,35,43,29])
plt.subplot(2,2,2) # (rows, columns, panel number)
plt.plot(x4,y4)
plt.title('2nd plot')



x5=np.array([11,22,33,44,55,66])
y5=np.array([10,60,34,45,55,40])
plt.subplot(2,2,3) # (rows, columns, panel number)
plt.plot(x5,y5)
plt.title('3nd plot')


# In[161]:


x3=np.array([0,2,4,6,8])
y3=np.array([5,3,6,3,12])          
plt.subplot(2,2,1) # (rows, columns, panel number)
plt.plot(x3,y3) 
plt.title('1st plot')


x4=np.array([1,2,3,4,5,6])
y4=np.array([0,30,24,35,43,29])
plt.subplot(2,2,2) # (rows, columns, panel number)
plt.plot(x4,y4)
plt.title('2nd plot')



x5=np.array([11,22,33,44,55,66])
y5=np.array([10,60,34,45,55,40])
plt.subplot(2,2,3) # (rows, columns, panel number)
plt.plot(x5,y5)
plt.title('3rd plot')


x6=np.array([110,220,330,440,550,660])
y6=np.array([100,600,340,450,550,400])
plt.subplot(2,2,4) # (rows, columns, panel number)
plt.plot(x6,y6)
plt.title('4th plot')


plt.suptitle('plots',color='red',size=20)


# # Scatter 
# the scatter() function plots oe for each observation...

# In[166]:


print(plt.scatter(x4,y4))


# In[165]:


print(plt.scatter(x5,y5))


# In[167]:


x7=np.array([15,18,25,15,30,50])
y7=np.array([18,45,15,20,32,35])


# In[170]:


print(plt.scatter(x5,y5,color='darkred'))
print(plt.scatter(x7,y7,color='hotpink'))


# # Change the color for dots

# In[171]:


print(plt.scatter(x4,y4))


# In[177]:


c1=(['red','purple','pink','cyan','orange','red'])


# In[178]:


print(plt.scatter(x4,y4,c=c1))


# # Specify a colormap in scatter plot

# In[191]:


c1=np.array([0,10,20,30,40,50])
plt.scatter(x4,y4,c=c1,cmap='viridis')


# # Specify a colorbar in scatter plot

# In[196]:


plt.scatter(x4,y4,c=c1,cmap='viridis')
plt.colorbar()


# In[202]:


c1=np.array([70,10,200,340,240,50])
plt.scatter(x4,y4,c=c1,cmap='viridis',s=c1)
plt.colorbar()


# # Alpha
# Adjust the transprency of the dots

# In[206]:


plt.scatter(x4,y4,c=c1,cmap='viridis',s=c1,alpha=0.3)
plt.colorbar()


# # Create bars--(bar())

# In[207]:


x8=np.array(["A","B","C","D","E"])
y8=np.array([12,34,45,65,20])


# In[208]:


plt.plot(x8,y8)


# In[209]:


plt.scatter(x8,y8)


# # Vertical bar

# In[216]:


plt.bar(x8,y8) #(bar())
plt.title('BAR PLOT',color='darkred')


# # Horizontal bar

# In[223]:


plt.barh(x8,y8) #(bar())
plt.title('BAR PLOT',color='pink')


# In[226]:


plt.barh(x8,y8) #(bar())


# In[231]:


plt.barh(x8,y8,color='gold') #(bar())


# In[235]:


plt.bar(x8,y8,color='gold',width=0.3)


# <h3>****** For horizontal to use height insted of width*****<h3>

# In[238]:


plt.barh(x8,y8,color='gold',height=0.5)


# # Histogram

# In[253]:


d1 = np.random.normal(10,20,100)
plt.hist(d1)


# # Piechart

# In[264]:


x9=np.array([25,20,36,16,5])


# In[265]:


plt.pie(x9)


# In[268]:


mlabels=["rohit","panav","chetya","tanya","bitya"]
plt.pie(x9,labels=mlabels)


# <h2>**** Explode****<h2>

# In[283]:


e2=[0.1,0,0.2,0,0 ]
plt.pie(x9,labels=mlabels,explode=e2)


# In[284]:


e1=[0.1,0.1 ,0.1 ,0.2,0.1 ]
plt.pie(x9,labels=mlabels,explode=e1)


# <h2>****Shadow ****<h2>

# In[285]:


plt.pie(x9,labels=mlabels,explode=e2,shadow=True)


# In[315]:


plt.pie(x9,labels=mlabels)
plt.legend(loc=1, fontsize='medium',)

 numeric value:

        ==================   =============
        Location String      Location Code
        ==================   =============
        'best' (Axes only)   0
        'upper right'        1
        'upper left'         2
        'lower left'         3
        'lower right'        4
        'right'              5
        'center left'        6
        'center right'       7
        'lower center'       8
        'upper center'       9
        'center'             10
        ==================   =============
# In[ ]:




