import pandas as pd
import statistics
import plotly.figure_factory as ff
import plotly.graph_objects as go
import csv

df = pd.read_csv("StudentsPerformance.csv")
StudentsPerformance = df["math score"].to_list()
mean = statistics.mean(StudentsPerformance)
median = statistics.median(StudentsPerformance)
mode = statistics.mode(StudentsPerformance)
stdDeviation = statistics.stdev(StudentsPerformance)


print("This is median",median)
print("This is mode :",mode)
print("This is mean",mean)
print("This is stdDeviation ",stdDeviation)

firstStdDevStart,firstStdDevEnd = mean-stdDeviation,mean+stdDeviation
secondStdDevStart,secondStdDevEnd = mean-(2*stdDeviation),mean+(2*stdDeviation)
thirdStdDevStart,thirdStdDevEnd = mean-(3*stdDeviation),mean+(3*stdDeviation)

print(firstStdDevStart,firstStdDevEnd)
print(secondStdDevStart,secondStdDevEnd)
print(thirdStdDevStart,thirdStdDevEnd)

listOfDataWithinFirstStdDv = [result for result in StudentsPerformance if result>firstStdDevStart and result<firstStdDevEnd]
listOfDataWithinSecondStdDv = [result for result in StudentsPerformance if result>secondStdDevStart and result<secondStdDevEnd]
listOfDataWithinThirdStdDv = [result for result in StudentsPerformance if result>thirdStdDevStart  and result<thirdStdDevEnd]

print("Percentage of data lies within first std deviation ",(len(listOfDataWithinFirstStdDv)*100.0)/len(StudentsPerformance))
print("Percentage of data lier within second std deviation",(len(listOfDataWithinSecondStdDv)*100.0)/len(StudentsPerformance))
print("Percentage of data lier within third std deviation",(len(listOfDataWithinThirdStdDv)*100.0)/len(StudentsPerformance))


fig = ff.create_distplot([StudentsPerformance],["Result"],show_hist=False)
fig.add_trace(go.Scatter(x = [mean,mean],y = [0,0.17],mode = 'lines',name = "Mean"))
fig.add_trace(go.Scatter(x = [firstStdDevStart,firstStdDevStart],y = [0,0.17],mode = 'lines',name = "First Stadred Deviation Start"))
fig.add_trace(go.Scatter(x = [firstStdDevEnd,firstStdDevEnd],y = [0,0.17],mode = 'lines',name = "First Stadred Deviation End"))
fig.add_trace(go.Scatter(x = [secondStdDevStart,secondStdDevStart],y = [0,0.17],mode = 'lines',name = "Second Stadred Deviation Start"))
fig.add_trace(go.Scatter(x = [secondStdDevEnd,secondStdDevEnd],y = [0,0.17],mode = 'lines',name = "Second Stadred Deviation End"))
fig.add_trace(go.Scatter(x = [thirdStdDevStart,thirdStdDevStart],y = [0,0.17],mode = 'lines',name = "Third Stadred Deviation Start"))
fig.add_trace(go.Scatter(x = [thirdStdDevEnd,thirdStdDevEnd],y = [0,0.17],mode = 'lines',name = "Third Stadred Deviation End"))
fig.show()


