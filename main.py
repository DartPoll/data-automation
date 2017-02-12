#Michael Zhu
#Loops through demographics, calculates chi-square values, returns dictionary of demographics with corresponding chi-square values

def main(survey_dict):

    #Create return dictionaries
    chi_square_dict = {}

    #Looping:
    #Loop through survey for each question
    #Loop through each question for answer choices
    #Loop through each answer choice to access demographic
    #Loop through demographic to access categories (e.g. white, male, etc.)
    #Run-time seems pretty bad?
    for questionID in survey_dict:
        if questionID == "Total":
            total_res = survey_dict["Total"]["Total"]
            continue

        for answerchoice in survey_dict[questionID]:

            for demographic in survey_dict[questionID][answerchoice]:
                if demographic == 'Total':
                    continue

                for category in survey_dict[questionID][answerchoice][demographic]:
                    # Calculate chi-square value
                    value = survey_dict[questionID][answerchoice][demographic][category]
                    expected = value * survey_dict[questionID][answerchoice]["Total"] / total_res
                    chi_value = abs((value - int(expected) ** 2) / int(expected))

                    # If category is in dictionary, just add value to existing chi-value sum associated with category
                    # Otherwise, create a new entry
                    if category in chi_square_dict:
                        chi_square_dict[category] += chi_value
                    else:
                        chi_square_dict[category] = chi_value

    #Return chi_square_dictionary
    return chi_square_dict
