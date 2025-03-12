---
title: Bases de l'API DOM d'Aspose.PDF
linktitle: Bases de l'API DOM
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 130
url: /fr/net/basics-of-dom-api/
description: Aspose.PDF for .NET utilise également l'idée de DOM pour représenter la structure d'un document PDF en termes d'objets.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Basics of Aspose.PDF DOM API",
    "alternativeHeadline": "Enhanced PDF Manipulation with Aspose.PDF DOM API in C#",
    "abstract": "La nouvelle API DOM Aspose.PDF for .NET fournit une approche orientée objet robuste pour manipuler les documents PDF en représentant leur structure sous forme d'arbre hiérarchique. Cette fonctionnalité permet aux développeurs d'accéder facilement, de mettre à jour et d'exporter des éléments PDF tout en améliorant la flexibilité et le contrôle sur la manipulation des documents grâce à une interface de programmation intuitive.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "891",
    "proficiencyLevel": "Beginner",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF for .NET",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
        "alternateName": "Aspose",
        "sameAs": [
            "https://facebook.com/aspose.pdf/",
            "https://twitter.com/asposepdf",
            "https://www.youtube.com/channel/UCmV9sEg_QWYPi6BJJs7ELOg/featured",
            "https://www.linkedin.com/company/aspose",
            "https://stackoverflow.com/questions/tagged/aspose",
            "https://aspose.quora.com/",
            "https://aspose.github.io/"
        ],
        "contactPoint": [
            {
                "@type": "ContactPoint",
                "telephone": "+1 903 306 1676",
                "contactType": "sales",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "sales",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "sales",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "url": "/net/basics-of-dom-api/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/basics-of-dom-api/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF peut effectuer non seulement des tâches simples et faciles, mais aussi faire face à des objectifs plus complexes. Consultez la section suivante pour les utilisateurs et développeurs avancés."
}
</script>

## Introduction à l'API DOM

Le Document Object Model (DOM) est une forme de représentation de documents structurés sous forme de modèle orienté objet. Le DOM est la norme officielle du World Wide Web Consortium (W3C) pour représenter des documents structurés de manière neutre par rapport à la plateforme et au langage.

En termes simples, le DOM est un arbre d'objets qui représente la structure d'un document. Aspose.PDF for .NET utilise également l'idée de DOM pour représenter la structure d'un document PDF en termes d'objets. Cependant, les aspects du DOM (comme ses éléments) sont manipulés dans la syntaxe du langage de programmation utilisé. L'interface publique d'un DOM est spécifiée dans son interface de programmation d'application (API).

### Introduction au document PDF

Le format de document portable (PDF) est une norme ouverte pour l'échange de documents. Un document PDF est une combinaison de texte et de données binaires. Si vous l'ouvrez dans un éditeur de texte, vous verrez les objets bruts qui définissent la structure et le contenu du document.

La structure logique d'un fichier PDF est hiérarchique et détermine la séquence par laquelle une application de visualisation dessine les pages du document et leur contenu. Un PDF est composé de quatre composants : objets, structure de fichier, structure de document et flux de contenu.

### Structure du document PDF

Comme la structure d'un fichier PDF est hiérarchique, Aspose.PDF for .NET accède également aux éléments de la même manière. La hiérarchie suivante vous montre comment le document PDF est logiquement structuré et comment l'API DOM Aspose.PDF for .NET le construit.

![Structure du document PDF](../images/structure.png)

### Accéder aux éléments du document PDF

L'objet Document est au niveau racine du modèle d'objet. L'API DOM Aspose.PDF for .NET vous permet de créer un objet Document et ensuite d'accéder à tous les autres objets dans la hiérarchie. Vous pouvez soit accéder à l'une des collections comme Pages ou à un élément individuel comme Page, etc. L'API DOM fournit des points d'entrée et de sortie uniques pour manipuler le document PDF comme indiqué ci-dessous :

- Ouvrir le document PDF.
- Accéder à la structure du document PDF de manière DOM.
- Mettre à jour les données dans le document PDF.
- Valider le document PDF.
- Exporter le document PDF dans différents formats.
- Enfin, enregistrer le document PDF mis à jour.

## Comment utiliser la nouvelle API Aspose.PDF for .NET

Ce sujet expliquera la nouvelle API Aspose.PDF for .NET et vous guidera pour commencer rapidement et facilement. Veuillez noter que les détails concernant l'utilisation des fonctionnalités particulières ne font pas partie de cet article.

Le Aspose.PDF for .NET est composé de deux parties :

- API DOM Aspose.PDF for .NET.
- Aspose.Pdf.Facades (ancien Aspose.PDF.Kit pour .NET).

Vous trouverez les détails de chacune de ces zones ci-dessous.

### API DOM Aspose.PDF for .NET

L'API DOM Aspose.PDF for .NET correspond à la structure du document PDF, ce qui vous aide à travailler avec les documents PDF non seulement au niveau du fichier et du document, mais aussi au niveau de l'objet. Nous avons fourni plus de flexibilité aux développeurs pour accéder à tous les éléments et objets du document PDF. En utilisant les classes de l'API DOM d'Aspose.PDF, vous pouvez obtenir un accès programmatique aux éléments et à la mise en forme du document. Cette nouvelle API DOM est composée de divers espaces de noms comme indiqué ci-dessous :

### Aspose.PDF

Cet espace de noms fournit la classe Document qui vous permet d'ouvrir et d'enregistrer un document PDF. La classe License fait également partie de cet espace de noms. Il fournit également des classes liées aux pages PDF, aux pièces jointes et aux signets comme Page, PageCollection, FileSpecification, EmbeddedFileCollection, OutlineItemCollection et OutlineCollection, etc.

#### Aspose.Text

Cet espace de noms fournit des classes qui vous aident à travailler avec le texte et ses divers aspects, par exemple Font, FontCollection, FontRepository, FontStyles, TextAbsorber, TextFragment, TextFragmentAbsorber, TextFragmentCollection, TextFragmentState, TextSegment et TextSegmentCollection, etc.

#### Aspose.Text.TextOptions

Cet espace de noms fournit des classes qui vous permettent de définir différentes options pour rechercher, éditer ou remplacer du texte, par exemple TextEditOptions, TextReplaceOptions et TextSearchOptions.

#### Aspose.InteractiveFeatures

Cet espace de noms contient des classes qui vous aident à travailler avec les fonctionnalités interactives du document PDF, par exemple travailler avec le document et d'autres actions. Cet espace de noms contient des classes comme GoToAction, GoToRemoteAction et GoToURIAction, etc.

#### Aspose.InteractiveFeatures.Annotations

Les annotations font partie des fonctionnalités interactives d'un document PDF. Nous avons dédié un espace de noms aux annotations. Cet espace de noms contient des classes qui vous aident à travailler avec les annotations, par exemple, Annotation, AnnotationCollection, CircleAnnotation et LinkAnnotation, etc.

#### Aspose.InteractiveFeatures.Forms

Cet espace de noms contient des classes qui vous aident à travailler avec les formulaires PDF et les champs de formulaire, par exemple Form, Field, TextBoxField et OptionCollection, etc.

#### Aspose.Pdf.Devices

Nous pouvons effectuer diverses opérations sur les documents PDF, comme convertir un document PDF en divers formats d'image. Cependant, de telles opérations n'appartiennent pas à l'objet Document et nous ne pouvons pas étendre la classe Document pour de telles opérations. C'est pourquoi nous avons introduit le concept de Device dans la nouvelle API DOM.

#### Aspose.Pdf.Facades

Avant Aspose.PDF for .NET, vous aviez besoin d'Aspose.PDF.Kit pour .NET pour manipuler des fichiers PDF existants. Pour exécuter l'ancien code Aspose.PDF.Kit, vous pouvez utiliser l'espace de noms Aspose.PDF.Facades.