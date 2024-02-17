# multi-stage-self-supervised-learning-model-for-OCT-classification

A novel multi-stage self-supervised learning model for classifying different retinal diseases from optical coherence tomography(OCT) images.
Our model can achieve a high level of performance with only a small amount of labeled data.

## Requirements
- Linux (Ubuntu 18.04 or later)
- Python>=3.6.2 and < 3.9
- PyTorch>=1.4
- torchvision
- CUDA
- OpenCV
- VISSL

## Installation Instruction
- Download and Install [Nvidia Drivers](https://www.nvidia.com/Download/driverResults.aspx/142567/en-us)
- Download and Install via Runfile [Nvidia Cuda Toolkit 9.0](https://developer.nvidia.com/cuda-90-download-archive?target_os=Linux&target_arch=x86_64&target_distro=Ubuntu&target_version=1604&target_type=runfilelocal)
- Download and Install [Nvidia CuDNN 7.1 or later](https://developer.nvidia.com/rdp/cudnn-archive)
- Install Python>=3.6.2 and < 3.9
- Install [PyTorch](https://pytorch.org/)>=1.4
- Install [VISSL](https://vissl.readthedocs.io/en/v0.1.6/)

## Install VISSL from source in Conda environment
- Install PyTorch, APEX
```bash
conda install pytorch==1.8.1 torchvision==0.9.1 cudatoolkit=10.2 -c pytorch
conda install -c vissl apex
```
- Install VISSL
```bash
# clone vissl repository
cd $HOME && git clone --recursive https://github.com/facebookresearch/vissl.git && cd $HOME/vissl/
git checkout v0.1.6
git checkout -b v0.1.6
pip install --progress-bar off -r requirements.txt
pip install opencv-python
# update classy vision install to commit stable for vissl.
pip uninstall -y classy_vision
pip install classy-vision@https://github.com/facebookresearch/ClassyVision/tarball/4785d5ee19d3bcedd5b28c1eb51ea1f59188b54d
# update fairscale install to commit stable for vissl.
pip uninstall -y fairscale
pip install fairscale==0.4.6
```
- VISSL citation
```
@misc{goyal2021vissl,
  author =       {Priya Goyal and Quentin Duval and Jeremy Reizenstein and Matthew Leavitt and Min Xu and
                  Benjamin Lefaudeux and Mannat Singh and Vinicius Reis and Mathilde Caron and Piotr Bojanowski and
                  Armand Joulin and Ishan Misra},
  title =        {VISSL},
  howpublished = {\url{https://github.com/facebookresearch/vissl}},
  year =         {2021}
}
```

## OCT datasets (OCT2017, Srinivasan2014, OCTID)
- OCT2017 dataset download link
```
https://data.mendeley.com/datasets/rscbjbr9sj/2
```
- OCT2017 dataset citation
```
@article{kermany2018identifying,
  title={Identifying medical diagnoses and treatable diseases by image-based deep learning},
  author={Kermany, Daniel S and Goldbaum, Michael and Cai, Wenjia and Valentim, Carolina CS and Liang, Huiying and Baxter, Sally L and McKeown, Alex and Yang, Ge and Wu, Xiaokang and Yan, Fangbing and others},
  journal={cell},
  volume={172},
  number={5},
  pages={1122--1131},
  year={2018},
  publisher={Elsevier}
}
```
- Srinivasan2014 dataset download link
```
http://people.duke.edu/~sf59/Srinivasan_BOE_2014_dataset.htm
```
- Srinivasan2014 dataset citation
```
@article{srinivasan2014fully,
  title={Fully automated detection of diabetic macular edema and dry age-related macular degeneration from optical coherence tomography images},
  author={Srinivasan, Pratul P and Kim, Leo A and Mettu, Priyatham S and Cousins, Scott W and Comer, Grant M and Izatt, Joseph A and Farsiu, Sina},
  journal={Biomedical optics express},
  volume={5},
  number={10},
  pages={3568--3577},
  year={2014},
  publisher={Optica Publishing Group}
}
```
- OCTID dataset download link
```
https://borealisdata.ca/dataverse/OCTID
```
- OCTID dataset citation
```
@article{gholami2020octid,
  title={OCTID: Optical coherence tomography image database},
  author={Gholami, Peyman and Roy, Priyanka and Parthasarathy, Mohana Kuppuswamy and Lakshminarayanan, Vasudevan},
  journal={Computers \& Electrical Engineering},
  volume={81},
  pages={106532},
  year={2020},
  publisher={Elsevier}
}
```

## pre-trained model
