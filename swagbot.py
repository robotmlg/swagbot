import responder

print 'Hello! I can solve math!'
while True:
  s = raw_input("> ")
  r = responder.respond(s)
  print r
  if r == responder.end_text:
    break
