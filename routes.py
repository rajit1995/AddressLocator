import urllib.request, urllib.parse, urllib.error
import json
import ssl
from app import app , db
from flask import render_template , redirect , url_for,flash, get_flashed_messages
from datetime import datetime
from models import Task
from flask_sqlalchemy import SQLAlchemy
from Geocode import geocode
import forms
#import FinalList as fl

@app.route('/')
@app.route('/add' , methods=['GET','POST'])
def add():   
    form = forms.AddTaskForm()
    if form.validate_on_submit() :
        print('Submitted Place : ', form.title.data)
        address = form.title.data
        tlist = geocode(address)
        print(tlist)
        db.create_all()
        if db.session.query(db.session.query(Task).filter_by(id =1).exists()).scalar() :
            u=db.session.get(Task,1)
            db.session.delete(u)
            db.session.commit()
            
        if tlist == None :
            place = form.title.data
            lat = "Not Found"           
            lng = "Not Found"
            Address  = "Not Found"
            placeid  = "Not Found"
            print(place + "\n " + lat + "\n " + lng + "\n " + Address + "\n " + placeid)
            t= Task(Place=form.title.data,Lattitude="Not Found" ,Longitude="Not Found" ,Address="Not Found",place_id="Not Found")
            flash('Data not retrieved')
            flash('Place name might be incorrect or have spelling mistakes')
            flash('Please click on Return Home and Enter correct place') 
            
        else :
            place = " " +tlist[0]
            
            if tlist[1] < 0.0 :
                lat1 = str(-1.0 *  tlist[1])
                lat = lat1 + " °S"
            elif tlist[1] > 0.0 :
                lat = str(tlist[1]) + " °N"
            else :
                lat = str(tlist[1])                        
            
            
            if tlist[2] < 0.0 :
                lng1 = str(-1.0 *  tlist[2])
                lng = lng1 + " °W"
            elif tlist[2] > 0.0 :
                lng = str(tlist[2]) + " °E"
            else :
                lng = str(tlist[2]) 
            
            Address  = tlist[3]
            placeid  = tlist[4]
            print(place + "\n " + str(lat) + "\n " + str(lng) + "\n " + Address + "\n " + placeid)
            t= Task(Place=place,Lattitude=lat ,Longitude=lng ,Address=Address,place_id=placeid)
            flash('Data retrieved')
        
        db.session.add(t)
        db.session.commit()
        return redirect(url_for('index')) 
    return render_template('add.html' ,  form = form )


@app.route('/index', methods=['GET','POST'])
def index():
    tasks = Task.query.all()
    form = forms.ReturnToHome()
    if form.validate_on_submit() :
        return redirect(url_for('add'))

    return render_template('index.html', form = form, tasks=tasks)



@app.route('/map', methods=['GET','POST'])
def map():

    form = forms.ReturnToData()
    if form.validate_on_submit() :
        return redirect(url_for('index'))
    
    return render_template('where.html', form = form)

@app.route('/index', methods=['GET','POST'])
def back():

    form = forms.OpenMap()
    if form.validate_on_submit() :
        return redirect(url_for('back'))
    
    return render_template('index.html', form = form)


