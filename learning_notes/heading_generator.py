def heading_generator(tag, heading_type):
  return f"<h{heading_type}>{tag}</h{heading_type}>"

print(heading_generator('Hi There', 3))