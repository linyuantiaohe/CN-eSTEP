from zoneinfo import available_timezones
import streamlit as st
import pandas as pd
from PIL import Image

st.set_page_config(
    page_title="碳中和电力技术经济政策决策分析模型",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'About': "Work hard!"
    }
)

st.title('碳中和电力技术经济政策决策分析模型 V1.0')
st.markdown('该程序用于生成模型情景文件并提交服务器运行。')

st.header(":blue[请依次选择并提交宏观情景-技术情景-政策情景]", divider='rainbow')
st.sidebar.markdown("@Copyright 华北电力大学 王歌课题组")
st.sidebar.markdown("欢迎提出意见和建议!")
st.sidebar.markdown("E-mail: wangge@ncepu.edu.cn")

a=1

col1, col2, col3 = st.columns(3)

with col1:
    with st.container(border=True):
        st.subheader("1. Marcoeconomics Scenario\n(宏观情景)")
        st.markdown("#### 1.1. Power demand")
        st.markdown("#### 1.1. 用电量")

        st.markdown("#### 1.2. Discount rate")
        st.markdown("#### 1.2. 折现率")
        discount_rate = st.slider('Select the discount rate', min_value=0.0, max_value=0.3, value=0.08, step=0.01, format='%.2f')
        st.write('Discount rate:', discount_rate)

        if st.button("Submit Marcoeconomics Scenario", type="primary", use_container_width=True):
            st.success('Marcoeconomics scenario submitted!')
            st.markdown(':red[**Please check:**]')
            st.write('Discount rate:', discount_rate)
            a=2



with col2:
    with st.container(border=True):
        st.subheader("2. Technology Scenario\n(技术情景)")
        st.markdown("#### 2.1. Available Power Technology")
        st.markdown("#### 2.1. 可用的发电技术")
        st.markdown("可以排除生物质, 海上风电, CCUS等技术, 但会保留常规的燃煤, 燃气, 核电, 水电, 陆上风电, 光伏.")
        conventional_techs = ['COAL', 'GAS', 'NUCLEAR', 'HYDRO', 'PV', 'OnWIND']
        other_techs = []
        st.markdown(
            'What technologies do you want to considered besides conventional technologies?')

        use_biomass = st.toggle('Biomass', value=True)
        use_ccus = st.toggle('CCUS', value=True)
        use_offwind = st.toggle('OffShore Wind', value=True)

        if use_biomass:
            other_techs.append('BIOMASS')
        if use_ccus:
            if use_biomass:
                other_techs = other_techs+['COALwCCS', 'GASwCCS', 'BIOMASSwCCS']
            else:
                other_techs = other_techs+['COALwCCS', 'GASwCCS']
        if use_offwind:
            other_techs.append('OffWIND')

        st.markdown("### 2.2. Available Storage Technology")
        st.markdown("### 2.2. 可用储能技术")
        st.markdown("选择可以在需求侧使用的储能技术.")

        use_li = st.toggle('Short duration Li battery', value=True)
        use_flow = st.toggle('Middle duration Flow battery', value=True)
        use_hydrogen = st.toggle('Long duration Hydrogen storage', value=True)

        available_storage_techs=[]
        if use_li:
            available_storage_techs.append('Li')
        if use_flow:
            available_storage_techs.append('Flow')
        if use_hydrogen:
            available_storage_techs.append('Hydrogen')

        st.markdown("#### 2.3. Learning rates in technology progress")
        st.markdown("#### 2.3. 新兴技术进步率")

        st.markdown("技术进步率情景, 可选择保守, 中等, 激进.")
        tech_prog_option = st.selectbox(
            'Which technology progress scenario do you want?',
            ('Conservative', 'Moderate', 'Advanced'))

        if st.button("Submit Technology Scenario", type="primary", use_container_width=True):
            st.success('Technoloy scenario submitted!')
            st.markdown(':red[**Please check:**]')
            st.write('Available power technologies: ', conventional_techs+other_techs)
            st.write('Available storage technologies: ', available_storage_techs)
            st.write('Technology progress scenario: ', tech_prog_option)
            available_techs = conventional_techs+other_techs
            tech_prog_sce = {'Conservative': 'PC',
                             'Moderate': 'PM', 'Advanced': 'PA'}[tech_prog_option]
            tech_scenario = 1
            a=3
        else:
            tech_scenario = -1

with col3:
    st.subheader("3. Policy Scenario\n(政策情景)")
    st.write(a)