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


def joint_probability(people, one_genes, two_genes, have_trait):
    """
    Compute and return a joint probability.

    The probability returned should be the probability that
        * everyone in set `one_genes` has one copy of the gene, and
        * everyone in set `two_genes` has two copies of the gene, and
        * everyone not in `one_genes` or `two_genes` does not have the gene, and
        * everyone in set `have_trait` has the trait, and
        * everyone not in set` have_trait` does not have the trait.

    Args:
        people (dict): A dictionary mapping person names to their parent information.
        one_genes (set): A set of people who have one copy of the gene.
        two_genes (set): A set of people who have two copies of the gene.
        have_trait (set): A set of people who have the trait.

    Returns:
        The joint probability.
    """

    probability = 1

    for person in people:
        gene_number = 0
        if person in one_genes:
            gene_number = 1
        elif person in two_genes:
            gene_number = 2

        trait = person in have_trait

        # If this person has no parents, use probability distribution
        if not people[person]['mother']:
            probability *= PROBS['gene'][gene_number] * PROBS['trait'][gene_number][trait]
        else:
            # Info about parents is available
            mother = people[person]['mother']
            father = people[person]['father']
            percentages = {}

            for parent in [mother, father]:
                parent_gene_number = 0
                if parent in one_genes:
                    parent_gene_number = 1
                elif parent in two_genes:
                    parent_gene_number = 2

                percentages[parent] = (
                    PROBS['mutation'] if parent_gene_number == 0 else
                    0.5 if parent_gene_number == 1 else
                    1 - PROBS['mutation']
                )

            # Calculate the person's gene number based on their parents' gene numbers.
            if gene_number == 0:
                # Probability of not inheriting gene from either parent
                prob_no_gene = (1 - percentages[mother]) * (1 - percentages[father])
                probability *= prob_no_gene
            elif gene_number == 1:
                # Probability of inheriting gene from one parent
                prob_one_gene = (1 - percentages[mother]) * percentages[father] + percentages[mother] * (1 - percentages[father])
                probability *= prob_one_gene
            else:
                # Probability of inheriting gene from both parents
                prob_two_genes = percentages[mother] * percentages[father]
                probability *= prob_two_genes

            # Multiply the probability by the trait probability.
            probability *= PROBS['trait'][gene_number][trait]

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
