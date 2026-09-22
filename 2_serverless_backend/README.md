# Phase 2: Serverless Backend Integration

## Overview
In Phase 2, I added serverless dynamic data processing capabilities to my static portfolio website. Using **AWS Lambda** for compute and **Amazon API Gateway** for HTTP routing, the frontend now asynchronously fetches messages from the backend without needing traditional server infrastructure.

---

## Architecture & Data Flow

`User Browser` ➔ `API Gateway (HTTP GET)` ➔ `AWS Lambda (Python 3.12)` ➔ `JSON Response`

1. **Frontend**: HTML5/JS frontend executes an asynchronous `fetch()` API call upon button trigger.
2. **API Gateway**: Acts as the HTTP entry point (`/hello`), forwarding incoming web requests to Lambda.
3. **AWS Lambda**: Executes a Python function on-demand, returning a JSON payload with appropriate CORS response headers.

---

## AWS Configuration Details

* **AWS Lambda Function**: `my-portfolio-backend`
  * **Runtime**: Python 3.12
  * **CORS**: Configured headers (`Access-Control-Allow-Origin: *`) to enable web interactions.
* **Amazon API Gateway**: `my-portfolio-api`
  * **API Type**: HTTP API
  * **Route**: `GET /hello`
  * **Integration Target**: `my-portfolio-backend`
  * **Stage**: `$default` (Auto-deployed)

---

## Key Learnings
* **Serverless Compute**: Built an event-driven, cost-effective serverless architecture.
* **CORS Management**: Resolved cross-origin issues between static S3 frontend and API Gateway backend.
* **API Integration**: Linked HTTP REST routes directly to serverless execution handlers.