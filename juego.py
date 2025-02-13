import pygame
import pygame_menu
import locale
from time import sleep
import random
from os.path import abspath, dirname
import conectar_postgreSQL as con

# Inicialización de Pygame
pygame.init()
locale.setlocale(locale.LC_ALL, '')
# base de path
BASE_PATH = abspath(dirname(__file__))
FONT_PATH = BASE_PATH + "/fonts/"
IMAGE_PATH = BASE_PATH + "/imagenes/"

# fondo de la ventana
imagen_fondo = pygame.image.load(IMAGE_PATH + 'fondo.jpg')
# cambiar icono
programIcon = pygame.image.load(IMAGE_PATH + 'ico.webp')
pygame.display.set_icon(programIcon)

SCREEN_WIDTH, SCREEN_HEIGHT = 626, 547
# Inicialización de la superficie de dibujo
ventana = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Taximetro")


pay_parado = con.sql_select('precios', 'parado')  
pay_movimiento = con.sql_select('precios', 'marcha')

def action():
    x , y = 0 , 0
    # cargar precios

    # Carga de la imagen del taxi
    taxi = pygame.image.load(IMAGE_PATH +'taxi.png')
    taxi = pygame.transform.scale(taxi, (100, 62))
    obstaculo = pygame.image.load(IMAGE_PATH + 'coche.png')
    obstaculo = pygame.transform.scale(obstaculo, (100, 62))
    # Obtengo el rectángulo del objeto anterior
    taxirect = taxi.get_rect()

    # valores para fuente de texto
    #pygame_menu.font.Font(FONT_PATH + 'DS-DIGI.TTF', 9)
    pygame.font.Font(FONT_PATH + 'DS-DIGI.TTF', 9)
    fuente = pygame.font.Font(FONT_PATH + 'DS-DIGI.TTF', 54)

    # Pongo el taxi ta en el origen de coordenadas
    taxirect.move_ip(240,400)

    # Bucle principal del juego
    playing = True
    x_obstaculo = -100
    y_obstaculo = random.randint(400, 470)
    while playing:
        x_obstaculo += 1
        x -= 0.01
        # Comprobamos los eventos
        #Comprobamos si se ha pulsado el botón de cierre de la ventana
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                playing = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            taxirect = taxirect.move(-3,0)
            x+=1
        elif keys[pygame.K_RIGHT]:
            taxirect = taxirect.move(3,0)
            x-=1
        elif keys[pygame.K_UP]:
            taxirect = taxirect.move(0,-3)
        elif keys[pygame.K_DOWN]:
            taxirect = taxirect.move(0,3)

       
        # Compruebo si el taxi llega a los límites "es la calle y los bordes de la ventana"
        
        if taxirect.right > ventana.get_width():
            taxirect = taxirect.move(-3,0)
            x-=1
        if taxirect.left < 0:
            taxirect = taxirect.move(3,0)
            x+=1
        if taxirect.top < 400:
            taxirect = taxirect.move(0,3)
        if taxirect.bottom > ventana.get_height() - 40:
            taxirect = taxirect.move(0,-3)
        
        # Movimiento del fondo
        x_relativa = x % imagen_fondo.get_rect().width
        ventana.blit(imagen_fondo, (x_relativa - imagen_fondo.get_rect().width, y))
        if x_relativa < SCREEN_WIDTH:
            ventana.blit(imagen_fondo, (x_relativa, 0))
        # Movimiento del obstáculo
        if x_obstaculo > ventana.get_width():
            x_obstaculo = -100
            y_obstaculo = random.randint(400, 470)

        obstaculo_rect = obstaculo.get_rect()
        obstaculo_rect.move_ip(x_obstaculo, y_obstaculo)
        #ventana.blit(imagen_fondo, (0, 0))
        # texto para la ventana
        texto_estado = fuente.render("Estado: Sin inciar", True, (125,125,125))
        texto_tarifa = fuente.render("Tarifa: Taximetro", True, (125,125,125))
        #texto_rect = texto_tarifa.get_rect()
        
        ventana.blit(texto_tarifa, [400, 10])
        ventana.blit(texto_estado, [10, 10])
        ventana.blit(obstaculo, obstaculo_rect)
        # Dibujo la taxi
        ventana.blit(taxi, taxirect)
        #obstaculo_ancho, obstaculo_alto = obstaculo.top_left
        
        # Compruebo si el taxi choca con el obstáculo
        if taxirect.colliderect(obstaculo_rect):
            if taxirect.y +5 < obstaculo_rect.y or taxirect.y  < obstaculo_rect.y -160:
                x -= 1
                x_obstaculo -= 1
                taxirect = taxirect.move(+3,0)
                
        # Todos los elementos del juego se vuelven a dibujar
        pygame.display.flip()
        # Controlamos la frecuencia de refresco (FPS)
        pygame.time.Clock().tick(60)
        

def mainMenu():
    surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    menu = pygame_menu.Menu('Bienvenido', 400, 300, theme=pygame_menu.themes.THEME_BLUE)
    menu.add.button('Precios', None)
    menu.add.button(f'Parado {locale.currency(pay_parado, grouping=True)}, Marcha {locale.currency(pay_movimiento, grouping=True)}', None)
    menu.add.button('Nuevo trayecto', action)
    #menu.add_button('About', about_function)
    menu.add.button('Salir', pygame_menu.events.EXIT)
    menu.mainloop(surface)

mainMenu()

# Salimos de Pygame
#pygame.quit()