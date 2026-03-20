Businesses really can’t afford for their systems to go down. A regional outage, or even a simple infrastructure issue can take an application offline and cause real problems; lost revenue, frustrated customers, and a lot of scrambling behind the scenes. That’s why having a solid disaster recovery plan matters so much. When you build your applications to run across multiple AWS Regions, with automatic failover and replicated data, you’re making sure your services stay available even if an entire Region has an issue. It’s one of the most reliable ways to keep your applications resilient and your users supported no matter what happens.

Cross Region Disaster Recovery 

Note: Lab instructions are located in the "docs" folder under the main folder called "aws-crossregion-disaster-recovery"

In this project I built an identical architecture across two different regions, us-east-1 and us-west-1. Then placed an auto scaling, load balanced architecture within the default VPC and connect it to an Amazon RDS MySQL database in the primary Region (us-east-1).   
 
The RDS MySQL database will have a Read Replica in the Secondary Region (us-west-1), and I stored the database credentials as a secret in AWS Secrets Manager. Failover routing with Amazon Route 53 will be used to automatically fail over from the primary Region to the secondary Region when I simulate the failure of the primary Region. 

