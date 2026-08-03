---
title: Configuration des services de reporting
linktitle: Configuration des services de reporting
type: docs
weight: 20
url: /reportingservices/setting-up-reporting-services/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

Notre premier arrêt sur le serveur Reporting Services est le gestionnaire de configuration Reporting Services.

{{% /alert %}}

## Compte de services :

**Assurez-vous de comprendre quel compte de service vous utilisez pour Reporting Services. Si nous rencontrons des problèmes, cela peut être lié au compte de service que vous utilisez. La valeur par défaut est Service réseau. Lorsque nous déployons de nouvelles versions, nous utilisons toujours des comptes de domaine, car c'est là que nous sommes susceptibles de rencontrer des problèmes. Pour cette instance de serveur, nous avons utilisé un compte de domaine appelé RSService.**

![Set Up](setting-up-reporting-services_1.png)

**Image1 : – Configuration d'un compte de service**

## Web Service URL:

{{% alert color="primary" %}}

**Nous devrons configurer l'URL du service Web. Il s'agit du répertoire virtuel ReportServer (vdir) qui héberge les services Web utilisés par Reporting Services et avec lequel SharePoint communiquera. Sauf si vous souhaitez personnaliser les propriétés du vdir (c'est-à-dire SSL, ports, en-têtes d'hôte, etc.), vous devriez simplement pouvoir cliquer sur Appliquer ici et être prêt à partir.**
![Web Service URL](setting-up-reporting-services_2.png)

**Image2 : - Configuration de l'URL du service Web Une fois l'URL du service Web configurée, vous devriez pouvoir voir les résultats suivants**

![Web Service URL Results](setting-up-reporting-services_3.png)

**Image3 : - Configuration réussie de l'URL du service Web**
{{% /alert %}}

## Base de données :

**We need to create the Reporting Services Catalog Database. This can be placed on any SQL 2008 or SQL 2008 R2 Database Engine. SQL11 would work ok as well, but that is still in BETA. This action will create two databases, ReportServer and ReportServerTempDB, by default.**

{{% alert color="primary" %}}
** L'autre étape importante consiste à vous assurer que vous choisissez SharePoint Integrated pour le type de base de données. Une fois ce choix effectué, il ne peut plus être modifié.**

![Creating Report Server Database](setting-up-reporting-services_4.png)

**Image4 : - Création d'une base de données du serveur de rapports**

![Setting up Database Server and Authentication Type](setting-up-reporting-services_5.png)

**Image5 : - Configuration du serveur de base de données et du type d'authentification**

![Setting up Database Name and Mode](setting-up-reporting-services_6.png)

**Image6 : - Configuration du nom et du mode de la base de données**
{{% /alert %}}

**Pour les informations d'identification, voici comment le Report Server communiquera avec le SQL Server. Quel que soit le compte que vous sélectionnez, vous recevrez certains droits dans la base de données du catalogue ainsi que dans certaines bases de données système via RSExecRole. MSDB est l'une de ces bases de données pour l'utilisation des abonnements car nous utilisons l'agent SQL.**

![Setting up Report Server database credentials](setting-up-reporting-services_7.png)

**Image7:- Setting up Report Server database credentials**

{{% alert color="primary" %}}

**Une fois les informations d'identification de la base de données spécifiées, nous devrions pouvoir obtenir les résultats comme spécifié ci-dessous.**

![Report Server database creation progress](setting-up-reporting-services_8.png)

**Image8 : - Progression de la création de la base de données Report Server**

![Report Server database completion summary](setting-up-reporting-services_9.png)

**Image9 : - Résumé de l'achèvement de la base de données Report Server**
{{% /alert %}}

## URL du gestionnaire de rapports :

**Nous pouvons ignorer l'URL du gestionnaire de rapports car elle n'est pas utilisée lorsque nous sommes en mode intégré SharePoint. SharePoint est notre interface. Le Gestionnaire de rapports ne fonctionne pas.**

## Clés de cryptage :

{{% alert color="primary" %}}
** Sauvegardez vos clés de cryptage et assurez-vous de savoir où vous les conservez. Si vous vous trouvez dans une situation où vous devez migrer la base de données ou la restaurer, vous en aurez besoin.**

![Report Server Encryption key backup](setting-up-reporting-services_10.png)

**Image10 : - Sauvegarde de la clé de chiffrement du serveur de rapports**
{{% /alert %}}

{{% alert color="primary" %}}
**Félicitation ! Nous avons configuré avec succès Reporting Services à l’aide de Configuration Manager. Si vous accédez à l'URL dans l'onglet URL du service Web, elle devrait afficher quelque chose de similaire à ce qui suit.**

![Report Server access after installation](setting-up-reporting-services_11.png)

**Image11 : - Accès au serveur de rapports après l'installation**

**Raison de l'erreur : SharePoint est installé sur notre WFE et nous avons terminé la configuration de Reporting Services. Dans cet exemple, Reporting Services et SharePoint se trouvent sur des machines différentes. S'ils étaient sur la même machine, vous n'auriez pas vu cette erreur. Nous devons techniquement installer SharePoint sur la RS Box. Cela signifie qu'IIS sera également activé.**
{{% /alert %}}

