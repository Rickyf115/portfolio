# Ricky Faure

Minneapolis, MN | 952-256-5622 | rickyf115@pm.me | linkedin.com/in/ricardo-faure-805175128 | github.com/Rickyf115

<!-- Generic (non-tailored) resume curated from docs/masters/ats.md. This file
feeds the ATS SYNC regions of index.html (via scripts/sync_index_from_ats.py)
and therefore Misc/resume.pdf. It follows the tailoring rules: a pruned,
readable cut of the master. Unlike prospectives/submitted copies it keeps bold
lead-in labels and metrics, because the site renders them as highlights.
When ats.md changes materially, re-curate this file to match. -->

---

## Summary

Principal Software Engineer at Optum building enterprise-grade platform infrastructure: custom Kubernetes Operators in Go, Kafka-as-a-Service and Elasticsearch-as-a-Service control planes, and Terraform-driven GKE orchestration moving 20+ petabytes of data across 800+ clusters at five nines reliability.

## Skills

**Core:** Go, Kubernetes, Kubernetes Operators, Kubebuilder / Operator SDK, Terraform, GCP, GKE, Apache Kafka, Elasticsearch, Helm, CI/CD, Python, distributed systems, SRE, infrastructure as code

**Additional:** Docker, Prometheus, Grafana, GitOps, GitHub Actions, bare-metal Kubernetes, certificate management, Java, Spring Boot, AI-assisted development, Claude Code, mentorship and technical teaching

## Experience

### Principal Software Engineer, TLCP

Optum, UnitedHealth Group | Minneapolis, MN | Jan 2020 - Present

Progressed Technology Development Program Associate (Jan 2020) > Software Engineer (Jan 2021) > Senior Software Engineer (Mar 2022) > Lead Software Engineer (Feb 2023) > Principal Software Engineer, TLCP (Feb 2024 - Present). Empower hundreds of teams across the enterprise to build data-driven services, moving tens of petabytes of data with minimal architectural overhead, using Kubernetes Operators and CI/CD to automate deployment, management, and hosting of enterprise-grade distributed systems across on-premise and multi-cloud environments.

- **Platform and team leadership:** Lead **15 engineers** across the Kafka-as-a-Service and Elasticsearch-as-a-Service platforms and advise **2 engineering leaders**, sustaining **five nines reliability** through Kubernetes Operators and disciplined infrastructure-as-code practices.
- **Kubernetes Operator development:** Build and maintain custom Kubernetes Operators (Go, Kubebuilder) for Kafka, Elasticsearch, Prometheus, Service Monitors, GCP VolumeSnapshots, certificate management, and bare-metal Kubernetes upgrade orchestration.
- **Control plane architecture:** Design and manage the platform's Kubernetes resource management control plane, managing **800+ clusters** across **thousands of nodes** in multi-tenant on-premise and GCP environments with **zero customer data loss** in production.
- **Self-service marketplace migration:** Achieved a **52% increase in resource deployments** by migrating from GitOps to a GUI-based management system within an enterprise marketplace, backed by a custom Terraform Provider and Kubernetes resource manager.
- **Cloud cost optimization:** Delivered **$2.5M in annual cost savings** through cloud resource optimization, instance type migrations, and elimination of excessive log retention in GCP.
- **Cloud scale and GKE orchestration:** Expanded the platform to handle **20+ petabytes of data movement** across on-premise and GCP by extending Kubernetes Operators for cloud environments; own provisioning and orchestration of the **30+ GKE clusters** backing these platforms through Terraform.
- **Agentic development workspaces:** Design and build agent-driven development workspaces that standardize the team's engineering workflow into a consistent, deterministic process, with reusable agent skills that automate remediation and SRE support tasks.

**Featured Project: Warpstream Cluster Provisioning Platform (Q4 2025 - Q1 2026)**

- Architected the end-to-end design for Warpstream-based Kafka cluster provisioning, from the customer-facing resource manager down to the backend infrastructure, and delivered a net-new Warpstream operator (Go) plus the Terraform cloud infrastructure behind it.
- Shipped to two of Optum's largest Apache Kafka on GCP customers as beta; Warpstream's diskless architecture is projected to reduce their annual Kafka infrastructure spend by approximately **80%**.

Technologies: Go, Kubebuilder, Kubernetes Operators, Helm, Terraform, GCP, GKE, GitHub Actions, Python, Kafka, Warpstream, Elasticsearch, Prometheus, Docker

### TDP Software Development Intern

Optum | Minneapolis, MN | Jun - Aug, 2017 - 2019

- Returned for three consecutive summer internships, contributing business-critical features to a monolithic application with automated unit and integration testing.

Technologies: Java, Spring Boot, Groovy Spock

## Projects

### Yo-Yo Mount Visualizer (active development)

3D trick engine that models yo-yo string mounts as graph topologies and aims to discover new tricks through pathfinding. Encodes mounts as schema-validated string traversals with canonical hashing, rendered in an interactive 3D visualizer with a Verlet rope physics simulation.

Technologies: TypeScript, React, react-three-fiber, graph modeling, pathfinding, physics simulation
Link: https://github.com/Rickyf115/yoyo-mount-visualizer

### Spin Ledger (closed source)

Single pane of glass for buy/sell/trade activity across skill toy community forums. Ingests unstructured, schemaless forum listings, normalizes them into a taxonomy-aware data model via deterministic rule-based entity extraction, and serves them through an indexed, searchable marketplace dashboard.

Technologies: Python, FastAPI, SQLAlchemy 2.0, Alembic, rule-based entity extraction, data normalization

### Self-Hosted Home Lab

Multi-machine home lab orchestrating containerized services with Docker, fronted by Caddy as a reverse proxy with automatic HTTPS; every service is served exclusively over TLS. Hosts a media server, network-attached storage, network-wide DNS-sinkhole ad blocking, secrets vaults, and closed-source project deployments, with private encrypted tunnels for secure remote access.

Technologies: Docker, Caddy, reverse proxy, TLS, DNS, VPN tunneling, NAS, Linux

### OSS Feed

Self-hosted weekly RSS digest that tracks releases from curated open source projects. A watchlist YAML feeds GitHub Actions to fetch releases, generate an XML feed, and publish via GitHub Pages, with Slack/Discord webhook notifications.

Technologies: JavaScript, GitHub Actions, RSS/Atom, GitHub Pages
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

Google Cloud Certified - Cloud Digital Leader, Google, 2025
