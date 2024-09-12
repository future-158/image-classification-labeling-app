default:
  just --list

install:   
    #!/bin/bash
    set -exo pipefail    
    source /opt/conda/etc/profile.d/conda.sh

    conda env list | grep  $PWD/venv || conda create -y --prefix $PWD/venv python=3.11 pip ipykernel
    conda activate $PWD/venv
    pip install streamlit-shortcuts
    pip install datasets cffi

download:
    #!/bin/env python
    from datasets import load_dataset
    from pathlib import Path

    img_dir = Path('data')
    img_dir.mkdir(exist_ok=True, parents=True)
    ds = load_dataset("roskyluo/stanford_cars_blip")    
    for i, sample in enumerate(ds['train'].take(50)):
        sample['image'].save( img_dir / f"image-{i}.jpg")
    ds['train'].shuffle()['text']
    

