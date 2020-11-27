# python 3
# 79: -------------------------------------------------------------------------
#
# Process datasets: Merge datasets and recode categorical features
#
# Author(s): Yanhan Si
# Updated: Nov 26, 2020
# 79: -------------------------------------------------------------------------

import pandas as pd
import numpy as np
import os

# List of file names to merge
xpt_files = ["DEMO.XPT", "TELO_A.XPT", "BMX.XPT"]

def get_data(year):
    """
    Return the merged data for a given year.

    The NHANES data files must first be downloaded into the directory
    data
    """
    base = "data"

    if year == 1999:
        xpt_files_use = xpt_files
    else:
        raise ValueError("Please provide the files names!")

    # Retain these variables.
    vars = [
        ["SEQN", "RIAGENDR", "RIDAGEYR", "RIDRETH1"],
        ["SEQN" , "TELOMEAN", "TELOSTD"],
        ["SEQN", "BMXWT", "BMXHT", "BMXBMI", "BMXLEG", "BMXARMC"],
    ]

    # Load each individual file and keep only the variables of interest
    da = []
    for idf, fn in enumerate(xpt_files_use):
        df = pd.read_sas(os.path.join(base, fn))
        df = df.loc[:, vars[idf]]
        da.append(df)

    # SEQN is a common subject ID that can be used to merge the files.
    # These are cross sectional (wide form) files, so there is at most
    # one row per subject.  Subjects may be missing from a file if they
    # did not participate in those assessments.  All subjects should be
    # present in the demog file.
    dx = pd.merge(da[0], da[1], left_on="SEQN", right_on="SEQN")
    dx = pd.merge(dx, da[2], left_on="SEQN", right_on="SEQN")

    # Recode sex as an indicator for female sex
    dx["Female"] = (dx.RIAGENDR == 2).astype(np.int)

    # Recode the ethnic groups
    dx["RIDRETH1"] = dx.RIDRETH1.replace({1: "MA", 2: "OH", 3: "NHW", 4: "NHB", 5: "OR"})

    # Drop rows with any missing data in the variables of interest
    dx = dx.dropna()

    return dx
