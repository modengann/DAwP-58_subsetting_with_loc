#!/usr/bin/env python3

import pandas as pd

def subsetting_with_loc(data):
    pass

def main():
    df = pd.read_csv('src/municipal.tsv', sep='\t', index_col=0)
    subsetting_with_loc(df)

if __name__ == "__main__":
    main()
