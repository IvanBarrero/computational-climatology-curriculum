# 🟩 Block 1 Micro-Research: Multidimensional Grid Engineering & Andean Diurnal Thermal Cycles

* **Curriculum Position:** Year 1 — Semester 1, Block 1 (Weeks 1–6)
* **Primary Stack:** Python (`xarray`, `dask`, `numpy`, `netCDF4`, `cdsapi`, `matplotlib`)
* **Dataset:** Copernicus CDS ERA5 Hourly Reanalysis (`0.25° × 0.25°` native grid)
* **Spatial Domain:** Colombian Andes & Surrounding Lowlands (`4°S–13°N`, `79°W–66°W`)
* **Status:** 🔄 In Progress — Repository structured; awaiting data ingestion and vectorized pipeline implementation.

---

## 1. Scientific & Engineering Objective

This micro-research applies data-oriented array programming and Climate and Forecast (`CF-1.X`) metadata conventions to analyze the **diurnal (24-hour) surface air temperature cycle** across Colombia's complex Andean topography.

Rather than relying on slow iterative loops over latitude, longitude, and time dimensions, this pipeline uses lazy Dask chunking and vectorized Xarray operations to:
1. Extract a regional spatiotemporal subset over Colombia from global/continental ERA5 NetCDF4 archives.
2. Convert ERA5 surface geopotential ($\Phi$) into geometric model mesh elevation ($z$) to stratify grid cells into distinct Andean altitudinal belts.
3. Align UTC timestamps to **Colombia Local Solar Time (`COT = UTC-5`)** and compute vectorized hourly climatologies, diurnal temperature ranges ($\text{DTR}$), and environmental lapse rates across elevation tiers.

---

## 2. Physical & Mathematical Formulation

### Mesh Elevation from Surface Geopotential
ERA5 stores surface topography as surface geopotential $\Phi$ (variable `z`, in $\text{m}^2\,\text{s}^{-2}$). Geometric height above sea level is approximated using standard gravity ($g_0 = 9.80665\,\text{m}\,\text{s}^{-2}$):

$$z = \frac{\Phi}{g_0}$$

### Altitudinal Stratification Tiers
Grid cells within the Colombian bounding box are masked into three topographic regimes:
* **Lowlands (Tierras Calientes):** $z < 1000\text{ m}$ (Amazon, Orinoquía, Caribbean & Pacific plains)
* **Mid-Elevation Andes (Tierras Templadas/Frías):** $1000\text{ m} \le z \le 2500\text{ m}$ (Inter-Andean valleys & coffee belt slopes)
* **High Andes & Páramo:** $z > 2500\text{ m}$ (High cordillera crests & alpine ecosystems)

### Diurnal Temperature Range ($\text{DTR}$)
For each grid cell $(\phi, \lambda)$ and elevation tier $k$, the mean diurnal cycle $\overline{T}_k(h)$ is computed across local solar hours $h \in \{0, 1, \dots, 23\}$:

$$\text{DTR}_k = \max_{h} \overline{T}_k(h) - \min_{h} \overline{T}_k(h)$$

---

## 3. Directory Structure

```text
Block-01_Andes-Grid-ERA5/
├── README.md                  # Methodology, equations, and empirical results (this file)
├── data/                      # [Gitignored] Raw ERA5 NetCDF files (t2m, d2m, z)
├── figures/                   # Generated diurnal cycle and elevation-mask plots
├── notebooks/                 # Exploratory Dask chunking & metadata inspection notebooks
└── src/
    ├── download_era5.py       # [TODO] CDS API script to fetch Colombia hourly ERA5 subset
    └── process_andes_grid.py  # [TODO] Vectorized Xarray pipeline for diurnal & altitude analysis
```

---

## 4. Reproducibility & Execution Workflow

1. **Activate the repository environment** (from the repository root):
   ```bash
   conda env create -f ../../environment.yml
   conda activate climate-sci
   ```
2. **Configure Copernicus CDS Credentials:** Ensure `~/.cdsapirc` is configured with your personal Copernicus Climate Data Store API key.
3. **Fetch ERA5 Data:**
   ```bash
   python src/download_era5.py
   ```
4. **Run Vectorized Processing & Generate Figures:**
   ```bash
   python src/process_andes_grid.py
   ```

---

## 5. Key Results & Figures *(To Be Completed)*

> **[TODO — Complete after running `process_andes_grid.py`]**
> * Add summary table comparing mean temperature, peak warming hour (COT), and $\text{DTR}$ across the three elevation tiers.
> * Embed generated figures from `figures/`:
>   * `figures/andes_elevation_tiers_map.png` — Spatial distribution of ERA5 `0.25°` elevation masks over Colombia.
>   * `figures/diurnal_cycle_by_altitude.png` — 24-hour temperature and specific/relative humidity evolution by elevation belt.

---

## 6. Engineering & Physical Takeaways *(To Be Completed)*

> **[TODO — Document your observations upon completion]**
> * **Memory & Chunking Performance:** Document Dask chunk sizes used (`time`, `latitude`, `longitude`), peak RAM footprint, and execution speed vs. eager loading.
> * **Boundary Layer & Topographic Physics:** Discuss how diurnal amplitude ($\text{DTR}$) and convective cloud timing differ between humid lowlands and high-altitude Andean ridges on a `0.25°` (~28 km) smoothed reanalysis mesh.
