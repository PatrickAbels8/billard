import pygame
pygame.display.set_caption("Billard")
pygame.font.init()

HEIGHT = 600
WIDTH = 1200
FPS = 50

FONT = pygame.font.SysFont("arial", 20)

class Ball:
	pass


def draw_window(win):
	win.fill((0, 0, 0))
	pygame.display.update()

def main():
	clock = pygame.time.Clock()
	win = pygame,display.set_mode((WIDTH, HEIGHT))

	run = True
	while(run):
		clock.tick(FPS)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False

		draw_window(win)

	pygame.quit()

if __name__ == '__main__':
	main()