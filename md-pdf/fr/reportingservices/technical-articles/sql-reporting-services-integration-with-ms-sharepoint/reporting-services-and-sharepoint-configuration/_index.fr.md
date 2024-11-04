---
title: Reporting Services and SharePoint configuration
type: docs
weight: 40
url: /reportingservices/reporting-services-and-sharepoint-configuration/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

Maintenant que SharePoint est installé et configuré sur le serveur RS et que RS est configuré et mis en place via le Gestionnaire de configuration de Reporting Services, nous pouvons passer à la configuration dans l'administration centrale. RS 2008 R2 a vraiment simplifié ce processus. Nous avions l'habitude d'avoir un processus en 3 étapes à réaliser pour que cela fonctionne. Maintenant, il n'y a plus qu'une seule étape.

{{% /alert %}}

{{% alert color="primary" %}}

Nous voulons aller sur le site Web de l'administrateur central, puis dans Paramètres généraux de l'application. Vers le bas, nous verrons Reporting Services.

![todo:image_alt_text](reporting-services-and-sharepoint-configuration_1.png)
**Image1**:- Boîte de dialogue de configuration de SharePoint

Sélectionnez le lien "Intégration de Reporting Services". L'écran suivant s'affichera.

![todo:image_alt_text](reporting-services-and-sharepoint-configuration_2.png)
**Image2**:- Spécifiez les identifiants d'intégration des services de rapports

{{% /alert %}}

## URL du service Web:

**Nous fournirons l'URL du serveur de rapports que nous avons trouvée dans le Gestionnaire de configuration des services de rapports.**

## Mode d'authentification:

**Nous sélectionnerons également un mode d'authentification. Le lien MSDN suivant explique en détail ce qu'ils sont.
Vue d'ensemble de la sécurité pour les services de rapports en mode intégré SharePoint**

{{% alert color="primary" %}}

**En bref, si votre site utilise l'authentification par revendications, vous utiliserez toujours l'authentification de confiance, quel que soit votre choix ici. Si vous souhaitez transmettre les identifiants Windows, vous voudrez choisir l'authentification Windows. Pour l'authentification de confiance, nous transmettrons le jeton SPUser et ne compterons pas sur l'identifiant Windows. Vous voudrez également utiliser l'authentification de confiance si vous avez configuré vos sites en mode classique pour NTLM et que RS est configuré pour NTLM. Kerberos serait nécessaire pour utiliser l'authentification Windows et pour la transmettre à votre source de données.**

{{% /alert %}}

## Activer la fonctionnalité :

{{% alert color="primary" %}}

**Cela vous donne la possibilité d'activer les Services de Reporting sur toutes les collections de sites, ou vous pouvez choisir celles sur lesquelles vous souhaitez l'activer. Cela signifie simplement quels sites pourront utiliser les Services de Reporting. Une fois terminé, vous devriez voir les résultats suivants**

![todo:image_alt_text](reporting-services-and-sharepoint-configuration_3.png)

**Image3 :**- Intégration réussie des Services de Reporting avec l'environnement SharePoint
{{% /alert %}}

{{% alert color="primary" %}}

En revenant à l'URL ReportServer, nous devrions voir quelque chose de similaire à ce qui suit

![todo:image_alt_text](reporting-services-and-sharepoint-configuration_4.png)

**Image4 :**- Les Services de Reporting sont connectés avec succès à l'environnement SharePoint

**REMARQUE :** ***Si votre site SharePoint est configuré pour SSL, il n'apparaîtra pas dans cette liste. C'est un problème connu et cela ne signifie pas qu'il y a un problème. Vos rapports devraient toujours fonctionner.***
{{% /alert %}}
{{% alert color="primary" %}}

Maintenant que nous avons intégré avec succès les deux produits, nous sommes prêts à utiliser les Services de Reporting dans SharePoint 2010. Comme la version précédente, nous avons une fonctionnalité (activée lorsque nous configurons l'intégration des Services de Reporting) dans la "Fonctionnalité de collection de sites". De plus, l'installation a ajouté 3 types de contenu à ajouter à notre site. Dans l'Image 7, nous pouvons voir 2 de ces types de contenu ajoutés dans une bibliothèque de documents pour créer un rapport personnalisé, comme nous pouvons le voir dans l'Image5 ci-dessous.

![todo:image_alt_text](reporting-services-and-sharepoint-configuration_5.png)

**Image5:**- Générateur de rapports

Le "Générateur de rapports" est un contrôle ActiveX, nous devons donc le télécharger sur le serveur, comme nous pouvons le voir dans l'Image 6 ci-dessous.

![todo:image_alt_text](reporting-services-and-sharepoint-configuration_6.png)

**Image6:**- Télécharger et installer le Générateur de rapports
{{% /alert %}}

{{% alert color="primary" %}}

Une fois le processus de téléchargement terminé, chargez le contrôle "Générateur de rapports". Maintenant, nous sommes prêts à concevoir notre premier rapport, comme indiqué dans l'Image7 ci-dessous.

![todo:image_alt_text](reporting-services-and-sharepoint-configuration_7.png)

**Image7:**- Générateur de rapports – Nouvel assistant de génération de rapport
{{% /alert %}}

{{% alert color="primary" %}}

Après avoir créé notre rapport, nous pourrions le sauvegarder dans la bibliothèque de documents créée pour placer les rapports dans notre SharePoint 2010. L'autre type de contenu doit être utilisé pour créer une connexion partagée en tant que source de données et les enregistrer dans une bibliothèque de documents dans SharePoint. Nous pouvons créer une bibliothèque de documents, ajouter ce type de contenu et après nous pouvons avoir nos connexions disponibles pour changer la source de données des rapports.

![todo:image_alt_text](reporting-services-and-sharepoint-configuration_8.png)

**Image8:**- Intégration réussie d'Aspose.PDF pour Reporting Services avec MS SharePoint
{{% /alert %}}