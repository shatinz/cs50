'''
    supervised-learning :
      given a data set of inpu-output pairs. learn a function to map input to outputs.
    
   classification :
      supervised learning task of learning a function mapping an input point to a discrete
      category.
    
    nearest-neighber classification:
      algorythm that, given an input ,chooses the class of the nearest data point to that input.

    k-nearest-neighbor classification :
      (k is presented for number of neighbors to be consider as near ) algorythm that, given an input,
      chooses the most common class out of the k nearest data points to that input.

    *vector-mathematics :
      h(x1,x2)= 1 if w0 + w1x1=w2x2 > or = 0
                0 otherwise

        wwight-vector w: (w0,w1,w2) 
        input vector x:(1,x1,x2)
        w . x: w0 + w1x1 +w2x2
           (h represent hypothesis)
            hw(x)= 1 if w.x > or = 0
            0 otherwise

        perceptron learning rule:
        given data point (x,y)(x is deta and y result of data), update each weight
        according to :
         wi = wi + a(actual value - estimate) * xi

         
        logistic-regression(soft threshold):
        idea: make an algorythem that works for only estimating margins and out of line datas.
    
        
    support-vector macines:
        maximum margin separator:
        boundary that maximizes the distance between an ofthe data points.

    regression:
        supervised learning task of learning a function mapping an input point to a continuous value.
    '''