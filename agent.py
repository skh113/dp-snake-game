import torch
import random
import numpy as np
from game import SnakeGameAI, Direction, Point
from collections import deque

MAX_MEMORY = 1_000_000
BATCH_SIZE = 1000
LEARNING_RATE = 0.001


class Agent:
    def __init__(self):
        self.games_number = 0
        self.epsilon = 0  # randomness
        self.gamma = 0  # discount rate
        self.memory = deque(maxlen=MAX_MEMORY)  # after filling it self -> popleft()

    def get_state(self, game):
        pass

    def remember(self, state, action, reward, next_state, done):
        pass

    def train_long_memory(self):
        pass

    def train_short_memory(self, state, action, reward, next_state, done):
        pass

    def get_action(self, state):
        pass


def train():
    plot_scores = []
    plot_mean_scores = []
    total_score = 0
    record = 0
    agent = Agent()
    game = SnakeGameAI()

    while True:
        # get old state
        old_state = agent.get_state(game)

        # get move
        final_move = agent.get_action(old_state)

        # perform move and get new state
        reward, done, score = game.play_step(final_move)
        new_state = agent.get_state(game)

        # train short memory
        agent.train_short_memory(old_state, final_move, reward, new_state, done)

        # remember
        agent.remember(old_state, final_move, reward, new_state, done)

        if done:
            # train long memory, plot results
            game.reset_game()
            agent.games_number += 1
            agent.train_long_memory()

            if score > record:
                record = score

            print(f"Game: {agent.games_number}, Score: {score}, Record: {record}")
            # plot


if __name__ == "__main__":
    train()
