from requests import Request, Session

s = Session()
req = Request('GET', 'https://youtube.com/results?search_query=Epik+High')
prepped = s.prepare_request(req)

# do something with prepped.body
# do something with prepped.headers
print(prepped.headers)

resp = s.send(prepped
	# ,
    # stream=stream,
    # verify=verify,
    # proxies=proxies,
    # cert=cert,
    # timeout=timeout
)

print(resp.headers)