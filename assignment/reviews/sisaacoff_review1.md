## Peer Review 1

### Strengths of their project 

1. You did a very good job getting and cleaning this dataset. You took the effort to parse the datset that stored in folders and subfolders and explore external tools from github to reads the .h5 files into a dataframe. 

2. You also did a very well exploring the dataset with various techiniques such as qqplot, histgrams and linear regression.

### Comments about things you think could be improved
1. I realized that in the case that the year is 0, the title of the song actually contains some information abut the year. For example, 'Christina The Astonishing (2010 Digital Remaster)' has `year = 0`, but I think use 2010 as year might be better than treated as `NA`.


### Questions about things you don't understand

### Comments about their code
1. I don't know if you realized that whenever you use matplotlib to plot year against some metrics, the year axes actually showd as integers instead of years. For example, 
```python
    fig, axes = plt.subplots(nrows=3,ncols=2)  
    axes[0,0].plot(year_gb.Loudness.mean()) 
    axes[0,0].set_ylabel("Loudness")
```
  The x axis was showed as integers rather than years and dates. I found out the issue related to this: http://stackoverflow.com/questions/26526230/plotting-datetimeindex-on-x-axis-with-matplotlib-creates-wrong-ticks-in-pandas-0 


### Suggestions for next steps
1. One suggestion is that you could probably use pd.to_tsv to export the cleaned dataset, so you can continue to bulid on analysis . Also it might be good to upload this clean dataset to your github so if other people are interested they can also work on it.
2. Maybe you can have another notebook with summary and key takeways from this one so you can use it for sharing and presenting.

