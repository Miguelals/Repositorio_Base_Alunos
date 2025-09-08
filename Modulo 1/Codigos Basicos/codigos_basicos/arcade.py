import pygame
import random
import sys

# Inicialização
pygame.init()
LARGURA, ALTURA = 800, 600
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Jogo de Sobrevivência Avançado")

# Cores
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
VERDE = (50, 200, 50)
VERMELHO = (200, 50, 50)
AZUL = (50, 50, 200)
AMARELO = (255, 255, 0)
LARANJA = (255, 165, 0)

# Fonte
fonte = pygame.font.SysFont("arial", 28)

# FPS
clock = pygame.time.Clock()
FPS = 60

# Classes do jogo

class Jogador(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((40, 50))
        self.image.fill(AZUL)
        self.rect = self.image.get_rect(center=(LARGURA//2, ALTURA//2))
        self.velocidade = 5
        self.hp_max = 100
        self.hp = self.hp_max
        self.ataque = 20
        self.pontos = 0
        self.ataque_temporario = 0
        self.ataque_buff_tempo = 0

    def update(self, teclas):
        if teclas[pygame.K_w] and self.rect.top > 0:
            self.rect.y -= self.velocidade
        if teclas[pygame.K_s] and self.rect.bottom < ALTURA:
            self.rect.y += self.velocidade
        if teclas[pygame.K_a] and self.rect.left > 0:
            self.rect.x -= self.velocidade
        if teclas[pygame.K_d] and self.rect.right < LARGURA:
            self.rect.x += self.velocidade

        # Atualiza buff ataque
        if self.ataque_buff_tempo > 0:
            self.ataque_buff_tempo -= 1
        else:
            self.ataque_temporario = 0

    @property
    def ataque_total(self):
        return self.ataque + self.ataque_temporario

    def atacar(self, inimigos):
        # Ataca inimigos na área frontal (retângulo à direita do jogador)
        ataque_area = pygame.Rect(self.rect.right, self.rect.top, 30, self.rect.height)
        atingidos = []
        for inimigo in inimigos:
            if ataque_area.colliderect(inimigo.rect):
                dano = max(0, self.ataque_total - inimigo.defesa + random.randint(-2, 2))
                inimigo.hp -= dano
                atingidos.append((inimigo, dano))
        return atingidos

class Inimigo(pygame.sprite.Sprite):
    def __init__(self, tipo):
        super().__init__()
        self.tipo = tipo
        self.image = pygame.Surface((40, 40))
        if tipo == 1:
            self.image.fill(VERMELHO)
            self.hp = 50
            self.velocidade = 2
            self.ataque = 10
            self.defesa = 3
            self.pontos = 10
        elif tipo == 2:
            self.image.fill(LARANJA)
            self.hp = 80
            self.velocidade = 1
            self.ataque = 20
            self.defesa = 5
            self.pontos = 20
        elif tipo == 3:
            self.image.fill(AMARELO)
            self.hp = 40
            self.velocidade = 3
            self.ataque = 7
            self.defesa = 2
            self.pontos = 15

        self.rect = self.image.get_rect()
        # Spawn na borda aleatória
        self.rect.x = random.choice([0, LARGURA - self.rect.width])
        self.rect.y = random.randint(0, ALTURA - self.rect.height)

    def update(self, jogador):
        if self.hp <= 0:
            return
        # Movimento simples: perseguir jogador
        if jogador.rect.x > self.rect.x:
            self.rect.x += self.velocidade
        elif jogador.rect.x < self.rect.x:
            self.rect.x -= self.velocidade

        if jogador.rect.y > self.rect.y:
            self.rect.y += self.velocidade
        elif jogador.rect.y < self.rect.y:
            self.rect.y -= self.velocidade

class Tiro(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((10, 5))
        self.image.fill(BRANCO)
        self.rect = self.image.get_rect(center=(x, y))
        self.velocidade = 10

    def update(self):
        self.rect.x += self.velocidade
        if self.rect.x > LARGURA:
            self.kill()

class Item(pygame.sprite.Sprite):
    def __init__(self, tipo):
        super().__init__()
        self.tipo = tipo
        self.image = pygame.Surface((30, 30))
        if tipo == 'pocao':
            self.image.fill(VERDE)
        elif tipo == 'ataque':
            self.image.fill(AMARELO)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, LARGURA - self.rect.width)
        self.rect.y = random.randint(0, ALTURA - self.rect.height)

def desenha_texto(texto, x, y, cor=BRANCO):
    img = fonte.render(texto, True, cor)
    tela.blit(img, (x, y))

def tela_inicial():
    tela.fill(PRETO)
    desenha_texto("Jogo de Sobrevivência Avançado", LARGURA//2 - 200, ALTURA//2 - 100, BRANCO)
    desenha_texto("Use WASD para mover", LARGURA//2 - 110, ALTURA//2 - 50, BRANCO)
    desenha_texto("Espaço para atacar com espada", LARGURA//2 - 180, ALTURA//2 - 20, BRANCO)
    desenha_texto("F para atirar", LARGURA//2 - 50, ALTURA//2 + 10, BRANCO)
    desenha_texto("Pressione ENTER para começar", LARGURA//2 - 170, ALTURA//2 + 60, BRANCO)
    pygame.display.flip()

    esperando = True
    while esperando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RETURN:
                    esperando = False

def pause():
    desenha_texto("PAUSE - Pressione P para continuar", LARGURA//2 - 180, ALTURA//2, BRANCO)
    pygame.display.flip()
    pausado = True
    while pausado:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_p:
                    pausado = False
        clock.tick(10)

def game_over_screen(pontos):
    tela.fill(PRETO)
    desenha_texto("GAME OVER!", LARGURA//2 - 80, ALTURA//2 - 50, VERMELHO)
    desenha_texto(f"Pontos: {pontos}", LARGURA//2 - 60, ALTURA//2, BRANCO)
    desenha_texto("Pressione R para reiniciar ou ESC para sair", LARGURA//2 - 210, ALTURA//2 + 50, BRANCO)
    pygame.display.flip()

    esperando = True
    while esperando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_r:
                    esperando = False
                elif evento.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

def main():
    tela_inicial()

    jogador = Jogador()
    inimigos = pygame.sprite.Group()
    tiros = pygame.sprite.Group()
    itens = pygame.sprite.Group()

    # Spawn inicial de inimigos
    for _ in range(5):
        tipo = random.choice([1, 2, 3])
        inimigos.add(Inimigo(tipo))

    # Spawn inicial de itens
    for _ in range(2):
        tipo = random.choice(['pocao', 'ataque'])
        itens.add(Item(tipo))

    todos_sprites = pygame.sprite.Group()
    todos_sprites.add(jogador)
    todos_sprites.add(inimigos)
    todos_sprites.add(itens)

    rodando = True
    while rodando:
        clock.tick(FPS)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_SPACE:
                    # Ataque corpo a corpo
                    inimigos_atingidos = jogador.atacar(inimigos)
                    for inimigo, dano in inimigos_atingidos:
                        print(f"Atingiu {inimigo.tipo} e causou {dano} de dano!")
                        if inimigo.hp <= 0:
                            jogador.pontos += inimigo.pontos
                            inimigo.kill()
                    if not inimigos_atingidos:
                        print("Ataque não acertou ninguém.")
                elif evento.key == pygame.K_f:
                    # Atira projétil
                    tiro = Tiro(jogador.rect.right, jogador.rect.centery)
                    tiros.add(tiro)
                    todos_sprites.add(tiro)
                elif evento.key == pygame.K_p:
                    pause()

        teclas = pygame.key.get_pressed()
        jogador.update(teclas)
        inimigos.update(jogador)
        tiros.update()

        # Colisão tiros x inimigos
        for tiro in tiros:
            colidiu = pygame.sprite.spritecollide(tiro, inimigos, False)
            if colidiu:
                for inimigo in colidiu:
                    dano = max(0, jogador.ataque_total - inimigo.defesa + random.randint(-3, 3))
                    inimigo.hp -= dano
                    if inimigo.hp <= 0:
                        jogador.pontos += inimigo.pontos
                        inimigo.kill()
                tiro.kill()

        # Colisão jogador x inimigos (dano)
        if pygame.sprite.spritecollideany(jogador, inimigos):
            jogador.hp -= 1
            if jogador.hp <= 0:
                rodando = False

        # Colisão jogador x itens
        itens_coletados = pygame.sprite.spritecollide(jogador, itens, True)
        for item in itens_coletados:
            if item.tipo == 'pocao':
                jogador.hp = min(jogador.hp + 40, jogador.hp_max)
            elif item.tipo == 'ataque':
                jogador.ataque_temporario = 15
                jogador.ataque_buff_tempo = FPS * 5  # 5 segundos de buff

            jogador.pontos += 10

        # Spawn aleatório de inimigos e itens
        if random.random() < 0.01 and len(inimigos) < 10:
            inimigos.add(Inimigo(random.choice([1, 2, 3])))
            todos_sprites.add(inimigos.sprites()[-1])

        if random.random() < 0.005 and len(itens) < 5:
            novo_item = Item(random.choice(['pocao', 'ataque']))
            itens.add(novo_item)
            todos_sprites.add(novo_item)

        tela.fill(PRETO)
        todos_sprites.draw(tela)

        # Barra de HP do jogador
        pygame.draw.rect(tela, VERMELHO, (10, 10, 200, 25))
        hp_porcentagem = jogador.hp / jogador.hp_max
        pygame.draw.rect(tela, VERDE, (10, 10, 200 * hp_porcentagem, 25))

        desenha_texto(f"Pontos: {jogador.pontos}", 10, 45, AMARELO)
        if jogador.ataque_buff_tempo > 0:
            desenha_texto("Buff de ataque ativo!", 10, 75, AZUL)

        pygame.display.flip()

    game_over_screen(jogador.pontos)
    main()  # reinicia o jogo

if __name__ == "__main__":
    main()
