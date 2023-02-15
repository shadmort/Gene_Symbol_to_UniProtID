#!/usr/bin/env python
# coding: utf-8

# ## Map Gene Symbol to Protein Name with Isoforms

# In[1]:


import pandas as pd
from tkinter import filedialog
import os
import numpy as np

import warnings
warnings.filterwarnings("ignore")

# input csv
print('Open UniProt ID Excel File')
UniProtraw = filedialog.askopenfilename()
print('Open Up-regulated Genes')
Upraw = filedialog.askopenfilename()
print('Open Down-regulated Genes')
Downraw = filedialog.askopenfilename()

# read files
UniProt = pd.read_excel(UniProtraw)
Up = pd.read_csv(Upraw)
Down = pd.read_csv(Downraw)

# rename Gene column and remove white space
UniProt.rename(columns={'Gene Names': 'Gene.Names', 'Entry': 'UniProt.ID', 'Protein names': 'Protein.Names'},
               inplace=True)
UniProt['Gene.Names'] = UniProt['Gene.Names'].str.split(' ').str[0]

# rename columns for merge
Up['Gene.Names'] = Up['symbol']
Down['Gene.Names'] = Down['symbol']

# merge
Up_1 = pd.merge(UniProt, Up, on = 'Gene.Names', how = 'right')
Down_1 = pd.merge(UniProt, Down, on = 'Gene.Names', how = 'right')

# concatenate
RegulatedProteins = pd.concat([Up_1, Down_1])

# clean
RegulatedProteins.drop(['symbol', 'adj.P.Val'], axis=1, inplace=True)
RegulatedProteins.rename(columns={'FC': 'Fold.Change', 'logFC': 'log.Fold.Change'}, inplace=True)
RegulatedProteins = RegulatedProteins.round(1)

# naming
Experiment = input('\nEnter Experiment Name: ')
Case = input('Enter Case: ')
Control = input('Enter Control: ')
Date = pd.to_datetime('today').date()

# find unmapped Genes
print('\n' + str(RegulatedProteins['Protein.Names'].isna().sum()) + ' IDs were not mapped')
RegulatedProteins.replace(np.NaN, 'NaN', inplace=True)
for i in range(RegulatedProteins.shape[0]):
    if RegulatedProteins['Protein.Names'].iloc[i] == 'NaN':
        print(RegulatedProteins['Gene.Names'].iloc[i])
    else:
        pass
                 
# dealing with protein isoforms
RegulatedProteins.replace('NaN', np.NaN, inplace=True)
if RegulatedProteins['Protein.Names'].isna().sum() > 0:
    goforiso = input('\nFind protein isoforms? \nEnter: y or n \n')
    if goforiso == 'y':               
        RegulatedProteins.replace(np.NaN, 'NaN', inplace=True)
        for i in range(RegulatedProteins.shape[0]):
            if RegulatedProteins['UniProt.ID'].iloc[i] == 'NaN':
                RegulatedProteins['UniProt.ID'].iloc[i] = RegulatedProteins['Gene.Names'].iloc[i][:-2]
        RegulatedProteinIsoforms = pd.merge(UniProt, RegulatedProteins,  on = 'UniProt.ID', how = 'right')
        RegulatedProteinIsoforms.drop(['Gene.Names_x', 'Protein.Names_y'], axis = 1, inplace=True)
        RegulatedProteinIsoforms.rename(columns={'Protein.Names_x': 'Protein.Names', 'Gene.Names_y': 'Gene.Names'},
                                    inplace=True)
        # find unmapped Genes
        print('\n' + str(RegulatedProteinIsoforms['Protein.Names'].isna().sum()) + ' IDs were not mapped')
        RegulatedProteinIsoforms.replace(np.NaN, 'NaN', inplace=True)
        for i in range(RegulatedProteinIsoforms.shape[0]):
            if RegulatedProteinIsoforms['Protein.Names'].iloc[i] == 'NaN':
                RegulatedProteinIsoforms['UniProt.ID'].iloc[i] = 'NaN'
                print(RegulatedProteinIsoforms['Gene.Names'].iloc[i])
            else:
                pass
        # option to export
        export2 = input('\nExport this file as .csv? \nEnter: y or n \n')
        if export2 == 'y':
            directory = Experiment
            print('Choose Parent Directory')
            parent_dir = filedialog.askdirectory()
            path = os.path.join(parent_dir, directory)
            os.mkdir(path)
            RegulatedProteinIsoforms.to_csv(f'{path}/{Case}_{Control}_RegulatedProteins_{Date}.csv')
        else:
            pass    
    else:
        # option to export
        export = input('Export this file as .csv? \nEnter: y or n \n')
        if export == 'y':
            directory = Experiment
            print('Choose Parent Directory')
            parent_dir = filedialog.askdirectory()
            path = os.path.join(parent_dir, directory)
            os.mkdir(path)
            RegulatedProteins.to_csv(f'{path}/{Case}_{Control}_RegulatedProteins_{Date}.csv')


else:
    # option to export
    export = input('Export this file as .csv? \nEnter: y or n \n')
    if export == 'y':
        directory = Experiment
        print('Choose Parent Directory')
        parent_dir = filedia
        log.askdirectory()
        path = os.path.join(parent_dir, directory)
        os.mkdir(path)
        RegulatedProteins.to_csv(f'{path}/{Case}_{Control}_RegulatedProteins_{Date}.csv')


# ### PromTArt5 is 'Promega trypsin artifact 5 K to R mods'

# In[2]:


RegulatedProteinIsoforms


# In[ ]:




