import pandas as pd
from datetime import datetime
from datetime import date
from datetime import timedelta
import numpy as np
in_path = r'C:\Users\praveen.manivannan\OneDrive - Ultragenic Research and Technologies Limited\TicketStatus\05-JUL\cummulative.csv'
out_path = r'C:\Users\praveen.manivannan\OneDrive - Ultragenic Research and Technologies Limited\TicketStatus\05-JUL\duration.xlsx'
dataset = pd.read_csv(in_path)
duration = pd.DataFrame(columns = ['Created Time','Technician','RequestID','Open','In Progress','Awaiting Approval','Awaiting User','Awaiting Governance','Closed', 'ToAwaitingGovernance','ToClosure'])
dataset.set_index(['Created Time'])
duration['RequestID'] = dataset['RequestID'].unique()
duration.set_index('RequestID',inplace=True)
for i in duration.index:
    #duration.loc[i]['Open'] = dataset.loc[((dataset['RequestID']==i) & (dataset['Request Status']=='Open')), 'Analyze Date']
    #--Created Time--
    temp = dataset.loc[(dataset['RequestID']==i),'Created Time'].tolist()
    duration.loc[i]['Created Time'] = datetime.strptime(temp[0],'%Y-%m-%d %H:%M:%S')
    #---Technician--
    temp = dataset.loc[(dataset['RequestID']==i),'Technician'].tolist()
    duration.loc[i]['Technician'] = temp[len(temp)-1]
    #--Open--
    temp = dataset.loc[((dataset['RequestID']==i) & (dataset['Request Status']=='Open')), 'Analyze Date'].tolist()
    if len(temp) !=0:
        duration.loc[i]['Open'] = datetime.strptime(temp[0],'%Y-%m-%d %H:%M:%S')
    #--In Progress--
    temp = dataset.loc[((dataset['RequestID']==i) & (dataset['Request Status']=='In Progress')), 'Analyze Date'].tolist()
    if len(temp) !=0: 
        duration.loc[i]['In Progres'] = datetime.strptime(temp[0],'%Y-%m-%d %H:%M:%S')
    #--Awaiting Approval--
    temp = dataset.loc[((dataset['RequestID']==i) & (dataset['Request Status']=='Awaiting Approval')), 'Analyze Date'].tolist()
    if len(temp) !=0: 
        duration.loc[i]['Awaiting Approval'] = datetime.strptime(temp[0],'%Y-%m-%d %H:%M:%S')
    #--Awaiting User--
    temp = dataset.loc[((dataset['RequestID']==i) & (dataset['Request Status']=='Awaiting User')), 'Analyze Date'].tolist()
    if len(temp) !=0: 
        duration.loc[i]['Awaiting User'] = datetime.strptime(temp[0],'%Y-%m-%d %H:%M:%S')
    #--Awaiting Governance -
    temp = dataset.loc[((dataset['RequestID']==i) & (dataset['Request Status']=='Awaiting Governance')), 'Analyze Date'].tolist()
    if len(temp) !=0: 
        duration.loc[i]['Awaiting Governance'] = datetime.strptime(temp[0],'%Y-%m-%d %H:%M:%S')
        duration.loc[i]['ToAwaitingGovernance'] =(duration.loc[i]['Awaiting Governance'] - duration.loc[i]['Created Time'])/pd.Timedelta(days=1)    #--Closed--
    temp = dataset.loc[((dataset['RequestID']==i) & (dataset['Request Status']=='Closed')), 'Analyze Date'].tolist()
    if len(temp) !=0: 
        duration.loc[i]['Closed'] = datetime.strptime(temp[0],'%Y-%m-%d %H:%M:%S')
        duration.loc[i]['ToClosure'] = (duration.loc[i]['Closed'] - duration.loc[i]['Created Time'])/pd.Timedelta(days=1)
duration.to_excel(out_path)
    
    
