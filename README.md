# GeoShield Sentinel 🌍🛰️

## Description
**GeoShield Sentinel** is an advanced landslide prediction and monitoring application designed to support India's disaster risk reduction efforts in vulnerable and hilly regions.

The platform leverages:
- **Earth Observation (EO)** satellite data (Sentinel-1, Sentinel-2, DEM)
- **Machine Learning** models
- **Real-time weather and soil data**

to provide **scalable**, **interpretable**, and **real-time landslide vulnerability forecasts**. The tool enables proactive governance, timely alerts, and improved resilience of communities.

---

## Tech Stack

### Backend
- **Python 3.10**
- **Flask** API
- **Scikit-learn** (ML pipeline)
- **GDAL / Rasterio** (geospatial data processing)

### Frontend
- **React.js** with **Mapbox GL JS** for dynamic map visualisation
- **D3.js** for charting
- REST API calls to backend

### Machine Learning Model
- **Random Forest Classifier** with hyperparameter tuning
- Features used:
  - **Slope** (derived from DEM)
  - **Rainfall data** (IMD)
  - **Land Use/Land Cover** (Sentinel-2)
  - **NDVI** (Sentinel-2)
  - **Soil Moisture** (Sentinel-1)
  - **Past Landslide Events** (Survey of India / Geological Survey of India)
  - **Population density** (Census data)
  
Accuracy (Validation F1 Score): **0.89**

---

## Data Sources

- **Sentinel-1**: SAR data for soil moisture  
- **Sentinel-2**: Multispectral data for NDVI, LULC  
- **Copernicus DEM**: 10m resolution Digital Elevation Model  
- **IMD Rainfall Data**: Daily precipitation  
- **Census of India**: Population data  
- **GSI Landslide Inventory**  

---

## Setup Instructions

### Prerequisites
- Python 3.8 or higher
- Node.js 14.x or higher
- npm (Node Package Manager)
- Git installed on your system

### Installation Steps

#### 1️⃣ Clone the Repository
```bash
git clone https://github.com/Prahlad-paradox-2025/GeoShield-SentinelV0.15.git
cd GeoShield-SentinelV0.15