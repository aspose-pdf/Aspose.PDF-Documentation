---
title: Configuration des services de rapports
type: docs
weight: 20
url: fr/reportingservices/setting-up-reporting-services/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

Notre premier arrêt sur le serveur des Services de rapports est le Gestionnaire de configuration des services de rapports.

{{% /alert %}}

## Compte de service :

**Assurez-vous de comprendre quel compte de service vous utilisez pour les Services de rapports. Si nous rencontrons des problèmes, cela peut être lié au compte de service que vous utilisez. Par défaut, c'est le Service Réseau. Lorsque nous déployons de nouvelles versions, nous utilisons toujours des comptes de domaine, car c'est là que nous sommes susceptibles de rencontrer des problèmes. Pour cette instance de serveur, nous avons utilisé un compte de domaine appelé RSService.**

![todo:image_alt_text](setting-up-reporting-services_1.png)

**Image1:- Configuration du compte de service**

## URL du service Web :

{{% alert color="primary" %}}

**Nous devrons configurer l'URL du service Web. This is the ReportServer virtual directory (vdir) that hosts the Web Services Reporting Services uses, and what SharePoint will communicate with. Unless you want to customize the properties of the vdir (i.e. SSL, ports, host headers, etc…), you should just be able to click Apply here and be good to go.**
![todo:image_alt_text](setting-up-reporting-services_2.png)

**Image2:- Configuration de l'URL du service Web Une fois que l'URL du service Web a été configurée, vous devriez pouvoir voir les résultats suivants**

![todo:image_alt_text](setting-up-reporting-services_3.png)

**Image3:- Configuration réussie de l'URL du service Web**
{{% /alert %}}

## Base de données:

**Nous devons créer la base de données du catalogue des services de rapport. Cela peut être placé sur n'importe quel moteur de base de données SQL 2008 ou SQL 2008 R2. SQL11 fonctionnerait également bien, mais il est encore en BETA. Cette action créera deux bases de données, ReportServer et ReportServerTempDB, par défaut.**

{{% alert color="primary" %}}
**L'autre étape importante consiste à s'assurer que vous choisissez SharePoint Integrated pour le type de base de données. **Une fois ce choix fait, il ne peut pas être modifié.**

![todo:image_alt_text](setting-up-reporting-services_4.png)

**Image4 : - Création de la base de données du serveur de rapports**

![todo:image_alt_text](setting-up-reporting-services_5.png)

**Image5 : - Configuration du serveur de base de données et du type d'authentification**

![todo:image_alt_text](setting-up-reporting-services_6.png)

**Image6 : - Configuration du nom de la base de données et du mode**
{{% /alert %}}

**Pour les informations d'identification, c'est ainsi que le serveur de rapports communiquera avec le serveur SQL. Quel que soit le compte que vous sélectionnez, il se verra accorder certains droits au sein de la base de données du catalogue ainsi que de quelques bases de données système via le RSExecRole. MSDB est l'une de ces bases de données pour l'utilisation des abonnements car nous utilisons SQL Agent.**

![todo:image_alt_text](setting-up-reporting-services_7.png)

**Image7 : - Configuration des informations d'identification de la base de données du serveur de rapports**

{{% alert color="primary" %}}

**Une fois les informations d'identification de la base de données spécifiées, nous devrions pouvoir obtenir les résultats comme spécifié ci-dessous.**

![todo:image_alt_text](setting-up-reporting-services_8.png)
**Image8:- Progression de la création de la base de données du serveur de rapports**

![todo:image_alt_text](setting-up-reporting-services_9.png)

**Image9:- Résumé de l'achèvement de la base de données du serveur de rapports**
{{% /alert %}}

## URL du Gestionnaire de Rapports:

**Nous pouvons ignorer l'URL du Gestionnaire de Rapports car elle n'est pas utilisée lorsque nous sommes en mode Intégré SharePoint. SharePoint est notre interface. Le Gestionnaire de Rapports ne fonctionne pas.**

## Clés de Chiffrement:

{{% alert color="primary" %}}
**Sauvegardez vos Clés de Chiffrement et assurez-vous de savoir où vous les gardez. Si vous vous trouvez dans une situation où vous devez migrer la Base de Données ou la restaurer, vous en aurez besoin.**

![todo:image_alt_text](setting-up-reporting-services_10.png)

**Image10:- Sauvegarde de la clé de chiffrement du serveur de rapports**
{{% /alert %}}

{{% alert color="primary" %}}
**Félicitations ! Nous avons configuré avec succès les Services de Rapport en utilisant le Gestionnaire de Configuration. Si vous accédez à l'URL de l'onglet URL du Service Web, cela devrait afficher quelque chose de similaire à ce qui suit.**

![todo:image_alt_text](setting-up-reporting-services_11.png)

**Image11:- Accès au serveur de rapports après l'installation**

**Raison de l'erreur : SharePoint est installé sur notre WFE et nous avons terminé la configuration des services de rapports. Dans cet exemple, les services de rapports et SharePoint sont sur des machines différentes. S'ils étaient sur la même machine, vous n'auriez pas vu cette erreur. Nous devons techniquement installer SharePoint sur la boîte RS. Cela signifie que IIS sera également activé.**  
{{% /alert %}}