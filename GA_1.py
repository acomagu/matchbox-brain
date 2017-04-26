
import random

def get_score(member):
    answers = (2, 0, 1, 1, 1, 2, 0, 2, 2, 0)
    return sum((int(m is a) for m, a in zip(member, answers)))

def generate_initial_gene():
    return tuple((random.randint(0, 2) for _ in range(10)))

def get_child(a, b, r):
    return a[:r] + b[r:]

def select(members):
    return sorted(members, key=(lambda x: get_score(x)), reverse=True)[:2]

def get_next_members(members):
    child = get_child(members[0], members[1], random.randint(0, 10))
    added = members + [child]
    mutated = [(mutate(member, random.randint(0, 9)) if random.randint(0, 6) < 5 else member) for member in added]
    selected = select(mutated)
    return selected

def mutate(member, r):
    return member[:r] + (((member[r] + 1) % 3),) + member[r+1:]

# def n_cycle(members, n):
#     return members if n == 0 else n_cycle(get_next_members(members), n-1)

members = [generate_initial_gene() for _ in range(2)]

# new_members = n_cycle(members, 10)

for _ in range(20):
    members = get_next_members(members)
    print(members, get_score(members[0]), get_score(members[1]))
