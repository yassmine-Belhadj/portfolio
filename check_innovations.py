import os

with open(r'c:\Users\Betech\Desktop\yassminePortf\index.html', 'r', encoding='utf-8') as f:
    text = f.read()

checks = [
    ('Skills section', 'id="skills"' in text),
    ('Devicon link', 'devicon.min.css' in text),
    ('Skills cards grid', 'id="skills-grid"' in text),
    ('Filter domain buttons', 'filterSkillDomain' in text),
    ('Filter projects by skill', 'filterProjectsBySkill' in text),
    ('Project search input', 'id="project-search"' in text),
    ('Search logic', 'updateProjectVisibility' in text),
    ('CV Modal in HTML', 'id="modal-cv"' in text),
    ('Schema.org JSON-LD', 'schema.org' in text),
    ('CV File 1 (Data Analyst PDF)', os.path.exists(r'c:\Users\Betech\Desktop\yassminePortf\CV_Yassmine_Belhadj_Data_Analyst.pdf')),
    ('CV File 2 (Ingenieure BI PDF)', os.path.exists(r'c:\Users\Betech\Desktop\yassminePortf\CV_Yassmine_Belhadj_Ingenieure_BI.pdf')),
    ('CV File Default (PDF)', os.path.exists(r'c:\Users\Betech\Desktop\yassminePortf\CV_Yassmine_Belhadj.pdf')),
]

for name, ok in checks:
    print(name, ':', 'OK' if ok else 'FAIL')
