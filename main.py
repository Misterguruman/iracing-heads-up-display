import sys, pygame, irsdk, math
import lib.colors as colors
import lib.interfaceutil as interface


if __name__ == "__main__":
    pygame.init()
    clock = pygame.time.Clock()
    ir = irsdk.IRSDK()
    ir.startup()

    previous_throttle = 0
    previous_brake = 0
    
    throttle_line = []
    brake_line = []
    
    screen = pygame.display.set_mode(interface.window_size)
    pygame.display.set_caption('Heads Over Display')

    font = pygame.font.Font('freesansbold.ttf', 48)

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()

        throttle_line.insert(0, int(ir['Throttle'] * 100))
        brake_line.insert(0, int(ir["BrakeRaw"] * 100))

        interface.renderUI(screen)

        if len(throttle_line) > 3:
            interface.renderPedalGraph(screen, throttle_line, brake_line)

        interface.renderRPM(screen, round(ir["RPM"]), font)
        

        interface.renderSpacialPosition(screen, round(math.degrees(ir["Pitch"]), 5) * 25)
        pygame.display.update()
        dt = clock.tick(60)


 

        