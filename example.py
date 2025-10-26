"""
Example usage of the SimilarWords library.
"""

from similar_words import SimilarWords


def main():
    # Initialize the library
    sw = SimilarWords()
    
    # Example 1: Get synonyms for a word
    print("=" * 50)
    print("Example 1: Get synonyms for 'happy'")
    print("=" * 50)
    synonyms = sw.get_synonyms("happy")
    print(f"Synonyms: {', '.join(synonyms[:10])}")
    print()
    
    # Example 2: Get synonyms with a limit
    print("=" * 50)
    print("Example 2: Get 5 synonyms for 'beautiful'")
    print("=" * 50)
    synonyms = sw.get_synonyms("beautiful", limit=5)
    print(f"Synonyms: {', '.join(synonyms)}")
    print()
    
    # Example 3: Get definitions
    print("=" * 50)
    print("Example 3: Get definitions for 'computer'")
    print("=" * 50)
    definitions = sw.get_definitions("computer")
    for i, definition in enumerate(definitions[:3], 1):
        print(f"{i}. {definition}")
    print()
    
    # Example 4: Get related words
    print("=" * 50)
    print("Example 4: Get related words for 'dog'")
    print("=" * 50)
    related = sw.get_related_words("dog", limit=15)
    print(f"Related words: {', '.join(related)}")
    print()
    
    # Example 5: Explore a word in detail
    print("=" * 50)
    print("Example 5: Explore the word 'run'")
    print("=" * 50)
    word = "run"
    print(f"Word: {word}")
    print(f"\nSynonyms ({len(sw.get_synonyms(word))} total):")
    print(f"  {', '.join(sw.get_synonyms(word, limit=10))}")
    print(f"\nDefinitions ({len(sw.get_definitions(word))} total):")
    for i, definition in enumerate(sw.get_definitions(word)[:3], 1):
        print(f"  {i}. {definition}")
    print(f"\nRelated words ({len(sw.get_related_words(word))} total):")
    print(f"  {', '.join(sw.get_related_words(word, limit=15))}")


if __name__ == "__main__":
    main()
