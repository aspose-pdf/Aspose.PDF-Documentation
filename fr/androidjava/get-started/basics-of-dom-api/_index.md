---
title: Bases de l'API DOM Aspose.PDF
linktitle: Bases de l'API DOM
type: docs
weight: 10
url: /fr/androidjava/basics-of-dom-api/
description: Aspose.PDF pour Android via Java utilise également l'idée de DOM pour représenter la structure d'un document PDF sous forme d'objets. Ici vous pouvez lire la description de cette structure.
lastmod: "2026-07-01"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Introduction à l'API DOM

Le modèle d'objet de document (DOM) est une forme de représentation des documents structurés sous forme de modèle orienté objet. Le DOM est le standard officiel du World Wide Web Consortium (W3C) pour représenter les documents structurés de manière neutre vis-à-vis de la plateforme et du langage.

En termes simples, le DOM est un arbre d'objets qui représente la structure d'un document. Aspose.PDF pour Android via Java utilise également l'idée de DOM pour représenter la structure d'un document PDF sous forme d'objets. Cependant, les aspects du DOM (tels que ses Elements) sont manipulés dans la syntaxe du langage de programmation utilisé. L'interface publique d'un DOM est spécifiée dans son interface de programmation d'application (API).

### Introduction au document PDF

Le format de document portable (PDF) est une norme ouverte pour l’échange de documents. Un document PDF est une combinaison de texte et de données binaires. Si vous l’ouvrez dans un éditeur de texte, vous verrez les objets bruts qui définissent la structure et le contenu du document.

La structure logique d’un fichier PDF est hiérarchique et détermine l’ordre dans lequel une application de visualisation dessine les pages du document et leur contenu. Un PDF est composé de quatre composants : objets, structure de fichier, structure du document et flux de contenu.

### Structure du document PDF

Comme la structure d’un fichier PDF est hiérarchique, Aspose.PDF for Java accède également aux éléments de la même manière. La hiérarchie suivante vous montre comment le document PDF est structuré logiquement et comment l’API DOM d’Aspose.PDF for Java le construit.

![Structure du document PDF](https://docs.aspose.com/pdf/java/images/structure.png)

### Accès aux éléments du document PDF

L'objet Document se trouve au niveau racine du modèle d'objets. L'Aspose.PDF for Android via Java DOM API vous permet de créer un objet Document puis d'accéder à tous les autres objets de la hiérarchie. Vous pouvez soit accéder à l'une des collections comme Pages, soit à un élément individuel comme Page, etc. Le DOM API fournit des points d'entrée et de sortie uniques pour manipuler le document PDF comme illustré ci-dessous :

- Ouvrir le document PDF
- Accéder à la structure du document PDF en style DOM
- Mettre à jour les données dans le document PDF
- Valider le document PDF
- Exporter le document PDF vers différents formats
- Enfin, enregistrez le document PDF mis à jour

## Comment utiliser le nouveau Aspose.PDF pour Android via l'API Java

Ce sujet expliquera le nouveau Aspose.PDF pour Android via l'API Java et vous guidera pour commencer rapidement et facilement. Veuillez noter que les détails concernant l'utilisation des fonctionnalités particulières ne font pas partie de cet article.

Le Aspose.PDF pour Android via Java est composé de deux parties :

- Aspose.PDF pour Android via Java DOM API
- Aspose.PDF.Facades 

Vous trouverez les détails de chacune de ces zones ci‑dessous.

### Aspose.PDF pour Android via Java DOM API

La nouvelle Aspose.PDF pour Android via Java DOM API correspond à la structure du document PDF, ce qui vous aide à travailler avec les documents PDF non seulement au niveau du fichier et du document, mais aussi au niveau de l'objet. Nous avons offert davantage de flexibilité aux développeurs pour accéder à tous les éléments et objets du document PDF. En utilisant les classes de l'Aspose.PDF DOM API, vous pouvez obtenir un accès programmatique aux éléments et à la mise en forme du document. Cette nouvelle DOM API comprend plusieurs espaces de noms comme indiqué ci-dessous :

### com.aspose.pdf

Cet espace de noms fournit la classe Document qui vous permet d'ouvrir et d'enregistrer un document PDF. La classe License fait également partie de cet espace de noms. Il fournit également des classes liées aux pages PDF, aux pièces jointes et aux signets, telles que com.aspose.pdf.Page, com.aspose.pdf.PageCollection, com.aspose.pdf.FileSpecification, com.aspose.pdf.EmbeddedFileCollection, com.aspose.pdf.OutlineItemCollection et com.aspose.pdf.OutlineCollection, etc.

#### com.aspose.pdf.text

Cet espace de noms fournit des classes qui vous aident à travailler avec le texte et ses différents aspects, par exemple com.aspose.pdf.Font, com.aspose.pdf.FontCollection, com.aspose.pdf.FontRepository, com.aspose.pdf.FontStyles, com.aspose.pdf.TextAbsorber, com.aspose.pdf.TextFragment, com.aspose.pdf.TextFragmentAbsorber, com.aspose.pdf.TextFragmentCollection, com.aspose.pdf.TextFragmentState, com.aspose.pdf.TextSegment et com.aspose.pdf.TextSegmentCollection, etc.

#### com.aspose.pdf.TextOptions

Cet espace de noms fournit des classes qui vous permettent de définir différentes options pour la recherche, l'édition ou le remplacement du texte, par exemple com.aspose.pdf.TextEditOptions, com.aspose.pdf.TextReplaceOptions et com.aspose.pdf.TextSearchOptions.

#### com.aspose.pdf.PdfAction

Cet espace de noms contient des classes qui vous aident à travailler avec les fonctionnalités interactives du document PDF, par exemple travailler avec le document et d'autres actions. Cet espace de noms contient des classes comme com.aspose.pdf.GoToAction, com.aspose.pdf.GoToRemoteAction et com.aspose.pdf.GoToURIAction, etc.

#### com.aspose.pdf.Annotation

Les annotations font partie des fonctionnalités interactives d’un document PDF. Nous avons dédié un espace de noms aux annotations. Cet espace de noms contient des classes qui vous aident à travailler avec les annotations, par exemple, com.aspose.pdf.Annotation, com.aspose.pdf.AnnotationCollection, com.aspose.pdf.CircleAnnotation et com.aspose.pdf.LinkAnnotation, etc.

#### com.aspose.pdf.Form

Cet espace de noms contient des classes qui vous aident à travailler avec les formulaires PDF et les champs de formulaire, par exemple com.aspose.pdf.Form, com.aspose.pdf.Field, com.aspose.pdf.TextBoxField et com.aspose.pdf.OptionCollection, etc.

#### com.aspose.pdf.devices 

Nous pouvons effectuer diverses opérations sur les documents PDF, comme convertir un document PDF en différents formats d’image. Cependant, ces opérations n’appartiennent pas à l’objet Document et nous ne pouvons pas étendre la classe Document pour de telles opérations. C’est pourquoi nous avons introduit le concept de Device dans la nouvelle API DOM.

##### com.aspose.pdf.facades

Avant Aspose.PDF for Java t.o.o, vous aviez besoin d'Aspose.PDF.Kit for Java pour manipuler les fichiers PDF existants. Pour exécuter l'ancien code Aspose.PDF.Kit, vous pouvez utiliser l'espace de noms com.aspose.pdf.facades.

