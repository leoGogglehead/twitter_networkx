import json
import sys
from datetime import datetime
import twtFunc as tF

# unit tests
# hashtags = [['spark','insight'],['democracy','election','spark'],['insight','apache','hadoop'],['official','cruz','trump','big'],['whatever','trump'],['insight','python','spark'],['hurricane','spark','clinton'],['aws','django','numpy'],['editor','spark','pop'],[' ','hadoop','pop']]
# times = ["Sun May 31 01:01:56 +0000 2016","Sun May 30 01:01:15 +0000 2016","Sun May 30 01:01:26 +0000 2016","Sun April 30 15:33:45 +0000 2016","Sun May 30 01:01:00 +0000 2015","Sun May 30 02:00:15 +0000 2016","Sun May 30 01:02:30 +0000 2016","Fri Oct 30 15:34:45 +0000 2015","Fri Oct 30 15:35:00 +0000 2015","Fri Oct 30 15:35:15 +0000 2015"]

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
