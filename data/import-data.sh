#!/usr/bin/env bash

DATADIR=$(echo 'select @@datadir;' | mysql | tail -n 1)
cp -v search_vehicle.tsv "${DATADIR}"
mysqlimport \
    -c make,model,body,flag,year,MSRP,details,image \
    --fields-terminated-by="\t" \
    search \
    search_vehicle.tsv
