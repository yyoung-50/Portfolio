# Vault Glossary

A reference list of common Vault terms, concepts, and components.

---

## A

### Accessor
A unique identifier for a token that can be used to look it up or revoke it without knowing the token value.

### ACL (Access Control List)
Defines what actions a token or identity can perform. Implemented through Vault policies.

---

## C

### Capability
Permissions assigned in a policy (e.g., create, read, update, delete, list, sudo).

### Certificate Authority (CA)
PKI component that signs certificates. Vault can act as a root or intermediate CA.

---

## E

### Entity
A Vault identity object that represents a user or machine across multiple auth methods.

### Entity Alias
A mapping between an auth method identity (e.g., GitHub username) and a Vault entity.

---

## K

### KV (Key-Value) Secrets Engine
Stores static secrets. KV v2 supports versioning, undelete, and metadata.

---

## L

### Lease
A time-bound credential issued by Vault. Must be renewed or will expire.

### Logical Volume (LV)
Not Vault-specific, but often referenced in storage discussions.

---

## M

### Mount
A path where a secrets engine or auth method is enabled (e.g., `auth/aws/`, `pki_int/`).

---

## P

### Policy
Rules that define what a token or identity can access.

### PKI (Public Key Infrastructure)
Vault engine used for issuing, revoking, and managing TLS certificates.

---

## R

### Raft Storage
Integrated storage backend used for HA clusters. Supports snapshots and replication.

### Revocation
Process of invalidating a token, lease, or certificate.

---

## S

### Seal / Unseal
Vault starts sealed; unseal keys are required to decrypt the master key.

### Secrets Engine
A plugin that stores or generates secrets (KV, PKI, Transit, AWS, etc.).

### Snapshot
A point-in-time backup of Raft storage.

---

## T

### Token
Primary authentication mechanism in Vault. Can be renewable or orphan.

### Transit Engine
Provides encryption-as-a-service without storing data.

---

## U

### Undelete
KV v2 feature allowing recovery of deleted secret versions.

---

## W

### Wrap / Response Wrapping
A secure way to deliver sensitive data using short-lived tokens.

