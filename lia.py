from calendar import weekday
from glob import glob
from turtle import onclick
from typing import Counter
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
#st.title("Enter the password")
#password = st.text_input("", type="password")
#st.form(key=password, clear_on_submit=False)

#globals:
global start
global end
global adults
global kids
global babies
global hotel

#if (password=="birman"):
    #First Questions
st.title("Eilat")
st.image("lialia.jpg")
start = int(st.selectbox("Enter the start", [10,11,12,13,14,15,16,17,18,19,20]))
end = int(st.selectbox("Enter the end", [10,11,12,13,14,15,16,17,18,19,20]))
adults = int(st.selectbox("Adults?",[2,1,3,4]))
kids = int(st.selectbox("Kids?",[0,1,2,3,4]))
babies = int(st.selectbox("Babies?",[0,1,2,3,4]))
hotel = st.selectbox("Hotel?", ["RB","KS","SP","LAG","RIV","ROG"])
NC = bool(st.selectbox("NC?",[True,False]))

num_nights = end - start

#REmarks to this
#kidsBool = st.button("Press if wanna add Kids / Babies")
#if (kidsBool):
#Some upgrades.. Nc, maybe flights.. single in dironit

# TESTS #

#total = (end-start) * 1000 
#st.success("Total: "+total)
#if total != 0:
    #st.balloons()
    #st.write(total)
#else:
#password = ""

# The real USE ---



# DATA ---- for one night: ..z: zol, ..y: yakar
#RB
RB_BEL_z = 1
RB_BEL_y = 1
RB_ROY_z = 1
RB_ROY_z = 1
#KS
KS_STD_z = 2
KS_STD_y = 2
#continue..

#EVENTS ----
#DEFining the fee in the function itself
def EVE_cocktail_10_16(start,end):
    cocktail_1_fee = 135 #define the fee of the event
    cocktail_10_16_fee = 0
    for _ in range(start,end):
        if cocktail_10_16_fee != 0:
            if _ == 10 or _ == 16:
                cocktail_10_16_fee = adults * cocktail_1_fee
        else:
            break
    return cocktail_10_16_fee
        
def EVE_soups_14(start,end):
    soups_14_fee = 0
    soups_1_fee = 70 #define the fee of the event
    for _ in range(start,end):
        if _ == 14:
            soups_14_fee = adults * soups_1_fee
    return soups_14_fee

def EVE_RB_bbq(start,end):
    bbq_12_19_ad_kd_fee = 0
    bbq_1_fee_adult = 145 #define the fee of the event
    bbq_1_fee_kid = 72 #define the fee of the event
    for _ in range(start,end):
        if _ == 12 or _ == 19:
            bbq_12_19_ad_kd_fee += bbq_1_fee_adult * adults
            bbq_12_19_ad_kd_fee += bbq_1_fee_kid * kids
    return bbq_12_19_ad_kd_fee

# Days fees
weekday = [12,13,14,15,16,19,20]
weekend = [10,11,17,18]

def WeekDaysCounter(start,end):
    Counter_weekdays = 0
    for day in range (start,end):
        if day in weekday:
            Counter_weekdays+=1
    return Counter_weekdays  

def WeekDaysENDCounter(start,end):
    Counter_weekENDdays = 0
    for day in range (start,end):
        if day in weekend:
            Counter_weekENDdays+=1
    return Counter_weekENDdays

# Hotels fees 

# Hotes discounts
# RB:
def Disc_RB(hotel):
    return 1
     
def RoomFeeRB(hotel):
    if hotel == "RB":
        pass    
        