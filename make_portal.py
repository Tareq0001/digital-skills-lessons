import os
import re

deploy_dir = r'C:\Users\abuos\.gemini\antigravity\scratch\deploy_lessons'
f2 = r'C:\Users\abuos\Desktop\درس_الوسائط_المتعددة.html'

with open(f2, 'r', encoding='utf-8') as f:
    multimedia_html = f.read()

# Extract logo img tags
logos_match = re.search(r'<div class="logos">([\s\S]*?)</div>', multimedia_html)
logos_html = logos_match.group(1) if logos_match else ""

portal_html = f"""<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>منصة دروس المهارات الرقمية - أ. طارق ابوعشي</title>
    <link href="https://fonts.googleapis.com/css2?family=Tajawal:wght@400;500;700;800;900&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        :root {{
            --primary: #6366f1;
            --primary-dark: #4f46e5;
            --bg: #0f172a;
            --card-bg: #1e293b;
            --text: #f8fafc;
            --text-muted: #94a3b8;
        }}
        * {{ box-sizing: border-box; margin: 0; padding: 0; }}
        body {{
            font-family: 'Tajawal', sans-serif;
            background: var(--bg);
            color: var(--text);
            min-height: 100vh;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: space-between;
            padding: 2rem 1rem;
            position: relative;
            overflow-x: hidden;
        }}
        
        /* Background Glows */
        .glow-1 {{
            position: absolute;
            top: -100px; right: -100px;
            width: 400px; height: 400px;
            background: radial-gradient(circle, rgba(99, 102, 241, 0.15) 0%, transparent 70%);
            pointer-events: none;
        }}
        .glow-2 {{
            position: absolute;
            bottom: -100px; left: -100px;
            width: 400px; height: 400px;
            background: radial-gradient(circle, rgba(236, 72, 153, 0.15) 0%, transparent 70%);
            pointer-events: none;
        }}
        
        .container {{
            max-width: 1100px;
            width: 100%;
            margin: 0 auto;
            text-align: center;
            z-index: 10;
        }}
        
        /* Logos Header */
        .logos {{
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 24px;
            margin-bottom: 24px;
            flex-wrap: wrap;
        }}
        .logos img {{
            height: 75px;
            object-fit: contain;
            filter: drop-shadow(0 4px 12px rgba(0,0,0,0.3));
        }}
        
        .hero-title {{
            font-size: clamp(1.8rem, 5vw, 2.8rem);
            font-weight: 900;
            background: linear-gradient(135deg, #a5b4fc 0%, #38bdf8 50%, #f472b6 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 12px;
        }}
        .hero-subtitle {{
            font-size: 1.15rem;
            color: var(--text-muted);
            margin-bottom: 8px;
        }}
        .hero-badge {{
            display: inline-block;
            background: rgba(99, 102, 241, 0.15);
            border: 1px solid rgba(99, 102, 241, 0.3);
            color: #a5b4fc;
            padding: 6px 18px;
            border-radius: 30px;
            font-size: 0.95rem;
            font-weight: 700;
            margin-bottom: 35px;
        }}
        
        /* Cards Grid */
        .cards-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 24px;
            margin-bottom: 40px;
        }}
        
        .lesson-card {{
            background: var(--card-bg);
            border: 1px solid #334155;
            border-radius: 20px;
            padding: 30px 24px;
            text-align: right;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            position: relative;
            overflow: hidden;
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
            text-decoration: none;
            color: inherit;
        }}
        .lesson-card::before {{
            content: '';
            position: absolute;
            top: 0; left: 0; right: 0;
            height: 5px;
        }}
        .card-1::before {{ background: linear-gradient(90deg, #3b82f6, #06b6d4); }}
        .card-2::before {{ background: linear-gradient(90deg, #8b5cf6, #ec4899); }}
        .card-3::before {{ background: linear-gradient(90deg, #10b981, #3b82f6); }}
        
        .lesson-card:hover {{
            transform: translateY(-8px);
            border-color: #6366f1;
            box-shadow: 0 20px 40px rgba(0, 0, 0, 0.4);
        }}
        
        .card-top {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 18px;
        }}
        .grade-tag {{
            font-size: 0.8rem;
            font-weight: 800;
            padding: 4px 12px;
            border-radius: 20px;
        }}
        .tag-1 {{ background: rgba(59, 130, 246, 0.15); color: #60a5fa; }}
        .tag-2 {{ background: rgba(139, 92, 246, 0.15); color: #c084fc; }}
        .tag-3 {{ background: rgba(16, 185, 129, 0.15); color: #34d399; }}
        
        .card-icon {{
            font-size: 2.5rem;
        }}
        
        .lesson-name {{
            font-size: 1.35rem;
            font-weight: 800;
            margin-bottom: 10px;
            color: #f8fafc;
        }}
        .lesson-desc {{
            font-size: 0.95rem;
            color: var(--text-muted);
            line-height: 1.6;
            margin-bottom: 20px;
            flex-grow: 1;
        }}
        
        .features-list {{
            display: flex;
            flex-wrap: wrap;
            gap: 6px;
            margin-bottom: 24px;
        }}
        .feature-pill {{
            background: #0f172a;
            border: 1px solid #334155;
            color: #cbd5e1;
            font-size: 0.75rem;
            padding: 4px 10px;
            border-radius: 8px;
        }}
        
        .card-btn {{
            width: 100%;
            padding: 12px;
            border-radius: 12px;
            border: none;
            font-family: inherit;
            font-size: 1rem;
            font-weight: 800;
            color: #fff;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 8px;
            cursor: pointer;
            transition: 0.2s;
        }}
        .btn-1 {{ background: linear-gradient(135deg, #2563eb, #0891b2); }}
        .btn-2 {{ background: linear-gradient(135deg, #7c3aed, #db2777); }}
        .btn-3 {{ background: linear-gradient(135deg, #059669, #0284c7); }}
        
        /* Footer */
        footer {{
            border-top: 1px solid #334155;
            padding-top: 20px;
            color: var(--text-muted);
            font-size: 0.9rem;
            text-align: center;
            width: 100%;
            max-width: 1100px;
        }}
        footer strong {{ color: #e2e8f0; }}
    </style>
</head>
<body>
    <div class="glow-1"></div>
    <div class="glow-2"></div>

    <div class="container">
        <!-- Logos -->
        <div class="logos">
            {logos_html}
        </div>

        <h1 class="hero-title">بوابة دروس المهارات الرقمية التفاعلية</h1>
        <p class="hero-subtitle">متوسطة أبها الأهلية (بنين) — شركة مواهب التربية للتعليم والتدريب</p>
        <div class="hero-badge">👨‍🏫 إعداد وتقديم: أ. طارق ابوعشي</div>

        <!-- Lessons Cards Grid -->
        <div class="cards-grid">
            <!-- 1st Intermediate -->
            <a href="grade1.html" class="lesson-card card-1">
                <div>
                    <div class="card-top">
                        <span class="grade-tag tag-1">الصف الأول متوسط</span>
                        <span class="card-icon">💻</span>
                    </div>
                    <h2 class="lesson-name">درس أجهزة الحاسب</h2>
                    <p class="lesson-desc">رحلة تفاعلية للتعرف على أنواع الحواسيب، أجزاء اللوحة الأم، وحدات الإدخال والإخراج، وأجهزة التخزين مع ألعاب تفاعلية واختبار ختامي.</p>
                    <div class="features-list">
                        <span class="feature-pill">🎮 لعبة سحب وتصنيف</span>
                        <span class="feature-pill">🧩 مطابقة أجهزة التخزين</span>
                        <span class="feature-pill">📝 اختبار تفاعلي 8 أسئلة</span>
                    </div>
                </div>
                <div class="card-btn btn-1">
                    <span>دخول الدرس الآن</span>
                    <i class="fas fa-arrow-left"></i>
                </div>
            </a>

            <!-- 2nd Intermediate -->
            <a href="grade2.html" class="lesson-card card-2">
                <div>
                    <div class="card-top">
                        <span class="grade-tag tag-2">الصف الثاني متوسط</span>
                        <span class="card-icon">🎬</span>
                    </div>
                    <h2 class="lesson-name">درس الوسائط المتعددة</h2>
                    <p class="lesson-desc">تعلم مفهوم الوسائط، تمييز امتدادات الصور والصوت والفيديو، مع لعبة التصنيف والسيناريوهات و<strong>استوديو مونتاج الفيديو العملي</strong>.</p>
                    <div class="features-list">
                        <span class="feature-pill">🎬 استوديو مونتاج عملي</span>
                        <span class="feature-pill">🎵 مؤثرات صوتية حية</span>
                        <span class="feature-pill">🎮 لعبة الامتدادات</span>
                        <span class="feature-pill">📝 اختبار فوري</span>
                    </div>
                </div>
                <div class="card-btn btn-2">
                    <span>دخول الدرس الآن</span>
                    <i class="fas fa-arrow-left"></i>
                </div>
            </a>

            <!-- 3rd Intermediate -->
            <a href="grade3.html" class="lesson-card card-3">
                <div>
                    <div class="card-top">
                        <span class="grade-tag tag-3">الصف الثالث متوسط</span>
                        <span class="card-icon">🛡️</span>
                    </div>
                    <h2 class="lesson-name">مقدمة في الأمن السيبراني</h2>
                    <p class="lesson-desc">استكشف مثلث الحماية CIA، ملفات التحقيق في الجرائم الإلكترونية، لعبة كشف التهديدات الأمنية، وأداة اختبار قوة كلمة المرور.</p>
                    <div class="features-list">
                        <span class="feature-pill">🔺 مثلث الحماية CIA</span>
                        <span class="feature-pill">🕵️ مسرح جرائم إلكترونية</span>
                        <span class="feature-pill">🔑 فاحص قوة كلمة المرور</span>
                        <span class="feature-pill">📝 اختبار 8 أسئلة</span>
                    </div>
                </div>
                <div class="card-btn btn-3">
                    <span>دخول الدرس الآن</span>
                    <i class="fas fa-arrow-left"></i>
                </div>
            </a>
        </div>
    </div>

    <footer>
        <p>جميع الحقوق محفوظة © 2026 | مادة المهارات الرقمية — <strong>أ. طارق ابوعشي</strong> — متوسطة أبها الأهلية</p>
    </footer>
</body>
</html>
"""

with open(os.path.join(deploy_dir, 'index.html'), 'w', encoding='utf-8') as f:
    f.write(portal_html)

print("Portal index.html generated successfully!")
