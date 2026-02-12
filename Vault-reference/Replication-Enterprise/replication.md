vault read sys/replication/status
vault write -f sys/replication/dr/primary/enable
vault write sys/replication/dr/primary/secondary-token-id=<name>
vault write sys/replication/dr/secondary/enable token=<token>

🟣 vault write -f sys/replication/... — enable DR or performance replication

🟣 Requires Vault Enterprise