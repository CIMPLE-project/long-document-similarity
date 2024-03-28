import matplotlib.pyplot as plt
import numpy as np
from statistics import mean


def plot_claim_distribution(claim_distribution, list_of_chunk_indeces, save=True, color='green', figure_size=(30, 10),
                            font_size=15):
    plt.figure(figsize=figure_size)
    dist = [int(x) for x in claim_distribution]
    graph = plt.hist(dist, rwidth=0.95, bins=range(len(list_of_chunk_indeces) + 1), color=color)
    plt.xticks(range(len(list_of_chunk_indeces)))
    for i in range(len(list_of_chunk_indeces) - 1):
        plt.text(graph[1][i], graph[0][i], str(graph[0][i]))
    plt.title('Number of claims found for each chunk', fontsize=font_size)
    if save is True:
        plt.savefig('claim_distribution.png')
    plt.show()


def create_y_matrix(selected_claim_indeces, found_information, chunk_indeces):
    y_array = []
    for ind in selected_claim_indeces:
        data = [(int(ci[3]), ci[0]) for ci in filter(lambda ci: ci[1] == ind, found_information)]

        for i in range(len(chunk_indeces)):
            if not any(filter(lambda d: d[0] == i, data)):
                data.append((i, 0))
        data = sorted(data, key=lambda d: d[0])

        y = [d[1] for d in data]
        y_array.append(y)

    return np.array(y_array)


def get_scores_from_claim_id(claim_id, found_information, list_of_chunk_indeces):
    data = [(int(ci[3]), ci[0]) for ci in filter(lambda ci: ci[1] == claim_id, found_information)]

    for i in range(len(list_of_chunk_indeces)):
        if not any(filter(lambda d: d[0] == i, data)):
            data.append((i, 0))

    data = sorted(data, key=lambda d: d[0])
    y = [d[1] for d in data]
    return np.array(y)


def plot_claim_appearances(y_values, list_of_chunk_indeces, claim_id=None, save=True, figure_size=(30, 10),
                           font_size=12):
    plt.figure(figsize=figure_size)
    plt.stem(list_of_chunk_indeces, y_values)
    plt.xticks(list_of_chunk_indeces)
    for x, y in zip(list_of_chunk_indeces, y_values):
        plt.annotate(y, xy=(x, y), xytext=(0, 5), textcoords='offset points', ha='center', fontsize=font_size)
    if claim_id is not None:
        plt.title('Claim ID number %s'%claim_id, fontsize=font_size+3)
    if save is True:
        plt.savefig('claim_appearances.png')
    plt.show()


def plot_average_chunk_scores(list_of_chunk_indeces, found_information, topn=3, save=True, color='green', figure_size=(30, 10),
                              font_size=15):
    mean_chunk_scores = []
    for chunk_id in list_of_chunk_indeces:
        y = [chi[0] for chi in filter(lambda chi: int(chi[3]) == chunk_id, found_information)]
        y = sorted(y, reverse=True)
        y = [y[i] if len(y) > i else 0 for i in range(topn)]
        y_mean = round(mean(y), 4)
        mean_chunk_scores.append(y_mean)

    plt.figure(figsize=figure_size)
    graph = plt.bar(list_of_chunk_indeces, mean_chunk_scores, color=color)
    plt.xticks(list_of_chunk_indeces)
    plt.bar_label(graph)
    plt.title('Normalized average cosine similarity score of top N claims for each chunk', fontsize=font_size)
    if save is True:
        plt.savefig('average_chunk_scores.png')
    plt.show()
