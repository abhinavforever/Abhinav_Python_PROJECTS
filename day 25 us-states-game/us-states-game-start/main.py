import turtle
import pandas
screen=turtle.Screen()
screen.title("U.S. States Game")
image="blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
data=pandas.read_csv("50_states.csv")#data is a dataframe
a = data['state'] #series of all the states
a = a.tolist() #list of all the states
print(a)
l=[] #list of all the guessed states
score=0
while len(l)!=50:
    answer_state=screen.textinput(title=f"Score: {score}/50",prompt="What's another state's name? ")
    answer_state=answer_state.title()

    if answer_state=="Exit":
        # missing_states=[]
        # for state in a:
        #     if state not in l:
        #         missing_states.append(state)
        missing_states = [state for state in a if state not in l]
        new_data=pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in a:
        if answer_state not in l:
            score+=1
            l.append(answer_state)
        t=turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data=data[data.state==answer_state]
        t.goto(int(state_data.x),int(state_data.y))
        t.write(answer_state)
#states_to_learn.csv
# with open("states_to_learn.csv",mode="r+") as file:
#     file.truncate(0)
# for state in a:
#     if state not in l:
#         with open("states_to_learn.csv",mode="a") as f:
#             f.write(f"{state}\n")