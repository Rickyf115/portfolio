# Ricky Faure

Minneapolis, MN | 952-256-5622 | rickyf115@pm.me | linkedin.com/in/ricardo-faure-805175128 | github.com/Rickyf115

---

## Summary

Principal Software Engineer at Optum, the technology arm of UnitedHealth Group, building enterprise-grade platform infrastructure since 2019. Deep backend and distributed systems owner: custom Kubernetes Operators in Go, Kafka-as-a-Service and Elasticsearch-as-a-Service control planes, GKE environment orchestration, and Terraform-driven infrastructure as code across on-premise and multi-cloud environments. Leads architecture design and platform management for systems that move 20+ petabytes of data and serve hundreds of enterprise teams, with hands-on SRE ownership of production streaming infrastructure spanning 800+ clusters and thousands of nodes at five nines reliability with zero data loss.

## Skills

**Core:** Go, Kubernetes, Kubernetes Operators, Kubebuilder / Operator SDK, Kubernetes CRDs, Terraform, custom Terraform Provider development, GCP, GKE, Apache Kafka, Elasticsearch, Helm, CI/CD, GitHub Actions, Python, distributed systems, SRE, infrastructure as code, architecture design

**Additional:** Docker, Prometheus, GitOps, bare-metal Kubernetes, GCP IAM, GCS, VPC, Artifact Registry (GAR), GCP VolumeSnapshots, certificate management, Jenkins, Java, Spring Boot, Groovy Spock, Kibana, Rally API automation, vulnerability management, mentorship and technical teaching, AI-assisted development, Claude Code, GitHub Copilot, OpenAI Codex

## Experience

### Principal Software Engineer, TLCP

Optum, UnitedHealth Group | Minneapolis, MN | Jan 2020 - Present

Progressed Technology Development Program Associate (Jan 2020) > Software Engineer (Jan 2021) > Senior Software Engineer (Mar 2022) > Lead Software Engineer (Feb 2023) > Principal Software Engineer, TLCP (Feb 2024 - Present). Empower hundreds of teams across the enterprise to build data-driven services, moving tens of petabytes of data with minimal architectural overhead, using Kubernetes Operators and CI/CD to automate deployment, management, and hosting of enterprise-grade distributed systems across on-premise and multi-cloud environments.

- **Platform and team leadership:** Lead a team of **7 engineers** building Kafka-as-a-Service and Elasticsearch-as-a-Service platforms, achieving **five nines reliability** via Kubernetes Operators and robust infrastructure-as-code practices.
- **Kubernetes Operator development:** Build and maintain custom Kubernetes Operators (Go, Kubebuilder) for Kafka, Elasticsearch, Prometheus, Service Monitors, GCP VolumeSnapshots, certificate management, and bare-metal Kubernetes upgrade orchestration.
- **Control plane architecture:** Design and manage the architecture of the platform's Kubernetes resource management control plane, in which operators generate and own concrete Kubernetes resources for automated deployment and configuration of streaming infrastructure at production scale, managing **800+ clusters** across **thousands of nodes** in multi-tenant on-premise and GCP environments.
- **Self-service marketplace migration:** Achieved a **52% increase in resource deployments** by migrating from GitOps to a GUI-based management system within an enterprise marketplace, backed by a custom Terraform Provider and Kubernetes resource manager.
- **Cloud cost optimization:** Delivered **$2.5M in annual cost savings** through cloud resource optimization, instance type migrations, and elimination of excessive log retention in GCP.
- **Cloud scale and GKE orchestration:** Expanded the platform to handle **20+ petabytes of data movement** across on-premise and GCP (GKE, GAR, IAM, GCS, VPC) by extending Kubernetes Operators for cloud environments; own provisioning and orchestration of the platform's GKE environments through Terraform and infrastructure as code.
- **SRE and production operations:** Serve in on-call rotation across a fleet of **800+ clusters** and **thousands of nodes**, delivering **five nines reliability** with **zero customer data loss** in production across the platform's history; respond to incidents, tune performance and utilization against SLAs, and stabilize high-throughput Kafka and Elasticsearch services.
- **Security automation:** Designed a vulnerability scanning workstream using reusable GitHub Actions, a custom Python Rally API library, and automated report generation, adopted org-wide.
- **Mentorship and teaching:** Mentor junior engineers in rotational programs; teach quarterly internal courses on Kubernetes Operators and Elasticsearch/Kibana.

**Featured Project: Warpstream Cluster Provisioning Platform (Q4 2025 - Q1 2026)**

- Architected the end-to-end design for Warpstream-based Kafka cluster provisioning: the networking design, the operator, agent, and resource specifications, and the resource flows from the customer-facing resource manager down to the backend infrastructure.
- Extended the platform's Kubernetes operators for net-new resource kinds and delivered a net-new Warpstream operator (Go) that generates all required Kubernetes resources and connects them into Cloud Storage buckets, Warpstream API registrations, and agent configs.
- Co-designed the Terraform cloud infrastructure for the Warpstream Clusters-as-a-Service deployment, including GCP Cloud Storage provisioning, VPC configuration, DNS, and IAM.
- Shipped to two of Optum's largest Apache Kafka on GCP customers as beta; Warpstream's diskless, Cloud Storage-based architecture eliminates local disk I/O from the stream processing data path, projected to reduce their annual Kafka infrastructure spend by approximately **80%**.

Technologies: Go, Kubebuilder, Kubernetes Operators, Helm, Terraform, GCP, GKE, GitHub Actions, Python, Kafka, Warpstream, Elasticsearch, Prometheus, Jenkins, Docker

### TDP Software Development Intern

Optum | Minneapolis, MN | Summer 2019 <!-- VERIFY: exact internship months; LinkedIn screenshot was cut off before this entry. -->

- Contributed business-critical features to a monolithic application, complete with feature implementations and automated unit and integration testing.

Technologies: Java, Spring Boot, Groovy Spock

## Projects

### OSS Feed

Self-hosted weekly RSS digest that tracks releases from curated open source projects. A watchlist YAML feeds GitHub Actions to fetch releases, generate an XML feed, and publish via GitHub Pages, with Slack/Discord webhook notifications and state management to avoid duplicate alerts.

Technologies: JavaScript, GitHub Actions, RSS/Atom, GitHub Pages, YAML
Link: https://github.com/Rickyf115/oss-feed

### Rubik's Cube Genetic Algorithm Solver

Evolutionary algorithm that solves a fully simulated Rubik's Cube model, exploring genetic computation applied to combinatorial optimization.

Technologies: Python, genetic algorithms, matrix math
Link: https://github.com/Rickyf115/rubiksCubeGeneticAlgo

### SafetyNet

iOS peer-to-peer messaging app requiring no Wi-Fi or cellular data. Uses device-to-device networking with end-to-end encryption for resilient off-grid communication.

Technologies: Swift, iOS, P2P networking, E2E encryption
Link: https://github.com/gould-ann/SafetyNet-legacy

### Ray Tracing Engine

Browser-based ray tracer in vanilla JavaScript. Renders spheres and triangles with Blinn-Phong lighting, reflections, and a free-moving camera, no GPU required.

Technologies: JavaScript, graphics pipeline, 3D rendering, Blinn-Phong
Link: https://github.com/svew/javascript-raytracing

### Sheet Vision (Senior Design)

Application that reads sheet music, plays it back, and listens to the user in real time, providing feedback to help learners draw parallels between notation and sound.

Technologies: ElectronJS, ReactJS, AWS, Python, computer vision
Link: ./Misc/project_plan.pdf

### Run Samurai, Run!

Top-down 2D infinite side-scrolling runner for mobile. Players fight through enemy mobs for upgrades and high scores, with single-player and head-to-head multiplayer modes.

Technologies: P5.js, HTML/CSS, PHP, AJAX, game loop development

## Education

Bachelor of Science in Computer Engineering, Minor in Cybersecurity, Iowa State University, 2015 - 2019

## Certifications

Google Cloud Certified - Cloud Digital Leader, Google <!-- VERIFY: issue year (and expiration if you want it listed). -->
