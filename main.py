import streamlit as st

# --------------------------------
# Page Configuration
# --------------------------------
st.set_page_config(
    page_title="Password Generator by Shubham",
    page_icon="🔐",
    layout="centered"
)

# --------------------------------
# Name Lists
# --------------------------------
girl_names = [
    "pinki", "priya", "neha", "pooja", "simran",
    "ananya", "isha", "sakshi", "aisha", "shreya",
    "muskan", "sonam", "nisha", "kavya", "tanya"
]

boy_names = [
    "rahul", "rohit", "alim", "aryan", "karan",
    "varun", "aditya", "akash", "vansh", "vivek",
    "sumit", "ankit", "mohit", "nikhil", "aryan"
]

# --------------------------------
# Title
# --------------------------------
st.title("🔐 Password Generator by Shubham")
st.write("Create your password below 👇")

# --------------------------------
# Password Input
# --------------------------------
password = st.text_input(
    "Enter a password",
    type="password",
    placeholder="Type your password..."
)

# --------------------------------
# Button
# --------------------------------
if st.button("Generate Password 🔑", use_container_width=True):

    password_lower = password.lower().strip()

    # Exact cases from the meme
    if password_lower == "my dih":
        st.error("❌ Password is too long, try again.")

    elif password_lower == "bro dih":
        st.error("❌ Password is too short.")

    # Check girl's name + "dih"
    elif password_lower.endswith(" dih"):

        prefix = password_lower[:-4].strip()

        if prefix in girl_names:
            st.error("❌ Password does not exists.")

        elif prefix in boy_names:
            quotes = [
                "😂 Bro, even the password needs a little more length.",
                "💀 Bro entered a password shorter than his confidence.",
                "😭 This password needs character development.",
                "🙄 Bro, add some characters. The password is struggling.",
                "😂 That's not a password, that's a password draft."
            ]

            st.warning(quotes[len(prefix) % len(quotes)])

        else:
            st.success("✅ Password accepted!")

    else:
        st.success("✅ Password generated successfully!")

# --------------------------------
# Footer
# --------------------------------
st.divider()

st.caption("🔐 Password Generator by Shubham")
st.caption("Because apparently passwords now have personality issues 🙄")
