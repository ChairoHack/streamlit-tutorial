import streamlit as st
import time

st.title('Streamlit入門')

st.write('プログレスバーの表示')
bar_status = st.empty()
bar_status.text('Start!!')

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1) 
    time.sleep(0.1)
bar_status.text('Done!!')

left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラム')

expander1 = st.expander('問い合わせ1')
expander1.write('問い合わせ内容を書く')
expander2 = st.expander('問い合わせ2')
expander2.write('問い合わせ内容を書く')
expander3 = st.expander('問い合わせ3')
expander3.write('問い合わせ内容を書く')

# text = st.text_input('あなたの趣味を教えて下さい。')
# condition = st.slider('あなたの今の調子は？', 0, 100, 50)

# 'あなたの趣味：', text
# 'コンディション：', condition


# if st.checkbox('Show Image'):
#     img = Image.open('pags.jpg')
#     st.image(img, caption='Pags', use_column_width=True)
