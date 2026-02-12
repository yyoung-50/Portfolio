📘 HASHICORP VAULT — PRACTICAL COMMAND REFERENCE GUIDE
A fast lookup guide for real-world Vault operations

# Key Commands Summary
vault status - Check server status
vault secrets list - List secret engines
vault auth list - List auth methods
vault kv put - Write secrets
vault kv get - Read secrets
vault kv list - List secrets
vault token lookup - View token info

AWS Commands
# Copy a file to EC2 Instance using pscp.exe
Browse to c:\Program Files\Putty, then run the command below 
pscp -i C:\Users\young\OneDrive\SharedKey\us-east-kp6.ppk C:\Tools\auth.json ec2-user@54.163.194.130:/home/ec2-user/
# Note: Download the PSCP.exe and place in the PUTTY install folder to run

# Note: to connect to EC2 instance via SSH
Convert the *.pem file to *.ppk, then upload to Putty.exe and save the session
In putty configuration go to SSH --> Auth --> Credentials. in credentials, browse to *.ppk file and save the session

🔐 1. KV v2 COMMANDS (vaultcourse/ mount)

# Log in with a valid token
vault login root

# Enable the secrets engines
vault secrets enable -path=kv1 -version=1 kv
vault secrets enable -path=kv2 -version=2 kv

# Write a secret
vault kv put vaultcourse/app01/test password="Password1!"

# Generate secret-id
vault write -f auth/approle/role/bryan/secret-id

# Read a secret
vault kv get vaultcourse/app01/test

# List keys
vault kv list vaultcourse/app01

# Delete (soft delete)
vault kv delete vaultcourse/app01/test

# Destroy (permanent)
vault kv destroy -versions=1 vaultcourse/app01/test

# Undelete
vault kv undelete -versions=1 vaultcourse/app01/test

🔐 2. AUTH METHOD COMMANDS

# List enabled auth methods
vault auth list
# Enable an auth method
vault auth enable userpass

# Enable at custom path
vault auth enable -path=bryan userpass

# Disable an auth method
vault auth disable userpass/

# Create a userpass user (Create a userpass user)

vault write auth/userpass/users/bryan \
    password="mypassword" \
    policies="default,admin"

# View userpass users
vault list auth/userpass/users

# View config of user
vault read auth/userpass/users/frank

 🔑 3. TOKEN COMMANDS
# Login (userpass)
vault login -method=userpass username=bryan

# Lookup current token (Vault’s whoami)
vault token lookup

# Create a token
vault token create -policy=admin
vault token create -ttl=1h
vault token create -policy=root -ttl=24h

# Note: when you create a new token, export it
Run command export VAULT_TOKEN="s.ABCDEVGETDSTETTP"

- Export a periodic token so the Vault CLI uses that token for all subsequent commands. Exporting sets the VAULT_TOKEN environment variable, which switches our identity
- Exporting a token prevents accidental renewal of the root token 

# Revoke a token
vault token revoke <token>

# Create a token with policy
vault token create \
    -policy="default" \
    -ttl="1h" \
    -explicit-max-ttl="2h"

# Create a batch token
vault token create -type=batch \
    -ttl="1h" \
    -policy="default"

# Lookup service token
vault token lookup <service_token>

# Lookup batch token (notice fewer properties)
vault token lookup <batch_token>

# Lookup token properties
vault token lookup

# Create a periodic token
vault token create -period="24h" \
    -policy="default

# Renew periodic token
vault token renew <periodic_token>

# Create orphan token
vault token create -orphan \
    -policy="default" \
    -ttl="1h"

# Create child of service token
VAULT_TOKEN=<service_token> vault token create

# Note about creating a child of a service token.
If you are not using the "real root token", you will get "permission denied because, you are using a service token that was created by a root token, not the root token itself. Child tokens cannot create more child tokens unless explicitly allowed.
Run "vault token lookup" and you will see the fields:
- type = service
- orphan = true
- path = auth/token/create
A real root toke would show:
- type = service 
- path = auth/token/root
Therefore, the child token does not have "create" capability on "auth/token/create and therefore cannot create new tokens.

# Create a token role
vault write auth/token/roles/app-role \
    allowed_policies="default" \
    orphan=true \
    token_period="1h" \
    renewable=true

# Create a token from a role
vault token create -role=app-role
# Output
/workspaces/vault-codespaces # vault write auth/token/roles/app-role \
>  allowed_policies="default" \
>  orphan=true \
>  token_period="1h" \
>  renewable=true
Success! Data written to: auth/token/roles/app-role

# view created roles
vault list auth/token/roles
# Output
Success! Data written to: auth/token/roles/app-role
/workspaces/vault-codespaces # vault list /auth/token/roles
Keys
----
app-role

# Create orphan - no parent relationship
vault token create -orphan

📜 4. POLICY COMMANDS
# List policies
vault policy list

# List user policies

# Read a policy
vault policy read admin

# Write a policy
vault policy write admin admin.hcl

# Read a policy
vault policy read admin

# Create admin policy and save to local directory
vault policy write admin-policy - <<EOF
path "secret/*" {
  capabilities = ["create", "read", "update", "delete", "list"]
}
EOF

vault policy write basic-policy - <<EOF
path "secret/data/user1/*" {
  capabilities = ["create", "read", "update", "delete", "list"]
}
EOF

# Delete a policy
vault policy delete admin

🧱 5. SECRETS ENGINE COMMANDS
# List secrets engines or Validate that the KV secrets engines are enabled
vault secrets list

# Enable KV v2
vault secrets enable -path=vaultcourse kv-v2

# Disable a secrets engine
vault secrets disable vaultcourse/

🌐 6. CURL API EXAMPLES (KV v2)
# Write a secret

curl --header "X-Vault-Token: $TOKEN" \
     --request POST \
     --data '{"data": {"password": "Password1!"}}' \
     http://127.0.0.1:8200/v1/vaultcourse/data/app01/test

# Read a secret

curl --header "X-Vault-Token: $TOKEN" \
     http://127.0.0.1:8200/v1/vaultcourse/data/app01/test | jq .

# List keys

curl --header "X-Vault-Token: $TOKEN" \
     http://127.0.0.1:8200/v1/vaultcourse/metadata/app01 | jq .

🔐 7. PERMISSIONS CHEAT SHEET (MOST COMMON PATHS)
# KV v2 read/write

path "vaultcourse/data/app01/*" {
  capabilities = ["create", "read", "update", "delete"]
}
# KV v2 list

path "vaultcourse/metadata/app01/*" {
  capabilities = ["list", "read"]
}

# Allow listing policies

path "sys/policies/acl" {
  capabilities = ["list"]
}

# Allow reading policies

path "sys/policies/acl/*" {
  capabilities = ["read"]
}

# Allow managing auth methods

path "sys/auth/*" {
  capabilities = ["create", "read", "update", "delete", "list"]
}

# Allow managing secrets engines

path "sys/mounts/*" {
  capabilities = ["create", "read", "update", "delete", "list"]
}

# Unset the environment variable
unset VAULT_TOKEN


🛠️ 8. TROUBLESHOOTING GUIDE (REAL-WORLD)
Problem: Permission denied
Cause: Token missing policy or wrong path

Fix:

Check token: vault token lookup

Check policy: vault policy read <policy>

Check mount path: vault secrets list

Problem: KV v2 path not found
Cause: Using KV v1 syntax
Fix:  
Use /data/ and /metadata/ endpoints.

# Problem: Policy changes not taking effect
Cause: Token is old
Fix:  
Re-login to get a fresh token.

Problem: curl returns {"errors":[]}
Cause: You queried a folder, not a secret
Fix:  
Use /metadata/ to list keys
Use /data/<secret> to read

# Problem: Cannot list policies
Cause: Missing access to sys/policies/acl  
Fix:  
Add list/read capabilities for that path.

# ⚠️ 9. MOST COMMON VAULT ERROR MESSAGES (DED)
# permission denied
Your token does not have the required capabilities for that path.

# no value found at <path>
The secret exists logically but has no data (or was deleted).

# unsupported path
You are using the wrong endpoint (KV v1 vs KV v2 mismatch).

# missing client token
You forgot to pass X-Vault-Token or your token expired.

# path is not allowed
Your policy does not match the exact mount path.

# invalid request
Your JSON body is malformed or missing "data": {} for KV v2.

# 403
Same as permission denied — policy issue.

# 404
Path does not exist OR wrong mount path.

# View roles on approle
vault list auth/approle/role

# Create role-id
vault read auth/approle/role/username/role-id

# view created users
vault list auth/userpass/users
# Output if no users found
No value found at auth/userpass/users