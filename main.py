# This is the server-side script to start the `ucdavis_honeypot`. This starts
# server and spawns n number of phantom identities.

import sys
import os
import argparse

# We import the python classes from the `src` directory

sys.path.append(os.path.join(os.getcwd()),"src")

from src import *

# We take the input parameters from the user here. All the parameters are
# taken while starting the server.

parser = argparse.ArgumentParser(
    description = "This program starts the `ucdavis_honeypot` program. The \
        project is described in details in the README.md document. It takes \
        the following parameters as input while starting the program. We \
        assume that the network administrator starts this program."
)

# We obtain the number of honeypot class objects to instantiate. Each such
# object is associated with a `fake` email address.

parser.add_argument(
    "--num_phantom",
    type = int,
    required = True,
    help = "Input the number of phantom users to spawn. Each phantom is a \
            class object of __ class which consumes __ bytes on \
            initialization."
)

# One of the prominent features of the `ucdaivs_honeypot` project is that it
# can filter out scam mails and generate reply emails using a machine
# learning model. This ensures a lower false-positive and better effectiveness
# in the case of scamming mails.

parser.add_argument(
    "--set_filter",
    type = bool,
    required = True,
    help = "`ucdavis_honeypot` has a machine-learning based filtering \
            mechanism for determining whether a given email is a spam mail \
            or not. If --set_filter is disabled, then we use a simple string \
            parsing based filter, whose accuracy is low.",
    choices = [True, False]
)

parser.add_argument(
    "--set_reply_mech",
    trype = bool,
    required = True,
    help = "Similar to --set_filter, --set_reply_mech(anism) either uses a \
            machine learning model to generate reply emails for the the \
            scammers. It can either be enabled or disabled.",
    choices = [True, False]
)

# Definition of __main__

if __name__ == "__main__":

    # First we check whether all the input parameters are correctly placed. If
    # not, then we exit the program.

    args = parser.parse_args()

    for i in range(0, args.num_phantom):

