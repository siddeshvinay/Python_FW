from actitimetests import Initialize,LoginLogout,Users
from selenium import webdriver
from utility import ApplicationIndependent,Configuration,ReportUtil
from datatableutil import Datatable
import os
import unittest
class DriverScript(unittest.TestCase):
    global testdata,oBrowser,ReportFileName
    ReportFileName = Configuration.ReportPath + "AutomationTestResultReport.html"
    def setUp(self):
        try:
            teststarttime = ApplicationIndependent.getDateTime();
            ReportUtil.createReport(ReportFileName, teststarttime, "QA Testing");
        except Exception as e:
            ApplicationIndependent.writeLog("There is an error raised during the execution of the Method setUp,Exception :" + e, "error")


    def testRunner(self):
        startTime=ApplicationIndependent.getDateTime()
        ReportUtil.startSuite("Scenario",ReportFileName)
        ControllerFileName="E:/PYTHON/Browser Drivers/Final_Automation_FW/Controller/data_Controller.xlsx"
        rc=Datatable.getRowCount(ControllerFileName,"Scenarios")
        print("# of tests in data_Controller.xlsx File ....",rc)
        for r in range(rc):
            testcaseid=Datatable.getCellData(ControllerFileName,"Scenarios","TestcaseID",r)
            testcasename=Datatable.getCellData(ControllerFileName,"Scenarios","TestcaseName",r)
            testdesc = Datatable.getCellData(ControllerFileName, "Scenarios", "Description", r)
            runStatus = Datatable.getCellData(ControllerFileName, "Scenarios", "RunStatus", r)

            print("testcaseid  :"+testcaseid)
            print("testcasename  :" + testcasename)
            print("testdesc  :" + testdesc)
            print("runStatus  :"+runStatus)
            if (runStatus.lower()=='yes'):
                testfilename=testcasename+".xlsx"
             #  print(testfilename)
                testscenarioFile="E:/PYTHON/Browser Drivers/Final_Automation_FW/TestScriptDataFiles/"+testfilename
                print(testscenarioFile)
                scenariorowcount=Datatable.getRowCount(testscenarioFile,testcaseid)

                methods = []
                listtestscriptid=[]
                listtsdescription =[]
                liststatus=[]
                listscreenshot=[]
                for tsid in range(scenariorowcount-1):
                    testscriptid=Datatable.getCellData(testscenarioFile,testcaseid,"TestScriptID",tsid+1)
                    tsdescription = Datatable.getCellData(testscenarioFile, testcaseid, "Description", tsid+1)
                    tsmethodname = Datatable.getCellData(testscenarioFile, testcaseid, "MethodName", tsid+1)

                    print("testscriptid  :" + testscriptid)
                    print("tsdescription  :" + tsdescription)
                    print("tsmethodname  :" + tsmethodname)

                    listtestscriptid.append(testscriptid)
                    listtsdescription.append(tsdescription)
                    methods.append(tsmethodname)

                Datatable.loadTestDataInEnvironmentVariable(testscenarioFile,"testdata")
                print(methods)

                for method in methods:
                    resultStatus =eval(method)
                    liststatus.append(resultStatus)
                    if (resultStatus=="Fail"):
                        ScreenshorPath=Configuration.ScreenshotPath+""
                        ScreenshorName = ScreenshorPath + "ScreenShot_" + testcasename + "_" + testscriptid + "_" + method + ".jpg";
                        listscreenshot.append(ScreenshorName)
                        ApplicationIndependent.captureScreenShot(ScreenshorName)
                    else:
                        listscreenshot.append("")
                    ApplicationIndependent.writeLog("The Execution status of method " + method + " from Scenario  " + testcasename + " :" + str(
                            resultStatus), "info");

                endTime = ApplicationIndependent.getDateTime()
                detailResultFileName=ReportUtil.writeDeatilTestResults(testcasename,listtestscriptid,listtsdescription,methods,liststatus,listscreenshot)
                print(detailResultFileName)
                if 'Fail' in liststatus:
                    ReportUtil.writeSummaryTestResults(ReportFileName,detailResultFileName,testcaseid,testcasename,"Failed",startTime,endTime)
                else:
                    ReportUtil.writeSummaryTestResults(ReportFileName, detailResultFileName, testcaseid, testcasename,"Passed", startTime, endTime)
                ApplicationIndependent.writeLog("+++++++++++++++++++++++++++++++++++++","info")


    def tearDown(self):
        try:
            # Clear all Environment Variables
            os.environ.clear()
            ReportUtil.endSuite(ReportFileName)
        except Exception as e:
            ApplicationIndependent.writeLog("There is an error raised during the execution of the Method tearDown,Exception :" + e, "error")




if __name__=='__main__':
    unittest.main()