'''
AI50 2023
Week 2: heredity.py
Complete the implementations of joint_probability, update, and normalize.
'''


import csv
import itertools
import sys

PROBS = {

    # Unconditional probabilities for having gene
    "gene": {
        2: 0.01,
        1: 0.03,
        0: 0.96
    },

    "trait": {

        # Probability of trait given two copies of gene
        2: {
            True: 0.65,
            False: 0.35
        },

        # Probability of trait given one copy of gene
        1: {
            True: 0.56,
            False: 0.44
        },

        # Probability of trait given no gene
        0: {
            True: 0.01,
            False: 0.99
        }
    },

    # Mutation probability
    "mutation": 0.01
}


def main():

    # Check for proper usage
    if len(sys.argv) != 2:
        sys.exit("Usage: python heredity.py data.csv")
    people = load_data(sys.argv[1])

    # Keep track of gene and trait probabilities for each person
    probabilities = {
        person: {
            "gene": {
                2: 0,
                1: 0,
                0: 0
            },
            "trait": {
                True: 0,
                False: 0
            }
        }
        for person in people
    }

    # Loop over all sets of people who might have the trait
    names = set(people)
    for have_trait in powerset(names):

        # Check if current set of people violates known information
        fails_evidence = any(
            (people[person]["trait"] is not None and
             people[person]["trait"] != (person in have_trait))
            for person in names
        )
        if fails_evidence:
            continue

        # Loop over all sets of people who might have the gene
        for one_gene in powerset(names):
            for two_genes in powerset(names - one_gene):

                # Update probabilities with new joint probability
                p = joint_probability(people, one_gene, two_genes, have_trait)
                update(probabilities, one_gene, two_genes, have_trait, p)

    # Ensure probabilities sum to 1
    normalize(probabilities)

    # Print results
    for person in people:
        print(f"{person}:")
        for field in probabilities[person]:
            print(f"  {field.capitalize()}:")
            for value in probabilities[person][field]:
                p = probabilities[person][field][value]
                print(f"    {value}: {p:.4f}")


def load_data(filename):
    """
    Load gene and trait data from a file into a dictionary.
    File assumed to be a CSV containing fields name, mother, father, trait.
    mother, father must both be blank, or both be valid names in the CSV.
    trait should be 0 or 1 if trait is known, blank otherwise.
    """
    data = dict()
    with open(filename) as f:
        reader = csv.DictReader(f)
        for row in reader:
            name = row["name"]
            data[name] = {
                "name": name,
                "mother": row["mother"] or None,
                "father": row["father"] or None,
                "trait": (True if row["trait"] == "1" else
                          False if row["trait"] == "0" else None)
            }
    return data


def powerset(s):
    """
    Return a list of all possible subsets of set s.
    """
    s = list(s)
    return [
        set(s) for s in itertools.chain.from_iterable(
            itertools.combinations(s, r) for r in range(len(s) + 1)
        )
    ]


def probability_for_person(person, one_genes_set, two_genes_set, have_trait_set):
    """
    Compute and return the probability of gene number and trait status for a single person.
    """
    # Determine the number of genes for this person based on their category
    if person in one_genes_set:
        num_genes = 1
    elif person in two_genes_set:
        num_genes = 2
    else:
        num_genes = 0

    # Determine if this person has the trait or not
    has_trait = person in have_trait_set

    # Get the probability of this person's gene number and trait status
    gene_number_probability = PROBS['gene'][num_genes]
    trait_probability = PROBS['trait'][num_genes][has_trait]

    # If this person has parents, calculate the probability of inheriting genes from them
    if people[person]['mother'] is not None:
        mother = people[person]['mother']
        father = people[person]['father']
        parent_gene_probs = {}
        for parent in [mother, father]:
            if parent in one_genes_set:
                parent_gene_prob = 0.5
            elif parent in two_genes_set:
                parent_gene_prob = 1 - PROBS['mutation']
            else:
                parent_gene_prob = PROBS['mutation']
            parent_gene_probs[parent] = parent_gene_prob

        # Calculate the probability of this person's gene number based on their parents' gene numbers
        if num_genes == 0:
            # Probability of not inheriting gene from either parent
            gene_number_probability = (1 - parent_gene_probs[mother]) * (1 - parent_gene_probs[father])
        elif num_genes == 1:
            # Probability of inheriting gene from one parent
            gene_number_probability = (1 - parent_gene_probs[mother]) * parent_gene_probs[father] + parent_gene_probs[mother] * (1 - parent_gene_probs[father])
        else:
            # Probability of inheriting gene from both parents
            gene_number_probability = parent_gene_probs[mother] * parent_gene_probs[father]

    return gene_number_probability * trait_probability


def joint_probability(people, one_genes_set, two_genes_set, have_trait_set):
    """
    Compute and return a joint probability.
    The probability returned should be the probability that
        * everyone in set `one_genes_set` has one copy of the gene, and
        * everyone in set `two_genes_set` has two copies of the gene, and
        * everyone not in `one_genes_set` or `two_genes_set` does not have the gene, and
        * everyone in set `have_trait_set` has the trait, and
        * everyone not in set` have_trait_set` does not have the trait.
    """
    # Initialize the probability to 1
    probability = 1

    # Loop through each person
    for person in people:

        # Calculate the probability of gene number and trait status for this person
        prob_person = probability_for_person(person, one_genes_set, two_genes_set, have_trait_set)

        # Multiply the probability for this person to the overall probability
        probability *= prob_person

    return probability


def update(probabilities, one_gene, two_genes, have_trait, p):
    """
    Update `probabilities` with a new joint probability `p`.
    """
    for person, person_probs in probabilities.items():
        # Update the gene distribution of the person
        if person in one_gene:
            person_probs["gene"][1] += p
        elif person in two_genes:
            person_probs["gene"][2] += p
        else:
            person_probs["gene"][0] += p

        # Update the trait distribution of the person
        has_trait = person in have_trait
        person_probs["trait"][has_trait] += p
        person_probs["trait"][not has_trait] += 0


def normalize(probabilities):
    """
    Update `probabilities` such that each probability distribution
    is normalized (i.e., sums to 1, with relative proportions the same).
    """
    for person in probabilities:

        # sum all values from the gene set
        genes = sum(probabilities[person]["gene"].values())

        # there are only three options, 0, 1, or 2 genes
        for i in range(0, 3):
            probabilities[person]["gene"][i] /= genes

        traits = sum(probabilities[person]["trait"].values())

        # there are only two options, 0 or 1 (False of True)
        for i in range(0, 2):
            probabilities[person]["trait"][i] /= traits


if __name__ == "__main__":
    main()
