import pygame
import psutil
import cpuinfo

pygame.init()
pygame.display.set_caption("--tp5 Projeto YacovR.--")
size = width, heitgh = 800, 600

screen = pygame.display.set_mode(size)
# todo:  Obtém informações da CPU
info_cpu = cpuinfo.get_cpu_info()
cpuList = psutil.cpu_percent(interval=1, percpu=True)

black = (0, 0, 0)
white = (255, 255, 255)
yellow = (255, 255, 0)
blue = (0, 0, 255)
red = (220, 20, 60)
green = (34, 139, 34)

# todo:  Create surface
s_mem = pygame.surface.Surface((800, 200))

s1 = pygame.surface.Surface((width, heitgh / 4))
s2 = pygame.surface.Surface((width, heitgh / 4))
s3 = pygame.surface.Surface((width, heitgh / 4))
s4 = pygame.surface.Surface((width, heitgh / 4))
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
            mostra_info_cpu()
            mostra_uso_cpu(s4, cpuList)
            cont = 0

        pygame.display.update()
        clock.tick(60)
        cont += 1

    pygame.quit()


# todo : Mostrar uso de cpu
def mostra_uso_cpu(s, l_cpu_percent):
    s.fill(green)
    num_cpu = len(l_cpu_percent)
    x = y = 10
    desl = 10
    alt = s.get_height() - 2 * y
    larg = (s.get_width() - 2 * y - (num_cpu + 1) * desl) / num_cpu
    d = x + desl
    for i in l_cpu_percent:
        pygame.draw.rect(s, red, (d, y, larg, alt))
        pygame.draw.rect(s, black, (d, y, larg, (1 - i / 100) * alt))
        d = d + larg + desl
    # parte mais abaixo da tela e à esquerda
    screen.blit(s, (0, heitgh / 4 *2))


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
    screen.blit(s1, (0, 0))


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
    screen.blit(s2, (0, heitgh / 4))


def mostra_info_cpu():
    s3.fill(black)
    mostra_texto(s3, "Nome:", "brand", 10)
    mostra_texto(s3, "Arquitetura:", "arch", 30)
    mostra_texto(s3, "Palavra (bits):", "bits", 50)
    mostra_texto(s3, "Frequência (MHz):", "freq", 70)
    mostra_texto(s3, "Núcleos (físicos): ", "nucleos", 90)
    dic_interfaces = psutil.net_if_addrs()
    # ip
    screen.blit(s3, (0, heitgh / 4 * 3))


# todo: Mostra texto de acordo com uma chave:
def mostra_texto(sn, nome, chave, pos_y):
    text = font.render(nome, True, white)
    sn.blit(text, (10, pos_y))
    if chave == "freq":
        s = str(round(psutil.cpu_freq().current, 2))
    elif chave == "nucleos":
        s = str(psutil.cpu_count())
        s = s + " (" + str(psutil.cpu_count(logical=False)) + ")"
    else:
        s = str(info_cpu[chave])
    text = font.render(s, True, white)
    sn.blit(text, (240, pos_y))


if __name__ == '__main__':
    main()
