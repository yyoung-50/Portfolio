# Secrets Management

vault kv put secret/myapp key=value
vault kv put secret/myapp @data.json	Store from JSON file
vault kv get secret/myapp
vault kv delete secret/myapp

# Secret Versions
vault kv undelete --versions=1 secret/myapp
vault kv get -version=2 secret/myapp	Get specific version
vault kv rollback -version=1 secret/myapp	Rollback to version
vault kv destroy -versions=2,3 secret/myapp	Destroy versions
vault kv undelete -versions=2 secret/myapp	Undelete versions
vault kv metadata delete secret/myapp

🟤 vault kv put — store secrets

🟤 vault kv undelete — recover deleted versions

🟤 vault kv metadata delete — permanently remove metadata


# Command	                                                # Description
vault kv put secret/myapp username=admin password=secret	Store secret
vault kv get secret/myapp	                                Retrieve secret
vault kv get -field=password secret/myapp	                Get specific field
vault kv delete secret/myapp	                            Delete secret
vault kv list secret/	                                    List secrets
vault kv metadata get secret/myapp	                        Get metadata