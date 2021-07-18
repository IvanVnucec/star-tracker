#!/bin/bash

parent_path=$( cd "$(dirname "${BASH_SOURCE[0]}")" ; pwd -P )
cd "$parent_path"

DATA_DIR='../data'

wget --no-clobber -P $DATA_DIR http://archive.eso.org/ASTROM/TYC-2/data/suppl_1.dat
wget --no-clobber -P $DATA_DIR http://archive.eso.org/ASTROM/TYC-2/data/suppl_2.dat
wget --no-clobber -P $DATA_DIR http://archive.eso.org/ASTROM/TYC-2/data/index.dat
wget --no-clobber -P $DATA_DIR http://archive.eso.org/ASTROM/TYC-2/data/catalog.dat
