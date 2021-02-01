import time
import pandas as pd
import numpy as np

# Defintion of the arraies
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
MONTHS = ['all', 'january', 'february','march','april','may',
'june','july','august','september','october','november','december']
DAYS = ['all', 'saturday', 'sunday','monday','tuesday','wednesday',
'thursday','friday']


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    city_=''
    month_=''
    day_ = '' # to test the loops

    print('Hello! Let\'s explore some US bikeshare data!\n')

    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while city_.lower() not in CITY_DATA:
        city_ = input("Please enter the city name chicago, new york, washigtonl \n")
        if city_.lower() in CITY_DATA:
            city = CITY_DATA[city_.lower()]
        else:
            print("please enter vaild city name either chicago, new york or washigton \n")


    # get user input for month (all, january, february, ... , june)
    while month_.lower() not in MONTHS:
        month_ = input("Please enter month all, january, february, ... etc, \n")
        if month_.lower() in MONTHS:
            month = month_.lower()
        else:
            print("please enter vaild month all, january, february, ... etc \n")



    # get user input for day of week (all, monday, tuesday, ... sunday)
    while day_.lower() not in DAYS:
        day_ = input("Please enter vaild day day of week (all, monday, tuesday, ... sunday ... etc, \n")
        if day_.lower() in DAYS:
            day = day_.lower()
        else:
            print("please enter vaild day name of week all, monday, tuesday, ... sunday ... etc \n")

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
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

        # filter by day of week if applicable
    if day != 'all':

        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month = df['month'].mode()[0]
    print("\n The most common month is : " + MONTHS[most_common_month].title())

    # TO DO: display the most common day of week
    most_common_day = df['day'].mode()[0]
    print("\n The most common day of the week is : " + DAYS[most_common_day].title())

    # TO DO: display the most common start hour
    most_common_hour = df['hour'].mode()[0]
    print("\n The most common hour is : " + str(most_common_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_start_station = df['Start Station'].mode()[0]
    print("\n The most common hour is : " + most_start_station)

    # TO DO: display most commonly used end station
    most_end_station = df['End Station'].mode()[0]
    print("\n The most common hour is : " + most_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    frequent_trip = (df['Start Station'] + "||" + df['End Station'].mode()[0])
    print("\n The most frequent combination of start and end station is : " + frequent_trip)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_time = df['Trip Duration'].sum()
    print("\n" , total_time)

    # TO DO: display mean travel time
    mean_time = df['Trip Duration'].mean()


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Types'].value_counts()
    print("\n user types is: \n", user_types)


    # TO DO: Display counts of gender
    print("\n number of user gender is: \n" +  df['Gender'].unique())

    # TO DO: Display earliest, most recent, and most common year of birth
    earliest_year_birth = df['Birth Year'].min()
    recent_year_birth = df['Birth Year'].max()
    most_common_year_birth = df['Birth Year'].mode()[0]
    print("\n The earliest year birth is : {}".format(earliest_year_birth))
    print("\n The recent year birth is : {}".format(recent_year_birth))
    print("\n The most common year birth is : {}".format(most_common_year_birth))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def display_data(df):
    """Displays raw data depends user request """

    print(df.head())
    next = 0
    while True:
        raw_data = input('\n Would you like to see the next five row of raw data? Enter yes or no.\n')
        if raw_data.lower() != 'yes':
            return
        next = next + 5



def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df) #print raw data

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
