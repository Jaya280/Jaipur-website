import streamlit as st
import wikipedia
st.set_page_config(page_title="chat with us", page_icon="🐘", layout="wide")
st.markdown("<h1 style='text-align: center; color: black;'> <marquee>WELCOME TO OUR HELPDESK </marquee></h1>", unsafe_allow_html=True)

def home_page():
    st.title("Jaipur City Guide")
    st.header("Welcome to Jaipur!")
    result=wikipedia.summary("Jaipur",sentences=8)
    st.write(result) 
    # Add images of Jaipur
    st.image("pic1.jpg", caption=" Hawa Mahal", use_container_width=True)
    st.image("pic2.jpg", caption=" Amber Fort", use_container_width=True)

def chatbot_page():


    with st.container():
         st.title("Khamma Ghani!, I am JT :wave:")
         st.header("I stand here to help you through your queries regarding the Pink City- JAIPUR")

    with st.container():
       st.write("---")
    

    with st.container():
       
       st.subheader("Type your questions below!!")
    question= st.text_input('Type your questions here')
    if question!= "":
     
     st.markdown("""
                YOUR QUESTION: {question}
                """)

    with st.container():
      
      st.sidebar.header("About JT")
      st.sidebar.markdown("""JT is an intelligent chatbot that understands commands. It performs various activities and can help with your queries.""")

def law_page():
    background_image = """
<style>
[data-testid="stAppViewContainer"] > .main {
    background-image: url("https://images.unsplash.com/photo-1570747408017-38b4c5959378");
    background-size: 100vw 100vh;  
    background-position: center;  
    background-repeat: no-repeat;
}
</style>
"""

    st.markdown(background_image, unsafe_allow_html=True)
    
          
    st.title("Jaipur City Guide - Laws Page ⚖")
    
    st.header("Laws and Regulations of Jaipur")
    st.write("""
        
        
### Rajasthan Civil Courts Ordinance, 1950:

1. *Publication:*
   - Published in the Rajasthan Gazette (Raj-Patra), Extraordinary No. 160, dated January 25, 1950.

2. *Classes of Courts:*
   - Subordinate civil courts in the state of Rajasthan, namely, the Court of District Judge, the Court of the Civil Judge, and the Court of the Munsiff.

3. *Power to Fix and Alter Local Limits:*
   - State government may fix and alter the local limits of the jurisdiction of any civil court.
   - District Judge may assign civil business to Civil Judges or Munsiffs within specified local limits.
   - Civil business arising beyond local limits but within those fixed by the state government is valid.

4. *Judges of Small Causes:*
   - A judge of a Court of Small Causes appointed as a Civil Judge is considered a Civil Judge.

5. *Power to Fix Number of District Judges:*
   - State government may fix and alter the number of District Judges.
   - Appointment, vacancies, postings, and promotions among District Judges made by the Governor in consultation with the High Court.
   - Eligibility for District Judge: Must have at least seven years' experience as an advocate or pleader, recommended by the High Court for appointment.

### Jaipur Traffic Rules:

- *Essential Documents:*
  - Valid driving license, insurance certification, and Pollution Under Control (PUC) certificate are necessary.
  - Strict adherence to seat belt rules in Jaipur; traffic police enforce this rigorously.
  - Use Google traffic details for journey planning.

- *Traffic Offenses and Fines:*
  - Common offenses include fines for two-wheelers and four-wheelers, mobile usage while driving, driving without a seat belt, overspeeding, jumping a red light, and more.

### Jaipur Development Authority Building Regulations, 2020:

1. *Short Title and Commencement:*
   - Known as Jaipur Development Authority, Jaipur (Jaipur Region Building) Building Regulations, 2020.
   - Came into force on the date of publication in the Official Gazette.
   - Applies to areas falling under Jaipur Region (excluding the walled city).

2. *Definitions:*
   - Defines terms such as Act, Competent Authority, Urban Area, Fire Officer, Ground Coverage, Occupancy Certificate, Plinth, and more.

3. *Building Standards:*
   - Specifies the area of the plot, maximum ground coverage, minimum setback, and maximum height according to road right of way for residential, commercial, and institutional plots.

4. *Specific Notes:*
   - Details regarding steel floor for parking, calculation of road width, maximum height regulations, and exceptions for affordable housing.



4. *Traffic Rules 🚗:*
   - Details regarding steel floor for parking, calculation of road width, maximum height regulations, and exceptions for affordable housing.
    -Enforced by the Jaipur Traffic Police.
    -Includes adherence to speed limits, mandatory seat belt usage, and prohibition of mobile phone usage while driving.

             
 
    
5. *Cultural Etiquette 🕌:*
    - Emphasizes the importance of respectful behavior to preserve Jaipur's traditions and ethos.
    - Dress codes are applicable at religious sites to maintain the cultural integrity of the city.

6. *Heritage Conservation 🏰*
    - Specific guidelines for iconic landmarks like Hawa Mahal and Amber Fort.
    - Restrictions on photography and conservation efforts to protect architectural marvels.

7. *Environmental Regulations 🌳*
    - Restrictions on waste disposal to address environmental concerns.
    - Initiatives to reduce plastic usage and promote sustainable tourism.

8. *Public Safety during Events 🎉*
    - Measures to ensure public safety during festivals and events.
    - Crowd management and order maintenance for a secure environment.

9. *Community Involvement 👥*
    - Neighbourhood watch programs and citizen patrols complement law enforcement.
    - Fosters a sense of responsibility among residents and visitors.
             
10. *Protection of Traditional Crafts 🎨*
    - Laws to protect traditional crafts and artisans.
    - Ensures the authenticity and quality of handmade products.

11. *Business Regulations 🛍*
    - Support for local entrepreneurship through simplified licensing procedures.
    2.Measures to ensure fair business practices and quality of goods and services.

12. *Consumer Protection 🛒*
    - Emphasis on protecting consumers with laws ensuring fair business practices.
    - Quality control measures for goods and services offered in the city.

13. *Economic Prosperity 🌆*
    - Laws supporting local businesses contribute to economic vibrancy.
    - Balance between tradition and progress, enhancing the unique charm of Jaipur's markets.

14. *General Legal Landscape*
    - Reflects commitment to maintaining a harmonious balance between tradition and progress.
    - Encourages visitors to familiarize themselves with the laws for a respectful and enjoyable experience.
                                                                                                                """)


def tourism_page():
    st.title("Jaipur City Guide - Tourism Page")
    st.title("Jaipur City Guide- TOURIST ATTARACTIONS IN JAIPUR 🕌")
    st.header("Feeling out of place and not sure about what to do in Jaipur? Worry Not!!")

    with st.container():
        st.write("Jaipur is one of the few cities in India offering many places to explore and things to do. It is not uncommon for people to revisit Jaipur."
        "For first-time travelers, places to visit in Jaipur are quite sorted with Amer Fort, Jaipur City Palace, Hawa Mahal, and Nahargarh Fort, to name a few.")
        st.write("-----------------------------------------")
    
    
    with st.container():
        st.write("""
    ###Amber Palace


    The history of Amber Fort Jaipur is truly captivating, dating all the way back to 967 CE. It was Alan Sign, the ruler of the Chanda clan of Meenas, who first constructed the fort and established a settlement called Amer. 

    However, it wasn't until 1592 that Raja Man Singh of the Kachwaha clan, known as one of Emperor Akbar's nine jewels (Navratna), rebuilt Amer ka Kila on top of the original structure. Throughout the reigns of various Rajput rulers, continuous renovations were made to this magnificent fort.
    The final additions and construction of Amer Palace were completed by Sawai Jai Singh, who was a descendant of Raja Man Singh." 
    Interestingly enough, Amber Fort is also referred to as Amber Palace due to its previous name: Ambikeshwar - named after Amba Mata Temple situated atop a hill in the capital city previously known as Dhundhar. Over time, however, this name got shortened from Ambikeshwar to Amber and eventually became Amer—marking its present-day identity within Indian history.
   
    *Entry Ticket Price
    The mesmerizing Amber Fort, nestled in the heart of Rajasthan, opens its ornate gates to visitors from all corners of the globe. The ticket prices offer a glimpse into the rich history and culture that awaits inside. For foreigners, a fair price of INR 550 is set per person, ensuring an unforgettable experience. Foreign students can embark on this journey for just INR 100 each, embracing knowledge alongside exploration. Meanwhile, Indians are granted access at a mere INR 50 per person; Indian students eagerly join their compatriots for only INR 10 a piece.
            
    *Amber Fort Timings
    The timings for visitors are from 8 AM to 7 PM, offering them a golden opportunity to immerse themselves in the royal history and architectural splendor of this majestic fortress. As the morning sun bathes its honey-hued walls, tourists are welcomed into a world where time seems to stand still. From exploring the intricate carvings and delicate mirror work inside the palaces to marveling at the panoramic views of Jaipur city from its towering ramparts, Amber Fort Timings ensures that every moment spent within these ancient walls is filled with wonder and awe.

    *Beauty for the eyes- Amer Fort
    Today, Amer Fort stands proudly as one of the most sought-after tourist attractions in Jaipur during a captivating sightseeing tour. Its majestic palace boasts a rich and fascinating history that intertwines with the breathtaking beauty of its surroundings, drawing visitors from every corner of the globe. It comes as no surprise that this remarkable landmark has been honored with UNESCO's prestigious World Heritage Site designation. Not only does Amer Fort captivate tourists, but it also serves as a cherished location for Bollywood filmmakers seeking to create enchanting period movies. From Jodha Akbar to Baji Rao Mastani and Bhool Bhulaiya, this magnificent fort has left an indelible mark on Indian cinema. Additionally, exploring the fort is made even more delightful by browsing through the numerous shops nearby offering exquisite Rajasthani handicrafts and stunning home decor pieces that serve as mementos of this extraordinary experience.
    
    ******
        

    ### Elefantastic Sanctuary

    Elefantastic Sanctuary, A unique conservation project set in Amber, Jaipur, Rajasthan has been in operation since in the 2000's with a goal to provide a sanctuary & elephant rehabilitation center. Mission: To protect and conserve elephants in a natural environment and to provide a healthy and fruitful life for all those creatures under the care. The rehabilitation center is owned and managed by a former Elephant Rider (Rahul) and focuses on healthcare management only.
    
    *What the owner has to say
    Although Rehabilitation Center was established in 2012, my family involvement with elephants dates to over four generations; before the Rehabilitation Center materialized, As I pondered about the possibilities, I realized that I want to give people an insight into the lives of Asian elephants. This were are vast misconceptions across India that animals - especially elephants – are badly mistreated. I decided that I wanted to eradicate these misconceptions. This decision inspired me to start The Elefantastic.
    their page mentions- Elefantastic seeks to introduce inbound travellers to India showcasing its great hospitality, extreme geography, yummy food, kaleidoscopic culture, deep-rooted spirituality, charming souvenirs, photogenic chaos and love for animals.


    *Ticket Prices
    Daytime experience rs. 5500 per person with fun activities and a chance to meet the elephants and feed them food.
    Nightime experience- rs. 11000 per person. with the joy of a camp night with the majestic beasts.
     
    *******

    ### Hawa Mahal

    Hawa Mahal, translated as the "Palace of Winds," stands as an iconic symbol of Jaipur's rich history and architectural marvel. This stunning structure, built in 1799 by Maharaja Sawai Pratap Singh, represents Rajputana architecture at its finest.

    *Timings and Entry Fees
    Hawa Mahal welcomes visitors from 9:00 AM to 5:00 PM every day. The entry fee for Indian nationals is typically around INR 50, while for foreign tourists, it is approximately INR 200. Additionally, there might be nominal charges for photography.

    *Best Features
    One of the most captivating features of Hawa Mahal is its intricate façade adorned with 953 small windows, or 'jharokhas,' intricately designed to allow royal women to observe street festivities without being seen. The delicate latticework and ornate architecture make it a photographer's delight and a historian's treasure trove.

    *Best Time to Visit
    The best time to visit Hawa Mahal is during the early morning or late afternoon when the sunlight casts a golden hue on its sandstone façade, creating a mesmerizing sight. Moreover, visiting during the cooler months, from October to March, ensures a more comfortable exploration of this historic gem.

    *******
                 
    ### Nahargarh Fort

    Nahargarh Fort, perched atop the Aravalli Hills overlooking the Pink City of Jaipur, is a majestic testament to Rajasthan's rich history and architectural prowess. Built in 1734 by Maharaja Sawai Jai Singh II, this imposing fortress was originally constructed as a defensive stronghold to protect the city.
    Visitors to Nahargarh Fort are greeted with stunning panoramic views of Jaipur's cityscape, making it a popular destination for tourists and locals alike. The fort's intricate architecture, characterized by its massive ramparts, intricate carvings, and sprawling courtyards, offers a glimpse into the opulent lifestyle of Rajasthan's royalty.

    *Timings
    Nahargarh Fort is open to visitors from 10:00 AM to 5:30 PM on all days of the week. The entry fee for Indian nationals is typically around INR 50, while for foreign nationals, it's around INR 200. Additionally, there might be additional charges for camera usage.

    *Best Features
    One of the best parts of Nahargarh Fort is the ambiance it offers during sunset. The fort provides a breathtaking backdrop as the sun dips below the horizon, casting a warm glow over Jaipur and creating a magical atmosphere.
    The best time to visit Nahargarh Fort is during the winter months, from October to March, when the weather is pleasant and ideal for exploring the fort's expansive grounds. However, visitors should note that the fort can get crowded during peak tourist seasons, so it's advisable to arrive early to avoid long queues and enjoy the serenity of this historical marvel.

    ********* """)
         
    st.image("pic2.jpg", caption=" Amber Fort", use_column_width=True)
    st.image("elefantastic.png", caption=" Elefantastic Sanctuary", use_column_width=True)
    st.image("pic1.jpg", caption="Hawa Mahal", use_column_width=True)
    st.image("garh.jpg", caption="Nahargarh Fort", use_column_width=True)
                    
        
def healthcare_page():
    # Dummy data for doctors
    doctors_data = [
        {"name": "Dr. Ajay Kumar", "specialty": "Cardiologist", "phone": "+91 98765 43210", "image": "doctor1.jpg"},
        {"name": "Dr. Priya Sharma", "specialty": "Dermatologist", "phone": "+91 98765 43211", "image": "doctor2.jpg"},
        {"name": "Dr. Rahul Singh", "specialty": "Pediatrician", "phone": "+91 98765 43212", "image": "doctor3.jpg"},
        # Add more doctors as needed
    ]

    def main():
        st.title("Jaipur City Guide - Healthcare")

        st.header("Doctors in Jaipur")

        # Option to search doctors by specialty
        specialties = set([doctor['specialty'] for doctor in doctors_data])
        selected_specialty = st.selectbox("Select Specialty", ["All"] + list(specialties))

        for doctor in doctors_data:
            if selected_specialty == "All" or selected_specialty == doctor['specialty']:
                st.write(f"## {doctor['name']}")
                st.image(doctor['image'], width=200)  # Doctor's image
                st.write(f"*Specialty:* {doctor['specialty']}")
                st.write(f"*Phone:* {doctor['phone']}")
                if st.button(f"Book Appointment with {doctor['name']}", key=doctor['name']):
                    show_form(doctor['name'])

    def show_form(doctor_name):
        st.write(f"## Book Appointment with {doctor_name}")
        with st.form(f"appointment_form_{doctor_name}"):
            name = st.text_input("Name")
            age = st.number_input("Age", min_value=0, max_value=150, step=1)
            number = st.text_input("Phone Number")
            health_issue = st.text_area("Health Issue")
            submitted = st.form_submit_button("Submit")

            if submitted:
                # Process the form data
                st.success("Appointment Booked!")
                st.write(f"**Name:** {name}")
                st.write(f"**Age:** {age}")
                st.write(f"**Phone Number:** {number}")
                st.write(f"**Health Issue:** {health_issue}")

    if __name__ == "__main__":
        main()


def history_page():
    st.title("Jaipur City Guide - History Page")
    st.write('''# Unveiling the Enigmatic Tapestry of Jaipur's History 🏰

Welcome to the enthralling saga of Jaipur, the Pink City of India! 🇮🇳 Nestled in the heart of Rajasthan, this vibrant city pulsates with rich history, majestic forts, and tales of valor. Let's embark on an extensive journey through time, traversing the annals of Jaipur's captivating past. 🕰

## The Genesis 🌄
Jaipur, with its intricate tapestry of history, was founded in 1727 by Maharaja Sawai Jai Singh II, a visionary ruler of the Kachwaha Rajput dynasty. 🤴 Driven by a profound desire to establish a new capital, he meticulously planned the city's layout based on ancient Vedic principles of architecture and town planning. The result? A meticulously structured city adorned with pink-hued buildings, earning it the moniker "Pink City." 💖

### The Visionary Maharaja 👑
Maharaja Sawai Jai Singh II, often hailed as the architect of modern Jaipur, envisioned a city that would not only serve as a political and economic center but also reflect the splendor and magnificence of Rajputana architecture. His foresight and ingenuity laid the foundation for Jaipur's illustrious legacy, a legacy that continues to thrive centuries later. 🏰

### Vedic Principles in Architecture 🏛
Drawing inspiration from ancient Vedic texts such as the Shilpa Shastra, Maharaja Jai Singh II incorporated sacred geometrical principles and astronomical calculations into the city's design. The result was not just a city but a celestial map on earth, aligning with the movements of the stars and planets. Each structure, from the grandiose forts to the humblest dwellings, bore the imprint of divine harmony and cosmic order. 🌌

## Architectural Marvels 🏛
One cannot explore Jaipur without being utterly mesmerized by its architectural wonders. The crown jewel, the *Jaipur City Palace, stands as a resplendent testament to the city's opulence and grandeur. 🏰 The intricate detailing, sprawling courtyards, and exquisite gardens within the palace complex reflect the splendor of a bygone era. Nearby, the **Hawa Mahal* (Palace of Winds) enthralls with its unique façade adorned with 953 windows, allowing royal ladies to observe street festivities while maintaining purdah. 🪟

### The Majestic Jaipur City Palace 🕌
Built over several centuries, the Jaipur City Palace is a mesmerizing blend of Rajput, Mughal, and European architectural styles. Its opulent halls, adorned with dazzling chandeliers and intricate frescoes, transport visitors to a bygone era of royal splendor. The palace complex also houses the *Chandra Mahal* and *Mubarak Mahal*, each a testament to Jaipur's rich cultural heritage and artistic finesse. 🎨

### Exploring the Intricacies of Hawa Mahal 🌬
Standing tall amidst the bustling streets of Jaipur, the Hawa Mahal is more than just a monument; it's a symbol of architectural ingenuity and cultural pride. Designed by Lal Chand Ustad, the palace's unique honeycomb structure allows for natural ventilation, keeping the interiors cool even during scorching summers. As the gentle breeze flows through its myriad windows, one can't help but marvel at the engineering marvels of ancient India. 🌀

## Forts of Valor ⚔
Perched atop the Aravalli hills, the *Amber Fort* beckons with its imposing ramparts and majestic gateways. 🏰 Built from red sandstone and marble, this fortress encapsulates the valor and grandeur of the Rajputana warriors. Within its walls lie tales of bravery and chivalry, echoing through the corridors of time. 🔱

### A Glimpse into the Amber Fort's Storied Past 🛡
Originally built by Raja Man Singh I in the 16th century, the Amber Fort served as the seat of power for the Kachwaha Rajputs for centuries. Its strategic location, overlooking the Maota Lake, provided a formidable defense against invading forces. The fort's sprawling courtyards, intricately carved palaces, and stunning views of the surrounding landscape continue to captivate visitors from far and wide. ⛰

### Beyond the Ramparts: Exploring Jaigarh Fort 🏹
Just a stone's throw away from the Amber Fort lies the formidable Jaigarh Fort, a testament to Jaipur's martial prowess and strategic foresight. Built by Maharaja Jai Singh II, this impregnable fortress served as the royal treasury and armory, safeguarding the wealth and treasures of the Kachwaha dynasty. Today, visitors can explore its extensive network of underground tunnels, marvel at the world's largest cannon, Jaivana, and soak in panoramic views of the Jaipur skyline. 🌄

## Cultural Tapestry 🎭
Jaipur is not just a city; it's a vibrant tapestry woven with threads of diverse cultures, traditions, and festivities. The *Jaipur Literature Festival, an annual gathering of literary luminaries and enthusiasts, serves as a melting pot of ideas and creativity. 📚 Meanwhile, the **Gangaur Festival* and *Teej Festival* celebrate the spirit of love and devotion, painting the city in hues of joy and merriment. 🎉

### Jaipur Literature Festival: Where Ideas Converge 📖
Every year, the Jaipur Literature Festival transforms the Pink City into a literary utopia, attracting writers, poets, and thinkers from around the world. From thought-provoking panel discussions to lively debates and book signings, the festival offers something for everyone. As the sun sets over the historic Diggi Palace, the air is filled with the aroma of freshly printed books and the buzz of intellectual discourse. 🌅

### Embracing Tradition: The Vibrant Festivals of Jaipur 🌺
Throughout the year, Jaipur comes alive with a myriad of festivals that celebrate its rich cultural heritage and traditions. The *Gangaur Festival, dedicated to the goddess Gauri, sees women adorned in traditional attire, carrying beautifully decorated clay pots on their heads as they offer prayers for the well-being of their husbands. Similarly, the **Teej Festival* marks the onset of the monsoon season, with women singing and dancing in the streets, dressed in colorful attire. These festivals not only showcase Jaipur's vibrant culture but also serve as a reminder of the enduring bonds of community and tradition. 💃

## Modern Metropolis 🌆
While Jaipur proudly preserves its heritage, it also embraces modernity with open arms. The bustling streets teem with life, adorned with bustling bazaars, aromatic spice markets, and vibrant handicraft stalls. 🛍 Moreover, the city's burgeoning IT sector and infrastructure developments underscore its transformation into a cosmopolitan hub, poised for a bright future. 💼

### The Pulse of Urban Jaipur 🏙
Amidst the ancient palaces and forts, modern Jaipur emerges as a vibrant metropolis, pulsating with energy and dynamism. From the high-tech corridors of the Jaipur IT Park to the chic cafes
and boutique stores lining the streets of C-Scheme, the city offers a glimpse into India's rapidly evolving urban landscape. As skyscrapers pierce the Jaipur skyline, the Pink City reinvents itself, blending tradition with innovation in perfect harmony. 🌇

### Navigating the Labyrinth of Markets 🛒
No visit to Jaipur is complete without exploring its bustling markets, where centuries-old traditions meet modern-day commerce. From the vibrant chaos of Johari Bazaar, where precious gemstones and traditional jewelry gleam in the sunlight, to the aromatic alleyways of Bapu Bazaar, overflowing with colorful textiles and handicrafts, each market offers a sensory feast for the soul. As you haggle with local vendors and sample street food delights, you'll find yourself immersed in the heartbeat of Jaipur's vibrant bazaars. 🎪

## Conclusion 🌟
As we conclude our extensive journey through the annals of Jaipur's history, one thing becomes abundantly clear—the Pink City is not merely a destination; it's a living, breathing testament to India's rich cultural tapestry and indomitable spirit. 🕌 So, whether you're tracing the footsteps of royalty or immersing yourself in the city's bustling streets, Jaipur promises an experience that transcends time. 🌈✨ Its history, like its forts, stands tall and resilient, inviting travelers from around the globe to partake in its grandeur and glory. 🌍🔍 From the architectural splendor of its palaces to the vibrant tapestry of its festivals, Jaipur captivates the imagination and leaves an indelible mark on the hearts of all who visit. 🎠🌺 As the sun sets over the Aravalli hills, casting a warm glow over the Pink City, one can't help but feel a sense of awe and wonder at the enduring legacy of Jaipur, a city where history truly comes alive. 🌄🏰🌟''')


def main():
    st.sidebar.title("Pages")
    
    selected_page = st.sidebar.radio("Select a page", ["Home", "Chatbot", "Law", "Tourism","Healthcare","History"])

    if selected_page == "Home":
        home_page()
    elif selected_page == "Chatbot":
        chatbot_page()
    elif selected_page == "Law":
        law_page()
    elif selected_page == "Tourism":
        tourism_page()
    elif selected_page == "Healthcare":
        healthcare_page()
    elif selected_page =="History":
        history_page()

main()
    











