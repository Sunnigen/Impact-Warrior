import json
import os


def obtain_json_data(file_name=''):
    if file_name:
        file = "{}\\assets\\{}.json".format(os.getcwd(), file_name)
    else:
        file = "%s\\assets\\mobs.json" % os.getcwd()
    if not os.path.isfile(file):
        print('Cannot find %s!!!' % file)
        raise FileNotFoundError

    with open(file, "r", encoding="utf8") as read_file:
        data = json.load(read_file)

    return data


def obtain_mob_table(file_name=''):
    if file_name:
        mob_file = "{}\\assets\\{}.json".format(os.getcwd(), file_name)
    else:
        mob_file = "%s\\assets\\mobs.json" % os.getcwd()
    if not os.path.isfile(mob_file):
        print('Cannot find %s!!!' % mob_file)
        raise FileNotFoundError

    with open(mob_file, "r", encoding="utf8") as read_file:
        mob_table = json.load(read_file)

    # print('mob_table:', mob_table)
    return mob_table


def obtain_item_table():
    item_file = "%s\\assets\\items.json" % os.getcwd()
    if not os.path.isfile(item_file):
        print('Cannot locate %s!!!' % item_file)
        raise FileNotFoundError

    with open(item_file, "r", encoding="utf8") as read_file:
        item_table = json.load(read_file)

    # print('item_table:', item_table)
    return item_table


def obtain_tile_set(key_word=''):
    tile_set_file = "%s\\assets\\tile_set.json" % os.getcwd()

    if not os.path.isfile(tile_set_file):
        print('Cannot locate %s!!!' % tile_set_file)
        raise FileNotFoundError

    with open(tile_set_file, "r", encoding="utf8") as read_file:
        tile_set_table = json.load(read_file)

    # print('item_table:', item_table)
    return tile_set_table


def obtain_prefabs(key_word=''):
    prefab_file = "%s\\assets\\prefab.json" % os.getcwd()

    if not os.path.isfile(prefab_file):
        print('Cannot locate %s!!!' % prefab_file)
        raise FileNotFoundError

    with open(prefab_file, "r", encoding="utf8") as read_file:
        prefab_table = json.load(read_file)

    # print('prefab_table:', prefab_table)
    return prefab_table


def obtain_factions(key_word=''):
    faction_file = "%s\\assets\\faction.json" % os.getcwd()

    if not os.path.isfile(faction_file):
        print('Cannot locate %s!!!' % faction_file)
        raise FileNotFoundError

    with open(faction_file, "r", encoding="utf8") as read_file:
        faction_file  = json.load(read_file)

    # print('prefab_table:', prefab_table)
    return faction_file


def obtain_particles(key_word=''):
    particle_file = "%s\\assets\\particles.json" % os.getcwd()

    if not os.path.isfile(particle_file):
        print('Cannot locate %s!!!' % particle_file)
        raise FileNotFoundError

    with open(particle_file, "r", encoding="utf8") as read_file:
        particle_file = json.load(read_file)

    return particle_file


def obtain_spells(key_word=''):
    spell_file = "%s\\assets\\spells.json" % os.getcwd()

    if not os.path.isfile(spell_file):
        print('Cannot locate %s!!!' % spell_file)
        raise FileNotFoundError

    with open(spell_file, "r", encoding="utf8") as read_file:
        spell_file = json.load(read_file)

    return spell_file