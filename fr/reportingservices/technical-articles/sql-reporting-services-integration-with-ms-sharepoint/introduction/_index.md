---
title: Introduction
type: docs
weight: 10
url: /fr/reportingservices/introduction/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

Aspose.PDF for Reporting Services a été très remarquable pour la génération de PDF via SQL Reporting Services depuis de nombreuses années et il offre diverses options de configuration et de paramétrage qui ne sont pas prises en charge par défaut dans SQL Reporting Services. Récemment, nous avons reçu quelques demandes concernant l'intégration d'Aspose.PDF pour Reporting Services avec SharePoint. Pour cet article, nous allons nous concentrer sur MS SharePoint 2010. Avant de continuer, nous supposons que vous avez déjà configuré une ferme SharePoint. Dans cet exemple, nous allons utiliser SharePoint Cloud complet. Cependant, les étapes sont similaires pour SharePoint Foundation Server.

{{% /alert %}}

{{% alert color="primary" %}}

Avant de continuer, jetons un coup d'œil aux sujets de référence que nous avons consultés lors de la préparation de cet article.

- [Aperçu de l'intégration des technologies Reporting Services et SharePoint](http://msdn.microsoft.com/en-us/library/bb326358.aspx)
- [Deployment Topologies for Reporting Services in SharePoint Integrated Mode](http://msdn.microsoft.com/en-us/library/bb510781.aspx)
- [Configuring Reporting Services for SharePoint 2010 Integration](http://msdn.microsoft.com/en-us/library/bb326356.aspx)

{{% /alert %}}

## Configuration de l'environnement

Notre configuration se compose de 4 serveurs. Elle comprend un contrôleur de domaine, un serveur SQL, un serveur SharePoint et un serveur pour les services de rapports. Vous pouvez choisir d'avoir SharePoint et les services de rapports sur le même serveur, ce qui simplifiera un peu les choses et je soulignerai certaines des différences.

## Prérequis d'installation

{{% alert color="primary" %}}

Le module complémentaire des services de rapports pour SharePoint est l'un des composants clés pour assurer le bon fonctionnement de l'intégration. L'Add-In doit être installé sur l'un des Web Front Ends (WFE) qui se trouve dans votre ferme SharePoint ainsi que sur le serveur Central Admin. L'une des nouvelles modifications avec SQL 2008 R2 et SharePoint 2010 est que l'Add-In 2008 R2 est désormais une pré-requis pour l'installation de SharePoint. Cela signifie que l'Add-In RS sera installé lorsque vous procéderez à l'installation de SharePoint. Cela a été montré et mis en évidence dans la figure ci-dessous. Cela évite en fait beaucoup de problèmes que nous avons rencontrés avec SP 2007 et RS 2008 lors de l'installation de l'Add-In.

![todo:image_alt_text](introduction_1.png)

**Image1 :- Add-in des Services de Rapport pour Share Point**
{{% /alert %}}

## Authentification SharePoint

**Avant de plonger dans les éléments d'intégration RS, une chose que je veux souligner à propos de la ferme SharePoint est la façon dont vous configurez le site. Plus précisément, comment vous configurez l'authentification pour le site. Que ce soit Classique ou Claims. Ce choix est important au début. Je ne crois pas que vous puissiez changer cette option une fois qu'elle est faite. Si vous pouvez la changer, ce ne serait pas un processus simple.

NOTE: ***Reporting Services 2008 R2 n'est PAS compatible avec Claims***

Même si vous choisissez que votre site SharePoint utilise Claims, Reporting Services lui-même n'est pas compatible avec Claims. Cela dit, cela affecte le fonctionnement de l'authentification avec Reporting Services. Alors, quelle est la différence du point de vue de Reporting Services ? Cela dépend de si vous voulez transmettre les identifiants de l'utilisateur à la source de données. Classique :- Peut utiliser Kerberos et transmettre les identifiants de l'utilisateur à votre source de données en arrière-plan (vous devrez utiliser Kerberos pour cela). Claims:- Un jeton Claims est utilisé et non un jeton Windows. RS utilisera toujours l'authentification de confiance dans ce scénario et n'aura accès qu'au jeton SPUser. Vous devrez stocker vos identifiants dans votre source de données.

Classique :- Peut utiliser Kerberos et transmettre les identifiants de l'utilisateur à votre source de données en arrière-plan (vous devrez utiliser Kerberos pour cela).
Claims :- Un jeton de revendications est utilisé et non un jeton Windows. RS utilisera toujours l'authentification de confiance dans ce scénario et n'aura accès qu'au jeton SPUser. Vous devrez stocker vos identifiants dans votre source de données.

Pour l'instant, nous voulons juste nous concentrer sur la configuration de RS. À ce stade, SharePoint est installé sur mon serveur SharePoint et configuré avec un site d'authentification classique sur le port 80. Sur le serveur RS, je viens d'installer les services de rapports et c'est tout.