import pygame
import random
import time
from button import Button


class Game:
    def __init__(self):
        pygame.init()
        self.maxn = 50
        self.WIDTH, self.HEIGHT = 600, 600

        self.window = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Sorting Algorithm Visualized")

        self.ints = [random.randint(1, self.maxn) for i in range(self.maxn)]
        self.period = 100 # ms
        self.clock = pygame.time.Clock()

    def updateColumns(self, arr, redBlocks = [None]):

        self.clock.tick(60)

        self.window.fill("black")
        
        for i, num in enumerate(arr):
            color = (255, 255, 255)
            if i in redBlocks:
                color = (255, 0, 0)
            pygame.draw.rect(self.window, color, (i*self.WIDTH/self.maxn, num*self.HEIGHT*0.8/self.maxn, self.WIDTH/self.maxn, num*self.HEIGHT*0.8))

        pygame.display.update()

        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    raise SystemExit

    def insertionSort(self):
        
        arr = self.ints

        for i, val1 in enumerate(arr):
            j = i
            while j > 0 and arr[j-1] > arr[j]:
                temp = arr[j-1]
                arr[j-1] = arr[j]
                arr[j] = temp
                j = j - 1
                
                self.updateColumns(arr, [j])

    def selectionSort(self):

        arr = self.ints

        for i, val1 in enumerate(arr):
            minindex = i
            for j in range(i+1, len(arr)):
                if arr[minindex] > arr[j]:
                    minindex = j
            arr[i], arr[minindex] = arr[minindex], arr[i]

            pygame.time.wait(50)
            self.updateColumns(arr, [i for i in range(i, minindex)])

    def bubbleSort(self):
        sorted = False
        i = 0
        while not sorted:
            sorted = True
            for i in range(len(self.ints)):
                if i < len(self.ints) - 1:
                    if self.ints[i] > self.ints[i + 1]:
                        self.ints[i], self.ints[i + 1] = self.ints[i + 1], self.ints[i]
                        sorted = False

                        self.updateColumns(self.ints, [i])





    def mergeSort(self,arr, start, end):
        
        if len(arr) > 1:
            mid = len(arr)//2

            L = arr[:mid]
            R = arr[mid:]

            self.mergeSort(L, start, start+mid)
            self.mergeSort(R, start+mid, end)

            i = j = k = 0

            while i < len(L) and j < len(R):
                if L[i] <= R[j]:
                    arr[k] = L[i]
                    i += 1
                    self.updateColumns(self.ints, [start+i, start+mid+i])
                else:
                    arr[k] = R[j]
                    j += 1
                    self.updateColumns(self.ints, [start+j, start+mid+j])
                k += 1
            while i < len(L):
                arr[k] = L[i]
                i += 1
                k += 1
                self.updateColumns(self.ints, [start+i, start+mid+i])
            while j < len(R):
                arr[k] = R[j]
                j += 1
                k += 1
                self.updateColumns(self.ints, [start+j, start+mid+j])

            m = 0
            for l in range(start, end):
                self.ints[l] = arr[m]
                m += 1

    def draw_text(self, text, font, text_col):
        img = font.render(text, True, text_col)

        # centering text in the middle of the screen
        x1 = img.get_width()
        y1 = img.get_height()
        x = self.WIDTH//2 - x1//2
        y = self.HEIGHT // 2 - y1//2


        self.window.blit(img, (x, y))
            

    def run(self):
        
        chosen = False
        #self.insertionSort()
        #self.selectionSort()
        #self.bubbleSort()

        TEXT_COL = (0, 0, 255)
        font = pygame.font.SysFont("arial black", 40)

        merge_image = pygame.image.load("images/Button_merge.png").convert_alpha()
        selection_image = pygame.image.load("./images/Button_selection.png").convert_alpha()
        insertion_image = pygame.image.load("./images/Button_insertion.png").convert_alpha()
        bubble_image = pygame.image.load("./images/Button_bubble.png").convert_alpha()

        merge_button = Button(self.WIDTH//2 - 300*.3, 200*.3, merge_image, 0.3)
        selection_button = Button(self.WIDTH//2 - 300*.3, 100 + 200*.3, selection_image, 0.3)
        insertion_button = Button(self.WIDTH//2 - 300*.3, 200 + 200*.3, insertion_image, 0.3)
        bubble_button = Button(self.WIDTH//2 - 300*.3, 300 + 200*.3, bubble_image, 0.3)

        self.updateColumns(self.ints)

        finished = False
        while True:

            self.clock.tick(60)

            if not chosen:
                if not finished:
                    self.updateColumns(self.ints)
                    finished = True

                if merge_button.draw(self.window):
                    chosen = True
                    self.mergeSort(self.ints, 0, len(self.ints))
                if selection_button.draw(self.window):
                    chosen = True
                    self.selectionSort()
                if insertion_button.draw(self.window):
                    chosen = True
                    self.insertionSort()
                if bubble_button.draw(self.window):
                    chosen = True
                    self.bubbleSort()
                
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        raise SystemExit
                pygame.display.update()

            else:
                if finished:
                    self.updateColumns(self.ints)
                    finished = False
                self.draw_text("Press SPACE to play again", font, TEXT_COL)

                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            self.ints = [random.randint(1, self.maxn) for i in range(self.maxn)]
                            chosen = False
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        raise SystemExit

                pygame.display.update()



if __name__ == "__main__":

    game = Game()

    game.run()