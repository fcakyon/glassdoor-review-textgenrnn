from model import generate, train
from preprocess import preprocess

csv_path = "data/aselsan_reviews.csv"
txt_path = "data/aselsan_reviews.txt"
textgenrnn_weight_path = "data/aselsan_reviews_weight.hdf5"
textgenrnn_output_path = "data/aselsan_reviews_textgenrcnn.txt"
num_epochs = 20  # number of training epochs
num_sentences = 20  # number of sentences to be generated after training

preprocess(csv_path, txt_path)
train(txt_path=txt_path, weight_path=textgenrnn_weight_path, num_epochs=num_epochs)
generate(
    weight_path=textgenrnn_weight_path,
    output_path=textgenrnn_output_path,
    num_sentences=num_sentences,
)
