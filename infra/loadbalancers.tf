resource "google_compute_region_backend_service" "marion-backend" {
  name             = "marion-backend"
  description      = "Backend Service for Marion"
  protocol         = "TCP"
  timeout_sec      = "10"
  session_affinity = "CLIENT_IP"

  backend {
    group = "${google_compute_region_instance_group_manager.marion.instance_group}"
  }

  health_checks = ["${google_compute_health_check.autohealing.self_link}"]
}

resource "google_compute_target_pool" "marion-targetpool" {
  name          = "marion-targetpool"
  health_checks = ["${google_compute_http_health_check.webservice.self_link}"]
}

resource "google_compute_forwarding_rule" "marion-internal" {
  name = "marion-internal"

  backend_service       = "${google_compute_region_backend_service.marion-backend.self_link}"
  load_balancing_scheme = "INTERNAL"
  subnetwork            = "${google_compute_subnetwork.marion-us-west1.self_link}"
  region                = "us-west1"
  ports                 = ["80"]
}
