CloudFront with Multiple Origins

This lab guide builds an Amazon CloudFront Distribution with multiple custom origins. The origins will be Amazon EC2 instances behind Application Load Balancers. The lab shows how to create a highly available solution across multiple Regions and uses CloudFront origin groups with failover configured.

To test the solution, you will simulate a network failure and trigger a cross-Region failover from one of the load balancers to the other one. The diagram below depicts the solution architecture:

![Architecture Diagram][cloudfront-with-multiple-origins.png]

Requirements (Prerequisites)

- ***AWS Free Tier Account***

- ***Basic Exposure to the AWS Console and completion of prior days learning.***

** Resources

See “cloudfront-lab-files” in GitHub repo

Exercise Overview

**Exercise 1 -** Create the S3 Bucket to host the website code

**Exercise 2 -** Create the US and UK Website EC2 instances

**Exercise 3 -** Create the Application Load Balancers

**Exercise 4** – Create the CloudFront Distribution

**Exercise 5** – Test the solution by simulating a network failure

**Exercise 6** – Clean up your resources

Exercise 1 - Create the S3 Bucket

Task 1 – Create the S3 Bucket to host the website code.

Create the S3 bucket and populate it with the HTML / CSS code.

1.  Head over to the Amazon S3 Console and click ‘Create Bucket’.

2.  First, we will create the S3 Bucket. Call it ‘s3-website-123456’, with the numbers appended being a random string of numbers.

3.  Select ‘Create Bucket’.

4.  Once you have created the bucket, click on it. Next, upload the website code. On the downloaded files open the folder called ‘cloudfront-lab-files. Within this folder, you will find two files:

> -website.css
>
> -index.html

5.  Click upload and simply drag and drop these two files into the folder (not the user data file), and again click upload. You should then see a success banner across the top bar of your AWS console.

> You should now have an S3 bucket populated with website code that the EC2 instances can download.

Exercise 2 - Create the US Website and UK Website EC2 instances

# Task 1 – Create the US Website instances 

We will now create the US Website EC2 instances. Remember to create this in the us-east-1 Region.

1.  First, we'll create the first US Website instance in us-east-1.

2.  Head over to the EC2 console and click Launch instance.

3.  Call it ‘US-Website-1’.

4.  Scroll down and choose ‘proceed without a key pair’ leaving the other default options.

5.  Create a security group called gives full access via port 80. Call it ‘US-Website-SG’.

6.  Choose a public subnet in the us-east-1a availability zone.

7.  We need to create an instance profile to allow EC2 to communicate with S3.

8.  Click ‘Create new IAM profile’ under advanced details and it will take us to the IAM console.

9.  Click Create Role and under common use cases select EC2 and click next.

10. Search for the AmazonS3ReadOnlyPolicy and attach it, click next:

11. Call the role ‘CloudFrontEC2S3Role’ and click create role.

12. Head back to the EC2 launch page and add the EC2 Role.

13. Next, also under advanced details paste in the user data from the resources titled ‘websiteuser data’.

14. Note that you will need to replace the ‘YOUR-BUCKET-HERE’ text with your actual bucket name to allow the user data to run properly.

15. Navigate back to the console after making the changes, paste in the user data and launch the instance.

16. We now need to follow the exact same steps to launch the second US Website instance. We will keep all the same settings as the first instance except changing the name to US-Website2), the availability zone should be ‘us-east-1b’.

17. Test that the EC2 instances have launched properly by launching the public IP of each instance.

# Task 2 – Create the UK Website EC2 instances 

> We will now create the UK Website EC2 instances. Remember to create this in the eu-west-1 Region.

1.  Following the same steps, we should launch the UK Website instances (UK-Website-1 and UK-Website-2). They should be using the same user data and should be launched in eu-west1a and eu-west-1b respectively.

2.  Create a second Security group with the exact same rules as the first Security Group but call it UK-Website-SG.

3.  Once you have launched these you can test access to the instance via the public IP for each instance.

> This shows which availability zone the instances are in and will show us that the load balancer is working and that CloudFront has failed over to the second Region once we simulate the failure.

Exercise 3 - Create the Application Load Balancers

# Task 1 – Create the US Website ALB 

> We will now create the first Application Load Balancer for the US instances. Remember to create this in the us-east-1 Region.

1.  Head over to the EC2 console in the us-east-1 Region and click Target Group.

2.  Choose instances as the target type and call the Target Group ‘USWebsiteTargetGroup’ and click next.

3.  Tick both US Website instances and click ‘include as pending below’.

4.  Click ‘Create Target Group’.

5.  We will now create the Load Balancer by clicking on Load Balancers, ‘Create Load Balancer’ and choose the application load balancer.

6.  Call it ‘USWebsiteLoadBalancer’.

7.  Select the two Availability Zones that we have selected earlier to launch the US Website instances in‘us-east-1a and us-east-1b’).

8.  Remove the default Security Group and select the US-Website-SG security group.

9.  Select the ‘USWebsiteTargetGroup’ for the listener on port 80.

10. Click create load balancer.

11. You should now be able to click on the DNS name of the load balancer and be routed across different targets, seeing it cycle between us-east-1a and us-east-1b.

# Task 2 – Create the UK Website ALB 

> We will now create the second Application Load Balancer for the UK based instances. Remember to create this in the eu-west-1 Region.

1.  We can now follow the exact same steps for the second application load balancer, except creating a target group called UKWebsiteTargetGroup and an ALB called

> UKWebsiteLoadBalancer. The ALB should balance the load across eu-west-1a and eu-west1b. Select the UK-Website-SG security group.

2.  Again, you should now be able to click on the DNS name of the load balancer and be routed across different targets, seeing it cycle between eu-west-1a and eu-west-1b.

Exercise 4 - Create the CloudFront Distribution

# Task 1 – Create the CloudFront Distribution 

We will now create the CloudFront Distribution.

1.  Head over to the Amazon CloudFront console and click ‘Create a CloudFront Distribution.

2.  Under ‘Origin domain’ choose the US-Website-LoadBalancer to associate with the CloudFront distribution.

3.  Under ‘cache and key origin requests’ enable ‘caching disabled’.

4.  Click ‘Create distribution’.

5.  You may need to select an option for WAF, choose “Do not enable security protections”.

# Task 2 – Create the origin and origin group 

We will now add the extra origin and create the origin group so we can failover between the two origins.

1.  Click on your distribution and click on the origins.

2.  Click ‘Create origin’ and add the second origin (UK ALB).

> ***Note:** Make sure both origins are configured for HTTP (not HTTPS)*

3.  Next, click ‘Create origin group.’

4.  Select both origins and use the up arrow to ensure that the US Website origin is at the top.

5.  Call it ‘lab-origin-group’ and select ‘**504 Gateway timeout’**.

6.  Click ‘Create origin group.’

7.  Once we have created the origin group, go to the CloudFront distribution again and under Behaviors, edit the default behavior to change the origin to route to the **origin group**.

8.  Click ‘Save changes’.

9.  Once changes are deployed try to access the CloudFront distribution using the domain name, e.g. ‘d4hbbln9lriji.cloudfront.net’.

10. You should see the website delivered from the us-east-1 Region.

Exercise 5 – Test the Solution

# Task 1 – Test the solution 

We will now test to see if the CloudFront distribution is working as intended.

1.  Head back to the EC2 console in the us-east-1 region.

2.  Go to the US-Website-SG security group and remove the security group rule which provides HTTP access.

3.  The purpose of this is that it provides a simulated failure and would typically service up a 504 HTTP error. However, we changed the routing behavior in the CloudFront distribution to trigger a cross-region failover if a 504 error occurs.

4.  You should see a quick failover to the other origin! – and see the UK based instances now serving the website.

Exercise 6 – Clean up the resources

# Task 1 – Delete the resources 

We will first delete the CloudFront distribution and any other billable resources.

1.  First, select the distribution and select ‘disable’.

2.  Once it is disabled, select it again, and click ‘delete’.

3.  Delete your load balancers, and your target groups, as well as your instances and your S3 buckets.


[def]: diagrams/cloudfront-multi-origin.png