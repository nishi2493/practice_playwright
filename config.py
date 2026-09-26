USERNAME = "ap.exec.a@ajantapharma.com"
PASSWORD = "AjantaUat@2026"

ENVIRONMENTS = {
    "uat": "https://uatapp.ajantaconnect.com/workbench/#/signIn",
    "dev": "YOUR_ACTUAL_DEV_URL"
}

def get_base_url(environment):
    return ENVIRONMENTS[environment]
