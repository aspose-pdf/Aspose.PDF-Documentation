---
title: Configuration de SharePoint sur le serveur de services de rapport
type: docs
weight: 30
url: fr/reportingservices/setting-up-sharepoint-on-reporting-services-server/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

Nous devons maintenant effectuer des étapes similaires à celles que nous avons effectuées pour le WFE de SharePoint. La première chose à faire est de passer par l'installation des prérequis et une fois que c'est fait, démarrer la configuration de SharePoint.

{{% /alert %}}

Pour la configuration, je choisis Server Farm et une installation complète pour correspondre à mon SharePoint Box, car je ne veux pas d'une installation autonome pour SharePoint.

## Configuration de SharePoint

{{% alert color="primary" %}}

**Dans l'assistant de configuration de SharePoint, nous voulons nous connecter à une ferme existante.**

![todo:image_alt_text](setting-up-sharepoint-on-reporting-services-server_1.png)

**Image1:- Assistant de configuration de SharePoint**
{{% /alert %}}

{{% alert color="primary" %}}

**Nous allons ensuite le pointer vers la base de données SharePoint_Config que notre ferme utilise.**  Si vous ne savez pas où cela se trouve, vous pouvez le découvrir via l'Administration Centrale à travers Paramètres du Système -> Gérer les Serveurs dans cette ferme.**

![todo:image_alt_text](setting-up-sharepoint-on-reporting-services-server_2.png)

**Image2:- Spécifier les paramètres de configuration de la base de données**

![todo:image_alt_text](setting-up-sharepoint-on-reporting-services-server_3.png)

**Image3:- Assistant de configuration SharePoint**
{{% /alert %}}

{{% alert color="primary" %}}

**Une fois l'assistant terminé, c'est tout ce que nous devons faire sur la boîte du serveur de rapports pour l'instant. En revenant à l'URL de ReportServer, nous verrons une autre erreur, mais c'est parce que nous ne l'avons pas configurée via l'Administrateur Central.**

![todo:image_alt_text](setting-up-sharepoint-on-reporting-services-server_4.png)

**Image4:- Erreur du serveur de rapports**
{{% /alert %}}