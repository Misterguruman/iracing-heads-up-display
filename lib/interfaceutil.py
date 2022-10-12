import pygame
import lib.colors as colors

#Initialize various rect sizes
window_size = window_width, window_height = 800, 800
tire_info_size = tire_info_width, tire_info_height = 420, 760
extra_info_size = extra_info_width, extra_info_height = 320, 100

#Initalize positions of panes
tire_info_position = tire_info_left, tire_info_top = 20, 20
pedal_info_position = pedal_info_left, pedal_info_top = 460, 20
rpm_info_position = rpm_info_left, rpm_info_top = 460, 140 
spacial_info_position = spacial_info_left, spacial_info_top = 460, 260

#Create pygame Rect Objects
tire_info_pane = pygame.Rect(tire_info_position, (tire_info_width, tire_info_height))
pedal_info_pane = pygame.Rect(pedal_info_position, extra_info_size)
rpm_info_pane = pygame.Rect(rpm_info_position, extra_info_size)
spacial_info_pane = pygame.Rect(spacial_info_position, extra_info_size)

def renderUI(surface):
    surface.fill(colors.BLACK)
  
    pygame.draw.rect(surface, colors.GRAY, tire_info_pane)
    pygame.draw.rect(surface, colors.GRAY, pedal_info_pane)
    pygame.draw.rect(surface, colors.GRAY, rpm_info_pane)
    pygame.draw.rect(surface, colors.GRAY, spacial_info_pane)

def renderPedalGraph(surface, throttle, brake):
    throttle_points = [((x * 2 + pedal_info_pane.left) , pedal_info_pane.bottom - throttle[x]) for x in range(len(throttle[0:161]))]
    brake_points = [((x * 2 + pedal_info_pane.left) , pedal_info_pane.bottom - brake[x]) for x in range(len(brake[0:161]))]
    pygame.draw.lines(surface, colors.GREEN, False, throttle_points, 3)
    pygame.draw.lines(surface, colors.RED1, False, brake_points, 3)

def renderRPM(surface, rpm, font):
    gauge = pygame.Rect(rpm_info_position, (extra_info_width * (rpm / 8000), rpm_info_pane.height))

    if rpm < 5000:
        pygame.draw.rect(surface, colors.GREEN, gauge )
    elif rpm < 7000:
        pygame.draw.rect(surface, colors.YELLOW1, gauge)
    else:
        pygame.draw.rect(surface, colors.RED1, gauge)

    text = font.render(str(rpm), True, colors.WHITE, colors.BLACK)
    textRect = text.get_rect()
    textRect.center = rpm_info_pane.center

    surface.blit(text, textRect)

def renderSpacialPosition(surface):
    pygame.draw.lines(surface, colors.WHITE, False, [(spacial_info_pane.left + 110, spacial_info_pane.center[1]), (spacial_info_pane.left + 150, spacial_info_pane.center[1]), (spacial_info_pane.left + 160, spacial_info_pane.center[1] + 15), (spacial_info_pane.left + 170, spacial_info_pane.center[1]), (spacial_info_pane.left + 210, spacial_info_pane.center[1])], 3)
    