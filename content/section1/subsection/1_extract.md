# 1. Extraction
<br>
<br>

<a href="https://colab.research.google.com/github/HP-Nunes/SMCapstone_GColab/blob/main/Notebook_1_extract.ipynb" target="_blank"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Google Colab, Extract"></a>


Lyft's Bay Wheels historical ridership dataset represents the bulk of the raw data. The data is stored within zipped csv files for each month of a given year, so I clicked and downloaded all the files within my date range of interest: i.e. January 2019 - August 2021.

I unzipped the files and saved each csv into a folder corresponding to the year the data was created (thus, I had three folders for 2019, 2020, and 2021). I then created a helper function to combine the monthly dataset into a single csv for each given year. 

You might think *why not just combine all of the yearly dataset into one csv file?* which is not an unreasonable thought. Wrangling data, in my experience, is an iterative process where incongruities in the raw dataset are uncovered throughout a series of trials and errors during the <b>Transformation</b> process. With these particular sets of data, I observed that their schema were not consistent between years (2019's data schema was changed due to rebranding). So dealing with each yearly set at once was less strenuous down the line. 

---
What could be improved:

*   Writing a batch script to download the csv files directly from Lyft's website;
    *   Issue: Lyft does not provide an API to call upon their historical dataset. Furthermore, due to the rebranding of Bay Wheels from Ford Go Bike in mid-2019, which is reflected in the filepath convention to the files, that added a layer of difficulty to work around with. 
*   Writing a batch script to unzip and store the zip files locally, without having to manually define the filepaths;
    *   Issue: I tried! But the zip files each contained a folder dedicated with a csv file formatted for MacOS, which I did not need to extract. Dealing with these issues cumulatively were starting to creep into the time I had dedicated for ETL; programmatic solutions here would have saved me 5-10 minutes at most.

---
### Data Sources

| [Lyft System Data](https://www.lyft.com/bikes/bay-wheels/system-data) | [DataSF](https://datasf.org/opendata/) |
|------------|-------------|
| <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a0/Lyft_logo.svg/199px-Lyft_logo.svg.png" width="250"> | <img src="http://www.azavea.com/wp-content/uploads/2015/04/DataSF.png" width="250"> |
| <ul><li><a href="https://s3.amazonaws.com/baywheels-data/index.html" target="_blank">Bay Wheels trip history data</a></li></ul> | <ul><li><a href="https://data.sfgov.org/Transportation/Bay-Area-Bikeshare-Stations/7jbp-yzp3" target="_blank">Bay Area Bikeshare Stations</a></li><li><a href="https://data.sfgov.org/Geographic-Locations-and-Boundaries/SF-Find-Neighborhoods/pty2-tcw4" target="_blank">SF Find Neighborhoods</a>
</li></ul> 
