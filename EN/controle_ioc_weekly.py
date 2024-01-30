import csv
import os
import requests

def download_week_csv(url, destination):
    response = requests.get(url)
    if response.status_code == 200:
        with open(destination, 'wb') as file:
            file.write(response.content)
        print("Téléchargement de week.csv terminé.")
    else:
        print("Échec du téléchargement de week.csv.")

def extract_iocs_from_week_csv(week_csv_file):
    iocs = []
    with open(week_csv_file, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            if len(row) >= 4:
                ioc = row[3].strip()
                iocs.append((row, ioc))
    return iocs

def search_ioc_in_jira_soc(ioc, jira_soc_file):
    with open(jira_soc_file, 'r') as file:
        jira_soc_data = file.readlines()
        for line in jira_soc_data:
            if ioc in line:
                return True
    return False

if __name__ == "__main__":
    # URL du fichier week.csv
    week_csv_url = "https://github.com/0xDanielLopez/TweetFeed/raw/master/week.csv"
    week_csv_file = "week.csv"
    jira_soc_file = "jira_soc.csv"

    # Téléchargement de week.csv
    download_week_csv(week_csv_url, week_csv_file)

    # Extraction des IoCs de la colonne 4 dans week.csv
    iocs = extract_iocs_from_week_csv(week_csv_file)

    # Recherche des IoCs dans jira_soc.csv et affichage des lignes correspondantes dans week.csv
    iocs_not_found = True
    for row, ioc in iocs:
        if search_ioc_in_jira_soc(ioc, jira_soc_file):
            iocs_not_found = False
            print(','.join(row))

    if iocs_not_found:
        print("Aucun IoC trouvé entre week.csv et jira_soc.csv.")
