#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
    temp=[]#Store number of batches of each available ingredients
    for item,amount_needed in recipe.items():#Go through recipe keys and values
        if item not in ingredients:#Check for keys are present in ingredients given
          return 0
        min_amount = ingredients[item] // amount_needed #Compute the no. of batches
        if min_amount == 0:#if ingredients are lacking, exit
          return 0
        if min_amount > 0:#if there is enough ingredients to make parts of recipe, save min amount
          temp.append(min_amount)
    return min(temp)#return of least min amount of batches possible to be made


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))