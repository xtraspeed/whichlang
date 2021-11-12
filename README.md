# whichlang

whichlang is a Python library for identifying the language of the given text for Indian languages.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install whichlang.

```bash
pip install whichlang
```

## Usage

```python
from whichlang import whichlang as wl

f = open('sample-test-files\\sample-hindi.txt','r')
data = f.read()

# returns tuple of top 3 probable languages, first one being most probable language
print (wl.which_lang(data))
>>> ('Hindi', 'Marathi', 'Punjabi') #Hindi is most probable. 
```

```
# For training a language model
# assamese.txt is train data
# Assamese is the language model created
python train_lang_models.py -f train-data\as\assamese.txt -l Assamese
```
## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)

## Available Languages
Hindi, Telugu, Tamil, Kannada, Malayalam, Punjabi, Marathi, Gujarati, Oriya, Assamese.

## Acknowledgements
1. We would like to thank the [Leipzig Corpora collection](https://corpora.uni-leipzig.de/en) where we collected data for training models. 
    Dirk Goldhahn, Thomas Eckart and Uwe Quasthoff (2012): Building Large Monolingual Dictionaries at the Leipzig Corpora Collection: From 100 to 200 Languages. In: Proceedings of the Eighth International Conference on Language Resources and Evaluation (LREC'12), 2012
2. whichlang is based on N-gram based Text categorization: Cavnar, William B., and John M. Trenkle. "N-gram-based text categorization." Proceedings of   SDAIR-94, 3rd annual symposium on document analysis and information retrieval. Vol. 161175. 1994.
 The same approach was used in library [langdetect]((https://github.com/fedelopez77/langdetect)). We found this approach quite effective and wanted to explore for Indian languages. In whichlang, we train, optimize and make  models readily available for Indian languages since these languages have been less explored.






