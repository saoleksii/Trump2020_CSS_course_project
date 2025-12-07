# Reddit Users' Reaction to Major US Political Events in 2020-2021
<div align="center">
  <b>Volik Oleksii and Vashchenko Mykola</b>
  <br>
  Faculty of Informatics, National University of «Kyiv-Mohyla Academy»
  <br><br>
  Computational Social Science
  <br>
  Teacher: Andrew Kurochkin
  <br><br>
  November 30, 2025
  <br>
  Kyiv 
</div>

## Executive summary
<div> 
This study analyzed 6 million Reddit records during 2020 US major political events to map the political discourse across Liberal, Conservative, and Neutral subreddits. Key findings:
  
* The **Liberal community** showed high unity and consistently pushed the dominant narrative.
* The **Conservative community** was decentralized and displayed fragmentation, heavily discussing radical and conspiracy topics.
* The **Neutral community** was most engaged during extreme, unpredictable events (like the Capitol Attack) rather than standard political processes.
* Sentiment across all groups turned highly **negative** after the Capitol Attack, driven primarily by users criticizing their political opponents ("Attack words") more frequently than supporting their own side ("Support words").
* The attention to the Capitol Attack completely **took over all discussions.**
</div>

## Project structure

## Instructions to setup the project
### Installation
- To repeat the process from the beginning, you need firstly to download from [here](https://academictorrents.com/details/30dee5f0406da7a353aff6a8c) raw data (2020.10-2021.03) both comments and submission. **Do not forget to change our local paths to your local paths and check requirements section.**
- Open scripts folder and download all files. You will need to run them in VScode or any IDE sequentially.
1. combine_folder_multiprocess.py (extract only needed subreddits, you will get 18 files)
2. to_csv.py and parallel_converter.py (this will convert files to csv)
3. combine_csv.py (to merge all 18 files in one)
4. select_data.csv (clean the filtered csv file)
5. combine_files.py (merge 2 files into 1)
- All further work was done in colab
1. dataset_processing.ipynb
2. exploratory_data_analysis.ipynb
3. analytical_report.ipynb
## Requirements
For to_csv.py and single_file_converter.py you will need to install zsstandard (to handle .zst format)
```
$ pip install zstandard
```
Other requirements can be found in requirements.txt
## Link to initial dataset 
Our prepared dataset can be found on google [disk processed_political_dataset.csv](https://drive.google.com/file/d/10Kcf1_rJTibaJOAjBQb2PhPvht6zZoey/view?usp=share_link)
