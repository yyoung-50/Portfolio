# Installation and Setup

# Command                           Description
vault version	                    Show Vault version
vault server -dev	                Start development server
vault server -config=config.hcl	    Start with configuration file
vault status	                    Check server status

# Manually Install Vault

# Vault installation and System Preparation

1.  Create Vault user and group:

\# Create vault group

sudo groupadd vault

\# Create vault user

sudo useradd -r -m -g vault -d /home/vault -s /bin/bash -c \"Vault
user\" vault

2.  Create necessary directories:

\# Create directories

sudo mkdir -p /opt/vault/data

sudo mkdir -p /etc/vault.d

sudo mkdir -p /var/lib/vault

sudo mkdir -p /usr/local/bin

\# Set ownership

sudo chown -R vault:vault /opt/vault

sudo chown -R vault:vault /etc/vault.d

sudo chown -R vault:vault /var/lib/vault

**Part 2: Installing Vault**

1.  Download and install Vault:

\# Download latest version of Vault

wget
https://releases.hashicorp.com/vault/1.18.3/vault_1.18.3_linux_amd64.zip

\# Unzip the package

sudo unzip vault_1.18.3_linux_amd64.zip -d /usr/local/bin/

\# Set ownership

sudo chown vault:vault /usr/local/bin/vault

\# Clean up

rm vault_1.18.3_linux_amd64.zip

2.  Verify the installation:

vault \--version

**Part 3: Configuring Vault**

1.  Create the configuration file:

sudo tee /etc/vault.d/vault.hcl \<\<EOF

storage \"file\" {

path = \"/opt/vault/data\"

}

listener \"tcp\" {

address = \"0.0.0.0:8200\"

tls_disable = 1 \# Only for dev/test

}

api_addr = \"http://127.0.0.1:8200\"

cluster_addr = \"http://127.0.0.1:8201\"

ui = true

disable_mlock = true \# Only for dev/test

EOF

2.  Set proper permissions:

sudo chmod 640 /etc/vault.d/vault.hcl

sudo chown -R vault:vault /etc/vault.d/vault.hcl

**Part 4: Starting Vault**

1.  Start Vault server in the background:

\# Switch to vault user

sudo -u vault /usr/local/bin/vault server -config=/etc/vault.d/vault.hcl
&

\# Press \<Enter\> to get the command prompt back

2.  Set environment variable:

export VAULT_ADDR=\'http://127.0.0.1:8200\'

3.  Verify Vault is running:

\# Check if Vault is responding

curl http://127.0.0.1:8200/v1/sys/health \| jq

4.  Verify Vault is running and responding to commands:

vault status

# Troubleshooting

1.  **Server Won't Start**

    - Check if process is running: ps aux \| grep vault

    - Check ownership of directories

    - Verify configuration file syntax

2.  **Cannot Connect**

    - Verify VAULT_ADDR is set

    - Check if process is running

    - Ensure Vault is unsealed

    - Test with curl: curl http://127.0.0.1:8200/v1/sys/health

3.  **Permission Issues**

    - Check ownership: ls -l /usr/local/bin/vault

    - Verify directory permissions: ls -l /opt/vault/data

**📚 Additional Resources**

- [[Vault Documentation]{.underline}](https://www.vaultproject.io/docs)

- [[Production
  Hardening]{.underline}](https://www.vaultproject.io/docs/concepts/production-hardening)

- [[Binary
  Downloads]{.underline}](https://www.vaultproject.io/downloads)

  **❗ Important Notes**

1.  **Security Considerations**

    - This setup uses tls_disable = 1 - not for production

    - Uses disable_mlock = true - not for production

    - Store unseal keys securely in production

    - Enable audit logging in production