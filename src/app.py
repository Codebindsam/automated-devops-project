from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>Automated DevOps Deployment Framework</title>

    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: Arial, Helvetica, sans-serif;
            background: #0b1120;
            color: #e5e7eb;
            line-height: 1.6;
        }

        .container {
            width: 92%;
            max-width: 1250px;
            margin: auto;
        }

        /* Header */
        header {
            background: #111827;
            border-bottom: 1px solid #263244;
            padding: 20px 0;
            position: sticky;
            top: 0;
            z-index: 100;
        }

        .nav {
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .logo {
            font-size: 22px;
            font-weight: bold;
            color: #60a5fa;
        }

        .status {
            display: flex;
            align-items: center;
            gap: 8px;
            color: #86efac;
            font-size: 14px;
        }

        .status-dot {
            width: 10px;
            height: 10px;
            background: #22c55e;
            border-radius: 50%;
            box-shadow: 0 0 10px #22c55e;
        }

        /* Hero */
        .hero {
            padding: 80px 0 60px;
            text-align: center;
        }

        .hero h1 {
            font-size: 48px;
            margin-bottom: 20px;
            color: white;
        }

        .hero h1 span {
            color: #60a5fa;
        }

        .hero p {
            max-width: 850px;
            margin: auto;
            color: #9ca3af;
            font-size: 18px;
        }

        .hero-badge {
            display: inline-block;
            margin-bottom: 25px;
            padding: 8px 16px;
            border: 1px solid #2563eb;
            border-radius: 30px;
            color: #93c5fd;
            background: #172554;
        }

        /* Sections */
        section {
            padding: 55px 0;
        }

        .section-title {
            text-align: center;
            margin-bottom: 40px;
        }

        .section-title h2 {
            font-size: 32px;
            color: white;
            margin-bottom: 10px;
        }

        .section-title p {
            color: #9ca3af;
        }

        /* Architecture flow */
        .pipeline {
            display: flex;
            align-items: center;
            justify-content: center;
            flex-wrap: wrap;
            gap: 12px;
        }

        .pipeline-step {
            background: #111827;
            border: 1px solid #334155;
            border-radius: 12px;
            padding: 18px 22px;
            min-width: 145px;
            text-align: center;
            transition: 0.2s;
        }

        .pipeline-step:hover {
            border-color: #60a5fa;
            transform: translateY(-3px);
        }

        .pipeline-icon {
            font-size: 30px;
            margin-bottom: 8px;
        }

        .pipeline-step strong {
            display: block;
            color: white;
        }

        .pipeline-step small {
            color: #94a3b8;
        }

        .arrow {
            color: #60a5fa;
            font-size: 25px;
            font-weight: bold;
        }

        /* Cards */
        .cards {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 20px;
        }

        .card {
            background: #111827;
            border: 1px solid #263244;
            border-radius: 14px;
            padding: 25px;
        }

        .card:hover {
            border-color: #3b82f6;
        }

        .card-icon {
            font-size: 35px;
            margin-bottom: 15px;
        }

        .card h3 {
            color: white;
            margin-bottom: 10px;
        }

        .card p {
            color: #9ca3af;
            font-size: 15px;
        }

        /* Status table */
        .status-table {
            width: 100%;
            border-collapse: collapse;
            background: #111827;
            border-radius: 14px;
            overflow: hidden;
        }

        .status-table th,
        .status-table td {
            padding: 16px 20px;
            text-align: left;
            border-bottom: 1px solid #263244;
        }

        .status-table th {
            background: #172033;
            color: #93c5fd;
        }

        .status-table td {
            color: #d1d5db;
        }

        .online {
            color: #86efac !important;
            font-weight: bold;
        }

        /* About */
        .about {
            background: #111827;
            border: 1px solid #263244;
            border-radius: 16px;
            padding: 35px;
        }

        .about p {
            color: #aeb8c7;
            margin-bottom: 15px;
        }

        .about ul {
            margin-left: 25px;
            color: #aeb8c7;
        }

        .about li {
            margin-bottom: 8px;
        }

        /* Footer */
        footer {
            border-top: 1px solid #263244;
            background: #080d18;
            padding: 30px 0;
            text-align: center;
            color: #64748b;
            margin-top: 40px;
        }

        .health {
            margin-top: 25px;
            display: inline-block;
            padding: 10px 20px;
            background: #052e16;
            border: 1px solid #166534;
            border-radius: 8px;
            color: #86efac;
        }

        @media (max-width: 900px) {
            .cards {
                grid-template-columns: 1fr 1fr;
            }

            .hero h1 {
                font-size: 38px;
            }
        }

        @media (max-width: 600px) {
            .cards {
                grid-template-columns: 1fr;
            }

            .pipeline {
                flex-direction: column;
            }

            .arrow {
                transform: rotate(90deg);
            }

            .hero h1 {
                font-size: 30px;
            }

            .status-table {
                font-size: 13px;
            }
        }
    </style>
</head>

<body>

<header>
    <div class="container nav">
        <div class="logo">⚙ DevOps Framework</div>

        <div class="status">
            <span class="status-dot"></span>
            Application Running
        </div>
    </div>
</header>


<!-- HERO -->
<section class="hero">
    <div class="container">

        <div class="hero-badge">
            Automated DevOps Deployment Framework
        </div>

        <h1>
            Build. Deploy. <span>Monitor.</span>
        </h1>

        <p>
            A complete DevOps deployment framework that automates
            application delivery from source-code management through
            CI/CD, containerization, Kubernetes deployment, and
            monitoring.
        </p>

        <div class="health">
            ✓ Application is healthy and running
        </div>

    </div>
</section>


<!-- WORKFLOW -->
<section>
    <div class="container">

        <div class="section-title">
            <h2>Deployment Workflow</h2>
            <p>Automated flow from source code to application monitoring</p>
        </div>

        <div class="pipeline">

            <div class="pipeline-step">
                <div class="pipeline-icon">👨‍💻</div>
                <strong>Developer</strong>
                <small>Writes Code</small>
            </div>

            <div class="arrow">→</div>

            <div class="pipeline-step">
                <div class="pipeline-icon">🐙</div>
                <strong>GitHub</strong>
                <small>Source Control</small>
            </div>

            <div class="arrow">→</div>

            <div class="pipeline-step">
                <div class="pipeline-icon">🏗️</div>
                <strong>Terraform</strong>
                <small>Infrastructure</small>
            </div>

            <div class="arrow">→</div>

            <div class="pipeline-step">
                <div class="pipeline-icon">🔨</div>
                <strong>Jenkins</strong>
                <small>CI/CD Pipeline</small>
            </div>

            <div class="arrow">→</div>

            <div class="pipeline-step">
                <div class="pipeline-icon">🐳</div>
                <strong>Docker</strong>
                <small>Container Registry</small>
            </div>

            <div class="arrow">→</div>

            <div class="pipeline-step">
                <div class="pipeline-icon">☸️</div>
                <strong>Kubernetes</strong>
                <small>Application Deploy</small>
            </div>

            <div class="arrow">→</div>

            <div class="pipeline-step">
                <div class="pipeline-icon">📊</div>
                <strong>Monitoring</strong>
                <small>Prometheus + Grafana</small>
            </div>

        </div>

    </div>
</section>


<!-- COMPONENTS -->
<section>
    <div class="container">

        <div class="section-title">
            <h2>DevOps Components</h2>
            <p>Technologies used in the deployment framework</p>
        </div>

        <div class="cards">

            <div class="card">
                <div class="card-icon">🐙</div>
                <h3>GitHub</h3>
                <p>
                    Provides source-code management and version control,
                    allowing application changes to be tracked and
                    integrated into the deployment workflow.
                </p>
            </div>

            <div class="card">
                <div class="card-icon">🏗️</div>
                <h3>Terraform</h3>
                <p>
                    Infrastructure as Code is used to define and
                    provision the infrastructure required by the
                    application environment.
                </p>
            </div>

            <div class="card">
                <div class="card-icon">🔨</div>
                <h3>Jenkins</h3>
                <p>
                    Automates the CI/CD process including source-code
                    checkout, application build, testing, Docker image
                    creation, and image publishing.
                </p>
            </div>

            <div class="card">
                <div class="card-icon">🐳</div>
                <h3>Docker</h3>
                <p>
                    Packages the application and its dependencies into
                    a portable container image for consistent deployment.
                </p>
            </div>

            <div class="card">
                <div class="card-icon">☸️</div>
                <h3>Kubernetes</h3>
                <p>
                    Manages application containers, deployments,
                    services, networking, and application availability.
                </p>
            </div>

            <div class="card">
                <div class="card-icon">📈</div>
                <h3>Prometheus & Grafana</h3>
                <p>
                    Prometheus collects application and infrastructure
                    metrics while Grafana provides dashboards for
                    monitoring and observability.
                </p>
            </div>

        </div>

    </div>
</section>


<!-- STATUS -->
<section>
    <div class="container">

        <div class="section-title">
            <h2>System Status</h2>
            <p>Current application and DevOps environment overview</p>
        </div>

        <table class="status-table">

            <tr>
                <th>Component</th>
                <th>Function</th>
                <th>Status</th>
            </tr>

            <tr>
                <td>Flask Application</td>
                <td>Web Application</td>
                <td class="online">● Running</td>
            </tr>

            <tr>
                <td>Docker</td>
                <td>Containerization</td>
                <td class="online">● Configured</td>
            </tr>

            <tr>
                <td>Kubernetes</td>
                <td>Container Orchestration</td>
                <td class="online">● Deployed</td>
            </tr>

            <tr>
                <td>Prometheus</td>
                <td>Metrics Collection</td>
                <td class="online">● Monitoring</td>
            </tr>

            <tr>
                <td>Grafana</td>
                <td>Metrics Visualization</td>
                <td class="online">● Dashboard Ready</td>
            </tr>

        </table>

    </div>
</section>


<!-- PROJECT DESCRIPTION -->
<section>
    <div class="container">

        <div class="section-title">
            <h2>About the Project</h2>
        </div>

        <div class="about">

            <p>
                The Automated DevOps Deployment Framework is designed
                to demonstrate an end-to-end approach for automating
                application deployment and monitoring.
            </p>

            <p>
                The framework integrates source-code management,
                infrastructure provisioning, continuous integration
                and continuous deployment, containerization,
                Kubernetes orchestration, and monitoring.
            </p>

            <p><strong>Key objectives:</strong></p>

            <ul>
                <li>Automate application deployment.</li>
                <li>Use Infrastructure as Code for infrastructure management.</li>
                <li>Implement a CI/CD pipeline using Jenkins.</li>
                <li>Containerize applications using Docker.</li>
                <li>Deploy and manage containers using Kubernetes.</li>
                <li>Collect application and infrastructure metrics.</li>
                <li>Visualize system performance using Grafana dashboards.</li>
            </ul>

        </div>

    </div>
</section>


<footer>
    <div class="container">
        Automated DevOps Deployment Framework
        <br>
        Flask • Docker • Kubernetes • Prometheus • Grafana • Jenkins • Terraform
    </div>
</footer>

</body>
</html>
"""


@app.route("/")
def home():
    return render_template_string(HTML)


@app.route("/health")
def health():
    return {
        "status": "healthy",
        "application": "Automated DevOps Deployment Framework"
    }


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
