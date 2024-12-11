from langchain_core.tools import tool
import random


class ToolList:

    @tool
    def getBPProcessStatus(processName: str, periodHrs: int) -> str:
        """get status of Blue Prism processName in the last periodHrs"""
        timeOfRun = random.randint(1, 24)
        status = ["successfully", "with error"]
        statusOfRun = random.choice(status)

        return " " +processName + " has completed " + statusOfRun + " at " + str(timeOfRun) + ":00 on resource RR1 "



    @tool
    def resubmitProcess(processName: str, resourceName: str) -> str:
        """creates a session of processName on runtime resource  resourceName"""
        status = ["successfully", "with error"]
        statusOfRun = random.choice(status)
        return " " + processName + " run " + statusOfRun + " on resource " + resourceName + " "

    @tool
    def sendEmailIT(text: str) -> str:
        """send email to IT team with steps taken"""

        return " Successfully sent email to IT team with text : " + text


    tools = [getBPProcessStatus, resubmitProcess, sendEmailIT]
