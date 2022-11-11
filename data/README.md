## Dataset

In this repository, we provide a few examples figures from the original dataset, with the same file structure as following. Here we give the file tree of the full dataset. Then we will in detail introduce each folder and file, to help you have a better understanding to this repo. 

```
.
├── convert/
│   └── smap-2022-08-03T13-48-18.19
│       ├── img.png
│       ├── label.png
│       ├── label_name.txt
│       └── label_viz.png
├── labelme/
│   └── smap-2022-08-03T13-48-18.19.json
├── original/
│   ├── 2022-08-03/
│   │   ├── view_1/
│   │   │   ├── smap-2022-08-03T13-48-18.19.jpeg
│   │   │   └── ...
│   │   ├── view_2/
│   │   │   └── ...
│   │   └── view_3/
│   │       └── ...
│   ├── 2022-08-04/
│   │   └── ...
│   └── ...
├── processed/
│   ├── 2022-08-03/
│   │   ├── view_1/
│   │   │   ├── smap-2022-08-03T13-48-18.19.jpeg
│   │   │   └── ...
│   │   ├── view_2/
│   │   │   └── ...
│   │   └── view_3/
│   │       └── ...
│   ├── 2022-08-04/
│   │   └── ...
│   └── ...
└── README.md
```

### Original dataset `original`

This folder is for the original downloaded dataset. Original figures are organized by date in each folder named by `yyyy-mm-dd`. Each folder has three subfolders which are three views figure `view_1`, `view_2`, `view_3`. Under the view folder there would be the figure named by the format `smap-yyyy-mm-ddThh-mm-ss.ss.jpeg`. 

### Processed dataset `processed`

In this preprocessing tool, the first step is converting the original figure to `csv` file for the next step's analysis. If you run the `notebook/01_file_convert.ipynb`, you can get the `processed` from the original data. The converted data has the same structure with the original dataset. Only the data changes from `jpeg` to `csv`.

### Labelme output `labelme` and `convert`

Following the startup tutorial, we will use the Lableme to label the figure, and the output would be a `json` file. We put those files in the `labelme` folder. Since this process has to be done manually, there will be not too many figures there. But if you have many labeled figure from different date and views, we still recommonment you to use the file structure same as the original dataset for a better organization. 

In the meanwhile, Labelme will also output four files for each input figure, which are shown in the `convert` folder: 

- `img.png`: the loaded image (left figure);
- `label.png`: your labeled place in the image will be marked by different colors (middle figure);
- `label_name.txt`: records the name for each label;
- `label_viz.png`: the loaded image with the label in the figure (right figure). 

<img src="../fig/segment.png" width="90%">

You can get better understanding by referring to the notebook `03_analysis.ipynb`. 

We hope this data file structure tutorial will help you avoid some bugs during the data preprocessing. 

