
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Customer Churn Prediction | Week 10</title>
    <style>
        :root {
            --primary: #2563eb;
            --dark: #0f172a;
            --muted: #64748b;
            --bg: #f8fafc;
            --card: #ffffff;
            --border: #e2e8f0;
        }

        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }

        body {
            font-family: Arial, Helvetica, sans-serif;
            background: var(--bg);
            color: var(--dark);
            line-height: 1.7;
        }

        header {
            background: linear-gradient(135deg, #0f172a, #1d4ed8);
            color: white;
            text-align: center;
            padding: 65px 20px;
        }

        header .tag {
            display: inline-block;
            padding: 5px 14px;
            border: 1px solid #93c5fd;
            border-radius: 30px;
            font-size: 13px;
            margin-bottom: 18px;
        }

        header h1 {
            font-size: clamp(30px, 5vw, 48px);
            margin-bottom: 12px;
        }

        header p {
            max-width: 720px;
            margin: auto;
            color: #dbeafe;
        }

        nav {
            background: white;
            border-bottom: 1px solid var(--border);
            padding: 15px;
            text-align: center;
        }

        nav a {
            color: var(--primary);
            text-decoration: none;
            margin: 0 12px;
            font-weight: bold;
            font-size: 14px;
        }

        main {
            max-width: 1050px;
            margin: 35px auto;
            padding: 0 20px;
        }

        section {
            background: var(--card);
            border: 1px solid var(--border);
            border-radius: 14px;
            padding: 28px;
            margin-bottom: 25px;
            scroll-margin-top: 20px;
        }

        h2 {
            font-size: 25px;
            margin-bottom: 15px;
        }

        h3 {
            margin: 15px 0 8px;
        }

        p {
            margin-bottom: 12px;
        }

        ul, ol {
            padding-left: 23px;
            margin: 10px 0;
        }

        li {
            margin-bottom: 7px;
        }

        .grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(210px, 1fr));
            gap: 16px;
        }

        .feature {
            padding: 18px;
            border: 1px solid var(--border);
            border-radius: 10px;
            background: #f8fafc;
        }

        .feature h3 {
            color: var(--primary);
            margin-top: 0;
        }

        .badge {
            display: inline-block;
            background: #dbeafe;
            color: #1d4ed8;
            padding: 5px 11px;
            border-radius: 20px;
            font-size: 13px;
            margin: 4px;
        }

        code {
            background: #eff6ff;
            color: #1d4ed8;
            padding: 3px 6px;
            border-radius: 4px;
        }

        pre {
            background: #0f172a;
            color: #e2e8f0;
            padding: 18px;
            border-radius: 10px;
            overflow-x: auto;
            margin: 15px 0;
        }

        pre code {
            background: transparent;
            color: inherit;
            padding: 0;
        }

        .note {
            border-left: 4px solid var(--primary);
            background: #eff6ff;
            padding: 15px;
            border-radius: 5px;
            margin: 15px 0;
        }

        .button {
            display: inline-block;
            background: var(--primary);
            color: white;
            text-decoration: none;
            padding: 11px 18px;
            border-radius: 8px;
            margin: 8px 5px 0 0;
        }

        .button:hover {
            background: #1d4ed8;
        }

        footer {
            text-align: center;
            padding: 30px 15px;
            background: var(--dark);
            color: #cbd5e1;
        }

        footer a {
            color: #93c5fd;
        }

        @media (max-width: 600px) {
            header {
                padding: 45px 18px;
            }

            section {
                padding: 20px;
            }

            nav a {
                display: inline-block;
                margin: 5px 8px;
            }
        }
    </style>
</head>

<body>

<header>
    <span class="tag">DEVELOPER'S ARENA · WEEK 10</span>
    <h1>Customer Churn Prediction</h1>
    <p>
        An end-to-end machine learning project focused on customer
        data analysis, preprocessing, feature engineering, and
        predictive modeling to support customer retention.
    </p>

    <a class="button"
       href="churn_prediction_pipeline.ipynb">
       Explore Notebook
    </a>

    <a class="button"
       href="Customer_Churn_Prediction_Report.pdf">
       View Project Report
    </a>
</header>

<nav>
    <a href="#overview">Overview</a>
    <a href="#objectives">Objectives</a>
    <a href="#workflow">Workflow</a>
    <a href="#files">Project Files</a>
    <a href="#installation">Setup</a>
</nav>

<main>

    <section id="overview">
        <h2>📌 Project Overview</h2>
        <p>
            Customer churn occurs when customers stop using a
            company's products or services. Predicting churn helps
            organizations identify customers who may leave and
            develop targeted retention strategies.
        </p>
        <p>
            This project explores customer data through preprocessing,
            feature engineering, model development, and evaluation.
            The Jupyter Notebook contains the primary analysis and
            prediction workflow.
        </p>

        <div class="grid">
            <div class="feature">
                <h3>🔎 Data Analysis</h3>
                <p>Inspect the dataset and understand customer patterns.</p>
            </div>
            <div class="feature">
                <h3>🧹 Preprocessing</h3>
                <p>Prepare the data for reliable machine learning.</p>
            </div>
            <div class="feature">
                <h3>⚙️ Feature Engineering</h3>
                <p>Transform relevant variables for model development.</p>
            </div>
            <div class="feature">
                <h3>📊 Evaluation</h3>
                <p>Review model metrics and validation outputs.</p>
            </div>
        </div>
    </section>

    <section id="objectives">
        <h2>🎯 Project Objectives</h2>
        <ul>
            <li>Understand the structure and quality of customer data.</li>
            <li>Identify missing values, data inconsistencies, and outliers.</li>
            <li>Prepare and transform features for machine learning.</li>
            <li>Build a workflow for customer churn prediction.</li>
            <li>Evaluate model performance using appropriate metrics.</li>
            <li>Document preprocessing, validation, and evaluation results.</li>
        </ul>
    </section>

    <section id="technologies">
        <h2>🛠️ Technologies Used</h2>
        <span class="badge">Python</span>
        <span class="badge">Jupyter Notebook</span>
        <span class="badge">Pandas</span>
        <span class="badge">NumPy</span>
        <span class="badge">Scikit-learn</span>
        <span class="badge">Matplotlib</span>
        <span class="badge">Seaborn</span>
        <span class="badge">Machine Learning</span>

        <p style="margin-top: 15px;">
            Refer to <code>requirements.txt</code> for the project's
            Python dependencies.
        </p>
    </section>

    <section id="workflow">
        <h2>🔄 Project Workflow</h2>
        <ol>
            <li><strong>Data loading:</strong> Load the customer dataset.</li>
            <li><strong>Data validation:</strong> Check dataset structure and quality.</li>
            <li><strong>Preprocessing:</strong> Handle data preparation and cleaning.</li>
            <li><strong>Feature engineering:</strong> Transform relevant input features.</li>
            <li><strong>Model development:</strong> Train the prediction model.</li>
            <li><strong>Model evaluation:</strong> Review the calculated evaluation metrics.</li>
            <li><strong>Documentation:</strong> Save reports and supporting outputs.</li>
        </ol>

        <div class="note">
            <strong>Note:</strong> The exact preprocessing steps, model
            algorithms, and evaluation results should be verified against
            the included Jupyter Notebook and report.
        </div>
    </section>

    <section id="files">
        <h2>📂 Project Structure</h2>
        <pre><code>WEEK 10/
├── churn_prediction_pipeline.ipynb
├── churn_data.csv
├── Customer_Churn_Prediction_Report.pdf
├── dataset_validation.json
├── feature_engineering_documentation.md
├── model_metrics.csv
├── outlier_report.csv
├── preprocessing_report.md
├── requirements.txt
├── validation_execution.json
└── SCREENSHOTS/
    └── Project screenshots</code></pre>

        <h3>Important Files</h3>
        <ul>
            <li><code>churn_prediction_pipeline.ipynb</code>:
                Main analysis and machine learning notebook.</li>
            <li><code>churn_data.csv</code>:
                Dataset used by the project.</li>
            <li><code>Customer_Churn_Prediction_Report.pdf</code>:
                Project report.</li>
            <li><code>preprocessing_report.md</code>:
                Preprocessing documentation.</li>
            <li><code>feature_engineering_documentation.md</code>:
                Feature engineering notes.</li>
            <li><code>model_metrics.csv</code>:
                Recorded model evaluation metrics.</li>
            <li><code>dataset_validation.json</code>:
                Dataset validation output.</li>
            <li><code>outlier_report.csv</code>:
                Recorded outlier analysis output.</li>
            <li><code>validation_execution.json</code>:
                Validation execution details.</li>
            <li><code>SCREENSHOTS/</code>:
                Supporting project screenshots.</li>
        </ul>
    </section>

    <section id="installation">
        <h2>🚀 Installation and Usage</h2>

        <h3>1. Clone the Repository</h3>
        <pre><code>git clone https://github.com/HARIESHSARAVANAN/DEVELOPER-S-ARENA-.git
cd DEVELOPER-S-ARENA-</code></pre>

        <h3>2. Navigate to Week 10</h3>
        <pre><code>cd "WEEK 10"</code></pre>

        <h3>3. Create a Virtual Environment (Recommended)</h3>
        <pre><code>python -m venv .venv</code></pre>

        <p>Activate it on Windows Git Bash:</p>
        <pre><code>source .venv/Scripts/activate</code></pre>

        <h3>4. Install Dependencies</h3>
        <pre><code>python -m pip install -r requirements.txt</code></pre>

        <h3>5. Run the Notebook</h3>
        <pre><code>jupyter notebook churn_prediction_pipeline.ipynb</code></pre>

        <p>
            If Jupyter Notebook is not installed, install it in the
            active environment before running the command.
        </p>
    </section>

    <section id="evaluation">
        <h2>📈 Model Evaluation</h2>
        <p>
            Model performance should be assessed using metrics
            appropriate for the classification task.
        </p>
        <ul>
            <li>Accuracy</li>
            <li>Precision</li>
            <li>Recall</li>
            <li>F1-score</li>
            <li>Confusion matrix</li>
        </ul>
        <p>
            Consult <code>model_metrics.csv</code> and the notebook
            for the actual metrics generated by this project.
            No performance values are assumed here.
        </p>
    </section>

    <section id="future">
        <h2>🔮 Future Improvements</h2>
        <ul>
            <li>Compare multiple classification algorithms.</li>
            <li>Use cross-validation and systematic hyperparameter tuning.</li>
            <li>Address class imbalance where appropriate.</li>
            <li>Improve model interpretability and feature analysis.</li>
            <li>Build a simple interface for churn risk predictions.</li>
            <li>Develop actionable customer retention recommendations.</li>
        </ul>
    </section>

    <section id="author">
        <h2>👨‍💻 Author</h2>
        <p><strong>Hariesh Saravanan</strong></p>
        <p>B.Tech Artificial Intelligence and Data Science</p>
        <a class="button"
           href="https://github.com/HARIESHSARAVANAN"
           target="_blank"
           rel="noopener noreferrer">
            Visit GitHub Profile
        </a>
    </section>

</main>

<footer>
    <p>Customer Churn Prediction · Developer's Arena · Week 10</p>
    <p>Built as a machine learning learning project.</p>
</footer>

</body>
</html>
