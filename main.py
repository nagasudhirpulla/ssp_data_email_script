from src.config.appConfig import loadAppConfig, loadPoints
from src.services.scadaFetcher import fetchScadaPntRtData
from src.services.emailSender import EmailSender
import datetime as dt
import jinja2


def main():
    print("loading config and points info")
    appConf: dict = loadAppConfig()
    points: dict = loadPoints()

    print("fetching points data")
    pntsData = {}
    pntsData["timestampStr"] = dt.datetime.now().strftime("%d-%b-%Y %H:%M")
    for pntKey in points:
        rtPntVal = fetchScadaPntRtData(pntId=points[pntKey])
        pntsData[pntKey] = rtPntVal
    # print(pntsData)

    print("populating template")
    template = jinja2.Environment(
        loader=jinja2.FileSystemLoader("./templates")
    ).get_template("msg_template.html")
    msgTxt = template.render({"data": pntsData})
    # print(msgTxt)

    print("sending email")
    receiverEmails = appConf["receiverEmails"]
    emailApi = EmailSender()
    emailApi.sendEmail(receiverEmails,
                       f"SSP Data {pntsData["timestampStr"]}", msgTxt)


if __name__ == "__main__":
    main()
