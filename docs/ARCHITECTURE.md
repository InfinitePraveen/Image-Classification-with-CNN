# Architecture

The baseline network uses stacked convolutional blocks with batch normalization and max pooling, followed by dropout and dense classification.

Input → Rescaling → Conv Block → Conv Block → Pool → Conv Block → Conv Block → Pool → Flatten → Dense → Softmax.
