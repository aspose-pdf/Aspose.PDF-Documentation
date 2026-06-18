---
title: Désinstallation de la licence Aspose.Pdf pour SharePoint
linktitle: Désinstallation de la licence Aspose.Pdf pour SharePoint
type: docs
weight: 30
url: /fr/sharepoint/uninstalling-aspose-pdf-for-sharepoint-license/
lastmod: "2026-06-18"
description: Veuillez suivre les étapes mentionnées dans cet article pour désinstaller la licence PDF SharePoint API.
---

## Étapes de désinstallation

{{% alert color="primary" %}}

Pour désinstaller la licence Aspose.PDF pour SharePoint, veuillez utiliser les étapes ci-dessous depuis la console du serveur.

1. Rétractez la solution de licence du farm :

  stsadm.exe -o retractsolution -name Aspose.PDF.SharePoint.License.wsp -immediate

2. Exécuter les travaux de minuteur administratifs pour terminer la rétractation immédiatement :

  stsadm.exe -o execadmsvcjobs

3. Attendez que la rétractation se termine. Vous pouvez utiliser Central   

  Administration pour vérifier si la rétractation s’est terminée sous Administration centrale -> Opérations -> Gestion des solutions

4. Supprimer la solution du magasin de solutions SharePoint :

  stsadm.exe -o deletesolution -name Aspose.PDF.SharePoint.License.wsp

{{% /alert %}}
