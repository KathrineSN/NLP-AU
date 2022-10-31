import torch
from torch import nn

import numpy as np


def gensim_to_torch_embedding(gensim_wv):
    """
    - Add type hints on input and output
    - add function description
    - understand the pad and unk embeddings, add an argument which makes these optional. 
        E.g. add_padding = True and add_unknown = True
    """
    embedding_size = gensim_wv.vectors.shape[1] # Getting the size of the embedding
    print(embedding_size)
    # create unknown and padding embedding
    unk_emb = np.mean(gensim_wv.vectors, axis=0).reshape((1, embedding_size)) # creating an initial 'mean' embedding
    pad_emb = np.zeros((1, gensim_wv.vectors.shape[1]))
    print(unk_emb)
    print(unk_emb.shape)
    print(pad_emb)
    print(unk_emb.shape)

    # add the new embedding
    embeddings = np.vstack([gensim_wv.vectors, unk_emb, pad_emb]) # stacking the gensim embeddings of each word in vocabulary and unknown and pad embedding
    print('embedding')
    print(embeddings)
    print(embeddings.shape)

    weights = torch.FloatTensor(embeddings) # weight is 'just' the tensor version of the embedding
    print('weight')
    print(weights)
    print(weights.shape)

    emb_layer = nn.Embedding.from_pretrained(embeddings=weights, padding_idx=-1)
    print('emb layer')
    print(emb_layer)

    # creating vocabulary
    vocab = gensim_wv.key_to_index
    vocab["UNK"] = weights.shape[0] - 2
    vocab["PAD"] = emb_layer.padding_idx

    return emb_layer, vocab