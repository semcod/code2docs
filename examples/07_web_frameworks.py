"""Example 7: Web Framework Integration - Document Flask/FastAPI endpoints.

This example shows how to use code2docs with web frameworks
to automatically document your API endpoints.
"""

from code2docs.analyzers.endpoint_detector import EndpointDetector, Endpoint
from code2llm.api import analyze


# =============================================================================
# DETECTING ENDPOINTS
# =============================================================================


def detect_flask_endpoints(project_path: str) -> list[Endpoint]:
    """Detect Flask endpoints in a project."""
    result = analyze(project_path)
    
    detector = EndpointDetector()
    endpoints = detector.detect(result, project_path)
    
    # Filter for Flask endpoints
    flask_endpoints = [e for e in endpoints if e.framework == "flask"]
    
    print(f"Found {len(flask_endpoints)} Flask endpoints:")
    for ep in flask_endpoints:
        print(f"  {ep.method} {ep.path} -> {ep.function_name}")
    
    return flask_endpoints


def detect_fastapi_endpoints(project_path: str) -> list[Endpoint]:
    """Detect FastAPI endpoints in a project."""
    result = analyze(project_path)
    
    detector = EndpointDetector()
    endpoints = detector.detect(result, project_path)
    
    # Filter for FastAPI endpoints
    fastapi_endpoints = [e for e in endpoints if e.framework == "fastapi"]
    
    print(f"Found {len(fastapi_endpoints)} FastAPI endpoints:")
    for ep in fastapi_endpoints:
        print(f"  {ep.method} {ep.path} -> {ep.function_name}")
    
    return fastapi_endpoints


# =============================================================================
# GENERATING API DOCUMENTATION
# =============================================================================


def generate_api_docs_from_endpoints(project_path: str, output_dir: str = "docs/api") -> str:
    """Generate API documentation from detected endpoints."""
    from code2docs.formatters.markdown import MarkdownFormatter
    
    result = analyze(project_path)
    detector = EndpointDetector()
    endpoints = detector.detect(result, project_path)
    
    f = MarkdownFormatter()
    lines = []
    
    # Group by framework
    frameworks = {}
    for ep in endpoints:
        if ep.framework not in frameworks:
            frameworks[ep.framework] = []
        frameworks[ep.framework].append(ep)
    
    # Title
    lines.append(f.heading("API Reference", level=1))
    lines.append("")
    
    # Document each framework's endpoints
    for framework, eps in frameworks.items():
        lines.append(f.heading(f"{framework.title()} Endpoints", level=2))
        lines.append("")
        
        for ep in eps:
            lines.append(f.heading(f"{ep.method} {ep.path}", level=3))
            lines.append(f.paragraph(f"**Handler:** `{ep.function_name}`"))
            
            if ep.docstring:
                lines.append(f.paragraph(ep.docstring))
            
            if ep.params:
                lines.append(f.paragraph("**Parameters:**"))
                for param in ep.params:
                    lines.append(f.list_item(f"`{param}`"))
            
            if ep.return_type:
                lines.append(f.paragraph(f"**Returns:** `{ep.return_type}`"))
            
            lines.append("")
    
    return "\n".join(lines)


# =============================================================================
# EXAMPLE FLASK APP FOR TESTING
# =============================================================================

EXAMPLE_FLASK_APP = '''
"""Example Flask application."""
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/api/users', methods=['GET'])
def get_users():
    """Get all users."""
    return jsonify([{"id": 1, "name": "John"}])

@app.route('/api/users', methods=['POST'])
def create_user():
    """Create a new user."""
    data = request.get_json()
    return jsonify({"id": 2, "name": data["name"]}), 201

@app.route('/api/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    """Get a specific user by ID."""
    return jsonify({"id": user_id, "name": "John"})
'''

EXAMPLE_FASTAPI_APP = '''
"""Example FastAPI application."""
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    name: str
    email: str

@app.get("/api/users")
async def list_users():
    """List all users."""
    return [{"id": 1, "name": "John"}]

@app.post("/api/users")
async def create_user(user: User):
    """Create a new user."""
    return {"id": 2, **user.dict()}

@app.get("/api/users/{user_id}")
async def get_user(user_id: int):
    """Get a specific user."""
    return {"id": user_id, "name": "John"}
'''


def create_example_web_apps(target_dir: str = "./example_web_apps") -> None:
    """Create example Flask and FastAPI apps for testing."""
    from pathlib import Path
    
    Path(target_dir).mkdir(exist_ok=True)
    
    # Save Flask app
    Path(f"{target_dir}/flask_app.py").write_text(EXAMPLE_FLASK_APP)
    
    # Save FastAPI app
    Path(f"{target_dir}/fastapi_app.py").write_text(EXAMPLE_FASTAPI_APP)
    
    print(f"Created example web apps in {target_dir}/")


# =============================================================================
# COMPLETE WORKFLOW
# =============================================================================


def document_web_project(project_path: str) -> dict:
    """Complete workflow: detect endpoints and generate docs."""
    from code2docs import generate_readme, Code2DocsConfig
    
    # Detect all endpoints
    result = analyze(project_path)
    detector = EndpointDetector()
    endpoints = detector.detect(result, project_path)
    
    # Generate API documentation
    api_docs = generate_api_docs_from_endpoints(project_path)
    
    # Generate README with API info
    config = Code2DocsConfig(
        project_name="Web API Project",
        readme_sections=["header", "overview", "installation", "api"]
    )
    
    # Count endpoints by method
    method_counts = {}
    for ep in endpoints:
        method_counts[ep.method] = method_counts.get(ep.method, 0) + 1
    
    print("API Summary:")
    for method, count in method_counts.items():
        print(f"  {method}: {count} endpoints")
    
    return {
        "endpoints": endpoints,
        "api_docs": api_docs,
        "method_counts": method_counts,
    }


if __name__ == "__main__":
    # Create example apps
    # create_example_web_apps()
    
    # Detect endpoints
    # detect_flask_endpoints("./example_web_apps")
    # detect_fastapi_endpoints("./example_web_apps")
    
    # Generate full docs
    # result = document_web_project("./example_web_apps")
    pass
