#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask,request,render_template


# In[2]:


#flask load it to an object - app

app = Flask(__name__) #__name__ by default is name, __ is a reserved word. 


# In[3]:


import joblib


# In[4]:


#decorator: any function you declare below, must come to this function first.
@app.route("/",methods=["GET","POST"])
def index(): #the moment you press submit, this will happen
    if request.method == "POST":
        rates = float(request.form.get("rates"))
        print(rates)
        model1=joblib.load("regression")
        r1 = model1.predict([[rates]])
        model2=joblib.load("tree")
        r2=model2.predict([[rates]])
        return(render_template("index.html",result1=r1, result2=r2))
    else:
        return(render_template("index.html",result1="waiting", result2="waiting"))


# In[ ]:


#cloud environment - irl should be cloud and development

if __name__ == "__main__":
    app.run()


# In[ ]:




