resource "google_compute_instance_template" "marion-template" {
  name        = "marion-app-template"
  description = "The template for the marion app servers in the target pool"

  tags = ["marion"]

  labels = {
    environment = "marion"
  }

  instance_description = "Marion app server"
  machine_type         = "n1-standard-1"
  can_ip_forward       = false

  scheduling {
    automatic_restart   = true
    on_host_maintenance = "MIGRATE"
  }

  disk {
    source_image = "debian-9-stretch-v20180501"
    auto_delete  = true
    boot         = true
  }

  network_interface {
    subnetwork    = "${google_compute_subnetwork.marion-us-west1.name}"
    access_config = {}
  }

  metadata {
    sshKey = "jkelty:${file("~/.ssh/gcp_key.pub")}"
  }

  metadata_startup_script = <<SCRIPT
    sudo apt-get update
    sudo apt-get install nginx -y
    SCRIPT
}
