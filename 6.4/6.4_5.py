import matplotlib.pyplot as plt


def strength(diagram_type, color, **kwargs):
    animals = list(kwargs.keys())
    strengths = list(kwargs.values())
    plt.figure()
    if diagram_type == 'barh':
        plt.barh(animals, strengths, color=color)
    elif diagram_type == 'bar':
        plt.bar(animals, strengths, color=color)
    plt.title('Strength')
    plt.xlabel('Strength') if diagram_type == 'bar' else plt.ylabel('Strength')
    plt.savefig('result.png')
    plt.close()