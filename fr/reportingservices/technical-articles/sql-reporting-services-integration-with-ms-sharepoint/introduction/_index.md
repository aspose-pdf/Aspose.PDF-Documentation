---
title: Introduction
linktitle: Introduction
type: docs
weight: 10
url: /fr/reportingservices/introduction/
lastmod: "2026-06-19"
---

{{% alert color="primary" %}}

Aspose.PDF for Reporting Services a été très remarquable pour la génération de PDF via SQL Reporting Services depuis de nombreuses années et il offre diverses options de configuration et de paramétrage qui ne sont pas prises en charge par défaut dans SQL Reporting Services. Récemment, nous avons reçu des demandes concernant l'intégration d'Aspose.PDF for Reporting Services avec SharePoint. Pour cet article, nous allons nous concentrer sur MS SharePoint 2010. Avant d'aller plus loin, nous supposons que vous avez déjà configuré une ferme SharePoint. Dans cet exemple, nous allons utiliser le SharePoint Cloud complet. Cependant, les étapes sont similaires pour SharePoint Foundation Server.

{{% /alert %}}

{{% alert color="primary" %}}

Avant d'aller plus loin, examinons les sujets de référence que nous avons consultés lors de la préparation de cet article.

- [Aperçu de l'intégration des services de reporting et de la technologie SharePoint](http://msdn.microsoft.com/en-us/library/bb326358.aspx)
- [Topologies de déploiement pour Reporting Services en mode intégré SharePoint](http://msdn.microsoft.com/en-us/library/bb510781.aspx)
- [Configuration de Reporting Services pour l'intégration SharePoint 2010](http://msdn.microsoft.com/en-us/library/bb326356.aspx)

{{% /alert %}}

## Configuration de l'environnement

Notre configuration comprend 4 serveurs. Elle comprend un contrôleur de domaine, un serveur SQL, un serveur SharePoint et un serveur pour Reporting Services. Vous pouvez choisir d'avoir SharePoint et Reporting Services sur la même machine, ce qui simplifiera un peu les choses et je soulignerai certaines des différences.

## Pré-requis d'installation

{{% alert color="primary" %}}

L'Add-In Reporting Services pour SharePoint est l'un des composants clés pour faire fonctionner correctement l'intégration. L'Add-In doit être installé sur n'importe quel Web Front End (WFE) de votre ferme SharePoint ainsi que sur le serveur d'administration centrale. Un des nouveaux changements avec SQL 2008 R2 & SharePoint 2010 est que l'Add-In 2008 R2 est désormais un pré-requis pour l'installation de SharePoint. Cela signifie que l'Add-In RS sera déployé lorsque vous installerez SharePoint. Il est montré et mis en évidence dans la figure ci-dessous. Cela évite réellement de nombreux problèmes que nous avons rencontrés avec SP 2007 et RS 2008 lors de l'installation de l'Add-In.

![todo:image_alt_text](introduction_1.png)

**Image1 :- Add-in Reporting Services pour Share Point**
{{% /alert %}}

## Authentification SharePoint

**Avant de plonger dans les éléments d'intégration RS, je veux souligner un point concernant le Farm SharePoint, à savoir comment vous configurez le site. Plus précisément, comment vous configurez l'authentification du site. Que ce soit Classic ou Claims. Ce choix est important dès le début. Je ne crois pas que vous puissiez modifier cette option une fois qu'elle est définie. Si vous pouvez la changer, ce ne serait pas un processus simple.**

NOTE: ***Reporting Services 2008 R2 n'est PAS compatible avec Claims***

Même si vous choisissez que votre site SharePoint utilise les Claims, Reporting Services lui-même n’est pas conscient des Claims. Cela dit, cela affecte le fonctionnement de l’authentification avec Reporting Services. Alors, quelle est la différence du point de vue de Reporting Services ? Tout dépend de si vous voulez transmettre les informations d’identification de l’utilisateur à la source de données. Classic:- Peut utiliser Kerberos et transmettre les informations d’identification de l’utilisateur à votre source de données back end (il faudra utiliser Kerberos pour cela). Claims:- Un jeton Claims est utilisé et non un jeton Windows. RS utilisera toujours l’Authentification de confiance dans ce scénario et n’aura accès qu’au jeton SPUser. Vous devrez stocker vos informations d’identification dans votre source de données.

Classic :- Peut utiliser Kerberos et transmettre les informations d’identification de l’utilisateur à votre source de données back end (il faudra utiliser Kerberos pour cela.

Claims :- Un jeton Claims est utilisé et non un jeton Windows. RS utilisera toujours l’Authentification de confiance dans ce scénario et n’aura accès qu’au jeton SPUser. Vous devrez stocker vos informations d’identification dans votre source de données.

Pour l'instant, nous voulons simplement nous concentrer sur la configuration de RS. À ce stade, SharePoint est installé sur ma SharePoint Box et configuré avec un site d'authentification classique sur le port 80. Sur le serveur RS, je viens d'installer Reporting Services et c'est tout.

