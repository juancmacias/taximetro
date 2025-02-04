import pygame
# Inicialización de Pygame
pygame.init()
# fondo de la ventana
imagen_fondo = pygame.image.load("imagenes/fondo.jpg")
# cambiar icono
programIcon = pygame.image.load('imagenes/ico.webp')
pygame.display.set_icon(programIcon)
# Inicialización de la superficie de dibujo
ventana = pygame.display.set_mode((626,547))
pygame.display.set_caption("Taximetro")


def jugar():
    # Carga de la imagen del taxi
    taxi = pygame.image.load("imagenes/taxi.png")
    taxi = pygame.transform.scale(taxi, (100, 62))
    # Obtengo el rectángulo del objeto anterior
    taxirect = taxi.get_rect()
    # valores para fuente de texto
    fuente = pygame.font.Font(None, 36)

    # Pongo el taxi ta en el origen de coordenadas
    taxirect.move_ip(240,400)
    # Bucle principal del juego
    jugando = True
    while jugando:
        # Comprobamos los eventos
        #Comprobamos si se ha pulsado el botón de cierre de la ventana
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                jugando = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            taxirect = taxirect.move(-3,0)
        if keys[pygame.K_RIGHT]:
            taxirect = taxirect.move(3,0)
        if keys[pygame.K_UP]:
            taxirect = taxirect.move(0,-3)
        if keys[pygame.K_DOWN]:
            taxirect = taxirect.move(0,3)


        # Compruebo si el taxi llega a los límites "es la calle y los bordes de la ventana"
        if taxirect.right > ventana.get_width():
            taxirect = taxirect.move(-3,0)
        if taxirect.left < 0:
            taxirect = taxirect.move(3,0)
        if taxirect.top < 400:
            taxirect = taxirect.move(0,3)
        if taxirect.bottom > ventana.get_height() - 40:
            taxirect = taxirect.move(0,-3)

        ventana.blit(imagen_fondo, (0, 0))
        # texto para la ventana
        texto_estado = fuente.render("Estado: Sin inciar", True, (125,125,125))
        texto_tarifa = fuente.render("Tarifa: Taximetro", True, (125,125,125))
        #texto_rect = texto_tarifa.get_rect()
        
        ventana.blit(texto_tarifa, [400, 10])
        ventana.blit(texto_estado, [10, 10])
        # Dibujo la pelota
        ventana.blit(taxi, taxirect)
        # Todos los elementos del juego se vuelven a dibujar
        pygame.display.flip()
        # Controlamos la frecuencia de refresco (FPS)
        pygame.time.Clock().tick(60)

jugar()

# Salimos de Pygame
pygame.quit()