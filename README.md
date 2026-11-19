# 🌍 Computational Climatology, Telemetry, and Physical AI (4-Year Track)

![Status](https://img.shields.io/badge/Status-Active%20Research-2ea44f?style=flat-square)
![Focus](https://img.shields.io/badge/Region-Colombian%20Tropics%20%26%20Andes-007ec6?style=flat-square)
![Stack](https://img.shields.io/badge/Stack-Python%20%7C%20Julia%20%7C%20CliMA%20%7C%20PyTorch-blueviolet?style=flat-square)

A self-directed, master's-level research curriculum bridging **geophysical fluid dynamics, satellite remote sensing, Bayesian data assimilation, and physics-informed machine learning**, applied to Colombia's tropical climate complexity.

* **Current Milestone:** 🟡 **Year 1, Block 1** — Theory complete; executing ERA5 Andean diurnal thermal cycle micro-research.
* **Target Pace:** ~6 to 12 hours/week (Sequential 6-week theoretical/applied blocks + dedicated 16-week portfolio benchmarks).
* **Technological Paradigm:** **Python** for Geospatial Data Engineering, Cloud Remote Sensing, and Core AI; **Julia** for Fluid Mechanics, GPU Numerical Simulation, and Bayesian Inversion.

---

## 🧭 Repository Architecture (Hybrid Portfolio Strategy)

This repository houses all **18 six-week micro-research blocks**. Major 16-week integrative benchmarks and the final manuscript live in dedicated standalone repositories:

| Track | Scope | Repository | Status |
| :--- | :--- | :--- | :--- |
| **Core Curriculum (Blocks 1–18)** | Modular scripts, numerical solvers, & technical reports | **This Repository** | 🟢 In Progress (Block 1) |
| **Year 1 Capstone (Weeks 37–52)** | Regional Driver of Climate Anomalies (Colombia EOF/AR1) | `andes-climate-diagnostics` *(Planned)* | ⚪ Upcoming |
| **Year 2 Capstone (Weeks 89–104)** | La Guajira Coupled Ocean-Atmosphere GPU Sandbox | `guajira-upwelling-coupling` *(Planned)* | ⚪ Upcoming |
| **Year 3 Capstone (Weeks 129–144)** | Extreme Event Satellite Pipeline & Attribution Tracker | `extreme-event-attribution` *(Planned)* | ⚪ Upcoming |
| **Year 4 Master Work (Weeks 157–208)** | Coupled Regional CliMA + PINN Emulator & AMS Preprint | `colombia-regional-clima-pinn` *(Planned)* | ⚪ Upcoming |

---

## 🗓️ YEAR 1: Geospatial Data Engineering & Physical Foundations (Python & Statistics)

### 📊 Semester 1: Continental Grid Structures and the Colombian Andes

- [ ] 🟩 **[Block 1 (Weeks 1–6): Data Engineering — The Multidimensional Grid](./Year-1_Geospatial-Foundations/Block-01_Andes-Grid-ERA5)** *(Theory ✅ | Micro-Research 🔄)*
  * **Focus:** Spatiotemporal tensors, CF-1.X conventions, NetCDF4/GRIB binary structures, and lazy Dask evaluation.
  * **Colombian Micro-Research:** Vectorized extraction of Copernicus CDS ERA5 grids over the Colombian Andes (`4°S–13°N, 79°W–66°W`) to isolate diurnal temperature cycles by mesh altitude.
  <details>
  <summary><b>View Detailed Weekly Schedule & Resources</b></summary>

  * **Primary Resources:** [Project Pythia Foundations](https://foundations.projectpythia.org/) (Core Scientific Python, NumPy Advanced, Xarray Deep Dive), NetCDF4 Python Docs, CF Conventions.
  * **Weeks 1–2:** Memory Architecture with NumPy & Vectorized Operations (`ndarray` pointers, strides, C vs. Fortran memory locality, boolean masking, broadcasting).
  * **Weeks 3–4:** Deserialization of Scientific Formats (NetCDF4/HDF5 vs. GRIB, block chunking, scale/offset packing).
  * **Weeks 5–6:** High-Level Abstraction with Xarray & Dask (`.sel()`, `.isel()`, `.groupby()`, `.resample()`).
  </details>

- [ ] 🟦 **[Block 2 (Weeks 7–12): Physical Science — Planetary Energy Balance & Cloud Microphysics](./Year-1_Geospatial-Foundations/Block-02_Radiative-Balance)**
  * **Focus:** Atmospheric thermodynamics, radiative transfer, 1D convective adjustment, and Kessler warm-rain microphysics.
  * **Colombian Micro-Research:** Markdown technical report with equations comparing Hartmann's theoretical radiative balance against NASA CERES satellite fluxes over the Colombian ITCZ.
  <details>
  <summary><b>View Detailed Weekly Schedule & Resources</b></summary>

  * **Primary Resources:** Marshall & Plumb (Ch. 3, 4), Hartmann (Ch. 1–3), Holton (Ch. 1, 9).
  * **Weeks 7–8:** Atmospheric Structure & Energy Conservation (Troposphere/stratosphere profiles, solar constant, albedo, Stefan-Boltzmann & Wien laws).
  * **Weeks 9–10:** Radiative Transfer, Pressure Dynamics & Cloud Microphysics (Greenhouse molecular profiles, Kessler parameterization, hydrostatic equation, geopotential thickness).
  * **Weeks 11–12:** 1D Radiative-Convective Numerical Modeling (Dry/moist adiabatic lapse rates, $N$-layer linear solver in SciPy, $CO_2$ doubling simulation).
  </details>

- [ ] 🟪 **[Block 3 (Weeks 13–18): Advanced Statistics — Matrix Methods and Principal Components](./Year-1_Geospatial-Foundations/Block-03_EOFs-Statistics)**
  * **Focus:** Multivariate linear algebra, spatial covariance matrices, Empirical Orthogonal Functions (EOFs), and Singular Value Decomposition (SVD).
  * **Colombian Micro-Research:** Seasonal cycle removal, $\sqrt{\cos(\phi)}$ area weighting, and EOF/PC extraction on NOAA ERSST v5 to isolate ENSO variability and test for secular trends.
  <details>
  <summary><b>View Detailed Weekly Schedule & Resources</b></summary>

  * **Primary Resources:** Daniel Wilks, *Statistical Methods in the Atmospheric Sciences* (Ch. 4, 12); `eofs` Python library.
  * **Weeks 13–14:** Multivariate Statistics on Gridded Fields (Spatiotemporal matrix layouts, sample covariance/correlation matrices, eigen-decomposition).
  * **Weeks 15–16:** Theory of Empirical Orthogonal Functions (Orthogonality constraints, North's Rule of Thumb, latitude area-weight correction).
  * **Weeks 17–18:** Numerical Decomposition with `eofs` (SVD over Xarray objects, loading maps, standardized PCs, variance fractions).
  </details>

---

### 🌊 Semester 2: Fluid Dynamics and Geoprocessing

- [ ] 🟩 **[Block 4 (Weeks 19–24): Data Engineering — Spatial Cartography and Geoprocessing](./Year-1_Geospatial-Foundations/Block-04_Cartography-Geoprocessing)**
  * **Focus:** Spherical-to-planar map projections, Coordinate Reference Systems (CRS), vector-raster masking, and spatial interpolation.
  * **Colombian Micro-Research:** Automated cartographic atlas mapping spatial correlations between thermal anomalies and Copernicus Land Cover changes across Colombian hydrographic basins.
  <details>
  <summary><b>View Detailed Weekly Schedule & Resources</b></summary>

  * **Primary Resources:** [Project Pythia Foundations](https://foundations.pythia.cc/landing.html) (Cartopy & Visualization), GeoPandas, Shapely, Rasterio.
  * **Weeks 19–20:** Cartopy Foundations & Projection Systems (Orthographic, PlateCarrée, Mercator, Lambert Conformal, dynamic CRS transforms).
  * **Weeks 21–22:** Vector-Raster Superimposition & Geographic Masking (Watershed shapefiles in GeoPandas, indexed Xarray masks).
  * **Weeks 23–24:** Non-Uniform Observational Data Processing (IDW, bilinear, and Kriging interpolation; sparse station filtering emulating IDEAM formats).
  </details>

- [ ] 🟦 **[Block 5 (Weeks 25–30): Physical Science — Atmosphere/Ocean Dynamics & Surface Feedbacks](./Year-1_Geospatial-Foundations/Block-05_Geophysical-Dynamics)**
  * **Focus:** Rotating Navier-Stokes equations, geostrophic and thermal wind balances, Ekman transport, and soil moisture feedback frameworks.
  * **Colombian Micro-Research:** Georeferenced error analysis of the geostrophic wind approximation near the Colombian ITCZ ($f 	o 0$) vs. mid-latitudes using ERA5 wind vectors, paired with continental surface heat flux evaluation.
  <details>
  <summary><b>View Detailed Weekly Schedule & Resources</b></summary>

  * **Primary Resources:** Marshall & Plumb (Ch. 5–7), Hartmann (Ch. 4, 6, 7), Holton (Ch. 2, 3, 5).
  * **Weeks 25–26:** Atmospheric Kinematics & Fundamental Forces (Rotating frame tensor derivations, Coriolis in spherical coordinates, substantial derivative).
  * **Weeks 27–28:** General Circulation, Geostrophic & Thermal Wind Balance (Cyclostrophic/gradient wind, vertical shear, Hadley/Ferrel/Polar cells).
  * **Weeks 29–30:** Ocean Dynamics & Land Surface Interface (Ekman pumping, westward intensification/$eta$-effect, Budyko curve & bucket soil moisture models).
  </details>

- [ ] 🟪 **[Block 6 (Weeks 31–36): Advanced Statistics — Time Series and Persistence](./Year-1_Geospatial-Foundations/Block-06_Time-Series-Persistence)**
  * **Focus:** Stochastic climate processes, AR(1) red noise, effective degrees of freedom, forecast skill scores, and Monte Carlo resampling.
  * **Colombian Micro-Research:** Extreme drought attribution script testing whether ENSO-driven drought persistence over Colombia exceeds centennial natural variability after correcting degrees of freedom for autocorrelation.
  <details>
  <summary><b>View Detailed Weekly Schedule & Resources</b></summary>

  * **Primary Resources:** Daniel Wilks, *Statistical Methods in the Atmospheric Sciences* (Ch. 9, 10).
  * **Weeks 31–32:** Stochastic Processes & Persistence Models (Stationarity, ACF, AR(1) red noise, Markov chains for wet/dry spells, effective sample size).
  * **Weeks 33–34:** Forecast Verification Methods (Contingency tables, Heidke Skill Score, ETS, RMSE, MAE, Brier Score, reliability diagrams).
  * **Weeks 35–36:** Adjusted Hypothesis Testing & Monte Carlo Simulation (Autocorrelation-corrected test statistics, bootstrapping for extreme thresholds).
  </details>

> **📊 Year 1 Portfolio Milestone (Weeks 37–52): The Regional Driver of Climate Anomalies (Colombia Case Study)**
> Unified Python diagnostic environment loading ERA5 fluxes, removing seasonal cycles, correcting degrees of freedom for AR(1) red noise, executing EOFs, and deploying interactive topography-superimposed loading maps with Monte Carlo uncertainty bands.

---

## 🗓️ YEAR 2: Scientific Computing, Numerical Fluids, & Hardware-Accelerated Modeling (Julia)

### 💻 Semester 3: Accelerated Thinking and Numerical Fluid Dynamics

- [ ] 🟩 **[Block 7 (Weeks 53–58): Data Engineering — Cloud Telemetry Foundations in Julia](./Year-2_Julia-Numerical-Fluids/Block-07_Cloud-Telemetry-Julia)**
  * **Focus:** Spectroscopy, bitwise cloud masking, and cloud-native Zarr/COG streaming via STAC catalogs in Julia.
  * **Colombian Micro-Research:** Parallelized Julia pipeline streaming MODIS/Sentinel Zarr arrays to strip cloud noise and quantify decadal retreat rates of Colombian Andean glaciers via NDVI/NDWI.
  <details>
  <summary><b>View Detailed Weekly Schedule & Resources</b></summary>

  * **Primary Resources:** [NASA ARSET](https://appliedsciences.nasa.gov/what-we-do/capacity-building/arset), `Zarr.jl`, `NCDatasets.jl`, `rioxarray` / STAC specs.
  * **Weeks 53–54:** Spectroscopy & Reflectance Signatures (Rayleigh/Mie scattering, spectral curves of ice/vegetation/water, NDVI/NDWI).
  * **Weeks 55–56:** Cloud Masking Logic & QA Flags (Bitwise operations on raw quality assurance bitmasks).
  * **Weeks 57–58:** Cloud-Native Storage Engineering (Chunked Zarr asynchronous I/O, STAC catalog queries).
  </details>

- [ ] 🟪 **[Block 8 (Weeks 59–64): Scientific Computing — Computational Thinking & Stability in Julia](./Year-2_Julia-Numerical-Fluids/Block-08_Julia-Type-Stability)**
  * **Focus:** Multiple dispatch for physical laws, parametric type systems, LLVM compilation, and zero-allocation optimization.
  * **Colombian Micro-Research:** Replicate the Block 2 1D radiative balance model in `Pluto.jl` parameterized for the Colombian tropics, benchmarking type stability with `@code_warntype`.
  <details>
  <summary><b>View Detailed Weekly Schedule & Resources</b></summary>

  * **Primary Resources:** MIT 18.S191 (*Introduction to Computational Thinking with Julia*), Julia Performance Tips.
  * **Weeks 59–60:** Julia Paradigm & Scientific Syntax (Array mutability, LLVM lowering, multiple dispatch vs. OOP).
  * **Weeks 61–62:** Simulation of Chaotic Systems & Heat Transfer PDEs (Lorenz attractor and diffusion PDEs in reactive `Pluto.jl` notebooks).
  * **Weeks 63–64:** Compiler Auditing & Code Optimization (`@code_warntype`, eliminating GC overhead and type instabilities).
  </details>

- [ ] 🟦 **[Block 9 (Weeks 65–70): Physical Science — Computational Fluid Dynamics in Julia](./Year-2_Julia-Numerical-Fluids/Block-09_CFD-Julia)**
  * **Focus:** Finite-difference discretization, Von Neumann stability analysis, CFL thresholds, and multi-threaded mesh slicing.
  * **Colombian Micro-Research:** Multi-threaded 1D thermal advection simulator over a slanted Andean slope validating CFL stability thresholds and CPU thread scaling.
  <details>
  <summary><b>View Detailed Weekly Schedule & Resources</b></summary>

  * **Primary Resources:** Dale Durran, *Numerical Methods for Fluid Dynamics*; `DifferentialEquations.jl`.
  * **Weeks 65–66:** Numerical Discretization & Stability (Forward/backward/centered finite differences, truncation error, Von Neumann stability, CFL condition).
  * **Weeks 67–68:** 1D/2D Advection Equations in Julia (Upwind, Leapfrog, Lax-Wendroff schemes; zero-allocation `@views` and `.=` broadcasting).
  * **Weeks 69–70:** Multi-threading & Distributed Parallelism (Spatial locality, domain decomposition with ghost cells via `Distributed.jl` / native threads).
  </details>

---

### 📊 Semester 4: Numerical Simulation and Next-Generation Models

- [ ] 🟩 **[Block 10 (Weeks 71–76): Physical Science — Tropical Dynamics & CliMA Core Structures](./Year-2_Julia-Numerical-Fluids/Block-10_Tropical-Dynamics-ClimaCore)**
  * **Focus:** Equatorial Kelvin/Rossby waves, MJO dynamics, discontinuous spectral elements in `ClimaCore.jl`, and tropical glacier surface energy balance.
  * **Colombian Micro-Research:** `ClimaCore.jl` columnar model parameterized for the Colombian tropical troposphere coupled to a high-altitude ice interface to simulate perturbation-driven glacier ablation.
  <details>
  <summary><b>View Detailed Weekly Schedule & Resources</b></summary>

  * **Primary Resources:** Holton (Ch. 11), Marshall & Plumb (Ch. 8, 11), [ClimaCore.jl Docs](https://github.com/CliMA/ClimaCore.jl).
  * **Weeks 71–72:** Tropical Climate Physics & General Circulation (Equatorial Kelvin/Rossby waves, MJO-topography coupling).
  * **Weeks 73–74:** Deep Convection & Spherical Grid Abstractions (ITCZ convective towers, spectral element discretization in `ClimaCore.jl`).
  * **Weeks 75–76:** Global Model Architecture & Cryosphere Thermodynamics (Dycore-physics coupling, tropical glacier ablation & energy balance equations).
  </details>

- [ ] 🟦 **[Block 11 (Weeks 77–82): Physical Science — Boundary Fluid Dynamics (Oceananigans on GPUs)](./Year-2_Julia-Numerical-Fluids/Block-11_Oceananigans-GPU)**
  * **Focus:** Non-hydrostatic Boussinesq equations, boundary-layer turbulence, coastal Ekman upwelling, and GPU kernel programming.
  * **Colombian Micro-Research:** 3D `Oceananigans.jl` simulation of wind-driven coastal upwelling off the La Guajira peninsula benchmarking CPU vs. `architecture = GPU()` runtimes.
  <details>
  <summary><b>View Detailed Weekly Schedule & Resources</b></summary>

  * **Primary Resources:** Hartmann (Ch. 4), Marshall & Plumb (Ch. 9, 10), [Oceananigans.jl Docs](https://clima.github.io/OceananigansDocumentation/stable/).
  * **Weeks 77–78:** Non-Hydrostatic Boussinesq Equations & Boundary Layer (Mixing-length theory, convective mixing, ocean stratification).
  * **Weeks 79–80:** Wind-Driven Ocean Dynamics & GPU Computing (Ekman divergence, `KernelAbstractions.jl`, GPU thread/shared memory mapping).
  * **Weeks 81–82:** Configuring 3D Domains in Oceananigans (Buoyancy gradients, wind stress `FluxBoundaryCondition`).
  </details>

- [ ] 🟪 **[Block 12 (Weeks 83–88): Advanced Statistics — Data Assimilation and Bayesian Inversion](./Year-2_Julia-Numerical-Fluids/Block-12_Bayesian-Inversion-EKP)**
  * **Focus:** Continuous Bayes' theorem, Ensemble Kalman Filters (EnKF), and derivative-free Ensemble Kalman Inversion (EKI).
  * **Colombian Micro-Research:** Calibration pipeline using `EnsembleKalmanProcesses.jl` to tune emissivity and heat-transfer parameters in the Block 8 thermal model against NASA CERES observations over Colombia.
  <details>
  <summary><b>View Detailed Weekly Schedule & Resources</b></summary>

  * **Primary Resources:** Oliver Olivera, *Data Assimilation: A Mathematical Introduction*; [EnsembleKalmanProcesses.jl Docs](https://clima.github.io/EnsembleKalmanProcesses.jl/dev/).
  * **Weeks 83–84:** The Data Assimilation Cycle (Forecast/analysis/update steps, 3D-Var/4D-Var vs. ensemble methods).
  * **Weeks 85–86:** The Ensemble Kalman Filter & Inversion (Background error covariance estimation, EKI for unobservable physical parameters).
  * **Weeks 87–88:** Automated Parameter Calibration in CliMA (Coupling black-box forward models with stochastic ensemble optimization).
  </details>

> **🛰️ Year 2 Portfolio Benchmark (Weeks 89–104): The Data-Coupled Tropical Ocean-Atmosphere Interface (La Guajira Upwelling Sandbox)**
> Sequential one-way NetCDF/Zarr file-coupled regional framework in Julia: `ClimaCore.jl` (forced by NASA CERES) exports surface wind stress ($	au$) and net heat flux ($Q_{net}$) into a GPU-accelerated 3D `Oceananigans.jl` coastal upwelling model, calibrated end-to-end via `EnsembleKalmanProcesses.jl` (`CATKEVerticalDiffusivity`).

---

## 🗓️ YEAR 3: Global Cycles, Cloud Ecosystems, Biogeochemistry, & Macro Data Systems (Python)

### 💻 Semester 5: Planet-Scale Observations and Biological/Chemical Couplings

- [ ] 🟩 **[Block 13 (Weeks 105–110): Data Engineering — Raw Spectral Imagery & Satellite Remote Sensing](./Year-3_Global-Biogeochemistry/Block-13_Satellite-Remote-Sensing)**
  * **Focus:** Geostationary vs. polar orbital geometry, radiative calibration, bitwise cloud clearing, and HDF5/GeoTIFF extraction.
  * **Deliverable:** Automated pipeline stripping cloud contamination from satellite imagery to isolate tropical ocean color or cryosphere layers.
  <details>
  <summary><b>View Detailed Weekly Schedule & Resources</b></summary>

  * **Primary Resources:** [NASA ARSET](https://appliedsciences.nasa.gov/what-we-do/capacity-building/arset), Marshall & Plumb (Ch. 2), `rioxarray`, `rasterio`.
  * **Weeks 105–106:** Satellite Orbits & Electromagnetic Bands (Geostationary vs. polar geometry, sensor calibration).
  * **Weeks 107–108:** Cloud-Masking & QA Flags (Bitwise pixel evaluations on MODIS/Sentinel arrays).
  * **Weeks 109–110:** HDF5 & GeoTIFF Pipelines (`rioxarray`/`rasterio` high-throughput extraction).
  </details>

- [ ] 🟦 **[Block 14 (Weeks 111–116): Physical Science — Internal Climate Oscillations & Macro Feedbacks](./Year-3_Global-Biogeochemistry/Block-14_Climate-Oscillations)**
  * **Focus:** Coupled ocean-atmosphere modes (ENSO, PDO, NAO), equatorial beta-plane wave mechanics, and IPCC AR6 radiative forcing feedbacks.
  * **Colombian Micro-Research:** Scientific report evaluating historical spatial teleconnections between deep ocean thermal trends and atmospheric oscillation indices over the Colombian Pacific domain.
  <details>
  <summary><b>View Detailed Weekly Schedule & Resources</b></summary>

  * **Primary Resources:** Hartmann (Ch. 10, 11), Holton (Ch. 11), Marshall & Plumb (Ch. 12), IPCC WGI AR6.
  * **Weeks 111–112:** Natural Climate Variations (ENSO, PDO, NAO coupled dynamics).
  * **Weeks 113–114:** Equatorial Beta-Plane Wave Equations (Kelvin & Rossby wave propagation triggering El Niño events).
  * **Weeks 115–116:** Anthropogenic Climate Change (Radiative forcing, climate sensitivity feedbacks, secular trend attribution).
  </details>

- [ ] 🟩 **[Block 15 (Weeks 117–122): Data Engineering — Massive Cloud Ecosystems & CMIP6 Projections](./Year-3_Global-Biogeochemistry/Block-15_CMIP6-Cloud-Ecosystems)**
  * **Focus:** Pangeo cloud archives, Planetary Computer STAC APIs, Aerosol Optical Depth (AOD), CMIP6 SSP scenarios, and Climate Data Operators (CDO).
  * **Colombian Micro-Research:** Cloud-querying Python script extracting 5 CMIP6 models across SSP1-2.6, SSP2-4.5, and SSP5-8.5, regridded via CDO onto a uniform northern South American grid.
  <details>
  <summary><b>View Detailed Weekly Schedule & Resources</b></summary>

  * **Primary Resources:** [Pangeo CMIP6 Archive](https://pangeo.io/), [Microsoft Planetary Computer](https://planetarycomputer.microsoft.com/), CDO CLI, Dask.
  * **Weeks 117–118:** Cloud-Optimized Formats & Atmospheric Chemistry (Zarr/COG STAC queries, Aerosol Optical Depth & biomass burning footprints).
  * **Weeks 119–120:** CMIP6 Emission Scenarios (SSP1-2.6, SSP2-4.5, SSP5-8.5 multi-model ensembles).
  * **Weeks 121–122:** Climate Data Operators (CDO) & Distributed Dask Reductions (Grid regridding, subsetting, parallel multi-model statistics).
  </details>

- [ ] 🟦 **[Block 16 (Weeks 123–128): Physical Science — Ocean Biogeochemistry, Aerosols, and Carbon Cycles](./Year-3_Global-Biogeochemistry/Block-16_Ocean-Biogeochemistry-TEOS10)**
  * **Focus:** Solubility/biological carbon pumps, carbonate buffer chemistry, aerosol scattering, and TEOS-10 seawater thermodynamics.
  * **Deliverable:** Standalone program computing 20-year local ocean density trends and carbonate saturation curves using the TEOS-10 Gibbs function library.
  <details>
  <summary><b>View Detailed Weekly Schedule & Resources</b></summary>

  * **Primary Resources:** Hartmann (Ch. 5), Marshall & Plumb (Ch. 11), [TEOS-10 Standard Library](http://www.teos-10.org/).
  * **Weeks 123–124:** Global Carbon Cycle & Aerosol Scattering (Solubility/biological pumps, Rayleigh/Mie aerosol profiles).
  * **Weeks 125–126:** Ocean Acidification & Thermal Expansion (Carbonate buffer equilibria, steric sea-level dynamics).
  * **Weeks 127–128:** TEOS-10 Seawater Thermodynamics (Absolute Salinity $S_A$, Conservative Temperature, hydrostatic density profiles).
  </details>

> **🛰️ Year 3 Portfolio Benchmark (Weeks 129–144): The Extreme Event Satellite Pipeline & Attribution Tracker**
> Automated Python pipeline pairing Pangeo CMIP6 future projections with real-time MODIS/Sentinel cloud Zarr streams via Planetary Computer APIs, using extreme value statistics to attribute marine heatwaves or cryosphere anomalies to internal variability (ENSO) vs. anthropogenic forcing.

---

## 🗓️ YEAR 4: Advanced Climate Artificial Intelligence & The AMS Master Work (Python)

### 💻 Semester 7: Physics-Informed Deep Learning & Advanced Planetary Meshes

- [ ] 🟪 **[Block 17 (Weeks 145–150): Advanced Statistics — Climate Machine Learning & Neural PDE Physics](./Year-4_Physical-AI/Block-17_Climate-ML-PINNs)**
  * **Focus:** Spatiotemporal cross-validation (preventing data leakage), Physics-Informed Neural Networks (PINNs), and conservation-constrained loss functions.
  * **Deliverable:** PyTorch spatiotemporal SST prediction model whose multi-task loss penalizes unphysical spikes and energy/mass conservation violations.
  <details>
  <summary><b>View Detailed Weekly Schedule & Resources</b></summary>

  * **Primary Resources:** PyTorch / TensorFlow, Scikit-Learn spatial validation frameworks, SciML PINN literature.
  * **Weeks 145–146:** Spatial ML & Leakage-Free Cross-Validation (Blocked spatial/temporal splits for autocorrelated climate fields).
  * **Weeks 147–148:** Physics-Informed Neural Networks (PINNs) (Embedding PDE residuals—mass, energy, momentum conservation—into loss functions).
  * **Weeks 149–150:** Spatiotemporal Deep Learning Architectures (Convolutional/tensor networks in PyTorch for anomaly forecasting).
  </details>

- [ ] 🟪 **[Block 18 (Weeks 151–156): Advanced Statistics — Global AI Weather Systems & Statistical Downscaling](./Year-4_Physical-AI/Block-18_AI-Weather-Downscaling)**
  * **Focus:** Spherical Graph Neural Networks (GraphCast, Pangu-Weather), icosahedral meshes, and topographic quantile mapping downscaling.
  * **Colombian Micro-Research:** High-fidelity downscaling pipeline translating coarse global temperature grids into high-resolution regional fields adjusted for Colombian Andean topography.
  <details>
  <summary><b>View Detailed Weekly Schedule & Resources</b></summary>

  * **Primary Resources:** GraphCast / Pangu-Weather architectural papers, empirical quantile mapping & topographic downscaling literature.
  * **Weeks 151–152:** Spherical Graph Neural Networks (GNNs) (Icosahedral planetary meshes avoiding polar singularities).
  * **Weeks 153–154:** Statistical Downscaling & Quantile Mapping (Bias correction and topographic elevation sharpening).
  * **Weeks 155–156:** Hybrid Numerical vs. AI Benchmarks (Accuracy, physical consistency, and compute/energy trade-offs).
  </details>

---

### 📊 Semester 8: The Grand Capstone Project and Portfolio Delivery

> **👑 Weeks 157–208: FINAL MASTER PROJECT — Accelerated Dynamic Modeling, Inverse Calibration, and AI Emulation of the Colombian Regional Climate**
> * **Dynamic Core (Julia):** 3D regional simulation in `ClimaAtmos.jl` / `Oceananigans.jl` configured over Colombia's Andean topography and Pacific/Caribbean coastlines with GPU acceleration.
> * **Inverse Calibration:** Automated `EnsembleKalmanProcesses.jl` assimilation loop tuning model parameters against cleaned NASA CERES/MODIS anomalies and cryosphere/aerosol feedbacks.
> * **AI Emulation & Downscaling:** PyTorch PINN emulator / downscaling pipeline projecting CMIP6 scenarios onto the calibrated regional domain.
> * **Deliverables:** Reproducible multi-language repository + peer-review-ready research preprint formatted to **American Meteorological Society (AMS)** guidelines.