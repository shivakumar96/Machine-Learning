from datsetGen import people,rating,movieName,moviefactor

#make use linear regression model and content based filtering to recommend movies
# xval is a list of movies with their factor
def gradDescent(xval,ratinglist) :
     thetacur = [] # to store float values 
     thetaprev = []
     intetacur = [] # integer value of theta 
     intetaprev = [] # " --------"
     n = len(xval[0])  # num of of factor/features of movie + 1
     m = len(xval)     # num of movies watched
     alpha = 0.05
     i = 0 
     while(i<n) :
          thetacur.append(0.2)
          intetacur.append(10)
          intetaprev.append(10)
          thetaprev.append(0.1)
          i+=1
     # actual gradient descendent algorithm
     count = 0  # to count the number of iterations
     while(True) :
          k = 0 
          count+=1
          sumlist = []
          while(k<n) :
               thetaprev[k] = thetacur[k]
               intetaprev[k] = intetacur[k] = int(thetaprev[k]*10000)  #10000 is used to take upto 4 decimal points precision
               sumlist.append(0.0)
               k+=1      
          i =0 ;j=0;k=0;
          
          while(i<m) :
               xi = xval[i]
               j=0
               sum1 =  0.0
               while(j<n):
                   sum1+=xi[j]*thetaprev[j]
                   j+=1
               sum1 = (sum1 - ratinglist[i])
               k = 0
               while(k<n):
                   sumlist[k]+= sum1*xi[k]
                   k+=1
               i+=1
               
          k=0
          while(k<n) :
                thetacur[k] = thetaprev[k] - alpha*sumlist[k]/m 
                intetacur[k] = int(thetacur[k]*10000)
                k+=1
          if(cmp(intetacur,intetaprev)==0) :
                        break ;
     
     print " number of iterations  is : ",count
     print " current values of theta  : ",thetacur
     print " \n\n\n"
     print " previous values of theta : ",thetaprev
     return thetacur


def getRecommendations(personid) :
      watched_movies = rating[int(personid)].keys() # get watched movie list
      watched_movies.sort() # sort the watched movies according to movie id
      not_watched = [] #  list of movies not watched 
      total_movie = movieName.keys() # get all movie id
      total_movie.sort()
      watched_rating = [] # list of rating for corresronding movies
      notwatched_rating = [] # to calculate and store raings of movies not watched

      #find rating of the movies watched
      for x in watched_movies :
            watched_rating.append(rating[int(personid)][x])

      # find the movies not watched
      for x in total_movie :
            if x not in watched_movies :
                 not_watched.append(x)

      not_watched.sort() # sort the not watched movies

      watched_movie_factor  = [] # list to store watched movies factors
      not_watched_factor = []  # list to store not watched movies factor

      # obtain movie factor for all the watched movies 
      for x in watched_movies :
             watched_movie_factor.append(moviefactor[x])

      # obtain movie factor for not watched movies
      for x in not_watched :
             not_watched_factor.append(moviefactor[x])
            
      # call the gradient descendent function to find theta values for that person
      theta = gradDescent(watched_movie_factor,watched_rating) # print the theta values obtained
      print " \n\n"
      print " the theta values are ",theta # print the values of theta we got
      
      predict = predictRating(not_watched,not_watched_factor,theta) # predict rating for not watched movies in dictionary form
      predrating = predict.values() # find all the movie  ratings 
      Mrate = max(predrating) # find maximum rating in the rating predicted
      print  "maximum rating got is: ",Mrate,"\n\n"
      
      threshold = Mrate - 0.75 # threshoud value of rating to predict movies
     
      recommend_movie_list = [] # store the movies to recomend which are having values greater than or equal to threshold
      for x in predict :
           if(predict[x] >= threshold ) :
               recommend_movie_list.append(x)
     
      # print the recommended movie list for the given person 
      print len(recommend_movie_list)," movies recommended they are \n\n"
  
      for x in recommend_movie_list :
            print x," | ",movieName[x]

      return
       

def predictRating(notwatched,notwatchedfactor,theta) :
      # predict the rating using theta values found
      prediction = {}
      rating = 0.0
      i = 0
      m = len(notwatched)
      while(i<m) :
          rating = 0.0
          k = 0
          x=notwatchedfactor[i]
          n = len(x)
          while(k<n) :
               rating+=theta[k]*x[k] ;
               k+=1
          prediction[notwatched[i]] = rating
          i+=1
      return prediction




# function starts from here
 
print " Enter person id : "

persid = str(input())

if persid in people :
         getRecommendations(persid)
else :
   print " invalid user id "

