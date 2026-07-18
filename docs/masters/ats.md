# Ricky Faure

Minneapolis, MN | 952-256-5622 | rickyf115@pm.me | linkedin.com/in/ricardo-faure-805175128 | github.com/Rickyf115

---

## Summary

Principal Software Engineer at Optum, the technology arm of UnitedHealth Group, building enterprise-grade platform infrastructure since 2019. Deep backend and distributed systems owner: custom Kubernetes Operators in Go, Kafka-as-a-Service and Elasticsearch-as-a-Service control planes, GKE environment orchestration, and Terraform-driven infrastructure as code across on-premise and multi-cloud environments. Leads architecture design and platform management for systems that move 20+ petabytes of data and serve hundreds of enterprise teams, with hands-on SRE ownership of production streaming infrastructure spanning 800+ clusters and thousands of nodes at five nines reliability with zero data loss.

## Skills

**Core:** Go, Kubernetes, Kubernetes Operators, Kubebuilder / Operator SDK, Kubernetes CRDs, Terraform, custom Terraform Provider development, GCP, GKE, Apache Kafka, Elasticsearch, Helm, CI/CD, GitHub Actions, Python, distributed systems, SRE, infrastructure as code, architecture design

**Additional:** Docker, Prometheus, Grafana, GitOps, bare-metal Kubernetes, GCP IAM, GCS, VPC, Artifact Registry (GAR), GCP VolumeSnapshots, certificate management, Jenkins, Java, Spring Boot, Groovy Spock, Kibana, Rally API automation, vulnerability management, mentorship and technical teaching, AI-assisted development, agentic development workflows, Claude Code, GitHub Copilot, OpenAI Codex

## Experience

### Principal Software Engineer, TLCP

Optum, UnitedHealth Group | Minneapolis, MN | Jan 2020 - Present

Progressed Technology Development Program Associate (Jan 2020) > Software Engineer (Jan 2021) > Senior Software Engineer (Mar 2022) > Lead Software Engineer (Feb 2023) > Principal Software Engineer, TLCP (Feb 2024 - Present). Empower hundreds of teams across the enterprise to build data-driven services, moving tens of petabytes of data with minimal architectural overhead, using Kubernetes Operators and CI/CD to automate deployment, management, and hosting of enterprise-grade distributed systems across on-premise and multi-cloud environments.

- **Platform and team leadership:** Lead **15 engineers** across the Kafka-as-a-Service and Elasticsearch-as-a-Service platforms and advise **2 engineering leaders**, sustaining **five nines reliability** through Kubernetes Operators and disciplined infrastructure-as-code practices.
- **Kubernetes Operator development:** Build and maintain custom Kubernetes Operators (Go, Kubebuilder) for Kafka, Elasticsearch, Prometheus, Service Monitors, GCP VolumeSnapshots, certificate management, and bare-metal Kubernetes upgrade orchestration.
- **Control plane architecture:** Design and manage the architecture of the platform's Kubernetes resource management control plane, in which operators generate and own concrete Kubernetes resources for automated deployment and configuration of streaming infrastructure at production scale, managing **800+ clusters** across **thousands of nodes** in multi-tenant on-premise and GCP environments.
- **Self-service marketplace migration:** Achieved a **52% increase in resource deployments** by migrating from GitOps to a GUI-based management system within an enterprise marketplace, backed by a custom Terraform Provider and Kubernetes resource manager.
- **Cloud cost optimization:** Delivered **$2.5M in annual cost savings** through cloud resource optimization, instance type migrations, and elimination of excessive log retention in GCP.
- **Cloud scale and GKE orchestration:** Expanded the platform to handle **20+ petabytes of data movement** across on-premise and GCP (GKE, GAR, IAM, GCS, VPC) by extending Kubernetes Operators for cloud environments; own provisioning and orchestration of the **30+ GKE clusters** backing these platforms through Terraform and infrastructure as code.
- **SRE and production operations:** Serve in on-call rotation across a fleet of **800+ clusters** and **thousands of nodes**, delivering **five nines reliability** with **zero customer data loss** in production across the platform's history; respond to incidents, tune performance and utilization against SLAs, and stabilize high-throughput Kafka and Elasticsearch services.
- **Observability as code:** Converted Grafana dashboard maintenance to infrastructure as code, keeping dashboards versioned and reproducible so observability scales with the many data sources the platform has grown to.
- **Agentic development workspaces:** Design and build agent-driven development workspaces that standardize the team's engineering workflow into a consistent, deterministic process; encode the full breadth of the platform's distributed projects and their interdependencies into durable agent context, and author reusable agent skills that automate remediation and SRE support tasks.
- **Security automation:** Designed a vulnerability scanning workstream using reusable GitHub Actions, a custom Python Rally API library, and automated report generation, adopted org-wide.
- **Mentorship and teaching:** Mentor junior engineers in rotational programs; teach quarterly internal courses on Kubernetes Operators and Elasticsearch/Kibana.

**Featured Project: Warpstream Cluster Provisioning Platform (Q4 2025 - Q1 2026)**

- Architected the end-to-end design for Warpstream-based Kafka cluster provisioning: the networking design, the operator, agent, and resource specifications, and the resource flows from the customer-facing resource manager down to the backend infrastructure.
- Extended the platform's Kubernetes operators for net-new resource kinds and delivered a net-new Warpstream operator (Go) that generates all required Kubernetes resources and connects them into Cloud Storage buckets, Warpstream API registrations, and agent configs.
- Co-designed the Terraform cloud infrastructure for the Warpstream Clusters-as-a-Service deployment, including GCP Cloud Storage provisioning, VPC configuration, DNS, and IAM.
- Shipped to two of Optum's largest Apache Kafka on GCP customers as beta; Warpstream's diskless, Cloud Storage-based architecture eliminates local disk I/O from the stream processing data path, projected to reduce their annual Kafka infrastructure spend by approximately **80%**.

**Featured Project: Kafka Cluster Provisioning Platform on GCP**

- Build and operate the Kafka-as-a-Service provisioning platform on GCP: custom Kubernetes Operators (Go) own the full cluster lifecycle on GKE, integrated with GCS, IAM, VPC, and Artifact Registry through Terraform-managed cloud infrastructure.
- Delivered provisioning first through GitOps-driven CI/CD pipelines, then migrated it to GUI-based self-service in the enterprise marketplace developer platform, backed by the custom Terraform Provider and Kubernetes resource management control plane.

**Featured Project: Kafka Cluster Provisioning Platform on Bare-Metal**

- Build and operate the on-premise Kafka-as-a-Service platform on bare-metal Kubernetes: operators automate cluster provisioning, configuration, certificate management, and rolling upgrades across multi-tenant environments, delivered first through CI/CD pipelines and subsequently through the self-service developer platform.
- Keep streaming workloads available through node cycling via the custom bare-metal Kubernetes upgrade orchestration operator.

**Featured Project: Elasticsearch Provisioning Platform on GCP**

- Extended the Elasticsearch-as-a-Service operators into GCP, provisioning clusters on GKE with Terraform-managed cloud infrastructure and operator-driven GCP VolumeSnapshot backup and restore; provisioning ran first through CI/CD pipelines before migrating to the self-service developer platform.

**Featured Project: Elasticsearch Provisioning Platform on Bare-Metal**

- Build and operate Elasticsearch-as-a-Service on bare-metal Kubernetes: operators automate cluster provisioning, configuration, certificate management, and Kibana access, with Prometheus and Service Monitor operators providing observability across the fleet; provisioning moved from CI/CD pipelines to the self-service developer platform.

Technologies: Go, Kubebuilder, Kubernetes Operators, Helm, Terraform, GCP, GKE, GitHub Actions, Python, Kafka, Warpstream, Elasticsearch, Prometheus, Jenkins, Docker

### TDP Software Development Intern

Optum | Minneapolis, MN | Jun - Aug, 2017 - 2019

- Returned for three consecutive summer internships (June - August, 2017, 2018, and 2019) with similar roles and responsibilities each year.
- Contributed business-critical features to a monolithic application, complete with feature implementations and automated unit and integration testing.

Technologies: Java, Spring Boot, Groovy Spock

## Projects

### Yo-Yo Mount Visualizer (active development)

3D trick engine that models yo-yo string mounts as graph topologies and aims to discover new tricks through pathfinding. Encodes mounts as ordered, schema-validated string traversals with canonical serialization and hash-based deduplication, renders them in an interactive 3D visualizer with switchable cameras and timeline scrubbing, and animates transitions with a fixed-timestep Verlet rope physics simulation.

Technologies: TypeScript, React, react-three-fiber, 3D visualization, graph modeling, pathfinding, physics simulation, Zod schema validation, Vite, pnpm monorepo, vitest
Link: https://github.com/Rickyf115/yoyo-mount-visualizer

### Spin Ledger (closed source)

Single pane of glass for buy/sell/trade activity across skill toy community forums. Ingests unstructured, schemaless forum listings that resist conventional parsing, normalizes them into a taxonomy-aware data model, and serves them through an indexed, searchable marketplace dashboard, turning fragmented community commerce into structured, queryable data.

<!-- VERIFY: tech stack for Spin Ledger (languages, search/index layer, hosting) so a Technologies line can be added. -->

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

Google Cloud Certified - Cloud Digital Leader, Google, 2025
