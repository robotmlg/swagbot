import classifier

def respond_question(text, valence) :
    if valence == 'pos' :
        return "I wish I knew."
    else :
        return "That's a tough question."

def respond_other(text, valence) :
    return ":P  Well, what next?"

def respond_statement(text, valence) :
    if valence == 'pos' :
        return "Great!  Tell me more."
    else :
        return "Ugh.  Is anything good happening?"

def respond_bye(text, valence) :
    return "I guess it's time for me to go then."

def respond_greet(text, valence) :
    return "Hey there!"

def respond_reject(text, valence) :
    if valence == 'pos' :
        return "Well, if you insist!"
    else :
        return "I still think you should reconsider."

def respond_emphasis(text, valence) :
    if valence == 'pos' :
        return '!!!'
    else :
        return ":("


responses = {'Accept': respond_other,
             'Bye': respond_bye,
             'Clarify': respond_other,
             'Continuer': respond_other,
             'Emotion': respond_other,
             'Emphasis': respond_emphasis,
             'Greet': respond_greet,
             'nAnswer': respond_other,
             'Other': respond_other,
             'Reject': respond_reject,
             'Statement': respond_statement,
             'System': respond_other,
             'whQuestion': respond_question,
             'yAnswer': respond_other,
             'ynQuestion': respond_question}


def respond(text) :
    act = expt3.classify(text)
    valence = expt1.classify(text)
    return responses[act](text, valence)
