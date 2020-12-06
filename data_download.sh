#!/usr/bin/env zsh

# 79: -------------------------------------------------------------------------
#
# To download the required datasets using: `zsh ./data_download.sh`
#
# Author(s): Yanhan Si
# Created: Nov 26, 2020
# Updated: Nov 27, 2020
# 79: -------------------------------------------------------------------------

wget https://wwwn.cdc.gov/Nchs/Nhanes/1999-2000/TELO_A.XPT -P data
wget https://wwwn.cdc.gov/Nchs/Nhanes/1999-2000/DEMO.XPT -P data
wget https://wwwn.cdc.gov/Nchs/Nhanes/1999-2000/BMX.XPT -P data
wget https://wwwn.cdc.gov/Nchs/Nhanes/2001-2002/TELO_B.XPT -P data
