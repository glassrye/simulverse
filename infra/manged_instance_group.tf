resource "google_compute_region_instance_group_manager" "marion" {
  name = "marion-rigm"

  base_instance_name        = "marion-app"
  instance_template         = "${google_compute_instance_template.marion-template.self_link}"
  region                    = "us-west1"
  distribution_policy_zones = ["us-west1-a", "us-west1-b", "us-west1-c"]

  target_pools = ["${google_compute_target_pool.marion-targetpool.self_link}"]
  target_size  = 3

  named_port {
    name = "http"
    port = 80
  }

  auto_healing_policies {
    health_check      = "${google_compute_health_check.autohealing.self_link}"
    initial_delay_sec = 300
  }
}
