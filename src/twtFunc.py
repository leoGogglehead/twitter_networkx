# function that gets just the text
def getTxt(Twt):
    import json
    # Create placeholder for new text
    new_text = [];
    for i in range(len(Twt)):
        txt = Twt[i]['text'].encode('ascii','ignore')
        new_text.append(txt)
    return new_text

# sort-and-remove function:
def sortRemove(list_time, list_txt):
    # Return sorting index using list of created_at time
    sort_index = sorted(range(len(list_time)), key=lambda k: list_time[k])
    # Sort list of time and list of texts chronologically
    list_time = [list_time[i] for i in sort_index]
    list_txt  = [list_txt[i] for i in sort_index]
    # find the differences between the last and all time before and do removal
    time_last = list_time[-1]
    timeDiff_list = [x - time_last for x in list_time]
    # Merge list of time differences with list_txt and list_time
    merged_list = map(lambda x,y,z:[x.total_seconds(),y,z], timeDiff_list,list_time,list_txt)
    # Get all items with time less than 60 seconds away from the latest time
    new_merged_list = [i for i in merged_list if i[0] >= -60]
    list_time = [i[1] for i in new_merged_list]
    list_txt = [i[2] for i in new_merged_list]
    return (list_time, list_txt)

# make a list of edges between hashtag txt
def makeListEdge(list_txt):
	from itertools import combinations
	list_edge = []
	# Create a list of combinations of hashtags 
	for i in list_txt:
		list_edge.append(list(combinations(sorted(i),2)))
	# Filter out empty edges 
	list_edge = filter(None, list_edge)
	# Create a list of edges
	list_edge = [i for j in list_edge for i in j]
	return list_edge

# Calculate the number of nodes and rolling average using networkx
def avgDeg(list_edge):
	import networkx as nx
	import matplotlib.pyplot as plt
	# Create graph and add edges
	G = nx.Graph()
	G.add_edges_from(list_edge)
	try:
		# Calculate the rolling average
		avgDegree = round(sum(G.degree().values())*1.00/len(G.nodes()),2)
		return len(G.nodes()),avgDegree
	except:
		print "Hashtags can't be connected in the last minute."
	


