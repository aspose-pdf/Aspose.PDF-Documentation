---
title: Désinstallation d'Aspose.PDF pour la licence SharePoint
linktitle: Désinstallation d'Aspose.PDF pour la licence SharePoint
type: docs
weight: 30
url: /fr/sharepoint/uninstalling-aspose-pdf-for-sharepoint-license/
lastmod: "2020-12-16"
description: Veuillez suivre les étapes mentionnées dans cet article pour désinstaller la licence API PDF SharePoint.
---

## Étapes de désinstallation

{{% alert color="primary" %}}

Pour désinstaller la licence Aspose.PDF for SharePoint, veuillez suivre les étapes ci-dessous à partir de la console du serveur.

1. Retirez la solution de licence de la batterie :

  stsadm.exe -o retractsolution -name Aspose.PDF.SharePoint.License.wsp -immediate

2. Execute administrative timer jobs to complete the retraction immediately:

  stsadm.exe -o execadmsvcjobs

3. Wait for the retraction to complete. You can use Central

  Administration pour vérifier si la rétractation est terminée sous Administration centrale -> Opérations -> Gestion des solutions

4. Supprimez la solution du magasin de solutions SharePoint :

  stsadm.exe -o deletesolution -name Aspose.PDF.SharePoint.License.wsp

{{% /alert %}}

