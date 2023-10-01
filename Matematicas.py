import pygame


def checaColisaoRaioRect(ray_origin, ray_dir, rec):

    print(ray_origin, ray_dir, rec)
    if ray_dir.x ==0 and ray_dir.y == 0:
        return (False,None,None)
    if ray_dir.x == 0:
        ray_dir.x = 0.000000001
    if ray_dir.y == 0:
        ray_dir.y = 0.0000000001
    inv_dir = pygame.Vector2(1/ray_dir.x,1/ray_dir.y)
    t_near = pygame.Vector2(((rec.x)-ray_origin.x)*inv_dir.x,(rec.y -ray_origin.y)*inv_dir.y)
    t_far   = pygame.Vector2( (rec.x + rec.width - ray_origin.x)*inv_dir.x, (rec.y + rec.height - ray_origin.y)*inv_dir.y )
    
    # certifica que o near é o mais proximo e o far o mais distante
    t_near.x, t_far.x = min(t_near.x, t_far.x),max(t_near.x, t_far.x)
    t_near.y, t_far.y = min(t_near.y, t_far.y),max(t_near.y, t_far.y)
    # verifica casos em que ele nunca vai colidir
    if t_near.x > t_far.y or t_near.y > t_far.x: return (False,None,None)

    # Find t of contact
    t_hit_near = max(t_near.x, t_near.y)
    t_hit_far  = min(t_far.x, t_far.y)

    # se ambos os fars forem negativos, ou seja eu ja passei
    if t_hit_far < 0: return (False,None,None) 

    # Find contact point
    pontoColisao = pygame.Vector2(ray_origin.x+ t_hit_near*ray_dir.x, ray_origin.y + t_hit_near*ray_dir.y )

    # Find normal
    if t_near.x >= t_near.y :
        normalColisao = pygame.Vector2(1,0) if (inv_dir.x < 0) else pygame.Vector2(-1,0)
    else:
        normalColisao = pygame.Vector2(0,1) if (inv_dir.y < 0) else pygame.Vector2(0,-1)

    return (t_hit_near >= 0 and t_hit_near < 1, normalColisao, pontoColisao)



def colisaoRectRect(jogador, retangulo):
    
    retanguloColisor = pygame.Rect(retangulo.x-0.5*jogador.width+jogador.velocidade.x, retangulo.y+jogador.velocidade.y+1 -0.5*jogador.height, retangulo.width+ jogador.width + jogador.velocidade.x, retangulo.height + jogador.height)
    pontoCentral = pygame.Vector2(jogador.x+jogador.width/2, jogador.y+jogador.height/2)
    velocidade = jogador.velocidade.copy()
    return checaColisaoRaioRect(pontoCentral, velocidade, retanguloColisor)