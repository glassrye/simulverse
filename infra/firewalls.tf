resource "google_compute_firewall" "marion-firewall" {
  name    = "marion-default-firewall"
  network = "${google_compute_network.marion-default.name}"

  allow {
    protocol = "icmp"
  }

  allow {
    protocol = "tcp"
    ports    = ["80", "8080", "443", "22"]
  }

  allow {
    protocol = "udp"
    ports    = ["53"]
  }
}
