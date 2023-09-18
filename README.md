# 🦖 Dino-NEAT

## Introduction
 The goal of this project is to create a simple implementation of NeuroEvolution of Augmenting Topologies (NEAT) on the popular chrome dinosaur game.
 
 ## Dataset
 Dataset is just a collection of images of cactus, different dinosaur movement and the terrain.

 ## Installation
 Clone the repository using the following command

 ```
 git clone https://github.com/yuziahaque/Dino_NEAT.git
 ```

 Install the required dependencies using the following command

 ```
 pip install -r requirements.txt
 ```

 ## Usage

 A config.txt file is provided in the repository for customization of the run.
 Pop size of the config.txt file is the number of dinosaurs per generation

 Do make changes to other config variables and see if you can produce any exciting results.

 To run the algorithm, Go to the directory folder and run the command
 ```
 python run main.py
 ```

 ## NEAT Brief Explanation
 NeuroEvolution of Augmenting Topologies (NEAT) is a genetic algorithm (GA) for the generation of evolving artificial neural networks (a neuroevolution technique)


 ## Configuration Information

 ### Network Parameters
  - 'num_hidden' = 0 --> The number of hidden layers in the network
  - 'num_inputs' = 2 --> The number of input layers in the network
  - 'num_outputs' = 1 --> The number of output layers

  - The neural network is activated with two inputs and the output the information:

    - The y-coordinate of the dinosaur (dinosaur.rect.y).
    - The distance between the dinosaur and the obstacle (distance(...)).
    - The output of the neural network (a single value) is used to determine whether the dinosaur should jump or not.