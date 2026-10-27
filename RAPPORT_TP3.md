# Rapport de TP : Déploiement Cloud, Observabilité et Évaluation sous Charge d'une API d'Inférence IA

**Module :** Intelligence Artificielle & Cloud Engineering  
**Niveau :** Mastère 1 Data Engineer  
**Projet :** API d'Inférence Dermatologique (`DermaScan API`)  
**Date :** 26 octobre 2026  

---

## 1. Architecture Système & Déploiement PaaS

### 1.1 Composants d'Infrastructure
* **Plateforme Cloud :** Microsoft Azure (Abonnement Évaluation).
* **Groupe de Ressources :** `rg-dermascan-prod`.
* **Registre de Conteneurs :** Azure Container Registry (ACR) pour l'archivage et le versionnage des images Docker.
* **Service d'Hébergement :** Azure App Service (Plan **B1 - Basic**, 1 vCPU, 1.75 GB RAM, Linux).

### 1.2 Pipeline de Déploiement
* Conteneurisation de l'application basée sur une image Python (`python:3.10-slim`).
* Publication de l'image sur ACR et liaison continue avec l'App Service via Webhooks de déploiement.

---

## 2. Observabilité, Diagnostic d'Incident et Remédiation (Partie 4)

### 2.1 Description de l'Incident V1
Lors du premier déploiement, l'App Service est entré dans une boucle d'échecs de démarrage (*cold start failures*), rendant l'application indisponible.

```text
Container has finished running with exit code: 0.
Container exited with exit code 0 during startup after 0.6s.
Cancelling site startup. Site is blocked due to multiple cold start failures.