---
title: Désinstallation de la Licence Aspose.Pdf pour SharePoint
type: docs
weight: 30
url: /fr/sharepoint/uninstalling-aspose-pdf-for-sharepoint-license/
lastmod: "2020-12-16"
description: Veuillez suivre les étapes mentionnées dans cet article pour désinstaller la Licence PDF SharePoint API.
---

## Étapes de Désinstallation

{{% alert color="primary" %}}

Pour désinstaller la licence Aspose.PDF pour SharePoint, veuillez utiliser les étapes ci-dessous depuis la console du serveur.

1. Rétractez la solution de licence de la ferme :

  stsadm.exe -o retractsolution -name Aspose.PDF.SharePoint.License.wsp -immediate

2. Exécutez les travaux planifiés administratifs pour compléter la rétractation immédiatement :

  stsadm.exe -o execadmsvcjobs

3. Attendez la fin de la rétractation. Vous pouvez utiliser l'Administration Centrale pour vérifier si la rétractation est terminée sous Administration Centrale -> Opérations -> Gestion des Solutions

4. Supprimez la solution du magasin de solutions SharePoint :

  stsadm.exe -o deletesolution -name Aspose.PDF.SharePoint.License.wsp

{{% /alert %}}