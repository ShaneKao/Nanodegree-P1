import csv
import pandas
def fix_turnstile_data(filenames):
    '''
    Filenames is a list of MTA Subway turnstile text files. A link to an example
    MTA Subway turnstile text file can be seen at the URL below:
    http://web.mta.info/developers/data/nyct/turnstile/turnstile_110507.txt
    
    As you can see, there are numerous data points included in each row of the
    a MTA Subway turnstile text file. 

    You want to write a function that will update each row in the text
    file so there is only one entry per row. A few examples below:
    A002,R051,02-00-00,05-28-11,00:00:00,REGULAR,003178521,001100739
    A002,R051,02-00-00,05-28-11,04:00:00,REGULAR,003178541,001100746
    A002,R051,02-00-00,05-28-11,08:00:00,REGULAR,003178559,001100775
    
    Write the updates to a different text file in the format of "updated_" + filename.
    For example:
        1) if you read in a text file called "turnstile_110521.txt"
        2) you should write the updated data to "updated_turnstile_110521.txt"

    The order of the fields should be preserved. 
    
    You can see a sample of the turnstile text file that's passed into this function
    and the the corresponding updated file in the links below:
    
    Sample input file:
    https://www.dropbox.com/s/mpin5zv4hgrx244/turnstile_110528.txt
    Sample updated file:
    https://www.dropbox.com/s/074xbgio4c39b7h/solution_turnstile_110528.txt
    '''
    for name in filenames:
        with open(name, 'rb') as f:
             reader = csv.reader(f)
             with open("updated_" + name, 'w') as fp:
                  a = csv.writer(fp)
                  for row in reader: 
                      header_row = row[0:3]
                      length =  ((len(row)-3)/5)

                      x = 3
                      big_list = []
                      for i in range(1,length + 1):
                          big_list = header_row + row[x:(x+5)]
                          a.writerow(big_list)
                          x = x + 5
        '''
        data=pandas.read_csv(name,header=None)
        print len(data.index)
        #print data.loc[999,0]
        for j in range(100):
            for i in range(8):
            
                df = pandas.DataFrame({'a': [data.loc[j,0]],
                       'b':[data.loc[j,1]],
                       'c':[data.loc[j,2]],
                      'd' :[data.loc[j,3+5*i]],
                   'e':[data.loc[j,4+5*i]],
                   'f':[data.loc[j,5+5*i]],
                   'g':[data.loc[j,6+5*i]],
                   'h':[data.loc[j,7+5*i]]
                   
                           
                       })
                #print df
                df.to_csv("updated_" + name,mode='a',header=False,index=False)    
        '''    
        
        #print 'updated_' + name
        #data.to_csv('updated_' + name,header=False)
        #print name
        # your code here
