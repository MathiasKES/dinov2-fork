# Full manual install:
```bash
conda create -n dinov2-xf python=3.9
conda activate dinov2-xf
```
```bash
pip install torch==2.0.0+cu117 torchvision==0.15.0+cu117 --extra-index-url https://download.pytorch.org/whl/cu117
conda install -c conda-forge omegaconf torchmetrics=0.10.3 fvcore iopath cmake ninja
pip install git+https://github.com/facebookincubator/submitit cuml-cu11 mmcv-full==1.5.0 mmsegmentation==0.27.0 --extra-index-url https://pypi.nvidia.com
```

## Build xformers compatible with our python version
```bash
pip install --no-deps git+https://github.com/facebookresearch/xformers@main
```