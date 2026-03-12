import os

def update_file(filename, replacements):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    for old, new in replacements:
        content = content.replace(old, new)
        
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

# INDEX.HTML Replacements
index_html_replacements = [
    ('<html lang="en" class="dark">', '<html lang="en">'),
    ("surface: '#1e293b', // slate-800", "surface: '#ffffff', // white"),
    ("bgmain: '#0f172a', // slate-900", "bgmain: '#f8fafc', // slate-50"),
    ("bordercolor: '#334155', // slate-700", "bordercolor: '#e2e8f0', // slate-200"),
    ("textmain: '#f8fafc', // slate-50", "textmain: '#0f172a', // slate-900"),
    ("textmuted: '#94a3b8' // slate-400", "textmuted: '#64748b' // slate-500"),
    
    # Sidebar
    ("text-xl font-bold tracking-tight text-white", "text-xl font-bold tracking-tight text-slate-900"),
    ("text-slate-300 hover:bg-slate-800 hover:text-white", "text-slate-600 hover:bg-slate-100 hover:text-brand-600"),
    
    # Navbar
    ('<h1 class="text-2xl font-bold text-white"', '<h1 class="text-2xl font-bold text-slate-900"'),
    ('text-slate-400">\n                <button class="hover:text-white', 'text-slate-500">\n                <button class="hover:text-brand-600'),
    ('</button>\n                <button class="hover:text-white', '</button>\n                <button class="hover:text-brand-600'),
    
    # Toast
    ('bg-slate-800 text-white', 'bg-white text-slate-800 border border-slate-200'),
    
    # Dashboard Camera
    ('<h2 class="text-xl font-bold text-white">Live Attendance Scanning</h2>', '<h2 class="text-xl font-bold text-slate-900">Live Attendance Scanning</h2>'),
    ('<p class="text-sm text-slate-400 mt-1">Ensure', '<p class="text-sm text-slate-500 mt-1">Ensure'),
    ('bg-emerald-900/40 text-emerald-400 border border-emerald-800/50', 'bg-emerald-50 text-emerald-700 border border-emerald-200'),
    # Stats
    ("bg-indigo-900/30 flex items-center justify-center text-indigo-400 text-2xl border border-indigo-800/50", "bg-indigo-50 flex items-center justify-center text-indigo-600 text-2xl border border-indigo-200"),
    ("text-xs font-bold text-slate-400 uppercase tracking-wider", "text-xs font-bold text-slate-500 uppercase tracking-wider"),
    ('<p class="text-3xl font-black text-white mt-1 leading-none"', '<p class="text-3xl font-black text-slate-900 mt-1 leading-none"'),
    ("bg-emerald-900/30 flex items-center justify-center text-emerald-400 text-2xl border border-emerald-800/50", "bg-emerald-50 flex items-center justify-center text-emerald-600 text-2xl border border-emerald-200"),
    ('<p class="text-xl font-bold text-emerald-400 mt-1 leading-none">Online</p>', '<p class="text-xl font-bold text-emerald-600 mt-1 leading-none">Online</p>'),
    
    # Logs Right Column
    ("bg-slate-800/50 rounded-t-2xl", "bg-slate-50 rounded-t-2xl"),
    ("font-bold text-white flex items-center gap-2", "font-bold text-slate-900 flex items-center gap-2"),
    ("text-slate-400 hover:text-white transition-colors bg-slate-700 p-1.5 rounded-lg border border-slate-600 hover:bg-slate-600", "text-slate-500 hover:text-brand-600 transition-colors bg-white p-1.5 rounded-lg border border-slate-200 hover:bg-slate-50"),
    
    # Register View
    ("text-xl font-bold text-white flex items-center", "text-xl font-bold text-slate-900 flex items-center"),
    ('<p class="text-sm text-slate-400 mt-1">Register a new', '<p class="text-sm text-slate-500 mt-1">Register a new'),
    ("text-sm font-semibold text-slate-300", "text-sm font-semibold text-slate-700"),
    ("border border-slate-600 bg-slate-800 text-white placeholder-slate-500 focus:bg-slate-700 focus:outline-none focus:ring-2 focus:ring-brand-500/50 focus:border-brand-500", "border border-slate-300 bg-white text-slate-900 placeholder-slate-400 focus:bg-white focus:outline-none focus:ring-2 focus:ring-brand-500/50 focus:border-brand-500"),
    
    ('<h4 class="font-bold text-white text-lg">', '<h4 class="font-bold text-slate-900 text-lg">'),
    ('text-slate-300 text-sm font-medium', 'text-slate-600 text-sm font-medium'),
    ("bg-brand-900/30 border border-brand-800/50", "bg-brand-50 border border-brand-200"),
    ('text-brand-200 leading-relaxed', 'text-brand-800 leading-relaxed'),
    ('id="capture-count"\n                                        class="text-white"', 'id="capture-count"\n                                        class="text-brand-900"'),
    ("w-full bg-slate-700 h-2", "w-full bg-slate-200 h-2"),
    ("bg-white hover:bg-slate-200 text-slate-900", "bg-brand-600 hover:bg-brand-700 text-white"),
    
    # Manage View
    ('<h2 class="text-2xl font-bold text-white">Manage Students</h2>', '<h2 class="text-2xl font-bold text-slate-900">Manage Students</h2>'),
    ('<p class="text-slate-400 mt-1">Edit profiles', '<p class="text-slate-500 mt-1">Edit profiles'),
    ("text-slate-300 hover:bg-slate-700 hover:text-white", "text-slate-600 hover:bg-slate-100 hover:text-brand-600"),
    ("bg-slate-800/50 border-b border-bordercolor", "bg-slate-50 border-b border-bordercolor"),
    
    # JS Block inside HTML for Nav active states
    ("b.classList.remove('bg-brand-900/30', 'text-brand-400', 'font-bold', 'border', 'border-brand-800/50');", "b.classList.remove('bg-brand-50', 'text-brand-700', 'font-bold', 'border', 'border-brand-200');"),
    ("b.classList.add('text-slate-300', 'font-medium');", "b.classList.add('text-slate-600', 'font-medium');"),
    ("icon.classList.remove('text-brand-400');", "icon.classList.remove('text-brand-700');"),
    
    ("btn.classList.remove('text-slate-300', 'font-medium');", "btn.classList.remove('text-slate-600', 'font-medium');"),
    ("btn.classList.add('bg-brand-900/30', 'text-brand-400', 'font-bold', 'border', 'border-brand-800/50');", "btn.classList.add('bg-brand-50', 'text-brand-700', 'font-bold', 'border', 'border-brand-200');"),
    ("btn.querySelector('i').classList.add('text-brand-400');", "btn.querySelector('i').classList.add('text-brand-700');"),
    
    ("initNav.classList.remove('text-slate-300', 'font-medium');", "initNav.classList.remove('text-slate-600', 'font-medium');"),
    ("initNav.classList.add('bg-brand-900/30', 'text-brand-400', 'font-bold', 'border', 'border-brand-800/50');", "initNav.classList.add('bg-brand-50', 'text-brand-700', 'font-bold', 'border', 'border-brand-200');"),
    ("initNav.querySelector('i').classList.add('text-brand-400');", "initNav.querySelector('i').classList.add('text-brand-700');"),
]

# SCRIPT.JS Replacements
script_js_replacements = [
    # Logs div
    ("hover:bg-slate-800/50 transition-colors border border-transparent hover:border-slate-700", "hover:bg-slate-50 transition-colors border border-transparent hover:border-slate-200"),
    ("bg-brand-900/40 border border-brand-800/50 flex items-center justify-center text-brand-400", "bg-brand-50 border border-brand-200 flex items-center justify-center text-brand-700"),
    ('<p class="text-sm font-bold text-white leading-tight">${log.Name}</p>', '<p class="text-sm font-bold text-slate-900 leading-tight">${log.Name}</p>'),
    ('<p class="text-xs text-slate-400 font-medium mt-0.5">ID: #${log.ID}</p>', '<p class="text-xs text-slate-500 font-medium mt-0.5">ID: #${log.ID}</p>'),
    ('text-emerald-400">', 'text-emerald-600">'),
    
    # Manage Students tr
    ('hover:bg-slate-800/50 transition-colors"', 'hover:bg-slate-50 transition-colors"'),
    ('text-slate-400 font-medium"', 'text-slate-500 font-medium"'),
    ('text-white font-bold flex', 'text-slate-900 font-bold flex'),
    ('bg-slate-800 border border-slate-700 flex items-center justify-center text-slate-400', 'bg-slate-100 border border-slate-200 flex items-center justify-center text-slate-600'),
    ('bg-emerald-900/40 text-emerald-400 border border-emerald-800/50', 'bg-emerald-50 text-emerald-700 border border-emerald-200'),
    ('bg-indigo-900/30 text-indigo-400 transition-all border border-indigo-800/50', 'bg-indigo-50 text-indigo-600 transition-all border border-indigo-200'),
    ('bg-red-900/30 text-red-400 transition-all border border-red-800/50', 'bg-red-50 text-red-600 transition-all border border-red-200'),
]

# STYLE.CSS Replacements
style_css_replacements = [
    ("background: #334155;", "background: #cbd5e1;"), # slate-300
    ("/* slate-700 */", "/* slate-300 */"),
    ("background: #475569;", "background: #94a3b8;"), # slate-400
    ("/* slate-600 */", "/* slate-400 */"),
]

# Execute updates
try:
    update_file('e:/PROJECTS/AttendX/templates/index.html', index_html_replacements)
    update_file('e:/PROJECTS/AttendX/static/script.js', script_js_replacements)
    update_file('e:/PROJECTS/AttendX/static/style.css', style_css_replacements)
    print("SUCCESS")
except Exception as e:
    print(f"FAILED: {e}")
