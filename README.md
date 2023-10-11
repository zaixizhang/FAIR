# Full Atom Protein Pocket Design via Iterative Refinement (FAIR) NeurIPS 2023 Spotlight [[pdf](https://arxiv.org/abs/2310.02553)]

<div align=center><img src="https://github.com/zaixizhang/FAIR/blob/main/FAIR.png" width="700"/></div>

## Install conda environment via conda yaml file
```bash
conda env create -f fair_env.yaml
conda activate fair_env
```

## Datasets
Please refer to [`README.md`](./data/README.md) in the `data` folder.

The data used for training / evaluating the model are organized in the [data](https://drive.google.com/drive/folders/1j21cc7-97TedI7eK?usp=share_link) Google Drive folder.

For a quick reproduction, you can download the preprocessed lmdb file and split file:
* `crossdocked_pocket10_processed_final.lmdb`
* `crossdocked_pocket10_split.pt`
Then place these files in the `data` folder.

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

