import pygame
from pygame.locals import *


class ChessGUI(object):

	def __init__(self, size):

		pygame.init()
		self.screenX = size
		self.screenY = size
		self.screen = pygame.display.set_mode((size, size))
		self.load_images()
		pygame.display.set_caption('Chess')
		self.play_gui()

		self.piece_paths = self.get_piece_paths()
		self.piece_images = self.load_images



	def draw_chess_board(self):

		for i in range(8):
			for j in range(8):

				if i%2 == 0:
					if j%2 == 0:
						self.screen.blit(self.darkSquare, (i*int(self.screenX/8), j*int(self.screenX/8)))

					else:
						self.screen.blit(self.lightSquare, (i*int(self.screenX/8), j*int(self.screenX/8)))

				elif i%2 != 0:
					if j%2 != 0:
						self.screen.blit(self.darkSquare, (i*int(self.screenX/8), j*int(self.screenX/8)))

					else:
						self.screen.blit(self.lightSquare, (i*int(self.screenX/8), j*int(self.screenX/8)))



	def draw_pieces(self, board):
		pass

	def draw_piece(self, symbol, x, y):


	def load_images(self):
		self.darkSquare = pygame.image.load('chess_assets/square_graydark.png')
		self.darkSquare = pygame.transform.scale(self.darkSquare, (int(self.screenX/8), int(self.screenY/8)))
		self.lightSquare = pygame.image.load('chess_assets/square_graylight.png')
		self.lightSquare = pygame.transform.scale(self.lightSquare, (int(self.screenX/8), int(self.screenY/8)))

		for key in self.piece_paths:



	def play_gui(self):
		# Variable to keep our main loop running
		running = True

		# Our main loop!
		while running:
		    # for loop through the event queue
		    for event in pygame.event.get():
		        # Check for KEYDOWN event; KEYDOWN is a constant defined in pygame.locals, which we imported earlier
		        if event.type == KEYDOWN:
		            # If the Esc key has been pressed set running to false to exit the main loop
		            if event.key == K_ESCAPE:
		                running = False
		        # Check for QUIT event; if QUIT, set running to false
		        elif event.type == QUIT:
		            running = False

		    self.draw_chess_board()
		    pygame.display.flip()


	def get_piece_paths(self):
		piece_paths = {}



chess_gui = ChessGUI(720)



