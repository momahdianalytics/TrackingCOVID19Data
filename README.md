# 🦠 COVID-19 Analytics Dashboard

A modern, dark-themed desktop application built with **Python**, **PySide6 (Qt for Python)**, **Matplotlib**, and **Seaborn** to visualize and explore global COVID-19 pandemic data.

---

## ✨ Features

- **Global KPI Overview**: Real-time summary cards highlighting Total Confirmed, Deaths, Recovered, and Active cases.
- **Interactive Visualizations**:
  - **Tab 1: Overview & Distribution**
    - Top 10 countries by confirmed cases.
    - Regional distribution by WHO Region.
    - Top 10 mortality figures.
    - Formatted tabular data summary.
  - **Tab 2: Correlations & Active Cases**
    - Scatter plot analysis: Recovered vs. Deaths across WHO Regions.
    - Scatter plot analysis: Confirmed vs. Active cases.
    - Top 10 active case rankings and detailed data breakdown.
- **Modern Dark UI**: Fully customized stylesheet using Tailwind-inspired palettes (Slate & Sky).
- **Reusable Component Architecture**: Declarative layout wrappers (`row`, `col`, `card`, `table_plot`, `kpi_card`) built on top of Qt widgets.
- **Robust Error Handling & Logging**: Integrated with `loguru` for structured debugging and file logging.

---

## 📁 Project Structure

```text
TrackingCOVID19Data/
├── data/
│   ├── country_wise_latest.csv   # Dataset containing country-level metrics
│   └── logo.ico                  # Application window and executable icon
├── logs/                         # Application runtime logs
├── pages/
│   ├── __init__.py
│   ├── tab_1.py                  # Overview metrics, charts, and table
│   └── tab_2.py                  # Correlation plots and active cases view
├── widgets/
│   ├── __init__.py
│   ├── button.py                 # Styled QPushButton helper
│   ├── card.py                   # Reusable container frame with header/subtitles
│   ├── col.py                    # Vertical layout wrapper (QVBoxLayout/QWidget)
│   ├── kpi_card.py               # Summary metric indicator cards
│   ├── plot.py                   # Seaborn/Matplotlib Qt canvas integration
│   ├── row.py                    # Horizontal layout wrapper (QHBoxLayout/QWidget)
│   ├── table.py                  # Formatted QTableWidget wrapper for pandas DataFrames
│   └── table_plot.py             # Combined chart + table component
├── df.py                         # Data loading and preprocessing pipelines
├── main.py                       # Main application entrypoint & window configuration
├── utils.py                      # CSS style builders, constants, and path resolvers
├── requirements.txt              # Project dependencies
├── output.json                   # Configuration preset for auto-py-to-exe
└── README.md                     # Documentation
```

---

## 🚀 Getting Started
### Prerequisites
 - Python 3.10+

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/TrackingCOVID19Data.git
cd TrackingCOVID19Data
```

### 2. Set Up a Virtual Environment

#### Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

#### macOS / Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Application
```bash
python main.py
```

---

## 📦 Building the Executable (.exe)
The repository includes an output.json configuration file pre-configured for auto-py-to-exe / PyInstaller.

### Using PyInstaller Directly
Run the following command from the root directory:

```bash
pyinstaller --noconfirm --onefile --windowed --icon "data/logo.ico" --name "TrackingCOVID19Data" --add-data "data;data/" main.py
```

### Using auto-py-to-exe GUI
#### Launch the tool:

```bash
auto-py-to-exe
```

Click **Import Config** at the bottom and select `output.json`, then click **Convert .py to .exe**.

---

## 🛠️ Built With
- PySide6 – Qt GUI toolkit for Python.
- Pandas – Data manipulation and analysis.
- Matplotlib & Seaborn – Statistical data visualization.
- Loguru – Logging utility.

---

## 📄 License
This project is open-source and available under the MIT License.