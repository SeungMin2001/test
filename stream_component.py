import streamlit as st

#-------------------------------------
# TEXT
#Title
st.title("Streamlit Basics")

# #Header
st.header("This is a header")

# #Subheader
# st.subheader("This is a subheader")

# #Text
# 단순성: 주로 단순한 문자열을 표시하는 데 사용됩니다. 입력된 문자열을 그대로 출력합니다.
# 포매팅 없음: 입력된 텍스트를 그대로 출력하며, Markdown이나 HTML 등의 구문을 해석하지 않습니다.
# 고정된 형식: 항상 일반 텍스트 형식으로 출력됩니다
#st.text("This is a simple text")

# #Write
# st.write
# 유연성: 다양한 데이터 유형을 처리할 수 있습니다. 단순한 문자열뿐만 아니라 DataFrame, Markdown, HTML, LaTeX, JSON 등의 여러 데이터 형식을 렌더링할 수 있습니다.
# 자동 형식 지정: 입력 데이터의 유형에 따라 자동으로 적절한 형식을 지정합니다. 예를 들어, DataFrame을 입력하면 표 형식으로 출력하고, Markdown 문자열을 입력하면 Markdown 구문을 렌더링합니다.
# 다양한 입력: 문자열, 숫자, 리스트, 딕셔너리, DataFrame 등 다양한 데이터 타입을 지원합니다.
#st.write("This is a write dimension")

#-------------------------------------

# st.header("Markdown and HTML")

# #Markdown
# # Hyperlinks
st.markdown("https://www.streamlit.io")
st.markdown("[Streamlit](https://www.streamlit.io)")

#-------------------------------------

# #HTML
html_page = """
<div style="background-color:blue;padding:50px">
	<p style="color:yellow;font-size:5'px">Enjoy Streamlit!</p>
</div>
"""

# st.markdown(html_page, unsafe_allow_html=True)

#-------------------------------------
st.success("Success!")
# st.info("Information")
# st.warning("This is a warning")
# st.error("This is an error!")

#-------------------------------------
# st.header("Images, Video and Audio")

# #Image
# from PIL import Image
# img = Image.open("packt.jpeg")
# st.image(img, width=300, caption="Packt Logo")

# #Video
# video_file = open("SampleVideo_1280x720_1mb.mp4","rb")
# video_bytes = video_file.read()
# st.video(video_bytes)

# #Video from an URL
# st.video("https://www.youtube.com/watch?v=q2EqJW8VzJo")

# #Audio
# audio_file = open("sample1.mp3","rb")
# audio_bytes = audio_file.read()
# st.audio(audio_bytes)

# st.header("Widgets")
#-------------------------------------

# #Button
# if st.button("Play"):
# 	st.text("Hello World!")

# #Checkbox
# if st.checkbox("Checkbox"):
# 	st.text("Checkbox selected")

# #Radio Button
radio_but = st.radio("Your Selection", ["A", "B"])
if radio_but == "A":
	st.info("You selected A")
else:
	st.info("You selected B")


# #Selectbox
# city = st.selectbox("Your City", ["Napoli", "Palermo", "Catania"])

# #Multiselect
# occupation = st.multiselect("Your Occupation", ["Programmer", "Data Scientist", "IT Consultant", "DBA"])

# #TEXT Input
# 단일 행 입력: 단일 행의 텍스트를 입력받는 데 사용됩니다. 사용자가 입력할 수 있는 텍스트 필드가 한 줄로 제한됩니다.
# 주 사용 사례: 이름, 이메일 주소, 단일 라인으로 된 짧은 텍스트 입력을 받을 때 유용합니다.
# 기본 제공 옵션: 기본값 설정, 플레이스홀더(입력 필드에 표시될 힌트 텍스트) 설정 등이 가능합니다.
# name = st.text_input("Your Name", "Write something...")
# st.text(name)

# # #NUMBER Input
# age = st.number_input("Input a number")

# # #TEXT Area
# 다중 행 입력: 여러 행의 텍스트를 입력받는 데 사용됩니다. 사용자가 여러 줄의 텍스트를 입력할 수 있도록 큰 입력 상자를 제공합니다.
# 주 사용 사례: 피드백, 댓글, 설명 등 긴 텍스트 입력이 필요한 경우에 적합합니다.
# 기본 제공 옵션: 기본값 설정, 플레이스홀더 설정, 줄 수 지정 등이 가능합니다.
# message = st.text_area("Your Message", "Write something...")

# # #SLIDER
# select_val = st.slider("Select a Value", 1, 10)

# # #BALLOONS
# if st.button("ballons"):
# 	st.balloons()

# st.header("Dataframes and Tables")

# import pandas as pd
# df = pd.read_csv("auto.csv")
# st.dataframe(df.head(10))

# st.table(df.head(10))


# #PLOTTINGS
# st.area_chart(df[["mpg","cylinders"]])
# st.bar_chart(df[["mpg",	"cylinders"]].head(20))
# st.line_chart(df[["mpg","cylinders"]].head(20))

# #SEABORN
# import matplotlib.pyplot as plt
# import seaborn as sns

# fig, ax = plt.subplots()
# corr_plot = sns.heatmap(df[["mpg","cylinders", "displacement"]].corr(), annot = True)
# st.pyplot(fig)

#Date and Time
# st.header("Date & Time")

# import datetime

# today = st.date_input("Today is", datetime.datetime.now())


# import time 

# hour = st.time_input("The time is", datetime.time(12,30))


#DISPLAY JSON CODE
# data = {"name":"John","surname":"Wick"}
# st.json(data)

# #Displaying CODE
# st.code("import pandas as pd")

# julia_code = """
# function doit(num::int)
# 	println(num)
# end
# """

# st.code(julia_code, language='julia')


# st.header("Progress Bar and Spinner")

# #Progress Bar
# import time

# my_bar = st.progress(0)
# for value in range(100):
# 	time.sleep(1)
# 	my_bar.progress(value+1)

# #SPINNER
import time

with st.spinner("Please wait..."):
	time.sleep(10)
st.success("Done!")