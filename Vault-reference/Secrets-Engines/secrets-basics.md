# secret engine basics

**Part 2: Secret Engines**

1.  List enabled secret engines:

vault secrets list

Notice there are several secrets engines already enabled, including a KV
store at secrets/

2.  Get information about a specific secrets engine:

vault secrets list -detailed

**Part 3: Authentication Methods**

1.  List enabled auth methods:

vault auth list



# Get detailed auth method information

vault auth list -detailed



# Write a secret

vault kv put secret/first hello=world

vault kv put secret/my-secret username=admin password=secret123

# Read a secret

vault kv get secret/first

vault kv get -field=hello secret/first

# List secrets in a path:

vault kv list secret/

# Delete a secret:

vault kv delete secret/first