import json
import sys
from datetime import datetime
import twtFunc as tF

def avgDegree(tweet_input,tweet_output):

    # Read inputs:
    inputFile = open(tweet_input, 'r')
    tweets = inputFile.readlines()
    # Open output file
    output = open(tweet_output,'w')

    # Create empty lists for time and hashtag texts
    list_txt = []
    list_time = []
    prev_avgDeg = 0
    
    # Calculate rolling average
    for i in range(len(tweets)+1):
        try:
            # Load twt
            twt = json.loads(tweets[i])
            # Get twt hashtag clump
            twtHash = twt['entities']['hashtags']
            # If there is nothin in hashtag skip to the next twt
            if not twtHash:
                output.write('%s\n'%(prev_avgDeg))
                continue
            else:
                # Get created_at time
                created_at = twt['created_at']
                created_at = datetime.strptime(created_at, '%a %b %d %H:%M:%S +0000 %Y')
                # Get txt from hashtag clump
                twtTxt = tF.getTxt(twtHash)
                # Keep adding created_at time and txt to list before sorting
                list_time.append(created_at)
                list_txt.append(twtTxt)

        except:
            continue
        # Sort tweet and txt to get whatever in the last 60s
        list_time_curr, list_txt_curr = tF.sortRemove(list_time, list_txt)
        if not list_txt_curr:
            # If the list of current text is empty aka hashtags all expired, return 0.
            output.write('%s\n'%(prev_avgDeg))
            # print 'No connected hashtag in the last minute'
        else:
            # Create a list of edges
            list_edge = tF.makeListEdge(list_txt_curr)
            try:
                # Calculate the number of nodes and rolling average
                nodeNumber, avgDeg = tF.avgDeg(list_edge)
                prev_nodeNumer = nodeNumber
                prev_avgDeg = avgDeg
                output.write('%s\n'%(avgDeg))
            except:
                # print 'Previous rolling average: ' + str(prev_avgDeg)
                output.write('%s\n'%(prev_avgDeg))

if __name__ == '__main__':
    
    tweet_input = sys.argv[1]
    tweet_output = sys.argv[2]

    avgDegree(tweet_input,tweet_output)
