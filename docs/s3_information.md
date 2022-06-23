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
│   ├── <cumulusr>/
│   ├── <node nomenclature>/
│   ├── <serial number device>/
│   ├── <extraction date (YYYY-MM-DD)>/
│   └── <TYPE OF DATA>/    (images_videos, audio) - Audio can be Ultrasonic or Audible
│       ├── *.JPG
│       ├── *.AVI
│       └── *.mp4
└── alf_data/   (This use is for Afresco)
```
