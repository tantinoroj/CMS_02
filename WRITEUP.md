# Write-up Template

For the Article CMS application, I analyzed both VM and App Service solutions considering the following aspects:
Resource	Cost	Scalability	Availability	Workflow
Virtual Machine	- Higher initial cost
- Pay for compute time even when idle
- Full control over instance type and resources	- Manual scaling configuration required
- Can scale vertically with instance size changes
- Requires additional setup for horizontal scaling	- Requires manual configuration for high availability
- Need to manage OS updates and maintenance
- More control over maintenance windows	- More complex initial setup
- Full control over deployment process
- Requires more DevOps knowledge
- Manual configuration of dependencies
App Service	- Lower initial cost
- Pay only for actual usage
- Free tier available for development
- Predictable pricing based on service plan	- Built-in auto-scaling capabilities
- Easy vertical and horizontal scaling
- No infrastructure management needed	- Built-in load balancing
- High availability included
- Automatic OS and platform updates	- Simple deployment process
- Built-in CI/CD with GitHub Actions
- Easy configuration through portal
- Managed SSL certificates


#### Solution selected
Azure App Service:
I chose Azure App Service for deploying the Article CMS application for the following reasons:
Cost Efficiency:
  The application has moderate resource requirements
  App Service's consumption-based pricing is more cost-effective for our usage
  No need to pay for unused compute resources
Development Workflow:
  Direct integration with GitHub for continuous deployment
  Built-in support for Python applications
  Easy configuration of environment variables
  Simple SSL certificate management
Maintenance:
  Automated platform and OS updates
  Built-in monitoring and logging
  No need for infrastructure management
  Automatic backup capabilities
Scalability:
  Easy scaling through the Azure portal
  Automatic scaling based on demand
  No need to manage VM instances manually

#####
App changes that would change your decision
Scale and Performance:
  Extremely high concurrent user load requiring fine-tuned server configuration
  Need for specific performance optimizations at the OS level

Cost Considerations:
  If the application scales to a point where VM costs become more economical
  Need for reserved instances or specific cost optimization strategies
  Requirements for specific regional deployments where App Service pricing is less favorable


