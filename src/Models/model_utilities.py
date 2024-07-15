import numpy as np
import keras
import tensorflow as tf

from Models.VectorQuantizer import VectorQuantizer


def get_batch(
    song: np.ndarray,
    sequence_length: int,
    batch_size: int,
    n_channels: int = 1,
    batch_offset: int = 1,
):
    """
    Create an input and output batch for sequence training.
    """

    song_length = len(song)
    max = 1 + song_length - (sequence_length + batch_offset)
    index = np.random.choice(max, batch_size)

    input_batch = [song[i : i + sequence_length] for i in index]
    output_batch = [
        song[i + batch_offset : i + sequence_length + batch_offset] for i in index
    ]

    x_batch = np.reshape(input_batch, [batch_size, sequence_length, n_channels])
    y_batch = np.reshape(output_batch, [batch_size, sequence_length, n_channels])
    return x_batch, y_batch


def display_batch_predictions(
    input_batch: np.ndarray, output_batch: np.ndarray, predictions: int = 10
):
    squeezed_in = np.squeeze(input_batch)
    squeezed_out = np.squeeze(output_batch)
    zipped = zip(squeezed_in, squeezed_out)

    for i, (input, output) in enumerate(zipped):
        if i >= predictions:
            break

        print(f"Input: {input} | Expected Output: {output}")


def int16_to_uint16(input: np.ndarray[np.int16]):
    uint16 = input + 2**15
    return uint16.astype(np.uint16)


def uint16_to_int16(input: np.ndarray[np.uint16]):
    int16 = input - 2**15
    return int16.astype(np.int16)


def float32_to_int16(input: np.ndarray[np.float32]):
    int16 = input * 2**15
    return int16.astype(np.int16)

def uint16_to_float32(input: np.ndarray[np.uint16]):
    float32 = input / 2**16 - 1
    return float32


def get_encoder(latent_dim=16):
    encoder_inputs = keras.Input(shape=(28, 28, 1))
    x = keras.layers.Conv2D(32, 3, activation="relu", strides=2, padding="same")(
        encoder_inputs
    )
    x = keras.layers.Conv2D(64, 3, activation="relu", strides=2, padding="same")(x)
    encoder_outputs = keras.layers.Conv2D(latent_dim, 1, padding="same")(x)
    return keras.Model(encoder_inputs, encoder_outputs, name="encoder")


def get_decoder(latent_dim=16):
    latent_inputs = keras.Input(shape=get_encoder(latent_dim).output.shape[1:])
    x = keras.layers.Conv2DTranspose(
        64, 3, activation="relu", strides=2, padding="same"
    )(latent_inputs)
    x = keras.layers.Conv2DTranspose(
        32, 3, activation="relu", strides=2, padding="same"
    )(x)
    decoder_outputs = keras.layers.Conv2DTranspose(1, 3, padding="same")(x)
    return keras.Model(latent_inputs, decoder_outputs, name="decoder")


def get_vqvae(latent_dim=16, num_embeddings=64):
    vq_layer = VectorQuantizer(num_embeddings, latent_dim, name="vector_quantizer")
    encoder = get_encoder(latent_dim)
    decoder = get_decoder(latent_dim)
    inputs = keras.Input(shape=(28, 28, 1))
    encoder_outputs = encoder(inputs)
    quantized_latents = vq_layer(encoder_outputs)
    reconstructions = decoder(quantized_latents)
    return keras.Model(inputs, reconstructions, name="vq_vae")
