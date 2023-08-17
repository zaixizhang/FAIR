## Rebuttal
<div align=left><img src="https://github.com/zaixizhang/FAIR/blob/main/rebuttal/vina.png" width="400"/></div>
<div align=right><img src="https://github.com/zaixizhang/FAIR/blob/main/rebuttal/vina1.png" width="400"/></div>
Figure 1. Here we show some examples that the generated molecules have lower affinity (higher Vina scores) than the reference. Therefore, these molecules have higher probabilities of not binding to the target pocket. The failure may due to the following reasons: (1) Some generated molecules accidentally collide with the pocket, which is unrealistic in nature. (2) The auto-regressive generation scheme may limit its ability for overall optimization. We can observe that some generated molecules only occupy part of the pocket. In the future, we will tackle the aforementioned problems by designing penalty loss to prohibit colliding and explore generation scheme that facilitate overall optimization. 

This is a preliminary version of FAIR for reference. 
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

