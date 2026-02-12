# Basic Authentication

# Command	                                    Description
vault auth -method=userpass username=myuser	    Login with username/password
vault auth -method=ldap username=myuser	        Login with LDAP
vault auth -method=github token=mytoken	        Login with GitHub
vault auth -method=aws	Login with AWS IAM
vault auth -method=kubernetes	              Login with Kubernetes