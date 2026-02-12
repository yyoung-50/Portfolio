






Introduction to Vault

**Part 1: Basic Server Status**

1.  Check the status of your Vault server:

vault status

This shows:

- Seal Status

- Initialize Status

- Server Version

- Storage Type

- HA Status

2.  Authenticate to Vault using the root token:

vault login root

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

Notice that several auth methods are available, including AppRole

2.  Get detailed auth method information:

vault auth list -detailed

**Part 4: Basic Key-Value Operations**

1.  Write a secret:

vault kv put secret/first hello=world

vault kv put secret/my-secret username=admin password=secret123

2.  Read a secret:

vault kv get secret/first

vault kv get -field=hello secret/first

3.  List secrets in a path:

vault kv list secret/

4.  Delete a secret:

vault kv delete secret/first

**Part 5: Token Information**

1.  View current token information:

vault token lookup

2.  View token capabilities:

vault token capabilities secret/first

3.  Create a new token:

vault token create -ttl=1h

**Challenge Exercise**

1.  Use JSON format for secret data:

vault kv put secret/user - \<\<EOF

{

\"data\": {

\"username\": \"admin\",

\"password\": \"secret\",

\"email\": \"admin@example.com\"

}

}

EOF

**Key Commands Summary**

- vault status - Check server status

- vault secrets list - List secret engines

- vault auth list - List auth methods

- vault kv put - Write secrets

- vault kv get - Read secrets

- vault kv list - List secrets

- vault token lookup - View token info

**Learning Resources**

- [[Vault CLI
  Commands]{.underline}](https://developer.hashicorp.com/vault/docs/commands)

- [[KV Secrets
  Engine]{.underline}](https://developer.hashicorp.com/vault/docs/secrets/kv)

- [[Getting Started
  Guide]{.underline}](https://developer.hashicorp.com/vault/tutorials/getting-started)

Storage Backends

<https://developer.hashicorp.com/vault/docs/configuration/storage>

Secrets Engines

<https://developer.hashicorp.com/vault/docs/secrets>

Auth Methods

<https://developer.hashicorp.com/vault/docs/auth>

Vault Security Model

<https://developer.hashicorp.com/vault/docs/internals/security>

Seal and Unseal

<https://developer.hashicorp.com/vault/docs/concepts/seal>

Seal and Unseal configuration

<https://developer.hashicorp.com/vault/docs/configuration/seal>

Seal and unseal aws

<https://developer.hashicorp.com/vault/docs/configuration/seal/awskms>

Audit Devices

<https://developer.hashicorp.com/vault/docs/audit>

Using the Vault CLI

**Initial Setup**

Let\'s verify your environment and set initial variables:

\# Verify Vault is running

vault status

\# Set Vault address and token (if not already set)

export VAULT_ADDR=\'http://127.0.0.1:8200\'

export VAULT_TOKEN=\'root\'

**Part 1: Basic CLI Operations**

1.  **Help and Documentation**

\# Get general help

vault help

\# Get help for a specific command

vault kv help

2.  **Server Information**

\# Check server status

vault status

\# View server configuration

vault read sys/config/state/sanitized

**Part 2: Working with Secrets**

1.  **Enable KV Secrets Engine**

\# Enable KV version 2 at path \'secrets\'

vault secrets enable -path=prd-secrets -version=2 kv

\# Verify enabled secrets engines

vault secrets list

2.  **Managing Secrets**

\# Create a secret

vault kv put prd-secrets/myapp/config \\

database_url=\"postgresql://localhost:5432/mydb\" \\

api_key=\"super-secret-123\"

\# Read a secret

vault kv get prd-secrets/myapp/config

\# Read specific version

vault kv get -version=1 prd-secrets/myapp/config

\# Read specific field

vault kv get -field=api_key prd-secrets/myapp/config

\# Format output as JSON

vault kv get -format=json prd-secrets/myapp/config

\# Update a secret

vault kv patch prd-secrets/myapp/config \\

api_key=\"new-secret-456\"

\# Delete latest version of a secret

vault kv delete prd-secrets/myapp/config

\# Permanently delete all versions

vault kv metadata delete prd-secrets/myapp/config

**Part 3: Policy Management**

1.  **Create a Policy**

\# Create policy file

cat \> app-policy.hcl \<\< EOF

path \"prd-secrets/data/myapp/\*\" {

capabilities = \[\"read\", \"list\"\]

}

path \"prd-secrets/metadata/myapp/\*\" {

capabilities = \[\"list\", \"read\"\]

}

EOF

\# Write policy to Vault

vault policy write app-reader app-policy.hcl

\# View policy

vault policy read app-reader

\# List all policies

vault policy list

**Part 4: Auth Methods**

1.  **Enable UserPass Auth**

\# Enable userpass auth method

vault auth enable userpass

\# Create a user

vault write auth/userpass/users/myapp \\

password=\"password123\" \\

policies=\"app-reader\"

\# List users

vault list auth/userpass/users

2.  **Login with UserPass**

\# Login and save token

VAULT_TOKEN=\$(vault login -method=userpass \\

username=myapp \\

password=password123 \\

-format=json \| jq -r \'.auth.client_token\')

\# Verify token and permissions

vault token lookup

**Part 5: Advanced Operations**

1.  **Secret Versioning**

\# Update secret multiple times

vault kv put prd-secrets/myapp/config message=\"version 1\"

vault kv put prd-secrets/myapp/config message=\"version 2\"

vault kv put prd-secrets/myapp/config message=\"version 3\"

\# Soft delete latest version

vault kv delete prd-secrets/myapp/config

\# Undelete version

vault kv undelete -versions=3 prd-secrets/myapp/config

2.  **Metadata Operations**

\# Add custom metadata and set the maximum versions of the secret

vault kv metadata put \\

-max-versions 5 \\

-custom-metadata \"environment=development\" \\

prd-secrets/myapp/config

\# Read metadata and see versions of secrets

vault kv metadata get prd-secrets/myapp/config

**🔍 Practice Exercises**

Try these exercises to reinforce your learning:

1.  **Basic Operations**

    - Create a new secret with multiple key-value pairs

    - Read specific fields from the secret

    - Update only one field using patch

    - Delete and undelete the secret

2.  **Policy Practice**

    - Create a policy that allows create and update but not delete

    - Create a new user with this policy

    - Test the permissions work as expected

3.  **Advanced Tasks**

    - Enable a new secrets engine at a custom path

    - Configure custom metadata for a secret

    - Work with secret versioning

**🎯 Success Criteria**

You\'ve completed the lab when you can:

-  Manage secrets using the CLI

-  Create and apply policies

-  Work with authentication methods

-  Handle secret versioning

-  Perform metadata operations

**📚 Common CLI Options**

- -format=json: Output in JSON format

- -field=key: Extract specific field

- -mount=path: Specify mount path

- -namespace=ns: Work in specific namespace (Enterprise)

**❓ Troubleshooting**

**Common Issues:**

1.  **Permission Denied**: Check your token\'s policies

2.  **Connection Failed**: Verify VAULT_ADDR is set correctly

3.  **Token Expired**: Login again to get a new token

**🔍 Additional CLI Tips**

1.  **Environment Variables**

\# Common Vault environment variables

export VAULT_ADDR=\'http://127.0.0.1:8200\'

export VAULT_TOKEN=\'your-token\'

export VAULT_NAMESPACE=\'admin\' \# Enterprise only

export VAULT_FORMAT=\'json\' \# Always output in JSON

2.  **Using jq with Vault**

\# Extract specific fields from JSON output

vault kv get -format=json prd-secrets/myapp/config \| jq -r
\'.data.data.api_key\'

\# Process multiple secrets

vault kv list -format=json prd-secrets/myapp/ \| jq -r
\'.data.keys\[\]\'

**📚 Additional Resources**

- [[Vault CLI
  Documentation]{.underline}](https://www.vaultproject.io/docs/commands)

- [[Vault Policy
  Documentation]{.underline}](https://www.vaultproject.io/docs/concepts/policies)

- [[Vault Auth
  Methods]{.underline}](https://www.vaultproject.io/docs/auth)

Using Audit Devices

** Verify Vault Status**

First, ensure Vault is running and you\'re authenticated:

\# Check Vault status

vault status

\# Log in with a valid token

vault login root

Note: If you are performing the labs on your own machine, you might need
to add sudo before the following commands to work. This is not necessary
on the Codespace instance since it automatically logs you in as
the root user.

**2. Enable File Audit Device**

Enable the file audit device and configure it to write to a specific
file:

\# Create directory for audit logs with appropriate permissions

mkdir -p /var/log/vault

chown vault:vault /var/log/vault

\# Enable file audit device

vault audit enable file file_path=/var/log/vault/audit.log

\# Verify audit device is enabled

vault audit list

\# View more details about the audit device, including the targeted
path/file

vault audit list \--detailed

**3. Generate Audit Events**

Perform various operations to generate audit logs:

a\. Create a secret:

\# Enable KV secrets engine if not already enabled

vault secrets enable -path=secret kv-v2

\# Repeat the step above to purposely create an error

vault secrets enable -path=secret kv-v2

\# Create a test secret

vault kv put secret/test-secret username=admin password=vault-demo

b\. Read the secret:

vault kv get secret/test-secret

c\. Update the secret:

vault kv put secret/test-secret username=admin password=updated-password

d\. List secrets:

vault kv list secret/

e\. Delete the secret:

vault kv delete secret/test-secret

**4. Examine Audit Logs**

Review and analyze the generated audit logs:

\# View raw audit logs

cat /var/log/vault/audit.log

\# Parse JSON logs with jq (if installed)

cat /var/log/vault/audit.log \| jq \'.\'

\# Search for specific operations performed above

grep \"secret/test-secret\" /var/log/vault/audit.log \| jq \'.\'

**5. Understanding Audit Log Structure**

Each audit log entry contains:

- timestamp

- type (request/response)

- auth information

- request/response data

- error information (if applicable)

Example analysis tasks:

\# Find all KV secret operations

grep \"secret/\" /var/log/vault/audit.log \| jq \'.\'

\# Look for specific authentication events

grep \"login\" /var/log/vault/audit.log \| jq \'.\'

\# Find error events

grep \"error\" /var/log/vault/audit.log \| jq \'.\'

**6. Log Rotation Practice**

Set up basic log rotation:

\# Create logrotate configuration

tee /etc/logrotate.d/vault \<\<EOF

/var/log/vault/audit.log {

daily

rotate 7

compress

delaycompress

missingok

notifempty

create 0640 vault vault

}

EOF

\# View the contents of the vault audit directory (and see there\'s only
one file)

ls /var/log/vault

\# Force a log rotatation

logrotate -f /etc/logrotate.d/vault

\# View the contents of the vault audit directory (and see the rotated
file)

\# Notice that audit.log is now empty

ls /var/log/vault

**7. Audit Device Management**

Practice common management tasks:

\# Disable audit device

vault audit disable file/

\# Re-enable with different options

vault audit enable -path=file2 file file_path=/var/log/vault/audit2.log

\# List all enabled audit devices

vault audit list -detailed

**Challenge Exercises**

1.  **Log Analysis Challenge**

    - Enable multiple auth methods (userpass, approle)

    - Generate login attempts with both successful and failed
      authentications

    - Use grep and jq to find all failed login attempts

2.  **Multiple Audit Devices**

    - Enable two file audit devices with different paths

    - Compare the logs between them

    - Understand the implications of multiple audit devices

3.  **Log Rotation Testing**

    - Generate a large number of audit events

    - Trigger manual log rotation

    - Verify rotated logs are properly compressed

**Troubleshooting Guide**

Common issues and solutions:

1.  **Permission Issues**

\# Fix permissions on audit log directory

chown -R vault:vault /var/log/vault

chmod 0740 /var/log/vault

2.  **Disk Space Management**

\# Check disk space usage

du -sh /var/log/vault/

\# Clean up old rotated logs

find /var/log/vault/ -name \"audit.log.\*\" -mtime +30 -delete

3.  **Audit Device Failures**

- Remember: If all audit devices fail, Vault will no longer respond to
  clients

- Always have sufficient disk space

- Monitor log file permissions

**Lab Cleanup**

\# Disable audit device

vault audit disable file/

\# Remove audit logs

rm -rf /var/log/vault/audit.log\*

\# Remove logrotate configuration

rm /etc/logrotate.d/vault

**Additional Resources**

- [[Vault Audit Devices
  Documentation]{.underline}](https://www.vaultproject.io/docs/audit)

- [[Vault Audit Devices
  API]{.underline}](https://www.vaultproject.io/api-docs/system/audit)

- [[Log Rotation Best
  Practices]{.underline}](https://www.vaultproject.io/docs/configuration/listener/tcp#rotation)

Vault Policies

**Part 1: Creating Your First Policy**

1.  First, verify that Vault is running and you\'re authenticated:

\# Log in with a valid token

vault login root

\# Check the status of the service

vault status

2.  Create a new file called readonly-policy.hcl in your VS Code editor
    with these contents:

\# Allow read-only access to secrets in the \'secret\' path

path \"secret/data/\*\" {

capabilities = \[\"read\", \"list\"\]

}

path \"secret/metadata/\*\" {

capabilities = \[\"list\"\]

}

3.  Write this policy to Vault:

vault policy write readonly-policy readonly-policy.hcl

4.  Verify the policy was created:

vault policy list

vault policy read readonly-policy

**Part 2: Testing Policy Restrictions**

1.  Create some test secrets:

\# Create two test secrets

vault kv put secret/test-1 password=\"secret123\"

vault kv put secret/test-2 api_key=\"abc123\"

2.  Create a token with the readonly policy:

vault token create -policy=readonly-policy

3.  Copy the token value and set it in your environment:

export VAULT_TOKEN=\"\<paste-token-here\>\"

4.  Test the policy restrictions:

\# These should work

vault kv get secret/test-1

vault kv list secret/

\# These should fail

vault kv put secret/test-3 password=\"newpass\"

vault kv delete secret/test-1

5.  When you\'re finished, log back in as root:

unset VAULT_TOKEN

vault login root

**Part 3: Creating a More Complex Policy with Entity Templating**

1.  Create the Policy

Create a file called app-policy.hcl with the following contents:

\# Allow management of app-specific secrets

path \"secret/data/app/{{identity.entity.name}}/\*\" {

capabilities = \[\"create\", \"read\", \"update\", \"delete\",
\"list\"\]

}

\# Allow listing of secret mount

path \"secret/metadata/\*\" {

capabilities = \[\"list\"\]

}

2.  Then, write the policy:

vault policy write app-policy app-policy.hcl

3.  Enable and Configure the Userpass Auth Method:

vault auth enable userpass

4.  Get the Userpass Accessor and set to a variable:

USERPASS_ACCESSOR=\$(vault auth list -format=json \| jq -r
\'.\"userpass/\".accessor\')

5.  Create an entity used to map the user to the policy:

vault write identity/entity name=\"app1\" policies=\"app-policy\"

Note the entity ID in the output.

6.  Create the Entity Alias for the Userpass user:

vault write identity/entity-alias \\

name=\"app1\" \\

mount_accessor=\"\$USERPASS_ACCESSOR\" \\

canonical_id=\"\<add_entity_id_here\>\"

Use the entity ID from the previous step in this command.

7.  Create the Userpass User

vault write auth/userpass/users/app1 \\

password=\"password123\"

8.  Test Login and Permissions using the Templated Policy:

\# Login as the user

vault login -method=userpass \\

username=app1 \\

password=password123

\# These should succeed

vault kv put secret/app/app1/config api_key=\"test123\"

vault kv get secret/app/app1/config

\# These should fail with 403

vault kv put secret/app/other-app/config api_key=\"test123\"

vault kv put secret/test-3 password=\"newpass\"

9.  When you\'re finished, log back in as root:

unset VAULT_TOKEN

vault login root

**Part 4: Understanding Policy Precedence**

1.  Create a new file called mixed-policy.hcl:

\# Grant some permissions

path \"secret/data/shared/\*\" {

capabilities = \[\"create\", \"read\", \"update\", \"list\"\]

}

\# But deny specific paths

path \"secret/data/shared/restricted/\*\" {

capabilities = \[\"deny\"\]

}

2.  Write and test the policy:

vault policy write mixed-policy mixed-policy.hcl

vault token create -policy=mixed-policy

\# Set your token to the new one

export VAULT_TOKEN=\"\<new-token\>\"

\# Test the permissions

vault kv put secret/shared/public data=\"public-info\" \# Should work

vault kv put secret/shared/restricted/secret data=\"sensitive\" \#
Should fail

**Cleanup**

1.  Return to your root token:

export VAULT_TOKEN=\"root\"

2.  Remove the policies and secrets:

vault policy delete readonly-policy

vault policy delete app-policy

vault policy delete mixed-policy

vault kv delete secret/test-1

vault kv delete secret/test-2

vault kv delete secret/app/app1/config

vault kv delete secret/shared/public

**Challenge Exercise**

Create a policy that:

- Allows read access to all secrets in secret/data/team-a/\*

- Allows write access only to secret/data/team-a/projects/\*

- Denies access to secret/data/team-a/admin/\*

- Allows listing capabilities on all paths

**Learning Resources**

- [[Vault Policies
  Documentation]{.underline}](https://developer.hashicorp.com/vault/docs/concepts/policies)

- [[Policy Syntax
  Documentation]{.underline}](https://developer.hashicorp.com/vault/docs/concepts/policies#policy-syntax)

- [[Policy Templates
  Documentation]{.underline}](https://developer.hashicorp.com/vault/docs/concepts/policies#policy-templates)

Working with Tokens

**Part 1: Service Tokens**

1.  Create basic service token:

\# Log in with a valid token

vault login root

\# Create a token

vault token create

2.  Create token with policy:

vault token create \\

-policy=\"default\" \\

-ttl=\"1h\" \\

-explicit-max-ttl=\"2h\"

**Part 2: Batch Tokens**

1.  Create batch token:

vault token create -type=batch \\

-ttl=\"1h\" \\

-policy=\"default\"

2.  Compare properties:

\# Lookup service token

vault token lookup \<service_token\>

\# Lookup batch token (notice fewer properties)

vault token lookup \<batch_token\>

**Part 3: Periodic Tokens**

1.  Create periodic token:

vault token create -period=\"24h\" \\

-policy=\"default\"

2.  Renew periodic token:

vault token renew \<periodic_token\>

**Part 4: Orphan Tokens**

1.  Create orphan token:

vault token create -orphan \\

-policy=\"default\" \\

-ttl=\"1h\"

2.  View token hierarchy:

\# Create child of service token

VAULT_TOKEN=\<service_token\> vault token create

\# Create orphan - no parent relationship

vault token create -orphan

**Part 5: Token Roles**

1.  Create token role:

vault write auth/token/roles/app-role \\

allowed_policies=\"default\" \\

orphan=true \\

token_period=\"1h\" \\

renewable=true

2.  Create token from role:

vault token create -role=app-role

**Challenge Exercises**

1.  Token Lifecycle:

    - Create periodic token

    - Renew it multiple times

    - Verify period remains constant

2.  Token Hierarchy:

    - Create parent token

    - Create child tokens

    - Revoke parent

    - Check child status

**Key Differences**

- Service Tokens: Default, renewable

- Batch Tokens: Lightweight, non-renewable

- Periodic Tokens: Auto-renewable indefinitely

- Orphan Tokens: No parent relationship

**Cleanup**

export VAULT_TOKEN=\"root\"

\# Revoke tokens

vault token revoke \<token\>

\# Remove token role

vault delete auth/token/roles/app-role

PKI Secrets Engine (Public Key Infrastructure)

**Step 1: Enable the PKI Secrets Engine**

1.  First, enable a PKI secrets engine for the root CA:

vault secrets enable -path=pki_root pki

2.  Configure the maximum lease TTL to 10 years:

vault secrets tune -max-lease-ttl=87600h pki_root

**Step 2: Generate Root CA**

1.  Generate and view the root certificate directly in the CLI:

vault write pki_root/root/generate/internal \\

common_name=\"Lab Root CA\" \\

ttl=87600h

2.  Generate it again but save to a file for later use:

vault write -format=json pki_root/root/generate/internal \\

common_name=\"Lab Root CA\" \\

ttl=87600h \> root_ca.json

cat root_ca.json \| jq -r .data.certificate \> root_ca.pem

3.  Configure the CA and CRL URLs:

vault write pki_root/config/urls \\

issuing_certificates=\"http://vault.lab:8200/v1/pki_root/ca\" \\

crl_distribution_points=\"http://vault.lab:8200/v1/pki_root/crl\"

**Step 3: Create Intermediate CA**

1.  Enable a PKI secrets engine for the intermediate CA:

vault secrets enable -path=pki_int pki

2.  Set a shorter max TTL for the intermediate CA (5 years):

vault secrets tune -max-lease-ttl=43800h pki_int

3.  Generate and view the intermediate CSR directly:

vault write pki_int/intermediate/generate/internal \\

common_name=\"Lab Intermediate CA\" \\

ttl=43800h

4.  Generate it again and save to a file:

vault write -format=json pki_int/intermediate/generate/internal \\

common_name=\"Lab Intermediate CA\" \\

ttl=43800h \> intermediate.json

cat intermediate.json \| jq -r .data.csr \> intermediate.csr

5.  Sign the intermediate CSR with the root CA and save to a file:

vault write -format=json pki_root/root/sign-intermediate \\

csr=@intermediate.csr \\

format=pem_bundle \\

ttl=43800h \> signed_intermediate.json

cat signed_intermediate.json \| jq -r .data.certificate \>
signed_intermediate.pem

7.  Import the signed certificate back into the Vault Intermediate:

vault write pki_int/intermediate/set-signed \\

certificate=@signed_intermediate.pem

**Step 4: Create a Role for Issuing Certificates**

1.  Create a role for issuing certificates for a webapp:

vault write pki_int/roles/webapp \\

allowed_domains=\"lab.local\" \\

allow_subdomains=true \\

max_ttl=720h \\

key_type=\"rsa\" \\

key_bits=2048 \\

allowed_uri_sans=\"dns://lab.local\" \\

require_cn=true \\

basic_constraints_valid_for_non_ca=true

**Step 5: Generate a Certificate for the webapp:**

1.  Generate and view a certificate directly in the CLI:

vault write pki_int/issue/webapp \\

common_name=\"webapp.lab.local\" \\

ttl=72h

This will display:

- The certificate

- The private key (Vault will only output the private key once)

- CA chain

- Serial number

- Other metadata

2.  Issue a certificate and save it to files (useful for deploying to
    services):

vault write -format=json pki_int/issue/webapp \\

common_name=\"webapp.lab.local\" \\

ttl=72h \> webapp_cert.json

\# Extract each component to its own file

cat webapp_cert.json \| jq -r .data.certificate \> webapp_cert.pem

cat webapp_cert.json \| jq -r .data.private_key \> webapp_key.pem

cat webapp_cert.json \| jq -r .data.ca_chain\[\] \> webapp_ca_chain.pem

\# \[Optional\] View each file to see the contents

cat webapp_cert.pem

cat webapp_key.pem

cat webapp_ca_chain.pem

**Step 6: Verify the Certificate**

1.  View the certificate details:

\# For the CLI-generated certificate, copy the certificate content to a
file first

\# For the file-based certificate:

openssl x509 -in webapp_cert.pem -text -noout

**Step 7: Working with Certificate Revocation**

1.  View a certificate\'s serial number:

\# Directly from CLI output when generating

vault write pki_int/issue/webapp common_name=\"temp.lab.local\" ttl=72h

\# Or from a saved certificate

openssl x509 -in webapp_cert.pem -noout -serial

2.  Revoke a certificate:

vault write pki_int/revoke \\

serial_number=\<serial_number_from_certificate\>

3.  Generate a new CRL:

vault write pki_int/config/urls \\

issuing_certificates=\"http://vault.lab:8200/v1/pki_int/ca\" \\

crl_distribution_points=\"http://vault.lab:8200/v1/pki_int/crl\"

**Create a Vault Policy for the Application named webapp to Generate a
PKI Certificate**

1.  Create a new file named webapp-policy.hcl

**Right-click** in the left navigation pane or use the command touch
webapp-policy.hcl

\# Permit reading the configured certificates

path \"pki_int/cert/\*\" {

capabilities = \[\"read\", \"list\"\]

}

\# Permit creating certificates from the webapp role

path \"pki_int/issue/webapp\" {

capabilities = \[\"create\", \"update\"\]

}

\# Allow reading the CRL and CA certificate

path \"pki_int/cert/ca\" {

capabilities = \[\"read\"\]

}

path \"pki_int/cert/crl\" {

capabilities = \[\"read\"\]

}

2.  Write the policy to Vault:

vault policy write policy-webapp-pki webapp-policy.hcl

Note: In production, you would most likely attach this policy to your
webapp\'s authentication role to give it the authorization to generate
certificates (among other permissions it might need).

**Challenge Exercises**

1.  Create certificates with different parameters:

    - Generate a certificate with multiple Subject Alternative Names
      (SANs):

    - vault write pki_int/issue/webapp \\

    - common_name=\"webapp.lab.local\" \\

    - alt_names=\"app.lab.local,api.lab.local\" \\

> ttl=72h

- Save the multi-SAN certificate to files

- Compare the CLI output with the saved files

2.  Create a wildcard certificate:

3.  vault write pki_int/issue/webapp \\

4.  common_name=\"\*.lab.local\" \\

> ttl=72h

5.  Implement certificate rotation:

    - Issue a certificate with a 1-hour TTL

    - Write a script to check expiration and auto-renew

    - Handle both CLI output and file-based storage

**Clean Up**

1.  Revoke all certificates issued by the intermediate CA:

vault write pki_int/tidy \\

tidy_cert_store=true \\

tidy_revoked_certs=true \\

safety_buffer=72h

2.  Disable the PKI secrets engines:

vault secrets disable pki_root

vault secrets disable pki_int

3.  Remove generated files:

rm \*.json \*.pem \*.csr

**Best Practices**

1.  **Certificate Generation**:

    - Use CLI output for testing and verification

    - Use file-based storage for production deployments

    - Always secure private key files with appropriate permissions

2.  **Root CA Management**:

    - Keep the root CA offline when not in use

    - Use long validity periods for root CAs

    - Maintain secure backups of root CA private keys

3.  **Intermediate CA**:

    - Use intermediate CAs for day-to-day certificate issuance

    - Implement regular rotation of intermediate CA certificates

    - Maintain separate intermediates for different environments

4.  **Monitoring and Auditing**:

    - Regular monitoring of certificate expiration

    - Audit of certificate issuance and revocation

    - Monitoring of CRL and OCSP availability

**Conclusion**

In this lab, you learned how to:

- Set up a complete PKI infrastructure using Vault

- Generate and manage root and intermediate CAs

- Issue certificates using both CLI and file-based methods

- Implement certificate management best practices

**Additional Resources**

- [[Vault PKI Secrets Engine
  Documentation]{.underline}](https://www.vaultproject.io/docs/secrets/pki)

- [[OpenSSL Documentation]{.underline}](https://www.openssl.org/docs/)

- [[PKI Best
  Practices]{.underline}](https://www.hashicorp.com/blog/certificate-management-with-vault)

- [[Automated Certificate
  Management]{.underline}](https://learn.hashicorp.com/tutorials/vault/pki-engine)

Transit Secrets Engine

1.  Enable the Transit engine:

\# Log in with a valid token

vault login root

\# Enable the Transit secrets engine

vault secrets enable transit

2.  Create an encryption key:

vault write -f transit/keys/my-app

**Part 1: Basic Encryption/Decryption**

1.  Encrypt data:

\# Encode data in base64

echo -n \"sensitive data\" \| base64

\# Encrypt the data

vault write transit/encrypt/my-app plaintext=\$(echo -n \"sensitive
data\" \| base64)

2.  Decrypt data:

\# Store the ciphertext from previous step

CIPHER=\"vault:v1:abc123\...\" \# Use your actual ciphertext

\# Decrypt

vault write transit/decrypt/my-app ciphertext=\$CIPHER

3.  Decode the result:

echo \"base64-output\" \| base64 -d \# Replace with actual output

**Part 2: Key Rotation**

1.  Rotate the encryption key:

vault write -f transit/keys/my-app/rotate

2.  Check key details:

vault read transit/keys/my-app

3.  Encrypt new data (uses latest key version):

vault write transit/encrypt/my-app plaintext=\$(echo -n \"new data\" \|
base64)

**Part 3: Key Management**

1.  Update key configuration:

\# Set minimum decryption version

vault write transit/keys/my-app/config min_decryption_version=1

\# Set minimum encryption version

vault write transit/keys/my-app/config min_encryption_version=1

\# Enable key deletion

vault write transit/keys/my-app/config deletion_allowed=true

2.  Create key with specific parameters:

vault write transit/keys/my-app-2 \\

type=\"aes256-gcm96\" \\

exportable=false \\

deletion_allowed=true

**Part 4: Data Key Generation**

1.  Generate data key:

vault write -f transit/datakey/plaintext/my-app

2.  Generate wrapped data key:

vault write -f transit/datakey/wrapped/my-app

**Challenge Exercise**

Create an encryption workflow:

1.  Create new encryption key

2.  Encrypt 3 pieces of data

3.  Rotate the key

4.  Encrypt new data

5.  Verify old data still decrypts

6.  List all key versions

**Cleanup**

vault delete transit/keys/my-app

vault delete transit/keys/my-app-2

vault secrets disable transit

**Key Features**

- Key rotation

- Configurable key types

- Versioning support

- Data key generation

- Secure key storage

Key/Value Secrets Engine

Metadata management

1.  Enable KV v1 and v2 engines:

\# Log in with a valid token

vault login root

\# Enable the secrets engines

vault secrets enable -path=kv1 -version=1 kv

vault secrets enable -path=kv2 -version=2 kv

2.  Verify newly mounted secrets engines:

vault secrets list

**Part 1: Basic Operations**

**KV Version 1**

\# Write a secret

vault kv put kv1/app1 username=admin password=secret123

\# Read a secret

vault kv get kv1/app1

\# Update a secret

vault kv put kv1/app1 username=admin password=newpass123

\# Read the updated secret

vault kv get kv1/app1

\# Delete a secret

vault kv delete kv1/app1

\# Read a secret (this should return \"no value found\")

vault kv get kv1/app1

**KV Version 2**

\# Write a secret

vault kv put kv2/app1 username=admin password=secret123

\# Read a secret

vault kv get kv2/app1

\# Update a secret

vault kv put kv2/app1 username=admin password=newpass123

\# Read the updated secret (notice it\'s now version 2)

vault kv get kv2/app1

\# Delete latest version

vault kv delete kv2/app1

\# Read the updated secret (notice only metadata is returned - but no
data)

vault kv get kv2/app1

**Part 2: KV v2 Versioning Features**

1.  Create multiple versions:

vault kv put kv2/config api_key=v1

vault kv put kv2/config api_key=v2

vault kv put kv2/config api_key=v3

2.  Read specific versions:

vault kv get -version=1 kv2/config

vault kv get -version=2 kv2/config

vault kv get -version=3 kv2/config

3.  View version metadata:

vault kv metadata get kv2/config

4.  Roll back to previous version:

vault kv rollback -version=1 kv2/config

5.  Read the latest version (notice it\'s now the same as v1)

vault kv get kv2/config

**Part 3: KV v2 Soft Delete**

1.  Delete and recover:

\# Delete latest version

vault kv delete kv2/app1

\# Read the latest version(notice only metadata is returned)

vault kv get kv2/app1

\# Undelete the version

vault kv undelete -versions=1 kv2/app1

\# Read the latest version(notice the data is back)

vault kv get kv2/app1

\# Permanently delete version

vault kv destroy -versions=1 kv2/app1

**Part 4: KV v2 Metadata Operations**

1.  Set custom metadata:

vault kv metadata put -custom-metadata=owner=\"ops\"
-custom-metadata=env=\"prod\" kv2/app1

2.  Read the secret and notice the custom metadata returned

vault kv get kv2/app1

3.  Configure the maximum number of versions for the specific path:

vault kv metadata put -max-versions=5 kv2/app1

4.  Delete all versions and metadata:

vault kv metadata delete kv2/app1

**Challenge Exercises**

1.  Version Management:

    - Create 3 versions of a secret

    - Delete version 2

    - Recover version 2

    - Verify all versions

2.  Metadata Management:

    - Create a secret with custom metadata

    - Update metadata without changing secret

    - List all metadata

    - Delete specific metadata fields

**Key Differences Summary**

- KV v1: No versioning, simple storage

- KV v2:

  - Version history

  - Soft delete

  - Metadata management

  - Rollback capability

  - Scheduled deletion

**Cleanup**

vault secrets disable kv1

vault secrets disable kv2
