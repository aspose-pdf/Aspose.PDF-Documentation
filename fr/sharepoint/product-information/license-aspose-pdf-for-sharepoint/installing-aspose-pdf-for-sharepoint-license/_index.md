---
title: Installation de la Licence Aspose.Pdf pour SharePoint
type: docs
weight: 10
url: /fr/sharepoint/installation-de-la-licence-aspose-pdf-pour-sharepoint/
lastmod: "2020-12-16"
description: Une fois que vous êtes satisfait de votre évaluation, vous pouvez acheter une licence pour l'API PDF SharePoint et suivre les instructions d'installation pour l'appliquer.
---

{{% alert color="primary" %}}

Une fois que vous êtes satisfait de votre évaluation, vous pouvez [acheter une licence](https://purchase.aspose.com/buy). Avant d'acheter, assurez-vous de comprendre et d'accepter les termes de l'abonnement de la licence.

{{% /alert %}}

{{% alert color="primary" %}}

La licence vous sera envoyée par email après que la commande ait été réglée. La licence est une archive .zip contenant un paquet de solution SharePoint régulier.
{{% /alert %}}

Cette archive contient :

- Aspose.PDF.SharePoint.License.wsp

Fichier de paquet de solution SharePoint. La Licence Aspose.PDF pour SharePoint est emballée comme une solution SharePoint pour faciliter le déploiement/retrait à travers la ferme de serveurs.

- readme.txt

Instructions d'installation de la licence.
 L'installation de la licence s'effectue depuis la console du serveur via stsadm.exe. Les étapes nécessaires pour installer la licence sont données ci-dessous.

**Remarque :** Les chemins sont omis pour plus de clarté. Vous devrez peut-être ajouter le chemin réel vers stsadm.exe et/ou le fichier de solution lors de leur exécution.

1. Exécutez stsadm pour ajouter la solution au magasin de solutions SharePoint :

stsadm.exe -o addsolution -filename Aspose.PDF.SharePoint.License.wsp

2. Déployez la solution sur tous les serveurs de la ferme :

stsadm.exe -o deploysolution -name Aspose.PDF.SharePoint.License.wsp -immediate -force

3. Exécutez les tâches administratives du minuteur pour compléter le déploiement immédiatement.

stsadm.exe -o execadmsvcjobs

**Remarque :** Vous recevrez un avertissement lors de l'exécution de l'étape de déploiement si le service d'administration de Windows SharePoint Services n'est pas démarré. Stsadm.exe dépend de ce service et du service de minuteur Windows SharePoint pour répliquer les données de solution à travers la ferme. Si ces services ne fonctionnent pas sur votre ferme de serveurs, vous devrez peut-être déployer la licence sur chaque serveur.