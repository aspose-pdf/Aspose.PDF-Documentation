---
title: Installation d'Aspose.PDF pour la licence SharePoint
linktitle: Installation d'Aspose.PDF pour la licence SharePoint
type: docs
weight: 10
url: /fr/sharepoint/installing-aspose-pdf-for-sharepoint-license/
lastmod: "2020-12-16"
description: Une fois que vous êtes satisfait de votre évaluation, vous pouvez acheter une licence pour l'API PDF SharePoint et suivre les instructions d'installation pour l'appliquer.
---

{{% alert color="primary" %}}

Une fois que vous êtes satisfait de votre évaluation, vous pouvez [acheter une licence](https://purchase.aspose.com/buy). Avant d'acheter, assurez-vous de comprendre et d'accepter les conditions d'abonnement à la licence.

{{% /alert %}}

{{% alert color="primary" %}}

La licence vous sera envoyée par email une fois la commande payée. La licence est une archive .zip contenant un package de solution SharePoint standard.

Ces archives contiennent :

- Aspose.PDF.SharePoint.License.wsp

Fichier de package de solution SharePoint. La licence Aspose.PDF for SharePoint est présentée sous forme de solution SharePoint pour faciliter le déploiement/la rétractation sur la batterie de serveurs.

- lisezmoi.txt

Instructions d'installation de la licence. L'installation de la licence s'effectue depuis la console du serveur via stsadm.exe. Les étapes requises pour installer la licence sont indiquées ci-dessous.

**Remarque :** Les chemins sont omis pour plus de clarté. Vous devrez peut-être ajouter le chemin réel vers stsadm.exe et/ou le fichier de solution lors de leur exécution.

1. Exécutez stsadm pour ajouter la solution au magasin de solutions SharePoint :

stsadm.exe -o addsolution -filename Aspose.PDF.SharePoint.License.wsp

2. Déployez la solution sur tous les serveurs de la ferme :

stsadm.exe -o déployersolution -name Aspose.PDF.SharePoint.License.wsp -immediate -force

3. Exécutez des tâches de minuterie administrative pour terminer le déploiement immédiatement.

stsadm.exe -o execadmsvcjobs

**Remarque :** Vous recevrez un avertissement lors de l'exécution de l'étape de déploiement si le service d'administration de Windows SharePoint Services n'est pas démarré. Stsadm.exe s'appuie sur ce service et sur le service de minuterie Windows SharePoint pour répliquer les données de la solution dans la batterie de serveurs. Si ces services ne s'exécutent pas sur votre batterie de serveurs, vous devrez peut-être déployer la licence sur chaque serveur.

{{% /alert %}}

