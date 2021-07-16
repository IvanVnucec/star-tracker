#!/bin/bash

parent_path=$( cd "$(dirname "${BASH_SOURCE[0]}")" ; pwd -P )
cd "$parent_path"

DATA_DIR='../data'

wget -P $DATA_DIR http://archive.eso.org/ASTROM/TYC-2/data/catalog.dat
wget -P $DATA_DIR http://archive.eso.org/ASTROM/TYC-2/data/index.dat
wget -P $DATA_DIR http://archive.eso.org/ASTROM/TYC-2/data/suppl_1.dat
wget -P $DATA_DIR http://archive.eso.org/ASTROM/TYC-2/data/suppl_2.dat
