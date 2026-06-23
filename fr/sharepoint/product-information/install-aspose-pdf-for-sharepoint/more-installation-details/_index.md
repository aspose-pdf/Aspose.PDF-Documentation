---
title: Plus de détails sur l'installation
linktitle: Plus de détails sur l'installation
type: docs
weight: 30
url: /fr/sharepoint/more-installation-details/
lastmod: "2026-06-18"
description: Plus d'informations sur l'installation de l'API PDF SharePoint explique comment déployer, activer et désactiver celle-ci sur les collections de sites.
---

## **Déploiement**

{{% alert color="primary" %}}

**Aspose.PDF for SharePoint effectue les actions suivantes lors du déploiement**:
- Installez Aspose.PDF.SharePoint.dll dans le Global Assembly Cache et ajoutez l'entrée SafeControl au fichier web.config.
- Installez le manifeste de fonctionnalité et les autres fichiers nécessaires dans les répertoires appropriés.
- Enregistrez la fonctionnalité dans la base de données SharePoint et rendez‑la disponible pour l’activation à l’étendue de la fonctionnalité.

{{% /alert %}}


## **Activation**

{{% alert color="primary" %}}

**Aspose.PDF for SharePoint est fournie sous forme de fonctionnalité au niveau du site (collection de sites) et peut être activée et désactivée sur les collections de sites.**

{{% /alert %}}

{{% alert color="primary" %}}

Lors de l'activation, la fonctionnalité effectue quelques modifications dans le répertoire virtuel de l'application Web parente de la collection de sites : ajouter la page des paramètres de conversion au fichier sitemap. Copier les fichiers de ressources nécessaires dans le dossier App_GlobalResources du répertoire virtuel.

{{% /alert %}}
