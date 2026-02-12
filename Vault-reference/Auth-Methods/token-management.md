# Token Authentication

# Token Management
vault token create -ttl=1h
vault login <token>
vault token lookup
vault token lookup <token>
vault token revoke <token>
vault token renew

🟡 vault token create — generate a new token

🟡 vault token revoke — invalidate a token manually

#vault #auth #token-auth