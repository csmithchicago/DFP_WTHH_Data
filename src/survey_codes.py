"""
this is used to create a mapping of questions in the survey data
CONSENT
"""

import json

metadata_dict = {
    "votereg": {
        "question": "Are you registered to vote?",
        "1": "Yes",
        "2": "No TERMINATE",
        "3": "Don't know TERMINATE",
    },
    "gender": {"question": "What is your gender?", "1": "Male", "2": "Female"},
    "birthyr": {"question": "In what year were you born?"},
    "CONSENT": {
        "question": "Did they give consent to participate?",
        "1": "Yes",
        "0": "No",
    },
    "educ": {
        "question": "What is the highest level of education you have completed?",
        "1": "Did not graduate from high school",
        "2": "High school graduate",
        "3": "Some college, but no degree (yet)",
        "4": "2-year college degree",
        "5": "4-year college degree",
        "6": "Postgraduate degree (MA, MBA, MD, JD, PhD, etc.)",
    },
    "race": {
        "question": "What racial or ethnic group best describes you?",
        "1": "White",
        "2": "Black or African-American",
        "3": "Hispanic or Latino",
        "4": "Asian or Asian-American",
        "5": "Native American",
        "8": "Middle Eastern",
        "6": "Mixed Race",
        "7": "Other",
    },
    "hispanic": {
        "question": "Are you of Spanish, Latino, or Hispanic origin or descent?",
        "1": "Yes",
        "2": "No",
    },
    "pp18_votelikely": {
        "question": (
            "On Tuesday, November 6 (ONCE IT IS NOVEMBER 1ST SHOULD"
            'SAY "This Tuesday" AND ON NOVEMBER 6TH IT SHOULD SAY '
            '"Today"), there will be midterm elections for Congress'
            "and other offices. How likely is it that you will vote "
            "in this election?"
        ),
        "title": "How likely is it that you will vote in this election?",
        "1": "Definitely will vote (TAKING EVERYONE)",
        "2": "Probably will vote (TAKING EVERYONE)",
        "3": "Maybe will vote (SOME VOTE HISTORY SCREEN)",
        "4": "Probably won't vote (TERMINATE)",
        "5": "Definitely will not vote (TERMINATE)",
        "7": "Already voted early in-person",
        "8": "Already voted by mail or absentee",
        "6": "Don't know (SOME VOTE HISTORY SCREEN)",
    },
    "senvote18": {
        "question": (
            "(ASK ONLY IN 2018 SENATE STATES) (IF NOT ALREADY VOTED) If "
            "the election for U.S. Senator of (state) were being held "
            "today, whom would you vote for?"
            "(IF ALREADY VOTED) In the election for U.S. Senator of "
            "(state), whom did you vote for?"
        ),
        "title": "In the election for U.S. Senator whom did/will you vote for?",
        "1": "Candidate's name (Democrat)",
        "2": "Candidate's name (2nd Democrat, if applicable)",
        "3": "Candidate's name (Republican)",
        "5": "Candidate's name (Independent, if applicable)",
        "7": "Other candidate",
        "15": "Undecided",
        "16": "I would not vote",
        "17": "Prefer not to say",
    },
    "senvote18_undecided": {
        "question": (
            "Even though you say you are undecided, if you had to"
            "choose, would you say you lean more toward "
            "(Candidate A) or (Candidate B)?"
        ),
        "8": "Lean Candidate's name (Democrat)",
        "9": "Lean Candidate's name (2nd Democrat, if applicable)",
        "10": "Lean Candidate's name (Republican)",
        "12": "Lean Candidate's name (Independent, if applicable)",
        "14": "Lean Other candidate",
        "15": "Undecided",
        "16": "I would not vote",
    },
    "specsenvote18": {
        "question": (
            "(ASK ONLY IN 2018 SPECIAL ELECTION SENATE STATES) (IF"
            "NOT ALREADY VOTED) If the special election for U.S. "
            "Senator of (state) were being held today, whom would "
            "you vote for? (IF ALREADY VOTED) In the special election "
            "for U.S. Senator of (state), whom did you vote for?"
        ),
        "1": "Candidate's name (Democrat)",
        "3": "Candidate's name (Republican)",
        "4": "Candidate's name (2nd Republican, if applicable)",
        "7": "Other candidate",
        "15": "Undecided",
        "16": "I would not vote",
        "17": "Prefer not to say",
    },
    "specsenvote18_undecided": {
        "question": (
            "Even though you say you are undecided, if you had to"
            "choose, would you say you lean more toward "
            "(Candidate A) or (Candidate B)?"
        ),
        "8": "Lean Candidate's name (Democrat)",
        "10": "Lean Candidate's name (Republican)",
        "11": "Lean Candidate's name (2 nd Republican, if applicable)",
        "14": "Lean Other candidate",
        "15": "Undecided",
        "16": "I would not vote",
    },
    "housevote18": {
        "question": (
            "If the election for U.S. House of Representatives were being held"
            "today, who would you vote for in the district where you live?"
            "(IF NOT ALREADY VOTED) If the election for U.S. House of "
            "Representatives were being held today, whom would you vote "
            "for in the district where you live? (IF ALREADY VOTED) In "
            "the election for U.S. House of Representatives, whom did you "
            "vote for in the district where you live?"
        ),
        "1": "Candidate's name (Democrat)",
        "2": "Candidate's name (2 nd Democrat, if applicable)",
        "3": "Candidate's name (Republican)",
        "4": "Candidate's name (2 nd Republican, if applicable)",
        "5": "Candidate's name (Independent, if applicable)",
        "6": "Candidate's name (2 nd Independent, if applicable)",
        "7": "Other candidate",
        "15": "Undecided",
        "16": "I would not vote",
        "17": "Prefer not to say",
    },
    "housevote18_undecided": {
        "question": (
            "Even though you say you are undecided, if you had to"
            "choose, would you say you lean more toward "
            "(Candidate A) or (Candidate B)?"
        ),
        "8": "Lean Candidate's name (Democrat)",
        "9": "Lean Candidate's name (2 nd Democrat, if applicable)",
        "10": "Lean Candidate's name (Republican)",
        "11": "Lean Candidate's name (2 nd Republican, if applicable)",
        "12": "Lean Candidate's name (Independent, if applicable)",
        "13": "Lean Candidate's name (2 nd Independent, if applicable)",
        "14": "Lean Other candidate",
        "15": "Undecided",
        "16": "I would not vote",
    },
    # (codes up to housevote18_full, house2_imputed, and house3)
    "govvote18": {
        "question": (
            "(ASK ONLY IN 2018 GOVERNOR STATES) (IF NOT ALREADY VOTED) If"
            "the election for Governor of (state) were being held today, "
            "whom would you vote for? (IF ALREADY VOTED) In the election "
            "for Governor of (state), whom did you vote for?"
        ),
        "1": "Candidate's name (Democrat)",
        "3": "Candidate's name (Republican)",
        "5": "Candidate's name (Independent, if applicable)",
        "6": "Candidate's name (2nd Independent, if applicable)",
        "7": "Other candidate",
        "15": "Undecided",
        "16": "I would not vote",
        "17": "Prefer not to say",
    },
    "govvote18_undecided": {
        "question": (
            "Even though you say you are undecided, if you had to"
            "choose, would you say you lean more toward "
            "(Candidate A) or (Candidate B)?"
        ),
        "8": "Lean Candidate's name (Democrat)",
        "10": "Lean Candidate's name (Republican)",
        "12": "Lean Candidate's name (Independent, if applicable)",
        "13": "Lean Candidate's name (2nd Independent, if applicable)",
        "14": "Lean Other candidate",
        "15": "Undecided",
        "16": "I would not vote",
    },
    # (codes up to govvote18_full)
    "direct": {
        "question": (
            "Generally speaking, do you think that things in this country "
            "are going in the right direction, or do you feel things have "
            "gotten pretty seriously off on the wrong track?"
        ),
        "1": "Right direction",
        "2": "Wrong track",
        "3": "Not sure",
    },
    "favor_labor": {
        "question": (
            "labor unions, Please rate your feelings toward each of the people, terms, "
            "and organizations below: do you feel very favorable toward "
            "them, somewhat favorable, somewhat unfavorable, very "
            "unfavorable, or have you never heard of them? RANDOMIZE"
        ),
        "1": "Very favorable",
        "2": "Somewhat favorable",
        "3": "Somewhat unfavorable",
        "4": "Very unfavorable",
        "5": "Never heard",
        "6": "Don't know",
    },
    "favor_dem": {
        "question": (
            "democratic party, Please rate your feelings toward each of the people, terms, "
            "and organizations below: do you feel very favorable toward "
            "them, somewhat favorable, somewhat unfavorable, very "
            "unfavorable, or have you never heard of them? RANDOMIZE"
        ),
        "1": "Very favorable",
        "2": "Somewhat favorable",
        "3": "Somewhat unfavorable",
        "4": "Very unfavorable",
        "5": "Never heard",
        "6": "Don't know",
    },
    "favor_rep": {
        "question": (
            "republican party, Please rate your feelings toward each of the people, terms, "
            "and organizations below: do you feel very favorable toward "
            "them, somewhat favorable, somewhat unfavorable, very "
            "unfavorable, or have you never heard of them? RANDOMIZE"
        ),
        "1": "Very favorable",
        "2": "Somewhat favorable",
        "3": "Somewhat unfavorable",
        "4": "Very unfavorable",
        "5": "Never heard",
        "6": "Don't know",
    },
    "favor_aca": {
        "question": (
            "affordable care act or obamacare, Please rate your "
            "feelings toward each of the people, terms, "
            "and organizations below: do you feel very favorable toward "
            "them, somewhat favorable, somewhat unfavorable, very "
            "unfavorable, or have you never heard of them? RANDOMIZE"
        ),
        "1": "Very favorable",
        "2": "Somewhat favorable",
        "3": "Somewhat unfavorable",
        "4": "Very unfavorable",
        "5": "Never heard",
        "6": "Don't know",
    },
    "favor_dtrump": {
        "question": (
            "donald trump, Please rate your feelings toward each of the people, terms, "
            "and organizations below: do you feel very favorable toward "
            "them, somewhat favorable, somewhat unfavorable, very "
            "unfavorable, or have you never heard of them? RANDOMIZE"
        ),
        "1": "Very favorable",
        "2": "Somewhat favorable",
        "3": "Somewhat unfavorable",
        "4": "Very unfavorable",
        "5": "Never heard",
        "6": "Don't know",
    },
    "favor_mcconnell": {
        "question": (
            "mitch mcconnell, Please rate your feelings toward each of the people, terms, "
            "and organizations below: do you feel very favorable toward "
            "them, somewhat favorable, somewhat unfavorable, very "
            "unfavorable, or have you never heard of them? RANDOMIZE"
        ),
        "1": "Very favorable",
        "2": "Somewhat favorable",
        "3": "Somewhat unfavorable",
        "4": "Very unfavorable",
        "5": "Never heard",
        "6": "Don't know",
    },
    "favor_demcong": {
        "question": (
            "dems in congress, Please rate your feelings toward each of the people, terms, "
            "and organizations below: do you feel very favorable toward "
            "them, somewhat favorable, somewhat unfavorable, very "
            "unfavorable, or have you never heard of them? RANDOMIZE"
        ),
        "1": "Very favorable",
        "2": "Somewhat favorable",
        "3": "Somewhat unfavorable",
        "4": "Very unfavorable",
        "5": "Never heard",
        "6": "Don't know",
    },
    "favor_repcong": {
        "question": (
            "repub in congress, Please rate your feelings toward each of the people, terms, "
            "and organizations below: do you feel very favorable toward "
            "them, somewhat favorable, somewhat unfavorable, very "
            "unfavorable, or have you never heard of them? RANDOMIZE"
        ),
        "1": "Very favorable",
        "2": "Somewhat favorable",
        "3": "Somewhat unfavorable",
        "4": "Very unfavorable",
        "5": "Never heard",
        "6": "Don't know",
    },
    "favor_metoo": {
        "question": (
            "\#metoo, Please rate your feelings toward each of the people, terms, "
            "and organizations below: do you feel very favorable toward "
            "them, somewhat favorable, somewhat unfavorable, very "
            "unfavorable, or have you never heard of them? RANDOMIZE"
        ),
        "1": "Very favorable",
        "2": "Somewhat favorable",
        "3": "Somewhat unfavorable",
        "4": "Very unfavorable",
        "5": "Never heard",
        "6": "Don't know",
    },
    "favor_blm": {
        "question": (
            "Black lives matter, Please rate your feelings toward each of the people, terms, "
            "and organizations below: do you feel very favorable toward "
            "them, somewhat favorable, somewhat unfavorable, very "
            "unfavorable, or have you never heard of them? RANDOMIZE"
        ),
        "1": "Very favorable",
        "2": "Somewhat favorable",
        "3": "Somewhat unfavorable",
        "4": "Very unfavorable",
        "5": "Never heard",
        "6": "Don't know",
    },
    "app_dtrmp": {
        "question": (
            "Do you approve or disapprove of the way Donald Trump "
            "is handling his job as President?"
        ),
        "1": "Strongly approve",
        "2": "Somewhat approve",
        "3": "Somewhat disapprove",
        "4": "Strongly disapprove",
        "5": "Not sure",
    },
    "suprpty": {
        "question": "Which of the following best describes you?",
        "1": "I have always been a supporter of the Democratic Party",
        "2": (
            "I was a supporter of the Republican Party, but have switched "
            "to supporting the Democratic Party"
        ),
        "3": (
            "I was a supporter of the Democratic Party, but have switched "
            "to supporting the Republican Party"
        ),
        "4": "I have always been a supporter of the Republican Party",
        "5": "Not sure",
    },
    "campaign_contact_emails": {
        "question": "Have you, Received emails from a campaign, organization or group",
        "1": "Yes, contacted by a Democrat or Democratic leaning group",
        "2": "Yes, contacted by a Republican or Republican leaning group",
        "3": "Yes, contacted by both",
        "4": "No, not contacted that way",
    },
    "campaign_contact_text": {
        "question": "Have you, Received a text message from a campaign, organization or group",
        "1": "Yes, contacted by a Democrat or Democratic leaning group",
        "2": "Yes, contacted by a Republican or Republican leaning group",
        "3": "Yes, contacted by both",
        "4": "No, not contacted that way",
    },
    "campaign_contact_mailer": {
        "question": (
            "Have you, Received printed materials in the mail "
            "from a campaign, organization or group"
        ),
        "1": "Yes, contacted by a Democrat or Democratic leaning group",
        "2": "Yes, contacted by a Republican or Republican leaning group",
        "3": "Yes, contacted by both",
        "4": "No, not contacted that way",
    },
    "campaign_contact_onlineads": {
        "question": "Have you, Saw political ads online",
        "1": "Yes, contacted by a Democrat or Democratic leaning group",
        "2": "Yes, contacted by a Republican or Republican leaning group",
        "3": "Yes, contacted by both",
        "4": "No, not contacted that way",
    },
    "campaign_contact_inperson": {
        "question": (
            "Have you, Spoke in person with someone from a campaign,"
            "organization or group"
        ),
        "1": "Yes, contacted by a Democrat or Democratic leaning group",
        "2": "Yes, contacted by a Republican or Republican leaning group",
        "3": "Yes, contacted by both",
        "4": "No, not contacted that way",
    },
    "campaign_contact_phone": {
        "question": "Have you, Received phone calls from a campaign, organization or group",
        "1": "Yes, contacted by a Democrat or Democratic leaning group",
        "2": "Yes, contacted by a Republican or Republican leaning group",
        "3": "Yes, contacted by both",
        "4": "No, not contacted that way",
    },
    "campaign_contact_TVads": {
        "question": "Have you, Saw political ads on television",
        "1": "Yes, contacted by a Democrat or Democratic leaning group",
        "2": "Yes, contacted by a Republican or Republican leaning group",
        "3": "Yes, contacted by both",
        "4": "No, not contacted that way",
    },
    "campaign_contact_socialmedia": {
        "question": (
            "Have you, Contacted by a campaign, organization or group"
            "through social media"
        ),
        "1": "Yes, contacted by a Democrat or Democratic leaning group",
        "2": "Yes, contacted by a Republican or Republican leaning group",
        "3": "Yes, contacted by both",
        "4": "No, not contacted that way",
    },
    "VOTE_GEN": {
        "question": "In general, how often do you vote?",
        "1": "I always vote",
        "2": "I usually vote",
        "3": "I sometimes vote",
        "4": "I rarely vote",
        "5": "I never vote",
    },
    # 'NONVOTE_WHY': {'question': ('if not VOTE_GEN == 1 In past elections when you haven\'t voted,'
    #                              'why has this been the case? Please select all that apply.')},
    "NONVOTE_WHY_1": {
        "question": (
            "I didn't feel like I knew enough to make an informed decision "
            "between the candidates"
        ),
        "1": "Yes",
        "2": "No",
    },
    "NONVOTE_WHY_2": {
        "question": "I didn't feel that any of the candidates represented my views",
        "1": "Yes",
        "2": "No",
    },
    "NONVOTE_WHY_3": {
        "question": "I wanted to vote, but wasn't registered",
        "1": "Yes",
        "2": "No",
    },
    "NONVOTE_WHY_4": {
        "question": "I wanted to vote, but didn't have time/was too busy that day",
        "1": "Yes",
        "2": "No",
    },
    "NONVOTE_WHY_5": {
        "question": "I wanted to vote, but couldn't find my polling location",
        "1": "Yes",
        "2": "No",
    },
    "NONVOTE_WHY_6": {
        "question": "I wanted to vote, but didn't have a required form of identification",
        "1": "Yes",
        "2": "No",
    },
    "NONVOTE_WHY_7": {"question": "Other", "1": "Yes", "2": "No"},
    "NONVOTE_WHY_t": {"question": ("Reason for not voting in past elections")},
    "VOTECONF": {
        "question": (
            "if turnout16 == 1 How confident are you that your vote in the "
            "2016 presidential election was counted as you intended?"
        ),
        "1": "Very confident",
        "2": "Somewhat confident",
        "3": "Not too confident",
        "4": "Not at all confident",
        "5": "No opinion",
        "6": "I did not vote for President",
    },
    "GENERATIONS": {
        "question": (
            "Please indicate the extent to which you agree with each of the"
            "following statements. Generations of slavery and discrimination "
            "have created conditions that make it difficult for African "
            "Americans to work their way out of the lower class."
        ),
        "1": "Strongly agree",
        "2": "Somewhat agree",
        "3": "Neither agree nor disagree",
        "4": "Somewhat disagree",
        "5": "Strongly disagree",
        "6": "No opinion",
    },
    "FAVORS": {
        "question": (
            "Please indicate the extent to which you agree with each of the following"
            "statements. Irish, Italian, Jewish, and many other minorities overcame "
            "prejudice and worked their way up. Blacks should do the same "
            "without any special favors."
        ),
        "1": "Strongly agree",
        "2": "Somewhat agree",
        "3": "Neither agree nor disagree",
        "4": "Somewhat disagree",
        "5": "Strongly disagree",
        "6": "No opinion",
    },
    "INSTITUTION": {
        "question": (
            "Please indicate the extent to which you agree with each of the"
            "following statements. White people in the U.S. have certain advantages because of"
            "the color of their skin."
        ),
        "1": "Strongly agree",
        "2": "Somewhat agree",
        "3": "Neither agree nor disagree",
        "4": "Somewhat disagree",
        "5": "Strongly disagree",
        "6": "No opinion",
    },
    "SYSTEM": {
        "question": (
            "Please indicate the extent to which you agree with each of the following"
            "statements. Racial problems in the U.S. are rare, isolated situations."
        ),
        "1": "Strongly agree",
        "2": "Somewhat agree",
        "3": "Neither agree nor disagree",
        "4": "Somewhat disagree",
        "5": "Strongly disagree",
        "6": "No opinion",
    },
    "EMPATHY": {
        "question": (
            "Please indicate the extent to which you agree with each of the following"
            "statements. I am angry that racism exists."
        ),
        "1": "Strongly agree",
        "2": "Somewhat agree",
        "3": "Neither agree nor disagree",
        "4": "Somewhat disagree",
        "5": "Strongly disagree",
        "6": "No opinion",
    },
    "racial_resentment_raw": {
        "question": (
            "(recode) Coded from GENERATIONS, FAVORS, INSTITUTION,"
            "SYSTEM, and EMPATHY. Sum of (“strongly agree” = 4, "
            "“somewhat agree” = 3, “neither agree nor disagree” = 2, "
            "“somewhat disagree” = 1, “strongly disagree” = 0) for SYSTEM "
            "and FAVORS, plus sum of (“strongly agree” = 0, “somewhat agree” ="
            "1, “neither agree nor disagree” = 2, “somewhat disagree” = 3, "
            "“strongly disagree” = 4) for EMPATHY, INSTITUTION, and "
            "GENERATIONS."
        )
    },
    "racial_resentment_scaled": {
        "question": (
            "(recode) Sum of racial_animus_scaled divided by its " "maximum value."
        )
    },
    # Next, we\'d like to get your feelings toward some groups who are in the news these
    # days. For each group listed, you will be asked to rate people in that group using
    # something we call the feeling thermometer. Ratings between 50 degrees and 100
    # degrees mean that you feel favorable and warm toward the group. Ratings between
    # 0 degrees and 50 degrees mean that you don\'t feel favorable toward the group and
    # that you don\'t care too much for that group. You would rate the person at the 50
    # degree mark if you don\'t feel particularly warm or cold toward the group.
    # FT Rate your feeling toward this group from zero (very cold or negative) to 100 (very
    # warm or positive).
    "FT_Whites": {
        "question": (
            "Whites Rate your feeling toward this group from zero "
            "(very cold or negative) to 100 (very warm or positive)."
        )
    },
    "FT_Blacks": {
        "question": (
            "Blacks Rate your feeling toward this group from zero (very "
            "cold or negative) to 100 (very warm or positive)."
        )
    },
    "FT_Latinos": {
        "question": (
            "Latinos Rate your feeling toward this group from zero "
            "(very cold or negative) to 100 (very warm or positive)."
        )
    },
    # Now we have some questions about different groups in our society. We\'re going to
    # show you a seven-point scale on which the characteristics of the people in a group
    # can be rated.
    "LAZY_Whites": {
        "question": "How lazy or hardworking is each group? Whites",
        "1": "Very lazy",
        "2": "Lazy",
        "3": "Somewhat lazy",
        "4": "Neither lazy nor hardworking",
        "5": "Somewhat hardworking",
        "6": "Hardworking",
        "7": "Very hardworking",
    },
    "LAZY_Blacks": {
        "question": "How lazy or hardworking is each group? Blacks",
        "1": "Very lazy",
        "2": "Lazy",
        "3": "Somewhat lazy",
        "4": "Neither lazy nor hardworking",
        "5": "Somewhat hardworking",
        "6": "Hardworking",
        "7": "Very hardworking",
    },
    "LAZY_Latinos": {
        "question": "How lazy or hardworking is each group? Latinos",
        "1": "Very lazy",
        "2": "Lazy",
        "3": "Somewhat lazy",
        "4": "Neither lazy nor hardworking",
        "5": "Somewhat hardworking",
        "6": "Hardworking",
        "7": "Very hardworking",
    },
    "INTELLIGENT_Whites": {
        "question": "How intelligent or unintelligent is each group? Whites",
        "1": "Very intelligent",
        "2": "Intelligent",
        "3": "Somewhat intelligent",
        "4": "Neither intelligent nor unintelligent",
        "5": "Somewhat unintelligent",
        "6": "Unintelligent",
        "7": "Very unintelligent",
    },
    "INTELLIGENT_Blacks": {
        "question": "How intelligent or unintelligent is each group? Blacks",
        "1": "Very intelligent",
        "2": "Intelligent",
        "3": "Somewhat intelligent",
        "4": "Neither intelligent nor unintelligent",
        "5": "Somewhat unintelligent",
        "6": "Unintelligent",
        "7": "Very unintelligent",
    },
    "INTELLIGENT_Latinos": {
        "question": "How intelligent or unintelligent is each group? Latinos",
        "1": "Very intelligent",
        "2": "Intelligent",
        "3": "Somewhat intelligent",
        "4": "Neither intelligent nor unintelligent",
        "5": "Somewhat unintelligent",
        "6": "Unintelligent",
        "7": "Very unintelligent",
    },
    "RACE_IDENT": {
        "question": "How important is being $race to your identity?",
        "4": "Very important",
        "3": "Somewhat important",
        "2": "Not very important",
        "1": "Not at all important",
    },
    "LINKFATE": {
        "question": (
            "Please indicate the extent to which you agree with the following"
            " statement: What happens generally to $raceval2 in this country "
            " will have something to do with what happens in your life."
        ),
        "1": "Strongly agree",
        "2": "Somewhat agree",
        "3": "Neither agree nor disagree",
        "4": "Somewhat disagree",
        "5": "Strongly disagree",
    },
    "FINPREP": {
        "question": (
            "Thinking about your household's finances today, could you "
            "cover a $400 emergency expense without borrowing it or taking on debt?"
        ),
        "1": "Yes, definitely",
        "2": "Yes, probably",
        "3": "Not sure",
        "4": "No, probably not",
        "5": "No, definitely not",
    },
    "DESERVE_poor": {
        "question": (
            "For each of the following groups, please say whether most people"
            " in the group have more money than they deserve, less money than they deserve, or"
            " about the right amount of money. Poor people"
        ),
        "1": "A lot more money than they deserve",
        "2": "Somewhat more money than they deserve",
        "3": "Slightly more money than they deserve",
        "4": "About the right amount of money",
        "5": "Slightly less money than they deserve",
        "6": "Somewhat less money than they deserve",
        "7": "A lot less money than they deserve",
    },
    "DESERVE_rich": {
        "question": (
            "For each of the following groups, please say whether most people"
            " in the group have more money than they deserve, less money than they deserve, or"
            " about the right amount of money. Rich people"
        ),
        "1": "A lot more money than they deserve",
        "2": "Somewhat more money than they deserve",
        "3": "Slightly more money than they deserve",
        "4": "About the right amount of money",
        "5": "Slightly less money than they deserve",
        "6": "Somewhat less money than they deserve",
        "7": "A lot less money than they deserve",
    },
    "CUSTOMS": {
        "question": (
            "Please indicate the extent to which you agree with each of the following"
            " statements. The growing number of newcomers from other countries threatens"
            " traditional American customs and values."
        ),
        "1": "Strongly agree",
        "2": "Somewhat agree",
        "3": "Neither agree nor disagree",
        "4": "Somewhat disagree",
        "5": "Strongly disagree",
        "6": "Not sure",
    },
    "SPEAK": {
        "question": (
            "Please indicate the extent to which you agree with each of the following"
            " statements. It bothers me when I come in contact with immigrants who speak little"
            " or no English."
        ),
        "1": "Strongly agree",
        "2": "Somewhat agree",
        "3": "Neither agree nor disagree",
        "4": "Somewhat disagree",
        "5": "Strongly disagree",
        "6": "Not sure",
    },
    "ENRICH": {
        "question": (
            "As you may know, Census projections show that by 2043 African"
            " Americans, Latinos, Asians, and other mixed racial and ethnic groups will together"
            " be a majority of the population. Thinking about the likely impact of this coming"
            " demographic change, how much do you agree or disagree with each of these"
            " statements? Americans will learn more from one another and be enriched by"
            " exposure to many different cultures."
        ),
        "1": "Strongly agree",
        "2": "Somewhat agree",
        "3": "Neither agree nor disagree",
        "4": "Somewhat disagree",
        "5": "Strongly disagree",
        "6": "Not sure",
    },
    "SERVICES": {
        "question": (
            "As you may know, Census projections show that by 2043 African"
            " Americans, Latinos, Asians, and other mixed racial and ethnic groups will together"
            " be a majority of the population. Thinking about the likely impact of this coming"
            " demographic change, how much do you agree or disagree with each of these"
            " statements? There will be too many demands on government services."
        ),
        "1": "Strongly agree",
        "2": "Somewhat agree",
        "3": "Neither agree nor disagree",
        "4": "Somewhat disagree",
        "5": "Strongly disagree",
        "6": "Not sure",
    },
    "JOBS": {
        "question": (
            "As you may know, Census projections show that by 2043 African Americans,"
            " Latinos, Asians, and other mixed racial and ethnic groups will together be a majority"
            " of the population. Thinking about the likely impact of this coming demographic"
            " change, how much do you agree or disagree with each of these statements? There"
            " will not be enough jobs for everybody."
        ),
        "1": "Strongly agree",
        "2": "Somewhat agree",
        "3": "Neither agree nor disagree",
        "4": "Somewhat disagree",
        "5": "Strongly disagree",
        "6": "Not sure",
    },
    "fear_of_demographic_change_raw": {
        "question": (
            "(recode) Coded from ENRICH, SERVICES,"
            "JOBS. Sum of (“strongly agree” = 4, “somewhat agree” = 3, "
            "“neither agree nor disagree” = 2, “somewhat disagree” = 1, "
            "“strongly disagree” = 0) for JOBS and SERVICES, plus sum "
            "of (“strongly agree” = 0, “somewhat agree” = 1, “neither agree"
            "nor disagree” = 2, “somewhat disagree” = 3, “strongly "
            "disagree” = 4) for ENRICH."
        )
    },
    "fear_of_demographic_change_scaled": {
        "question": (
            "(recode) Sum of fear_of_demographic_change_raw "
            "divided by its maximum value."
        )
    },
    "FLAG": {
        "question": "Which of the following is closer to your view regarding the Confederate flag?",
        "1": "Slavery and White Supremacy",
        "2": "Southern Heritage and Culture",
        "3": "Don't know",
    },
    "PATH": {
        "question": (
            "Please indicate whether you favor or oppose each of the "
            "following proposals addressing immigration: Provide a path to "
            "citizenship for some undocumented immigrants who agree to return to"
            " their home country for a period of time and pay substantial fines."
        ),
        "1": "Strongly support",
        "2": "Somewhat support",
        "3": "Neither support nor oppose",
        "4": "Somewhat oppose",
        "5": "Strongly oppose",
        "6": "Don't know",
    },
    "BORDER": {
        "question": (
            "Please indicate whether you favor or oppose each of "
            "the following proposals addressing immigration: Increase "
            "border security by building a fence along part of the US "
            "border with Mexico."
        ),
        "1": "Strongly support",
        "2": "Somewhat support",
        "3": "Neither support nor oppose",
        "4": "Somewhat oppose",
        "5": "Strongly oppose",
        "6": "Don't know",
    },
    "DEPORT": {
        "question": (
            "Please indicate whether you favor or oppose each of the following"
            " proposals addressing immigration: Deport undocumented immigrants to their"
            " native countries."
        ),
        "1": "Strongly support",
        "2": "Somewhat support",
        "3": "Neither support nor oppose",
        "4": "Somewhat oppose",
        "5": "Strongly oppose",
        "6": "Don't know",
    },
    # 'SOCIALDOMINANCE': {'question': ('There are many kinds of groups in the world: men and'
    #                                  'women, ethnic and religious groups, nationalities, political '
    #                                  'factions. How much do you support or oppose these ideas about'
    #                                  ' groups in general? For each statement, please state whether'
    #                                  ' you strongly agree, somewhat agree, neither agree nor'
    #                                  'disagree, somewhat disagree, or strongly disagree.')},
    "SOCIALDOMINANCE_PRIORITIES": {
        "question": "In setting priorities, we must consider all groups",
        "1": "Strongly agree",
        "2": "Somewhat agree",
        "3": "Neither agree nor disagree",
        "4": "Somewhat disagree",
        "5": "Strongly disagree",
    },
    "SOCIALDOMINANCE_NOTPUSH": {
        "question": "We should not push for group equality",
        "1": "Strongly agree",
        "2": "Somewhat agree",
        "3": "Neither agree nor disagree",
        "4": "Somewhat disagree",
        "5": "Strongly disagree",
    },
    "SOCIALDOMINANCE_EQUALIDEAL": {
        "question": "Group equality should be our ideal",
        "1": "Strongly agree",
        "2": "Somewhat agree",
        "3": "Neither agree nor disagree",
        "4": "Somewhat disagree",
        "5": "Strongly disagree",
    },
    "SOCIALDOMINANCE_SUPERIOR": {
        "question": "Superior groups should dominate inferior groups",
        "1": "Strongly agree",
        "2": "Somewhat agree",
        "3": "Neither agree nor disagree",
        "4": "Somewhat disagree",
        "5": "Strongly disagree",
    },
    "REMARKS": {
        "question": (
            "Please indicate the extent to which you agree with the following"
            " statements: Most women interpret innocent remarks or acts as being sexist."
        ),
        "1": "Strongly agree",
        "2": "Somewhat agree",
        "3": "Neither agree nor disagree",
        "4": "Somewhat disagree",
        "5": "Strongly disagree",
        "6": "Don't know",
    },
    "OFFEND": {
        "question": (
            "Please indicate the extent to which you agree with the following"
            " statements: Women are too easily offended."
        ),
        "1": "Strongly agree",
        "2": "Somewhat agree",
        "3": "Neither agree nor disagree",
        "4": "Somewhat disagree",
        "5": "Strongly disagree",
        "6": "Don't know",
    },
    "APPRECIATE": {
        "question": (
            "Please indicate the extent to which you agree with the following"
            " statements: Most women fail to appreciate fully all that men do for them."
        ),
        "1": "Strongly agree",
        "2": "Somewhat agree",
        "3": "Neither agree nor disagree",
        "4": "Somewhat disagree",
        "5": "Strongly disagree",
        "6": "Don't know",
    },
    "hostile_sexism_raw": {
        "question": (
            "(recode) Coded from REMARKS, OFFEND, APPRECIATE."
            "Sum of (“strongly agree” = 4, “somewhat agree” = 3, "
            "“neither agree nor disagree” = 2, “somewhat disagree” "
            "= 1, “strongly disagree” = 0) across these three items."
        )
    },
    "hostile_sexism_scaled": {
        "question": "(recode) Sum of hostile_sexism_raw divided by its maximum value."
    },
    "GENDERPERSONALITY_INDEP": {
        "question": (
            "Select the number that describes where you fall on "
            "the scale between the two characteristics. 1 = Not "
            "at all independent; 5 = Very independent"
        )
    },
    "GENDERPERSONALITY_EMOT": {
        "question": (
            "Select the number that describes where you fall on "
            "the scale between the two characteristics. "
            "1 = Not at all emotional; 5 = Very emotional"
        )
    },
    "GENDERPERSONALITY_CONFIDENT": {
        "question": (
            "Select the number that describes where you fall on "
            "the scale between the two characteristics. "
            "1 = Very Confident; 5 = Not at all confident"
        )
    },
    "GENDERPERSONALITY_HELPFUL": {
        "question": (
            "Select the number that describes where you fall "
            "on the scale between the two characteristics. "
            "1 = Not at all helpful to others; 5 = Very helpful to others"
        )
    },
    "GENDERPERSONALITY_DECISIONS": {
        "question": (
            "Select the number that describes where you fall "
            "on the scale between the two characteristics. "
            "1 = Can make decisions easily; 5 = Has difficulty making decisions"
        )
    },
    "POP_1": {
        "question": (
            "Please indicate the extent to which you agree with the following statement:"
            " It doesn't really matter who you vote for because the rich control both political"
            " parties."
        ),
        "1": "Strongly agree",
        "2": "Somewhat agree",
        "3": "Neither agree nor disagree",
        "4": "Somewhat disagree",
        "5": "Strongly disagree",
        "6": "Not sure",
    },
    "POP_2": {
        "question": (
            "Please indicate the extent to which you agree with the following statement:"
            " The system is stacked against people like me."
        ),
        "1": "Strongly agree",
        "2": "Somewhat agree",
        "3": "Neither agree nor disagree",
        "4": "Somewhat disagree",
        "5": "Strongly disagree",
        "6": "Not sure",
    },
    "POP_3": {
        "question": (
            "Please indicate the extent to which you agree with the following statement:"
            " I'd rather put my trust in the wisdom of ordinary people than in the opinions of"
            " experts and intellectuals."
        ),
        "1": "Strongly agree",
        "2": "Somewhat agree",
        "3": "Neither agree nor disagree",
        "4": "Somewhat disagree",
        "5": "Strongly disagree",
        "6": "Not sure",
    },
    "ICE": {
        "question": "Would you support or oppose defunding Immigration and Customs Enforcement (ICE)?",
        "1": "Strongly support",
        "2": "Somewhat support",
        "3": "Neither support nor oppose",
        "4": "Somewhat oppose",
        "5": "Strongly oppose",
        "6": "Not sure",
    },
    "BAIL_item": {
        "question": (
            "Would you support or oppose ending cash bail for individuals awaiting"
            " trial, and instead only detaining individuals pre-trial if "
            "they were a violence or flight risk?"
        ),
        "1": "Strongly support",
        "2": "Somewhat support",
        "3": "Neither support nor oppose",
        "4": "Somewhat oppose",
        "5": "Strongly oppose",
        "6": "Not sure",
    },
    "WELTEST": {
        "question": (
            "Would you support or oppose requiring recipients of government aid"
            " such as food assistance or Medicaid to pass a drug test in "
            "order to receive those benefits?"
        ),
        "1": "Strongly support",
        "2": "Somewhat support",
        "3": "Neither support nor oppose",
        "4": "Somewhat oppose",
        "5": "Strongly oppose",
        "6": "Not sure",
    },
    "PUBLICINT": {
        "question": (
            "Would you support or oppose the creation of a publicly-owned Internet"
            " company to fill coverage gaps in rural, urban, or remote areas that "
            "currently lack robust Internet access?"
        ),
        "1": "Strongly support",
        "2": "Somewhat support",
        "3": "Neither support nor oppose",
        "4": "Somewhat oppose",
        "5": "Strongly oppose",
        "6": "Not sure",
    },
    "GREENJOB": {
        "question": (
            "Would you support or oppose giving every unemployed American who"
            " wants one a job building energy-efficient infrastructure?"
        ),
        "1": "Strongly support",
        "2": "Somewhat support",
        "3": "Neither support nor oppose",
        "4": "Somewhat oppose",
        "5": "Strongly oppose",
        "6": "Not sure",
    },
    "POLFEE": {
        "question": (
            "Would you support or oppose a policy to charge pollution fees on "
            "companies that emit high levels of greenhouse gasses?"
        ),
        "1": "Strongly support",
        "2": "Somewhat support",
        "3": "Neither support nor oppose",
        "4": "Somewhat oppose",
        "5": "Strongly oppose",
        "6": "Not sure",
    },
    "PUBLICGEN": {
        "question": (
            "Would you support or oppose having the government produce"
            " generic versions of life-saving drugs, even if it required"
            " revoking patents held by pharmaceutical companies?"
        ),
        "1": "Strongly support",
        "2": "Somewhat support",
        "3": "Neither support nor oppose",
        "4": "Somewhat oppose",
        "5": "Strongly oppose",
        "6": "Not sure",
    },
    "BOND": {
        "question": (
            "Would you support or oppose giving every American a $5,000 savings"
            " account at birth that they can access when they turn 18, paid for by raising taxes on"
            " estates worth $10,000,000?"
        ),
        "1": "Strongly support",
        "2": "Somewhat support",
        "3": "Neither support nor oppose",
        "4": "Somewhat oppose",
        "5": "Strongly oppose",
        "6": "Not sure",
    },
    "FREECOLL": {
        "question": (
            "Would you support or oppose a law that would raise taxes on income"
            " in excess of $200,000 per year by 5 percent in order to cover college tuition for all"
            " students, while capping the rise in tuition at the rate of inflation for all colleges"
            " accepting such funding?"
        ),
        "1": "Strongly support",
        "2": "Somewhat support",
        "3": "Neither support nor oppose",
        "4": "Somewhat oppose",
        "5": "Strongly oppose",
        "6": "Not sure",
    },
    "WEALTH": {
        "question": "Would you support or oppose a tax on wealth greater than $100 million?",
        "1": "Strongly support",
        "2": "Somewhat support",
        "3": "Neither support nor oppose",
        "4": "Somewhat oppose",
        "5": "Strongly oppose",
        "6": "Not sure",
    },
    "AVR": {
        "question": (
            "Would you support or oppose a policy where all eligible US citizens would be"
            " automatically registered to vote (unless they opt out) when applying for licenses and"
            " other IDs at DMVs, Medicaid offices, healthcare exchanges and other public agencies?"
        ),
        "1": "Strongly support",
        "2": "Somewhat support",
        "3": "Neither support nor oppose",
        "4": "Somewhat oppose",
        "5": "Strongly oppose",
        "6": "Not sure",
    },
    "M4A": {
        "question": (
            "Would you support or oppose expanding Medicare such that it becomes the"
            " main health insurance provider for all Americans?"
        ),
        "1": "Strongly support",
        "2": "Somewhat support",
        "3": "Neither support nor oppose",
        "4": "Somewhat oppose",
        "5": "Strongly oppose",
        "6": "Not sure",
    },
    "MARREP": {
        "question": (
            "In states where marijuana is legal, would you support or oppose requiring"
            " that any tax revenues collected from its sale be re-invested in communities"
            " disproportionately affected by the War on Drugs?"
        ),
        "1": "Strongly support",
        "2": "Somewhat support",
        "3": "Neither support nor oppose",
        "4": "Somewhat oppose",
        "5": "Strongly oppose",
        "6": "Not sure",
    },
    "MARAM": {
        "question": (
            "Some people are currently incarcerated for marijuana-related offenses in"
            " states where marijuana has since been legalized. Do you support or oppose"
            " releasing these people from prison?"
        ),
        "1": "Strongly support",
        "2": "Somewhat support",
        "3": "Neither support nor oppose",
        "4": "Somewhat oppose",
        "5": "Strongly oppose",
        "6": "Not sure",
    },
    "MARLEG": {
        "question": "Would you support or oppose fully legalizing marijuana at the national level?",
        "1": "Strongly support",
        "2": "Somewhat support",
        "3": "Neither support nor oppose",
        "4": "Somewhat oppose",
        "5": "Strongly oppose",
        "6": "Not sure",
    },
    "YEMEN": {
        "question": (
            "The United States is currently providing military equipment and logistical"
            " support for Saudi Arabia's intervention in the civil war in Yemen. Would you support"
            " or oppose ending US involvement in the conflict?"
        ),
        "1": "Strongly support",
        "2": "Somewhat support",
        "3": "Neither support nor oppose",
        "4": "Somewhat oppose",
        "5": "Strongly oppose",
        "6": "Not sure",
    },
    "SOLITARY": {
        "question": (
            "Would you support or oppose ending the practice of solitary "
            "confinement in the United States?"
        ),
        "1": "Strongly support",
        "2": "Somewhat support",
        "3": "Neither support nor oppose",
        "4": "Somewhat oppose",
        "5": "Strongly oppose",
        "6": "Not sure",
    },
    "GUNS": {
        "question": "Which of the following is closest to your view on gun regulations?",
        "1": "It should be more difficult to buy all types of guns",
        "2": "It should be more difficult to buy some types of guns",
        "3": "The current regulations regarding the purchase of guns are about right",
        "4": "It should be less difficult to buy some types of guns",
        "5": "It should be less difficult to buy all types of guns",
        "6": "Not sure",
    },
    "POLCORRECT": {
        "question": (
            'There\'s been a lot of talk lately about "political correctness." Some'
            " people think that the way people talk needs to change with the times to be more "
            "sensitive to people from different backgrounds. Others think that this has already "
            "gone too far and many people are just too easily offended. Which is closer to your "
            "opinion?"
        ),
        "1": "The way people talk needs to change a lot",
        "2": "The way people talk needs to change a little",
        "3": "People are a little too easily offended",
        "4": "People are much too easily offended",
    },
    "NDIVERSE": {
        "question": (
            "Compared to other places near where you live, "
            "would you say your neighborhood is more diverse, or more homogeneous? "
            "1 = More diverse; 10 = More homogeneous"
        )
    },
    "NDEMS": {
        "question": (
            "About what percentage of the people who live in your neighborhood do"
            "you think are Democrats? (Enter a whole number between 0 and 100)"
        )
    },
    # 'SOURCES': {'question': ('In the past week, did you get news from any of the following sources?'
    #                          'Please select all that apply:')},
    "SOURCES_1": {
        "question": ("In the past week, did you get news from CNN"),
        "1": "Yes",
        "2": "No",
    },
    "SOURCES_2": {
        "question": ("In the past week, did you get news from Fox News"),
        "1": "Yes",
        "2": "No",
    },
    "SOURCES_3": {
        "question": ("In the past week, did you get news from MSNBC"),
        "1": "Yes",
        "2": "No",
    },
    "SOURCES_4": {
        "question": (
            "In the past week, did you get news from Other Cable News TV Networks"
        ),
        "1": "Yes",
        "2": "No",
    },
    "SOURCES_5": {
        "question": ("In the past week, did you get news from Local TV News"),
        "1": "Yes",
        "2": "No",
    },
    "SOURCES_6": {
        "question": (
            "In the past week, did you get news from National nightly network TV news"
        ),
        "1": "Yes",
        "2": "No",
    },
    "SOURCES_7": {
        "question": ("In the past week, did you get news from News websites or apps"),
        "1": "Yes",
        "2": "No",
    },
    "SOURCES_8": {
        "question": (
            "In the past week, did you get news from Your local daily print newspaper"
        ),
        "1": "Yes",
        "2": "No",
    },
    "SOURCES_9": {
        "question": (
            "In the past week, did you get news from National print newspapers"
        ),
        "1": "Yes",
        "2": "No",
    },
    "SOURCES_10": {
        "question": ("In the past week, did you get news from News on the radio"),
        "1": "Yes",
        "2": "No",
    },
    "SOURCES_11": {
        "question": ("In the past week, did you get news from Late night comedy shows"),
        "1": "Yes",
        "2": "No",
    },
    "SOURCES_12": {
        "question": ("In the past week, did you get news from Facebook"),
        "1": "Yes",
        "2": "No",
    },
    "SOURCES_13": {
        "question": ("In the past week, did you get news from Twitter"),
        "1": "Yes",
        "2": "No",
    },
    "SOURCES_14": {
        "question": ("In the past week, did you get news from Reddit"),
        "1": "Yes",
        "2": "No",
    },
    "SOURCES_15": {
        "question": ("In the past week, did you get news from YouTube"),
        "1": "Yes",
        "2": "No",
    },
    "SOURCES_16": {
        "question": (
            "In the past week, did you get news from Other social media "
            "such as LinkedIn, Instagram, or Snapchat"
        ),
        "1": "Yes",
        "2": "No",
    },
    "SOURCES_17": {
        "question": ("In the past week, did you get news from None of these"),
        "1": "Yes",
        "2": "No",
    },
    "pid3": {
        "question": "Generally speaking, do you think of yourself as a ...?",
        "1": "Democrat",
        "2": "Republican",
        "3": "Independent",
        "4": "Other",
        "5": "Not sure",
    },
    "pid7_dems": {
        "question": "Would you call yourself a strong Democrat or a not very strong Democrat?",
        "1": "Strong Democrat",
        "2": "Not very strong Democrat",
    },
    "pid7_reps": {
        "question": "Would you call yourself a strong Republican or a not very strong Republican?",
        "6": "Not very strong Republican",
        "7": "Strong Republican",
    },
    "pid7_oths": {
        "question": "Do you think of yourself as closer to the Democratic or the Republican Party?",
        "3": "The Democratic Party",
        "5": "The Republican Party",
        "4": "Neither",
        "8": "Not sure",
    },
    "pid7": {
        "question": "Generally speaking, do you think of yourself as a ...?",
        "1": "Strong Democrat",
        "2": "Not very strong Democrat",
        "3": "Lean Democrat",
        "4": "Independent",
        "5": "Lean Republican",
        "6": "Not very strong Republican",
        "7": "Strong Republican",
        "8": "Not sure",
    },
    "dtrpsupp": {
        "question": (
            "(ASK ONLY REPUBLICANS) Do you consider yourself more a supporter"
            "of President Donald Trump or a supporter of the Republican Party?"
        ),
        "1": "Trump supporter, strongly",
        "2": "Trump supporter, somewhat",
        "3": "Republican Party supporter, somewhat",
        "4": "Republican Party supporter, strongly",
        "5": "Not sure",
    },
    "ideo5": {
        "question": "In general, how would you describe your own political viewpoint?",
        "1": "Very liberal",
        "2": "Liberal",
        "3": "Moderate",
        "4": "Conservative",
        "5": "Very conservative",
        "6": "Not sure",
    },
    "turnout16": {
        "question": "Did you vote in the election on Tuesday, November 8, 2016?",
        "1": "Yes",
        "2": "No",
    },
    "presvote16post": {
        "question": "ask if turnout16=1 Who did you vote for in the election for President?",
        "1": "Hillary Clinton",
        "2": "Donald Trump",
        "3": "Gary Johnson",
        "4": "Jill Stein",
        "5": "Evan McMullin",
        "6": "Other",
        "7": "Did not vote for President",
    },
    "djtrelct": {
        "question": (
            "Regardless of how you voted in 2016, with the information you have now,"
            " would you vote to re-elect Donald Trump in 2020?"
        ),
        "1": "Yes",
        "2": "No",
        "3": "Not sure",
    },
    "housevote16post": {
        "question": (
            "ask if turnout16=1 In the election for U.S. House of"
            " Representatives in November of 2016, who did you "
            "vote for in the district where you lived?"
        ),
        "1": "The Democratic candidate",
        "2": "The Republican candidate",
        "3": "Another candidate",
        "4": "Did not vote for a representative in Congress in 2016",
    },
    "e14_presvote12": {
        "question": (
            "ask if birthyr < 1995 and votereg in 1 Which candidate did you"
            " vote for in the 2012 Presidential election?"
        ),
        "1": "Barack Obama",
        "2": "Mitt Romney",
        "3": "Other candidate",
        "4": "I did not vote",
    },
    "union_combined_1": {
        "question": "Yes, current union member",
        "2": "No",
        "1": "Yes",
    },
    "union_combined_5": {"question": "Yes, retired unionmember", "2": "No", "1": "Yes"},
    "union_combined_2": {
        "question": "Yes, someone in household is a current union member",
        "2": "No",
        "1": "Yes",
    },
    "union_combined_6": {
        "question": "Yes, someone in household is a retired union member",
        "2": "No",
        "1": "Yes",
    },
    "union_combined_3": {
        "question": "No one in household is a union member",
        "2": "No",
        "1": "Yes",
    },
    "union_combined_4": {
        "question": "Not sure if anyone in household is or has been a union member",
        "2": "No",
        "1": "Yes",
    },
    "marstat": {
        "question": "What is your marital status?",
        "1": "Married",
        "2": "Separated",
        "3": "Divorced",
        "4": "Widowed",
        "5": "Never married",
        "6": "Domestic / civil partnership",
    },
    "child18": {
        "question": "Are you the parent or guardian of any children under the age of 18?",
        "1": "Yes",
        "2": "No",
    },
    "religpew": {
        "question": "What is your present religion, if any?",
        "1": "Protestant",
        "2": "Roman Catholic",
        "3": "Mormon",
        "4": "Eastern or Greek Orthodox",
        "5": "Jewish",
        "6": "Muslim",
        "7": "Buddhist",
        "8": "Hindu",
        "9": "Atheist",
        "10": "Agnostic",
        "11": "Nothing in particular",
        "12": "Something else",
    },
    "pew_bornagain": {
        "question": (
            "Would you describe yourself as a “born-again” or "
            "evangelical Christian, or not?"
        ),
        "1": "Yes",
        "2": "No",
    },
    "pew_churatd": {
        "question": (
            "Aside from weddings and funerals, how often do you attend religious"
            "services?"
        ),
        "1": "More than once a week",
        "2": "Once a week",
        "3": "Once or twice a month",
        "4": "A few times a year",
        "5": "Seldom",
        "6": "Never",
        "7": "Don't know",
    },
    "employ": {
        "question": "Which of the following best describes your current employment status?",
        "1": "Working full time now",
        "2": "Working part time now",
        "3": "Temporarily laid off",
        "4": "Unemployed",
        "5": "Retired",
        "6": "Permanently disabled",
        "7": "Taking care of home or family",
        "8": "Student",
        "9": "Other job",
    },
    "faminc_new": {
        "question": "Thinking back over the last year, what was your family's annual income?",
        "1": "Less than $10,000",
        "2": "$10,000 - $19,999",
        "3": "$20,000 - $29,999",
        "4": "$30,000 - $39,999",
        "5": "$40,000 - $49,999",
        "6": "$50,000 - $59,999",
        "7": "$60,000 - $69,999",
        "8": "$70,000 - $79,999",
        "9": "$80,000 - $99,999",
        "10": "$100,000 - $119,999",
        "11": "$120,000 - $149,999",
        "12": "$150,000 - $199,999",
        "13": "$200,000 - $249,999",
        "14": "$250,000 - $349,999",
        "15": "$350,000 - $499,999",
        "16": "$500,000 or more",
        "97": "Prefer not to say",
    },
    "educ2": {
        "question": "(recode) What is the highest level of education you have completed?",
        "1": "Less than college",
        "2": "College",
    },
    "educ4": {
        "question": "(recode) What is the highest level of education you have completed?",
        "1": "High school or less",
        "2": "Some college",
        "3": "College grad",
        "4": "Postgrad",
    },
    "age5": {
        "question": "(recode) What is your age?",
        "1": "18-29",
        "2": "30-39",
        "3": "40-49",
        "4": "50-64",
        "5": "65+",
    },
    "race4": {
        "question": "(recode) What racial or ethnic group best describes you?",
        "1": "White",
        "2": "Black",
        "3": "Hispanic",
        "4": "Other",
    },
    "race3": {
        "question": "(recode) What racial or ethnic group best describes you?",
        "1": "White/other",
        "2": "Black",
        "3": "Hispanic",
    },
    "race2": {
        "question": "(recode) What racial or ethnic group best describes you?",
        "1": "White",
        "2": "Non-white",
    },
    "state": {
        "question": "What state do you vote in?",
        "1": "Alabama",
        "2": "Alaska",
        "4": "Arizona",
        "5": "Arkansas",
        "6": "California",
        "8": "Colorado",
        "9": "Connecticut",
        "10": "Delaware",
        "11": "District of Columbia",
        "12": "Florida",
        "13": "Georgia",
        "15": "Hawaii",
        "16": "Idaho",
        "17": "Illinois",
        "18": "Indiana",
        "19": "Iowa",
        "20": "Kansas",
        "21": "Kentucky",
        "22": "Louisiana",
        "23": "Maine",
        "24": "Maryland",
        "25": "Massachusetts",
        "26": "Michigan",
        "27": "Minnesota",
        "28": "Mississippi",
        "29": "Missouri",
        "30": "Montana",
        "31": "Nebraska",
        "32": "Nevada",
        "33": "New Hampshire",
        "34": "New Jersey",
        "35": "New Mexico",
        "36": "New York",
        "37": "North Carolina",
        "38": "North Dakota",
        "39": "Ohio",
        "40": "Oklahoma",
        "41": "Oregon",
        "42": "Pennsylvania",
        "44": "Rhode Island",
        "45": "South Carolina",
        "46": "South Dakota",
        "47": "Tennessee",
        "48": "Texas",
        "49": "Utah",
        "50": "Vermont",
        "51": "Virginia",
        "53": "Washington",
        "54": "West Virginia",
        "55": "Wisconsin",
        "56": "Wyoming",
    },
    # for these, 1: yes and 2: no, _txt are other actions
    "pp18_polactions_txt": {
        "question": ("How have you participated in politics in the last 6 months?")
    },
    "pp18_polactions_1": {
        "question": (
            "Volunteered for a candidate, political party, or other political "
            "organization"
        ),
        "2": "No",
        "1": "Yes",
    },
    "pp18_polactions_2": {
        "question": ("In the last 6 months have you attended a rally or protest"),
        "2": "No",
        "1": "Yes",
    },
    "pp18_polactions_3": {
        "question": (
            "In the last 6 months have you, called or wrote to an " "elected official"
        ),
        "2": "No",
        "1": "Yes",
    },
    "pp18_polactions_4": {
        "question": (
            "In the last 6 months have you, attended a town hall held "
            "by an elected official"
        ),
        "2": "No",
        "1": "Yes",
    },
    "pp18_polactions_5": {
        "question": (
            "In the last 6 months have you, posted about politics on " "social media"
        ),
        "2": "No",
        "1": "Yes",
    },
    "pp18_polactions_6": {
        "question": (
            "In the last 6 months have you, made a donation to a candidate, "
            "party, or other political organization"
        ),
        "2": "No",
        "1": "Yes",
    },
    "pp18_polactions_7": {
        "question": ("In the last 6 months have you, Other"),
        "2": "No",
        "1": "Yes",
    },
    "pp18_polactions_8": {
        "question": ("In the last 6 months have you, I have not done any of the above"),
        "2": "No",
        "1": "Yes",
    },
    "weight_DFP": {
        "question": (
            "The sample was weighted according to age, sex, race, education, "
            "urban/rural status, partisanship, marital status, and Census region "
            "to be nationally representative of 2018 voters according to Catalist, "
            "and to a post-election correction consisting of the national two-party "
            "vote share."
        )
    },
    "EMOTIONS": {
        "question": (
            "Now, when you think about voting in the "
            "upcoming elections for Congress this November, "
            "which of the following emotions best describe "
            "why you are voting? You may choose up to three"
            "responses."
        )
    },
    "EMOTIONS_1": {
        "1": "Yes",
        "2": "No",
        "question": (
            "Now, when you think about voting in the "
            "upcoming elections for Congress this November, "
            "which of the following emotions best describe "
            "why you are voting? You may choose up to three "
            "responses."
        ),
        "title": "('Are you voting in this election because you are angry?')",
    },
    "EMOTIONS_10": {
        "1": "Yes",
        "2": "No",
        "question": (
            "Now, when you think about voting in the "
            "upcoming elections for Congress this November, "
            "which of the following emotions best describe "
            "why you are voting? You may choose up to three "
            "responses."
        ),
        "title": "('Are you voting in this election because you are proud?')",
    },
    "EMOTIONS_11": {
        "1": "Yes",
        "2": "No",
        "question": (
            "Now, when you think about voting in the "
            "upcoming elections for Congress this November, "
            "which of the following emotions best describe "
            "why you are voting? You may choose up to three "
            "responses."
        ),
        "title": "('Are you voting in this election because you are happy?')",
    },
    "EMOTIONS_12": {
        "1": "Yes",
        "2": "No",
        "question": (
            "Now, when you think about voting in the "
            "upcoming elections for Congress this November, "
            "which of the following emotions best describe "
            "why you are voting? You may choose up to three "
            "responses."
        ),
        "title": "('Are you voting in this election because you are confused?')",
    },
    "EMOTIONS_13": {
        "1": "Yes",
        "2": "No",
        "question": (
            "Now, when you think about voting in the "
            "upcoming elections for Congress this November, "
            "which of the following emotions best describe "
            "why you are voting? You may choose up to three "
            "responses."
        ),
        "title": "('Are you voting in this election because you are indifferent?')",
    },
    "EMOTIONS_14": {
        "1": "Yes",
        "2": "No",
        "question": (
            "Now, when you think about voting in the "
            "upcoming elections for Congress this November, "
            "which of the following emotions best describe "
            "why you are voting? You may choose up to three "
            "responses."
        ),
        "title": "('Are you voting in this election because you are bored?')",
    },
    "EMOTIONS_15": {
        "1": "Yes",
        "2": "No",
        "question": (
            "Now, when you think about voting in the "
            "upcoming elections for Congress this November, "
            "which of the following emotions best describe "
            "why you are voting? You may choose up to three "
            "responses."
        ),
        "title": "('Are you voting in this election because you are powerful?')",
    },
    "EMOTIONS_16": {
        "1": "Yes",
        "2": "No",
        "question": (
            "Now, when you think about voting in the "
            "upcoming elections for Congress this November, "
            "which of the following emotions best describe "
            "why you are voting? You may choose up to three "
            "responses."
        ),
        "title": "('Are you voting in this election because you are powerless?')",
    },
    "EMOTIONS_17": {
        "1": "Yes",
        "2": "No",
        "question": (
            "Now, when you think about voting in the "
            "upcoming elections for Congress this November, "
            "which of the following emotions best describe "
            "why you are voting? You may choose up to three "
            "responses."
        ),
        "title": "('Are you voting in this election because you are not sure?')",
    },
    "EMOTIONS_2": {
        "1": "Yes",
        "2": "No",
        "question": (
            "Now, when you think about voting in the "
            "upcoming elections for Congress this November, "
            "which of the following emotions best describe "
            "why you are voting? You may choose up to three "
            "responses."
        ),
        "title": "('Are you voting in this election because you are interested?')",
    },
    "EMOTIONS_3": {
        "1": "Yes",
        "2": "No",
        "question": (
            "Now, when you think about voting in the "
            "upcoming elections for Congress this November, "
            "which of the following emotions best describe "
            "why you are voting? You may choose up to three "
            "responses."
        ),
        "title": "('Are you voting in this election because you are worried?')",
    },
    "EMOTIONS_4": {
        "1": "Yes",
        "2": "No",
        "question": (
            "Now, when you think about voting in the "
            "upcoming elections for Congress this November, "
            "which of the following emotions best describe "
            "why you are voting? You may choose up to three "
            "responses."
        ),
        "title": "('Are you voting in this election because you are hopeful?')",
    },
    "EMOTIONS_5": {
        "1": "Yes",
        "2": "No",
        "question": (
            "Now, when you think about voting in the "
            "upcoming elections for Congress this November, "
            "which of the following emotions best describe "
            "why you are voting? You may choose up to three "
            "responses."
        ),
        "title": "('Are you voting in this election because you are frustrated?')",
    },
    "EMOTIONS_6": {
        "1": "Yes",
        "2": "No",
        "question": (
            "Now, when you think about voting in the "
            "upcoming elections for Congress this November, "
            "which of the following emotions best describe "
            "why you are voting? You may choose up to three "
            "responses."
        ),
        "title": "('Are you voting in this election because you are excited?')",
    },
    "EMOTIONS_7": {
        "1": "Yes",
        "2": "No",
        "question": (
            "Now, when you think about voting in the "
            "upcoming elections for Congress this November, "
            "which of the following emotions best describe "
            "why you are voting? You may choose up to three "
            "responses."
        ),
        "title": "('Are you voting in this election because you are confident?')",
    },
    "EMOTIONS_8": {
        "1": "Yes",
        "2": "No",
        "question": (
            "Now, when you think about voting in the "
            "upcoming elections for Congress this November, "
            "which of the following emotions best describe "
            "why you are voting? You may choose up to three "
            "responses."
        ),
        "title": "('Are you voting in this election because you are helpless?')",
    },
    "EMOTIONS_9": {
        "1": "Yes",
        "2": "No",
        "question": (
            "Now, when you think about voting in the "
            "upcoming elections for Congress this November, "
            "which of the following emotions best describe "
            "why you are voting? You may choose up to three "
            "responses."
        ),
        "title": "('Are you voting in this election because you are depressed?')",
    },
    "USR": {
        "question": " (coded up) Do you live in a rural, suburban, or urban area?",
        "1": "Rural",
        "2": "Suburban",
        "3": "Urban",
    },
    # these are used for analysis and plotting
    "misc": {
        "unknown_cols": [
            "has_voted",
            "senvote18_full",
            "specsenvote18_full",
            "govvote18_full",
            "which_module",
            "house2_imputed",
            "house3",
            "gov2_imputed",
            "gov3",
            "sen2_imputed",
            "sen3",
            "housevote18_full",
            "which_sample",
        ],
        "quant_cols": [
            "FT_Whites",
            "FT_Blacks",
            "FT_Latinos",
            "hostile_sexism_raw",
            "hostile_sexism_scaled",
            "GENDERPERSONALITY_INDEP",
            "GENDERPERSONALITY_EMOT",
            "GENDERPERSONALITY_CONFIDENT",
            "GENDERPERSONALITY_HELPFUL",
            "GENDERPERSONALITY_DECISIONS",
            "NDEMS",
            "hostile_sexism_raw",
            "hostile_sexism_scaled",
            "racial_resentment_raw",
            "racial_resentment_scaled",
            "fear_of_demographic_change_raw",
            "fear_of_demographic_change_scaled",
            "weight_DFP",
        ],
        "other_cols": [
            "state",
            "race_t",
            "senvote18_t",
            "senvote18_undecided_t",
            "specsenvote18_t",
            "specsenvote18_undecided_t",
            "housevote18_t",
            "housevote18_undecided_t",
            "govvote18_t",
            "govvote18_undecided_t",
            "NONVOTE_WHY_t",
            "pp18_polactions_txt",
            "pid3_t",
            "presvote16post_t",
            "e14_presvote12_t",
            "religpew_t",
        ],
        "agree_order": [
            "Strongly agree",
            "Somewhat agree",
            "Neither agree nor disagree",
            "Somewhat disagree",
            "Strongly disagree",
            "Don't know",
        ],
        "age_order": ["18-29", "30-39", "40-49", "50-64", "65+"],
        "net_positivity_dict": {
            "Strongly agree": "Positive",
            "Somewhat agree": "Positive",
            "Neither agree nor disagree": "Neutral",
            "Somewhat disagree": "Negative",
            "Strongly disagree": "Negative",
        },
        "state_dict": {
            "Alaska": "AK",
            "Alabama": "AL",
            "Arkansas": "AR",
            "Arizona": "AZ",
            "California": "CA",
            "Colorado": "CO",
            "Connecticut": "CT",
            "District of Columbia": "DC",
            "Delaware": "DE",
            "Florida": "FL",
            "Georgia": "GA",
            "Hawaii": "HI",
            "Iowa": "IA",
            "Idaho": "ID",
            "Illinois": "IL",
            "Indiana": "IN",
            "Kansas": "KS",
            "Kentucky": "KY",
            "Louisiana": "LA",
            "Massachusetts": "MA",
            "Maryland": "MD",
            "Maine": "ME",
            "Michigan": "MI",
            "Minnesota": "MN",
            "Missouri": "MO",
            "Mississippi": "MS",
            "Montana": "MT",
            "North Carolina": "NC",
            "North Dakota": "ND",
            "Nebraska": "NE",
            "New Hampshire": "NH",
            "New Jersey": "NJ",
            "New Mexico": "NM",
            "Nevada": "NV",
            "New York": "NY",
            "Ohio": "OH",
            "Oklahoma": "OK",
            "Oregon": "OR",
            "Pennsylvania": "PA",
            "Rhode Island": "RI",
            "South Carolina": "SC",
            "South Dakota": "SD",
            "Tennessee": "TN",
            "Texas": "TX",
            "Utah": "UT",
            "Virginia": "VA",
            "Vermont": "VT",
            "Washington": "WA",
            "Wisconsin": "WI",
            "West Virginia": "WV",
            "Wyoming": "WY",
        },
    },
}

with open("../raw_data/dfp_survey_questions.json", "w") as fp:
    json.dump(metadata_dict, fp, sort_keys=True, indent=4)

print("finished")
