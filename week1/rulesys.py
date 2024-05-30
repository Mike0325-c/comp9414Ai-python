# def is_prime(n):
#     if n < 2:
#         return False
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             return False
#     return True

# primes = [num for num in range(1, 1001) if is_prime(num)]
# print(primes)



# import matplotlib

import time 

import gymnasium as gym 
env = gym.make("MountainCar-v0", render_mode="human")
observation, info = env.reset()
print(env)

print("start")
step = 0

for _ in range(200):
    # time.sleep(0.01)
    if observation[0] > -0.53 and observation[1] > 0:
        action = 2
        
    elif observation[0] < -0.53 and observation[1] < 0:
        action = 0
    elif observation[0] < -0.53 and observation[1] > 0:
        action = 2
    elif observation[0] > -0.53 and observation[1] < 0:
        action = 0
    else:
        action = 1
    # action = env.action_space.sample()
    observation, reward, terminated, truncated, info = env.step(action)
    step += 1
    if terminated or truncated:
        observation, info = env.reset()
        break
print(step)
env.close()

