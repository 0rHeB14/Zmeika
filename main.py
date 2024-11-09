import pygame
import random

# Настройки игры
WIDTH, HEIGHT = 600, 400
CELL_SIZE = 20
WHITE, GREEN, RED, BLUE = (255, 255, 255), (0, 255,
                                            0), (255, 0, 0), (0, 0, 255)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Змейка - Собери 10 артефактов")
clock = pygame.time.Clock()

# Начальные параметры змейки
snake_pos = [[100, 50]]
snake_direction = "RIGHT"
artifact_count = 0

# Создание артефакта в случайной позиции


def place_artifact():
    return [random.randrange(1, WIDTH // CELL_SIZE) * CELL_SIZE,
            random.randrange(1, HEIGHT // CELL_SIZE) * CELL_SIZE]


artifact_pos = place_artifact()

# Основной цикл игры
game_over = False
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_direction != "DOWN":
                snake_direction = "UP"
            elif event.key == pygame.K_DOWN and snake_direction != "UP":
                snake_direction = "DOWN"
            elif event.key == pygame.K_LEFT and snake_direction != "RIGHT":
                snake_direction = "LEFT"
            elif event.key == pygame.K_RIGHT and snake_direction != "LEFT":
                snake_direction = "RIGHT"

    # Движение змейки
    if snake_direction == "UP":
        new_head = [snake_pos[0][0], snake_pos[0][1] - CELL_SIZE]
    elif snake_direction == "DOWN":
        new_head = [snake_pos[0][0], snake_pos[0][1] + CELL_SIZE]
    elif snake_direction == "LEFT":
        new_head = [snake_pos[0][0] - CELL_SIZE, snake_pos[0][1]]
    elif snake_direction == "RIGHT":
        new_head = [snake_pos[0][0] + CELL_SIZE, snake_pos[0][1]]

    # Добавляем новую голову и проверяем, подобрали ли артефакт
    snake_pos.insert(0, new_head)
    if abs(snake_pos[0][0] - artifact_pos[0]) < CELL_SIZE and abs(snake_pos[0][1] - artifact_pos[1]) < CELL_SIZE:
        artifact_count += 1
        artifact_pos = place_artifact()
    else:
        snake_pos.pop()  # Убираем хвост, если не съели артефакт

    # Проверка на победу
    if artifact_count == 10:
        print("Поздравляем, вы собрали все артефакты!")
        game_over = True

    # Проверка столкновений со стенами и собой
    if (snake_pos[0][0] < 0 or snake_pos[0][0] >= WIDTH or
        snake_pos[0][1] < 0 or snake_pos[0][1] >= HEIGHT or
            snake_pos[0] in snake_pos[1:]):
        print("Игра окончена!")
        game_over = True

    # Отображение игры
    screen.fill(WHITE)
    for segment in snake_pos:
        pygame.draw.rect(screen, GREEN, pygame.Rect(
            segment[0], segment[1], CELL_SIZE, CELL_SIZE))
    pygame.draw.rect(screen, RED, pygame.Rect(
        artifact_pos[0], artifact_pos[1], CELL_SIZE, CELL_SIZE))

    pygame.display.flip()
    clock.tick(10)

pygame.quit()
