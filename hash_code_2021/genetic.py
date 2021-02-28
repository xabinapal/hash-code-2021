import logging
import random

from hash_code_2021 import Scheduler

MUTATION_PROBABILITY = 0.2


def should_mutate(mutation_probability):
    return random.random() <= mutation_probability


def create_population(scheduler, population, mutation_probability, car_count):
    source = scheduler.serialize()
    creatures = list()

    for _ in range(population):
        schedule = dict()
        for intersection, data in source.items():
            phenotype = list()
            for streets in data:
                genotype = [streets[0], streets[1]]

                if should_mutate(mutation_probability):
                    genotype[1] = random.randint(0, car_count)

                phenotype.append(genotype)

            if should_mutate(mutation_probability):
                random.shuffle(phenotype)

            schedule[intersection] = phenotype

        creatures.append(Scheduler.deserialize(schedule))

    return creatures


def combine_phenotypes(a, b, mutation_probability, car_count):
    schedule = dict()

    a = a.serialize()
    b = b.serialize()

    for intersection in a.keys():
        phenotype = list()
        for idx in range(len(a[intersection])):
            genotype = (
                a[intersection][idx]
                if random.randint(0, 1) == 1
                else b[intersection][idx]
            )

            if should_mutate(mutation_probability):
                genotype[1] = random.randint(0, car_count)

            phenotype.append(genotype)

        schedule[intersection] = phenotype

    if should_mutate(mutation_probability):
        random.shuffle(phenotype)

    return Scheduler.deserialize(schedule)


def modify_population(creatures, mutation_probability, car_count):
    new_population = list()

    for _ in range(len(creatures)):
        phenotype_a = random.choice(creatures)
        phenotype_b = random.choice(creatures)

        new_population.append(
            combine_phenotypes(
                phenotype_a, phenotype_b, mutation_probability, car_count
            )
        )

    return new_population


def execute(
    simulator, population, iterations, creatures, mutation_probability, car_count
):
    best_score = 0
    best_scheduler = None

    for iteration in range(iterations):
        logging.info("Iteration: #%d" % (iteration + 1,))

        idx = 0
        for phenotype in creatures:
            logging.info(
                "Simulating with scheduler %d: %s"
                % (
                    idx + 1,
                    phenotype.serialize(),
                )
            )

            score = simulator.execute(phenotype)

            if score > best_score:
                best_score = score
                best_scheduler = phenotype

            idx += 1

        creatures = modify_population(creatures, mutation_probability, car_count)

    logging.info("Best score: %d" % (best_score,))
    logging.info("Population: %s" % (best_scheduler.serialize(),))

    return best_score, best_scheduler
