import xlrd
import os
'''
Created By:
Created Date:
Reviewd By:
Modified By:
Parameters:
return Type:
Purpose:
'''
def getRowCount(FileName,SheetName):
    rc=0
    try:
        wb = xlrd.open_workbook(FileName)
        sheet = wb.sheet_by_name(SheetName)
        rc = sheet.nrows
        return rc
    except Exception:
        print("Invalid File Name or Sheet Name !!!!!")




'''
Created By:
Created Date:
Reviewd By:
Modified By:
Parameters:
return Type:
Purpose:
'''
def getColumnCount(FileName,SheetName):
    cc=0
    try:
        wb = xlrd.open_workbook(FileName)
        sheet = wb.sheet_by_name(SheetName)
        cc = sheet.ncols
        return cc - 1
    except Exception:
        print("Invalid File Name or Sheet Name !!!!!")


'''
Created By:
Created Date:
Reviewd By:
Modified By:
Parameters:
return Type:
Purpose:
'''
def getCellData(FileName,SheetName,ColumnName,RowNum):
    colNum=0
    try:
        wb = xlrd.open_workbook(FileName)
        sheet = wb.sheet_by_name(SheetName)

        firstrow = sheet.row_values(0)
        for data in firstrow:

            if (data == ColumnName):
                break
            colNum += 1

        celldata = sheet.cell_value(RowNum, colNum)
        return celldata
    except Exception:
        print("Invalid File Name or Sheet Name !!!!!")



def loadTestDataInEnvironmentVariable(FileName,SheetName):
    try:
        wb = xlrd.open_workbook(FileName)
        sheet = wb.sheet_by_name(SheetName)

        columnnames=sheet.row_values(0)
        columnvalue=sheet.row_values(1)

        for i in range(len(columnnames)):
            os.environ[columnnames[i]]=str(columnvalue[i])
    except Exception:
        print("Invalid File Name or Sheet Name !!!!!")


#loadTestDataInEnvironmentVariable("E:/PYTHONPROJECTS/ActiTime-Automation/TestScriptDataFiles/Login.xlsx","testdata")


