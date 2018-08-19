terraform {
  backend "gcs" {
    bucket      = "image-store-scratch-jbk-2"
    prefix      = "terraform/state"
    credentials = "account.json"
  }
}

variable "network_name" {
  default = "marion-default"
}

variable "subnet_name" {
  default = "marion-us-west1"
}

variable "target_pool" {
  default = "marion-targetpool"
}

variable "autohealing" {
  default = "autohealing"
}

provider "google" {
  credentials = "${file("account.json")}"
  project     = "extreme-unison-201615"
  region      = "us-west1"
}
