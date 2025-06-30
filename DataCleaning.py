import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def csv_conversion(data):
    dataframe = pd.read_csv(data, encoding="ISO-8859-1")
    return dataframe

def csv_description(dataset, commentary=None):
    if dataset == "municipal-building-energy-use-2009-2014.csv":
        link = "https://catalog.data.gov/dataset/municipal-building-energy-usage"
        message = "\nThis data set contains energy use data from 2009-2014 for 139 municipally operated buildings. Metrics include: Site & Source EUI, annual electricity, natural gas and district steam consumption, greenhouse gas emissions and energy cost. Weather-normalized data enable building performance comparisons over time, despite unusual weather events."
        note = "NOTE: has per year energy estimates of the same locations"
        location = ("Location: Allegheny County / City of Pittsburgh")
    elif dataset == "DCAS_Managed_Building_Energy_Usage.csv":
        link = "https://catalog.data.gov/dataset/dcas-managed-building-energy-usage"
        message = "\nCity Building Energy Usage Data."
        note = "NOTE: Could be useful, data dictionary claims that the spreadsheet is annually updated"
        location = ("Location: City of New York/ New York")
    elif dataset == "Energy_Usage_From_DOE_Buildings.csv":
        link = "https://catalog.data.gov/dataset/energy-usage-from-doe-buildings"
        message = "\nEnergy data from a select portfolio of City-Owned buildings (DOE)"
        note = "NOTE: Useful for per month building total predictions!"
        location = ("Location: City of New York/ New York")
    elif dataset == "Municipal_Building_Energy_Use_and_Energy_Star_Score.csv":
        link = "https://catalog.data.gov/dataset/municipal-building-energy-use-and-energy-star-score"
        message = "\nEnergy data on Providence Municipal buildings by year"
        note = ("NOTE: Useful for per year building total predictions!")
        location = ("Location: City of Providence/Rhode Island")
    elif dataset == "Energy_Usage_2010.csv":
        link = "https://catalog.data.gov/dataset/energy-usage-2010"
        message = "\nDisplays several units of energy consumption for households, businesses, and industries in the City of Chicago during 2010. Electric The data was aggregated from ComEd and Peoples Natural Gas by Accenture. Electrical and gas usage data comprises 88 percent of Chicago's buildings in 2010. The electricity data comprises 68 percent of overall electrical usage in the city while gas data comprises 81 percent of all gas consumption in Chicago for 2010. Census blocks with less than 4 accounts is displayed at the Community Area without further geographic identifiers. This dataset also contains selected variables describing selected characteristics of the Census block population, physical housing, and occupancy."
        note = ("")
        location = ("Location: City of Chicago/ Illinois")
    elif dataset == "F6a29a0f-cc32-4fd4-8adb-d45e11e09022.csv":
        link = "https://catalog.data.gov/dataset/allegheny-county-municipal-building-energy-and-water-use"
        message = "\nThis dataset contains energy and water use information from 2010 to the previous full month for County-operated buildings. Metrics include: kBtu (thousand British thermal units), site and source EUI (energy use intensity), annual electricity, natural gas and steam consumption and cost, and water and sewer use and cost. Weather-normalized data enable building performance comparisons over time, despite unusual weather events."
        note = ("")
        location = ("Location: Allegheny County / City of Pittsburgh")
    print(dataset + location + ". " + message + "\n" + note)
    return link