import streamlit as st
import pandas as pd

# 데이터 불러오기
df = pd.read_csv('nobel_winners.csv')

# 데이터 유형 및 누락 데이터 처리
df['Year'] = df['Year'].astype(int)
df['Category'] = df['Category'].str.strip()
df['Nationality'] = df['Nationality'].fillna('')
df['Motivation'] = df['Motivation'].fillna('')
df['Explain'] = df['Explain'].fillna('')


# 사이드바 필터
st.sidebar.header('필터 옵션')
year = st.sidebar.selectbox('수상 연도', sorted(df['Year'].unique()), index=0)
category = st.sidebar.selectbox('수상 부문', sorted(df['Category'].unique()), index=0)

# 필터링된 데이터
filtered_df = df[(df['Year'] == year) & (df['Category'] == category)]

# 메인 화면에 데이터 표시
if not filtered_df.empty:
    for index, row in filtered_df.iterrows():
        st.markdown(row['Explain'], unsafe_allow_html=True)
        
else:
    st.write('해당 조건에 맞는 수상자가 없습니다.')

