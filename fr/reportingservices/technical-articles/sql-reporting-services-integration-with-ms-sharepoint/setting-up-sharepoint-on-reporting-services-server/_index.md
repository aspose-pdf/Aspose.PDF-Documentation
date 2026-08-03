---
title: Configuration de SharePoint sur le serveur Reporting Services
linktitle: Configuration de SharePoint sur le serveur Reporting Services
type: docs
weight: 30
url: /reportingservices/setting-up-sharepoint-on-reporting-services-server/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

Now we need to perform similar steps as we did for the SharePoint WFE. First thing is to go through the Prereq uisites install and once it is done, startup the SharePoint setup.

{{% /alert %}}

Pour la configuration, je choisis Server Farm et une installation complète correspondant à ma SharePoint Box, car je ne souhaite pas d'installation autonome pour SharePoint.

## Configuration SharePoint

{{% alert color="primary" %}}

**Dans l'assistant de configuration SharePoint, nous souhaitons nous connecter à une batterie de serveurs existante.**

![SharePoint Configuration Wizard](setting-up-sharepoint-on-reporting-services-server_1.png)

**Image1 : - Assistant de configuration SharePoint**
{{% /alert %}}

{{% alert color="primary" %}}

**We will then point it to the SharePoint_Config database that our farm is using. If you don't know where this is, you can find out through Central Admin through System Settings -> Manager Servers in this farm.**

![SharePoint Configuration Database](setting-up-sharepoint-on-reporting-services-server_2.png)

**Image2 : - Spécifiez les paramètres de configuration de la base de données**

![SharePoint Configuration Wizard](setting-up-sharepoint-on-reporting-services-server_3.png)

**Image3 : - Assistant de configuration SharePoint**
{{% /alert %}}

{{% alert color="primary" %}}

**Une fois l'assistant terminé, c'est tout ce que nous devons faire sur la boîte du serveur de rapports pour le moment. En revenant à l'URL du ReportServer, nous verrons une autre erreur, mais c'est parce que nous ne l'avons pas configuré via l'Administrateur central.**

![SharePoint Configuration Error](setting-up-sharepoint-on-reporting-services-server_4.png)

**Image4 : – Erreur du serveur de rapports**
{{% /alert %}}
