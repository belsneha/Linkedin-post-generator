import streamlit as st

# Dummy topic tag class
class FewShotPosts:
    def get_tags(self):
        return [
            "Artificial Intelligence", "Machine Learning", "Data Science", "Deep Learning",
            "Natural Language Processing", "Computer Vision", "Big Data", "Cloud Computing", "Cybersecurity",
            "Blockchain", "Web Development", "Mobile Development", "DevOps", "Startups", "Entrepreneurship",
            "Product Management", "UX/UI Design", "Career Advice", "Remote Work", "Freelancing", "Leadership",
            "Marketing", "Sales", "Software Engineering", "Tech News", "Innovation", "Agile", "AI Ethics",
            "Prompt Engineering", "SaaS", "EdTech", "FinTech", "Healthcare Tech", "Personal Branding",
            "Job Hunting", "Interview Tips", "Resume Writing", "Public Speaking", "Networking"
        ]

# Improved generation logic with length variety
def generate_post(topic, length, language):
    if language == "English":
        if length == "Short":
            return f"{topic} is booming! Stay ahead and share your take with your network. 🚀"
        elif length == "Medium":
            return (
                f"In today's tech-driven world, {topic} has become a game-changer. Professionals across industries are adopting it "
                "to enhance efficiency, solve complex problems, and stay competitive. Whether you're learning or leading, this field offers "
                "huge growth potential. Share your insights or questions to start a meaningful conversation!"
            )
        else:  # Long
            return (
                f"{topic} is no longer just a buzzword — it's transforming the way we live, work, and think. From automating tasks to enabling "
                "advanced decision-making, it's being applied in healthcare, finance, education, and beyond.\n\n"
                "For professionals, now is the perfect time to upskill in this space. Whether you're just starting or already hands-on, your "
                "journey in {topic} matters. Share your experiences, challenges, and learnings to help others grow while building your own brand.\n\n"
                "#LinkedIn #Learning #Growth #Career"
            )

    elif language == "Hinglish":
        if length == "Short":
            return f"{topic} trending hai! Kya aap bhi is field mein ho?"
        elif length == "Medium":
            return (
                f"{topic} ka use har domain mein badhta jaa raha hai. Chahe aap developer ho ya product manager, is technology ka knowledge "
                "aapke career ko next level pe le ja sakta hai. Apne thoughts LinkedIn pe share karo, aur dusron ke saath connect karo!"
            )
        else:  # Long
            return (
                f"Aaj ke time mein {topic} sirf ek technical skill nahi, ek zarurat ban chuki hai. Har company chahti hai ki unke systems smart ho, fast ho, "
                "aur data-driven decisions le sakein — aur yeh sab possible hai is technology ke through.\n\n"
                "Mujhe yaad hai jab maine pehli baar is field ko explore kiya tha, bahut excitement tha aur utne hi doubts bhi. Lekin jaise jaise maine seekhna "
                "shuru kiya, mujhe samajh aaya ki real growth wahi hoti hai jab aap continuously learn karte ho aur apne learnings ko dusron ke saath share karte ho.\n\n"
                "Aapka experience kisi ke liye motivation ban sakta hai. Share karo, inspire karo. 💡"
            )

    elif language == "Hindi":
        if length == "Short":
            return f"{topic} एक महत्वपूर्ण विषय बन गया है। क्या आप इससे जुड़े हैं?"
        elif length == "Medium":
            return (
                f"{topic} ने तकनीक की दुनिया में क्रांति ला दी है। इसके माध्यम से व्यवसाय तेज़, स्मार्ट और कुशल हो रहे हैं। "
                "यदि आप इस क्षेत्र में हैं या इसमें प्रवेश करना चाहते हैं, तो यह सही समय है सीखने और अपने अनुभव साझा करने का।"
            )
        else:  # Long
            return (
                f"{topic} वर्तमान युग में तकनीकी विकास का प्रतीक बन गया है। शिक्षा, स्वास्थ्य, वित्त और कई अन्य क्षेत्रों में इसकी उपयोगिता ने "
                "नई संभावनाओं के द्वार खोल दिए हैं। इससे न केवल कार्यक्षमता में वृद्धि हो रही है, बल्कि यह नवाचार को भी प्रोत्साहित कर रहा है।\n\n"
                "जब मैंने इस क्षेत्र में शुरुआत की, तो कई प्रश्न और संदेह थे। परन्तु अभ्यास और सीखने की प्रक्रिया ने मेरे दृष्टिकोण को विस्तार दिया। "
                "अब मैं मानता हूँ कि अपने अनुभव साझा करना न केवल दूसरों की मदद करता है, बल्कि आत्मविकास का भी एक माध्यम है।\n\n"
                "आइए इस यात्रा को साझा करें और एक-दूसरे को प्रेरित करें।"
            )

    else:
        return "Language not supported."

# Streamlit UI
st.title("LinkedIn Post Generator")

# Layout for dropdowns
col1, col2, col3 = st.columns(3)
fs = FewShotPosts()
tags = fs.get_tags()

# Dropdown inputs
with col1:
    selected_topic = st.selectbox("Select a Topic", options=tags)
with col2:
    selected_length = st.selectbox("Select Post Length", options=["Short", "Medium", "Long"])
with col3:
    selected_language = st.selectbox("Select Language", options=["English", "Hinglish", "Hindi"])

# Button and output
if st.button("Generate"):
    post = generate_post(selected_topic, selected_length, selected_language)
    st.success("✅ Generated Post:")
    st.write(post)

# Show user's selections (optional)
st.markdown("### 🔎 Your Selections:")
st.write(f"- **Topic**: {selected_topic}")
st.write(f"- **Length**: {selected_length}")
st.write(f"- **Language**: {selected_language}")
