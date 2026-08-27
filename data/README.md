# Dataset Setup

This project uses the Kaggle **CIFAR-10** dataset.

Recommended Kaggle dataset:
https://www.kaggle.com/datasets/ayush1220/cifar10

The dataset contains 60,000 32×32 RGB images across:

1. airplane
2. automobile
3. bird
4. cat
5. deer
6. dog
7. frog
8. horse
9. ship
10. truck

## Option A — Kaggle CLI

Install and authenticate the Kaggle API, then download the dataset:

```bash
kaggle datasets download -d ayush1220/cifar10 -p data/raw
```

Extract the downloaded archive according to the dataset structure.

## Option B — Kaggle Web

Download the dataset from the Kaggle page and place the extracted files under `data/raw/`.

## Important

The raw dataset is deliberately excluded from Git because of its size and dataset terms. Do not commit the full dataset unless you have verified that redistribution is permitted.
