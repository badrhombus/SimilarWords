"""
Core module for finding similar words using NLTK's WordNet.
"""

from typing import List, Set, Optional


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
        try:
            from nltk.corpus import wordnet
            # Try to access wordnet to see if it's available
            wordnet.synsets('test')
        except LookupError:
            # WordNet not downloaded, download it
            import nltk
            nltk.download('wordnet', quiet=True)
            nltk.download('omw-1.4', quiet=True)
    
    def get_synonyms(self, word: str, limit: Optional[int] = None) -> List[str]:
        """
        Get synonyms for a given word.
        
        Args:
            word: The word to find synonyms for
            limit: Maximum number of synonyms to return (None for all)
            
        Returns:
            A list of synonyms for the word
        """
        from nltk.corpus import wordnet
        
        synonyms: Set[str] = set()
        
        # Get all synsets for the word
        for syn in wordnet.synsets(word):
            # Get all lemmas (word forms) for each synset
            for lemma in syn.lemmas():
                synonym = lemma.name().replace('_', ' ')
                # Don't include the original word
                if synonym.lower() != word.lower():
                    synonyms.add(synonym)
        
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
        from nltk.corpus import wordnet
        
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
        from nltk.corpus import wordnet
        
        related: Set[str] = set()
        
        for syn in wordnet.synsets(word):
            # Add synonyms
            for lemma in syn.lemmas():
                related_word = lemma.name().replace('_', ' ')
                if related_word.lower() != word.lower():
                    related.add(related_word)
            
            # Add hypernyms (more general terms)
            for hypernym in syn.hypernyms():
                for lemma in hypernym.lemmas():
                    related_word = lemma.name().replace('_', ' ')
                    if related_word.lower() != word.lower():
                        related.add(related_word)
            
            # Add hyponyms (more specific terms)
            for hyponym in syn.hyponyms():
                for lemma in hyponym.lemmas():
                    related_word = lemma.name().replace('_', ' ')
                    if related_word.lower() != word.lower():
                        related.add(related_word)
        
        result = sorted(list(related))
        
        if limit is not None and limit > 0:
            result = result[:limit]
        
        return result
