import streamlit as st
import random


def play_game(user_choice):
    choices = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(choices)
    
    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        result = "You win!"
    else:
        result = "You lose!"
    
    return user_choice, computer_choice, result


if "wins" not in st.session_state:
    st.session_state.wins = 0
    st.session_state.losses = 0
    st.session_state.ties = 0


st.title("🎮 Rock Paper Scissors Game")


st.write("Choose your weapon below and see if you can beat the computer!")

choices = {'rock': '✊ Rock', 'paper': '✋ Paper', 'scissors': '✌️ Scissors'}
user_choice = st.radio(
    "Your Choice:",
    options=list(choices.keys()),
    format_func=lambda x: choices[x],
    horizontal=True,
)


if st.button("Play"):
    with st.spinner('Computer is choosing...'):
        user, computer, result = play_game(user_choice)

        
        if result == "You win!":
            st.session_state.wins += 1
        elif result == "You lose!":
            st.session_state.losses += 1
        else:
            st.session_state.ties += 1

        
        col1, col2 = st.columns(2)
        with col1:
            st.write("**Your Choice:**")
            st.image(f"{user}.png", width=150)
        with col2:
            st.write("**Computer's Choice:**")
            st.image(f"{computer}.png", width=150)

        
        if result == "You win!":
            st.image("winner.gif", use_column_width=True)
        elif result == "You lose!":
            st.image("loser.gif", use_column_width=True)
        else:
            st.image("tie.gif", use_column_width=True)


st.write("---")
st.write("### Scores:")
st.write(f"**Wins:** {st.session_state.wins}")
st.write(f"**Losses:** {st.session_state.losses}")
st.write(f"**Ties:** {st.session_state.ties}")


st.write("---")
st.markdown("<p style='text-align: center;'>Made with ❤️ using Streamlit</p>", unsafe_allow_html=True)
