import streamlit as st
import numpy as np
from pandas import DataFrame as df
import plotly.express as px

def fl(lopt,start_const,end_const,start,end):
    l = np.linspace(start,end,100)
    mask_right = (l>(start_const*lopt))*1
    mask_left = (l<(end_const*lopt))*1
    fl_output = 1-((l-lopt)/(lopt/2))**2
    fl_output = mask_right*fl_output*mask_left
    return {"Norm Force":fl_output,"Norm Length":l}

def fv(v_max,c,start,end):
    v=np.linspace(start,end,100)
    # if l<=lopt:
    out = (v_max-v)/(v_max+2.5*v)
    # else:
    # out = 1.3-0.3*(v_max-c*v_max)/(1+(c**2)*v)
    return {"Norm Force":out,"Norm Velocity":v}

st.markdown("# Assignment #3")

st.markdown("### F-L")

lopt = st.number_input("Lopt",value = 1.0)
c1,c2 = st.columns(2)
start_constant = c1.number_input("Start Constant",value = 0.5)
end_constant = c1.number_input("End Constant",value = 1.5)
start = c2.number_input("Start",value = 0.0)
end = c2.number_input("End",value = 2.0)

fl_output = fl(lopt,start_constant,end_constant,start,end)
fl_df = df(fl_output)
fl_fig = px.line(fl_df,x="Norm Length",y="Norm Force")
st.plotly_chart(fl_fig)
c1.download_button(label="Download F-L Data as CSV",data = fl_df.to_csv().encode("utf-8"),file_name='FL_Data.csv',mime='text/csv')

st.markdown("### F-V")
v_max = st.number_input("Vmax",value = 3.0)
c3,c4 = st.columns(2)
c = c3.number_input("C",value = 2.5)
start_fv = c4.number_input("Start",value = -1.0)
end_fv = c4.number_input("End",value = 0.5)
fv_output = fv(v_max,c,start_fv,end_fv)
fv_df = df(fv_output)
fv_fig = px.line(fv_df,x="Norm Velocity",y="Norm Force")
st.plotly_chart(fv_fig)
c3.download_button(label="Download F-V Data as CSV",data = fv_df.to_csv().encode("utf-8"),file_name='FV_Data.csv',mime='text/csv')