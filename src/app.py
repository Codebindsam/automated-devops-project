from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Automated DevOps Deployment Framework</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background: #f4f7fb;
                margin: 0;
                padding: 0;
                color: #1f2937;
            }

            .header {
                background: #172554;
                color: white;
                padding: 30px;
                text-align: center;
            }

            .header h1 {
                margin: 0;
                font-size: 32px;
            }

            .header p {
                margin-top: 10px;
                font-size: 17px;
            }

            .container {
                max-width: 1100px;
                margin: 40px auto;
                padding: 20px;
            }

            .card-container {
                display: flex;
                flex-wrap: wrap;
                gap: 20px;
                justify-content: center;
            }

            .card {
                background: white;
                width: 280px;
                padding: 25px;
                border-radius: 12px;
                box-shadow: 0 4px 15px rgba(0,0,0,0.1);
            }

            .card h2 {
                color: #172554;
                margin-top: 0;
            }

            .card p {
                line-height: 1.6;
                color: #4b5563;
            }

            .status {
                background: #dcfce7;
                color: #166534;
                padding: 15px;
                border-radius: 8px;
                text-align: center;
                margin-bottom: 30px;
                font-weight: bold;
            }

            .workflow {
                background: white;
                margin-top: 40px;
                padding: 30px;
                border-radius: 12px;
                box-shadow: 0 4px 15px rgba(0,0,0,0.08);
            }

            .workflow h2 {
                color: #172554;
            }

            .workflow ol {
                line-height: 2;
                font-size: 17px;
            }

            footer {
                margin-top: 50px;
                background: #172554;
                color: white;
                text-align: center;
                padding: 20px;
            }
        </style>
    </head>

    <body>

        <div class="header">
            <h1>Automated DevOps Deployment Framework</h1>
            <p>Design and Implementation of an Automated CI/CD Deployment Pipeline</p>
        </div>

        <div class="container">

            <div class="status">
                ✓ Application is running successfully
            </div>

            <div class="card-container">

                <div class="card">
                    <h2>GitHub</h2>
                    <p>
                        Source code is maintained using GitHub for version
                        control and collaborative development.
                    </p>
                </div>

                <div class="card">
                    <h2>Terraform</h2>
                    <p>
                        Infrastructure as Code is used to automate and
                        standardize infrastructure provisioning.
                    </p>
                </div>

                <div class="card">
                    <h2>Jenkins</h2>
                    <p>
                        Jenkins automates the CI/CD workflow including
                        source checkout, build, testing and deployment.
                    </p>
                </div>

                <div class="card">
                    <h2>Docker</h2>
                    <p>
                        The application is packaged into a container image
                        to provide a consistent runtime environment.
                    </p>
                </div>

                <div class="card">
                    <h2>Kubernetes</h2>
                    <p>
                        Kubernetes manages application containers and
                        provides scalable and reliable deployment.
                    </p>
                </div>

                <div class="card">
                    <h2>Monitoring</h2>
                    <p>
                        Prometheus collects application metrics while
                        Grafana provides dashboards and observability.
                    </p>
                </div>

            </div>

            <div class="workflow">
                <h2>Deployment Workflow</h2>

                <ol>
                    <li>Developer commits application source code.</li>
                    <li>GitHub stores and manages the source code.</li>
                    <li>Terraform provisions the required infrastructure.</li>
                    <li>Jenkins automatically executes the CI/CD pipeline.</li>
                    <li>Docker builds and packages the application.</li>
                    <li>The container is deployed to Kubernetes.</li>
                    <li>Prometheus collects application and infrastructure metrics.</li>
                    <li>Grafana visualizes metrics through monitoring dashboards.</li>
                </ol>
            </div>

        </div>

        <footer>
            Automated DevOps Deployment Framework | CI/CD | Docker | Kubernetes | Monitoring
        </footer>

    </body>
    </html>
    """


@app.route("/health")
def health():
    return {"status": "healthy"}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
