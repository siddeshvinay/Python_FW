from utility import ApplicationIndependent,Configuration
global ReportFileName,ReportDirectorypath,strScenarioName

ReportFileName=""
ReportDirectorypath=""
strScenarioName=""

testscriptid = []
description = []
methodname = []
teststatus = []
screenshotName = []
'''
Created By:
Created Date:
Reviewd By:
Modified By:
Parameters:
return Type:
Purpose:
'''
def createReport(FileName,teststarttime,environment):
    try:
        ReportFileName=FileName
        ReportDirectorypath = Configuration.ReportPath

        file=open(FileName,"w")
        file.write("<html>")
        file.write("<head><title>ActiTime Automation Results</title></head>")
        file.write("<body>")
        file.write("<h1 align=center>ActiTime Automation Results</h1>")
        file.write("<table border=2>")
        file.write("<h3>Automation Summary</h3>")
        file.write("<tr>")
        file.write("<th align=center>Item Name</th>")
        file.write("<th align=center>Item Value</th>")
        file.write("</tr>")
        file.write("<tr>")
        file.write("<td>Application Name</td>")
        file.write("<td>" + Configuration.applicationname + "</td>")
        file.write("</tr>")
        file.write("<tr>")
        file.write("<td>Application Version</td>")
        file.write("<td>" + Configuration.applicationversion + "</td>")
        file.write("</tr>")
        file.write("<tr>")
        file.write("<td>Browser Name</td>")
        file.write("<td>" + Configuration.browserName + "</td>")
        file.write("</tr>")
        file.write("<tr>")
        file.write("<td>Application URL</td>")
        file.write("<td>" + Configuration.url + "</td>")
        file.write("</tr>")
        file.write("<tr>")
        file.write("<td>Environment</td>")
        file.write("<td>" + environment + "</td>")
        file.write("</tr>")
        file.write("<tr>")
        file.write("<td>Automation Start Time</td>")
        file.write("<td>" + teststarttime + "</td>")
        file.write("</tr>")
        file.write("<tr>")
        file.write("<td>Automation End Time</td>")
        file.write("<td>END_TIME</td>")
        file.write("</tr>")
        file.write("</table>")
        file.write("</body>")
        file.write("</html>")
        file.close()
    except Exception as e:
        ApplicationIndependent.writeLog("There is an error raised during the execution of the Method createReport,Exception :" + e, "error")


'''
Created By:
Created Date:
Reviewd By:
Modified By:
Parameters:
return Type:
Purpose:
'''
def startSuite(ScenarioName,ReportFileName):

    try:
        strScenarioName=str(ScenarioName).replace(" ","_")
        file = open(ReportFileName, "a")
        file.write("<html>")
        file.write("<body>")
        file.write("<table width=100% border=2>")
        file.write("<h2>Automation Execution Details</h2>")
        file.write("<tr>")
        file.write("<th align=center width=15%>Testcase ID</th>")
        file.write("<th align=center width=20%>Testcase Name</th>")
        file.write("<th align=center width=15%>Status</th>")
        file.write("<th align=center width=25%>Test Start Time</th>")
        file.write("<th align=center width=25%>Test End Time</th>")
        file.write("</tr>")
        file.close()
    except Exception as e:
        ApplicationIndependent.writeLog("There is an error raised during the execution of the Method startSuite,Exception :" + e, "error")


'''
Created By:
Created Date:
Reviewd By:
Modified By:
Parameters:
return Type:
Purpose:
'''
def endSuite(ReportFileName):
    try:
        file = open(ReportFileName, "a")
        file.write("</table>")
        file.close()
    except Exception as e:
        ApplicationIndependent.writeLog("There is an error raised during the execution of the Method endSuite,Exception :" + e, "error")


'''
Created By:
Created Date:
Reviewd By:
Modified By:
Parameters:
return Type:
Purpose:
'''
def addArrayList(scriptid,desc,methodname1,Status,screenshot):
    testscriptid.append(scriptid)
    description.append(desc)
    methodname.append(methodname1)
    teststatus.append(Status)
    screenshotName.append(screenshot)



'''
Created By:
Created Date:
Reviewd By:
Modified By:
Parameters:
return Type:
Purpose:
'''
def writeDeatilTestResults(testscenarioname,listtestscriptid,listtsdescription,methods,listStatus,listScreenShot):
    try:
        ReportDirectorypath = Configuration.ReportPath
        FileName = ReportDirectorypath +"Scenario" + "_" + testscenarioname + "_Results.html";
        #print(FileName)
        file = open(FileName, "w")

        file.write("<html>")
        file.write("<head><title>" + testscenarioname + " Detail Results</title></head>")
        file.write("<body>")
        file.write("<h1 align=center>" + testscenarioname + " Detail Results</h1>")
        file.write("<table border=1 width=100%>")
        file.write("<h2 align=left>" + testscenarioname + " Detail Results</h2>")
        file.write("<tr>")
        file.write("<th width=15%>TestScriptID</th>")
        file.write("<th width=20%>Description</th>")
        file.write("<th width=25%>TestScriptName</th>")
        file.write("<th width=15%>Status</th>")
        file.write("<th width=25%>ScreenShotName</th>")
        file.write("</tr>")
        for i in range(len(methods)):
            file.write("<tr>")
            file.write("<td width=10%>" + listtestscriptid[i] + "</td>")
            file.write("<td width=20%>" + listtsdescription[i] + "</td>")
            file.write("<td width=15%>" + methods[i] + "</td>")
            if (str(listStatus[i]).lower() == "pass"):
                file.write("<td width=10%>" + listStatus[i] + "</td>")
                file.write("<td width=25%>&nbsp</td>")
            else:
                file.write("<td width=10%>" + listStatus[i] + "</td>")
                file.write("<td width=25%><a href=file:///" + listScreenShot[i] + ".jpg" + ">ScreenShotName</a></td>")
            file.write("</tr>")

        file.write("</table>")
        file.write("</body>")
        file.write("</html>")
        file.close()

    except Exception as e:
        ApplicationIndependent.writeLog("There is an error raised during the execution of the Method writeDeatilTestResults,Exception :" + e, "error")
    return FileName



'''
Created By:
Created Date:
Reviewd By:
Modified By:
Parameters:
return Type:
Purpose:
'''
def writeSummaryTestResults(mainReportFileName,detailFileName,testcaseid,testname,status,starttime,endtime):
    try:
        file = open(mainReportFileName, "a")
        file.write("<tr>")
        file.write("<td width=15% align=center>" + testcaseid + "</td>")
        file.write("<td width=20% align=center>" + testname + "</td>")
        file.write("<td width=15% align=center><a href=file:///" + detailFileName + ">" + status + "</a></td>")
        file.write("<td width=25% align=center>" + starttime + "</td>")
        file.write("<td width=25% align=center>" + endtime + "</td>")
        file.write("</tr>")
    except Exception as e1:
        ApplicationIndependent.writeLog("There is an error raised during the execution of the Method writeTestResults,Exception :" + e1, "error")


'''
FileName="E:/SIDE/ResultReport.html"
createReport(FileName,"","")
'''