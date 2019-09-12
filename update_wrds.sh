#!/usr/bin/env bash
printf "Updating Audit Analytics (audit) ...\n"
audit/update_audit.py
printf "\nUpdating CRSP (crsp) ...\n"
cd crsp
./update_crsp.py
printf "\nUpdating DealScan (dealscan) ...\n"
cd ..
dealscan/update_dealscan.py
printf "\nUpdating IBES (ibes) ...\n"
ibes/update_ibes.py
printf "\nUpdating RavenPack (rpna) ...\n"
rpna/update_rpna.py
printf "\nUpdating Thomson Reuters (tfn) ...\n"
tfn/update_tfn.py
wrdssec/update_wrdssec.py
