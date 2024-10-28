import pandas as pd #alias
import functions
grades_dict = {'Wally': [87, 96, 70],
               'Eva': [100, 87, 90],
               'Sam': [94, 77, 90],
               'Katie': [100, 81, 82],
               'Bob': [83, 65, 85]}
grades_df = pd.DataFrame(grades_dict)
grades_df.index = ['test1', 'test2', 'test3']
functions.print_it('Dictionary entries', grades_df)
# create a dataframe with 3-digit student numbers as index, 
# and data that stores three quiz grades  <<< TO DO
grades2_dict = { 'name': ['Samir', 'Lana', 'Xav'],
                 'quiz1' : [33,55,77],
                 'quiz2' : [34,57,74],
                 'quiz3' : [31,52,76]
}
grades2_df = pd.DataFrame(grades2_dict)
grades2_df.index = [232,433,677]
functions.print_it('Grade book 2', grades2_df)