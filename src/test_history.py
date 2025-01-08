# History is a dict of progression histories ordered by most recent set first
history = {
	"full-bridges": [("2025-01-01T11:05", [10, 10, 10])]
}

MAX_LEVEL = 3

def log2level(progression, log):
	# for each level (starting with the highest)
	for level, sets in progression_library[progression]['level'][::-1]:
		# has the log enough sets ? and are all the sets better or equal to the current level ?
		if len(log) >= len(sets) and all(a >= b for a, b in zip(log, sets)):
			return level
	return None

def attempted(progression):
	return progression in history

def last_set(progression):
	return history[progression][0]
	

def current_level(progression):
	# TODO add an option to search only the newer X months

	m = 0
	# For every logged sets of the progression
	for h in history[progression]:
		# find the maximum level achieved
		l = log2level(progression, h)
		if m < l:
			m = l

		if m == MAX_LEVEL:
			# If we found the maximum level then no need to check the rest
			return m
	return m


def current_progression(movement):
	# plus petite progression pas niveau 3
	for prog_name in movement:
		# par ordre croissant de progression
		if current_level(prog_name) != MAX_LEVEL:
			return prog_name