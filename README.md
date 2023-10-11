# Full Atom Protein Pocket Design via Iterative Refinement (FAIR) NeurIPS 2023 Spotlight [[pdf](https://arxiv.org/abs/2310.02553)]

<div align=center><img src="https://github.com/zaixizhang/FAIR/blob/main/FAIR.png" width="700"/></div>

## Install conda environment via conda yaml file
```bash
conda env create -f fair_env.yaml
conda activate fair_env
```

## Datasets
Please refer to [`README.md`](./data/README.md) in the `data` folder.

The data used for training / evaluating the model are organized in the [data](https://drive.google.com/drive/folders/1cyhwpmm8a3Z3i8yCms0BRW5tIMalMXex?usp=sharing) Google Drive folder.

For a quick reproduction, you can download the preprocessed lmdb file and name2id file:
* `crossdocked_pocket10_processed_final.lmdb`
* `crossdocked_pocket10_name2id.pt`
  
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
Expected results on the CrossDocked dataset:

| AAR  | RMSD   |
|-------|-------|
| 40.8\% ± 10.9 \% | 1.44 ± 0.06 |

## Citation
```
@article{zhang2023full,
  title={Full-Atom Protein Pocket Design via Iterative Refinement},
  author={Zhang, Zaixi and Lu, Zepu and Hao, Zhongkai and Zitnik, Marinka and Liu, Qi},
  journal={NeurIPS},
  year={2023}
}
```
