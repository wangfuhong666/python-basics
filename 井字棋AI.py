import pygame
import sys

# 初始化pygame
pygame.init()

# 画面配置（保持和之前一致，操作无学习成本）
WINDOW_SIZE = 450
CELL_SIZE = WINDOW_SIZE // 3
LINE_COLOR = (100, 100, 100)
BG_COLOR = (240, 240, 240)
X_COLOR = (255, 69, 0)  # 玩家X（红色）
O_COLOR = (30, 144, 255)  # AI O（蓝色）
FONT = pygame.font.Font(None, 60)

# 1. 核心游戏逻辑（判断胜负、空位置、评估得分）
def is_winner(state, player):
    """判断当前玩家是否获胜"""
    lines = [
        [state[0][0], state[0][1], state[0][2]],
        [state[1][0], state[1][1], state[1][2]],
        [state[2][0], state[2][1], state[2][2]],
        [state[0][0], state[1][0], state[2][0]],
        [state[0][1], state[1][1], state[2][1]],
        [state[0][2], state[1][2], state[2][2]],
        [state[0][0], state[1][1], state[2][2]],
        [state[0][2], state[1][1], state[2][0]]
    ]
    return [player, player, player] in lines

def get_available_moves(state):
    """获取所有空位置（i,j）"""
    moves = []
    for i in range(3):
        for j in range(3):
            if state[i][j] is None:
                moves.append((i, j))
    return moves

def is_board_full(state):
    """判断棋盘是否下满"""
    return len(get_available_moves(state)) == 0

def evaluate(state):
    """评估当前棋盘得分：AI赢=10，玩家赢=-10，平局=0"""
    if is_winner(state, 'O'):
        return 10
    elif is_winner(state, 'X'):
        return -10
    else:
        return 0

# 2. 极小极大算法+α-β剪枝（完美策略核心）
def minimax(state, depth, is_maximizing, alpha, beta):
    """
    - is_maximizing: True=AI（O）选最优解（最大化得分），False=玩家（X）选最优解（最小化得分）
    - alpha: 最大化玩家的当前最优值，beta: 最小化玩家的当前最优值
    - 剪枝：当beta <= alpha时，无需遍历后续子节点，直接返回
    """
    score = evaluate(state)
    # 终止条件：分出胜负或棋盘满
    if score == 10 or score == -10:
        return score - depth  # 赢的越快，得分越高（鼓励速胜）
    if is_board_full(state):
        return 0

    if is_maximizing:
        max_score = -float('inf')
        # AI遍历所有空位置，找最大得分
        for move in get_available_moves(state):
            i, j = move
            state[i][j] = 'O'
            # 递归调用（切换为玩家回合）
            current_score = minimax(state, depth + 1, False, alpha, beta)
            state[i][j] = None  # 回溯：撤销落子
            max_score = max(max_score, current_score)
            alpha = max(alpha, current_score)
            if beta <= alpha:  # 剪枝：后续子节点无需遍历
                break
        return max_score
    else:
        min_score = float('inf')
        # 玩家遍历所有空位置，找最小得分
        for move in get_available_moves(state):
            i, j = move
            state[i][j] = 'X'
            # 递归调用（切换为AI回合）
            current_score = minimax(state, depth + 1, True, alpha, beta)
            state[i][j] = None  # 回溯：撤销落子
            min_score = min(min_score, current_score)
            beta = min(beta, current_score)
            if beta <= alpha:  # 剪枝：后续子节点无需遍历
                break
        return min_score

def best_move(state):
    """AI选择最优落子（基于极小极大算法）"""
    best_score = -float('inf')
    optimal_move = None
    # 遍历所有空位置，计算每个位置的得分
    for move in get_available_moves(state):
        i, j = move
        state[i][j] = 'O'
        current_score = minimax(state, 0, False, -float('inf'), float('inf'))
        state[i][j] = None  # 回溯：撤销落子
        # 选择得分最高的落子
        if current_score > best_score:
            best_score = current_score
            optimal_move = move
    return optimal_move

# 3. 可视化绘制函数（和之前一致，画面无变化）
def draw_board(screen, board):
    screen.fill(BG_COLOR)
    # 画棋盘线条
    for i in range(1, 3):
        pygame.draw.line(screen, LINE_COLOR, (0, i*CELL_SIZE), (WINDOW_SIZE, i*CELL_SIZE), 3)
        pygame.draw.line(screen, LINE_COLOR, (i*CELL_SIZE, 0), (i*CELL_SIZE, WINDOW_SIZE), 3)
    # 画X和O
    for i in range(3):
        for j in range(3):
            if board[i][j] == 'X':
                start1 = (j*CELL_SIZE + 50, i*CELL_SIZE + 50)
                end1 = ((j+1)*CELL_SIZE - 50, (i+1)*CELL_SIZE - 50)
                start2 = ((j+1)*CELL_SIZE - 50, i*CELL_SIZE + 50)
                end2 = (j*CELL_SIZE + 50, (i+1)*CELL_SIZE - 50)
                pygame.draw.line(screen, X_COLOR, start1, end1, 6)
                pygame.draw.line(screen, X_COLOR, start2, end2, 6)
            elif board[i][j] == 'O':
                center = (j*CELL_SIZE + CELL_SIZE//2, i*CELL_SIZE + CELL_SIZE//2)
                pygame.draw.circle(screen, O_COLOR, center, CELL_SIZE//2 - 50, 6)

def draw_text(screen, text, color, y_offset=0):
    text_surface = FONT.render(text, True, color)
    text_rect = text_surface.get_rect(center=(WINDOW_SIZE//2, WINDOW_SIZE//2 + y_offset))
    screen.blit(text_surface, text_rect)

# 4. 主游戏逻辑（可视化交互）
def play_hard_tic_tac_toe():
    screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
    pygame.display.set_caption("井字棋 AI（高难度·完美策略）")
    clock = pygame.time.Clock()
    board = [[None for _ in range(3)] for _ in range(3)]
    game_over = False
    ai_thinking = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # 玩家落子（鼠标点击空位置）
            if event.type == pygame.MOUSEBUTTONDOWN and not game_over and not ai_thinking:
                x, y = pygame.mouse.get_pos()
                j = x // CELL_SIZE  # 列（0-2）
                i = y // CELL_SIZE  # 行（0-2）
                if 0 <= i < 3 and 0 <= j < 3 and board[i][j] is None:
                    board[i][j] = 'X'
                    # 判断玩家是否获胜
                    if is_winner(board, 'X'):
                        game_over = True
                        winner_text = "你赢了！（真厉害！）"
                    elif is_board_full(board):
                        game_over = True
                        winner_text = "平局！（AI完美防守）"
                    else:
                        ai_thinking = True  # AI开始思考最优落子

        # AI最优落子（极小极大算法）
        if ai_thinking and not game_over:
            ai_move = best_move(board)
            board[ai_move[0]][ai_move[1]] = 'O'
            # 判断AI是否获胜
            if is_winner(board, 'O'):
                game_over = True
                winner_text = "AI赢了！"
            elif is_board_full(board):
                game_over = True
                winner_text = "平局！（AI完美防守）"
            ai_thinking = False

        # 绘制画面
        draw_board(screen, board)
        if ai_thinking:
            draw_text(screen, "AI思考中...", (150, 150, 150), -50)
        if game_over:
            color = (0, 200, 0) if "赢了" in winner_text else (255, 0, 0)
            draw_text(screen, winner_text, color, 50)
            draw_text(screen, "点击关闭窗口", (100, 100, 100), 100)

        pygame.display.flip()
        clock.tick(30)

# 运行高难度游戏
if __name__ == "__main__":
    play_hard_tic_tac_toe()



