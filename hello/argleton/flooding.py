import networkx as nx
from collections import OrderedDict


def route(config,G):

	s,d = config[0],config[1]

	# will contain unvisited nodes(as keys) and their neighbours(as values)
	router = OrderedDict()

	drop_count = 0
	success_count = 0 

	# stores all traversed edges
	path_edges = []

	# initialise all nodes as unvisited
	for x in G.nodes():
		G.node[x]['vis'] = False

	# initialise router dictionary with the source node
	neighb = G.neighbors(s)
	router[s] = neighb
	

	for key in router.keys():

		if key == d:
			success_count+=1

		else:

			# mark current node(key) as visited
			G.node[key]['vis'] = True

			# if all neighbours are marked visited, drop that packet
			if all([G.node[y]['vis'] for y in router[key]]):
				drop_count+=1

			else:
				# traverse to current node's neighbours
				for values in router[key]:

					# if a neighbours is already visited, drop that packet
					if G.node[values]['vis'] == True:
						continue
					
					else:
						# append current_node,neighbour_node
						path_edges.append([key,values])
						# append the neighbour node in router_dictionary with it's neighbours
						router[values] = G.neighbors(values)

		del router[key]

	return path_edges

