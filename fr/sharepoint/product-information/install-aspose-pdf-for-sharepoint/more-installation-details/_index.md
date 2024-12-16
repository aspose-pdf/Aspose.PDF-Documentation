---
title: Plus de détails sur l'installation
type: docs
weight: 30
url: /fr/sharepoint/more-installation-details/
lastmod: "2020-12-16"
description: Plus d'informations sur l'installation de l'API PDF SharePoint expliquent comment la déployer, l'activer et la désactiver sur les collections de sites.
---

## **Déploiement**

{{% alert color="primary" %}}

**Aspose.PDF pour SharePoint effectue les actions suivantes lors du déploiement :**
- Installer Aspose.PDF.SharePoint.dll dans le Global Assembly Cache et ajouter une entrée SafeControl dans le fichier web.config.
- Installer le manifeste de fonctionnalité et d'autres fichiers nécessaires dans les répertoires appropriés.
- Enregistrer la fonctionnalité dans la base de données SharePoint et la rendre disponible pour l'activation au niveau de la fonctionnalité.

{{% /alert %}}


## **Activation**

{{% alert color="primary" %}}

**Aspose.PDF pour SharePoint est emballé comme une fonctionnalité au niveau du site (collection de sites) et peut être activé et désactivé sur les collections de sites.**

{{% /alert %}}

{{% alert color="primary" %}}

Lors de l'activation, la fonctionnalité apporte quelques modifications au répertoire virtuel de l'application web parent de la collection de sites : Ajouter une page de paramètres de conversion au fichier sitemap.
 Copy necessary resource files to the App_GlobalResources folder in the virtual directory.

{{% /alert %}}