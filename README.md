# Netflix movie CSV exploration using python modules and EDA methods

## Introduction
This movie dataset contains following informations about 8807 Netflix productions:
+ type
+ title
+ country
+ release year
+ *rating : ['NR' < 'G' < 'PG' < 'PG-13' < 'R']
+ duration
+ cast_count
+ estimated budget in USD
Main goal is to find something interesting about this dataset.
In this work I use following python modules: pandas, matplotlib.pyplot, seaborn anid scipy.stats

* ***Rating column is not about productions quality***. It tells us what audience age is directed to.
  + NR - no restrictions
  + G  - general audience
  + PG - parental guidance
  + PG-13 - not appropriate for children under 13
  + R  - restricted, children under 17 require accompanying parent or adult guardian

## EDA


