# -*- coding: utf-8 -*-
import codecs, re

path = r'c:\Users\Betech\Desktop\yassminePortf\index.html'
with codecs.open(path, 'r', 'utf-8') as f:
    content = f.read()

# ─────────────────────────────────────────────────────────────
# 1. Update Navbar links
# ─────────────────────────────────────────────────────────────
old_nav_desktop = """                    <a href="#about" class="hover:text-brand-raspberry dark:hover:text-brand-accentDark transition-colors hover-trigger">À Propos</a>
                    <a href="#skills" class="hover:text-brand-raspberry dark:hover:text-brand-accentDark transition-colors hover-trigger">Compétences</a>
                    <a href="#certifications" class="hover:text-brand-raspberry dark:hover:text-brand-accentDark transition-colors hover-trigger">Certifications</a>
                    <a href="#experience" class="hover:text-brand-raspberry dark:hover:text-brand-accentDark transition-colors hover-trigger">Parcours</a>
                    <a href="#projects" class="hover:text-brand-raspberry dark:hover:text-brand-accentDark transition-colors hover-trigger">Projets</a>
                    <a href="#contact" class="hover:text-brand-raspberry dark:hover:text-brand-accentDark transition-colors hover-trigger">Contact</a>"""

new_nav_desktop = """                    <a href="#about" class="hover:text-brand-raspberry dark:hover:text-brand-accentDark transition-colors hover-trigger">À Propos</a>
                    <a href="#services" class="hover:text-brand-raspberry dark:hover:text-brand-accentDark transition-colors hover-trigger">Valeur Métier</a>
                    <a href="#skills" class="hover:text-brand-raspberry dark:hover:text-brand-accentDark transition-colors hover-trigger">Compétences</a>
                    <a href="#sql-sandbox" class="hover:text-brand-raspberry dark:hover:text-brand-accentDark transition-colors hover-trigger">SQL Sandbox</a>
                    <a href="#certifications" class="hover:text-brand-raspberry dark:hover:text-brand-accentDark transition-colors hover-trigger">Certifications</a>
                    <a href="#experience" class="hover:text-brand-raspberry dark:hover:text-brand-accentDark transition-colors hover-trigger">Parcours</a>
                    <a href="#projects" class="hover:text-brand-raspberry dark:hover:text-brand-accentDark transition-colors hover-trigger">Projets</a>
                    <a href="#contact" class="hover:text-brand-raspberry dark:hover:text-brand-accentDark transition-colors hover-trigger">Contact</a>"""

content = content.replace(old_nav_desktop, new_nav_desktop)

old_nav_mobile = """                <a href="#about" class="block px-3 py-2 text-base font-medium">À Propos</a>
                <a href="#skills" class="block px-3 py-2 text-base font-medium">Compétences</a>
                <a href="#certifications" class="block px-3 py-2 text-base font-medium">Certifications</a>
                <a href="#experience" class="block px-3 py-2 text-base font-medium">Parcours</a>
                <a href="#projects" class="block px-3 py-2 text-base font-medium">Projets</a>
                <a href="#contact" class="block px-3 py-2 text-base font-medium">Contact</a>"""

new_nav_mobile = """                <a href="#about" class="block px-3 py-2 text-base font-medium">À Propos</a>
                <a href="#services" class="block px-3 py-2 text-base font-medium">Valeur Métier</a>
                <a href="#skills" class="block px-3 py-2 text-base font-medium">Compétences</a>
                <a href="#sql-sandbox" class="block px-3 py-2 text-base font-medium">SQL Sandbox</a>
                <a href="#certifications" class="block px-3 py-2 text-base font-medium">Certifications</a>
                <a href="#experience" class="block px-3 py-2 text-base font-medium">Parcours</a>
                <a href="#projects" class="block px-3 py-2 text-base font-medium">Projets</a>
                <a href="#contact" class="block px-3 py-2 text-base font-medium">Contact</a>"""

content = content.replace(old_nav_mobile, new_nav_mobile)

# ─────────────────────────────────────────────────────────────
# 2. Insert Business Value Matrix Section (before Skills)
# ─────────────────────────────────────────────────────────────
value_section = """
    <!-- VALUE PROPOSITION SECTION -->
    <section id="services" class="py-20 bg-brand-soft/30 dark:bg-[#1a0f1e] border-t-2 border-brand-textLight dark:border-brand-accentDark">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="text-center max-w-3xl mx-auto mb-16">
                <span class="inline-block px-3 py-1 rounded-full bg-brand-soft dark:bg-[#3d2440] text-brand-raspberry dark:text-brand-accentDark font-bold text-xs uppercase tracking-wider border border-brand-raspberry/30 mb-3">
                    Valeur Métier &amp; Solutions
                </span>
                <h2 class="text-4xl font-bold">
                    Ce que j'apporte à votre <span class="font-serif italic text-brand-raspberry dark:text-brand-accentDark">entreprise</span>
                </h2>
                <p class="opacity-75 mt-3 text-base md:text-lg">
                    Au-delà des lignes de code et des outils, je transforme vos problématiques métier en solutions décisionnelles fiables et directement actionnables.
                </p>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
                <!-- 1. Pilotage Stratégique -->
                <div class="neo-card p-6 flex flex-col justify-between bg-white dark:bg-[#2D1B2E] hover-trigger">
                    <div>
                        <div class="w-14 h-14 rounded-xl bg-pink-100 dark:bg-pink-950/50 border-2 border-brand-textLight dark:border-brand-accentDark flex items-center justify-center text-3xl mb-4">
                            📊
                        </div>
                        <h3 class="text-xl font-bold mb-2">Pilotage &amp; Décisionnel</h3>
                        <p class="text-sm opacity-80 leading-relaxed mb-4">
                            Définition de KPIs stratégiques et conception de tableaux de bord Power BI dynamiques pour donner une visibilité claire aux décideurs.
                        </p>
                    </div>
                    <ul class="text-xs space-y-2 opacity-90 border-t border-gray-200 dark:border-gray-700 pt-3">
                        <li class="flex items-center gap-1.5"><i class="ph-bold ph-check text-brand-raspberry"></i> Reporting automatisé</li>
                        <li class="flex items-center gap-1.5"><i class="ph-bold ph-check text-brand-raspberry"></i> Data storytelling &amp; UX</li>
                        <li class="flex items-center gap-1.5"><i class="ph-bold ph-check text-brand-raspberry"></i> Suivi du CA, marge &amp; rétention</li>
                    </ul>
                </div>

                <!-- 2. Pipelines & ETL -->
                <div class="neo-card p-6 flex flex-col justify-between bg-white dark:bg-[#2D1B2E] hover-trigger">
                    <div>
                        <div class="w-14 h-14 rounded-xl bg-purple-100 dark:bg-purple-950/50 border-2 border-brand-textLight dark:border-brand-accentDark flex items-center justify-center text-3xl mb-4">
                            ⚙️
                        </div>
                        <h3 class="text-xl font-bold mb-2">Pipelines ETL &amp; Flux</h3>
                        <p class="text-sm opacity-80 leading-relaxed mb-4">
                            Automatisation de flux d'intégration (Talend, SSIS, Python) pour extraire, nettoyer et synchroniser des données multi-sources.
                        </p>
                    </div>
                    <ul class="text-xs space-y-2 opacity-90 border-t border-gray-200 dark:border-gray-700 pt-3">
                        <li class="flex items-center gap-1.5"><i class="ph-bold ph-check text-brand-raspberry"></i> Fiabilisation &amp; Qualité de données</li>
                        <li class="flex items-center gap-1.5"><i class="ph-bold ph-check text-brand-raspberry"></i> Élimination des saisies manuelles</li>
                        <li class="flex items-center gap-1.5"><i class="ph-bold ph-check text-brand-raspberry"></i> Web scraping &amp; Connecteurs API</li>
                    </ul>
                </div>

                <!-- 3. DWH & Modélisation -->
                <div class="neo-card p-6 flex flex-col justify-between bg-white dark:bg-[#2D1B2E] hover-trigger">
                    <div>
                        <div class="w-14 h-14 rounded-xl bg-blue-100 dark:bg-blue-950/50 border-2 border-brand-textLight dark:border-brand-accentDark flex items-center justify-center text-3xl mb-4">
                            🏗️
                        </div>
                        <h3 class="text-xl font-bold mb-2">Entrepôts de Données</h3>
                        <p class="text-sm opacity-80 leading-relaxed mb-4">
                            Modélisation dimensionnelle (schémas en étoile &amp; constellation) pour structurer vos données et accélérer les requêtes analytiques.
                        </p>
                    </div>
                    <ul class="text-xs space-y-2 opacity-90 border-t border-gray-200 dark:border-gray-700 pt-3">
                        <li class="flex items-center gap-1.5"><i class="ph-bold ph-check text-brand-raspberry"></i> Architecture décisionnelle</li>
                        <li class="flex items-center gap-1.5"><i class="ph-bold ph-check text-brand-raspberry"></i> SQL Server, PostgreSQL, MySQL</li>
                        <li class="flex items-center gap-1.5"><i class="ph-bold ph-check text-brand-raspberry"></i> Optimisation des index &amp; volumétrie</li>
                    </ul>
                </div>

                <!-- 4. Data Science & IA -->
                <div class="neo-card p-6 flex flex-col justify-between bg-white dark:bg-[#2D1B2E] hover-trigger">
                    <div>
                        <div class="w-14 h-14 rounded-xl bg-amber-100 dark:bg-amber-950/50 border-2 border-brand-textLight dark:border-brand-accentDark flex items-center justify-center text-3xl mb-4">
                            🤖
                        </div>
                        <h3 class="text-xl font-bold mb-2">Analyse Prédictive &amp; IA</h3>
                        <p class="text-sm opacity-80 leading-relaxed mb-4">
                            Passer du constat à la prédiction grâce aux modèles de Machine Learning (XGBoost, Random Forest) et à l'IA générative.
                        </p>
                    </div>
                    <ul class="text-xs space-y-2 opacity-90 border-t border-gray-200 dark:border-gray-700 pt-3">
                        <li class="flex items-center gap-1.5"><i class="ph-bold ph-check text-brand-raspberry"></i> Moteurs de recommandation</li>
                        <li class="flex items-center gap-1.5"><i class="ph-bold ph-check text-brand-raspberry"></i> Classification &amp; Vision (CNN)</li>
                        <li class="flex items-center gap-1.5"><i class="ph-bold ph-check text-brand-raspberry"></i> Déploiement MLOps (Docker, MLflow)</li>
                    </ul>
                </div>
            </div>
        </div>
    </section>
"""

content = content.replace('    <!-- SKILLS SECTION -->', value_section + '\n    <!-- SKILLS SECTION -->', 1)

# ─────────────────────────────────────────────────────────────
# 3. Insert SQL Sandbox Section (between Skills and Certifications)
# ─────────────────────────────────────────────────────────────
sql_section = """
    <!-- SQL SANDBOX SECTION -->
    <section id="sql-sandbox" class="py-20 bg-white dark:bg-brand-dark border-t-2 border-brand-textLight dark:border-brand-accentDark">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="flex flex-col md:flex-row justify-between items-start md:items-end mb-10 gap-4">
                <div>
                    <span class="inline-block px-3 py-1 rounded-full bg-brand-soft dark:bg-[#3d2440] text-brand-raspberry dark:text-brand-accentDark font-bold text-xs uppercase tracking-wider border border-brand-raspberry/30 mb-2">
                        ⚡ Démonstrateur Technique
                    </span>
                    <h2 class="text-4xl font-bold">
                        SQL <span class="font-serif italic text-brand-raspberry dark:text-brand-accentDark">Sandbox</span>
                    </h2>
                    <p class="text-sm opacity-70 mt-1">
                        Testez en direct des requêtes SQL analytiques avancées répondant à des problématiques métier concrètes.
                    </p>
                </div>
                <div class="text-xs font-mono px-3 py-1.5 rounded-lg border border-brand-textLight dark:border-brand-accentDark bg-brand-soft/40 dark:bg-[#3d2440] flex items-center gap-2">
                    <span class="inline-block w-2.5 h-2.5 rounded-full bg-green-500 animate-pulse"></span>
                    <span class="font-semibold">Moteur SQL Virtuel Actif</span>
                </div>
            </div>

            <!-- Case selector buttons -->
            <div class="flex gap-2 flex-wrap mb-6" id="sql-cases">
                <button class="sql-case-btn neo-btn px-4 py-2 rounded-lg text-xs font-bold bg-brand-raspberry text-white hover-trigger transition-all" data-case="1">
                    🎯 Cas 1 : Top Clients &amp; Contribution au CA (Window Functions)
                </button>
                <button class="sql-case-btn neo-btn px-4 py-2 rounded-lg text-xs font-bold bg-white dark:bg-brand-textLight text-brand-textLight dark:text-brand-accentDark hover-trigger transition-all" data-case="2">
                    🔄 Cas 2 : Cohortes &amp; Taux de Churn Mensuel (CTE)
                </button>
                <button class="sql-case-btn neo-btn px-4 py-2 rounded-lg text-xs font-bold bg-white dark:bg-brand-textLight text-brand-textLight dark:text-brand-accentDark hover-trigger transition-all" data-case="3">
                    ⚠️ Cas 3 : Détection d'Anomalies de Ventes (HAVING &amp; Sous-requête)
                </button>
            </div>

            <!-- IDE Terminal Box -->
            <div class="neo-card overflow-hidden bg-[#1E1220] text-white border-2 border-brand-textLight dark:border-brand-accentDark shadow-neo dark:shadow-neo-dark">
                <!-- Terminal Header -->
                <div class="flex justify-between items-center px-4 py-3 bg-[#150a17] border-b border-gray-700">
                    <div class="flex items-center gap-2">
                        <span class="w-3 h-3 rounded-full bg-red-500 inline-block"></span>
                        <span class="w-3 h-3 rounded-full bg-yellow-500 inline-block"></span>
                        <span class="w-3 h-3 rounded-full bg-green-500 inline-block"></span>
                        <span class="text-xs font-mono text-gray-400 ml-2" id="sql-filename">top_customers_window.sql</span>
                    </div>
                    <button id="copy-sql-btn" class="text-xs flex items-center gap-1.5 px-3 py-1.5 rounded bg-[#2D1B2E] hover:bg-brand-raspberry transition-colors text-white font-mono border border-gray-700 hover:border-brand-raspberry">
                        <i class="ph-bold ph-copy"></i> Copier la requête
                    </button>
                </div>

                <!-- Query Code View -->
                <div class="p-6 font-mono text-xs md:text-sm overflow-x-auto leading-relaxed border-b border-gray-800 bg-[#1A0E1C]" id="sql-code-display">
                    <!-- Dynamic SQL Content -->
                </div>

                <!-- Result Preview Header -->
                <div class="px-6 py-2.5 bg-[#150a17] border-b border-gray-800 flex justify-between items-center text-xs font-mono text-gray-300">
                    <span class="flex items-center gap-2">
                        <i class="ph-bold ph-table text-brand-accentDark"></i> Résultat simulé de la requête (Table View)
                    </span>
                    <span class="text-green-400 font-semibold" id="sql-rows-info">● 4 lignes retournées (0.014s)</span>
                </div>

                <!-- Result Table -->
                <div class="p-4 overflow-x-auto bg-[#1E1220]" id="sql-table-display">
                    <!-- Dynamic Table Content -->
                </div>
            </div>
        </div>
    </section>
"""

content = content.replace('    <!-- CERTIFICATIONS SECTION -->', sql_section + '\n    <!-- CERTIFICATIONS SECTION -->', 1)

# ─────────────────────────────────────────────────────────────
# 4. Update Projects Header with Instant Search & Filters
# ─────────────────────────────────────────────────────────────
old_projects_header = """            <div class="flex flex-col md:flex-row justify-between items-end mb-12 gap-4">
                <h2 class="text-4xl font-bold">
                    Mes <span class="font-serif italic text-brand-raspberry dark:text-brand-accentDark">Projets</span>
                </h2>
                <!-- Filters -->
                <div class="flex gap-2 flex-wrap" id="project-filters">
                    <button class="neo-btn px-4 py-1 rounded-full text-sm bg-brand-textLight text-white dark:bg-brand-accentDark dark:text-brand-textLight" data-filter="all">Tous</button>
                    <button class="neo-btn px-4 py-1 rounded-full text-sm bg-white dark:bg-brand-textLight text-brand-textLight dark:text-brand-accentDark" data-filter="bi">BI & ETL</button>
                    <button class="neo-btn px-4 py-1 rounded-full text-sm bg-white dark:bg-brand-textLight text-brand-textLight dark:text-brand-accentDark" data-filter="ml">ML & IA</button>
                    <button class="neo-btn px-4 py-1 rounded-full text-sm bg-white dark:bg-brand-textLight text-brand-textLight dark:text-brand-accentDark" data-filter="dev">Dev</button>
                </div>
            </div>"""

new_projects_header = """            <div class="flex flex-col lg:flex-row justify-between items-start lg:items-end mb-8 gap-4">
                <div>
                    <h2 class="text-4xl font-bold">
                        Mes <span class="font-serif italic text-brand-raspberry dark:text-brand-accentDark">Projets</span>
                    </h2>
                    <p class="text-sm opacity-70 mt-1" id="project-count-text">21 projets interactifs avec présentations Canva intégrées</p>
                </div>
                
                <div class="flex flex-col sm:flex-row gap-3 w-full lg:w-auto items-stretch sm:items-center">
                    <!-- Barre de recherche instantanée -->
                    <div class="relative flex-grow sm:w-72">
                        <i class="ph-bold ph-magnifying-glass absolute left-3 top-1/2 -translate-y-1/2 text-gray-400"></i>
                        <input type="text" id="project-search" placeholder="Rechercher (ex: Python, SQL, Power BI...)" 
                               class="w-full pl-9 pr-8 py-2 text-xs md:text-sm border-2 border-brand-textLight dark:border-brand-accentDark rounded-full bg-white dark:bg-brand-dark focus:outline-none focus:ring-2 focus:ring-brand-raspberry">
                        <button id="clear-search" class="absolute right-3 top-1/2 -translate-y-1/2 text-gray-400 hover:text-brand-raspberry hidden" title="Effacer">
                            <i class="ph-bold ph-x"></i>
                        </button>
                    </div>

                    <!-- Filters -->
                    <div class="flex gap-1.5 flex-wrap" id="project-filters">
                        <button class="filter-btn neo-btn px-3 py-1.5 rounded-full text-xs font-bold bg-brand-textLight text-white dark:bg-brand-accentDark dark:text-brand-textLight" data-filter="all">Tous (21)</button>
                        <button class="filter-btn neo-btn px-3 py-1.5 rounded-full text-xs font-bold bg-white dark:bg-brand-textLight text-brand-textLight dark:text-brand-accentDark" data-filter="bi">BI &amp; ETL</button>
                        <button class="filter-btn neo-btn px-3 py-1.5 rounded-full text-xs font-bold bg-white dark:bg-brand-textLight text-brand-textLight dark:text-brand-accentDark" data-filter="ml">ML &amp; IA</button>
                        <button class="filter-btn neo-btn px-3 py-1.5 rounded-full text-xs font-bold bg-white dark:bg-brand-textLight text-brand-textLight dark:text-brand-accentDark" data-filter="dev">Dev</button>
                    </div>
                </div>
            </div>

            <!-- Message aucun résultat -->
            <div id="no-projects-msg" class="hidden text-center py-12 neo-card bg-white dark:bg-brand-dark max-w-md mx-auto mb-8">
                <span class="text-4xl block mb-2">🔍</span>
                <h3 class="font-bold text-lg">Aucun projet trouvé</h3>
                <p class="text-xs opacity-70 mt-1">Essayez un autre mot-clé (ex: Python, SQL, Talend, Power BI, Docker...)</p>
            </div>"""

content = content.replace(old_projects_header, new_projects_header)

# ─────────────────────────────────────────────────────────────
# 5. Replace Projects Filter Script with Combined Search + Filter + SQL Sandbox Script
# ─────────────────────────────────────────────────────────────
old_filter_script_pattern = re.compile(
    r'// Projects Filter\s*const filters = document\.querySelectorAll\(\'#project-filters button\'\);.*?// Modals',
    re.DOTALL
)

new_scripts = """// ─── SEARCH & FILTER PROJETS ──────────────────────────────
        const projectSearchInput = document.getElementById('project-search');
        const clearSearchBtn = document.getElementById('clear-search');
        const projectFilters = document.querySelectorAll('#project-filters button');
        const projectItems = document.querySelectorAll('.project-item');
        const projectCountText = document.getElementById('project-count-text');
        const noProjectsMsg = document.getElementById('no-projects-msg');

        let activeCategory = 'all';
        let searchQuery = '';

        function updateProjectVisibility() {
            let visibleCount = 0;
            const query = searchQuery.trim().toLowerCase();

            projectItems.forEach(p => {
                const category = p.getAttribute('data-category') || '';
                const title = (p.querySelector('h3')?.textContent || '').toLowerCase();
                const desc = (p.querySelector('p')?.textContent || '').toLowerCase();
                const tags = Array.from(p.querySelectorAll('.text-brand-raspberry')).map(t => t.textContent.toLowerCase()).join(' ');
                const textContent = `${title} ${desc} ${tags}`;

                const matchesCat = (activeCategory === 'all' || category === activeCategory);
                const matchesSearch = (!query || textContent.includes(query));

                if (matchesCat && matchesSearch) {
                    p.style.display = 'flex';
                    visibleCount++;
                } else {
                    p.style.display = 'none';
                }
            });

            if (projectCountText) {
                projectCountText.textContent = `${visibleCount} projet${visibleCount > 1 ? 's' : ''} affiché${visibleCount > 1 ? 's' : ''}`;
            }

            if (noProjectsMsg) {
                noProjectsMsg.classList.toggle('hidden', visibleCount > 0);
            }
        }

        // Filter button click
        projectFilters.forEach(btn => {
            btn.addEventListener('click', () => {
                projectFilters.forEach(b => {
                    b.classList.remove('bg-brand-textLight', 'text-white', 'dark:bg-brand-accentDark', 'dark:text-brand-textLight');
                    b.classList.add('bg-white', 'text-brand-textLight');
                });
                btn.classList.remove('bg-white', 'text-brand-textLight');
                btn.classList.add('bg-brand-textLight', 'text-white', 'dark:bg-brand-accentDark', 'dark:text-brand-textLight');

                activeCategory = btn.getAttribute('data-filter') || 'all';
                updateProjectVisibility();
            });
        });

        // Search input
        if (projectSearchInput) {
            projectSearchInput.addEventListener('input', (e) => {
                searchQuery = e.target.value;
                if (clearSearchBtn) {
                    clearSearchBtn.classList.toggle('hidden', !searchQuery);
                }
                updateProjectVisibility();
            });
        }

        if (clearSearchBtn) {
            clearSearchBtn.addEventListener('click', () => {
                projectSearchInput.value = '';
                searchQuery = '';
                clearSearchBtn.classList.add('hidden');
                updateProjectVisibility();
            });
        }

        // ─── SQL SANDBOX DATA & LOGIC ────────────────────────────
        const sqlCasesData = {
            1: {
                filename: 'top_customers_window.sql',
                info: '● 4 lignes retournées (0.014s)',
                code: `<span class="text-pink-400">WITH</span> CustomerTotals <span class="text-pink-400">AS</span> (
    <span class="text-pink-400">SELECT</span> 
        c.customer_id,
        c.customer_name,
        c.country,
        <span class="text-blue-400">SUM</span>(o.total_amount) <span class="text-pink-400">AS</span> total_revenue,
        <span class="text-blue-400">COUNT</span>(o.order_id) <span class="text-pink-400">AS</span> total_orders
    <span class="text-pink-400">FROM</span> dim_customers c
    <span class="text-pink-400">JOIN</span> fact_sales o <span class="text-pink-400">ON</span> c.customer_id = o.customer_id
    <span class="text-pink-400">WHERE</span> o.order_date >= <span class="text-yellow-300">'2025-01-01'</span>
    <span class="text-pink-400">GROUP BY</span> c.customer_id, c.customer_name, c.country
)
<span class="text-pink-400">SELECT</span> 
    customer_name,
    country,
    total_revenue,
    <span class="text-blue-400">ROUND</span>(total_revenue * <span class="text-yellow-300">100.0</span> / <span class="text-blue-400">SUM</span>(total_revenue) <span class="text-pink-400">OVER</span>(), <span class="text-yellow-300">2</span>) <span class="text-pink-400">AS</span> revenue_share_pct,
    <span class="text-blue-400">DENSE_RANK</span>() <span class="text-pink-400">OVER</span> (<span class="text-pink-400">ORDER BY</span> total_revenue <span class="text-pink-400">DESC</span>) <span class="text-pink-400">AS</span> rank_position
<span class="text-pink-400">FROM</span> CustomerTotals
<span class="text-pink-400">ORDER BY</span> rank_position
<span class="text-pink-400">LIMIT</span> <span class="text-yellow-300">4</span>;`,
                rawQuery: `WITH CustomerTotals AS (
    SELECT 
        c.customer_id, c.customer_name, c.country,
        SUM(o.total_amount) AS total_revenue,
        COUNT(o.order_id) AS total_orders
    FROM dim_customers c
    JOIN fact_sales o ON c.customer_id = o.customer_id
    WHERE o.order_date >= '2025-01-01'
    GROUP BY c.customer_id, c.customer_name, c.country
)
SELECT 
    customer_name, country, total_revenue,
    ROUND(total_revenue * 100.0 / SUM(total_revenue) OVER(), 2) AS revenue_share_pct,
    DENSE_RANK() OVER (ORDER BY total_revenue DESC) AS rank_position
FROM CustomerTotals
ORDER BY rank_position
LIMIT 4;`,
                table: `<table class="w-full text-left font-mono text-xs">
                    <thead>
                        <tr class="border-b border-gray-700 text-gray-400">
                            <th class="py-2 px-3">Rank</th>
                            <th class="py-2 px-3">Client</th>
                            <th class="py-2 px-3">Pays</th>
                            <th class="py-2 px-3 text-right">CA Total</th>
                            <th class="py-2 px-3 text-right">Part du CA</th>
                        </tr>
                    </thead>
                    <tbody class="divide-y divide-gray-800">
                        <tr class="hover:bg-white/5">
                            <td class="py-2 px-3 font-bold text-brand-accentDark">#1</td>
                            <td class="py-2 px-3 font-semibold text-white">TechnoCorp S.A.</td>
                            <td class="py-2 px-3 text-gray-300">France</td>
                            <td class="py-2 px-3 text-right font-bold text-green-400">142,500 DT</td>
                            <td class="py-2 px-3 text-right text-gray-300">24.5 %</td>
                        </tr>
                        <tr class="hover:bg-white/5">
                            <td class="py-2 px-3 font-bold text-brand-accentDark">#2</td>
                            <td class="py-2 px-3 font-semibold text-white">Atlas Retail</td>
                            <td class="py-2 px-3 text-gray-300">Tunisie</td>
                            <td class="py-2 px-3 text-right font-bold text-green-400">118,200 DT</td>
                            <td class="py-2 px-3 text-right text-gray-300">20.3 %</td>
                        </tr>
                        <tr class="hover:bg-white/5">
                            <td class="py-2 px-3 font-bold text-brand-accentDark">#3</td>
                            <td class="py-2 px-3 font-semibold text-white">Global Distribution</td>
                            <td class="py-2 px-3 text-gray-300">Allemagne</td>
                            <td class="py-2 px-3 text-right font-bold text-green-400">95,800 DT</td>
                            <td class="py-2 px-3 text-right text-gray-300">16.5 %</td>
                        </tr>
                        <tr class="hover:bg-white/5">
                            <td class="py-2 px-3 font-bold text-brand-accentDark">#4</td>
                            <td class="py-2 px-3 font-semibold text-white">MedLogistics</td>
                            <td class="py-2 px-3 text-gray-300">Italie</td>
                            <td class="py-2 px-3 text-right font-bold text-green-400">72,400 DT</td>
                            <td class="py-2 px-3 text-right text-gray-300">12.4 %</td>
                        </tr>
                    </tbody>
                </table>`
            },
            2: {
                filename: 'cohort_churn_analysis.sql',
                info: '● 4 cohortes analysées (0.021s)',
                code: `<span class="text-pink-400">WITH</span> MonthlyActivity <span class="text-pink-400">AS</span> (
    <span class="text-pink-400">SELECT</span> 
        user_id,
        <span class="text-blue-400">DATE_TRUNC</span>(<span class="text-yellow-300">'month'</span>, login_date) <span class="text-pink-400">AS</span> activity_month,
        <span class="text-blue-400">MIN</span>(<span class="text-blue-400">DATE_TRUNC</span>(<span class="text-yellow-300">'month'</span>, login_date)) <span class="text-pink-400">OVER</span> (<span class="text-pink-400">PARTITION BY</span> user_id) <span class="text-pink-400">AS</span> cohort_month
    <span class="text-pink-400">FROM</span> fact_user_logins
)
<span class="text-pink-400">SELECT</span> 
    <span class="text-blue-400">TO_CHAR</span>(cohort_month, <span class="text-yellow-300">'YYYY-MM'</span>) <span class="text-pink-400">AS</span> cohort,
    <span class="text-blue-400">COUNT</span>(<span class="text-pink-400">DISTINCT</span> user_id) <span class="text-pink-400">AS</span> cohort_size,
    <span class="text-blue-400">ROUND</span>(<span class="text-blue-400">COUNT</span>(<span class="text-pink-400">DISTINCT CASE WHEN</span> activity_month = cohort_month + <span class="text-pink-400">INTERVAL</span> <span class="text-yellow-300">'1 month'</span> <span class="text-pink-400">THEN</span> user_id <span class="text-pink-400">END</span>) * <span class="text-yellow-300">100.0</span> / <span class="text-blue-400">COUNT</span>(<span class="text-pink-400">DISTINCT</span> user_id), <span class="text-yellow-300">1</span>) <span class="text-pink-400">AS</span> retention_m1_pct,
    <span class="text-blue-400">ROUND</span>(<span class="text-yellow-300">100.0</span> - (<span class="text-blue-400">COUNT</span>(<span class="text-pink-400">DISTINCT CASE WHEN</span> activity_month = cohort_month + <span class="text-pink-400">INTERVAL</span> <span class="text-yellow-300">'1 month'</span> <span class="text-pink-400">THEN</span> user_id <span class="text-pink-400">END</span>) * <span class="text-yellow-300">100.0</span> / <span class="text-blue-400">COUNT</span>(<span class="text-pink-400">DISTINCT</span> user_id)), <span class="text-yellow-300">1</span>) <span class="text-pink-400">AS</span> churn_m1_pct
<span class="text-pink-400">FROM</span> MonthlyActivity
<span class="text-pink-400">GROUP BY</span> cohort_month
<span class="text-pink-400">ORDER BY</span> cohort_month <span class="text-pink-400">DESC</span>
<span class="text-pink-400">LIMIT</span> <span class="text-yellow-300">4</span>;`,
                rawQuery: `WITH MonthlyActivity AS (
    SELECT 
        user_id,
        DATE_TRUNC('month', login_date) AS activity_month,
        MIN(DATE_TRUNC('month', login_date)) OVER (PARTITION BY user_id) AS cohort_month
    FROM fact_user_logins
)
SELECT 
    TO_CHAR(cohort_month, 'YYYY-MM') AS cohort,
    COUNT(DISTINCT user_id) AS cohort_size,
    ROUND(COUNT(DISTINCT CASE WHEN activity_month = cohort_month + INTERVAL '1 month' THEN user_id END) * 100.0 / COUNT(DISTINCT user_id), 1) AS retention_m1_pct,
    ROUND(100.0 - (COUNT(DISTINCT CASE WHEN activity_month = cohort_month + INTERVAL '1 month' THEN user_id END) * 100.0 / COUNT(DISTINCT user_id)), 1) AS churn_m1_pct
FROM MonthlyActivity
GROUP BY cohort_month
ORDER BY cohort_month DESC
LIMIT 4;`,
                table: `<table class="w-full text-left font-mono text-xs">
                    <thead>
                        <tr class="border-b border-gray-700 text-gray-400">
                            <th class="py-2 px-3">Cohorte</th>
                            <th class="py-2 px-3">Inscrits</th>
                            <th class="py-2 px-3 text-right">Rétention M+1</th>
                            <th class="py-2 px-3 text-right">Taux de Churn M+1</th>
                            <th class="py-2 px-3 text-center">Statut Santé</th>
                        </tr>
                    </thead>
                    <tbody class="divide-y divide-gray-800">
                        <tr class="hover:bg-white/5">
                            <td class="py-2 px-3 font-semibold text-white">2025-09</td>
                            <td class="py-2 px-3 text-gray-300">1,240 utilisateurs</td>
                            <td class="py-2 px-3 text-right font-bold text-green-400">82.4 %</td>
                            <td class="py-2 px-3 text-right text-yellow-300">17.6 %</td>
                            <td class="py-2 px-3 text-center"><span class="px-2 py-0.5 rounded text-[10px] bg-green-900/50 text-green-300">Excellent</span></td>
                        </tr>
                        <tr class="hover:bg-white/5">
                            <td class="py-2 px-3 font-semibold text-white">2025-08</td>
                            <td class="py-2 px-3 text-gray-300">1,150 utilisateurs</td>
                            <td class="py-2 px-3 text-right font-bold text-green-400">79.1 %</td>
                            <td class="py-2 px-3 text-right text-yellow-300">20.9 %</td>
                            <td class="py-2 px-3 text-center"><span class="px-2 py-0.5 rounded text-[10px] bg-green-900/50 text-green-300">Stable</span></td>
                        </tr>
                        <tr class="hover:bg-white/5">
                            <td class="py-2 px-3 font-semibold text-white">2025-07</td>
                            <td class="py-2 px-3 text-gray-300">980 utilisateurs</td>
                            <td class="py-2 px-3 text-right font-bold text-green-400">76.8 %</td>
                            <td class="py-2 px-3 text-right text-yellow-300">23.2 %</td>
                            <td class="py-2 px-3 text-center"><span class="px-2 py-0.5 rounded text-[10px] bg-green-900/50 text-green-300">Stable</span></td>
                        </tr>
                        <tr class="hover:bg-white/5">
                            <td class="py-2 px-3 font-semibold text-white">2025-06</td>
                            <td class="py-2 px-3 text-gray-300">850 utilisateurs</td>
                            <td class="py-2 px-3 text-right font-bold text-yellow-300">71.2 %</td>
                            <td class="py-2 px-3 text-right text-red-400">28.8 %</td>
                            <td class="py-2 px-3 text-center"><span class="px-2 py-0.5 rounded text-[10px] bg-yellow-900/50 text-yellow-300">Alerte</span></td>
                        </tr>
                    </tbody>
                </table>`
            },
            3: {
                filename: 'negative_margin_alerts.sql',
                info: '● 3 anomalies détectées (0.009s)',
                code: `<span class="text-pink-400">SELECT</span> 
    p.product_id,
    p.product_name,
    p.category,
    <span class="text-blue-400">SUM</span>(s.quantity) <span class="text-pink-400">AS</span> total_units_sold,
    <span class="text-blue-400">ROUND</span>(<span class="text-blue-400">SUM</span>(s.revenue), <span class="text-yellow-300">2</span>) <span class="text-pink-400">AS</span> total_revenue,
    <span class="text-blue-400">ROUND</span>(<span class="text-blue-400">SUM</span>(s.revenue - (p.cost_price * s.quantity)), <span class="text-yellow-300">2</span>) <span class="text-pink-400">AS</span> net_margin,
    <span class="text-blue-400">ROUND</span>(<span class="text-blue-400">SUM</span>(s.revenue - (p.cost_price * s.quantity)) * <span class="text-yellow-300">100.0</span> / <span class="text-blue-400">NULLIF</span>(<span class="text-blue-400">SUM</span>(s.revenue), <span class="text-yellow-300">0</span>), <span class="text-yellow-300">1</span>) <span class="text-pink-400">AS</span> margin_pct
<span class="text-pink-400">FROM</span> dim_products p
<span class="text-pink-400">JOIN</span> fact_sales s <span class="text-pink-400">ON</span> p.product_id = s.product_id
<span class="text-pink-400">GROUP BY</span> p.product_id, p.product_name, p.category
<span class="text-pink-400">HAVING</span> <span class="text-blue-400">SUM</span>(s.revenue - (p.cost_price * s.quantity)) < <span class="text-yellow-300">0</span>
<span class="text-pink-400">ORDER BY</span> net_margin <span class="text-pink-400">ASC</span>;`,
                rawQuery: `SELECT 
    p.product_id,
    p.product_name,
    p.category,
    SUM(s.quantity) AS total_units_sold,
    ROUND(SUM(s.revenue), 2) AS total_revenue,
    ROUND(SUM(s.revenue - (p.cost_price * s.quantity)), 2) AS net_margin,
    ROUND(SUM(s.revenue - (p.cost_price * s.quantity)) * 100.0 / NULLIF(SUM(s.revenue), 0), 1) AS margin_pct
FROM dim_products p
JOIN fact_sales s ON p.product_id = s.product_id
GROUP BY p.product_id, p.product_name, p.category
HAVING SUM(s.revenue - (p.cost_price * s.quantity)) < 0
ORDER BY net_margin ASC;`,
                table: `<table class="w-full text-left font-mono text-xs">
                    <thead>
                        <tr class="border-b border-gray-700 text-gray-400">
                            <th class="py-2 px-3">Produit</th>
                            <th class="py-2 px-3">Catégorie</th>
                            <th class="py-2 px-3 text-right">Unités</th>
                            <th class="py-2 px-3 text-right">CA</th>
                            <th class="py-2 px-3 text-right">Marge Nette</th>
                            <th class="py-2 px-3 text-center">Diagnostic</th>
                        </tr>
                    </thead>
                    <tbody class="divide-y divide-gray-800">
                        <tr class="hover:bg-white/5">
                            <td class="py-2 px-3 font-semibold text-white">Smart Watch V3 (Promo)</td>
                            <td class="py-2 px-3 text-gray-300">Électronique</td>
                            <td class="py-2 px-3 text-right">450</td>
                            <td class="py-2 px-3 text-right">31,500 DT</td>
                            <td class="py-2 px-3 text-right font-bold text-red-400">-4,200 DT (-13.3%)</td>
                            <td class="py-2 px-3 text-center"><span class="px-2 py-0.5 rounded text-[10px] bg-red-900/60 text-red-300">Remise excessive</span></td>
                        </tr>
                        <tr class="hover:bg-white/5">
                            <td class="py-2 px-3 font-semibold text-white">Casque Bluetooth ANC</td>
                            <td class="py-2 px-3 text-gray-300">Accessoires</td>
                            <td class="py-2 px-3 text-right">280</td>
                            <td class="py-2 px-3 text-right">18,200 DT</td>
                            <td class="py-2 px-3 text-right font-bold text-red-400">-1,850 DT (-10.1%)</td>
                            <td class="py-2 px-3 text-center"><span class="px-2 py-0.5 rounded text-[10px] bg-red-900/60 text-red-300">Hausse coût logistique</span></td>
                        </tr>
                        <tr class="hover:bg-white/5">
                            <td class="py-2 px-3 font-semibold text-white">Support Ergonomique</td>
                            <td class="py-2 px-3 text-gray-300">Bureau</td>
                            <td class="py-2 px-3 text-right">190</td>
                            <td class="py-2 px-3 text-right">7,600 DT</td>
                            <td class="py-2 px-3 text-right font-bold text-red-400">-640 DT (-8.4%)</td>
                            <td class="py-2 px-3 text-center"><span class="px-2 py-0.5 rounded text-[10px] bg-yellow-900/60 text-yellow-300">Erreur prix catalogue</span></td>
                        </tr>
                    </tbody>
                </table>`
            }
        };

        let currentSqlCase = 1;
        const sqlFilename = document.getElementById('sql-filename');
        const sqlCodeDisplay = document.getElementById('sql-code-display');
        const sqlTableDisplay = document.getElementById('sql-table-display');
        const sqlRowsInfo = document.getElementById('sql-rows-info');
        const sqlCaseBtns = document.querySelectorAll('.sql-case-btn');
        const copySqlBtn = document.getElementById('copy-sql-btn');

        function renderSqlCase(num) {
            const data = sqlCasesData[num];
            if (!data) return;
            currentSqlCase = num;

            if (sqlFilename) sqlFilename.textContent = data.filename;
            if (sqlRowsInfo) sqlRowsInfo.textContent = data.info;
            if (sqlCodeDisplay) sqlCodeDisplay.innerHTML = `<pre class="whitespace-pre-wrap">${data.code}</pre>`;
            if (sqlTableDisplay) sqlTableDisplay.innerHTML = data.table;

            sqlCaseBtns.forEach(btn => {
                const c = parseInt(btn.getAttribute('data-case'));
                if (c === num) {
                    btn.classList.remove('bg-white', 'text-brand-textLight', 'dark:bg-brand-textLight');
                    btn.classList.add('bg-brand-raspberry', 'text-white');
                } else {
                    btn.classList.remove('bg-brand-raspberry', 'text-white');
                    btn.classList.add('bg-white', 'text-brand-textLight');
                    if (document.documentElement.classList.contains('dark')) {
                        btn.classList.add('dark:bg-brand-textLight');
                    }
                }
            });
        }

        sqlCaseBtns.forEach(btn => {
            btn.addEventListener('click', () => {
                const num = parseInt(btn.getAttribute('data-case'));
                renderSqlCase(num);
            });
        });

        if (copySqlBtn) {
            copySqlBtn.addEventListener('click', () => {
                const data = sqlCasesData[currentSqlCase];
                if (data && data.rawQuery) {
                    navigator.clipboard.writeText(data.rawQuery).then(() => {
                        const originalHTML = copySqlBtn.innerHTML;
                        copySqlBtn.innerHTML = '<i class="ph-bold ph-check text-green-400"></i> Copié !';
                        setTimeout(() => {
                            copySqlBtn.innerHTML = originalHTML;
                        }, 2000);
                    });
                }
            });
        }

        // Initial render
        renderSqlCase(1);

        // Modals"""

content = old_filter_script_pattern.sub(new_scripts, content)

with codecs.open(path, 'w', 'utf-8') as f:
    f.write(content)

print("Innovations added successfully!")
