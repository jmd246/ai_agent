from agent import Agent
from lib.util.parser import Parser

import logging


logging.basicConfig(level=logging.INFO,filename="openrouter.log", filemode="w")



    # check response for what function to call perofrm the call and return the results back to the llm

def main():
    # set up the argument parser and parse the command line arguments
    
    parser = Parser(data=None)
    args = parser.setup_argparse().parse_args()

    # create an instance of the Agent class
    agent = Agent(user_prompt=args.user_prompt, verbose=args.verbose)
    # run the agent
    if not agent.run() :
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
