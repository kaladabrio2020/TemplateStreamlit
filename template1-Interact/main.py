import pandas  as pd

import streamlit as st

import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(layout="wide")

st.markdown("""
<style>

.block-container
{
    padding-top: 2rem;
    padding-bottom: 0rem;
    margin-top: 2rem;
}

</style>
""", unsafe_allow_html=True)


card1, card2, card3 = st.columns([1, 1, 1],border=True, vertical_alignment='bottom')

with card1: st.metric("Metric 1", "1,234")
with card2: st.metric("Metric 2", "1,234")
with card3: st.metric("Metric 3", "1,234")


fig11 = go.Figure([
    go.Scatter(x=[1, 2, 3], y=[4, 5, 6])
])
fig11.update_layout(
    height=300,
    title = dict(
        text='Oi',
        automargin=True
    ), 
    margin=dict(l=0, r=0, t=50, b=0)
)

fig12 = go.Figure([
    go.Bar(x=["A", "B", "C"], y=[1, 2, 3]),
])
fig12.update_layout(
    height=300, 
    title = dict(
        text='Oi',
        automargin=True
    ),
    margin=dict(l=0, r=0, t=50, b=0)
)

fig13 = go.Figure([
    go.Pie(labels=["A", "B", "C"], values=[1, 2, 3]),
])
fig13.update_layout(
    height=300, 
    title = dict(
        text='Oi',
        automargin=True
    ),
    margin=dict(l=0, r=0, t=50, b=0)
)


col1, col2, col3 = st.columns([3, 2, 2], border=True, vertical_alignment='center')
col1.plotly_chart(fig11, key="fig11")
col2.plotly_chart(fig12, key="fig12")
col3.plotly_chart(fig13, key="fig13")


col1, col2, col3 = st.columns([2, 3, 1.5], border=True, vertical_alignment='center')
col1.plotly_chart(fig11, key="fig21")
col2.plotly_chart(fig12, key="fig22")
col3.plotly_chart(fig13, key="fig23")