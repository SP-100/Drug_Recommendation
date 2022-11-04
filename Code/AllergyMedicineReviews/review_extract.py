from functions import review_scrape

# Scraping ORAL antihistamines and decongestants
for i in range(10):
    try:
        # antihistamine & decongestants for allergies
        review_scrape(12065, 'cetrizine', 1, 5)
        review_scrape(12127, 'zyrtec', 1, 19)
        review_scrape(148989, 'levocetirizine', 1, 4)
        review_scrape(148996, 'xyzal', 1, 20)
        review_scrape(13823, 'fexofenadine', 1, 5)
        review_scrape(1428, 'diphenhydramine', 1, 10)
        review_scrape(5680, 'benadryl', 1, 10)
        review_scrape(21779, 'zyrtec-d', 1, 4)
        review_scrape(13823, 'fexofenadine', 1, 5)
        review_scrape(73, 'loratadine', 1, 6)
        # NSAIDs for backache
        review_scrape(5166, 'ibuprofen', 1, 14)
        review_scrape(5173, 'naproxen', 1, 37)
        review_scrape(1098, 'aleve', 1, 10)
        review_scrape(362, 'acetaminophen', 1, 7)
        review_scrape(7076, 'tylenol', 1, 4)
        # Antiviral Medications for cold sore
        review_scrape(941, 'acyclovir', 1, 19)
        review_scrape(6279, 'valacyclovir', 1, 9)
        review_scrape(6157, 'famciclovir', 1, 4)
    finally:
        break


# Merging all csv files into one
import pandas as pd
import os
os.getcwd()

# Change cwd to the reviews folder
# path = r"C:\Users\ShrawanPun\Drug Recommendation Project\Code\AllergyMedicineReviews"
# os.chdir(path)

master_df = pd.DataFrame()

for file in os.listdir(os.getcwd()):
    if file.endswith('.csv'):
        master_df = pd.concat([pd.read_csv(file)])

master_df.to_csv('MedicineReviews.csv', index=False)

