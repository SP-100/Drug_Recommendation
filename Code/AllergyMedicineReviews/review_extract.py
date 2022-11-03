from functions import review_scrape

# Scraping ORAL antihistamines and decongestants
for i in range(10):
    try:
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
    finally:
        break


import pandas as pd
import os

master_df = pd.DataFrame()

for file in os.listdir(os.getcwd()):
    if file.endswith('.csv'):
        master_df = master_df.concat(pd.read_csv(file))

master_df.to_csv('Allergy medicine reviews.csv', index=False)

# # ANTIHISTAMINES

# # oral
# cetrizine = "https://www.webmd.com/drugs/drugreview-12065-cetirizine-oral?conditionid=&sortval=1&page="
# zyrtec = "https://www.webmd.com/drugs/drugreview-12127-zyrtec-oral?conditionid=&sortval=1&page="
# levocetirizine = "https://www.webmd.com/drugs/drugreview-148989-levocetirizine-oral?conditionid=&sortval=1&page="
# xyzal = "https://www.webmd.com/drugs/drugreview-148996-xyzal-oral?conditionid=&sortval=1&page="
# fexofenadine = "https://www.webmd.com/drugs/drugreview-13823-fexofenadine-oral?conditionid=&sortval=1&page="
# diphenhydramine = "https://www.webmd.com/drugs/drugreview-1428-diphenhydramine-oral?conditionid=&sortval=1&page="
# benadryl = "https://www.webmd.com/drugs/drugreview-5680-benadryl-oral?conditionid=&sortval=1&page="
# clarinex = "https://www.webmd.com/drugs/drugreview-22326-clarinex-oral?conditionid=&sortval=1&page="


# # DECONGESTANTS

# # oral
# zyrtec-D = "https://www.webmd.com/drugs/drugreview-21779-zyrtec-d-oral?conditionid=&sortval=1&page="
# fexofenadine = "https://www.webmd.com/drugs/drugreview-13823-fexofenadine-oral?conditionid=&sortval=1&page="
# loratadine = "https://www.webmd.com/drugs/drugreview-73-loratadine-oral?conditionid=&sortval=1&page="
# semprex-d = "https://www.webmd.com/drugs/drugreview-410-semprex-d-oral?conditionid=&sortval=1&page="
