#BayesianProbabilities

##A report describing your domain and knowledge, why you selected the method of uncertainty that you did, difficulties you had in implementation, enhancements that you feel should be made if you were going to spend more time on it, and whether the uncertainty approach selected fits the problem you implemented or whether you think one of the other approaches would be better, and why.

The domain I selected was auto diagnosis, specifically, identifying why a vehicle wouldn't start. My knowledge base was generated off the
 top of my head based upon my experience in working with vehicles. All of the hypotheses/evidence is relatively general, although relatively 
 accurate as well. I selected Bayesian Probability as uncertainty handling as I felt that given the level of overlap in evidence in
 auto diagnosis (i.e. my engine cranks but doesn't turn over could be indicative of multiple issues) was well suited to conditional probability calculation, 
 i.e. it's more likely that my battery is dead than my starter, and this is the liklihood that if the latter is the case, I will see x,y,z symptoms
 vs something else. From a difficulty perspective, the implementation was relatively easy. What I considered to be the 
 most difficult part was the actual categorization and building of the data. There are so many different subtle reasons a vehicle 
 can fail to start, it as rather difficult to determine what was in-scope and what was out of scope to be in the dataset of the 
  assignment. As far as enhancements go, I would like to build a much larger data set, getting very granular with the potential causes of  
  vehicle failure. In believe that the logic itself, in both the rule changing as well as the the Bayesian probability calculate is relatively
  cut and dry. The only more optimal thing I would think to do would be to make the application more real-world and gatehr
  actual user input on likelihoods. I.e. There is a 25% chance the oil is outdated, a 50% chance it's the alternator, etc. In my mind, 
   this was the best approach for the job. I do not think that another uncertainly handling mechanism would be more effective. 

##Sample Run 1

```
The Observations

Engine Doesn't Crank
Lights Turn On
Visible Wear or Damage
    Smell of Gasoline

Of the Given Observations, These Are Potential Causes

Malfunction In Fuel Injection System (Carburetor)
Bad Fuel Line

Bayesian Evidential Probabilities

P(Malfunction In Fuel Injection System (Carburetor)|Engine Doesn't Crank): 0.0821467688938
P(Malfunction In Fuel Injection System (Carburetor)|Smell of Gasoline): 0.0328587075575
P(Malfunction In Fuel Injection System (Carburetor)|Lights Turn On): 0.10843373494
P(Malfunction In Fuel Injection System (Carburetor)|Visible Wear or Damage): 0.0251916757941
P(Malfunction In Fuel Injection System (Carburetor)|Leaking Gasoline): 0.0449069003286
P(Bad Fuel Line|Engine Doesn't Crank): 0.205366922234
P(Bad Fuel Line|Smell of Gasoline): 0.0547645125958
P(Bad Fuel Line|Lights Turn On): 0.271084337349
P(Bad Fuel Line|Visible Wear or Damage): 0.0629791894852
P(Bad Fuel Line|Leaking Gasoline): 0.112267250821



Based Upon the Evidence Supported By Bayesian Probability, We Can Assume that Bad Fuel Line Is The Cause Of The Failure
```

##Sample Run 2
```
The Observations

Lights Turn On
Key Won't Turn

Of the Given Observations, These Are Potential Causes

Bad Ignition System
Wheel Lock

Bayesian Evidential Probabilities

P(Bad Ignition System|Engine Doesn't Crank): 0.212765957447
P(Bad Ignition System|Lights Turn On): 0.234042553191
P(Bad Ignition System|Key Won't Turn): 0.0756501182033
P(Bad Ignition System|Visible Wear or Damage): 0.00236406619385
P(Wheel Lock|Engine Doesn't Crank): 0.212765957447
P(Wheel Lock|Lights Turn On): 0.234042553191
P(Wheel Lock|Key Won't Turn): 0.0283687943262



Based Upon the Evidence Supported By Bayesian Probability, We Can Assume that Wheel Lock Is The Cause Of The Failure
```

##Sample Run 3
```
The Observations

Lights Turn On
Very High Mileage
Engine Cranks But Doesn't Run
Visible Wear or Damage

Of the Given Observations, These Are Potential Causes

Bad Alternator
Malfunction In Fuel Injection System (Carburetor)
Bad Starter
Bad Fuel Line

Bayesian Evidential Probabilities

P(Bad Alternator|Engine Doesn't Crank): 0.00936503035916
P(Bad Alternator|Lights Turn On): 0.00401358443964
P(Bad Alternator|Very High Mileage): 0.00689513224246
P(Bad Alternator|Visible Wear or Damage): 0.00195533600906
P(Bad Alternator|Engine Cranks But Doesn't Run): 0.00977668004528
P(Malfunction In Fuel Injection System (Carburetor)|Engine Doesn't Crank): 0.0385921580735
P(Malfunction In Fuel Injection System (Carburetor)|Smell of Gasoline): 0.0154368632294
P(Malfunction In Fuel Injection System (Carburetor)|Engine Cranks But Doesn't Run): 0.0118349284759
P(Malfunction In Fuel Injection System (Carburetor)|Lights Turn On): 0.050941648657
P(Malfunction In Fuel Injection System (Carburetor)|Visible Wear or Damage): 0.0118349284759
P(Malfunction In Fuel Injection System (Carburetor)|Very High Mileage): 0.0298446022435
P(Malfunction In Fuel Injection System (Carburetor)|Leaking Gasoline): 0.0210970464135
P(Bad Starter|Engine Doesn't Crank): 0.0983328187712
P(Bad Starter|Lights Turn On): 0.102655140475
P(Bad Starter|Very High Mileage): 0.057270762581
P(Bad Starter|Visible Wear or Damage): 0.0248533497993
P(Bad Starter|Engine Cranks But Doesn't Run): 0.102655140475
P(Bad Fuel Line|Engine Doesn't Crank): 0.0964803951837
P(Bad Fuel Line|Smell of Gasoline): 0.0257281053823
P(Bad Fuel Line|Engine Cranks But Doesn't Run): 0.0295873211897
P(Bad Fuel Line|Lights Turn On): 0.127354121642
P(Bad Fuel Line|Very High Mileage): 0.0411649686117
P(Bad Fuel Line|Visible Wear or Damage): 0.0295873211897
P(Bad Fuel Line|Leaking Gasoline): 0.0527426160338



Based Upon the Evidence Supported By Bayesian Probability, We Can Assume that Bad Starter Is The Cause Of The Failure
```