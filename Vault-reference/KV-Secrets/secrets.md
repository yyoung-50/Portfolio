vault secrets list
vault secrets list --detailed
vault secrets enable <type>
vault secrets enable -path=<path> <type>
vault secrets disable <path>

🟢 vault secrets enable — activate KV, PKI, Transit, etc.

🟢 vault secrets disable — remove a secrets engine