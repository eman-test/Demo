import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york.csv',
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
    city =   input("Please select the city you want to analyze data about (chicago, new york, washington):\n").lower()
    city_options  =   ["chicago", "new york", "washington"]
    while city not in city_options:
        city =  input(""" please select the correct city:
    -chicago
    -new york
    -washington
    """)

    month =   input("please select month you need to filter(january, february, ... , june)? Type 'all' for no filter:\n").lower()
    month_options = ["january", "february", "march", "april", "may", "june","all"]
    while month not in month_options:
        month  =  input(""" please select the correct month :
    -january
    -february
    -march
    -april
    -may
    -june
    -all
    """)

    day = input("please select the day(sunday, monday,tuesday,...,friday)? Type 'all' for no filter:\n").lower()
    day_options = ["sunday", "monday", "tuesday","wednesday","thursday","friday","saturday","all"]
    while day not in day_options:
       day =  input(""" please select the correct day:
    -sunday
    -monday
    -tuesday
    -wednesday
    -thursday
    -friday
    -saturday
    -all
    """)
    #print("city")
    print('-'*40)
    return city, month, day



def load_data(city, month, day):
    df = pd.read_csv(CITY_DATA[city])
    #city_file = 'chicago.csv'
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]
        if day != 'all':
            df = df[df['day_of_week'] == day.title()]
        # filter by day of week to create the new dataframe
        
    
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
   

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    df['month'] = df['Start Time'].dt.month
    frq_month = df['month'].mode()[0]
    print("most frequent month is: \n")
    print(frq_month)

    # TO DO: display the most common day of week
    df['day_of_week'] = df['Start Time'].dt.month
    frq_week = df['day_of_week'].mode()[0]
    print("most frequent day is: \n")
    print(frq_week)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.month
    frq_hour = df['hour'].mode()[0]
    print("most frequent hour is: \n")
    print(frq_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_station_frq = df['Start Station'].mode()[0]
    print("Most Frequency Start Station is: \n")
    print(start_station_frq)

# TO DO: display most commonly used end station
    end_station_frq = df['End Station'].mode()[0]
    print("Most Frequency End Station is: \n")
    print(end_station_frq)

    # TO DO: display most frequent combination of start station and end station trip
    df['combination'] = df['Start Station'] + df['End Station']
    comb_start_end =  df['combination'].mode()[0]
    print("Combination of Start and End Stations are: \n")
    print(comb_start_end)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    
    total_trip_time= df['Trip Duration'].sum()
    print("Total Trip Time is: \n")
    print(total_trip_time)

    avg_trip_time= df['Trip Duration'].mean()
    print("Avg Trip Time is: \n")
    print(avg_trip_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type_count= df['User Type'].value_counts()
    print("Total User Count is: \n")
    print(user_type_count)
    
    # TO DO: Display counts of gender
    if 'Gender' in df:
        gender_count=df['Gender'].value_counts()
        print("Gender Count is:\n")
        print(gender_count)
    else:
        print("There's no Gender for this city")
    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        earliest_year= df['Birth Year'].min()
        print("The Earlist Year is :\n")
        print(earliest_year)
        recent_year= df['Birth Year'].max()
        print("The Most Recent Year is :\n")
        print(recent_year)
        common_year= df['Birth Year'].mode()[0]
        print("The Most Common Year is :\n")
        print(common_year)
    else:
        print("There's no Birth Year for this city")
        
        print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
        
def user_data(df):     
    user_data= input("Do you want to see the data? (please answer with  'Yes' or 'No') :\n").lower()
    if user_data not in ['yes', 'no']:
        user_data = input("Please type Yes or No.\n").lower()
    data=0
    while True:
        if user_data == 'yes':
           print(df.iloc[data : data + 5])
           data += 5
           ask_again= input("Do you want to see more extra data? (please answer with 'Yes' or 'No') :\n").lower()
           if ask_again not in ['yes', 'no']:
                ask_again=  input("Please type Yes or No.\n").lower()
           if ask_again != 'yes':
                    break
        elif user_data == 'no':
           return        
       

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        user_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
	
	
	
	
	
	
	
	# https://github.com/pss2138/Udacity-Programming-for-Data-Science-with-Python-Project2/blob/master/bikeshare.py
	
