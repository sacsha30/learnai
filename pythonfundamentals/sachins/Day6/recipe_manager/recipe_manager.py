import os
import sys
from pathlib import Path

a_list = []

def welcome():
    print('Welcome!')

def dir_info():
    recipe_dir = Path(Path.cwd(),'Recipes')
    print(f'{count_recipes()} recipes are located at {recipe_dir}')

def count_recipes():
    counter = 0
    recipes_dir = Path(Path.cwd(),'Recipes')
    for file in recipes_dir.glob('**/*.txt'):
        counter += 1
    return counter

def display_options():
    options = '''
    1. View Recipe
    2. Create Recipe
    3. Generate Category
    4. Delete Recipe
    5. Delete Category
    6. Exit'''
    return options

def process_selected_option(selected_option):
    if selected_option == 1:
        view_recipe()
    elif selected_option == 2:
        create_recipe()
    elif selected_option == 3:
        create_category()
    elif selected_option == 4:
        delete_recipe()
    elif selected_option == 5:
        delete_category()
    elif selected_option == 6:
        exit_program()
    else:
        print('Wrong option! Please try again!')

def display_categories():
    recipes_dir = Path(Path.cwd(),'Recipes')
    categories = os.listdir(recipes_dir)
    categories_str = ''
    for index, category in enumerate(categories):
        categories_str += f'{index + 1}. {category}\n'
    return categories_str

def choose_category():
    selected_category = input('Please choose a category: \n'+display_categories())
    return selected_category

def display_recipes(category):
    recipes_dir = Path(Path.cwd(),'Recipes',category)
    recipes = [file.stem for file in recipes_dir.iterdir()]
    recipes_str = ''
    for index, recipe in enumerate(recipes):
        recipes_str += f'{index + 1}. {recipe}\n'
    return recipes_str

def choose_recipe(category):
    selected_recipe = input('Please choose a recipe: \n'+display_recipes(category))
    return selected_recipe

def view_recipe():
    selected_category = choose_category()
    selected_recipe = choose_recipe(selected_category)
    recipe_file = Path(Path.cwd(),'Recipes',selected_category,selected_recipe+'.txt')
    file = open(recipe_file,'r')
    print(file.read())

def create_recipe():
    selected_category = choose_category()
    recipe_name = input('Enter your recipe name: \n')
    recipe_content = input('Enter your recipe content: \n')
    recipe_file = Path(Path.cwd(),'Recipes',selected_category,recipe_name+'.txt')
    file = open(recipe_file,'w')
    file.write(recipe_content)
    file.close()
    print('Recipe created successfully!')

def create_category():
    category_name = input('Enter your category name: \n')
    os.mkdir(Path(Path.cwd(),'Recipes',category_name))
    print('Category created successfully!')

def delete_recipe():
    selected_category = choose_category()
    recipe_name = input('Enter recipe name to be deleted: \n')
    os.remove(Path(Path.cwd(),'Recipes',selected_category,recipe_name+'.txt'))
    print('Recipe deleted successfully!')

def delete_category():
    selected_category = choose_category()
    os.removedirs(Path(Path.cwd(),'Recipes',selected_category))
    print('Category deleted successfully!')

def exit_program():
    sys.exit('Goodbye!')

def main():
    while True:
        welcome()
        dir_info()
        selected_option = input('Choose an option to continue: \n'+display_options()+'\n')
        process_selected_option(int(selected_option))
        continue_status = input('Do you want to continue (y/n)... \n')
        if continue_status == 'n':
            exit_program()

main()

