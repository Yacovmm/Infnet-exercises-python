import pygame
import psutil

pygame.init()
pygame.display.set_caption("--tp4 Projeto YacovR.--")
size = width, heitgh = 800, 600

screen = pygame.display.set_mode(size)

black = (0, 0, 0)
white = (255, 255, 255)
yellow = (255, 255, 0)
blue = (0, 0, 255)
red = (220, 20, 60)
green = (34, 139, 34)

# todo:  Create surface
s_mem = pygame.surface.Surface((800, 200))

s1 = pygame.surface.Surface((width, heitgh/3))
s2 = pygame.surface.Surface((width, heitgh/3))
s3 = pygame.surface.Surface((width, heitgh/3))
#
# pygame.draw.rect(s1, blue, (20, 50, width-2*20, 70))
# screen.blit(s1, (0, 0))
# pygame.draw.rect(s2, blue, (20, 50, width-2*20, 70))
# screen.blit(s2, (0, heitgh/3))
# pygame.draw.rect(s3, blue, (20, 50, width-2*20, 70))
# screen.blit(s3, (0, 2*heitgh/3))

pygame.display.init()

# todo: clock
clock = pygame.time.Clock()
# todo: initializing font
pygame.font.init()
font = pygame.font.Font(None, 32)
fontGrande = pygame.font.Font(None, 50)


def main():
    done = True
    cont = 60
    while done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = False
        if cont == 60:
            show_memory_use()
            show_disc_use()
            cont = 0

        pygame.display.update()
        clock.tick(60)
        cont += 1

    pygame.quit()


# todo : Mostrar uso de memória
def show_memory_use():
    mem = psutil.virtual_memory()
    larg = width - 2 * 20
    s1.fill(black)
    pygame.draw.rect(s1, blue, (20, 50, larg, 70))
    larg = larg * mem.percent / 100
    pygame.draw.rect(s1, red, (20, 50, larg, 70))
    mem_text = str(mem.percent) + '%'
    txt = fontGrande.render(mem_text, 1, white)
    s1.blit(txt, (25, 70 / 2 + 25))
    total = round(mem.total / (1024 * 1024 * 1024), 2)
    texto_barra = "Uso de Memória (Total: " + str(total) + "GB):"
    text = font.render(texto_barra, 1, white)
    s1.blit(text, (20, 10))
    screen.blit(s1, (0,0))


def show_disc_use():
    disco = psutil.disk_usage('.')
    larg = width - 2 * 20
    s2.fill(black)
    pygame.draw.rect(s2, blue, (20, 50, larg, 70))
    larg = larg * disco.percent / 100
    pygame.draw.rect(s2, red, (20, 50, larg, 70))
    total = round(disco.total / (1024 * 1024 * 1024), 2)
    texto_barra = "Uso de Disco: (Total: " + str(total) + "GB):"
    text = font.render(texto_barra, 1, white)
    s2.blit(text, (20, 10))
    screen.blit(s2,(0, heitgh/3))


if __name__ == '__main__':
    main()
