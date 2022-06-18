# Data type

In this bucket `s3://sipecam-open-data` there are 3 types of data: 
- images (`.jpg`)
- videos (`.mp4`)
- audio (`.avi`)

# Structure

The easy access data can be found under the path `s3://sipecam-open-data/data/`. 

The structure folder is the following:

```
sipecam-open-data 
├── data/
│   ├── <cumulus number>/
│   ├── <node>_<cumulus number>_<random numbers>/
│   ├── <device name>/
│   ├── <extraction date (YYYY-MM-DD)>/
│   └── <TYPE OF DATA>/    (images_videos, audio)
│       ├── *.JPG
│       ├── *.AVI
│       └── *.mp4
└── alf_data/   (This use is for Afresco)
```
