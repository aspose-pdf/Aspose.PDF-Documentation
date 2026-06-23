---
title: Installation de la licence Aspose.Pdf pour SharePoint
linktitle: Installation de la licence Aspose.Pdf pour SharePoint
type: docs
weight: 10
url: /fr/sharepoint/installing-aspose-pdf-for-sharepoint-license/
lastmod: "2026-06-18"
description: Une fois que vous êtes satisfait de votre évaluation, vous pouvez acheter une licence pour l'API PDF SharePoint et suivre les instructions d'installation pour l'appliquer.
---

{{% alert color="primary" %}}

Une fois que vous êtes satisfait de votre évaluation, vous pouvez [acheter une licence](https://purchase.aspose.com/buy). Avant d'acheter, assurez-vous de comprendre et d'accepter les conditions d'abonnement de la licence.

{{% /alert %}}

{{% alert color="primary" %}}

La licence vous sera envoyée par e‑mail après le paiement de la commande. La licence est une archive .zip contenant un paquet de solution SharePoint standard.

Cette archive contient :

- Aspose.PDF.SharePoint.License.wsp

Fichier de package de solution SharePoint. La licence Aspose.PDF for SharePoint est empaquetée en tant que solution SharePoint afin de faciliter le déploiement/la rétraction sur l'ensemble de la ferme de serveurs.

- readme.txt

Instructions d'installation de la licence. L'installation de la licence est effectuée depuis la console du serveur via stsadm.exe. Les étapes nécessaires pour installer la licence sont indiquées ci-dessous.

**Note :** Les chemins sont omis pour plus de clarté. Vous devrez peut-être ajouter le chemin réel vers stsadm.exe et/ou le fichier de solution lors de leur exécution.

1. Exécutez stsadm pour ajouter la solution au magasin de solutions SharePoint :

stsadm.exe -o addsolution -filename Aspose.PDF.SharePoint.License.wsp

2. Déployez la solution sur tous les serveurs du farm :

stsadm.exe -o deploysolution -name Aspose.PDF.SharePoint.License.wsp -immediate -force

3. Exécutez les tâches du minuteur administratives pour terminer le déploiement immédiatement.

stsadm.exe -o execadmsvcjobs

**Note :** Vous recevrez un avertissement lors de l'exécution de l'étape de déploiement si le service Windows SharePoint Services Administration n'est pas démarré. Stsadm.exe dépend de ce service et du service Windows SharePoint Timer Service pour reproduire les données de la solution à travers la ferme. Si ces services ne fonctionnent pas sur votre ferme de serveurs, vous devrez peut-être déployer la licence sur chaque serveur.


{{% /alert %}}
