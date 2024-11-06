---
title: Module d'importation de PDF Umbraco
type: docs
weight: 10
url: fr/net/umbraco-pdf-import-module/
description: Apprenez à installer et utiliser le module d'importation de PDF Umbraco
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

## Introduction

**Aspose.PDF pour .NET** est un composant de création et de manipulation de documents PDF qui permet à vos applications .NET de lire, écrire et manipuler des documents PDF existants sans utiliser Adobe Acrobat. Il vous permet également de créer des formulaires et de gérer les champs de formulaires intégrés dans un document PDF.

**Aspose.PDF pour .NET** est abordable et offre une richesse incroyable de fonctionnalités incluant des options de compression PDF; création et manipulation de tableaux; prise en charge des objets graphiques; fonctionnalité de lien hypertexte étendue; contrôles de sécurité avancés; gestion des polices personnalisées; intégration avec des sources de données; ajouter ou retirer des signets; créer une table des matières; ajouter, mettre à jour, supprimer des pièces jointes et des annotations; importer ou exporter des données de formulaire PDF; ajouter, remplacer ou retirer du texte et des images; diviser, concaténer, extraire ou insérer des pages; transformer des pages en image; imprimer des documents PDF et bien plus encore.
**Aspose.PDF pour .NET** est abordable et offre une richesse incroyable de fonctionnalités incluant les options de compression PDF ; création et manipulation de tableaux ; prise en charge des objets graphiques ; fonctionnalité de lien hypertexte étendue ; contrôles de sécurité avancés ; gestion des polices personnalisées ; intégration avec des sources de données ; ajouter ou retirer des signets ; créer une table des matières ; ajouter, mettre à jour, supprimer des pièces jointes et des annotations ; importer ou exporter des données de formulaire PDF ; ajouter, remplacer ou retirer du texte et des images ; diviser, concaténer, extraire ou insérer des pages ; transformer des pages en image ; imprimer des documents PDF et bien plus encore

### **Fonctionnalités du Module**

Umbraco PDF Import est un module complémentaire open source de [Aspose](http://www.aspose.com/) qui permet aux développeurs d'obtenir/lire le contenu de tout document PDF sans nécessiter d'autre logiciel.
Umbraco PDF Import est un module open source de [Aspose](http://www.aspose.com/) qui permet aux développeurs de lire le contenu de tout document PDF sans nécessiter d'autres logiciels.

## Exigences du système et plateformes prises en charge

### **Exigences du système**

Pour configurer le module Aspose .NET Pdf Import pour Umbraco, vous devez répondre aux exigences suivantes :

- Umbraco 6.0 +

N'hésitez pas à nous contacter si vous souhaitez installer ce module sur d'autres versions d'Umbraco.

### **Plateformes prises en charge**

Le module est pris en charge sur toutes les versions de

- Umbraco fonctionnant sur ASP.NET 4.0

## Téléchargement

Vous pouvez télécharger Aspose .NET Pdf Import pour Umbraco à partir de l'un des emplacements suivants

- [CodePlex](https://asposeumbraco.codeplex.com/releases)
- [Github](https://github.com/asposemarketplace/Aspose_for_Umbraco/releases)
- [Sourceforge](https://sourceforge.net/projects/asposeumbraco/files/)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-umbraco/downloads)
- [Umbraco](https://our.umbraco.org/projects/developer-tools/import-from-pdf-using-aspose-pdf)
- [Umbraco](https://our.umbraco.org/projects/developer-tools/import-from-pdf-using-aspose-pdf)

## Installation

Une fois téléchargé, veuillez suivre ces étapes pour installer ce package sur votre site Umbraco :

1. Connectez-vous à la section **Développeur** d'Umbraco, par exemple <http://www.myblog.com/umbraco/>
1. Dans l'arborescence, déployez le dossier **Packages**.
   À partir de là, il y a deux manières d'installer un package : sélectionnez **Installer le package local** ou parcourez le **Répertoire des packages Umbraco.**
1. Si vous installez un **package local**, ne décompressez pas le package mais chargez le zip dans Umbraco.
1. Suivez les instructions à l'écran.

**Note :** Vous pourriez recevoir une erreur ‘Maximum request length exceeded’ lors de l'installation. Vous pouvez facilement résoudre ce problème en mettant à jour la valeur ‘maxRequestLength’ dans votre fichier web.config d'Umbraco.

```xml
  <httpRuntime requestValidationMode="2.0" enableVersionHeader="false" maxRequestLength="25000" />
```

## Utilisation

Après avoir installé le macro, il est vraiment simple de commencer à l'utiliser sur votre site web :

1.
1.
1. Cliquez sur **Paramètres** dans la liste des sections en bas à gauche de l'écran.
1. Déployez le nœud **Modèles** et sélectionnez le modèle auquel vous souhaitez ajouter un macro, par exemple Blog post.
1. Sélectionnez la position dans le modèle sélectionné où vous souhaitez placer le bouton.
1. Cliquez sur **Insérer un Macro** dans la barre supérieure.
1. Dans **Choisir un macro**, sélectionnez le macro installé et cliquez sur **OK**.

Vous avez réussi à ajouter le modèle. Un bouton intitulé **Importer depuis Pdf** apparaît désormais sur toutes les pages créées à l'aide de ce modèle. N'importe qui peut simplement cliquer sur le bouton et importer le contenu d'un document PDF.

## Démonstration Vidéo

Veuillez consulter [la vidéo](https://www.youtube.com/watch?v=zmZTJ86B25E) ci-dessous pour voir le module en action.

## Support, Étendre et Contribuer

### Support

Dès les premiers jours d'Aspose, nous savions que donner simplement de bons produits à nos clients ne serait pas suffisant.
Dès les premiers jours d'Aspose, nous savions que simplement offrir de bons produits à nos clients ne serait pas suffisant.

C'est pourquoi nous offrons un support gratuit. Quiconque utilise notre produit, qu'il l'ait acheté ou qu'il utilise une évaluation, mérite toute notre attention et notre respect.

Vous pouvez signaler tout problème ou suggestion lié à Aspose.PDF .NET pour les modules Umbraco sur l'une des plateformes suivantes :

- [CodePlex](https://asposeumbraco.codeplex.com/workitem/list/basic)
- [Github](https://github.com/asposemarketplace/Aspose_for_Umbraco/issues)
- [Sourceforge](https://sourceforge.net/p/asposeumbraco/tickets/?source=navbar)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-umbraco/issues?status=new&status=open)

#### Importation depuis Pdf

- [Réseau de développeurs Microsoft - Q et R](https://code.msdn.microsoft.com/Umbraco-Import-from-Pdf-d4659bc8/view/Discussions#content)

### Étendre et contribuer

Aspose .NET PDF Import pour Umbraco est open source et son code source est disponible sur les principaux sites de codage social listés ci-dessous.
Aspose .NET PDF Import pour Umbraco est open source et son code source est disponible sur les principaux sites de codage social listés ci-dessous.

#### Code Source

Vous pouvez obtenir le dernier code source à partir de l'un des emplacements suivants :

- [CodePlex](https://asposeumbraco.codeplex.com/SourceControl/latest)
- [Github](https://github.com/asposemarketplace/Aspose_for_Umbraco)
- [Sourceforge](https://sourceforge.net/p/asposeumbraco/code/ci/master/tree/)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-umbraco/src)

#### Comment configurer le code source

Vous devez avoir installé ce qui suit pour ouvrir et étendre le code source :

- Visual Studio 2010 ou supérieur

Veuillez suivre ces étapes simples pour commencer :

1. Téléchargez/Clonez le code source.
1. Ouvrez Visual Studio 2010 et choisissez **Fichier** > **Ouvrir Projet**
1. Parcourez jusqu'au dernier code source que vous avez téléchargé et ouvrez **Aspose.Import from PDF.sln**
