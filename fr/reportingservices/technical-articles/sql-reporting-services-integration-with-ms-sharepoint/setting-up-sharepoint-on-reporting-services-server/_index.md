---
title: Configurer SharePoint sur le serveur Reporting Services
linktitle: Configurer SharePoint sur le serveur Reporting Services
type: docs
weight: 30
url: /fr/reportingservices/setting-up-sharepoint-on-reporting-services-server/
lastmod: "2026-06-19"
---

{{% alert color="primary" %}}

Maintenant, nous devons effectuer des étapes similaires à celles que nous avons réalisées pour le WFE SharePoint. La première chose est de passer par l'installation des prérequis uisites et, une fois terminée, de démarrer l'installation de SharePoint.

{{% /alert %}}

Pour la configuration, je choisis Server Farm et une installation complète afin de correspondre à mon SharePoint Box, car je ne souhaite pas d'installation autonome pour SharePoint.

## Configuration de SharePoint

{{% alert color="primary" %}}

**Dans l’assistant de configuration SharePoint, nous voulons nous connecter à une ferme existante.**

![todo:image_alt_text](setting-up-sharepoint-on-reporting-services-server_1.png)

**Image1:- Assistant de configuration SharePoint**
{{% /alert %}}

{{% alert color="primary" %}}

**Nous le pointerons alors vers la base de données SharePoint_Config que notre ferme utilise. Si vous ne savez pas où elle se trouve, vous pouvez le découvrir via Central Admin dans Paramètres du système -> Gérer les serveurs de cette ferme.**

![todo:image_alt_text](setting-up-sharepoint-on-reporting-services-server_2.png)

**Image2:- Spécifier les paramètres de configuration de la base de données**

![todo:image_alt_text](setting-up-sharepoint-on-reporting-services-server_3.png)

**Image3:- Assistant de configuration SharePoint**
{{% /alert %}}

{{% alert color="primary" %}}

**Une fois l’assistant terminé, c’est tout ce que nous devons faire sur la boîte du serveur de rapports pour le moment. En revenant à l’URL du ReportServer, nous verrons une autre erreur, mais c’est parce que nous ne l’avons pas configurée via le Central Administrator.**

![todo:image_alt_text](setting-up-sharepoint-on-reporting-services-server_4.png)

**Image4 :- Erreur du serveur de rapports**
{{% /alert %}}

