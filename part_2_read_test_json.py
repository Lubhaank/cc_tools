import test_data
import json

#Creates and returns a GameLibrary object(defined in test_data) from loaded json_data
def make_game_library_from_json( json_data ):
    #Initialize a new GameLibrary
    game_library = test_data.GameLibrary()

    ### Begin Add Code Here ###

    #Loop through the json_data

    for game_data in json_data["games"]:


        game = test_data.Game()
        platform = test_data.Platform()

        platform.name = game_data["platform"]["name"]
        platform.launch_year = game_data["platform"]["launch_year"]

        game.platform = platform
        game.year = game_data["year"]
        game.title = game_data["title"]


        
        game_library.add_game(game)
    

    return game_library


#Part 2
input_json_file = "data/test_data.json"


with open(input_json_file, "r") as reader:

    test_json = json.load(reader)

test_data = make_game_library_from_json(test_json)

print(test_data)

