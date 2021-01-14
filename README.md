# Introduction
This repo lets you train [char-rnn](http://karpathy.github.io/2015/05/21/rnn-effectiveness/) with Glassdoor reviews of [Aselsan](https://www.glassdoor.com/Reviews/Aselsan-Reviews-E41213.htm), [TAI](https://www.glassdoor.com/Reviews/Turkish-Aerospace-Industries-Reviews-E326234.htm), [Turkcell](hhttps://www.glassdoor.com/Reviews/Turkcell-Reviews-E9709.htm) and [Turkish Airlines](https://www.glassdoor.com/Reviews/Turkish-Airlines-Reviews-E13316.htm)

Refer to [demo notebook](<https://github.com/fcakyon/glassdoor-review-textgenrnn/tree/main/notebook/demo.ipynb>) for sample usage.

# Installation
First, make sure that you're using Python 3.

1. Clone or download this repository.
2. Run `pip install -r requirements.txt` inside this repo. Consider doing this inside of a Python virtual environment.

# Usage
Download Glassdoor reviews of any company using [glassdoor-review-scraper](https://github.com/MatthewChatham/glassdoor-review-scraper). Scraped reviews for Aselsan, TAI, Turkcell and Turkish Airlines are provided under `data` folder as `companyname_reviews.csv`.

1. Edit train/generator parameters for desired company, `nano aselsan_review_generator.py`
2. Train and generate reviews for desired company, `python aselsan_review_generator.py`
3. Generated texts will be saved to `textgenrnn_output_path`



