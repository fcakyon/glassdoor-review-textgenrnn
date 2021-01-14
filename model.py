from textgenrnn import textgenrnn


def train(
    txt_path,
    weight_path,
    num_epochs=10,
):
    """
    Trains char rnn model using the data in txt_path for num_epochs epochs.
    Then saves the trained model to weight_path.
    """
    # train textgenrnn
    textgen = textgenrnn()
    textgen.train_from_file(file_path=txt_path, num_epochs=num_epochs)

    # save weights
    textgen.save(weights_path=weight_path)


def generate(weight_path, output_path, num_sentences=20):
    """
    Generates num_sentences number of sentences using the model weights given in weight_path.
    Then saves the generated sentences to output_path.
    """
    # generate textgenrnn results to file
    textgen = textgenrnn(weight_path)
    textgen.generate_to_file(output_path, n=num_sentences)
