import time
import pandas as pd
import numpy as np

months = ['january', 'february', 'march', 'april', 'may', 'june']
days = [1,2,3,4,5,6,7]

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("Would you like to see data for Chicago, New York, or Washington?\n")
        if city.lower() not in CITY_DATA:
            print("invalid option.")
        else:
            break


    # get user input for month (all, january, february, ... , june)
    month = input("Which month? January, february, March, April, May, or June or all?\n").lower()

    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("Which day? Please type your response as an integer (e.g.), 1=Sunday) or all.\n")

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday
    df['hour'] = df['Start Time'].dt.hour
    if month != 'all':
        month =  months.index(month) + 1
        df = df[ df['month'] == month ]
    if day != 'all':
        day =  days.index(int(day)) - 1
        df = df[ df['day_of_week'] == day ]
    return df


def time_stats(df):

        """Displays statistics on the most frequent times of travel."""

        print('\nCalculating The Most Frequent Times of Travel...\n')
        start_time = time.time()

    # display the most common month
        most_common_month = df['month'].value_counts().idxmax()
        print("The most common month is : " + str(most_common_month))


    # display the most common day of week
        most_common_day = df['day_of_week'].value_counts().idxmax()
        print("The most common dayofweek is : " + str(most_common_day))

    # display the most common start hour
        most_common_hour = df['hour'].value_counts().idxmax()
        print("The most common hour is : " + str(most_common_hour))

        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    most_common_start_station = df['Start Station'].value_counts().idxmax()
    print("The most common start station : "+ str(most_common_start_station))

    # display most commonly used end station
    most_common_end_station = df['End Station'].value_counts().idxmax()
    print("The most common end station : " + str(most_common_end_station))

    # display most frequent combination of start station and end station trip
    most_common_combination = df[['Start Station', 'End Station']].mode().loc[0]
    print("The most common combination - start and end : " + str(most_common_combination))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    travel_duration_sum = df['Trip Duration'].sum()
    print('\nthe sum of trip duration in secounds is :' + str(travel_duration_sum))
    # display mean travel time
    travel_duration_mean = df['Trip Duration'].mean()
    print('\nthe mean of trip duration is :' + str(travel_duration_mean))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_counts = df['User Type'].value_counts()
    print('\nthe  counts of user types is :' + '\n' + str(user_counts))

    # Display counts of gender

    try:
        gender_counts = df['Gender'].value_counts()
        print('\nthe  counts of gender is :' + '\n' + str(gender_counts))
    # Display earliest, most recent, and most common year of birth
        birth_year_min = df['Birth Year'].min()
        birth_year_max = df['Birth Year'].max()
        birth_year_common = df['Birth Year'].value_counts().idxmax()
        print(('\nthe earliest year of birth is :' + '\n' + str(int(birth_year_min))))
        print(('\nthe most recent year of birth is :' + '\n' + str(int(birth_year_max))))
        print(('\nthe most common year of birth is :' + '\n' + str(int(birth_year_common))))
    except KeyError:
        pass
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_row_data(df):
    """Displays raw bikeshare data."""
    is_row = input("\nWould you like to examine a random 5 users trip data? Type \'yes\' or \'no\' ----very importent: in pandas Monday == 0 … Sunday == 6\n")
    if is_row.lower() != 'yes':
        return
    chosen_idx = np.random.choice(len(df), size = 5)
    random_row_data = df.iloc[chosen_idx]
    print(random_row_data)

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_row_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
