tags_one = {
  'python',
  'coding',
  'tutorials',
  'coding'
}

tags_two = {
  'ruby',
  'coding',
  'tutorials',
  'development'
}

# There are a few duplicate elements

# Merged tags - removes duplicates
"""
merged_tags = tags_one | tags_two
print(merged_tags)
"""

# Tags in tags_one but not in tags_two - so only unique tags that aren't in both
"""
exclusive_to_tag_one = tags_one - tags_two
print(exclusive_to_tag_one)
"""
# so you can obviously flip this and see those only in tags_two


#Universal tags - tags have to be in both
universal_tags = tags_one & tags_two
print(universal_tags)