import pygame
import sys
import maps
import camera
import car
import traffic_lamp
from loader import load_image
from pygame.locals import *


def main():
    clock = pygame.time.Clock()
    running = True
    # game_font = pygame.font.Font(None, 24)
    cam = camera.Camera()
    # controlled_car = car.Car(600, 350, 270)
    controlled_car = car.Car(600, 350, 270)

    traffic_lamp1 = traffic_lamp.TrafficLamp(1300, 200, 90)
    traffic_lamp2 = traffic_lamp.TrafficLamp(2400, 560, 90)
    traffic_lamp3 = traffic_lamp.TrafficLamp(1600, 1050, 90)
    traffic_lamp4 = traffic_lamp.TrafficLamp(400, 1250, 90)

    map_s = pygame.sprite.Group()
    map_s.add(maps.Map(0, 0))

    cars = pygame.sprite.Group()
    cars.add(controlled_car)

    traffic_lamps = pygame.sprite.Group()
    traffic_lamps.add(traffic_lamp1)
    traffic_lamps.add(traffic_lamp2)
    traffic_lamps.add(traffic_lamp3)
    traffic_lamps.add(traffic_lamp4)

    # for e_car in cars:
    #     print(e_car.x)
    cam.set_pos(controlled_car.x, controlled_car.y)

    # getTicksLastFrame = pygame.time.get_ticks()
    while running:
        keys = pygame.key.get_pressed()
        # print(controlled_car.find_way_direction())
        # # print(controlled_car.current_nav_index)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break  # break out of the for loop
            if event.type == pygame.KEYUP:
                if keys[K_p]:
                    pass
                    # controlled_car.reset()
                    # target.reset()
                if keys[K_q]:
                    pygame.quit()
                    sys.exit(0)

            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False
                break

            # mouse events
            # pos = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pressed1, pressed2, pressed3 = pygame.mouse.get_pressed()
                if pressed1 or pressed2 or pressed3:
                    if pressed1:
                        print("left click")
                    if pressed2:
                        print("middle click")
                    if pressed3:
                        print("right click")
                pos = pygame.mouse.get_pos()
                print(pos)

                # Check for key input. (KEYDOWN, trigger often)
        # controlled_car.steerleft()
        # if target.timeleft > 0:
        if True:
            if keys[K_w]:
                controlled_car.set_speed(2)
            if keys[K_LEFT]:
                controlled_car.steerleft()
            if keys[K_RIGHT]:
                controlled_car.steerright()
            if keys[K_UP]:
                controlled_car.accelerate()
            if keys[K_SPACE]:
                controlled_car.stop()
            # else:
            #     controlled_car.soften()
            if keys[K_DOWN]:
                controlled_car.deaccelerate()

        cam.set_pos(controlled_car.x, controlled_car.y)
        # print(str(cam.x)+" : "+str(cam.y))
        # draw background
        screen.blit(background, (0, 0))

        # update map and render map
        map_s.update(cam.x, cam.y)
        map_s.draw(screen)


        # update and render traffic lamps
        traffic_lamps.update(cam.x, cam.y)
        traffic_lamps.draw(screen)
        for lamp in traffic_lamps:
            lamp.render(screen)

        # update and render cars
        cars.update(cam.x, cam.y)
        # print(cam.x, cam.y)
        cars.draw(screen)



        # finish render
        pygame.display.flip()

        # t = pygame.time.get_ticks()
        # deltaTime in seconds.
        # deltaTime = (t - getTicksLastFrame) / 1000.0
        # getTicksLastFrame = t
        # print(deltaTime)
        clock.tick(60)


if __name__ == "__main__":
    # initialization
    pygame.init()

    screen = pygame.display.set_mode((1200, 600))
    pygame.display.set_caption('Car Race Fuzzy Controller.')
    pygame.mouse.set_visible(True)
    font = pygame.font.Font(None, 24)

    CENTER_W = int(pygame.display.Info().current_w / 2)
    CENTER_H = int(pygame.display.Info().current_h / 2)

    # new background surface
    background = pygame.Surface(screen.get_size())
    # print(background)
    background = background.convert_alpha(background)
    background.fill((82, 86, 94))

    # Enter the mainloop.
    main()

    pygame.quit()
    sys.exit(0)
