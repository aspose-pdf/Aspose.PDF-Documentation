---
title: Configuration de Reporting Services et de SharePoint
linktitle: Reporting Services and SharePoint configuration
type: docs
weight: 40
url: /reportingservices/reporting-services-and-sharepoint-configuration/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

Maintenant que SharePoint est installé et configuré sur le serveur RS et que RS est installé et configuré via le gestionnaire de configuration de Reporting Services, nous pouvons passer à la configuration dans Central Admin. RS 2008 R2 a vraiment simplifié ce processus. Nous avions l'habitude d'avoir un processus en 3 étapes que vous deviez suivre pour que cela fonctionne. Il ne nous reste plus qu'une étape.

{{% /alert %}}

{{% alert color="primary" %}}

Nous souhaitons accéder au site Web de l'administrateur central, puis aux paramètres généraux de l'application. Vers le bas, nous verrons Reporting Services.

![Configuration-step1](reporting-services-and-sharepoint-configuration_1.png)
**Image1** : boîte de dialogue de configuration SharePoint

Sélectionnez le lien « Intégration de Reporting Services ». L'écran suivant s'affichera.

![Configuration-step2](reporting-services-and-sharepoint-configuration_2.png)
**Image2** : - Spécifiez les informations d'identification de l'intégration de Reporting Services

{{% /alert %}}

## URL du service Web :

**Nous fournirons l'URL du serveur de rapports que nous avons trouvé dans le gestionnaire de configuration de Reporting Services.**

## Mode d'authentification :

**Nous sélectionnerons également un mode d'authentification. Le lien MSDN suivant explique en détail de quoi il s’agit.
Présentation de la sécurité pour Reporting Services en mode intégré SharePoint**

{{% alert color="primary" %}}

**En bref, si votre site utilise l'authentification par réclamation, vous utiliserez toujours l'authentification de confiance, quel que soit ce que vous choisissez ici. Si vous souhaitez transmettre les informations d'identification Windows, vous souhaiterez choisir l'authentification Windows. Pour l'authentification approuvée, nous transmettrons le jeton SPUser et ne nous fierons pas aux informations d'identification Windows. Vous souhaiterez également utiliser l'authentification approuvée si vous avez configuré vos sites en mode classique pour NTLM et que RS est configuré pour NTLM. Kerberos serait nécessaire pour utiliser l'authentification Windows et pour la transmettre à votre source de données.**

{{% /alert %}}

## Activer la fonctionnalité :

{{% alert color="primary" %}}

**Cela vous donne la possibilité d'activer les services de reporting sur toutes les collections de sites, ou vous pouvez choisir celles sur lesquelles vous souhaitez l'activer. Cela signifie simplement quels sites pourront utiliser Reporting Services. Une fois terminé, vous devriez voir les résultats suivants**

![Configuration-step3](reporting-services-and-sharepoint-configuration_3.png)

**Image3 :** - Intégration réussie de Reporting Services avec l'environnement SharePoint
{{% /alert %}}

{{% alert color="primary" %}}

En revenant à l'URL du ReportServer, nous devrions voir quelque chose de similaire à ce qui suit

![Configuration-step4](reporting-services-and-sharepoint-configuration_4.png)

**Image4 :** - Reporting Services est connecté avec succès à l'environnement SharePoint

**REMARQUE :** ***Si votre site SharePoint est configuré pour SSL, il n'apparaîtra pas dans cette liste. C'est un problème connu et cela ne signifie pas qu'il y a un problème. Vos rapports devraient toujours fonctionner.***
{{% /alert %}}

{{% alert color="primary" %}}

Maintenant que nous avons intégré avec succès les deux produits, nous sommes prêts à utiliser Reporting Services dans SharePoint 2010. Comme dans la version précédente, nous disposons d'une fonctionnalité (activée lorsque nous configurons l'intégration de Reporting Services) dans la « Fonctionnalité de collection de sites ». L'installation a également ajouté 3 types de contenu à ajouter à notre site. Dans l'image 7, nous pouvons voir 2 d'entre eux types de contenu ajoutés dans une bibliothèque de documents pour créer un rapport personnalisé en utilisant le, comme nous pouvons le voir dans l'image5 ci-dessous.

![Configuration-step5](reporting-services-and-sharepoint-configuration_5.png)

**Image5 :** - Générateur de rapports

Le « Reporter Builder » est un contrôle ActiveX, nous devons donc le télécharger sur le serveur, comme nous pouvons le voir dans l'image 6 ci-dessous.

![Configuration-step6](reporting-services-and-sharepoint-configuration_6.png)

**Image6 :** - Téléchargez et installez Report Builder
{{% /alert %}}

{{% alert color="primary" %}}

Une fois le processus de téléchargement terminé, chargez le contrôle « Report Builder ». Nous sommes maintenant prêts à concevoir notre premier rapport, comme le montre l'image 7 ci-dessous.

![Configuration-step7](reporting-services-and-sharepoint-configuration_7.png)

**Image7 :** - Report Builder – Nouvel assistant de génération de rapport
{{% /alert %}}

{{% alert color="primary" %}}

After create our report we could save it in the document library created to put the reports in our SharePoint 2010. The other content type must be used to create shared connection as data source and save them in a document library in SharePoint. We can create a document library, add this content type and after we can have our connections available to change the data source of the reports.

![Configuration-step8](reporting-services-and-sharepoint-configuration_8.png)

**Image8 :** - Intégration réussie d'Aspose.PDF pour Reporting Services avec MS SharePoint
{{% /alert %}}

