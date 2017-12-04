import pygame
import sys
import maps
import camera
import car
import random
import traffic_lamp
import barrier
from button import AddBarrierButton
from loader import load_image
from pygame.locals import *


class FuzzyCarApp():
    def __init__(self):
        pygame.init()
        self.tick_index = 0
        self.screen = pygame.display.set_mode((1200, 600))
        pygame.display.set_caption('Car Race Fuzzy Controller.')
        pygame.mouse.set_visible(True)
        font = pygame.font.Font(None, 24)

        # CENTER_W = int(pygame.display.Info().current_w / 2)
        # CENTER_H = int(pygame.display.Info().current_h / 2)

        # new background surface
        self.background = pygame.Surface(self.screen.get_size())
        # print(background)
        self.background = self.background.convert_alpha(self.background)
        self.background.fill((82, 86, 94))

        self.clock = pygame.time.Clock()
        self.running = True
        self.pause = False
        # game_font = pygame.font.Font(None, 24)
        self.cam = camera.Camera()
        # controlled_car = car.Car(600, 350, 270)
        self.map_s = pygame.sprite.Group()
        self.map = maps.Map(0, 0)
        self.map_s.add(self.map)

        bottom_right_screen = (1200, 600)
        barrier_btn_group_topleft = \
            (bottom_right_screen[0] - 200, bottom_right_screen[1] - 200)
        # add barrier buttons
        self.buttons = pygame.sprite.Group()
        self.add_far_barrier_btn = AddBarrierButton(
            AddBarrierButton.FAR,
            barrier_btn_group_topleft[0],
            barrier_btn_group_topleft[1],
            "Add far barrier")
        self.add_medium_barrier_btn = AddBarrierButton(
            AddBarrierButton.MEDIUM,
            barrier_btn_group_topleft[0],
            barrier_btn_group_topleft[1] + 60,
            "Add medium barrier")
        self.add_near_barrier_btn = AddBarrierButton(
            AddBarrierButton.NEAR,
            barrier_btn_group_topleft[0],
            barrier_btn_group_topleft[1] + 120,
            "Add near barrier")

        self.buttons.add(self.add_near_barrier_btn)
        self.buttons.add(self.add_far_barrier_btn)
        self.buttons.add(self.add_medium_barrier_btn)

        self.cars = pygame.sprite.Group()
        self.controlled_car = car.Car(600, 350, 270)
        self.cars.add(self.controlled_car)

        self.traffic_lamps = pygame.sprite.Group()

        traffic_lamp1 = traffic_lamp.TrafficLamp(line_index=random.randint(5,10), distance=50, dir=90)
        traffic_lamp2 = traffic_lamp.TrafficLamp(line_index=random.randint(11,15), distance=20, dir=90)
        traffic_lamp3 = traffic_lamp.TrafficLamp(line_index=random.randint(26,29), distance=10, dir=90)
        traffic_lamp4 = traffic_lamp.TrafficLamp(line_index=random.randint(20,25), distance=10, dir=90)

        self.traffic_lamps.add(traffic_lamp1)
        self.traffic_lamps.add(traffic_lamp2)
        self.traffic_lamps.add(traffic_lamp3)
        self.traffic_lamps.add(traffic_lamp4)

        self.barriers = pygame.sprite.Group()
        # test_barrier = barrier.Barrier(1742, 462, remaining_time=4000)
        # self.barriers.add(test_barrier)

        self.cam.set_pos(self.controlled_car.x, self.controlled_car.y)

    def main(self):
        controlled_car = self.controlled_car
        running = True
        # getTicksLastFrame = pygame.time.get_ticks()
        while running:
            self.tick_index += 1
            # if self.tick_index % 120 == 0:
            #     print(self.tick_index % 120)
            #     pass
            # print('running!')
            keys = pygame.key.get_pressed()
            # print(controlled_car.find_way_direction())
            # # print(controlled_car.current_nav_index)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    break  # break out of the for loop
                if event.type == pygame.KEYUP:
                    if keys[K_r]:
                        self.pause = False
                    if keys[K_p]:
                        self.pause = True
                        # sys.exit(0)
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
                    if pressed1:  # left click
                        # print("left click")
                        pos = pygame.mouse.get_pos()
                        print("clicked!: "+  str(pos[0])+' - '+str(pos[1]))
                        print('current cam pos: '+str(self.cam.x)+' - '+str(self.cam.y))
                        for add_barrier_btn in self.buttons:
                            pass
                            if add_barrier_btn.is_clicked(pos[0], pos[1]) and \
                                            len(self.barriers) == 0:
                                # print(add_barrier_btn.type)
                                rand_barrier_index, rand_line_distance, rand_barrier_pos = \
                                    self.map.find_random_barrier_pos(
                                        add_barrier_btn.type,
                                        self.controlled_car.current_line_index,
                                        (self.controlled_car.x,
                                         self.controlled_car.y))

                                # self.pause = True
                                if rand_barrier_pos is not None:
                                    pass
                                    new_barrier = barrier.Barrier(
                                        rand_barrier_index,
                                        rand_line_distance,
                                        rand_barrier_pos[0],
                                        rand_barrier_pos[1],
                                        remaining_time=600
                                    )
                                    self.barriers.add(new_barrier)

            self.cam.set_pos(controlled_car.x, controlled_car.y)
            # print(str(cam.x)+" : "+str(cam.y))
            # draw background
            self.screen.blit(self.background, (0, 0))

            # update map and render map
            self.map_s.update(self.cam.x, self.cam.y)
            self.map_s.draw(self.screen)

            self.buttons.update(self.cam.x, self.cam.y)
            self.buttons.draw(self.screen)
            for game_button in self.buttons:
                game_button.render_text(self.screen)

            # update and render traffic lamps
            self.traffic_lamps.update(self.cam.x, self.cam.y)
            # self.traffic_lamps.draw(self.screen)
            for lamp in self.traffic_lamps:
                lamp.render(self.screen)

            # update and render traffic lamps
            for road_barrier in self.barriers:
                if road_barrier.remaining_time == 0:
                    self.barriers.remove(road_barrier)
            self.barriers.update(self.cam.x, self.cam.y)
            self.barriers.draw(self.screen)
            for road_barrier in self.barriers:
                road_barrier.render_text(self.screen)
            # update and render cars
            self.cars.update(self.cam.x, self.cam.y, self)
            # print(cam.x, cam.y)
            self.cars.draw(self.screen)

            # finish render
            pygame.display.flip()

            # t = pygame.time.get_ticks()
            # deltaTime in seconds.
            # deltaTime = (t - getTicksLastFrame) / 1000.0
            # getTicksLastFrame = t
            # print(deltaTime)
            self.clock.tick(60)


if __name__ == "__main__":
    # initialization
    # Enter the mainloop.
    app = FuzzyCarApp()
    app.main()
    pygame.quit()
    sys.exit(0)
