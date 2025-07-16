# APSAM
代码框架参考SAMUS

[SAMUS: Adapting Segment Anything Model for Clinically-Friendly and Generalizable Ultrasound Image Segmentation.](https://arxiv.org/pdf/2309.06824.pdf)\

## 环境配置
Following [Segment Anything](https://github.com/facebookresearch/segment-anything), `python=3.8.16`, `pytorch=1.8.0`, and `torchvision=0.9.0` are used in SAMUS.

1. Create a virtual environment for SAMUS and activate the environment.
    ```
    conda create -n SAMUS python=3.8
    conda activate SAMUS
    ```
2. Install Pytorch and TorchVision.
   (you can follow the instructions [here](https://pytorch.org/get-started/locally/))
3. Install other dependencies.
  ```
    pip install -r requirements.txt
  ```
## Checkpoints
原始SAM的ckpt已经放在`/home/data2/zkj/llt_code/SAMUS/checkpoints/sam_vit_b_01ec64.pth`
APSAM的ckpt全部在`/home/data2/zkj/llt_code/SAMUS/checkpoints/`里面的文件夹

## Data
各X光数据集分割版本在`/home/data2/zkj/semantic-seg-dataset/`

## 训练
在主目录shell运行：
```
python train_our.py --modelname fpSAM_noCNN --task Xrayall
```
靠config传入训练，训练参数请移步`utils/config.py`中的Xrayall设置

## 测试

```
python test.py --modelname fpSAM_noCNN --task Xrayall
```
还没适配好，这个现在用不了

## 引用
Thanks for：
```
@misc{lin2023samus,
      title={SAMUS: Adapting Segment Anything Model for Clinically-Friendly and Generalizable Ultrasound Image Segmentation}, 
      author={Xian Lin and Yangyang Xiang and Li Zhang and Xin Yang and Zengqiang Yan and Li Yu},
      year={2023},
      eprint={2309.06824},
      archivePrefix={arXiv},
      primaryClass={cs.CV}
}
```

