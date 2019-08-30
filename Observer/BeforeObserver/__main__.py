from kpi_data import KPI_Data 

# REport in current KPI values
for kpi in KPI_Data:
    if kpi.name == 'open':
        print("Current open ticket {}".format(kpi.value))
    elif kpi.name == "new":
        print('New tickets for today is {}'.format(kpi.value))
    elif kpi.name == 'closed':
        print('the ticket closed for today is {}'.format(kpi.value))