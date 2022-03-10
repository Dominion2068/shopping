import streamlit as st
from PIL import Image
from streamlit_player import st_player
import json
import requests
from streamlit_lottie import st_lottie


st.set_page_config(page_title="Online Shops",page_icon='🛍️')

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# hide_st_style = """
#             <style>
#             #MainMenu {visibility: hidden;}
#             footer {visibility: hidden;}
#             header {visibility: hidden;}
#             </style>
#             """
# st.markdown(hide_st_style, unsafe_allow_html=True)


# padding = 0
# st.markdown(f""" <style>
#     .reportview-container .main .block-container{{
#         padding-top: {padding}rem;
#         padding-right: {padding}rem;
#         padding-left: {padding}rem;
#         padding-bottom: {padding}rem;
#     }} </style> """, unsafe_allow_html=True)

#lottie_shops = load_lottieurl('https://assets10.lottiefiles.com/private_files/lf30_9kdbftpx.json')


col1, col2, col3, = st.columns([0.5, 1, 0.5])
# col2.image('img6.jpg',use_column_width=True, width=300,caption = '')
# st_lottie(lottie_shops, height=200)
col2.header("Online Shopping Link")

st.write('----')  
  
col1, col2 = st.columns(2)
col1.markdown('**ORI TIWA** Skin Care Product')
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
    # def load_lottiefile(filepath: str):
    #     with open(filepath, 'r') as f:
    #         return json.load(f)
    # lottief = load_lottiefile('order-now.json')
    
    #height=, width=
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
    # lottie_buy = load_lottieurl('https://assets2.lottiefiles.com/packages/lf20_pMgZwk.json')
    if st.button('Show Prices'):
        st.markdown('**Prices**')
        st.markdown('- 1 litre: N3000')
        st.markdown('- 400ml: N1500')
        st_lottie(lottie_buy, height=100)
    
    st.markdown("""----""")

    # def load_lottieurl(url: str):
    #     r = requests.get(url)
    #     if r.status_code != 200:
    #         return None
    #     return r.json()
    
    # lottie_deliver = load_lottieurl('https://assets2.lottiefiles.com/packages/lf20_d3chs3uh.json')
    
    
    
    if st.button('Place Your Orders for Ori Tiwa'):
        st.markdown(contact_form, unsafe_allow_html = True)
        #use local css file
        def local_css(file_name):
            with open(file_name) as f:
                st.markdown(f'<style>{f.read()}</style>',unsafe_allow_html = True)   

        local_css('style/style.css')
        st.markdown('**Delivery Available**')
        st_lottie(lottie_deliver)
    
    
    if st.button('Contact Details: Ori Tiwa'):
        st.write('*Location: 15, Ogunsehinde Street, Ketu Lagos; Phone and WhatsApp: +234 803 585 8020*')
        st.markdown('[Facebook](https://www.facebook.com/groups/655539858236060/?ref=share)')
        st.markdown('[Instagram](https://www.instagram.com/ori_tiwa/)')
        st.markdown('Note: We deliver within and outside Nigeria, Contact us for resell and bulk purchases')
    
    if st.button('Reset'):
        st.empty()
    

    




col2.markdown('**Maranatha** Outfits')
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
    
    if st.button('Reset to Proceed'):
        st.empty()
    st.subheader('Shun the bandwagon,be the trend!!!!!')
    
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
    # if st.button('Reset to Default Page'):
    #     st.empty()

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
    # if st.button('Clear Prices'):
    #     st.empty()
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

    # def load_lottieurl(url: str):
    #     r = requests.get(url)
    #     if r.status_code != 200:
    #         return None
    #     return r.json()
    
    # lottie_order = load_lottieurl('https://assets1.lottiefiles.com/packages/lf20_jejpizop.json')
    # lottie_delivery = load_lottieurl('https://assets2.lottiefiles.com/packages/lf20_cpkrjlxq.json')
    # lottie_thanks = load_lottieurl('https://assets3.lottiefiles.com/private_files/lf30_zjkforca.json')
    # st_lottie(lottie_order)

    # lottiem = load_lottiefile('order-now.json')
    # st_lottie(lottiem)
    
    if st.button("Place Your Orders for Maranatha Outfits"):
        st.markdown('**Order form for Maranatha Outfits**')
        st.markdown(contact_form, unsafe_allow_html = True)
        #use local css file
        def local_css(file_name):
            with open(file_name) as f:
                st.markdown(f'<style>{f.read()}</style>',unsafe_allow_html = True)
                  

        local_css('style/style.css')
        
        st.markdown('**Delivery Available**')
        # st_lottie(lottie_delivery)
        
        

    if st.button('Reset Order Form'):
        st.empty()


    if st.button('Contact Details: Maranatha Outfits'):
        st.write('*Location: 12, Sanusi Ajilete Street, Off College Road Ogba Lagos; Phone:+234 802 825 9456 and WhatsApp: +234 809 825 9456*')
        st.markdown('[Facebook](https://www.facebook.com/maranathacolours/)')
        st.markdown('[Instagram](https://www.instagram.com/maranathacolours_76/)')
        #st.markdown('Note: We deliver within and outside Nigeria, delivery fees apply')
    
    
    # if st.button('Reset All'):
    #     pyautogui.hotkey('ctrl','F5')
#col1, col2 = st.columns(2)

#st.write('----')
st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)

# st.markdown('**Josephine Wears** Women Clothing Line')
from annotated_text import annotated_text
col1.header('Josephine Wears')
colj_expander = col1.expander('Enter Shop3: Josephine Wears')
with colj_expander:
    # colj_expander.image('./jos/j20.jpg', use_column_width=True,caption = '')
    st.write('----')

    
    contact_form = """
    <form action="https://formsubmit.co/josephinewears@hotmail.com" method="POST">
    <input type="hidden" name="_captcha" value="false">
    <input type="hidden" name="Order Form" value="For Josephine Wears">
    <input type="text" name="name" placeholder= "Your name" required>
    <input type="email" name="email" placeholder= "Your email" required>
    <input type="text" name="phone" placeholder= "Mobile Phone" required>
    <input type="text" name="order" placeholder= "Design Name and Quantity Requested">
    <input type="text" name="delivery" placeholder= "Pick-up or Drop-off?">
    <input type="text" name="location" placeholder= "Drop-off Location">
    <textarea name="message" placeholder= "Message and or Mearsurements here"></textarea>
    <button type="submit">Send</button>
    </form>
    """
    def buy():
        st.markdown('----')
        st.write('''Kindly fill to: 
   
1. Invite us for measurement or presentation
2. Send your measurements
3. Order or buy any of the designs
4. Ask questions''')
        st.write('''Call or WhatsApp us directly on:    
**+234 8034858131**''')
        st.markdown(contact_form, unsafe_allow_html = True)
        #use local css file
        def local_css(file_name):
            with open(file_name) as f:
                st.markdown(f'<style>{f.read()}</style>',unsafe_allow_html = True)
        local_css('style/style.css')

    
    vendor_form = """
    <form action="https://formsubmit.co/josephinewears@hotmail.com" method="POST">
    <input type="hidden" name="_captcha" value="false">
    <input type="hidden" name="Vendor/Distributor/Marketer Form" value="For Josephine Wears">
    <input type="text" name="name" placeholder= "Your name" required>
    <input type="email" name="email" placeholder= "Your email" required>
    <input type="text" name="phone" placeholder= "Mobile Phone" required>
    <input type="text" name="Preferred Design" placeholder= "Design Name" required>
    <input type="text" name="name" placeholder= "Your Country or State in Nigeria">
    <textarea name="message" placeholder= "Your Brief Profile Here"></textarea>
    <button type="submit">Send</button>
    </form>
    """
    def vendor():
        st.markdown('----')
        st.markdown(vendor_form, unsafe_allow_html = True)
        #use local css file
        def local_css(file_name):
            with open(file_name) as f:
                st.markdown(f'<style>{f.read()}</style>',unsafe_allow_html = True)
        local_css('style/style.css')



    def contact():
        st.markdown('----')
        st.write('''**Office Address:**

32, Fred Williams Street, Station Bus Stop, Iju Road, Fagba, Lagos''')
        st.write('''Call or WhatsApp us directly on:    
**+234 8034858131**''')
        st.write('Email: josephinewears@hotmail.com')
        st.write('**Social Media Pages:**')
        st.markdown('[Facebook](https://www.facebook.com/groups/2519407625043523/?ref=share)')
        st.markdown('[Instagram](https://www.instagram.com/josephinewears_)')
        
    
    comment_form = """
    <form action="https://formsubmit.co/josephinewears@hotmail.com" method="POST">
    <input type="hidden" name="_captcha" value="false">
    <input type="hidden" name="Contact or Suggestion Form" value="For Josephine Wears">
    <input type="email" name="email" placeholder= "Your email">
    <textarea name="message" placeholder= "Your suggestions here"></textarea>
    <button type="submit">Send Suggestions</button>
    </form>
    """
    def comment():
        st.markdown('----')
        st.write('''*Your feedback on this category of designs and your insights on fashion will be appreciated. 
        Kindly fill the comments or suggestions form below and click send*''')
        st.markdown(comment_form, unsafe_allow_html = True)
        #use local css file
        def local_css(file_name):
            with open(file_name) as f:
                st.markdown(f'<style>{f.read()}</style>',unsafe_allow_html = True)
        local_css('style/style.css')
    
    def det():
        st.write('''*This section will contain a short video describing this design
        the inspiration behind it, the possible materials usage, type of occasions, available variants etc*''')

    st.write('''FIND THE DESIGN FOR YOUR BODY TYPE HERE

Every woman is beautifully made, however it is important to take note of your body size and type when choosing a dress. 
Your body shape should determine what style that best suits you and not forcing a style to suit your body type.''')

    body = Image.open('./jos/body.jpg')
    st.image(body, use_column_width=True,caption='')


    st.write('''A style or design might look great on somebody else that you think you could have the same. Some customers are gifted with creativity that they create their own designs and or know what’s best for them. Not all customers have this ability. 
    If you find yourself in the latter, your best bet is to get a designer that can connect with you and help you build your wardrobe for all functions. Even if you don’t make clothes but buy off the hangers, 
    you still need a stylist or fashion expert to guide you through.
    
Josephine Wears Company is a garment production company producing fashionable apparels and dainty designs.
Our products are durable, never colors, weather friendly and of good quality. Our designs are world-class
we put great care and creativity towards ensuring that we compare with the best designs elsewhere.
''')
    
    md = Image.open('./jos/MD.jpg')
    st.image(md, use_column_width=True,caption='Josephine Ogar MD/CEO')

    original = Image.open('./jos/j18.jpg')
    original2 = Image.open('./jos/j18a.jpg')
    annotated_text(('MERMAID',"#e3e4e8"))
    heiress1 = Image.open('./jos/j26d.jpg')
    heiress2 = Image.open('./jos/j26a.jpg')
    heiress3 = Image.open('./jos/j17.jpg')
    st.image(original,use_column_width=True,caption = 'Damask and Tinted Organza Layered Dress') 
    
    jos1 = st.radio(label = 'Click to check out more about the Mermaid', options = ['Mermaid Details','Mermaid Serenade','Enlarge Mermaid',
                                                                'Mermaid Gallery','What do you think?','Place Your Orders for Mermaid',
                                                               'Contact Details','I Want to be a Marketer or Distributor'])
    
    if jos1 == 'Mermaid Serenade':
        annotated_text(('MERMAID Serenade',"#e3e4e8"))
        st.image(original2, use_column_width=True,caption='')
       
    
    if jos1 == 'Enlarge Mermaid':
        st.image(original2, width=500,caption= '')
    
    if jos1 == 'Mermaid Details':
        st.write('''*A fitted dress with several layers of organza flared around the knee. 
        A very good traditional marriage attire. A special evening wear and Sunday attire.*''')
    
    if jos1 == 'Place Your Orders for Mermaid':
        #st.write('Kindly fill to invite us for measurement and or presentation')
        buy()
        contact()

    if jos1 == 'Mermaid Gallery':
        st.write('')

    if jos1 == 'What do you think?':
        comment()
    
    if jos1 == 'Contact Details':
        contact()
    
    if jos1 == 'I Want to be a Marketer or Distributor':
        vendor()
        
    st.markdown('----')

    annotated_text(('HEIRESS',"#FFFFFF"))
    st.image(heiress1,use_column_width=True,caption = 'Gold Trimmings on Duchess')
    annotated_text(('Tulle GROOVE',"#RSPQZZ"))
    st.image(heiress3,use_column_width=True,caption = 'Blend of Tulle and Satin Embellished with Roses') 
    jos2 = st.radio(label = 'Click to check out more about the Heiress', options = ['Heiress Details','Back View',
                                                                    'Enlarge Heiress','Heiress Gallery',
                                                                    'What do you think?','Place Your Orders for Heiress',
                                                               'Contact Details', 'I Want to be a Marketer or Distributor'])
    
    if jos2 == 'Heiress Details':
        st.write('For all children events and occasions: party, school, wedding etc.')

    if jos2 == 'Back View':
        annotated_text(('HEIRESS Back View',"#FFFFFF"))
        st.image(heiress2, use_column_width=True,caption='')
        
        
    if jos2 == 'Enlarge Heiress':
        st.image(heiress1, width=500,caption= '')
        st.image(heiress2, width=500,caption='')
        annotated_text(('Tulle GROOVE',"#RSPQZZ"))
        st.image(heiress3, width=500,caption='')
        st.write('*Scroll back up to continue with Heiress*')
    
    if jos2 == 'Place Your Orders for Heiress':
        buy()
    
    if jos2 == 'Heiress Gallery':
        st.write('')
        
    if jos2 == 'What do you think?':
        comment()
   
    if jos2 == 'Contact Details':
        contact()
    
    if jos2 == 'I Want to be a Marketer or Distributor':
        vendor()

    st.markdown('----')

    eve1 = Image.open('./jos/j3a.jpg')
    eve2 = Image.open('./jos/j3b.jpg')
    eve3 = Image.open('./jos/j42.jpg')
    eve4 = Image.open('./jos/j43.jpg')
    annotated_text(('EVE',"#123466"))
    st.image(eve2,use_column_width=True,caption = 'Adult Tulle Ruffled Dress Embelished with Sequin Around the Waist')
    annotated_text(('BRIDAL',"#123466"))
    st.image(eve3,use_column_width=True,caption = 'Adult Tulle Dress with Lace') 
    jos3 = st.radio(label = 'Click to check out more about Eve', options = ['Eve Details','Another View',
                                                                    'Enlarge Eve','Eve Gallery',
                                                                    'What do you think?','Place Your Orders for Eve',
                                                               'Contact Details','I Want to be a Marketer or Distributor'])

    if jos3 == 'Eve Details':
        st.write('Adult party dress suitable for events like weddings, graduation etc')

    if jos3 == 'Another View':
        annotated_text(('EVE 2',"#123466"))
        st.image(eve1, use_column_width=True,caption='')
        st.image(eve4, use_column_width=True,caption='')
        
        
    if jos3 == 'Enlarge Eve':
        st.image(eve1, width=500,caption= '')
        st.image(eve3, width=500,caption='')
        st.image(eve4, width=500,caption='')
        #st.image(eve3, width=500,caption='')
        st.write('*Scroll back up to continue Eve*')
    
    if jos3 == 'Place Your Orders for Eve':
        buy()
    
    if jos3 == 'Eve Gallery':
        st.write('')
        
    if jos3 == 'What do you think?':
        comment()
    
    if jos3 == 'Contact Details':
        contact()
    
    if jos3 == 'I Want to be a Marketer or Distributor':
        vendor()


    st.markdown('----')
    annotated_text(('PRINCESS AND BARBIE RANGE',"#147466"))
    st.markdown('----')

    princess1 = Image.open('./jos/j20.jpg')
    princess2 = Image.open('./jos/j11a.jpg')
    barbie = Image.open('./jos/j2a.jpg')
    annotated_text(('PRINCESS-A',"#147466"))
    st.image(princess1,use_column_width=True,caption = 'Organza blended with lace')
    annotated_text(('PRINCESS-B',"#147466"))
    st.image(princess2, use_column_width=True,caption='Embellished Tulle Layered Dress')
    annotated_text(('BARBIE',"#147466"))
    st.image(barbie, use_column_width=True,caption='Tulle and Lace Combo')
    jos4 = st.radio(label = 'Click to check out more about the Princess', options = ['Princess Details','Another View',
                                                                    'Enlarge Princess','Princess Gallery',
                                                                    'What do you think?','Place Your Orders for Princess',
                                                               'Contact Details','I Want to be a Marketer or Distributor'])

    if jos4 == 'Princess Details':
        st.write('Flower girl, bridal train, school party, wedding guest, birthday wear, kiddies party')

    if jos4 == 'Another View':
        st.write('*Coming in a bit! To contain other views of the Princess Design*')
        
        
    if jos4 == 'Enlarge Princess':
        annotated_text(('PRINCESS-A',"#147466"))
        st.image(princess1, width=500,caption= '')
        annotated_text(('PRINCESS-B',"#147466"))
        st.image(princess2, width=500,caption='')
        annotated_text(('BARBIE',"#147466"))
        st.image(barbie, width=500,caption='')
        st.write('*Scroll back up to continue with Princess*')
    
    if jos4 == 'Place Your Orders for Princess':
        buy()
    
    if jos4 == 'Princess Gallery':
        st.write('')
        
    if jos4 == 'What do you think?':
        comment()

    if jos4 == 'Contact Details':
        contact()

    if jos4 == 'I Want to be a Marketer or Distributor':
        vendor()


    st.markdown('----')

    annotated_text(('ANKARA RANGE',"#147466"))
    st.markdown('----')
    sisi1 = Image.open('./jos/j10a.jpg')
    sisi2 = Image.open('./jos/j10b.jpg')
    sisi3 = Image.open('./jos/j31.jpg')
    sisi4 = Image.open('./jos/j33.jpg')
    sisi5 = Image.open('./jos/j36.jpg')
    sisi6 = Image.open('./jos/j37.jpg')
    sisi7 = Image.open('./jos/j32.jpg')
    #sisi8 = Image.open('./jos/j39.jpg')
    annotated_text(('SISI-A',"#122336"))
    st.image(sisi1,use_column_width=True,caption = 'Embellished Ankara Fitted Flared Dress')
    annotated_text(('SISI-B',"#147466"))
    st.image(sisi2, use_column_width=True,caption='Ankara Layered Dress')
    annotated_text(('ANKARA FREESTYLE-A',"#147466"))
    st.image(sisi3, use_column_width=True,caption='Nice Combo of 2 Different Ankara')
    annotated_text(('ANKARA FREESTYLE-B',"#237169"))
    st.image(sisi4, use_column_width=True,caption='Short Ankara Dress')
    annotated_text(('PRINTEX',"#147466"))
    st.image(sisi5, use_column_width=True,caption='Full Flared Ankara Dress Embellished with Simple Trimmings to Highlight the Background')
    annotated_text(('PRINTEX CREPE',"#888888"))
    st.image(sisi6, use_column_width=True,caption='Occasional Evening Dress')
    jos5 = st.radio(label = 'Click to check out more about the Ankara Range', options = ['Ankara Details','Another View',
                                                                    'Enlarge Ankara','Ankara Gallery',
                                                                    'What do you think?','Place Your Orders for Ankara',
                                                               'Contact Details','I Want to be a Marketer or Distributor'])

    if jos5 == 'Ankara Details':
        st.write('For all traditional events: Owanbes, traditional weddings, church events, occassional events etc.')

    if jos5 == 'Another View':
        st.write('*Coming in a bit! To contain other views of the Sisi Design*')
        
        
    if jos5 == 'Enlarge Ankara':
        annotated_text(('SISI-A',"#122336"))
        st.image(sisi1, width=500,caption= '')
        annotated_text(('SISI-B',"#147466"))
        st.image(sisi2, width=500,caption='')
        annotated_text(('ANKARA FREESTYLE',"#147466"))
        st.image(sisi3, width=500,caption='')
        annotated_text(('ANKARA FREESTYLE',"#147466"))
        st.image(sisi4, width=500,caption='')
        annotated_text(('PRINTEX',"#147466"))
        st.image(sisi5, width=500,caption='')
        annotated_text(('PRINTEX CREPE',"#888888"))
        st.image(sisi6, width=500,caption='')
        st.text('Scroll back up to continue')
        color = st.color_picker('pick')

    if jos5 == 'Place Your Orders for Ankara':
        buy()
    
    if jos5 == 'Ankara Gallery':
        st.image(sisi7,use_column_width=True,caption = '''Nice Combo of 2 Different Ankara''')
        #st.image(sisi8,use_column_width=True,caption = '''The Chic body 'hugger' ''')
        
    if jos5 == 'What do you think?':
        comment()

    if jos5 == 'Contact Details':
        contact()
    
    if jos5 == 'I Want to be a Marketer or Distributor':
        vendor()

    st.markdown('----')

    annotated_text(('EVENING DRESS RANGE',"#147466"))
    st.markdown('----')
    belle1 = Image.open('./jos/j27.jpg')
    belle2 = Image.open('./jos/j23.jpg')
    annotated_text(("GLAM","#74FF6G"))
    st.image(belle2, use_column_width=True,caption='Lace/Crepe Combo Evening Dress')
    annotated_text(('THE GALE Evening Dress',"#799913"))
    st.image(belle1,use_column_width=True,caption = 'Gold Lace/Raw Silk')
    jos6 = st.radio(label = 'Click to check out more about Glam and Gale', options = ['GLAM AND GALE Details','Another View of GLAM AND GALE',
                                                                    'Enlarge the GLAM AND GALE','The GLAM AND GALE Gallery',
                                                                    'What do you think?','Place Orders for GLAM AND GALE',
                                                               'Contact Details','I Want to be a Marketer or Distributor'])

    if jos6 == 'GLAM AND GALE Details':
        st.write('''*For evening events, Sunday attire, naming ceremony,
        can be worn as a wedding guests, or a chief bridesmaid.
        The Gale is a an elegant timeless that can be worn for evening events musical awards, wedding, graduation
        ceremony and traditional events*''')

    if jos6 == 'Another View or GLAM AND GALE':
        st.write('*Coming in a bit! To contain other views of the Sisi Design*')
        
        
    if jos6 == 'Enlarge the GLAM AND GALE':
        annotated_text(('GLAM',"#147466"))
        st.image(belle2, width =500,caption= 'Lace/Crepe Combo Evening Dress')
        annotated_text(('THE GALE Evening Dress',"#799913"))
        st.image(belle1, width =500,caption = 'Gold Lace/Raw Silk')
        st.write('Scroll back up to continue with The GLAM AND GALE')
    
    if jos6 == 'Place Orders for GLAM AND GALE':
        buy()
    
    if jos6 == 'The GLAM AND GALE Gallery':
        st.write('')
        
    if jos6 == 'What do you think?':
        comment()
    
    if jos6 == 'Contact Details':
        contact()
    
    if jos6 == 'I Want to be a Marketer or Distributor':
        vendor()
    
    st.markdown('----')
    annotated_text(('THE BODY CON RANGE',"#147466"))
    st.markdown('----')
    body1 = Image.open('./jos/j28.jpg')
    body2 = Image.open('./jos/j13.jpg')
    body3 = Image.open('./jos/j8.jpg')
    body4 = Image.open('./jos/j5.jpg')
    body5 = Image.open('./jos/j16.jpg')
    body6 = Image.open('./jos/j21.jpg')
    body7 = Image.open('./jos/j29.jpg')
    body8 = Image.open('./jos/j30.jpg')
    annotated_text(('BODY CON-A',"#222233"))
    st.image(body1,use_column_width=True,caption = 'Formal yet so chic')
    annotated_text(("BODY CON-B","#764333"))
    st.image(body2, use_column_width=True,caption='Body Con with Side Pleats and Sleeves')
    annotated_text(("BODY CON-C","#XXXXXX"))
    st.image(body3, use_column_width=True,caption='''The Chic body 'hugger' ''')
    #annotated_text(('BODY CON-C',"#691090"))
    # st.image(body7,use_column_width=True,caption = 'Spandex formal/casual dress. Slighted side knee flare attaced for more glam')
    jos7 = st.radio(label = 'Click to check out more about the Body Con', options = ['Body Con Details','Another View',
                                                                    'Enlarge the Body Con','The Body Con Gallery',
                                                                    'What do you think?','Place Your Orders for Body Con',
                                                               'Contact Details','I Want to be a Marketer or Distributor'])

    if jos7 == 'Body Con Details':
        st.write('''*The Body Con range of designs is flexible and adaptable to your event needs as they come in 
        both formal and casual wears - office, dinner, hangouts, simple parties. Specifically designed to 
        accentuates the body curves. Check the Body Con Gallery for more designs*''')

    if jos7 == 'Another View':
        st.write('*Coming in a bit! To contain other views of the Sisi Design*')
        
        
    if jos7 == 'Enlarge the Body Con':
        #annotated_text(('THE BELLE OF THE BALL-A',"#799913"))
        #st.image(belle1, width=500,caption= 'Gold Lace/Raw Silk')
        annotated_text(('GLAM',"#147466"))
        st.image(belle2, width=500,caption= 'Lace/Crepe Combo Evening Dress')
        st.write('Scroll back up to continue with The Belle')
    
    if jos7 == 'Place Your Orders for Body Con':
        buy()
    
    if jos7 == 'The Body Con Gallery':
        #st.image(body3,use_column_width=True,caption = '''The Chic body 'hugger' ''')
        st.image(body4,use_column_width=True,caption = '''Curves 'Showcaser' for every woman''')
        st.image(body5,use_column_width=True,caption = 'Formal dress with cascading ruffles attached to one side to accentuate the hips')
        st.image(body6,use_column_width=True,caption = 'The Body Con Feel Fly')
        st.image(body7,use_column_width=True,caption = 'Spandex formal/casual dress. Slighted side knee flare attaced for more glam')
        st.image(body8,use_column_width=True,caption = 'Body Con Graduation')

    if jos7 == 'What do you think?':
        comment()
    
    if jos7 == 'Contact Details':
        contact()
    
    if jos7 == 'I Want to be a Marketer or Distributor':
        vendor()
    
    st.markdown('----')
    annotated_text(('THE BOSS RANGE',"#147466"))
    st.markdown('----')
    boss1 = Image.open('./jos/j6.jpg')
    boss5 = Image.open('./jos/j34.jpg')
    boss2 = Image.open('./jos/j22.jpg')
    boss3 = Image.open('./jos/j25.jpg')
    boss4 = Image.open('./jos/j38.jpg')
    annotated_text(('THE BOSS GLAM',"#888777"))
    st.image(boss1,use_column_width=True,caption = 'Embellished Ankara Fitted Flared Dress')
    annotated_text(('BABY STEPHEN',"#888777"))
    st.image(boss5,use_column_width=True,caption = 'Embellished Ankara Fitted Flared Dress')
    annotated_text(('THE BOSS-A',"#888777"))
    st.image(boss2, use_column_width=True,caption='Ankara Layered Dress')
    annotated_text(('THE BOSS-B',"#888777"))
    st.image(boss3, use_column_width=True,caption='Nice Combo of 2 Different Ankara')
    annotated_text(('THE BOSS-C',"#888777"))
    st.image(boss4, use_column_width=True,caption='Flora Crepe, Formal/Casual Wear')
    jos8 = st.radio(label = 'Click to check out more about the Boss', options = ['The Boss Details','Another View',
                                                                    'Enlarge The Boss','The Boss Gallery',
                                                                    'What do you think?','Place Your Orders for The Boss',
                                                               'Contact Details','I Want to be a Marketer or Distributor'])

    if jos8 == 'The Boss Details':
        st.write('Hybrid designs that allows you to seamlessly fit into formal and informal occassions or events')

    if jos8 == 'Another View':
        st.write('*Coming in a bit! To contain other views of The Boss Designs*')
        
        
    if jos8 == 'Enlarge The Boss':
        annotated_text(('THE BOSS GLAM',"#888777"))
        st.image(boss1, width=500,caption= '')
        annotated_text(('BABY STEPHEN',"#888777"))
        st.image(boss5, width=500,caption= '')
        annotated_text(('THE BOSS-A',"#888777"))
        st.image(boss2, width=500,caption='')
        annotated_text(('THE BOSS-B',"#888777"))
        st.image(boss3, width=500,caption='')
        annotated_text(('THE BOSS-C',"#888777"))
        st.image(boss4, width=500,caption='')
        st.write('Scroll back up to continue with The Boss')
        color = st.color_picker('pick')

    if jos8 == 'Place Your Orders for The Boss':
        buy()
    
    if jos8 == 'The Boss Gallery':
        st.write('')
        
    if jos8 == 'What do you think?':
        comment()
    
    if jos8 == 'Contact Details':
        contact()
    
    if jos8 == 'I Want to be a Marketer or Distributor':
        vendor()


    st.markdown('----')
    annotated_text(('MUMS RANGE',"#147466"))
    st.markdown('----')
    mum1 = Image.open('./jos/j4a.jpg')
    mum2 = Image.open('./jos/j40.jpg')
    mum3 = Image.open('./jos/j41.jpg')
    annotated_text(("MUMS-A","#KKKKKK"))
    st.image(mum1, use_column_width=True,caption='Velvet and Lace')
    annotated_text(("MUMS-B","#KKKKKK"))
    st.image(mum2, use_column_width=True,caption='Full lace flared maternity dress, wrap bodice for easy breastfeeding')
    annotated_text(('MUMS-C',"#KKKKKK"))
    st.image(mum3,use_column_width=True,caption = 'Flared maternity dress made with soft damask and very rich sequin fabric')
    jos9 = st.radio(label = 'Click to check out more about Mums', options = ['Mums Details','Another View of Mums',
                                                                    'Enlarge Mums','Mums Gallery',
                                                                    'What do you think?','Place Your Orders for Mums',
                                                               'Contact Details','I Want to be a Marketer or Distributor'])

    if jos9 == 'Mums Details':
        st.write('''*Suitable dress for all pregnant and breastfeeding mothers *''')

    if jos9 == 'Another View of Mums':
        st.write('*Coming in a bit! To contain other views of the Sisi Design*')
        
        
    if jos9 == 'Enlarge Mums':
        annotated_text(('MUMS-A',"#147466"))
        st.image(mum1, width =500,caption= '')
        annotated_text(('MUMS-B',"#799913"))
        st.image(mum2, width =500,caption = '')
        annotated_text(('MUMS-C',"#799913"))
        st.image(mum3, width =500,caption = '')
        st.write('Scroll back up to continue with MUMS')
    
    if jos9 == 'Place Your Orders for Mums':
        buy()
    
    if jos9 == 'Mums Gallery':
        st.write('')
        
    if jos9 == 'What do you think?':
        comment()

    if jos9 == 'Contact Details':
        contact()
    
    if jos9 == 'I Want to be a Marketer or Distributor':
        vendor()


st.write('')
st.markdown("""----""")    
col1, col2, col3, = st.columns([0.5, 1, 0.5])
col2.write('*Developer: Dominion Research Solutions*')
col2.write('*32, Admiralty Way Lekki Phase1 Lagos*')




#st.markdown('**Order Form**')
contact_form = """
<form action="https://formsubmit.co/dominionresearchsolutions@gmail.com" method="POST">
<input type="hidden" name="_captcha" value="false">
<input type="hidden" name="__next" value="https://share.streamlit.io/dominion2068/shopping/main/shop.py/thanks.html">
<input type="hidden" name="Contact or Suggestion Form" value="For Dominion Reserach Solutions">
<input type="text" name="name" placeholder= "Your name" required>
<input type="email" name="email" placeholder= "Your email" required>
<input type="text" name="phone" placeholder= "mobile phone" required>
<textarea name="message" placeholder= "Your message here"></textarea>
<button type="submit">Send</button>
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
if col2.button('Close Contact Form'):
    st.empty()