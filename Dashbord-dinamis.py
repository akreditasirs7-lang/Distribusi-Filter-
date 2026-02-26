<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dashboard DB Distribusi</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <style>
        .hover-lift {
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        }
        
        .hover-lift:hover {
            transform: translateY(-4px) scale(1.02);
            box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04);
        }
        
        .filter-select {
            width: 100%;
            padding: 8px 12px;
            border: 2px solid #e5e7eb;
            border-radius: 12px;
            background: rgba(255, 255, 255, 0.8);
            backdrop-filter: blur(10px);
            transition: all 0.3s ease;
        }
        
        .filter-select:focus {
            outline: none;
            border-color: #3b82f6;
            background: rgba(255, 255, 255, 0.95);
            transform: scale(1.02);
        }
        
        @keyframes float {
            0%, 100% { transform: translateY(0px); }
            50% { transform: translateY(-10px); }
        }
        
        .float-animation {
            animation: float 6s ease-in-out infinite;
        }
        
        @keyframes fadeInUp {
            from {
                opacity: 0;
                transform: translateY(30px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }
        
        .fade-in-up {
            animation: fadeInUp 0.6s ease-out;
        }
        
        @keyframes pulse {
            0%, 100% { transform: scale(1); }
            50% { transform: scale(1.05); }
        }
        
        .pulse-animation {
            animation: pulse 2s ease-in-out infinite;
        }

        .status-indicator {
            position: fixed;
            top: 20px;
            right: 20px;
            z-index: 1000;
            padding: 12px 16px;
            border-radius: 8px;
            color: white;
            font-weight: 500;
            box-shadow: 0 4px 12px rgba(0,0,0,0.15);
        }
        
        .status-success { background: #10b981; }
        .status-error { background: #ef4444; }
        .status-loading { background: #3b82f6; }

        /* Forest Animation Styles */
        @keyframes sway-gentle {
            0%, 100% { transform: translateX(0) rotate(0deg); }
            25% { transform: translateX(3px) rotate(1deg); }
            50% { transform: translateX(0) rotate(0deg); }
            75% { transform: translateX(-3px) rotate(-1deg); }
        }
        
        @keyframes sway-medium {
            0%, 100% { transform: translateX(0) rotate(0deg); }
            33% { transform: translateX(5px) rotate(2deg); }
            66% { transform: translateX(-5px) rotate(-2deg); }
        }
        
        @keyframes sway-strong {
            0%, 100% { transform: translateX(0) rotate(0deg); }
            50% { transform: translateX(8px) rotate(3deg); }
        }
        
        .animate-sway-gentle { animation: sway-gentle 8s ease-in-out infinite; }
        .animate-sway-medium { animation: sway-medium 6s ease-in-out infinite; }
        .animate-sway-strong { animation: sway-strong 4s ease-in-out infinite; }
        
        /* Tree Silhouettes */
        .tree {
            position: absolute;
            bottom: 0;
        }
        
        .tree1 {
            left: 5%;
            width: 60px;
            height: 120px;
            background: linear-gradient(to top, #1f2937 0%, #374151 70%, #22c55e 100%);
            clip-path: polygon(45% 0%, 55% 0%, 60% 15%, 70% 15%, 65% 25%, 75% 25%, 70% 35%, 80% 35%, 75% 50%, 85% 50%, 80% 65%, 90% 65%, 85% 80%, 95% 80%, 90% 95%, 100% 95%, 100% 100%, 0% 100%, 0% 95%, 10% 95%, 5% 80%, 15% 80%, 10% 65%, 20% 65%, 15% 50%, 25% 50%, 20% 35%, 30% 35%, 25% 25%, 35% 25%, 30% 15%, 40% 15%);
        }
        
        .tree2 {
            right: 8%;
            width: 80px;
            height: 140px;
            background: linear-gradient(to top, #1f2937 0%, #374151 60%, #16a34a 100%);
            clip-path: polygon(40% 0%, 60% 0%, 65% 20%, 75% 20%, 70% 35%, 80% 35%, 75% 50%, 85% 50%, 80% 70%, 90% 70%, 85% 85%, 95% 85%, 90% 100%, 100% 100%, 0% 100%, 10% 100%, 5% 85%, 15% 85%, 10% 70%, 20% 70%, 15% 50%, 25% 50%, 20% 35%, 30% 35%, 25% 20%, 35% 20%);
        }
        
        .tree3 {
            left: 15%;
            width: 45px;
            height: 90px;
            background: linear-gradient(to top, #374151 0%, #4b5563 70%, #15803d 100%);
            clip-path: polygon(40% 0%, 60% 0%, 70% 25%, 80% 25%, 75% 50%, 85% 50%, 80% 75%, 90% 75%, 85% 100%, 100% 100%, 0% 100%, 15% 100%, 10% 75%, 20% 75%, 15% 50%, 25% 50%, 20% 25%, 30% 25%);
        }
        
        .tree4 {
            right: 25%;
            width: 55px;
            height: 110px;
            background: linear-gradient(to top, #1f2937 0%, #374151 65%, #166534 100%);
            clip-path: polygon(42% 0%, 58% 0%, 65% 18%, 75% 18%, 70% 32%, 80% 32%, 75% 48%, 85% 48%, 80% 65%, 90% 65%, 85% 82%, 95% 82%, 90% 100%, 100% 100%, 0% 100%, 10% 100%, 5% 82%, 15% 82%, 10% 65%, 20% 65%, 15% 48%, 25% 48%, 20% 32%, 30% 32%, 25% 18%, 35% 18%);
        }
        
        /* Floating Leaves */
        .leaf {
            position: absolute;
            width: 8px;
            height: 8px;
            background: #22c55e;
            border-radius: 0 100% 0 100%;
            opacity: 0.7;
        }
        
        .leaf1 {
            top: 15%;
            left: 20%;
            animation: leaf-fall 12s ease-in-out infinite;
            background: #16a34a;
        }
        
        .leaf2 {
            top: 25%;
            right: 30%;
            animation: leaf-fall 15s ease-in-out infinite reverse;
            background: #15803d;
        }
        
        .leaf3 {
            top: 35%;
            left: 60%;
            animation: leaf-fall 18s ease-in-out infinite;
            background: #22c55e;
        }
        
        .leaf4 {
            top: 45%;
            right: 15%;
            animation: leaf-fall 14s ease-in-out infinite reverse;
            background: #166534;
        }
        
        .leaf5 {
            top: 55%;
            left: 40%;
            animation: leaf-fall 16s ease-in-out infinite;
            background: #16a34a;
        }
        
        @keyframes leaf-fall {
            0%, 100% { 
                transform: translateY(0) translateX(0) rotate(0deg);
                opacity: 0.7;
            }
            25% { 
                transform: translateY(20px) translateX(10px) rotate(90deg);
                opacity: 1;
            }
            50% { 
                transform: translateY(40px) translateX(-5px) rotate(180deg);
                opacity: 0.5;
            }
            75% { 
                transform: translateY(20px) translateX(-15px) rotate(270deg);
                opacity: 0.8;
            }
        }
    </style>
</head>
<body class="min-h-screen bg-gradient-to-br from-blue-50 via-indigo-50 to-purple-50 relative overflow-x-hidden">
    <!-- Animated Forest Background -->
    <div class="fixed inset-0 -z-10 overflow-hidden">
        <!-- Forest gradient -->
        <div class="absolute inset-0 bg-gradient-to-b from-green-100 via-emerald-50 to-green-200"></div>
        
        <!-- Tree silhouettes -->
        <div class="tree tree1 animate-sway-gentle"></div>
        <div class="tree tree2 animate-sway-medium"></div>
        <div class="tree tree3 animate-sway-strong"></div>
        <div class="tree tree4 animate-sway-gentle"></div>
        
        <!-- Floating leaves -->
        <div class="leaf leaf1"></div>
        <div class="leaf leaf2"></div>
        <div class="leaf leaf3"></div>
        <div class="leaf leaf4"></div>
        <div class="leaf leaf5"></div>
    </div>
    <!-- Status Indicator -->
    <div id="statusIndicator" class="status-indicator hidden">
        <div class="flex items-center space-x-2">
            <div id="statusIcon">⏳</div>
            <span id="statusText">Loading...</span>
        </div>
    </div>

    <!-- Header -->
    <header class="bg-white/80 backdrop-blur-md shadow-lg border-b border-white/20 fade-in-up">
        <div class="max-w-7xl mx-auto px-4 py-4">
            <div class="flex items-center justify-between">
                <div class="flex items-center space-x-3">
                    <div class="w-10 h-10 bg-gradient-to-br from-blue-500 to-purple-600 rounded-xl flex items-center justify-center pulse-animation shadow-lg">
                        <svg class="w-5 h-5 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z"></path>
                        </svg>
                    </div>
                    <h1 class="text-xl font-bold bg-gradient-to-r from-blue-600 to-purple-600 bg-clip-text text-transparent">Dashboard DB Distribusi</h1>
                </div>
                <div class="flex items-center space-x-3">
                    <span id="lastUpdate" class="text-sm text-gray-500 hidden sm:block">-</span>
                    <button id="backToSetupBtn" class="bg-gradient-to-r from-gray-500 to-gray-600 hover:from-gray-600 hover:to-gray-700 text-white px-4 py-2 rounded-xl text-sm transition-all duration-300 hover:scale-105 shadow-lg">
                        Ganti Sheet
                    </button>
                    <button id="refreshBtn" class="bg-gradient-to-r from-blue-500 to-purple-600 hover:from-blue-600 hover:to-purple-700 text-white px-4 py-2 rounded-xl text-sm transition-all duration-300 hover:scale-105 shadow-lg">
                        Refresh
                    </button>
                </div>
            </div>
        </div>
    </header>

    <!-- Setup Panel -->
    <div id="setupPanel" class="max-w-4xl mx-auto mt-8 px-4 fade-in-up">
        <div class="bg-white/80 backdrop-blur-sm rounded-2xl shadow-xl p-8 border border-white/20 hover-lift">
            <h2 class="text-lg font-semibold text-gray-900 mb-4">Koneksi Google Sheets</h2>
            <div class="space-y-4">
                <div>
                    <label class="block text-sm font-medium text-gray-700 mb-2">URL Google Sheets</label>
                    <input type="text" id="sheetUrl" placeholder="https://docs.google.com/spreadsheets/d/YOUR_SHEET_ID/edit#gid=0" 
                           class="w-full px-3 py-2 border border-gray-300 rounded focus:ring-2 focus:ring-blue-500 focus:border-blue-500">
                    <div class="mt-2 p-3 bg-blue-50 border border-blue-200 rounded text-sm">
                        <p class="font-medium text-blue-800 mb-1">Setup:</p>
                        <p class="text-blue-700">1. Sheet bernama "DB Distribusi" → 2. File → Share → Publish to web → 3. Pilih "Entire Document" dan "Web page" → 4. Publish</p>
                    </div>
                </div>
                <div class="flex space-x-3">
                    <button id="connectBtn" class="bg-green-500 hover:bg-green-600 text-white px-4 py-2 rounded">
                        Hubungkan
                    </button>
                </div>
            </div>
        </div>
    </div>

    <!-- Dashboard Content -->
    <div id="dashboardContent" class="hidden max-w-7xl mx-auto mt-6 px-4 pb-8">
        <!-- Filter Section -->
        <div class="bg-white/80 backdrop-blur-sm rounded-2xl shadow-xl p-6 mb-8 border border-white/20 fade-in-up float-animation">
            <h3 class="text-lg font-semibold text-gray-900 mb-4">
                Filter Data
                <span id="filterInfo" class="ml-3 text-sm text-blue-600 bg-blue-100 px-2 py-1 rounded"></span>
            </h3>
            <div class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-3">
                <div>
                    <label class="block text-xs font-medium text-gray-700 mb-1">Jenis Pengimputan</label>
                    <select id="requestTypeFilter" class="filter-select text-sm">
                        <option value="">Semua</option>
                    </select>
                </div>
                <div>
                    <label class="block text-xs font-medium text-gray-700 mb-1">Jenis Permintaan</label>
                    <select id="requestCategoryFilter" class="filter-select text-sm">
                        <option value="">Semua</option>
                    </select>
                </div>
                <div>
                    <label class="block text-xs font-medium text-gray-700 mb-1">RS/Klinik</label>
                    <select id="hospitalFilter" class="filter-select text-sm">
                        <option value="">Semua</option>
                    </select>
                </div>
                <div>
                    <label class="block text-xs font-medium text-gray-700 mb-1">Komponen</label>
                    <select id="componentFilter" class="filter-select text-sm">
                        <option value="">Semua</option>
                    </select>
                </div>
                <div>
                    <label class="block text-xs font-medium text-gray-700 mb-1">Golongan Darah</label>
                    <select id="bloodTypeFilter" class="filter-select text-sm">
                        <option value="">Semua</option>
                    </select>
                </div>
                <div>
                    <label class="block text-xs font-medium text-gray-700 mb-1">Rhesus</label>
                    <select id="rhesusFilter" class="filter-select text-sm">
                        <option value="">Semua</option>
                        <option value="Positif">Positif</option>
                        <option value="Negatif">Negatif</option>
                    </select>
                </div>
                <div>
                    <label class="block text-xs font-medium text-gray-700 mb-1">Bulan</label>
                    <select id="monthFilter" class="filter-select text-sm">
                        <option value="">Semua</option>
                        <option value="Januari">Januari</option>
                        <option value="Februari">Februari</option>
                        <option value="Maret">Maret</option>
                        <option value="April">April</option>
                        <option value="Mei">Mei</option>
                        <option value="Juni">Juni</option>
                        <option value="Juli">Juli</option>
                        <option value="Agustus">Agustus</option>
                        <option value="September">September</option>
                        <option value="Oktober">Oktober</option>
                        <option value="November">November</option>
                        <option value="Desember">Desember</option>
                    </select>
                </div>
                <div>
                    <label class="block text-xs font-medium text-gray-700 mb-1">Tahun</label>
                    <select id="yearFilter" class="filter-select text-sm">
                        <option value="">Semua</option>
                    </select>
                </div>
            </div>
            <div class="mt-4">
                <button id="resetFilter" class="bg-red-500 hover:bg-red-600 text-white px-4 py-2 rounded text-sm">
                    Reset Filter
                </button>
            </div>
        </div>

        <!-- Stats Cards -->
        <div class="grid grid-cols-1 md:grid-cols-2 gap-6 mb-6">
            <div class="bg-white/80 backdrop-blur-sm rounded-xl shadow-lg p-6 hover-lift border border-white/20">
                <div class="flex items-center justify-between">
                    <div>
                        <p class="text-sm text-gray-600 mb-1">Total Distribusi</p>
                        <p id="totalDistribution" class="text-3xl font-bold text-blue-600">0</p>
                        <p class="text-xs text-gray-500 mt-1">unit darah</p>
                    </div>
                    <div class="w-12 h-12 bg-gradient-to-br from-blue-400 to-blue-600 rounded-xl flex items-center justify-center shadow-lg">
                        <span class="text-white text-xl">🩸</span>
                    </div>
                </div>
            </div>



            <div class="bg-white/80 backdrop-blur-sm rounded-xl shadow-lg p-6 hover-lift border border-white/20">
                <div class="flex items-center justify-between">
                    <div>
                        <p class="text-sm text-gray-600 mb-1">Komponen Terbanyak</p>
                        <p id="topComponent" class="text-lg font-bold text-purple-600">-</p>
                        <p id="topComponentCount" class="text-xs text-gray-500">0 unit</p>
                        <div class="mt-2">
                            <p class="text-xs text-gray-600">RS Terbanyak:</p>
                            <p id="topHospital" class="text-sm font-semibold text-red-600">-</p>
                        </div>
                    </div>
                    <div class="w-12 h-12 bg-gradient-to-br from-purple-400 to-red-500 rounded-xl flex items-center justify-center shadow-lg">
                        <span class="text-white text-xl">🏆</span>
                    </div>
                </div>
            </div>
        </div>

        <!-- Charts Section -->
        <div class="grid grid-cols-1 lg:grid-cols-3 gap-6 mb-8">
            <div class="bg-white/80 backdrop-blur-sm rounded-2xl shadow-xl p-6 hover-lift border border-white/20 fade-in-up">
                <h3 class="text-lg font-semibold bg-gradient-to-r from-red-500 to-blue-500 bg-clip-text text-transparent mb-4">Distribusi Golongan Darah</h3>
                <div class="h-48">
                    <canvas id="bloodTypeChart"></canvas>
                </div>
            </div>
            <div class="bg-white/80 backdrop-blur-sm rounded-2xl shadow-xl p-6 hover-lift border border-white/20 fade-in-up">
                <h3 class="text-lg font-semibold bg-gradient-to-r from-green-500 to-red-500 bg-clip-text text-transparent mb-4">Distribusi Rhesus</h3>
                <div class="h-48">
                    <canvas id="rhesusChart"></canvas>
                </div>
            </div>
            <div class="bg-white/80 backdrop-blur-sm rounded-2xl shadow-xl p-6 hover-lift border border-white/20 fade-in-up">
                <h3 class="text-lg font-semibold bg-gradient-to-r from-blue-500 to-purple-500 bg-clip-text text-transparent mb-4">Top 5 Komponen</h3>
                <div class="h-48">
                    <canvas id="componentChart"></canvas>
                </div>
            </div>
        </div>

        <div class="grid grid-cols-1 lg:grid-cols-2 gap-6 mb-8">
            <div class="bg-white/80 backdrop-blur-sm rounded-2xl shadow-xl p-6 hover-lift border border-white/20 fade-in-up">
                <h3 class="text-lg font-semibold bg-gradient-to-r from-green-500 to-blue-500 bg-clip-text text-transparent mb-4">Trend Bulanan</h3>
                <div class="h-48">
                    <canvas id="monthlyChart"></canvas>
                </div>
            </div>
            <div class="bg-white/80 backdrop-blur-sm rounded-2xl shadow-xl p-6 hover-lift border border-white/20 fade-in-up">
                <h3 class="text-lg font-semibold bg-gradient-to-r from-purple-500 to-red-500 bg-clip-text text-transparent mb-4">Top 5 RS/Klinik</h3>
                <div class="h-48">
                    <canvas id="hospitalChart"></canvas>
                </div>
            </div>
        </div>

        <!-- Data Table -->
        <div class="bg-white/80 backdrop-blur-sm rounded-2xl shadow-xl overflow-hidden border border-white/20 fade-in-up">
            <div class="px-4 py-3 border-b flex items-center justify-between">
                <h3 class="text-sm font-semibold text-gray-900">Data Distribusi</h3>
                <span id="recordCount" class="text-xs text-gray-600">0 data</span>
            </div>
            <div class="overflow-x-auto">
                <table class="min-w-full divide-y divide-gray-200">
                    <thead id="tableHead" class="bg-gray-50">
                        <!-- Headers will be populated -->
                    </thead>
                    <tbody id="tableBody" class="bg-white divide-y divide-gray-200">
                        <!-- Data will be populated -->
                    </tbody>
                </table>
            </div>
            <div id="paginationControls"></div>
        </div>
    </div>

    <script>
        // Global variables
        let currentData = [];
        let filteredData = [];
        let charts = {};

        // Status management
        function showStatus(type, message, icon = '⏳') {
            const indicator = document.getElementById('statusIndicator');
            const iconEl = document.getElementById('statusIcon');
            const textEl = document.getElementById('statusText');
            
            indicator.className = `status-indicator status-${type}`;
            iconEl.textContent = icon;
            textEl.textContent = message;
            indicator.classList.remove('hidden');
            
            if (type === 'success' || type === 'error') {
                setTimeout(() => {
                    indicator.classList.add('hidden');
                }, 3000);
            }
        }

        function hideStatus() {
            document.getElementById('statusIndicator').classList.add('hidden');
        }

        // Auto-load sheet data function
        function autoLoadSheetData() {
            const sheetUrl = 'https://docs.google.com/spreadsheets/d/10dE-WS9I_he6TEyen1GAqPIObA5G9m09eHQn4_59eeY/edit?usp=sharing';
            console.log('🚀 Auto-loading sheet data...');
            loadSheetData(sheetUrl);
        }

        // CSV parsing functions
        function convertToCSVUrl(url) {
            try {
                const match = url.match(/\/spreadsheets\/d\/([a-zA-Z0-9-_]+)/);
                if (match) {
                    const sheetId = match[1];
                    return [
                        `https://docs.google.com/spreadsheets/d/${sheetId}/export?format=csv&gid=0`,
                        `https://docs.google.com/spreadsheets/d/${sheetId}/gviz/tq?tqx=out:csv`,
                        `https://docs.google.com/spreadsheets/d/${sheetId}/export?format=csv`
                    ];
                }
                return null;
            } catch (error) {
                console.error('URL conversion error:', error);
                return null;
            }
        }

        function parseCSV(csv) {
            const lines = csv.split(/\r?\n/).filter(line => line.trim().length > 0);
            if (lines.length === 0) return { headers: [], data: [] };

            function parseCSVLine(line) {
                const result = [];
                let current = '';
                let inQuotes = false;
                
                for (let i = 0; i < line.length; i++) {
                    const char = line[i];
                    if (char === '"') {
                        if (inQuotes && line[i + 1] === '"') {
                            current += '"';
                            i++;
                        } else {
                            inQuotes = !inQuotes;
                        }
                    } else if (char === ',' && !inQuotes) {
                        result.push(current.trim());
                        current = '';
                    } else {
                        current += char;
                    }
                }
                result.push(current.trim());
                return result;
            }

            const headers = parseCSVLine(lines[0]);
            const data = [];

            for (let i = 1; i < lines.length; i++) {
                const line = lines[i].trim();
                if (line) {
                    const values = parseCSVLine(line);
                    const row = {};
                    headers.forEach((header, index) => {
                        row[header] = values[index] || '';
                    });
                    const hasData = Object.values(row).some(val => val && val.toString().trim());
                    if (hasData) data.push(row);
                }
            }

            return { headers, data };
        }

        // Filter and data management
        function populateFilters(data) {
            const hospitals = [...new Set(data.map(row => row['RS/Klinik Tujuan']).filter(h => h))].sort();
            const components = [...new Set(data.map(row => row['Komponen']).filter(c => c))].sort();
            const bloodTypes = [...new Set(data.map(row => row['Golongan Darah']).filter(b => b))].sort();
            const years = [...new Set(data.map(row => row['Tahun']).filter(y => y))].sort((a, b) => b - a);
            const requestTypes = [...new Set(data.map(row => row['Jenis Pengimputan']).filter(r => r))].sort();
            const requestCategories = [...new Set(data.map(row => row['Jenis Permintaan']).filter(r => r))].sort();

            document.getElementById('hospitalFilter').innerHTML = '<option value="">Semua</option>' + 
                hospitals.map(h => `<option value="${h}">${h}</option>`).join('');
            
            document.getElementById('componentFilter').innerHTML = '<option value="">Semua</option>' + 
                components.map(c => `<option value="${c}">${c}</option>`).join('');
            
            document.getElementById('bloodTypeFilter').innerHTML = '<option value="">Semua</option>' + 
                bloodTypes.map(b => `<option value="${b}">${b}</option>`).join('');
            
            document.getElementById('yearFilter').innerHTML = '<option value="">Semua</option>' + 
                years.map(y => `<option value="${y}">${y}</option>`).join('');
            
            document.getElementById('requestTypeFilter').innerHTML = '<option value="">Semua</option>' + 
                requestTypes.map(r => `<option value="${r}">${r}</option>`).join('');
            
            document.getElementById('requestCategoryFilter').innerHTML = '<option value="">Semua</option>' + 
                requestCategories.map(r => `<option value="${r}">${r}</option>`).join('');
        }

        function applyFilters() {
            const filters = {
                requestType: document.getElementById('requestTypeFilter').value,
                requestCategory: document.getElementById('requestCategoryFilter').value,
                hospital: document.getElementById('hospitalFilter').value,
                component: document.getElementById('componentFilter').value,
                bloodType: document.getElementById('bloodTypeFilter').value,
                rhesus: document.getElementById('rhesusFilter').value,
                month: document.getElementById('monthFilter').value,
                year: document.getElementById('yearFilter').value
            };

            filteredData = currentData.filter(row => {
                return (!filters.requestType || row['Jenis Pengimputan'] === filters.requestType) &&
                       (!filters.requestCategory || row['Jenis Permintaan'] === filters.requestCategory) &&
                       (!filters.hospital || row['RS/Klinik Tujuan'] === filters.hospital) &&
                       (!filters.component || row['Komponen'] === filters.component) &&
                       (!filters.bloodType || row['Golongan Darah'] === filters.bloodType) &&
                       (!filters.rhesus || row['Rhesus'] === filters.rhesus) &&
                       (!filters.month || row['Bulan'] === filters.month) &&
                       (!filters.year || row['Tahun'] === filters.year);
            });

            document.getElementById('filterInfo').textContent = `${filteredData.length}/${currentData.length} data`;
            updateDashboard();
        }

        function updateDashboard() {
            updateStats(filteredData);
            createTable(filteredData);
            createCharts(filteredData);
        }

        function updateStats(data) {
            const jumlahColumn = Object.keys(data[0] || {}).find(h => h.toLowerCase().includes('jumlah')) || 'Jumlah';
            const totalUnits = data.reduce((sum, row) => sum + (parseInt(row[jumlahColumn]) || 0), 0);
            
            document.getElementById('totalDistribution').textContent = totalUnits.toLocaleString('id-ID');

            // Top component
            const components = {};
            data.forEach(row => {
                const comp = row['Komponen'];
                if (comp) {
                    const units = parseInt(row[jumlahColumn]) || 0;
                    components[comp] = (components[comp] || 0) + units;
                }
            });

            if (Object.keys(components).length > 0) {
                const topComponent = Object.keys(components).reduce((a, b) => components[a] > components[b] ? a : b);
                document.getElementById('topComponent').textContent = topComponent;
                document.getElementById('topComponentCount').textContent = `${components[topComponent].toLocaleString('id-ID')} unit`;
            } else {
                document.getElementById('topComponent').textContent = '-';
                document.getElementById('topComponentCount').textContent = '0 unit';
            }

            // Top hospital
            const hospitals = {};
            data.forEach(row => {
                const hospital = row['RS/Klinik Tujuan'];
                if (hospital) hospitals[hospital] = (hospitals[hospital] || 0) + 1;
            });

            if (Object.keys(hospitals).length > 0) {
                const topHospital = Object.keys(hospitals).reduce((a, b) => hospitals[a] > hospitals[b] ? a : b);
                const shortName = topHospital.length > 15 ? topHospital.substring(0, 15) + '...' : topHospital;
                document.getElementById('topHospital').textContent = shortName;
            } else {
                document.getElementById('topHospital').textContent = '-';
            }

            document.getElementById('recordCount').textContent = `${data.length} data (${totalUnits.toLocaleString('id-ID')} unit)`;
            document.getElementById('lastUpdate').textContent = `Update: ${new Date().toLocaleTimeString('id-ID')}`;
        }

        function createTable(data) {
            const tableHead = document.getElementById('tableHead');
            const tableBody = document.getElementById('tableBody');

            if (data.length === 0) {
                tableHead.innerHTML = '<tr><th class="px-3 py-2 text-center text-gray-500">Tidak ada data</th></tr>';
                tableBody.innerHTML = '<tr><td class="px-3 py-3 text-center text-gray-500">Tidak ada data</td></tr>';
                return;
            }

            const headers = Object.keys(data[0]);
            tableHead.innerHTML = `<tr>${headers.map(h => `<th class="px-3 py-2 text-left text-xs font-medium text-gray-500 uppercase">${h}</th>`).join('')}</tr>`;

            const currentPage = window.currentPage || 1;
            const itemsPerPage = 20;
            const startIndex = (currentPage - 1) * itemsPerPage;
            const displayData = data.slice(startIndex, startIndex + itemsPerPage);

            tableBody.innerHTML = displayData.map((row, index) => `
                <tr class="${index % 2 === 0 ? 'bg-white' : 'bg-gray-50'}">
                    ${headers.map(header => {
                        let value = row[header] || '-';
                        if (header === 'Jumlah') {
                            return `<td class="px-3 py-2 text-sm font-medium text-right">${parseInt(value) || 0}</td>`;
                        }
                        if (header === 'Golongan Darah') {
                            const colors = { 'A': 'bg-red-100 text-red-800', 'B': 'bg-blue-100 text-blue-800', 'AB': 'bg-purple-100 text-purple-800', 'O': 'bg-green-100 text-green-800' };
                            const color = colors[value] || 'bg-gray-100 text-gray-800';
                            return `<td class="px-3 py-2 text-sm"><span class="px-2 py-1 rounded text-xs ${color}">${value}</span></td>`;
                        }
                        if (header === 'RS/Klinik Tujuan' && value.length > 20) {
                            value = value.substring(0, 20) + '...';
                        }
                        return `<td class="px-3 py-2 text-sm">${value}</td>`;
                    }).join('')}
                </tr>
            `).join('');

            // Simple pagination
            const totalPages = Math.ceil(data.length / itemsPerPage);
            if (totalPages > 1) {
                document.getElementById('paginationControls').innerHTML = `
                    <div class="px-4 py-3 border-t flex justify-between items-center">
                        <button onclick="changePage(${currentPage - 1})" ${currentPage === 1 ? 'disabled' : ''} 
                                class="px-3 py-1 text-sm border rounded ${currentPage === 1 ? 'bg-gray-100 text-gray-400' : 'bg-white hover:bg-gray-50'}">
                            Previous
                        </button>
                        <span class="text-sm text-gray-600">${currentPage} / ${totalPages}</span>
                        <button onclick="changePage(${currentPage + 1})" ${currentPage === totalPages ? 'disabled' : ''} 
                                class="px-3 py-1 text-sm border rounded ${currentPage === totalPages ? 'bg-gray-100 text-gray-400' : 'bg-white hover:bg-gray-50'}">
                            Next
                        </button>
                    </div>
                `;
            } else {
                document.getElementById('paginationControls').innerHTML = '';
            }
        }

        function changePage(newPage) {
            const totalPages = Math.ceil(filteredData.length / 20);
            if (newPage < 1 || newPage > totalPages) return;
            window.currentPage = newPage;
            createTable(filteredData);
        }

        function createCharts(data) {
            // Destroy existing charts
            Object.values(charts).forEach(chart => {
                if (chart && typeof chart.destroy === 'function') {
                    chart.destroy();
                }
            });
            charts = {};

            if (data.length === 0) return;

            // Blood Type Chart
            const bloodTypes = {};
            data.forEach(row => {
                const type = row['Golongan Darah'] || 'Unknown';
                bloodTypes[type] = (bloodTypes[type] || 0) + 1;
            });

            charts.bloodTypeChart = new Chart(document.getElementById('bloodTypeChart'), {
                type: 'doughnut',
                data: {
                    labels: Object.keys(bloodTypes),
                    datasets: [{
                        data: Object.values(bloodTypes),
                        backgroundColor: ['#EF4444', '#3B82F6', '#8B5CF6', '#10B981'],
                        borderWidth: 3,
                        borderColor: '#ffffff',
                        hoverBorderWidth: 5,
                        hoverOffset: 10
                    }]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    plugins: { 
                        legend: { position: 'bottom', labels: { boxWidth: 12, font: { size: 10 } } },
                        tooltip: {
                            callbacks: {
                                label: function(context) {
                                    const label = context.label || '';
                                    const value = context.parsed;
                                    const total = context.dataset.data.reduce((a, b) => a + b, 0);
                                    const percentage = ((value / total) * 100).toFixed(1);
                                    return `${label}: ${value} data (${percentage}%)`;
                                }
                            }
                        }
                    },
                    elements: {
                        arc: {
                            borderRadius: 8
                        }
                    }
                }
            });

            // Rhesus Chart
            const rhesusTypes = {};
            data.forEach(row => {
                const rhesus = row['Rhesus'] || 'Unknown';
                rhesusTypes[rhesus] = (rhesusTypes[rhesus] || 0) + 1;
            });

            charts.rhesusChart = new Chart(document.getElementById('rhesusChart'), {
                type: 'pie',
                data: {
                    labels: Object.keys(rhesusTypes),
                    datasets: [{
                        data: Object.values(rhesusTypes),
                        backgroundColor: ['#10B981', '#EF4444', '#6B7280'],
                        borderWidth: 3,
                        borderColor: '#ffffff',
                        hoverBorderWidth: 5,
                        hoverOffset: 15
                    }]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    plugins: { 
                        legend: { position: 'bottom', labels: { boxWidth: 12, font: { size: 10 } } },
                        tooltip: {
                            callbacks: {
                                label: function(context) {
                                    const label = context.label || '';
                                    const value = context.parsed;
                                    const total = context.dataset.data.reduce((a, b) => a + b, 0);
                                    const percentage = ((value / total) * 100).toFixed(1);
                                    return `${label}: ${value} data (${percentage}%)`;
                                }
                            }
                        }
                    },
                    elements: {
                        arc: {
                            borderRadius: 6
                        }
                    }
                }
            });

            // Component Chart
            const jumlahColumn = Object.keys(data[0]).find(h => h.toLowerCase().includes('jumlah')) || 'Jumlah';
            const components = {};
            data.forEach(row => {
                const comp = row['Komponen'];
                if (comp) {
                    const units = parseInt(row[jumlahColumn]) || 0;
                    components[comp] = (components[comp] || 0) + units;
                }
            });

            const topComponents = Object.entries(components).sort(([,a], [,b]) => b - a).slice(0, 5);

            if (topComponents.length > 0) {
                charts.componentChart = new Chart(document.getElementById('componentChart'), {
                    type: 'bar',
                    data: {
                        labels: topComponents.map(([name]) => name),
                        datasets: [{
                            data: topComponents.map(([, units]) => units),
                            backgroundColor: [
                                '#3B82F6',
                                '#10B981',
                                '#8B5CF6',
                                '#F59E0B',
                                '#EF4444'
                            ],
                            borderColor: '#ffffff',
                            borderWidth: 2,
                            borderRadius: 8,
                            borderSkipped: false,
                            hoverBackgroundColor: [
                                '#1E40AF',
                                '#047857',
                                '#5B21B6',
                                '#D97706',
                                '#DC2626'
                            ],
                            hoverBorderWidth: 3
                        }]
                    },
                    options: {
                        responsive: true,
                        maintainAspectRatio: false,
                        plugins: { 
                            legend: { display: false },
                            tooltip: {
                                callbacks: {
                                    label: function(context) {
                                        return `${context.label}: ${context.parsed.y.toLocaleString('id-ID')} unit`;
                                    }
                                }
                            }
                        },
                        scales: { 
                            y: { 
                                beginAtZero: true,
                                ticks: {
                                    callback: function(value) {
                                        return value.toLocaleString('id-ID');
                                    }
                                }
                            }
                        }
                    }
                });
            }

            // Monthly Chart
            const monthlyData = {};
            data.forEach(row => {
                const month = row['Bulan'] || 'Unknown';
                const units = parseInt(row[jumlahColumn]) || 0;
                monthlyData[month] = (monthlyData[month] || 0) + units;
            });

            const months = ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember'];
            const monthlyValues = months.map(month => monthlyData[month] || 0);

            charts.monthlyChart = new Chart(document.getElementById('monthlyChart'), {
                type: 'line',
                data: {
                    labels: months,
                    datasets: [{
                        data: monthlyValues,
                        borderColor: '#10B981',
                        backgroundColor: 'rgba(16, 185, 129, 0.1)',
                        tension: 0.4,
                        fill: true
                    }]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    plugins: { legend: { display: false } },
                    scales: { y: { beginAtZero: true } }
                }
            });

            // Hospital Chart
            const hospitals = {};
            data.forEach(row => {
                const hospital = row['RS/Klinik Tujuan'];
                if (hospital) {
                    const units = parseInt(row[jumlahColumn]) || 0;
                    hospitals[hospital] = (hospitals[hospital] || 0) + units;
                }
            });

            const topHospitals = Object.entries(hospitals).sort(([,a], [,b]) => b - a).slice(0, 5);

            if (topHospitals.length > 0) {
                charts.hospitalChart = new Chart(document.getElementById('hospitalChart'), {
                    type: 'bar',
                    data: {
                        labels: topHospitals.map(([name]) => name.length > 15 ? name.substring(0, 15) + '...' : name),
                        datasets: [{
                            data: topHospitals.map(([, count]) => count),
                            backgroundColor: [
                                '#8B5CF6',
                                '#3B82F6',
                                '#10B981',
                                '#F59E0B',
                                '#EF4444'
                            ],
                            borderColor: '#ffffff',
                            borderWidth: 2,
                            borderRadius: 6,
                            borderSkipped: false,
                            hoverBackgroundColor: [
                                '#6D28D9',
                                '#1E40AF',
                                '#047857',
                                '#D97706',
                                '#DC2626'
                            ],
                            hoverBorderWidth: 3
                        }]
                    },
                    options: {
                        responsive: true,
                        maintainAspectRatio: false,
                        indexAxis: 'y',
                        plugins: { 
                            legend: { display: false },
                            tooltip: {
                                callbacks: {
                                    label: function(context) {
                                        return `${context.label}: ${context.parsed.x.toLocaleString('id-ID')} unit`;
                                    }
                                }
                            }
                        },
                        scales: { 
                            x: { 
                                beginAtZero: true,
                                ticks: {
                                    callback: function(value) {
                                        return value.toLocaleString('id-ID');
                                    }
                                }
                            }
                        }
                    }
                });
            }
        }

        // Google Sheets loading
        async function loadSheetData(url) {
            showStatus('loading', 'Menghubungkan ke Google Sheets...', '⏳');
            
            try {
                console.log('🔄 Loading sheet data from:', url);
                const csvUrls = convertToCSVUrl(url);
                if (!csvUrls) throw new Error('URL tidak valid - pastikan format Google Sheets URL benar');

                console.log('📡 Trying CSV URLs:', csvUrls);
                let csvData = null;
                let lastError = null;
                
                for (let i = 0; i < csvUrls.length; i++) {
                    const csvUrl = csvUrls[i];
                    try {
                        console.log(`🌐 Attempt ${i + 1}: Fetching ${csvUrl}`);
                        
                        const response = await fetch(csvUrl, {
                            method: 'GET',
                            mode: 'cors',
                            cache: 'no-cache'
                        });
                        
                        console.log(`📊 Response ${i + 1}: Status ${response.status}`);
                        
                        if (response.ok) {
                            csvData = await response.text();
                            console.log(`✅ Success! Data length: ${csvData.length} characters`);
                            break;
                        } else {
                            lastError = `HTTP ${response.status}: ${response.statusText}`;
                            console.warn(`⚠️ Failed attempt ${i + 1}:`, lastError);
                        }
                    } catch (error) {
                        console.error(`❌ Fetch error attempt ${i + 1}:`, error);
                        lastError = error.message;
                        continue;
                    }
                }

                if (!csvData || csvData.trim().length === 0) {
                    throw new Error(`Gagal mengambil data dari Google Sheets.\n\nLast error: ${lastError}\n\nPastikan:\n1. Sheet sudah di-publish (File → Share → Publish to web)\n2. Pilih "Entire Document" dan "Web page"\n3. Klik "Publish"`);
                }

                console.log('🔍 Parsing CSV data...');
                const { data, headers } = parseCSV(csvData);
                console.log(`📋 Headers found: ${headers.join(', ')}`);
                console.log(`📊 Parsed ${data.length} data rows`);
                
                if (data.length === 0) {
                    throw new Error('Data kosong atau format tidak sesuai.\n\nPastikan sheet memiliki data dan header yang benar.');
                }

                currentData = data;
                filteredData = data;
                
                populateFilters(data);
                updateDashboard();
                
                console.log('🎉 Successfully loaded and displayed data!');
                showStatus('success', `Berhasil memuat ${data.length} data dari Google Sheets!`, '✅');
                
                document.getElementById('setupPanel').classList.add('hidden');
                document.getElementById('dashboardContent').classList.remove('hidden');

            } catch (error) {
                console.error('💥 Load error:', error);
                showStatus('error', `Error: ${error.message}`, '❌');
            }
        }

        // Event listeners
        document.addEventListener('DOMContentLoaded', () => {
            console.log('🚀 Page loaded, connecting to Google Sheets...');
            
            // Set default URL
            const yourSheetUrl = 'https://docs.google.com/spreadsheets/d/1gqC4BV8oDNu-mD1v8x3kSq1W4ElsbNI_ymgA_xjiwQQ/edit?usp=sharing';
            document.getElementById('sheetUrl').value = yourSheetUrl;
            
            // Auto-load sheet data immediately
            autoLoadSheetData();
        });

        document.getElementById('connectBtn').addEventListener('click', () => {
            const url = document.getElementById('sheetUrl').value.trim();
            if (!url) {
                showStatus('error', 'Masukkan URL Google Sheets', '⚠️');
                return;
            }
            loadSheetData(url);
        });



        document.getElementById('refreshBtn').addEventListener('click', () => {
            const url = document.getElementById('sheetUrl').value.trim();
            if (url) {
                loadSheetData(url);
            } else {
                autoLoadSheetData();
            }
        });

        // Filter listeners
        ['requestTypeFilter', 'requestCategoryFilter', 'hospitalFilter', 'componentFilter', 'bloodTypeFilter', 'rhesusFilter', 'monthFilter', 'yearFilter'].forEach(id => {
            document.getElementById(id).addEventListener('change', () => {
                window.currentPage = 1;
                applyFilters();
            });
        });

        document.getElementById('resetFilter').addEventListener('click', () => {
            ['requestTypeFilter', 'requestCategoryFilter', 'hospitalFilter', 'componentFilter', 'bloodTypeFilter', 'rhesusFilter', 'monthFilter', 'yearFilter'].forEach(id => {
                document.getElementById(id).value = '';
            });
            window.currentPage = 1;
            filteredData = [...currentData];
            document.getElementById('filterInfo').textContent = `${filteredData.length}/${currentData.length} data`;
            updateDashboard();
        });

        document.getElementById('backToSetupBtn').addEventListener('click', () => {
            currentData = [];
            filteredData = [];
            
            Object.values(charts).forEach(chart => {
                if (chart && typeof chart.destroy === 'function') {
                    chart.destroy();
                }
            });
            charts = {};
            
            document.getElementById('dashboardContent').classList.add('hidden');
            document.getElementById('setupPanel').classList.remove('hidden');
        });
    </script>
<script>(function(){function c(){var b=a.contentDocument||a.contentWindow.document;if(b){var d=b.createElement('script');d.innerHTML="window.__CF$cv$params={r:'9d3c911897b0243f',t:'MTc3MjA3ODc1NS4wMDAwMDA='};var a=document.createElement('script');a.nonce='';a.src='/cdn-cgi/challenge-platform/scripts/jsd/main.js';document.getElementsByTagName('head')[0].appendChild(a);";b.getElementsByTagName('head')[0].appendChild(d)}}if(document.body){var a=document.createElement('iframe');a.height=1;a.width=1;a.style.position='absolute';a.style.top=0;a.style.left=0;a.style.border='none';a.style.visibility='hidden';document.body.appendChild(a);if('loading'!==document.readyState)c();else if(window.addEventListener)document.addEventListener('DOMContentLoaded',c);else{var e=document.onreadystatechange||function(){};document.onreadystatechange=function(b){e(b);'loading'!==document.readyState&&(document.onreadystatechange=e,c())}}}})();</script></body>
</html>
