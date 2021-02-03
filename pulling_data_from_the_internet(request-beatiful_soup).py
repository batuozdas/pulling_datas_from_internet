import requests
from bs4 import BeautifulSoup

r = requests.get('https://www.skysports.com/premier-league-table/2019')
soup = BeautifulSoup(r.content,'html.parser')
data = soup.find_all('td',{'class':'standing-table__cell'})
datas = []
for i in data:
    text = i.text
    datas.append(text)
# datas value will be like ['1','\nLiverpool\n','38','32','3','3','85','33','52','99','\n',
                         #  '2','\nManchester City\n','38','26','3','9','102','35','67','81','\n',
                         #  '3','\nManchester United\n','38',...]
# Now we have to seperate datas to categories. For that we will create empty lists.
numbers = [] ; team_names = [] ; total_games = [] ; won_games = [] ; tied_games = [] ; lost_games = []
goals_for = [] ; goals_against = [] ; goal_difference = [] ; points = []

# We create a categories.
categories = ['numbers','team_names','total_games','won_games','tied_games','lost_games','goals_for','goals_against','goal_difference','points']
for category in categories:
    indice = categories.index(category) # We take index of every category from categories list.
    # If category is 'numbers' indice will be equal to 0. We will get in a for loop. j value will increase 11 by 11 between 0 and length of 'datas' value.
    # The reason why we increased j value by 11, if you look at lines between 11-14, between every categories there are 11 elements. j value will be (0,11,22,33,44,55,...)
    # we use globals()[category] to change strings to variable. In this case category is equal to numbers. Numbers will be variable after globals command. Now we can add 
    # datas[j] values (in this case these values will be: '1','2','3','4',...) to numbers list. 
    # After 'numbers' category is over, new category will be 'team_names'. indice of team_names will be 1. j value will be (1,12,23,34,45,56,...). We will change string 
    # 'team_names' value to variable 'team_names' value. And we will add datas[j] values (in this case these values will be:'\nLiverpool\n','\nManchester City\n',
    # '\nManchester United\n',... ) to team_names list. As you can see there are '\n' characters in these names. To delete these characters we use replace command.
    # And for loop will continue to every categories are seperated.
    for j in range(indice,len(datas),11):
        globals()[category].append(datas[j].replace('\n',''))

# If code lines from 18 to 31 is so complicated, you can use code lines from 34 to 44. They both do the same things.
"""for i in range(0,len(datas),11):
    numbers.append(datas[i])
    team_names.append(datas[i+1].replace('\n', ''))
    total_games.append(datas[i+2])
    won_games.append(datas[i+3])
    tied_games.append(datas[i+4])
    lost_games.append(datas[i+5])
    goals_for.append(datas[i+6])
    goals_against.append(datas[i+7])
    goal_difference.append(datas[i+8])
    points.append(datas[i+9])"""

# After seperating categories, now we need to zip them. numbers = ['1','2','3',...]
                                                      # team_names = ['Liverpool','Manchester City','Manchester United',...]
                                                      # total_games = ['38','38','38',...]
                                                      # won_games = ['32','26','18',...]
# After zip command they will be like this: [{1,Liverpool,38,32,...},{2,Manchester City,38,26,...},{3,Manchester United,38,18,...}]
table = list(zip(numbers,team_names,total_games,won_games,tied_games,lost_games,goals_for,goals_against,goal_difference,points))
print(table)
# For better visual, we are gonna use pandas library.
import pandas as pd
df = pd.DataFrame(table,columns=['No','Team Name','GP','Won','Tied','Lost','Goals For',
                                 'Goals Against','Goal Difference','Points'])
df = df.set_index('No')
print(df)