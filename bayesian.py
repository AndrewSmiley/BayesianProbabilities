__author__ = 'Andrew'
import json

"""
This is an example of reasoning using Bayesian Probabilities.
The bayesian probability piece
Given a set of conditional probabilities,  a set of evidential probabilities and a set of prior probabilities, determine
 a given input

The rule piece
Build a rule system

The domain
The domain is simple, auto diagnosis, my car wont start.
"""


class Hypothesis:
    """
    this is a simple class to represent a conclusion (i.e. a hypothesis) that is tied to rules.
    We store conditional probability (the likelihood that the hypothesis is true given all the evidence) and the
    prior probability (the probability that the hypothesis is true overall)
    """

    def __init__(self, cond, prob=0.0, evid=[]):
        """
        This is our constructor. Name is the only required argument, we need to be able to name our hypothesis SOMETHING
        Otherwise prior and conditonal probability can be set to 0.0 and evidence can be an empty list
        """
        self.name = cond
        self.prior_probability = prob
        self.evidence = evid
        self.conditional_probability = 0.0


class Evidence():
    """
    This is a simple class to represent evidence found or rules. Essentially, what this one contains is the name of the
    evidence/rule and the evidential probability that we can assign when it has been matched with a rule
    """

    def __init__(self, name, prob=0.0):
        self.name = name
        self.evidential_probability = prob

    pass


    def __str__(self):
        """
        Just using this for debugging purposes
        """
        return self.name


def compute_conditional_probability(hypotheses):
    """
    This function helps us calculate the conditional probability of P(h|E) i.e. what is the probability that h is true given the evidence E
    :param hypotheses: our individual hypotheses.
    """
    # first, we need to determine what our denominator is
    #sum for all i (p(E | hi) * p(hi))
    denominator = 0.0
    #just iterate through and do     (p(E | hi) * p(hi)) and add the result to the denominator
    for hypothesis in hypotheses:
        for evidence in hypothesis.evidence:
            denominator = (evidence.evidential_probability * hypothesis.prior_probability) + denominator

    #once we have the denominator, we can calculate the conditonal probability
    print "\nBayesian Evidential Probabilities\n"
    #for each hypothesis and its corresponding evidence, we need to do P(hi, ei)
    for hypothesis in hypotheses:
        for evidence in hypothesis.evidence:
            #calculate the conditional probability
            conditional_probability = evidence.evidential_probability * hypothesis.prior_probability / denominator
            #update the conditional probability of the hypothesis
            hypothesis.conditional_probability = conditional_probability
            #print for debugging purposes
            print "P(%s|%s): %s" % (hypothesis.name, evidence.name, conditional_probability)

    #finally, we will sort each hypothesis by most likely based upon the conditional probability
    hypotheses.sort(key=lambda x: x.conditional_probability, reverse=True)


def determine_hypotheses(working_memory, hypotheses):
    """
    This function simply looks at working memory and determines what hypotheses are applicable given the observations
    (or rules hit). This is basically forward chaining
    :param working_memory: The observations
    :param hypotheses: the potential hypotheses
    :return: list a list containing the conflict set
    """
    conflict_set = []
    # iterate through all the rules in working memory
    # basically, what we are saying here, is give me all the hypotheses where the rule is in the evidence
    # that would support that hypothesis and that is not already in the conflict set
    for hypothesis in hypotheses:
        #this was changed to reflect AND vs OR. i.e. Give me all hypotheses where Engine Doesn't Crank AND Lights Turn on
        #AND Visble Wear or Damage has occured
        if set([x.name for x in working_memory]).issubset(set([x.name for x in hypothesis.evidence])):
            conflict_set.append(hypothesis)

        # if all(z.name == x.name for z in working_memory for x in hypothesis.evidence):
        #         conflict_set.append(hypothesis)
#output the potential causes
    print "\nOf the Given Observations, These Are Potential Causes\n"
    for item in conflict_set:
        print item.name
    return conflict_set

# read in the test data

#these are our hypotheses also our right side of a^b -> c
hypotheses = []
#the rules are just broken out from the evidence that is wrapped in with the hypotheses
rules = []
#working memory is just all the rules that we've hit
working_memory = []

#get the rules and the
for k, v in json.loads(open("data.json").read()).iteritems():
    #first, gather all the rules
    [rules.append(y) for y in [Evidence(x['name'], prob=x['evidential_probability']) for x in v['evidence'] if
                               not any(z.name == x['name'] for z in rules)]]
    #next, form our hypothesis and the corresponding evidence
    hypotheses.append(Hypothesis(k, prob=v['prior_probability'],
                                 evid=[Evidence(x['name'], prob=x['evidential_probability']) for x in v['evidence']]))

    # data.append(Hypothesis(k, evid=[Evidence(x) for x in v]))
for identified_evidence in json.loads(open("observations.json").read()):
    working_memory.append(rules[next((i for i, item in enumerate(rules) if item.name == identified_evidence), -1)])
    # hypotheses = filter(lambda x: any())
#just output the observations
print "\nThe Observations\n"
for evidence in working_memory:
    print evidence.name

#calculate the conflict set (i.e. the potential hypotheses)
conflict_set = determine_hypotheses(working_memory, hypotheses)
#next, we calculate the conditional probability of the conflict set and sort by most likely given the observations
compute_conditional_probability(conflict_set)
#now, filter out anything that has a < 1% probability
rules.sort(key=lambda x: x.name)

print "\n\n\nBased Upon the Evidence Supported By Bayesian Probability, We Can Assume that %s Is The Cause Of The Failure" % (
conflict_set[0].name)














