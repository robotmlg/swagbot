prefix = 'prefix'
infix = 'infix'

mathverbs = {'multiply': prefix,
             'times': infix,
             'divide ':prefix, # extra space so that it's not detected in "divided"
             'divided':infix,
             'add' : prefix,
             'plus': infix,
             'minus': infix,
             'subtract': prefix}

mathpreps = {'to',
             'by',
             'from'}


def text2int(textnum, numwords={}):
  if not numwords:
    units = [
      "zero", "one", "two", "three", "four", "five", "six", "seven", "eight",
      "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
      "sixteen", "seventeen", "eighteen", "nineteen",
    ]

    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

    scales = ["hundred", "thousand", "million", "billion", "trillion"]

    numwords["and"] = (1, 0)
    for idx, word in enumerate(units):    numwords[word] = (1, idx)
    for idx, word in enumerate(tens):     numwords[word] = (1, idx * 10)
    for idx, word in enumerate(scales):   numwords[word] = (10 ** (idx * 3 or 2), 0)

  current = result = 0
  for word in textnum.split():
    if word not in numwords:
      raise Exception("Illegal word: " + word)

    scale, increment = numwords[word]
    current = current * scale + increment
    if scale > 100:
      result += current
      current = 0

  return result + current


def parse_arith(sen):

  op1 = None
  try:
    op1 = text2int(sen)
  except:
    pass
  else:
    return {'verb':None, 'op1':op1, 'op2':None}
    

  # find the verb in the sentence
  v = None
  for v in mathverbs:
    if v in sen: 
      break

  if v is None:
    return None

  # if it's a prefix verb, find the preposition and then parse
  if mathverbs[v] is prefix:
    verb_pos = sen.find(v)

    # find the first space for the start of the first operand
    op1_pos = sen.find(' ',verb_pos) + 1


    # find the preposition
    p = None
    for p in mathpreps:
      if p in sen:
        break
    if p is None:
      return None

    prep_pos = sen.find(p)

    # find the first space after the preposition for the second operand
    op2_pos = sen.find(' ',prep_pos) + 1

    op1  =  sen[op1_pos:prep_pos]
    op2  =  sen[op2_pos:]


  # if it's an infix verb, grab the operands from around the verb
  elif mathverbs[v] is infix:
    verb_pos = sen.find(v)

    # find the first space after the verb for the second operand
    op2_pos = sen.find(' ',verb_pos) + 1
    if v is 'divided':
      op2_pos = sen.find(' ',op2_pos) + 1

    op1  =  sen[0:verb_pos]
    op2  =  sen[op2_pos:]
    
  # print mathverbs[v]
  # print v
  # print op1
  # print op2

  return {'verb':v, 'op1':op1, 'op2':op2}

  
