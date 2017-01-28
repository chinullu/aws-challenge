# aws-challenge
write a quick script to enumerate all ports an arbitrary EC2 instance has open via its security groups rules. Consider only “ingress” rules, and remember to include all possible sources of traffic (other security groups or CIDRs). 

I was unable to complete the code exactly as specified in the doc but most of the use case works and instead of printing the output in table. I'm printing it as dictionary page.

Before Executing this Python File

-Set these environment variables for your AWS access credentials:
 
    - export AWS_ACCESS_KEY_ID=your_access_key_id
    - export AWS_SECRET_ACCESS_KEY=your_secret_access_key

-Now, Excute the file as follow
    - ./sg.py i-361c43bf us-east-1 (./filename.py <Instance_ID><Region_Name>

-The output File is uploaded and available along python file.

I have masked the public IP's from the output for security reasons. Few web services were hosted at that locations.
