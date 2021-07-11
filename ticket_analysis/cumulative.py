import pandas as pd
from datetime import datetime
from datetime import date
import glob
in_path = r'C:\Users\praveen.manivannan\OneDrive - Ultragenic Research and Technologies Limited\TicketStatus\ticket_analysis\archive_file'
out_path = r'C:\Users\praveen.manivannan\OneDrive - Ultragenic Research and Technologies Limited\TicketStatus\ticket_analysis\analysis_file\cummulative.csv'
all_files = glob.glob(in_path + "/*.xlsx")
all_data = pd.DataFrame()
duration = pd.DataFrame()
for filename in all_files:
    dataset = pd.read_excel(filename)
    dataset = dataset[['Created Time', 'Analyze Date','RequestID','Request Status','Technician']]
    #print(filename)
    dataset['Created Time'] = [datetime.strptime(i,'%d-%m-%Y %H:%M') for i in dataset['Created Time']]
    all_data = all_data.append(dataset, ignore_index=True)
all_data = all_data[all_data['Created Time']> datetime.strptime('01-01-2021','%d-%m-%Y')]
all_data.sort_values('Analyze Date')
all_data.to_csv(out_path)
print('Cumulative caculation completed and cummulative.xlsx written')

        
