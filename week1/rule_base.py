import numpy as np
import matplotlib.pyplot as plt
import gymnasium as gym


def select_action(action_selection_code):
    if action_selection_code == 0:
        action = env.action_space.sample() #random action
    elif action_selection_code == 1:
        action = 2 #push to the right
    elif action_selection_code == 2:
        #two rules
        if observation[0] > -0.53 and observation[1] > 0:
          action = 2
        elif observation[0] < -0.53 and observation[1] < 0:
          action = 0
        else:
          action = 1
          
    elif action_selection_code == 3:
        #four rules
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
        
    else:
      action = 1

    return action


print("Starting Mountain Car")
env = gym.make("MountainCar-v0")
#env = gym.make("MountainCar-v0", render_mode="human")
observation, info = env.reset()
iter = 200
agents = 100
approaches = 4

steps = np.zeros((agents, approaches))

for k in range(approaches):
    for j in range(agents):
        for i in range(iter):
            action = select_action(k) #0: random action, 1: push to the right, 2: two rules, 3: four rules
            observation, reward, terminated, truncated, info = env.step(action)
            #print(observation)
    
            if terminated or truncated:
                observation, info = env.reset()
                break
        
        #print("Finished in %i steps"%i)
        steps[j][k] = i

bp = plt.boxplot(steps, showmeans=True)
plt.title("Number of steps needed")
plt.xlabel("Method")
plt.ylabel("Actions")
plt.xticks(np.arange(1,5), ('Random', 'Always right', 'Two rules', 'Four rules'))
plt.show()

print("Closing environment")
env.close()




