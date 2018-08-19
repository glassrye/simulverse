resource "google_compute_network" "marion-default" {
  name                    = "marion-default"
  auto_create_subnetworks = "False"
  description             = "Marion Default Network for Subnetworks"
}

resource "google_compute_subnetwork" "marion-us-west1" {
  name          = "marion-us-west1"
  ip_cidr_range = "10.69.0.0/22"
  network       = "${google_compute_network.marion-default.self_link}"
  description   = "Default Admin Network"
}
