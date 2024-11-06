---
title: Notions de base de l'API DOM Aspose.PDF
linktitle: Notions de base de l'API DOM
type: docs
weight: 110
url: pt/python-java/basics-of-dom-api/
description: Aspose.PDF pour Java utilise également l'idée de DOM pour représenter la structure d'un document PDF en termes d'objets. Ici, vous pouvez lire la description de cette structure.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Introduction à l'API DOM

Le Document Object Model (DOM) est une forme de représentation de documents structurés en tant que modèle orienté objet. Le DOM est la norme officielle du World Wide Web Consortium (W3C) pour représenter les documents structurés de manière neutre en termes de plateforme et de langage.

En termes simples, le DOM est un arbre d'objets qui représente la structure d'un document.
 Aspose.PDF pour Java utilise également l'idée de DOM pour représenter la structure d'un document PDF en termes d'objets. Cependant, les aspects du DOM (tels que ses Éléments) sont manipulés dans la syntaxe du langage de programmation utilisé. L'interface publique d'un DOM est spécifiée dans son interface de programmation d'application (API).

### Introduction au Document PDF

Le format de document portable (PDF) est une norme ouverte pour l'échange de documents. Un document PDF est une combinaison de texte et de données binaires. Si vous l'ouvrez dans un éditeur de texte, vous verrez les objets bruts qui définissent la structure et le contenu du document.

La structure logique d'un fichier PDF est hiérarchique et détermine la séquence par laquelle une application de visualisation dessine les pages du document et leur contenu. Un PDF est composé de quatre composants : objets, structure de fichier, structure de document et flux de contenu.

### Structure du Document PDF

Comme la structure d'un fichier PDF est hiérarchique, Aspose.PDF pour Java accède également aux éléments de la même manière. La hiérarchie suivante vous montre comment le document PDF est structuré logiquement et comment Aspose.PDF pour l'API DOM Java le construit.

![Structure du Document PDF](../images/structure.png)

### Accéder aux Éléments du Document PDF

L'objet Document est au niveau racine du modèle objet. L'API DOM Aspose.PDF pour Java vous permet de créer un objet Document puis d'accéder à tous les autres objets de la hiérarchie. Vous pouvez soit accéder à l'une des collections comme Pages ou à un élément individuel comme Page, etc. L'API DOM fournit des points d'entrée et de sortie uniques pour manipuler le document PDF comme indiqué ci-dessous :

- Ouvrir le document PDF
- Accéder à la structure du document PDF dans le style DOM
- Mettre à jour les données dans le document PDF
- Valider le document PDF
- Exporter le document PDF dans différents formats
- Enfin, sauvegarder le document PDF mis à jour

## Comment Utiliser la Nouvelle API Aspose.PDF pour Java

Ce sujet expliquera la nouvelle API Aspose.PDF pour Java et vous guidera pour commencer rapidement et facilement. Veuillez noter que les détails concernant l'utilisation des fonctionnalités particulières ne font pas partie de cet article.

Aspose.PDF pour Java est composé de deux parties :

- Aspose.PDF pour Java DOM API
- Aspose.PDF.Facades

Vous trouverez ci-dessous les détails de chacune de ces parties.

### Aspose.PDF pour Java DOM API

La nouvelle API DOM d'Aspose.PDF pour Java correspond à la structure du document PDF, ce qui vous aide à travailler avec les documents PDF non seulement au niveau du fichier et du document, mais aussi au niveau de l'objet. Nous avons offert plus de flexibilité aux développeurs pour accéder à tous les éléments et objets du document PDF. En utilisant les classes de l'API DOM d'Aspose.PDF, vous pouvez obtenir un accès programmatique aux éléments et au formatage du document. Cette nouvelle API DOM est composée de divers espaces de noms comme indiqué ci-dessous :

### com.aspose.pdf

Cet espace de noms fournit la classe Document qui vous permet d'ouvrir et d'enregistrer un document PDF. La classe License fait également partie de cet espace de noms. Elle fournit également des classes liées aux pages PDF, aux pièces jointes et aux signets comme com.aspose.pdf.Page, com.aspose.pdf.PageCollection, com.aspose.pdf.FileSpecification, com.aspose.pdf.EmbeddedFileCollection, com.aspose.pdf.OutlineItemCollection, et com.aspose.pdf.OutlineCollection, etc.

#### com.aspose.pdf.text

Cet espace de noms fournit des classes qui vous aident à travailler avec le texte et ses divers aspects, par exemple com.aspose.pdf.Font, com.aspose.pdf.FontCollection, com.aspose.pdf.FontRepository, com.aspose.pdf.FontStyles, com.aspose.pdf.TextAbsorber, com.aspose.pdf.TextFragment, com.aspose.pdf.TextFragmentAbsorber, com.aspose.pdf.TextFragmentCollection, com.aspose.pdf.TextFragmentState, com.aspose.pdf.TextSegment et com.aspose.pdf.TextSegmentCollection, etc.

#### com.aspose.pdf.TextOptions

Cet espace de noms fournit des classes qui vous permettent de définir différentes options pour rechercher, éditer ou remplacer du texte, par exemple com.aspose.pdf.TextEditOptions, com.aspose.pdf.TextReplaceOptions, et com.aspose.pdf.TextSearchOptions.
#### com.aspose.pdf.PdfAction

Ce namespace contient des classes qui vous aident à travailler avec les fonctionnalités interactives du document PDF, par exemple travailler avec le document et d'autres actions. Ce namespace contient des classes comme com.aspose.pdf.GoToAction, com.aspose.pdf.GoToRemoteAction et com.aspose.pdf.GoToURIAction, etc.

#### com.aspose.pdf.Annotation

Les annotations font partie des fonctionnalités interactives d'un document PDF. Nous avons dédié un namespace pour les annotations. Ce namespace contient des classes qui vous aident à travailler avec les annotations, par exemple, com.aspose.pdf.Annotation, com.aspose.pdf.AnnotationCollection, com.aspose.pdf.CircleAnnotation et com.aspose.pdf.LinkAnnotation, etc.

#### com.aspose.pdf.Form

Ce namespace contient des classes qui vous aident à travailler avec les formulaires PDF et les champs de formulaire, par exemple com.aspose.pdf.Form, com.aspose.pdf.Field, com.aspose.pdf.TextBoxField et com.aspose.pdf.OptionCollection, etc.

#### com.aspose.pdf.devices

Nous pouvons effectuer diverses opérations sur les documents PDF, telles que convertir un document PDF en différents formats d'image.
 Cependant, de telles opérations n'appartiennent pas à l'objet Document et nous ne pouvons pas étendre la classe Document pour de telles opérations. C'est pourquoi nous avons introduit le concept de Device dans la nouvelle API DOM.

##### com.aspose.pdf.facades

Avant Aspose.PDF pour Java, vous aviez besoin d'Aspose.PDF.Kit pour Java pour manipuler des fichiers PDF existants. Pour exécuter l'ancien code Aspose.PDF.Kit, vous pouvez utiliser l'espace de noms com.aspose.pdf.facades.