# Back-End Demo

This demo creates a simulated back-end service.

The service listens on port 8080 and returns a static response to the /hello path. example http://(IP Address):8080/hello

## Features included in the demo

Builds a python application and deploys it as a container to GKE.  There are two environments - Dev and Prod.  Prod has clusters on both the east and west coasts.

### Cloud Build
Steps
- Build
- Push to AR
- Create a release for Cloud Deploy
Waitfor

### Artifact Registry
- Local Python Repository
- Remote Python Repository
- Virtual Python Repository
- Vulnerability analysis

### Cloud Deploy
- Approvals
- single-target deployment
- mulit-target deployment
- Canary Deployment Pattern to multi-target
- Automation
- Promotion
- Deploy parameters
- pre-deploy hook sample on Dev
- Verification on Dev


Demo text