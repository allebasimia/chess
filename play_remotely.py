"""
 goal: send an empty "game" dictionary  from one machine to another
 tangential - allow baords to be rendered in jupyter notebooks
 what if just created for self personal tool to study RL algorithms in context of any game wanted?
 yeah that sounds more fun
 and then could simulate millions of games to train game models across thousdands of GPUS
 yes please do that
 goal: i want to train a game playing model - to keep simple, will start with chess (and also to avoid headache of
 renaming repo right at this moment)
 chess (really wish this were connect n right now)
 allow for https - in sense that still want to talk with each of machines
 what's the networking part? or intermachine communication part? when want to connect with other nodes in network?
 potentially
 to start - maybe single model on single machine? look up pytorch models or tensorfow

 # goal - think you just want to set up a container - and then can have training on a bunch of nodes
 - what's a toy version of this?
 - still focus on meat - which is to create the chess game
 - two features going on - actual remote chess game and then AI component for creating the best ML
 - AI chess agents
 - focus on the first part
 - can also work on the second part
 - --> will have two projects done by time of Anthropic interview
 - right now - send a basic HTTP request with a board
 - the more complete, braad, etc. interesting system can work on, *the better* - will be exposed to more
 - finally can 100% do this all in python
"""

# set up connection
