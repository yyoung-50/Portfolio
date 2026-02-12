# Policy Management

vault policy list
vault policy write <policy_name> <file.hcl>
vault policy write my-policy <<EOF
<rules>
EOF

vault policy read <name>
vault policy delete <name>

vault policy write — define ACL rules

vault policy read — view policy contents

# Create a Policy

# Create policy file

cat \> app-policy.hcl \<\< EOF

path \"prd-secrets/data/myapp/\*\" {

capabilities = \[\"read\", \"list\"\]

}

path \"prd-secrets/metadata/myapp/\*\" {

capabilities = \[\"list\", \"read\"\]

}

EOF

# Write policy to Vault

vault policy write app-reader app-policy.hcl

# View policy

vault policy read app-reader

# List all policies

vault policy list