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
        function(input)
          f(1200)=5800
          f(500)=13400
        hypothesis(input)
    
    EVALUATING HYPOTHESIS:
      loss function : function that express how poorly our hypothesis perform.
        0-1 loss function(for discrete values) :
        l(actual, predict)=
          0 if actual = predict
          1 otherwise
            L1loss function(how far apart where the actual value and predicted values):
            L(actual,predicted)=|actual-predict|
            l2 loss function(effectively penaliing much more harshly any thing that is worse prediction):
            L(actual,predict)=(actual-predicted)2
        OVERFITTING :
        a model that fits so closely to a particular data set and therefore may fail generalize to future data.
          regularizatio:
            penalizing pypothesis that are more complex to favor simpler, more general hypotheses.
            cost(h) = loss(h) + complexity(h)
          holdout cross-validation:
            splitting data into a training set and a test set, such is trainnig happens on the training set,
            and is evaluated on the test set.
          k-fold cross-validation:
          splitting data into k sets, and experimenting k times, using each set as a test once,
          and using remaining data as training set. 
    reinforcement learning:
      given a set of rewards or punishments, learn what action to take in in  future.
      state-action-reward
        marcov decision process:
        model for decision-making, representing states, actions and their rewards
        .set of states s
        .set of actions(s)
      transitiont model p(s'|s,a)
        .reward function r(s,a,s')
      q-learning
         method for learning a function q(s,a) estimate of the value of performing action a in state s
         .start with q(s,a) = 0 for all s,a
         .when we taken an action and recieve a reward
         .estimate the vlue of q(s,a) based on current reward and expected future rewards
         .update q(s,a) to take into account old estimate as well as our new estimate
             q(s,a) + q(s,a) a(new value estimate - old value estimate)
         .alfa value : how much value we get to new estimate compare to old estimate
         .alfa value 1 : we really value our new estimate
      exploit: older information that leads to reward
      explore: what might lead to a better reward in future. finding new 
      e-greedy:
        set e equal to how often we want to move randomly
        with probability 1-e , choose estimated best move.
        with probability 3, choose a random move.
      function approximation :
        approximating q(s,a) , often by a function combinig various features, rather than storing one value for every state-action pair
  unsupervised learning
  givven input without any additional feedback, learn pattens.
    clustering:
    organizing a set of objects into groups in such a way that similar objects tend to be in the same group
      k-means clustering
        algorythm for clustering sata based on repeadly assigning points to cluster and updating those clusters centers
        

 


      


    '''