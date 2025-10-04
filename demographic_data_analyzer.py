import pandas as pd
import numpy as np
def calculate_demographic_data(print_data=True):
    data = pd.read_csv("C:/Users/LENOVO/OneDrive/Escritorio/Samuel Jara/Programación/FreeCodeCamp/adult.data.csv")
    
    race_count = data["race"].value_counts()
    average_age_men = data[data["sex"] == "Male"]["age"].mean()
    percentage_bachelors = (data["education"] == "Bachelors").mean() * 100
    
    higher_education = data['education'].isin(['Bachelors','Masters','Doctorate'])
    lower_education = ~higher_education
    
    higher_education_rich = (data[higher_education]['salary'] == '>50K').mean() * 100
    lower_education_rich = (data[lower_education]['salary'] == '>50K').mean() * 100
    
    min_work_hours = data["hours-per-week"].min()
    num_min_workers = ((data["hours-per-week"] == min_work_hours) & (data["salary"] == ">50K")).sum()
    rich_percentage = (data["salary"] == ">50K").mean() * 100
    
    highest_earning_country = (data["salary"] == ">50K").groupby(data["native-country"]).mean().idxmax()
    highest_earning_country_percentage = ((data["salary"] == ">50K").groupby(data["native-country"]).mean() * 100).max()
    
    top_IN_occupation = data[(data["salary"] == ">50K") & (data["native-country"] == "India")]["occupation"].value_counts().idxmax()
    
    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Number of rich among those who work fewest hours: {num_min_workers}")
        print(f"Percentage of rich overall: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'num_min_workers': num_min_workers,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }

print(calculate_demographic_data())

































"""data = pd.read_csv("C:/Users/LENOVO/OneDrive/Escritorio/Samuel Jara/Programación/FreeCodeCamp/adult.data.csv")

def calculate_demographic_data(print_data=True):
    # Read data from file
    data = pd.read_csv("C:/Users/LENOVO/OneDrive/Escritorio/Samuel Jara/Programación/FreeCodeCamp/adult.data.csv")
    
    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = data["race"].nunique()

    # What is the average age of men?
    average_age_men = (data["sex"] == "Male").mean()

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = (data["education"]=="Bachelors").mean() * 100

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = data['education'].isin(['Bachelors','Masters','Doctorate']).sum()
    lower_education = (~data['education'].isin(['Bachelors','Masters','Doctorate'])).sum()

    # percentage with salary >50K
    higher_education_rich = (data["education"].isin(["Bachelors", "Masters", "Doctorate"]) & (data["salary"] == ">50K")).mean() * 100
    lower_education_rich = (data[~data['education'].isin(['Bachelors','Masters','Doctorate'])]['salary'] == '>50K').mean() * 100

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = data["hours-per-week"].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = ((data["hours-per-week"] == data["hours-per-week"].min()) & (data["salary"] == ">50K")).sum()

    rich_percentage = ((data["salary"] == ">50K")).sum()

    # What country has the highest percentage of people that earn >50K?
    highest_earning_country = (data["salary"] == ">50K").groupby(data["native-country"]).mean().idxmax()
    highest_earning_country_percentage = ((data["salary"] == ">50K").groupby(data["native-country"]).mean() * 100).idxmax()


    # Identify the most popular occupation for those who earn >50K in India.
    top_IN_occupation = top_IN_occupation = data[(data["salary"] == ">50K") & (data["native-country"] == "India")]["occupation"].value_counts().idxmax()

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }

print(calculate_demographic_data(data))"""