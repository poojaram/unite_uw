import pandas as pd
import numpy as np
import re

def is_null(variable):
    return isinstance(variable, float) and np.isnan(variable)

file = pd.read_csv("data_set.csv", encoding='latin1')
questions = [
    "App Cycle",
    "App #",
    "Timestamp",
    "Which of the following apply to you?",
    "Are you applying as a participant or a facilitator?",
    "What is your name? (first name last name)?",
    "What is your status at UW (freshman, sophomore, junior, senior, graduate student, transfer junior, etc.)?",
    "Yes, Maybe or no",
    "Note",
    "Yes, Maybe or no",
    "Note",
    "Final Decision",
    "Notes",
    "Which Early Fall Start course are you taking?",
    "I am a/an...",
    "Which country or which area are you from? (e.g. \"Leavenworth, WA\" or \"Beijing, China\")",
    "We require every participant to attend a 2-night retreat that is critical for team bonding. We leave early evening of Friday, 8/31 and return early afternoon of Sunday 9/2 (Reminder: this is the Labor Day weekend. Please plan ahead). Will you be able to make it?",
    "We require every facilitator to attend a 1-night \"mini\" facilitator retreat. We leave on early Saturday morning, 4/1 and return Sunday morning, 4/2. Will you be able to make it?",
    "Tell us about yourself and what motivates you to apply for Unite UW?",
    "Describe your own culture, and share a meaningful cultural exchange experience. (Note: At Unite UW, we try not to overgeneralize a culture based on nationalities. For example, different regions of India could have very different cultural significance.)",
    "Can you share a story when you well connected with someone who is different than you? What did you learn from this connection?",
    "Assuming you look forward to making new close friends and finding a new community at UW, what challenges do you foresee? And how can Unite UW help you overcome those challenges?",
    "Is there anything else you would like us to know about you?",
    "List potential time conflicts with Unite UW EFS '18 schedule below.",
    "How did you hear about Unite UW? (If your friend referred you, write their name.)",
    "In addition to the mandatory meetings above, you are also expected to meet your partner or your small group outside of the program. Where would you want to go and what would you like to do with your partner/group? And why?",
    "What attributes do you have to contribute to connecting international and domestic students?",
    "If qualified, would you be interested in becoming a group facilitator? Please read more about facilitator roles and time commitment and apply if desired at https://goo.gl/forms/XNKPFAxmFKTtrgVk2.",
    "(Optional) We don't want to miss any strong candidates who might not prefer writing as the best way to show who they are. So if you would like to, please send a short video to uniteuw@uw.edu, with your name in the video title.",
    "(Facilitator Only) Describe a past experience when you were responsible for initiating and facilitating a small group activity? What was the best part and what was the most challenging part?",
    "(Facilitator Only) Aside from language, what would you consider to be the biggest barriers that keep people with different cultural backgrounds (e.g. domestic and international students) from connecting with one another?",
    "(Facilitator Only) What resources, channels or networks can you utilize to promote Unite UW to other freshmen huskies?"
]


new_data = []
for index, row in file.iterrows():
    # Name
    name =  row[questions[5]]

    # Grade as numbers
    grade = row[questions[6]]
    if is_null(grade):
        grade = "Undetermined"
    elif "freshman" in grade or "Freshman" in grade:
        grade = "Freshman"
    elif "sophomore" in grade or "Sophomore" in grade:
        grade = "Sophomore"
    elif "junior" in grade or "Junior" in grade:
        grade = "Junior"
    elif "senior" in grade or "Senior" in grade:
        grade = "Senior"
    elif "graduate" in grade or "Graduate" in grade:
        grade = "Graduate"
    else:
        grade = "Undetermined"

    # Application Cycle
    app_cycle = row[questions[0]]

    # Participant vs Facilitator
    app_type = row[questions[4]]
    if "Participant" in app_type:
        app_type = "Participant"
    else:
        app_type = "Facilitator"

    # Has Name Reference
    reference = row[questions[24]]
    reference_binary = 0
    pattern = re.compile("[A-Z]{1}[a-z]+\s{1}[A-Z]{1}[a-z]+")
    if not is_null(reference):
        word_match = pattern.findall(reference)
        names = []
        not_a_name = ["Dawg", "Daze", "Hall", "Red", "Square", "Chinese",
            "Fig", "Facebook", "Friendship", "Fall", "Husky", "Email",
            "From", "Advising", "Meeting", "Session", "Student", "The",
            "University", "Website", "Program", "Leadership", "Department",
            "Community", "Transfer", "Quarter", "School", "Year", "Unite",
            "Study", "National", "Research", "Japanese", "Korean", "Indian",
            "Resident", "Videographer", "Fair", "Suite", "Institute", "Work",
            "Event", "Orientation", "President", "Ambassador", "Professor",
            "Huskies", "New", "Leader"]
        for word in word_match:
            if not any(faulty_word in word for faulty_word in not_a_name):
                names.append(word)
        if len(names) != 0 or "Dan" in reference or "Zhu" in reference:
            reference_binary = 1

    # Length of the Application
    length = 0
    written_portions = [18, 19, 20, 21, 22, 25, 26, 29, 30]
    for i in written_portions:
        if not is_null(row[questions[i]]):
            length += len(row[questions[i]])

    # Binary Variable - Video
    video = row[questions[28]]
    video_binary = 0
    if "Yes, I would like to send a video to uniteuw@uw.edu" in video:
        video_binary = 1

    # Binary Variable - Returning Student
    returning_student = row[questions[3]]
    returning_binary = 0
    if "I applied to Unite UW before but I didn't get accepted." in returning_student:
        returning_binary = 1

    new_row = [name, grade, app_cycle, app_type, reference_binary, length, video_binary, returning_binary]
    new_data.append(new_row)

# Export the new data
index = [i for i in range(len(file))]
columns = ["Name", "Grade", "Cycle", "Application Type", "Reference Exists", "Length", "Video", "Returning Student"]
new_file = pd.DataFrame(data = new_data, index=index, columns=columns)
new_file.to_csv(path_or_buf="formatted_data_set.csv")
