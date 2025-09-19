from ydata_profiling import ProfileReport
import pandas as pd
 
data = pd.read_excel('files/consolidados_IPM.xlsx')

data["Cluster"].describe()
# print('hola')

# report = ProfileReport(data)
# report.to_file("report.html")


if __name__ == "__main__":

    # print(data.info())
    data["Cluster"].describe()
    profile = ProfileReport(data, title="v1")
    profile.te_notebook.iframe()
    profile.to_file("v1.html")