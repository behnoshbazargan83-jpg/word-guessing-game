import random
words = {
    "animals": ["lion","tiger","monky","bee"],
    "fruits" : ["pineapple","orange","cucumber","avocado"],
    "colors" : ["yellow","blue","red","violet"],
    "misc" : ["phone","glass","bag","pillow"],
}

def pick_words():
    category = random.choice(["animals","fruits","colors","misc"])
    word = random.choice(words[category])
    return category,word

def creat_display(gessed , word):
        display = ""
        for d in word:
            if d in gessed:
                display += d

            else:
                display += "_"
        return display
def count_letter(word):
    if word == "":
        return 0

    else:
        return 1 + count_letter(word[1:])

def make_score_keaper():
    score = 0 
    
    def score_die(point):
        nonlocal score

        score += point
        return score

    return score_die

def show_massage(*line , **option):
    sep = option.get("sep" , "\n")
    border = option.get("border" , "_" *20)
    print(border)
    print(sep.join(line))
    print(border)

add_score= make_score_keaper()
total_game = 0

def play_round():
    global total_game
    total_game += 1
    category,word = pick_words()
    gessed = []
    lives = 6
    print("number game:", total_game)
    print (category , count_letter(word))

         

    while lives > 0 :
        display = creat_display(gessed , word)
        print(display , "| lives:", lives)


        if "_" not in display:
            print("you won!")
            all = add_score(lives * 10)
            print("all_socre:" , all)

            break
    
        gess = input("enter a letter:").lower()

        if len(gess) != 1 or not gess.isalpha():
            print("enter one letter ho!")
            continue 

        if gess in gessed:
            print("alredy gessd that!")
            continue

        gessed.append(gess)

        if gess not in word:
            lives -=1

    if lives ==0:
        print("you lost! the word was :" , word)


def mian():
    while True:
        play_round()
        answer = input("you wanna play again? (y\n)").lower()
        if answer != "y":
            break
        show_massage("goodbay! it was great game bro!")


mian()

        








