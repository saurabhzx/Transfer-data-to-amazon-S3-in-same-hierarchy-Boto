Transfer-data-to-amazon-S3-in-same-hierarchy-Boto
=================================================

Transfer data in the same hierarchy from Shared Hosting to Amazon Web Services (AWS) S3 by using SDK for Python (Boto)

In this we will install SDK for Python(Boto) for S3 and transfer the data from your shared hosting to the amazon S3 bucket.Boto helps take the complexity out of coding by providing Python APIs for many AWS services including Amazon S3, Amazon EC2, Amazon DynamoDB, and more.

Step 1:- Install Boto by using pip in your server or local machine form where you want to transfer data

<             pip install boto

Step 2: Configure the Access Keys

You have to give your AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY provided by AWS to authenticate the Boto for using your account.

You will get these keys from security credentials of AWS account.

Export your access keys to environment variables and replace the ellipses (...) with your access keys:

export AWS_ACCESS_KEY_ID="..."

export AWS_SECRET_ACCESS_KEY="..."


You can also make boto config file it will automatically get security credentials from config file.

A boto config file is simply a .ini format configuration file that specifies values for options that control the behavior of the boto library. Upon startup, the boto library looks for configuration files in the following locations and in the following order:

/etc/boto.cfg - for site-wide settings that all users on this machine will use*
~/.boto - for user-specific settings*

The options are merged into a single, in-memory configuration that is available as boto.config.

An example ~/.boto file should look like:

aws_access_key_id = <your_access_key_here>
aws_secret_access_key = <your_secret_key_here>



If you don't want to save your security credentials on the server or your local machine than at each time you have to pass on these variables while making connection to Boto.

Step 3:- Run this python script transfer.py to transfer the data form your server to AWS S3

