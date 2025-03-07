# Calculate Special Bonus

import pandas as pd

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    employees['bonus'] = employees.apply(lambda x : x['salary']
                                         if x['employee_id'] % 2 and
                                         not x['name'].startswith('M')
                                         else 0, axis = 1)
    df = employees[['employee_id', 'bonus']].sort_values('employee_id')
    print(df)
    return df

data = [[2, 'Meir', 3000], [3, 'Michael', 3800], [7, 'Addilyn', 7400], [8, 'Juan', 6100], [9, 'Kannon', 7700]]
employees = pd.DataFrame(data, columns=['employee_id', 'name', 'salary']).astype({'employee_id':'int64', 'name':'object', 'salary':'int64'})
calculate_special_bonus(employees)