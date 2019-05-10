def spam():
  print("spam")

def grok():
  print("grok")

blah = 42

# Only export 'spam' and 'grok'
__all__ = ['spam', 'grok']
