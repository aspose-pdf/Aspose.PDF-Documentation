---
title: Plus de détails d'installation
linktitle: Plus de détails d'installation
type: docs
weight: 30
url: /fr/sharepoint/more-installation-details/
lastmod: "2020-12-16"
description: Plus d'informations sur l'installation de l'API PDF SharePoint explique comment la déployer, l'activer et la désactiver sur les collections de sites.
---

## Déploiement

{{% alert color="primary" %}}

**Aspose.PDF for SharePoint effectue les actions suivantes pendant le déploiement :**

- Installez Aspose.PDF.SharePoint.dll dans Global Assembly Cache et ajoutez l'entrée SafeControl au fichier web.config.
- Installez le manifeste de fonctionnalité et les autres fichiers nécessaires dans les répertoires appropriés.
- Enregistrez la fonctionnalité dans la base de données SharePoint et rendez-la disponible pour l'activation au niveau de la fonctionnalité.

{{% /alert %}}

## Activation

{{% alert color="primary" %}}

**Aspose.PDF for SharePoint est fourni en tant que fonctionnalité au niveau du site (collection de sites) et peut être activé et désactivé sur les collections de sites.**

{{% /alert %}}

{{% alert color="primary" %}}

Lors de l'activation, la fonctionnalité apporte quelques modifications au répertoire virtuel de l'application Web parent de la collection de sites : Ajouter la page des paramètres de conversion au fichier de plan du site. Copiez les fichiers de ressources nécessaires dans le dossier App_GlobalResources dans le répertoire virtuel.

{{% /alert %}}

