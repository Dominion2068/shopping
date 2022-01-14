import streamlit as st
from PIL import Image
from streamlit_player import st_player


st.set_page_config(page_title="Online Shops",page_icon='🛍️')

# st.markdown(""" <style>
# #MainMenu {visibility: hidden;}
# footer {visibility: hidden;}
# </style> """, unsafe_allow_html=True)

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)


# padding = 0
# st.markdown(f""" <style>
#     .reportview-container .main .block-container{{
#         padding-top: {padding}rem;
#         padding-right: {padding}rem;
#         padding-left: {padding}rem;
#         padding-bottom: {padding}rem;
#     }} </style> """, unsafe_allow_html=True)

col1, col2, col3, = st.columns([0.5, 1, 0.5])
#col2.image('img6.jpg',use_column_width=True, width=300,caption = '')
col2.header("The Market Link")

col1, col2 = st.columns(2)
col1.subheader('ORI TIWA Skin Care Product')
col1_expander = col1.expander('Enter Shop1: ORI TIWA')
with col1_expander:
    logo = Image.open('./ori/006.jpg')
    st.image(logo, use_column_width=True, caption = '')
    st.markdown("""----""")
    if st.button('Product Description'):
        st.markdown("*ORItiwa is a mixture of Shea Butter with different natural ingredients that makes your skin smooth and glowing. It is suitable for all skin types.*")
        st.markdown("*ORItiwa Shea butter provides a soothing relief for itchy, flaky and dry skin. It's moisturizing properties help hydrate itchy skin caused by dryness while the strong anti bacterial properties will fight off germs that cause itchiness.*")
        st.markdown('*We look after your skin; your beauty is enhanced with our product*')
    if st.button('Close Description'):
        st.empty()
    st.markdown("""----""")
    st.image('./ori/003.jpg',  use_column_width=True, caption = 'Skin that glows: Funmi Collins Adepegba(CEO)')
    st.markdown('**Dispelling the misconceptions and emphasizing on the benefits**')
    st_player('https://www.facebook.com/funmmy.collins/videos/10222680622144870/',height=290)
    
    #col1, col2, col3 = st.columns(3)
    first = Image.open('./ori/001.jpg')
    second = Image.open('./ori/004.jpg')
    #third = Image.open('./ori/002.jpg')
    st.image(first, use_column_width=True,caption='')
    st.image(second, use_column_width=True,caption='')
    #st.image(third, use_column_width=True,caption='Yeah')
    st.markdown("""----""")
    st.markdown('**Testimonies: The Effectiveness of ORI TIWA**')
    st_player('https://www.facebook.com/funmmy.collins/videos/10222468645965598/',height=150)
    st_player('https://www.facebook.com/funmmy.collins/videos/10219501931439589/')
    st_player('https://www.facebook.com/funmmy.collins/videos/10222802233625081/',height=290)
    st_player('https://www.facebook.com/funmmy.collins/videos/10222731451935583/')
    
    

    st.markdown("""----""")
    #st.markdown('**Order Form**')
    contact_form = """
    <form action="https://formsubmit.co/oritiwabeautyproducts@gmail.com" method="POST">
    <input type="hidden" name="_captcha" value="false">
    <input type="text" name="name" placeholder= "Your name" required>
    <input type="email" name="email" placeholder= "Your email" required>
    <input type="text" name="phone" placeholder= "mobile phone" required>
    <input type="text" name="order" placeholder= "product name and quantity requested">
    <input type="text" name="delivery" placeholder= "Pick-up or Drop-off?">
    <input type="text" name="location" placeholder= "drop-off location">
    <textarea name="message" placeholder= "Your message here"></textarea>
    <button type="submit">Send Order</button>
    </form>
    """
    st.markdown('**Prices**')
    st.markdown('- 1 litre: N3000')
    st.markdown('- 400ml: N1500')
    if st.button('Order Form: Ori Tiwa'):
        st.markdown('**Order form for Ori Tiwa**')
        st.markdown(contact_form, unsafe_allow_html = True)
        #use local css file
        def local_css(file_name):
            with open(file_name) as f:
                st.markdown(f'<style>{f.read()}</style>',unsafe_allow_html = True)   

        local_css('style/style.css')
        #st.write('click Send before you reset')
    
    
    if st.button('Contact Details: Ori Tiwa'):
        st.write('*Location: 15, Ogunsehinde Street, Ketu Lagos; Phone and WhatsApp: +234 803 585 8020*')
        st.markdown('[Facebook](https://www.facebook.com/groups/655539858236060/?ref=share)')
        st.markdown('[Instagram](https://www.instagram.com/ori_tiwa/)')
        st.markdown('Note: We deliver within and outside Nigeria, Contact us for resell and bulk purchases')
    
    if st.button('Reset'):
        st.empty()
    
    
    




col2.subheader('Maranatha Outfits')
col2_expander = col2.expander('Enter Shop2: Maranatha')
with col2_expander:
    col2_expander.image('./per/020.jpg', use_column_width=True,caption = '')
    if st.button('Product Descriptions'):
        st.markdown('*Maranatha Outfits (Maranatha Tie & Dye) is your go-to place for best quality hand dyed t-shirts and materials in yardages for that outfit that stands you out in gatherings.*')
        st.markdown('*We care about the environment and Mother Earth 🌍, and we take our recycling ♻️ and upcycling very serious. Rather than increase the trash problem, change your old, faded clothes to brand new, and enjoy many more great years of use out of them. Tees, jeans, skirts, shirts, bedsheets, table clothes, tapestries, we renew them all.*')
    if st.button('Close'):
        st.empty()
    st.markdown("""-----""")
    st.markdown('**From Ordinary to Extraordinary**')
    st.markdown("""-----""")
    first = Image.open('./per/017.jpg')
    second = Image.open('./per/016.jpg')
    third = Image.open('./per/018.jpg')
    st.subheader('Jackets')
    st.image(first, use_column_width=True,caption='Extend the lifespan of your jackets')
    st.image(third, use_column_width=True,caption='')
    st.markdown("""-----""")
    st.subheader('T-shirts makeovers')
    st.image(second, use_column_width=True,caption='Renew your t-shirts')
    if st.button('Enlarge T-Shirts View'):
        st.image(second,width=500,caption= '')
        third = Image.open('./per/010.jpg')
        fourth = Image.open('./per/015.jpg')
        fifth = Image.open('./per/026.jpg')
        sixth = Image.open('./per/007.jpg')
        two = Image.open('./per/025.jpg')
        one = Image.open('./per/028.jpg')
        st.image(sixth,width=500,caption= '')
        st.image(third, width=500,caption='')
        st.image(fourth,width=500,caption= '')
        st.image(fifth,width=500,caption= '')
        st.image(two,width=500,caption= '')
        st.image(one,width=500,caption= '')

    

    # if st.button('Reset T-Shirts to Default'):
    #     st.empty()
    st.markdown("""-----""")

    st.subheader('Hoodies')
    
    seven = Image.open('./per/004.jpg')
    eight = Image.open('./per/008.jpg')
    st.image(seven, use_column_width=True,caption='Amazing....right!!!!')
    st.image(eight,use_column_width=True,caption= '')
    
    st.markdown("""-----""")
    st.subheader('Shirts')
    shirt1 = Image.open('./per/002.jpg')
    st.image(shirt1, use_column_width=True,caption="Trendy!!!!....isn't it?")

    
    if st.button('Reset to Continue'):
        st.empty()
        #caching.clear_cache()
    #     eight = Image.open('./per/008.jpg')
    #     ten = Image.open('./per/009.jpg')
    #     st.image(eight,width=500,caption= '')
    #     st.image(ten,width=500,caption= '')
    #     st.empty()

    if st.button('View More Shirts'):
        eight = Image.open('./per/008.jpg')
        ten = Image.open('./per/009.jpg')
        shirt2 = Image.open('./per/006.jpg')
        shirt3 = Image.open('./per/011.jpg')
        shirt4 = Image.open('./cloth/016.jpg')
        shirt5 = Image.open('./cloth/008.jpg')
        shirt6 = Image.open('./cloth/014.jpg')
        shirt7 = Image.open('./cloth/018.jpg')
        st.image(shirt2,width=500,caption= '')
        st.image(shirt3,width=500,caption= '')
        st.image(shirt4,width=500,caption= '')
        st.image(shirt5,width=500,caption= '')
        st.image(shirt6,width=500,caption= '')
        st.image(shirt7,width=500,caption= '')
        st.image(shirt1,width=500,caption= '')

    st.markdown("""-----""")
    #st_player('https://www.facebook.com/maranathacolours/videos/848017566088447/')

    # Gallery
    st.subheader('Shun the bandwargon,be the trend!!!!!')
    if st.button('Reset to Proceed'):
        st.empty()
    if st.button('Be the Trend Gallery..'):
        g1 = Image.open('./per/024.jpg')
        g2 = Image.open('./per/022.jpg')
        g3 = Image.open('./per/003.jpg')
        g4 = Image.open('./per/020.jpg')
        g5 = Image.open('./per/029.jpg')
        g6 = Image.open('./per/018.jpg')
        g7 = Image.open('./per/027.jpg')
        g8 = Image.open('./per/023.jpg')
        g9 = Image.open('./per/001.jpg')
        ten = Image.open('./per/009.jpg')
        st.image(g4,width=500,caption= '')
        st.image(g1,width=500,caption= '')
        st.image(g2,width=500,caption= '')
        st.image(g3,width=500,caption= '')
        st.image(g5,width=500,caption= '')
        st.image(g6,width=500,caption= '')
        st.image(g7,width=500,caption= '')
        st.image(g8,width=500,caption= '')
        st.image(g9,width=500,caption= '')
        st.image(ten,width=500,caption= '')
    if st.button('Reset to Default Page'):
        st.empty()

    st.markdown("""----""")
    if st.button('View Prices'):
        st.markdown('**Brocade Fabrics**')
        st.markdown('- N2500 per yard')
        st.text('')
        st.markdown('**T shirts (V neck and Round neck)**')
        st.markdown('- XL/XXL N6000')
        st.markdown('- Large N6000')
        st.markdown('- Medium N5000')
        st.markdown('- Small N5000')
        st.text('')
        st.markdown('**Hoodies**')
        st.markdown('- XL/XXL N15000')
        st.markdown('- Large N14000')
        st.markdown('- Medium N13000')
        st.markdown('- Small N13000')
        st.text('')
        st.markdown('**Jackets**')
        st.markdown('- XL/XXL N14000')
        st.markdown('- Large N13000')
        st.markdown('- Medium N12000')
        st.markdown('- Small N12000')
        st.text('')
        st.markdown('**Renewal/Recycling ♻️**')
        st.markdown('- An item such as tees, shirt , jeans, skirt  is N2000')
        st.markdown('- Complete natives #4000 (excluding agbada)')
        st.markdown('Other items are negotiable')
    if st.button('Clear Prices'):
        st.empty()
    st.markdown("""----""")

    #st.markdown('**Order Form**')
    contact_form = """
    <form action="https://formsubmit.co/maranathacolours@gmail.com" method="POST">
    <input type="hidden" name="_captcha" value="false">
    <input type="text" name="name" placeholder= "Your name" required>
    <input type="email" name="email" placeholder= "Your email" required>
    <input type="text" name="phone" placeholder= "mobile phone" required>
    <input type="text" name="order" placeholder= "product name and quantity requested">
    <input type="text" name="delivery" placeholder= "Pick-up or Drop-off?">
    <input type="text" name="location" placeholder= "drop-off location">
    <textarea name="message" placeholder= "Your message here"></textarea>
    <button type="submit">Send Order</button>
    </form>
    """
    if st.button("Order Form: Maranatha Outfits"):
        st.markdown('**Order form for Maranatha Outfits**')
        st.markdown(contact_form, unsafe_allow_html = True)
        #use local css file
        def local_css(file_name):
            with open(file_name) as f:
                st.markdown(f'<style>{f.read()}</style>',unsafe_allow_html = True)   

        local_css('style/style.css')
        #st.write('click Send before you reset')
    
    
    if st.button('Contact Details: Maranatha Outfits'):
        st.write('*Location: 12, Sanusi Ajilete Street, Off College Road Ogba Lagos; Phone:+234 802 825 9456 and WhatsApp: +234 809 825 9456*')
        st.markdown('[Facebook](https://www.facebook.com/maranathacolours/)')
        st.markdown('[Instagram](https://www.instagram.com/maranathacolours_76/)')
        st.markdown('Note: We deliver within and outside Nigeria, delivery fees apply')
    if st.button('Reset Order Form'):
        st.empty()
    
    # if st.button('Reset All'):
    #     pyautogui.hotkey('ctrl','F5')

st.write('')
st.markdown("""----""")    
col1, col2, col3, = st.columns([0.5, 1, 0.5])
col2.write('*Developer: Dominion Research Solutions*')
col2.write('*32, Admiralty Way Lekki Phase1 Lagos*')

#st.markdown('**Order Form**')
contact_form = """
<form action="https://formsubmit.co/dominionresearchsolutions@gmail.com" method="POST">
<input type="hidden" name="_captcha" value="false">
<input type="text" name="name" placeholder= "Your name" required>
<input type="email" name="email" placeholder= "Your email" required>
<input type="text" name="phone" placeholder= "mobile phone" required>
<textarea name="message" placeholder= "Your message here"></textarea>
<button type="submit">Send Order</button>
</form>
"""

if col2.button('Contact Developer'):
    #st.markdown('**Order form for Maranatha Outfits**')
    col2.markdown(contact_form, unsafe_allow_html = True)
    #use local css file
    def local_css(file_name):
        with open(file_name) as f:
            st.markdown(f'<style>{f.read()}</style>',unsafe_allow_html = True)   

    local_css('style/style.css')
col2.write('')
if col2.button('Close FORM'):
    st.empty()
    

