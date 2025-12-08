<h1 align="center"> Reddit Users' Reaction to Major US Political Events in 2020-2021 </h1>
<div align="center">
  <b>Volik Oleksii and Vashchenko Mykola</b>
  <br>
  Faculty of Informatics, National University of «Kyiv-Mohyla Academy»
  <br><br>
  Computational Social Science
  <br>
  Teacher: Andrew Kurochkin
  <br><br>
  2025
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
| No |  Name | Details 
|----|------------|-------|
| 1  | scritps folder | Contains all scripts for filtering the dataset
| 2  | notebooks folder | Main steps including cleaning dataset, analysis and report
| 3  | google disk | All csv files (dataset versions) and vizualization folder
| 4  | requirements.txt | Contains versions for notebooks


## Instructions to setup the project
### Installation
- To repeat the process from the beginning, you need firstly to download from [here](https://academictorrents.com/details/30dee5f0406da7a353aff6a8c) raw data (2020.10-2021.03) both comments and submission. **Do not forget to change our local paths to your local paths and check requirements section.**
- Open scripts folder and download all files. You will need to run them in VScode or any IDE sequentially.
1. **combine_folder_multiprocess.py** (extract only needed subreddits, you will get 18 files)
2. **to_csv.py** and parallel_converter.py (this will convert files to csv)
3. **combine_csv.py** (to merge all 18 files in one)
4. **select_data.py** (clean the filtered csv file)
5. **combine_files.py** (merge 2 files into 1)
- All further work was done in colab (except final report)
1. **dataset_processing.ipynb**
2. **exploratory_data_analysis.ipynb**
3. **final_report.pdf**
### How to open and use notebooks on your device
1. Copy link to  repository (https://github.com/saoleksii/reddit_political_behaviour)
2. Open [Google Colab welcome page](https://colab.research.google.com/)
3. In the pop-up window select GitHub
4. Paste the copied link into the input field above
5. Open the notebooks that will appear in a new tab
6. In each of opened notebooks, click **File - Save a copy to Disk** (so you can run the code yourself)
## Requirements
- For to_csv.py and single_file_converter.py you will need to install **zsstandard** (to handle .zst format)
```
$ pip install zstandard
```
- Other **requirements** can be found in requirements.txt

- **Figures** that are needed for eda are in [viz folder](https://drive.google.com/drive/folders/17n695fXgHJ4Rjn_pyuABSdn0hI6gX7PO?usp=share_link) on google disk.

- All **csv files** used in notebooks are on [google disk](https://drive.google.com/drive/folders/1Z82Rf8wvCk6QPcBqU2IR7wlUCQ9tHtjY?usp=sharing), just create folder copy and use your file path instead of default 
## Link to initial dataset 
Our prepared dataset can be found on google disk [processed_political_dataset.csv](https://drive.google.com/file/d/10Kcf1_rJTibaJOAjBQb2PhPvht6zZoey/view?usp=share_link)
