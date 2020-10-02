#same as original
import random
from functools import reduce
from operator import concat

#Additional functionality

def return_list_of_txt_files_in_path(username, category_path):
    user_folder = username
    pack_paths_file = './' + user_folder + category_path
    pack_paths_list = open(pack_paths_file, 'r').read().splitlines()
    return pack_paths_list

def turn_list_of_files_into_list_of_their_contents(user_category_txtlist):
    contents_lists = []
    for i in user_category_txtlist:
        one_pack_file = i
        one_pack_list = open(one_pack_file, 'r').read().splitlines()
        contents_lists.append(one_pack_list)
    return contents_lists
    
def flatten_list(nested_list):

    flat_list = []
    for sublist in nested_list:
        for item in sublist:
            flat_list.append(item)
    return flat_list 


#A lot of these variables will be replaced by functions later. I'll eventually add
#the ability for the user to choose their packs. This will generate files and file paths,
# which is also where some of the variables will come from.
# Right now, the packs are just assigned to the user by hand.

user = input('who is playing? try abc, lotus, kid, or nsfw')

opponents_path = '/opponents/opponents_paths.txt'
contests_path = '/contests/contests_paths.txt'

user_opponents_txtlist = return_list_of_txt_files_in_path(user, opponents_path)
user_contests_txtlist = return_list_of_txt_files_in_path(user, contests_path)

opponents_nested = turn_list_of_files_into_list_of_their_contents(user_opponents_txtlist)
contests_nested = turn_list_of_files_into_list_of_their_contents(user_contests_txtlist)

opponents = flatten_list(opponents_nested)
contests2 = flatten_list(contests_nested)


turn_list_of_files_into_list_of_their_contents(user_opponents_txtlist)

def random_ages(min_age=1, max_age=101):
    while True:
        yield random.randint(min_age, max_age)

def random_fighters(fighters):
    while True:
        yield random.choice(fighters)

def random_contests(contests):
    while True:
        yield random.choice(contests)

def get_fight(fighter_a, fighter_a_age, fighter_b, fighter_b_age, contest):
    return reduce(concat, [
        'Who would win in ',
        contest,
        ', a ',
        str(fighter_a_age),
        '-year-old ',
        fighter_a,
        ' or a ',
        str(fighter_b_age),
        '-year-old ',
        fighter_b,
        '?'
    ])

if __name__ == '__main__':
    # Must be phrased to fit syntax, "a 40-year old ____"
    fighters = opponents

    # Must be phrased to fit syntax, "Who would win in ____"
    contests = contests2

    fighters = random_fighters(fighters)
    contests = random_contests(contests)
    ages = random_ages()

    while True:
        print(get_fight(
            fighter_a       = next(fighters),
            fighter_a_age   = next(ages),
            fighter_b       = next(fighters),
            fighter_b_age   = next(ages),
            contest         = next(contests),
        ))

        if input("Run again? y/n: ").lower() != "y":
            print("Goodbye.")
            break
