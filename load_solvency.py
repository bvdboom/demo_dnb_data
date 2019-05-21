def read_sheet(num, xls):
    sheet = xls.parse(num)
    # columns names to lower
    sheet.columns = [c.lower() for c in sheet.columns]
    # set index to relatienaam and periode
    sheet.set_index(['relatienaam', 'periode'], inplace = True)
    # data cleaning (the excel sheet contains some process data
    drop_list = [i for i in sheet.columns if "unnamed" in i]
    sheet.drop(drop_list, axis = 1, inplace = True)
    if "selectielijst" in sheet.columns:
        sheet.drop("selectielijst", axis = 1, inplace = True)
    if "row_name" in sheet.columns:
        sheet.drop("row_name", axis = 1, inplace = True)
        sheet = sheet.pivot(columns = 'row_header')
    sheet.fillna(0, inplace = True)
    # shortening some column names of the balance sheet
    if num == 14:
        sheet.columns = [c.replace(" , solvency ii value","") for c in sheet.columns]
        sheet.columns = [c.replace("assets|","") for c in sheet.columns]
        sheet.columns = [c.replace("liabilities|","") for c in sheet.columns]
    return sheet
