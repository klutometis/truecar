#!/usr/bin/env bash

DATADIR=$(echo 'select @@datadir;' | mysql | tail -n 1)

echo 'truncate search_vehicle' | mysql -v search

cp -v search_vehicle.tsv "${DATADIR}/search"
mysqlimport \
    -c make,model,body,flag,year,MSRP,details,image \
    --fields-terminated-by="\t" \
    search \
    search_vehicle.tsv
