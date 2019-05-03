def urlprint(protocol, host, domain):
  url = '{}://{}.{}'.format(protocol, host, domain)
  # use unittest.mock to redirect print from stdout
  print(url)