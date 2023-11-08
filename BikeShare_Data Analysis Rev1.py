import time
import pandas as pd
import numpy as np

CITY_DATA = { 'Chi': 'chicago.csv',
              'Ny': 'new_york_city.csv',
              'W': 'washington.csv' }

cities=['Chi','Ny','W']
months=['January', 'February', 'March', 'April', 'May', 'June', 'All']
days=['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday','All' ]

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input("Please enter the name of the city you are interested in, in this format: Chi, Ny or W for Chicago, New York City and Washington respectively\n\n").title()
    
    while city not in cities:
        print("This City selection is not valid. Please try again!")
        city = input("Please enter the name of the city you are interested in, in this format: Chi, Ny or W for Chicago, New York City and Washington respectively\n\n").title()
        
    df = pd.read_csv(CITY_DATA[city])
    # TO DO: get user input for month (all, january, february, ... , june)
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['months']= df['Start Time'].dt.month_name
    month = input("\n\nPlease select the month of interest as in: January or type All if you need no filter applied\n\n").title()
    while month not in months:
        print("This Month selection is not valid. Please try again!")
        month = input("\n\nPlease select the month of interest as in: January or type All if you need no filter applied\n\n").title()
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    df['days']=df['Start Time'].dt.day_name
    day = input("\n\nPlease select the day of interest as in: Monday or type All if you need no filter applied\n\n").title()
    while day not in days:
        print("This Day selection is not valid. Please try again!")
        day = input("\n\nPlease select the day of interest as in: Monday or type All if you need no filter applied\n\n").title()

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
    df['months_year']= df['Start Time'].dt.month_name()
    df['days_of_week']=df['Start Time'].dt.day_name()
    
    if month != "All":
        df = df[df['months_year']==month]
    if day != "All":
        df = df[df['days_of_week']==day]
        
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month = df['months_year'].mode()[0]
    print('\n Most common month is', most_common_month)

    # TO DO: display the most common day of week
    most_common_day = df['days_of_week'].mode()[0]
    print('\n Most common day is', most_common_day)
    
    # TO DO: display the most common start hour
    df['Start hour']=df['Start Time'].dt.hour
    most_common_start_hour = df['Start hour'].mode()[0]
    print('\n Most common start hour is', most_common_start_hour)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_used_start_stations = df['Start Station'].mode()[0]
    print ("\n Most used Start Stations: ", most_used_start_stations)                              

    # TO DO: display most commonly used end station
    most_used_end_stations = df['End Station'].mode()[0]
    print ("\n Most used End Stations: ", most_used_end_stations)

    # TO DO: display most frequent combination of start station and end station trip
    df['Full Trip'] = df['Start Station'] +"   "+"-->"+"   "+ df['End Station']
    most_common_trip = df['Full Trip'].mode()[0]
    print ("\n Most common trips: ", most_common_trip)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total travel time: ', total_travel_time)

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('Mean travel time: ', mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    count_of_user_types = df['User Type'].value_counts()
    print("\nCounts of user types are:\n", count_of_user_types)


    # TO DO: Display counts of gender
    if 'Gender' in df:
        count_of_genders = df['Gender'].value_counts()
        print('\nCounts of gender:\n', count_of_genders)
    else:
        print('\nGender stats is not available in this dataframe\n')


    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Gender' in df:
        earliest_year = df['Birth Year'].min()
        print('\nEarliest year of birth: ', earliest_year)
        most_recent_year = df['Birth Year'].max()
        print('\nMost recent year of birth: ', most_recent_year)
        most_common_year = df['Birth Year'].mode()[0]
        print('\nMost common year of birth: ', most_common_year)
    else:
        print('\nYear of Birth data is not available in this dataframe\n')
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def raw_data(city):
    
    df = pd.read_csv(CITY_DATA[city])
    
    print('\nRaw data is available to check')
    start = 0
    while True:
        Answer = input('\nDo you want to have a look on the raw data in 5 rows at a time? Type yes or no\n').lower()
        if Answer not in ['yes', 'no']:
            print('\nInvalid answer. Please try again!')
        elif Answer == 'yes':
            print(df.iloc[start:start+5])
            start = start + 5
        elif Answer == 'no':
            break
            
def main():
    while True:
        city, month, day = get_filters()
        print(city, month, day)
        df = load_data(city, month, day)
        print(df.head())
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(city)
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
