import classifier
import mathparse
import insultgen
import wikistuff

end_text = 'Okay, so long!'
born_list = ['born', 'birth', 'birthday']
death_list = ['die', 'died', 'death']

#def respond_math(text) :


def respond_question(text, valence):
    t = text.lower().split()
    if t[0] == 'when':
      #get the name
      name = text[text.find(' '):] #skip over "when"
      name = name[text.find(' '):] #skip over verb
      name = name[:name.rfind(' ')]
      name_l = name.split()
      url = "http://en.wikipedia.org/wiki/" + name_l[0]
      if len(name_l) > 1:
        url += '_' + name_l[1]

      if any(word in text for word in born_list):
        return wikistuff.findTheBirth(url)
      if any(word in text for word in death_list):
        return wikistuff.findTheDeath(url)
        

      return name
      
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
        g = insultgen.insultgen()
        return g.generateInsult()

def respond_bye(text, valence) :
    return end_text

def respond_greet(text, valence) :
    return "Hey there!"

def respond_reject(text, valence) :
    if valence == 'pos' :
        return "Well, if you insist!"
    else :
        g = insultgen.insultgen()
        return g.generateInsult()

def respond_emphasis(text, valence) :
    if valence == 'pos' :
        return '!!!'
    else :
        g = insultgen.insultgen()
        return g.generateInsult()


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
    # if text.split()[0].lower() == 'solve'
      
    act = classifier.expt3.classify(text)
    valence = classifier.expt1.classify(text)
    # print act
    return responses[act](text, valence)
