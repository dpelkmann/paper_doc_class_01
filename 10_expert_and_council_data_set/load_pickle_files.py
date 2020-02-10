#!/bin/python
# ---------------------------------------------------------
# load_pickle_files.py
#
# David Pelkmann <david.pelkmann@fh-bielefeld.de>
#       Department of Engineering Sciences and Mathematics
#       University of Applied Sciences Bielefeld
#
# 11. February 2020 (dp)
# ---------------------------------------------------------
# Info
# ----
# 
# ---
import pickle
import article_stack

stack_expert_a = pickle.load(open("./expert_a.p", "rb"))
stack_expert_b = pickle.load(open("./expert_b.p", "rb"))
stack_expert_c = pickle.load(open("./expert_c.p", "rb"))
stack_council = pickle.load(open("./expert_council.p", "rb"))