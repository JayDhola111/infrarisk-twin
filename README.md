# InfraRisk Twin

InfraRisk Twin is an AI-assisted geospatial platform for analysing the climate resilience of urban infrastructure.

The project combines public 3D building models, heavy-rain hazard maps, infiltration data and weather observations to identify exposed buildings and prioritise infrastructure for further inspection.

## Problem

Infrastructure-related data is often distributed across different GIS files, 3D models, databases and technical documents.

This makes it difficult to quickly answer questions such as:

- Which buildings are most exposed to heavy rainfall?
- Which access routes may be affected?
- Which infrastructure assets should be inspected first?
- Which adaptation measures are supported by technical guidelines?

## Project objectives

- Integrate 3D building, GIS, weather and environmental datasets
- Store and analyse spatial data using PostgreSQL and PostGIS
- Calculate transparent infrastructure-risk indicators
- Orchestrate analytical tools using LangGraph
- Retrieve technical recommendations using RAG
- Visualise buildings, hazard zones and risk results
- Generate traceable reports containing sources and assumptions

## Planned architecture

1. Data ingestion and validation
2. Geospatial transformation and storage
3. Spatial risk analysis
4. Risk prioritisation
5. LangGraph workflow orchestration
6. RAG-based guideline retrieval
7. FastAPI backend
8. React and TypeScript frontend

## Technology stack

- Python
- GeoPandas
- PostgreSQL/PostGIS
- FastAPI
- CityGML
- LangGraph
- RAG
- React
- TypeScript
- Docker
- Git

## Data sources

The prototype uses publicly available datasets, including:

- Hamburg LoD2 3D building models
- Hamburg heavy-rain hazard data
- Hamburg infiltration-potential data
- Deutscher Wetterdienst weather observations

The repository does not redistribute large source datasets. Download instructions and source references will be documented separately.

## Current status

Active development.

### Initial work

- Project architecture defined
- Public data sources identified
- Data-ingestion module prepared

### Next steps

- Implement the first geospatial ingestion pipeline
- Load a selected Hamburg area
- Add GeoPandas spatial analysis
- Configure PostgreSQL/PostGIS
- Implement risk scoring
- Add LangGraph orchestration
- Add RAG retrieval
- Develop the web interface

## Important limitation

This project is a decision-support prototype. Its outputs are not certified engineering assessments and require professional validation before operational use.
