from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier

ROLES = {
    "☕ Java Developer": {
        "key": "java",
        "model_name": "Logistic Regression",
        "model_class": "model-java",
        "color": "#3B82F6",
        "keywords": [
            "java", "j2ee", "spring", "hibernate", "maven", "junit", "jsp",
            "servlet", "jdbc", "rest", "soap", "microservices", "jvm", "springboot",
            "angular", "javascript", "sql", "orm", "jpa", "git", "jenkins",
            "docker", "aws", "tomcat", "weblogic", "websphere", "design patterns",
            "multithreading", "collections", "streams", "lambda"
        ],
    },
    "📊 Business Analyst": {
        "key": "ba",
        "model_name": "Decision Tree",
        "model_class": "model-ba",
        "color": "#10B981",
        "keywords": [
            "business analyst", "requirements", "stakeholder", "user stories",
            "gap analysis", "process improvement", "brd", "frd", "uml",
            "use case", "data analysis", "sql", "excel", "tableau", "powerbi",
            "jira", "agile", "scrum", "workflow", "documentation", "wireframe",
            "business intelligence", "reporting", "kpi", "metrics", "visio",
            "change management", "risk assessment", "uat", "testing"
        ],
    },
    "🗂️ Project Manager": {
        "key": "pm",
        "model_name": "Support Vector Machine",
        "model_class": "model-pm",
        "color": "#F59E0B",
        "keywords": [
            "project manager", "pmp", "scrum master", "agile", "waterfall",
            "sdlc", "budget", "resource planning", "risk management", "stakeholder",
            "milestone", "gantt", "ms project", "jira", "confluence", "delivery",
            "cross functional", "roadmap", "sprint", "kanban", "escalation",
            "vendor management", "pmo", "prince2", "timeline", "scope", "sla",
            "change management", "team leadership", "program management"
        ],
    },
    "⚙️ DevOps Engineer": {
        "key": "devops",
        "model_name": "Random Forest",
        "model_class": "model-devops",
        "color": "#EF4444",
        "keywords": [
            "devops", "docker", "kubernetes", "jenkins", "ci/cd", "aws",
            "azure", "gcp", "terraform", "ansible", "linux", "bash", "python",
            "git", "github", "gitlab", "monitoring", "prometheus", "grafana",
            "nginx", "apache", "microservices", "cloud", "infrastructure",
            "pipeline", "helm", "argocd", "elk", "splunk", "nagios",
            "automation", "scripting", "security", "networking"
        ],
    },
}

ROLE_MODELS = {
    "☕ Java Developer":   LogisticRegression(max_iter=500, class_weight="balanced"),
    "📊 Business Analyst": DecisionTreeClassifier(max_depth=10, class_weight="balanced"),
    "🗂️ Project Manager":  SVC(kernel="linear", probability=True, class_weight="balanced"),
    "⚙️ DevOps Engineer":  RandomForestClassifier(n_estimators=100, class_weight="balanced", random_state=42),
}

KEYWORD_THRESHOLD = 8
DATA_PATH = "data/resumes.csv"
