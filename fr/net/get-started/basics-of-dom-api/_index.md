---
title: Principes de base de l'API DOM Aspose.PDF
linktitle: Principes de base de l'API DOM
type: docs
weight: 140
url: /fr/net/basics-of-dom-api/
description: Aspose.PDF pour .NET utilise également l'idée de DOM pour représenter la structure d'un document PDF en termes d'objets.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Introduction à l'API DOM

Le Modèle d'Objet de Document (DOM) est une forme de représentation des documents structurés comme un modèle orienté objet. DOM est la norme officielle du World Wide Web Consortium (W3C) pour représenter les documents structurés de manière neutre en termes de plateforme et de langue.

En termes simples, DOM est un arbre d'objets qui représentent la structure d'un document.
En des mots simples, le DOM est un arbre d'objets qui représente la structure de certains documents.

### Introduction au document PDF

Le format de document portable (PDF) est une norme ouverte pour l'échange de documents. Un document PDF est une combinaison de texte et de données binaires. Si vous l'ouvrez dans un éditeur de texte, vous verrez les objets bruts qui définissent la structure et le contenu du document.

La structure logique d'un fichier PDF est hiérarchique et détermine la séquence par laquelle une application de visualisation dessine les pages du document et leur contenu. Un PDF est composé de quatre composants : objets, structure de fichier, structure de document et flux de contenu.

### Structure du document PDF

Comme la structure d'un fichier PDF est hiérarchique, Aspose.PDF pour .NET accède également aux éléments de la même manière. La hiérarchie suivante vous montre comment le document PDF est structuré logiquement et comment l'API DOM Aspose.PDF pour .NET le construit.

![Structure du document PDF](../images/structure.png)

### Accès aux éléments du document PDF

L'objet Document est au niveau racine du modèle objet.
L'objet Document est au niveau racine du modèle d'objet.

- Ouvrir le document PDF
- Accéder à la structure du document PDF dans le style DOM
- Mettre à jour les données dans le document PDF
- Valider le document PDF
- Exporter le document PDF dans différents formats
- Enfin, sauvegarder le document PDF mis à jour

## Comment utiliser la nouvelle API Aspose.PDF pour .NET

Ce sujet expliquera la nouvelle API Aspose.PDF pour .NET et vous guidera pour démarrer rapidement et facilement. Veuillez noter que les détails concernant l'utilisation des fonctionnalités particulières ne font pas partie de cet article.

L'Aspose.PDF pour .NET est composé de deux parties :

- Aspose.PDF pour .NET DOM API
- Aspose.PDF.Facades (anciennement Aspose.PDF.Kit pour .NET)
Vous trouverez ci-dessous les détails de chacun de ces domaines.

### Aspose.PDF pour .NET DOM API

L'API DOM Aspose.PDF pour .NET correspond à la structure du document PDF, ce qui vous aide à travailler avec les documents PDF non seulement au niveau du fichier et du document, mais aussi au niveau de l'objet.
L'API DOM Aspose.PDF pour .NET correspond à la structure du document PDF, ce qui vous aide à travailler avec les documents PDF non seulement au niveau du fichier et du document, mais aussi au niveau de l'objet.

### Aspose.PDF

Cet espace de noms fournit la classe Document qui vous permet d'ouvrir et de sauvegarder un document PDF. La classe License fait également partie de cet espace de noms. Il fournit également des classes liées aux pages PDF, aux pièces jointes et aux signets comme Page, PageCollection, FileSpecification, EmbeddedFileCollection, OutlineItemCollection et OutlineCollection, etc.

#### Aspose.Text

Cet espace de noms fournit des classes qui vous aident à travailler avec le texte et ses différents aspects, par exemple Font, FontCollection, FontRepository, FontStyles, TextAbsorber, TextFragment, TextFragmentAbsorber, TextFragmentCollection, TextFragmentState, TextSegment et TextSegmentCollection, etc.

#### Aspose.Text.TextOptions

Cet espace de noms fournit des classes qui vous permettent de définir différentes options pour rechercher, éditer ou remplacer du texte, par exemple TextEditOptions, TextReplaceOptions et TextSearchOptions.
Cet espace de noms fournit des classes qui vous permettent de définir différentes options pour la recherche, l'édition ou le remplacement de texte, par exemple TextEditOptions, TextReplaceOptions et TextSearchOptions.

#### Aspose.InteractiveFeatures

Cet espace de noms contient des classes qui vous aident à travailler avec les fonctionnalités interactives du document PDF, par exemple travailler avec le document et d'autres actions. Cet espace de noms contient des classes comme GoToAction, GoToRemoteAction et GoToURIAction, etc.

#### Aspose.InteractiveFeatures.Annotations

Les annotations font partie des fonctionnalités interactives d'un document PDF. Nous avons dédié un espace de noms pour les annotations. Cet espace de noms contient des classes qui vous aident à travailler avec les annotations, par exemple, Annotation, AnnotationCollection, CircleAnnotation et LinkAnnotation, etc.

#### Aspose.InteractiveFeatures.Forms

Cet espace de noms contient des classes qui vous aident à travailler avec les formulaires PDF et les champs de formulaire, par exemple Form, Field, TextBoxField et OptionCollection, etc.

#### Aspose.PDF.Devices

Nous pouvons effectuer diverses opérations sur les documents PDF telles que la conversion d'un document PDF en divers formats d'image.
Nous pouvons effectuer diverses opérations sur les documents PDF, telles que convertir un document PDF en différents formats d'image.

##### Aspose.PDF.Facades

Avant Aspose.PDF pour .NET, vous aviez besoin d'Aspose.PDF.Kit pour .NET pour manipuler les fichiers PDF existants. Pour exécuter l'ancien code Aspose.PDF.Kit, vous pouvez utiliser l'espace de noms Aspose.PDF.Facades.
