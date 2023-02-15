# Gene2UniProtID
Convert gene symbol to UniProt ID and Protein Name, including isoforms.

You will need to download the excel file from UniProt (UniProtKB Reviewed, Human Proteins) onto your local machine for this function. 

*https://www.uniprot.org/uniprotkb?facets=reviewed%3Atrue%2Cmodel_organism%3A9606&query=%2A*

Please follow the link above to download. Select ‘Download All’, ‘Excel’ format and choose ‘Entry Name’, ‘Protein Name’, and ‘Gene Name’ from the ‘Customize Columns’ section. Download this file onto you local machine.

You will also need separate .csv files for up- and down-regulated genes you wish to assign Uniprot IDs and Protein Names to.

Make sure you are using the latest version of Python 3.

Run the Gene2UniProtID.py file in the command line by navigating to the directory the .py file is in and typing ‘python3 Gene2UniProtID.py’ into the command line.

Follow the command line prompts to choose your up- and down-regulated .csv files. 

Name your experiment: this will later become the folder in which the final .csv file will be exported.

Name the control and case for your experiment: this will later become the name of the .csv file. Today’s date will also be attached to the file.

At the end, you will have the opportunity to check for isoforms if all genes are not mapped to UniProtIDs.

Navigate to your preferred parent directory: a new folder will be made there, and the resultant .csv file will be in that folder.
