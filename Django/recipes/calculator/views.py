from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}


def dish_view(request, dish):
    if dish == 'omlet':
        number = int(request.GET.get('servings', 1))
        context = {
            "recipe": {item: num * number for item, num in DATA['omlet'].items()}
        }
        return render(request, 'calculator/index.html', context)
    elif dish == 'pasta':
        number = int(request.GET.get('servings', 1))
        context = {
            "recipe": {item: round(num * number, 2) for item, num in DATA['pasta'].items()}
        }
        return render(request, 'calculator/index.html', context)
    elif dish == 'buter':
        number = int(request.GET.get('servings', 1))
        context = {
            "recipe": {item: num * number for item, num in DATA['buter'].items()}
        }
        return render(request, 'calculator/index.html', context)

