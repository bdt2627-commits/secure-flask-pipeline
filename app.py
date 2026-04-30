from flask import Flask

app = Flask(__name__)

# --- नया प्रोफेशनल लाइट-थीम डिज़ाइन ---
clean_design = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Professional Portfolio | DevSecOps</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; }
        body { background-color: #f8fafc; color: #1e293b; }
        
        /* नेविगेशन */
        nav { background: white; padding: 20px 10%; display: flex; justify-content: space-between; align-items: center; box-shadow: 0 2px 10px rgba(0,0,0,0.05); position: fixed; width: 100%; top: 0; z-index: 100; }
        .nav-brand { font-weight: 800; font-size: 1.2rem; color: #2563eb; }
        .nav-links { display: flex; gap: 25px; }
        .nav-links a { text-decoration: none; color: #64748b; font-weight: 500; font-size: 0.9rem; }

        /* हीरो सेक्शन */
        .hero { background: white; padding: 150px 10% 80px 10%; text-align: left; border-bottom: 1px solid #e2e8f0; }
        .hero h1 { font-size: 3rem; color: #0f172a; margin-bottom: 20px; line-height: 1.2; }
        .hero p { font-size: 1.25rem; color: #475569; max-width: 700px; margin-bottom: 30px; }
        
        .badge-container { display: flex; gap: 10px; margin-bottom: 20px; }
        .badge { background: #dcfce7; color: #166534; padding: 6px 15px; border-radius: 20px; font-size: 0.85rem; font-weight: bold; border: 1px solid #bbf7d0; }

        /* सेक्शन स्टाइल */
        .container { padding: 80px 10%; }
        h2 { font-size: 2rem; margin-bottom: 40px; color: #0f172a; display: flex; align-items: center; gap: 15px; }
        h2::after { content: ""; height: 2px; background: #cbd5e1; flex-grow: 1; }

        /* ग्रिड सिस्टम */
        .grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 30px; }
        .card { background: white; padding: 35px; border-radius: 12px; border: 1px solid #e2e8f0; transition: 0.3s; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1); }
        .card:hover { transform: translateY(-5px); box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1); border-color: #2563eb; }
        .card h3 { margin-bottom: 15px; color: #1e293b; font-size: 1.25rem; }
        .card p { color: #64748b; font-size: 0.95rem; line-height: 1.7; }

        footer { background: #0f172a; color: #94a3b8; padding: 50px 10%; text-align: center; }
        .btn { background: #2563eb; color: white; padding: 12px 25px; border-radius: 8px; text-decoration: none; font-weight: bold; display: inline-block; }
    </style>
</head>
<body>

    <nav>
        <div class="nav-brand">PORTFOLIO.SYS</div>
        <div class="nav-links">
            <a href="#skills">SKILLS</a>
            <a href="#experience">EXPERIENCE</a>
            <a href="#projects">PROJECTS</a>
        </div>
    </nav>

    <div class="hero">
        <div class="badge-container">
            <div class="badge">SECURE DEPLOYMENT ACTIVE</div>
            <div class="badge" style="background:#eff6ff; color:#1d4ed8; border-color:#dbeafe;">CERTIFIED BCA GRADUATE</div>
        </div>
        <h1>DevSecOps & Cloud Security <br><span style="color:#2563eb;">Infrastructure Engineer.</span></h1>
        <p>Specializing in automated security pipelines, containerization with Docker, and building resilient software infrastructures for modern cloud environments.</p>
        <a href="#projects" class="btn">View Live Projects</a>
    </div>

    <div class="container" id="skills">
        <h2>Technical Core</h2>
        <div class="grid">
            <div class="card">
                <h3>Cloud Operations</h3>
                <p>Advanced knowledge of Docker containerization, managing microservices, and port-level network configurations.</p>
            </div>
            <div class="card">
                <h3>Development</h3>
                <p>Full-stack development using Python and Flask, with a strong foundation in BCA-level software engineering.</p>
            </div>
            <div class="card">
                <h3>Security Systems</h3>
                <p>Implementing DevSecOps principles, vulnerability scanning, and secure API management for web applications.</p>
            </div>
        </div>
    </div>

    <div class="container" id="experience" style="background: #f1f5f9;">
        <h2>Practical Experience</h2>
        <div class="card" style="max-width: 800px;">
            <h3 style="color:#2563eb;">Android Development Intern | Prodigy InfoTech</h3>
            <p style="margin-bottom: 10px;"><strong>Duration:</strong> 136 Hours (Completed April 2026)</p>
            <p>Focused on developing high-performance mobile applications and understanding the complete software development lifecycle in a professional setting.</p>
        </div>
    </div>

    <footer>
        <p>Targeting Professional Opportunities in the UAE Job Market (Dubai & Abu Dhabi)</p>
        <p style="margin-top: 15px; font-size: 0.8rem;">&copy; 2026 Professional DevSecOps Portfolio. Built with Docker & Flask.</p>
    </footer>

</body>
</html>
"""

@app.route('/')
def home():
    return clean_design

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)