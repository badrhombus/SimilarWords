# SimilarWords

A Python library for finding similar words (synonyms and related words) using NLTK's WordNet.

## Features

- **Get Synonyms**: Find synonyms for any word
- **Get Definitions**: Retrieve definitions for words
- **Get Related Words**: Find related words including synonyms, hypernyms (broader terms), and hyponyms (narrower terms)
- **Automatic WordNet Setup**: Automatically downloads required NLTK data on first use

## Installation

```bash
pip install -r requirements.txt
```

Or install directly:

```bash
pip install nltk
```

## Usage

### Basic Usage

```python
from similar_words import SimilarWords

# Initialize the library
sw = SimilarWords()

# Get synonyms for a word
synonyms = sw.get_synonyms("happy")
print(synonyms)  # ['blessed', 'felicitous', 'glad', 'well-chosen', ...]

# Get synonyms with a limit
synonyms = sw.get_synonyms("beautiful", limit=5)
print(synonyms)  # First 5 synonyms

# Get definitions
definitions = sw.get_definitions("computer")
print(definitions)
# ['a machine for performing calculations automatically', ...]

# Get related words (synonyms + hypernyms + hyponyms)
related = sw.get_related_words("dog", limit=10)
print(related)  # ['Canis familiaris', 'canine', 'domestic dog', ...]
```

### Running the Example

```bash
python example.py
```

This will demonstrate various features of the library.

### Running Tests

```bash
python -m pytest tests/
```

Or using unittest:

```bash
python -m unittest discover tests
```

## API Reference

### `SimilarWords`

The main class for finding similar words.

#### Methods

- **`get_synonyms(word: str, limit: Optional[int] = None) -> List[str]`**
  
  Get synonyms for a given word.
  
  - `word`: The word to find synonyms for
  - `limit`: Maximum number of synonyms to return (None for all)
  - Returns: A list of synonyms

- **`get_definitions(word: str) -> List[str]`**
  
  Get definitions for a given word.
  
  - `word`: The word to get definitions for
  - Returns: A list of definitions

- **`get_related_words(word: str, limit: Optional[int] = None) -> List[str]`**
  
  Get related words including synonyms, hypernyms, and hyponyms.
  
  - `word`: The word to find related words for
  - `limit`: Maximum number of related words to return (None for all)
  - Returns: A list of related words

## Requirements

- Python 3.7+
- NLTK 3.8+

## License

MIT License

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.