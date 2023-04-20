'''
AI50 2023
Week 2: pagerank.py
Complete the implementation of transition_model, sample_pagerank, and iterate_pagerank
'''

import os
import random
import re
import sys

DAMPING = 0.85
SAMPLES = 10000


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    ranks = iterate_pagerank(corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")


def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(
            link for link in pages[filename]
            if link in pages
        )

    return pages


def transition_model(corpus, page, damping_factor):
    """
    Return a probability distribution over which page to visit next,
    given a current page.

    With probability `damping_factor`, choose a link at random
    linked to by `page`. With probability `1 - damping_factor`, choose
    a link at random chosen from all pages in the corpus.
    """
    distribution = {}
    links = corpus[page]
    if len(links) == 0:
        # If the current page has no links, return a uniform probability distribution over all pages.
        for page in corpus:
            distribution[page] = 1 / len(corpus)
    else:
        # If the current page has links, calculate the probability of moving to each linked page.
        for link in links:
            distribution[link] = damping_factor / len(links)
        # Add the probability of moving to a random page not linked from the current page.
        for page in corpus:
            if page not in links:
                distribution[page] = (1 - damping_factor) / (len(corpus) - len(links))
    return distribution


def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    rank = {}
    # Initialize the rank for each page to 0
    for page in corpus:
        rank[page] = 0
    # Start with a random page
    current_page = random.choice(list(corpus.keys()))
    # Sample n pages and update the rank accordingly
    for i in range(n):
        # Increment the count for the current page
        rank[current_page] += 1
        # Get the transition probability distribution for the current page
        distribution = transition_model(corpus, current_page, damping_factor)
        # Convert the distribution to separate lists of pages and probabilities
        pages = list(distribution.keys())
        probabilities = list(distribution.values())
        # Use the distribution to randomly choose the next page to visit
        current_page = random.choices(pages, weights=probabilities, k=1)[0]
    # Normalize the rank by dividing each count by the total number of samples
    for page in rank:
        rank[page] /= n
    return rank


def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    # Initialize variables
    num_pages = len(corpus)
    initial_rank = 1 / num_pages
    ranks = {page: initial_rank for page in corpus}
    new_ranks = None

    # Loop until PageRank values converge
    while new_ranks is None or max(abs(ranks[page] - new_ranks[page]) for page in corpus) > 0.001:
        ranks = new_ranks or ranks
        new_ranks = {page: (1 - damping_factor) / num_pages + damping_factor * sum(
            ranks[link] / len(corpus[link]) for link in corpus if page in corpus[link]) for page in corpus}

    # Normalize ranks so they sum to 1
    rank_sum = sum(ranks.values())
    ranks = {page: rank / rank_sum for page, rank in ranks.items()}

    return ranks


if __name__ == "__main__":
    main()
