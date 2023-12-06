import pandas as pd

def calculate_demographic_data(print_data=True):

    df = pd.read_csv("adult.data.csv")

    race_count = df["race"].value_counts()

    average_age_men = df[df["sex"] == "Male"]["age"].mean()

    percentage_bachelors = (df["education"] == "Bachelors").sum() / df.shape[0] * 100

    higher_education = df[df["education"].isin(["Bachelors", "Masters", "Doctorate"])]
    percentage_higher_education = (higher_education["salary"] == ">50K").sum() / higher_education.shape[0] * 100

    lower_education = df[~df["education"].isin(["Bachelors", "Masters", "Doctorate"])]
    percentage_lower_education = (lower_education["salary"] == ">50K").sum() / lower_education.shape[0] * 100

    min_work_hours = df["hours-per-week"].min()

    num_min_workers = df[df["hours-per-week"] == min_work_hours]
    rich_percentage = (num_min_workers["salary"] == ">50K").sum() / num_min_workers.shape[0] * 100

    country_stats = df[df["salary"] == ">50K"]["native-country"].value_counts(normalize=True) * 100
    highest_earning_country = country_stats.idxmax()
    highest_earning_country_percentage = country_stats.max()

    top_IN_occupation = df[(df["native-country"] == "India") & (df["salary"] == ">50K")]["occupation"].value_counts().idxmax()

    if print_data:
        print("Race count:\n", race_count)
        print("\nAverage age of men:", round(average_age_men, 1))
        print("\nPercentage with Bachelors degrees:", round(percentage_bachelors, 1))
        print("\nPercentage with higher education that earn >50K:", round(percentage_higher_education, 1))
        print("\nPercentage without higher education that earn >50K:", round(percentage_lower_education, 1))
        print("\nMin work hours per week:", min_work_hours)
        print("\nPercentage of rich among those who work fewest hours:", round(rich_percentage, 1))
        print("\nCountry with highest percentage of rich:", highest_earning_country)
        print("\nPercentage of rich people in the country:", round(highest_earning_country_percentage, 1))
        print("\nTop occupation in India:", top_IN_occupation)

    return {
        "race_count": race_count,
        "average_age_men": round(average_age_men, 1),
        "percentage_bachelors": round(percentage_bachelors, 1),
        "percentage_higher_education": round(percentage_higher_education, 1),
        "percentage_lower_education": round(percentage_lower_education, 1),
        "min_work_hours": min_work_hours,
        "rich_percentage": round(rich_percentage, 1),
        "highest_earning_country": highest_earning_country,
        "highest_earning_country_percentage": round(highest_earning_country_percentage, 1),
        "top_IN_occupation": top_IN_occupation
    }
