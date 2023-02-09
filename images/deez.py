import pygame

pygame.init()

window = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Test")

deez = False
font = pygame.font.SysFont("arial black", 40)
TEXT_COL = (255, 255, 255)

def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    window.blit(img, (x, y))

while True:

    if deez:
        draw_text('1', font, TEXT_COL, 400, 400)
    else:
        draw_text('2', font, TEXT_COL, 400, 400)
    
    for event in pygame.event.get():
        print(event.type, pygame.K_2)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_2:
                deez = True
            if event.key == pygame.K_1:
                deez = False
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit

    pygame.display.update()