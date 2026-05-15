terraform {
  required_version = ">= 1.6.0"
  required_providers {
    databricks = {
      source  = "databricks/databricks"
      version = ">= 1.40.0"
    }
  }
}

provider "databricks" {}

resource "databricks_secret_scope" "mlops" {
  name = "mlops-project"
}
