import numpy as np


def get_blocking_entity_at_location(entities, destination_x, destination_y):
    # Check if Entity is "Blocking" at X, Y Location Specified
    for entity in entities:
        if entity.blocks and entity.position.x == destination_x and entity.position.y == destination_y:
            return entity

    return None


def get_blocking_entities_at_location(entities, target_x, target_y, origin_x, origin_y, attack_types):
    # print('\nget_blocking_entities_at_location')
    opposite_x = target_x - origin_x
    opposite_y = target_y - origin_y
    # print(opposite_x, opposite_y)

    # targetable_positions = [(origin_x - opposite_x - 1, origin_y - opposite_y - 1),
    #                         (origin_x - opposite_x - 1, origin_y - opposite_y    ),
    #                         (origin_x - opposite_x - 1, origin_y - opposite_y + 1),
    #                         (origin_x - opposite_x + 1, origin_y - opposite_y - 1),
    #                         (origin_x - opposite_x + 1, origin_y - opposite_y    ),
    #                         (origin_x - opposite_x + 1, origin_y - opposite_y + 1),
    #                         (origin_x - opposite_x    , origin_y - opposite_y - 1),
    #                         (origin_x - opposite_x    , origin_y - opposite_y + 1)]
    targetable_positions = [(origin_x - 1, origin_y - 1),
                            (origin_x - 1, origin_y    ),
                            (origin_x - 1, origin_y + 1),
                            (origin_x + 1, origin_y - 1),
                            (origin_x + 1, origin_y    ),
                            (origin_x + 1, origin_y + 1),
                            (origin_x    , origin_y - 1),
                            (origin_x    , origin_y + 1)]

    # (3) Tile
    # targetable_positions = [(origin_x + opposite_x, origin_y + opposite_y),
    #                         (origin_x + opposite_x, origin_y             ),
    #                         (origin_x             , origin_y + opposite_y)]


    if (origin_x, origin_y) in targetable_positions:
        targetable_positions.remove((origin_x, origin_y))

    # print('\norigin_x, origin_y:', origin_x, origin_y)
    # print('targetable_positions:', targetable_positions)

    # Check if Entity is "Blocking" at X, Y Location Specified
    main_target = None
    targetable_entities = []
    for entity in entities:

        # Place Main Target to front
        if entity.blocks and (entity.position.x, entity.position.y) == (target_x, target_y):
            main_target = entity
            continue

        if entity.blocks and (entity.position.x, entity.position.y) in targetable_positions:
            targetable_entities.append(entity)
            targetable_positions.remove((entity.position.x, entity.position.y))

    if not main_target:
        return [], targetable_entities

    # Return targetted entities and all rest of tiles
    return [main_target] + targetable_entities, targetable_positions


def get_map_object_at_location(map_objects, destination_x, destination_y):
    # Check if Object is "Blocking" at X, Y Location Specified
    for map_object in map_objects:
        if map_object.position.x == destination_x and map_object.position.y == destination_y:
            return map_object
    return None
