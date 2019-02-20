import cc_dat_utils
import json
import cc_data
#Part 3
#Load your custom JSON file
#Convert JSON data to cc_data
#Save converted data to DAT file


def make_ccdat_from_json(json_data):

	cc_dat = cc_data.CCDataFile()


	for level in json_data["levels"]:


		cclevel = cc_data.CCLevel()

		cclevel.level_number = level["level_number"]
		cclevel.time = level["time"]
		cclevel.num_chips = level["chip_number"]
		cclevel.upper_layer = level["upper_layer"]
		cclevel.lower_layer = level["lower_layer"]


		for field in level["option_fields"]:

			if(field["type"] == 3):

				mapfield = cc_data.CCMapTitleField(field["title"])
				cclevel.add_field(mapfield)

			elif(field["type"] == 6):

				passwordfield = cc_data.CCEncodedPasswordField(field["password"])
				cclevel.add_field(passwordfield)

			elif(field["type"] == 7):

				hintfield = cc_data.CCMapHintField(field["hint"])
				cclevel.add_field(hintfield)

			elif(field["type"] == 10):

				monsters = []

				for coord in field["monsters"]:

					ccCoord = cc_data.CCCoordinate(coord[0], coord[1])
					monsters.append(ccCoord)

				monsterfield = cc_data.CCMonsterMovementField(monsters)
				cclevel.add_field(monsterfield)



			elif(field["type"] == 4):


				traps = []

				for trap in field["traps"]:

					coordsbutton = trap["button_coord"]
					coordstrap = trap["trap_coord"]

					cctrapcontrol = cc_data.CCTrapControl(coordsbutton[0],coordsbutton[1], coordstrap[0], coordstrap[1])
					traps.append(cctrapcontrol)

				trapfield = cc_data.CCTrapControlsField(traps)

				cclevel.add_field(trapfield)



			elif(field["type"] == 5):

				machines = []

				for machine in field["machines"]:

					coordsbutton = machine["button_coord"]
					coordsmachine = machine["machine_coord"]

					ccmachinecontrol = cc_data.CCCloningMachineControl(coordsbutton[0],coordsbutton[1], coordsmachine[0], coordsmachine[1])
					machines.append(ccmachinecontrol)

				machinesfield = cc_data.CCCloningMachineControlsField(machines)

				cclevel.add_field(machinesfield)

			else:

				continue


		cc_dat.add_level(cclevel)


	return cc_dat









input_json_file = "data/lubhaank_cc1.json"

with open(input_json_file, "r") as reader:

    ccdat_json = json.load(reader)

cc_data_all_levels = make_ccdat_from_json(ccdat_json)

output_dat_file = "data/lubhaank_cc1.dat"

cc_dat_utils.write_cc_data_to_dat(cc_data_all_levels, output_dat_file)
#print(cc_data_all_levels)