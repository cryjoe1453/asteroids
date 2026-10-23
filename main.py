from constants import(
SCREEN_WIDTH,
SCREEN_HEIGHT,
)
from logger import log_state
import pygame

def main() -> None:
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0.0
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        pygame.display.flip()
        dt = clock.tick(60) / 1000

    print(
        f"Starting Asteroids with pygame version: {pygame.version.ver} \n"
        f"Screen width: {SCREEN_WIDTH} \n"
        f"Screen height: {SCREEN_HEIGHT}"
    )

if __name__ == "__main__":
    main()
