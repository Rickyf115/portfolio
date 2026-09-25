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

Principal Software Engineer at Optum, programming since 2012, leading multi-year roadmaps for enterprise-grade platform infrastructure: custom Kubernetes Operators in Go, Kafka-as-a-Service and Elasticsearch-as-a-Service control planes, and Terraform-driven GKE orchestration moving 20+ petabytes of data across 800+ clusters at five nines reliability. Partners with VP-level leaders and vendors (Warpstream, GCP), and builds production AI agents with responsible-use review gates.

## Skills

**Core:** Go, Python, Java, Kubernetes, Kubernetes Operators, Kubebuilder / Operator SDK, Terraform, GCP, GKE, AWS, Apache Kafka, Elasticsearch, Cassandra, Helm, CI/CD, distributed systems, SRE, infrastructure as code, technical roadmap planning

**Additional:** ArgoCD, Kargo, Docker, Prometheus, Thanos, Grafana, PagerDuty, GitHub Actions, canary and blue/green releases, bare-metal Kubernetes, Confluent Schema Registry, C, C#, AI agent development, responsible AI practices, Claude Code, mentorship and technical teaching

## Experience

### Principal Software Engineer, TLCP

Optum, UnitedHealth Group | Minneapolis, MN | Jan 2020 - Present

Progressed Technology Development Program Associate (Jan 2020) > Software Engineer (Jan 2021) > Senior Software Engineer (Mar 2022) > Lead Software Engineer (Feb 2023) > Principal Software Engineer, TLCP (Feb 2024 - Present). Empower hundreds of teams across the enterprise to build data-driven services, moving tens of petabytes of data with minimal architectural overhead, using Kubernetes Operators and CI/CD to automate deployment, management, and hosting of enterprise-grade distributed systems across on-premise and multi-cloud environments.

- **Platform and team leadership:** Lead **15 engineers** across the Kafka-as-a-Service and Elasticsearch-as-a-Service platforms and advise **2 engineering leaders**, sustaining **five nines reliability** with **zero customer data loss** in production.
- **Multi-year Kafka roadmap:** Led the **2-year** roadmap that took Kafka provisioning from CI/CD pipelines to self-service in the enterprise marketplace, backed by a custom Terraform Provider; resource deployments rose **52%** and usage has grown nearly **3x**.
- **Executive influence:** Wrote a Kubernetes security report for a VP that set the organization's GKE security standard (IAM, Workload Identity, least-privilege RBAC) and secured funding to move off bare metal; partnered with a VP to design an org-wide SRE model adopted by **4 engineering teams**.
- **Automated deployment pipelines:** Lead the automated deployment initiative across **30 GKE clusters** with ArgoCD, Kargo, promotion pipelines, and canary and blue/green releases, cutting pull requests per change from **30+ to 2**.
- **Control plane architecture:** Design and manage the platform's Kubernetes control plane across **800+ clusters** and **~2,000 GCP instances**, with the largest GKE cluster exceeding **1,000 nodes** and **20+ petabytes of data movement**.
- **Cloud cost and GCP partnership:** Delivered **$2.5M in annual savings** by eliminating excessive log retention in GCP; manage the GCP partnership for CUD allocation, reservations, and right-sizing.
- **Agentic development:** Build agentic workspaces and agent skills used by **30+ engineers**, shipping **~50 fully agent-developed features** to production and cutting support response time from several days to about **1 hour**; building AI support agents projected to save **4,160 engineering hours a year**.

**Featured Project: Warpstream Cluster Provisioning Platform (Q4 2025 - Present)**

- Architected the end-to-end design for Warpstream-based Kafka cluster provisioning and delivered a net-new Warpstream operator (Go) plus its Terraform cloud infrastructure; lead the Warpstream vendor partnership and the roadmap for it as a net-new product.
- Projected to cut beta customers' annual Kafka spend by approximately **80%**; migrated workloads already save roughly **$2.9M per year**.

Technologies: Go, Kubebuilder, Kubernetes Operators, Helm, Terraform, GCP, GKE, ArgoCD, Kargo, GitHub Actions, Python, Kafka, Warpstream, Elasticsearch, Prometheus, Thanos, Docker

### TDP Software Development Intern

Optum | Minneapolis, MN | Jun - Aug, 2017 - 2019

- Returned for three consecutive summer internships, contributing business-critical features to a monolithic application with automated unit and integration testing.

Technologies: Java, Spring Boot, Groovy Spock

## Projects

### HostPort Allocator (open source contribution)

Contributed to HostPort Allocator, an open source Kubernetes host port allocator.

Technologies: Kubernetes

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

Site-Only: true

Evolutionary algorithm that solves a fully simulated Rubik's Cube model, exploring genetic computation applied to combinatorial optimization.

Technologies: Python, genetic algorithms, matrix math
Link: https://github.com/Rickyf115/rubiksCubeGeneticAlgo

### SafetyNet

Site-Only: true

iOS peer-to-peer messaging app requiring no Wi-Fi or cellular data. Uses device-to-device networking with end-to-end encryption for resilient off-grid communication.

Technologies: Swift, iOS, P2P networking, E2E encryption
Link: https://github.com/gould-ann/SafetyNet-legacy

### Ray Tracing Engine

Site-Only: true

Browser-based ray tracer in vanilla JavaScript. Renders spheres and triangles with Blinn-Phong lighting, reflections, and a free-moving camera, no GPU required.

Technologies: JavaScript, graphics pipeline, 3D rendering, Blinn-Phong
Link: https://github.com/svew/javascript-raytracing

### Sheet Vision (Senior Design)

Site-Only: true

Application that reads sheet music, plays it back, and listens to the user in real time, providing feedback to help learners draw parallels between notation and sound.

Technologies: ElectronJS, ReactJS, AWS Lambda, AWS S3, OpenCV, Python, computer vision
Link: ./Misc/project_plan.pdf

### Run Samurai, Run!

Site-Only: true

Top-down 2D infinite side-scrolling runner for mobile. Players fight through enemy mobs for upgrades and high scores, with single-player and head-to-head multiplayer modes.

Technologies: P5.js, HTML/CSS, PHP, AJAX, game loop development

## Education

Bachelor of Science in Computer Engineering, Minor in Cybersecurity, Iowa State University, 2015 - 2019

## Certifications

Google Cloud Certified - Cloud Digital Leader, Google, 2025

AI Dojo - Safe AI Agent Development and Usage, Optum (internal accreditation), 2025
