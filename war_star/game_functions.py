import sys
import  pygame

def update_screen(ai_settings,screen,ship):
    """更新屏幕图像，并切换到新屏幕"""
    #每次循环都要重绘屏幕
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    #让最近绘制的屏幕可见
    pygame.display.flip()

def check_events(ship):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,ship)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

def check_keydown_events(event,ship):
        if event.key == pygame.K_RIGHT:
            ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            ship.moving_left = True
def check_keyup_events(event,ship):
        if event.key == pygame.K_RIGHT:
            ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            ship.moving_left = False