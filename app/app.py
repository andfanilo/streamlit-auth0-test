import streamlit as st

st.title("✨ Thanks for checking in!")

if not st.experimental_user["email_verified"]:
    st.warning("Please verify your email and login back to unlock all features")

with st.sidebar:
    st.header(f"Logged in with {st.experimental_user.email}")
    if st.button("🔓 Logout"):
        st.logout(st.secrets["auth"]["redirect_uri"])
    with st.expander(
        "Checkout your `st.experimental_user` local ID Token from the Identity Provider, securely stored in a cookie that expires in 30 days"
    ):
        st.json(st.experimental_user)
    st.link_button(
        "Find Any Bug?",
        url="https://github.com/andfanilo/streamlit-auth0-test/issues",
        icon=":material/bug_report:",
        type="tertiary",
    )

st.markdown(
    "It really helps me test out [Auth0](https://auth0.com/) so I feel I can properly recommend it in my next video"
)

st.link_button(
    "Get the Source Code",
    url="https://github.com/andfanilo/streamlit-auth0-test/",
    icon=":material/code:",
)

st.markdown(
    "Ready to get your Data projects noticed? 😁 While I finish editing the video, here are a few resources"
)

st.divider()

with st.container(border=True):
    st.image("./img/fan_course.jpg")
    st.subheader("Learn Streamlit in 2 hours")
    st.markdown(
        "Watch me go through the 30 Days Challenge for all Streamlit best practices"
    )
    st.link_button(
        "**Watch the free lesson**",
        url="https://youtu.be/ydWjwxQ8fVE?si=7VtNdvceA8rqedby",
        icon=":material/event:",
        type="primary",
    )
with st.container(border=True):
    st.image("./img/fan_consulting.jpg")
    st.subheader("Subscribe to my newsletter")
    st.markdown(
        "I really need to write more emails...I'll send an email with the video when it's done!"
    )
    st.link_button(
        "**Access my emails**",
        url="https://newsletter.andfanilo.com",
        icon=":material/mail:",
        type="primary",
    )
with st.container(border=True):
    st.image("./img/fan_tea.jpg")
    st.subheader("Support the DataFan tribe")
    st.markdown(
        "Help me research, edit and share on the latest data apps with a cup of tea"
    )
    st.link_button(
        "**Buy me Gyokuro Sencha**",
        url="https://buymeacoffee.com/andfanilo",
        icon=":material/emoji_food_beverage:",
        type="primary",
    )
