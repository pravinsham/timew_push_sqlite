import pandas as pd
from datetime import datetime
in_path = r'C:\Users\praveen.manivannan\OneDrive - Ultragenic Research and Technologies Limited\TicketStatus\ticket_analysis\current_file\GASGC_Agenda.xlsx'
out_path = r'C:\Users\praveen.manivannan\OneDrive - Ultragenic Research and Technologies Limited\TicketStatus\ticket_analysis\analysis_file\DailyOpenTickets.xlsx'
dataset = pd.read_excel(in_path)
dataset = dataset[['RequestID','Subject','Request Status','Requester','Technician','Group','Priority','Created Time','Due By Time','Last Updated Time']]
dataset['Created Time'] = [datetime.strptime(i,'%d-%m-%Y %H:%M') for i in dataset['Created Time']]
dataset['Last Updated Time'] = [datetime.strptime(i,'%d-%m-%Y %H:%M') for i in dataset['Last Updated Time']]
dataset['Due By Time'] = ['01-01-1900 00:00' if i == '-'  else i for  i in dataset['Due By Time']]
dataset['Due By Time'] = [datetime.strptime(i,'%d-%m-%Y %H:%M') for i in dataset['Due By Time']]
dataset.to_excel(out_path)
print("Daily Open Tickes Calculation Completed")