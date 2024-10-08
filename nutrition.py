def main():

    item = input("Item: ").lower()

    fruits = {"apple": 130,
              "avocado": 50,
              "banana": 110,
              "cantaloupe": 50,
              "grapefruit": 60,
              "grapes": 90,
              "honeydew melon": 50,
              "kiwifruit": 90,
              "lemon": 15,
              "lime": 20,
              "nectarine": 60,
              "orange": 80,
              "peach": 60,
              "pear": 100,
              "pineapple": 50,
              "plums": 70,
              "sweet cherries": 100,
              "tangerine": 50,
              "watermelon": 80
    }

    if item in fruits.keys():
        print(f"Calories: {fruits[item]}")


if __name__=="__main__":
    main()
