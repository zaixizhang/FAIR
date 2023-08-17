## Rebuttal
<div align=center><img src="https://github.com/zaixizhang/FAIR/blob/main/rebuttal/vina.png" width="400"/><img src="https://github.com/zaixizhang/FAIR/blob/main/rebuttal/vina1.png" width="400"/></div>
Figure 1. Box plot Vina scores with re-docking (left) and without re-docking (right) on the CrossDocked dataset.


<div align=center><img src="https://github.com/zaixizhang/FAIR/blob/main/rebuttal/vina2.png" width="400"/><img src="https://github.com/zaixizhang/FAIR/blob/main/rebuttal/vina3.png" width="400"/></div>
Figure 1. Box plot Vina scores with re-docking (left) and without re-docking (right) on the Binding MOAD dataset.


## Install conda environment via conda yaml file
```bash
conda env create -f fair_env.yaml
conda activate fair_env
```

## Datasets
Please refer to [`README.md`](./data/README.md) in the `data` folder.


## Training

```
python train.py
```

## Testing

```
python test.py
```

