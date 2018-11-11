# Unite UW

The recruitment process in our project refers to the overall process of attracting students to apply to the program, and then shortlisting and selecting the most suitable ones for the program every quarter. After discussing with our community partner, Olivia Dan Zhu (danz2@uw.edu), we formulated the following as our goal for this project: We are finding the most effective strategy to rank candidates based on the following criteria -
* Commitment towards the program
* Open-minded and curiosity to learn new cultures
* Balanced proportion of Extroverts and Introverts
* Geographical diversity and cultural background

## Getting Started

In order to run the program, you must have the information of the applicants in a csv file. The file on the applicants for the quarter must include the following in formation in column format:
* Which of the following apply to you?
* Are you applying as a participant or a facilitator?
* What is your name? (first name last name)?
* What is your status at UW (freshman, sophomore, junior, senior, graduate student, transfer junior, etc.)?
* First review results
* First reviewer comment
* Second review results
* Second reviewer comment
* Final Decision
* Final reviewer comment
* Which Early Fall Start course are you taking?
* International or Domestic
* Which country or which area are you from? (e.g. "Leavenworth, WA" or "Beijing, China")
* Available for the 2 day required retreat?
* Available for the 1 day facilitator's retreat?
* Tell us about yourself and what motivates you to apply for Unite UW?
* Describe your own culture, and share a meaningful cultural exchange experience.
* Can you share a story when you well connected with someone who is different than you?
* What challenges do you foresee in Unite UW?
* Is there anything else you would like us to know about you?
* List potential time conflicts with Unite UW schedule.
* How did you hear about Unite UW?
* Small group or partner activity idea
* Personal attributes to connect to club members?
* If qualified, would you be interested in becoming a group facilitator?
* Video Response
* (Facilitator Only) Describe a past experience when you were responsible for initiating and facilitating a small group activity? What was the best part and what was the most challenging part?
* (Facilitator Only) Aside from language, what would you consider to be the biggest barriers that keep people with different cultural backgrounds from connecting with one another?
* (Facilitator Only) What resources, channels or networks can you utilize to promote Unite UW to other freshmen huskies?
* (Facilitator Only) If you are not selected as a facilitator, will you consider to be a participant?

Then, run the following code:
```
python run_assessment.py file_name.csv
```
The resulting ranking of the applicants and the scores for the respective areas of the applicant will show in a file named "file_name_result.csv". Here are the 4 categories where we score the applicants:
1. Commitment to the Club
2. Open-Mindedness
3. Balanced Personalities
4. Geographical Diversity

Note that the scores can be explicitly specified by the following command:
```
python run_assessment.py file_name.csv 1 2 1 1
```
The four parameters after the file name represents the four weights for the respective categories mentioned above. Note that the default values for the weights are all ones.


## Built With

* [Python](https://www.python.org/downloads/) - The language used
* [Doc2Vec](https://github.com/jhlau/doc2vec) - The sentiment analysis software used

## Authors

* **Aaron Beomjun Bae** - *Initial work* - [University of Washington](https://github.com/aaronbae)
* **Aman Arya** - *Initial work* - [University of Washington](https://github.com/aarya22)
* **Pooja Ramanathan** - *Initial work* - [University of Washington](https://github.com/PurpleBooth)

## Acknowledgments
