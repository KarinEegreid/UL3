import pygame  # Impordime pygame.

# Käivitame pygame
pygame.init()

# värvid
red = [255, 0, 0]  # Punane värv
lGreen = [153, 255, 153]  # Hele roheline värv

# Ekraani seaded
screen = pygame.display.set_mode((640, 480))  # Ekraani parameetrite seadmine
pygame.display.set_caption("Karl Paju IS22 ÜL3")  # Ekraanile nime andmine
screen.fill(lGreen)  # Paigaldab ekraanile helerohelise värvi


# Funktsioon ruutude joonistamiseks

def draw_squares(size, rows, columns, color): # Funktsioon võtab 4 sisendit: suurus, read, veerud ja ruutude värv.
    for row in range(rows):  # See kasutab pesastatud loopi, et luua soovitud arv ruutude ridu ja veerge.
        for column in range(columns): # on for-loop, mis kordub läbi kindlaksmääratud veergude vahemiku.
            square = pygame.Rect(column * size, row * size, size, size)  # Iga ruut luuakse kindla suuruse ja asukohaga.
            pygame.draw.rect(screen, color, square, 1) # Funktsioon joonistab iga ruudu ekraanile määratud värvi ja äärise laiusega.


# Loopi loomine
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Joonistab ruudud ekraanile sisestatud parameetritega ning värviga
    draw_squares(20, 24, 32, (red))

    pygame.display.update()  # uuendab ekraani

# Sulgeb pygame.
pygame.quit()
