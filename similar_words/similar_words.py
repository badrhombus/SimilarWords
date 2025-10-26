"""
Core module for finding similar words using NLTK's WordNet.
"""

from typing import List, Set, Optional

try:
    from nltk.corpus import wordnet
except ImportError:
    wordnet = None


class SimilarWords:
    """
    A class to find similar words (synonyms) using WordNet.
    
    This class provides methods to find synonyms and related words
    for a given word using NLTK's WordNet corpus.
    """
    
    def __init__(self):
        """Initialize the SimilarWords instance and ensure WordNet is available."""
        self._ensure_wordnet()
    
    def _ensure_wordnet(self):
        """Ensure WordNet data is downloaded and available."""
        global wordnet
        if wordnet is None:
            from nltk.corpus import wordnet as wn
            wordnet = wn
        
        try:
            # Try to access wordnet to see if it's available
            wordnet.synsets('test')
        except LookupError:
            # WordNet not downloaded, download it
            import nltk
            nltk.download('wordnet', quiet=True)
            nltk.download('omw-1.4', quiet=True)
    
    def _extract_lemmas(self, synsets, original_word: str) -> Set[str]:
        """
        Extract lemmas from synsets, excluding the original word.
        
        Args:
            synsets: Iterable of WordNet synsets
            original_word: The original word to exclude
            
        Returns:
            A set of lemma names
        """
        lemmas: Set[str] = set()
        for syn in synsets:
            for lemma in syn.lemmas():
                lemma_name = lemma.name().replace('_', ' ')
                if lemma_name.lower() != original_word.lower():
                    lemmas.add(lemma_name)
        return lemmas
    
    def get_synonyms(self, word: str, limit: Optional[int] = None) -> List[str]:
        """
        Get synonyms for a given word.
        
        Args:
            word: The word to find synonyms for
            limit: Maximum number of synonyms to return (None for all)
            
        Returns:
            A list of synonyms for the word
        """
        synonyms = self._extract_lemmas(wordnet.synsets(word), word)
        result = sorted(list(synonyms))
        
        if limit is not None and limit > 0:
            result = result[:limit]
        
        return result
    
    def get_definitions(self, word: str) -> List[str]:
        """
        Get definitions for a given word.
        
        Args:
            word: The word to get definitions for
            
        Returns:
            A list of definitions for the word
        """
        definitions = []
        for syn in wordnet.synsets(word):
            definitions.append(syn.definition())
        return definitions
    
    def get_related_words(self, word: str, limit: Optional[int] = None) -> List[str]:
        """
        Get related words including synonyms, hypernyms, and hyponyms.
        
        Args:
            word: The word to find related words for
            limit: Maximum number of related words to return (None for all)
            
        Returns:
            A list of related words
        """
        related: Set[str] = set()
        
        for syn in wordnet.synsets(word):
            # Add synonyms
            related.update(self._extract_lemmas([syn], word))
            
            # Add hypernyms (more general terms)
            related.update(self._extract_lemmas(syn.hypernyms(), word))
            
            # Add hyponyms (more specific terms)
            related.update(self._extract_lemmas(syn.hyponyms(), word))
        
        result = sorted(list(related))
        
        if limit is not None and limit > 0:
            result = result[:limit]
        
        return result
