import pandas as pd

if __name__ == '__main__':
    df = pd.read_csv('salary.csv', index_col=0)
    print(df.head())
    print(df.columns)

    f = open("triadic_dataset.csv", "w")
    for index, row in df.head(5000).iterrows():
        income_value = 'income_' + str(index)
        try:
            if row['capital-gain'] > 60000:
                s = income_value + ',capital-gain,' + row['salary'] + "\n"
                f.write(s)
            if row['education-num'] > 16:
                s = income_value + ',education-num,' + row['salary'] + "\n"
                f.write(s)
            if row['hours-per-week'] > 60:
                s = income_value + ',hours-per-week,' + row['salary'] + "\n"
                f.write(s)
            if row['capital-loss'] > 1000:
                s = income_value + ',capital-loss,' + row['salary'] + "\n"
                f.write(s)
            if row['marital-status'] in [' Divorced']:
                s = income_value + ',marital-status,' + row['salary'] + "\n"
                f.write(s)
            if row['relationship'] in [' Not-in-family']:
                s = income_value + ',relationship,' + row['salary'] + "\n"
                f.write(s)

        except:
            print('Entry could not be added.')
    f.close()

