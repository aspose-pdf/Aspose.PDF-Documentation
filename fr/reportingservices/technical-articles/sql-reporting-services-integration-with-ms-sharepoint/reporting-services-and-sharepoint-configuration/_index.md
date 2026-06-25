---
title: Configuration de Reporting Services et SharePoint
linktitle: Configuration de Reporting Services et SharePoint
type: docs
weight: 40
url: /fr/reportingservices/reporting-services-and-sharepoint-configuration/
lastmod: "2026-06-19"
---

{{% alert color="primary" %}}

Maintenant que SharePoint est installé et configuré sur le serveur RS et que RS est configuré via le Reporting Services Configuration Manager, nous pouvons passer à la configuration dans Central Admin. RS 2008 R2 a vraiment simplifié ce processus. Auparavant, nous devions suivre un processus en 3 étapes pour le faire fonctionner. Maintenant, nous n'avons plus qu'une seule étape.

{{% /alert %}}

{{% alert color="primary" %}}

Nous voulons accéder au site Web Central Administrator, puis à Paramètres d'application généraux. Vers le bas, nous verrons Reporting Services.

![todo:image_alt_text](reporting-services-and-sharepoint-configuration_1.png)
**Image1**:- boîte de dialogue de configuration SharePoint

Sélectionnez le lien "Reporting Services Integration". L'écran suivant sera affiché.

![todo:image_alt_text](reporting-services-and-sharepoint-configuration_2.png)
**Image2**:- Spécifier les informations d’identification d’intégration de Reporting Services

{{% /alert %}}

## URL du service Web :

**Nous fournirons l'URL du serveur de rapports que nous avons trouvé dans le Gestionnaire de configuration des services de rapports.**

## Mode d'authentification :

**Nous sélectionnerons également un mode d'authentification. Le lien MSDN suivant explique en détail ce que c’est.
Vue d'ensemble de la sécurité pour Reporting Services en mode intégré SharePoint**

{{% alert color="primary" %}}

**En bref, si votre site utilise l'authentification par revendications, vous utiliserez toujours l'authentification fiable quel que soit votre choix ici. Si vous souhaitez transmettre les informations d'identification Windows, vous devez choisir l'authentification Windows. Pour l'authentification fiable, nous transmettrons le jeton SPUser et ne dépendrons pas des informations d'identification Windows. Vous souhaiterez également utiliser l'authentification fiable si vous avez configuré vos sites en mode classique pour NTLM et que RS est configuré pour NTLM. Kerberos serait nécessaire pour utiliser l'authentification Windows et la transmettre à votre source de données.**

{{% /alert %}}

## Activer la fonctionnalité :

{{% alert color="primary" %}}

**Cela vous donne la possibilité d’activer les Reporting Services sur toutes les collections de sites, ou vous pouvez choisir celles sur lesquelles vous souhaitez les activer. Cela signifie simplement quels sites pourront utiliser les Reporting Services. Une fois terminé, vous devriez voir les résultats suivants**

![todo:image_alt_text](reporting-services-and-sharepoint-configuration_3.png)

**Image3:**- Intégration réussie des Reporting Services avec l’environnement SharePoint
{{% /alert %}}

{{% alert color="primary" %}}

En revenant à l’URL ReportServer, nous devrions voir quelque chose de similaire à ce qui suit

![todo:image_alt_text](reporting-services-and-sharepoint-configuration_4.png)

**Image4:**- Les Reporting Services sont connectés avec succès à l’environnement SharePoint

**NOTE:** ***Si votre site SharePoint est configuré pour SSL, il n’apparaîtra pas dans cette liste. C’est un problème connu et cela ne signifie pas qu’il y a un problème. Vos rapports devraient toujours fonctionner.***
{{% /alert %}}

{{% alert color="primary" %}}

Maintenant que nous avons intégré avec succès les deux produits, nous sommes prêts à utiliser Reporting Services dans SharePoint 2010. Comme dans la version précédente, nous disposons d’une fonctionnalité (activée lorsque nous configurons l’intégration de Reporting Services) dans la « Site Collection Feature ». L’installation a également ajouté 3 types de contenu à ajouter à notre site. Dans l’Image 7, nous pouvons voir 2 de ces types de contenu ajoutés dans une bibliothèque de documents pour créer un rapport personnalisé en les utilisant, comme nous pouvons le voir dans l’Image5 ci‑dessous.

![todo:image_alt_text](reporting-services-and-sharepoint-configuration_5.png)

**Image5 :**- Report Builder

Le “Reporter Builder” est un contrôle ActiveX, nous devons donc le télécharger sur le serveur, comme nous pouvons le voir dans l’Image 6 ci‑dessous.

![todo:image_alt_text](reporting-services-and-sharepoint-configuration_6.png)

**Image6:**- Télécharger et installer Report Builder
{{% /alert %}}

{{% alert color="primary" %}}

Une fois le processus de téléchargement terminé, chargez le contrôle “Report Builder”. Nous sommes maintenant prêts à concevoir notre premier rapport, comme le montre l'Image7 ci‑dessous.

![todo:image_alt_text](reporting-services-and-sharepoint-configuration_7.png)

**Image7:**- Report Builder – Assistant de génération d’un nouveau rapport
{{% /alert %}}

{{% alert color="primary" %}}

Après avoir créé notre rapport, nous pouvons l’enregistrer dans la bibliothèque de documents créée pour stocker les rapports dans notre SharePoint 2010. L’autre type de contenu doit être utilisé pour créer une connexion partagée en tant que source de données et les enregistrer dans une bibliothèque de documents dans SharePoint. Nous pouvons créer une bibliothèque de documents, ajouter ce type de contenu et, ainsi, disposer de nos connexions disponibles pour modifier la source de données des rapports.

![todo:image_alt_text](reporting-services-and-sharepoint-configuration_8.png)

**Image8:**- Intégration réussie d'Aspose.PDF pour Reporting Services avec MS SharePoint
{{% /alert %}}


