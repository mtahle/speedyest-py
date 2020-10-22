import speedtest   

st = speedtest.Speedtest()

servernames =[]  
st.get_servers(servernames)
# download = st.download()
upload = round(st.upload()/1024/1024)
ping = st.results.ping
print 'Internet speed test- > ', 'ping:', ping,',','Upload:', upload