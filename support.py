from os import walk
import pygame


def import_folder(path):
    surface_list = []
    for _, __, image in walk(path):
        for name in image:
            full_path = path + '/' + name
            image_surf = pygame.image.load(full_path).convert_alpha()
            surface_list.append(image_surf)
    # print(surface_list)
    return surface_list

# print(import_folder('graphics/character/idle'))
