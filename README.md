# Full Atom Protein Pocket Design via Iterative Refinement (FAIR) NeurIPS 2023 Spotlight

<div align=center><img src="https://github.com/zaixizhang/FAIR/blob/main/FAIR.png" width="700"/></div>

## Install conda environment via conda yaml file
```bash
conda env create -f fair_env.yaml
conda activate fair_env
```

## Datasets
Please refer to [`README.md`](./data/README.md) in the `data` folder.


## Training
The model hyperparameters can be adjusted in `config`.
```
python train.py
```

## Testing
A checkpoint of our model is provided in the `checkpoint` folder.
```
python test.py
```

