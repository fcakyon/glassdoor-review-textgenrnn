import pandas


def preprocess(source_path, target_path):
    """
    Preprocesses pros and cons column of the csv file given in source_path.
    Then exports each sentence in a new line to target_path as a txt file.
    """
    csv_path = source_path
    txt_path = target_path

    # read scraped reviews
    data = pandas.read_csv(csv_path)

    # parse sentences
    sentences = []
    for con in data.cons.tolist():
        sentences.extend(str(con).split("\n"))
    for pro in data.pros.tolist():
        sentences.extend(str(pro).split("\n"))

    # remove unwanted senteces/ clean sentences
    filtered_sentences = []
    unwanted_word_list = [
        "Helpfu",
        "Advice to Management",
        "Cons",
        "hola",
        "mal ambiente",
    ]
    for sentence in sentences:
        sentence = (
            sentence.replace("-", "")
            .replace("a)", "")
            .replace("b)", "")
            .replace("*", "")
        )
        if (
            not any([unwanted_word in sentence for unwanted_word in unwanted_word_list])
            and sentence
            and (sentence != "none")
            and (sentence != "PERFECT")
        ):
            if sentence[0] == " ":
                sentence = sentence[1:]

            filtered_sentences.append(sentence)

    # export processed sentences
    with open(txt_path, "w") as filehandle:
        for sentence in filtered_sentences:
            filehandle.write("%s\n" % sentence)
