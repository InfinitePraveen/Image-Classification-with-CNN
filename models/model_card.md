# Model Card — CIFAR-10 CNN

## Model

`cifar10_cnn.keras`

## Intended Use

Educational image classification on CIFAR-10-like 32×32 RGB images.

## Classes

airplane, automobile, bird, cat, deer, dog, frog, horse, ship, truck.

## Input

RGB image resized to 32×32 pixels and normalized to `[0, 1]`.

## Output

Ten-class softmax probabilities.

## Limitations

- CIFAR-10 images are very small.
- Real-world photographs may differ substantially from CIFAR-10.
- Confidence is not a guarantee of correctness.
- Performance depends on the exact training run and hardware.

## Reproducibility

Use the notebooks in numerical order. Record the random seed, TensorFlow version, epochs and batch size for comparable experiments.
