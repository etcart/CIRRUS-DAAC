# Onboarding new DAAC stacks to consolidated cumulus

## cross-account permissions

### Consolidated-stack-side IAM permissions to access S3 buckets
all buckets from legacy DAAC accounts that the consolidated stack will need to access should be added to the partner_bucket_names list at daac/variables/<maturity> in full, including prefix.