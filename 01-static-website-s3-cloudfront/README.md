# Project 1: Static Website Hosting with S3 & CloudFront

## Architecture
User Browser ---> Amazon CloudFront (CDN) ---> Amazon S3 (Origin Bucket)

## Tech Stack & Services
* **Amazon S3:** Object storage for static web assets.
* **Amazon CloudFront:** Global Content Delivery Network (CDN) for fast loading & HTTPS security.
* **Origin Access Control (OAC):** Restricted S3 bucket access so traffic only flows through CloudFront.

## Key Learnings
1. Setting up static website origins in AWS.
2. Configuring CloudFront distributions for global low-latency delivery.
3. Securing storage buckets using custom JSON bucket policies and OAC.
4. Diagnosing and resolving `403 AccessDenied` errors.

## Live Site
* Domain: https://d3jmhoyiig9pur.cloudfront.net
