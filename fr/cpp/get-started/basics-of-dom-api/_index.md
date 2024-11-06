---
title: Notions de base de Aspose.PDF DOM API
linktitle: Notions de base de DOM API
type: docs
weight: 120
url: fr/cpp/basics-of-dom-api/
description: Aspose.PDF pour C++ utilise également l'idée de DOM pour représenter la structure d'un document PDF en termes d'objets. Ici, vous pouvez lire la description de cette structure.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Introduction à l'API DOM

Le Document Object Model (DOM) est une forme de représentation de documents structurés sous forme de modèle orienté objet. DOM est la norme officielle du World Wide Web Consortium (W3C) pour représenter les documents structurés de manière neutre vis-à-vis de la plateforme et du langage.

En termes simples, le DOM est un arbre d'objets qui représente la structure de certains documents. Aspose.PDF for C++ utilise également l'idée de DOM pour représenter la structure d'un document PDF en termes d'objets. Cependant, les aspects du DOM (comme ses éléments) sont manipulés dans la syntaxe du langage de programmation utilisé. L'interface publique d'un DOM est spécifiée dans son interface de programmation d'application (API).

### Introduction au Document PDF

Le Portable Document Format (PDF) est une norme ouverte pour l'échange de documents. Un document PDF est une combinaison de texte et de données binaires. Si vous l'ouvrez dans un éditeur de texte, vous verrez les objets bruts qui définissent la structure et le contenu du document.

La structure logique d'un fichier PDF est hiérarchique et détermine la séquence par laquelle une application d'affichage dessine les pages du document et leur contenu. Un PDF est composé de quatre composants : les objets, la structure de fichier, la structure du document et les flux de contenu.

### Structure du Document PDF

Comme la structure d'un fichier PDF est hiérarchique, Aspose.PDF pour C++ accède également aux éléments de la même manière. La hiérarchie suivante vous montre comment le document PDF est logiquement structuré et comment Aspose.PDF pour C++ DOM API le construit.

![Structure du Document PDF](../images/structure.png)

### Accéder aux Éléments du Document PDF

L'objet Document est au niveau racine du modèle d'objet. L'API Aspose.PDF pour C++ DOM vous permet de créer un objet Document puis d'accéder à tous les autres objets de la hiérarchie. Vous pouvez soit accéder à l'une des collections comme Pages ou à un élément individuel comme Page, etc. L'API DOM fournit des points d'entrée et de sortie uniques pour manipuler le document PDF comme montré ci-dessous :

- Ouvrir un document PDF
- Accéder à la structure du document PDF en style DOM
- Mettre à jour les données dans le document PDF
- Valider le document PDF
- Exporter le document PDF dans différents formats
- Enfin, enregistrer le document PDF mis à jour

## Comment Utiliser la Nouvelle API Aspose.PDF pour C++

Ce sujet expliquera la nouvelle API Aspose.PDF pour C++ et vous guidera pour commencer rapidement et facilement. Veuillez noter que les détails concernant l'utilisation des fonctionnalités particulières ne font pas partie de cet article.

Le Aspose.PDF pour C++ est composé de deux parties :

- Aspose.PDF pour C++ DOM API
- Aspose.PDF.Facades

Vous trouverez les détails de chacune de ces zones ci-dessous.

### Aspose.PDF pour C++ DOM API

Le Aspose.PDF pour C++ DOM API correspond à la structure du document PDF, ce qui vous aide à travailler avec les documents PDF non seulement au niveau du fichier et du document, mais aussi au niveau de l'objet. Nous avons fourni plus de flexibilité aux développeurs pour accéder à tous les éléments et objets du document PDF. En utilisant les classes de l'API Aspose.PDF DOM, vous pouvez accéder de manière programmatique aux éléments et à la mise en forme du document. Cette nouvelle API DOM est composée de divers espaces de noms comme indiqué ci-dessous :

### Référence de l'espace de noms Aspose::Pdf

Cet espace de noms fournit la classe Document qui vous permet d'ouvrir et de sauvegarder un document PDF.

#### Référence de l'espace de noms Aspose::Pdf::Text

Cet espace de noms fournit des classes qui vous aident à travailler avec le texte et ses divers aspects, par exemple Font, FontCollection, FontRepository, FontSource, TextAbsorber, TextFragment, TextFragmentAbsorber, TextFragmentCollection, TextFragmentState, TextSegment et TextSegmentCollection etc.
#### Aspose::Pdf::Collections Namespace Reference

Ce namespace fournit la classe AsposeHashDictionary.

#### Aspose::Pdf::CommonData Namespace Reference

#### Aspose::Pdf::Diagnostics Namespace Reference

#### Aspose::Pdf::Drawing Namespace Reference

Ce namespace fournit les classes : Curve, Circle, Arc, Rectangle, Graph, etc., pour ajouter des éléments graphiques à votre fichier PDF.

#### Aspose::Pdf::Engine Namespace Reference

Ce namespace fournit les classes Addressing, Interactive, Security, CommonData, IO, Presentation.

#### Aspose::Pdf::GroupProcessor Namespace Reference

Ce namespace fournit les classes : ExtractorFactory - représente une fabrique pour créer des objets IPdfTypeExtractor, IDocumentPageTextExtractor, IDocumentTextExtractor, IPdfTypeExtractor classes - représente une interface pour interagir avec l'extracteur.

#### Aspose::Pdf::Interchange Namespace Reference

#### Aspose::Pdf::LogicalStructure Namespace Reference

Ce namespace fournit les classes : AnnotationElement, AttributeOwnerStandard, CaptionElement, DocumentElement, FormElement, GroupingElement, ILSTextElement, PrivateElement, WarichuWTElement, etc.

#### Aspose::Pdf::Operators Namespace Reference

Ce namespace fournit des classes des opérateurs suivants : BasicSetColorAndPatternOperator, BlockTextOperator, SetCharWidthBoundingBox, SetColorStroke, SetHorizontalTextScaling, SetTextRenderingMode, TextShowOperator, etc.

#### Aspose::Pdf::Optimization Namespace Reference

Ce namespace fournit deux classes - ImageCompressionOptions et OptimizationOptions.

#### Aspose::Pdf::PageModel Namespace Reference

#### Aspose::Pdf::PdfAOptionClasses Namespace Reference

Ce namespace fournit deux classes : FontEmbeddingOptions - la norme PDF/A exige que toutes les polices soient intégrées dans le document. Cette classe inclut des indicateurs pour les cas où il n'est pas possible d'intégrer certaines polices car elles sont absentes sur le PC de destination. ToUnicodeProcessingRules - Cette classe décrit des règles qui peuvent être utilisées pour résoudre l'erreur Adobe Preflight "Le texte ne peut pas être mappé à Unicode".

#### Aspose::Pdf::Sanitization Namespace Reference

Ce namespace fournit deux classes : Details_SanitizationException et IRecovery.

#### Aspose::Pdf::Tagged Namespace Reference

Ce namespace fournit les classes Details_TaggedException - Représente une exception pour le contenu TaggedPDF d'un document. ITaggedContent - Représente une interface pour travailler avec le contenu TaggedPdf d'un document? et TaggedPdfExceptionCode.

#### Aspose::Pdf::Validation Namespace Reference

#### Aspose::Pdf::XfaConverter Namespace Reference

Ce namespace fournit la classe XfaParserOptions - classe pour gérer l'encapsulation des données liées.

#### Aspose::Pdf::Annotations Namespace Reference

Les annotations font partie des fonctionnalités interactives d'un document PDF. Nous avons dédié un namespace pour les annotations. Ce namespace contient des classes qui vous aident à travailler avec les annotations, par exemple, Annotation, AnnotationCollection, CircleAnnotation et LinkAnnotation etc.

#### Aspose::Pdf::Forms Namespace Reference

Ce namespace contient des classes qui vous aident à travailler avec les formulaires PDF et les champs de formulaire, par exemple Form, Field, TextBoxField et OptionCollection etc.

#### Aspose::Pdf::Devices Namespace Reference

Nous pouvons effectuer diverses opérations sur les documents PDF, telles que la conversion d'un document PDF en divers formats d'image. Cependant, de telles opérations n'appartiennent pas à l'objet Document et nous ne pouvons pas étendre la classe Document pour de telles opérations. C'est pourquoi nous avons introduit le concept de Device dans la nouvelle API DOM.

##### Référence de l'espace de noms Aspose::Pdf::Facades

Vous pouvez utiliser l'espace de noms Aspose.PDF.Facades. Cet espace de noms fournit des classes AutoFiller - représente une classe pour recevoir des données d'une base de données ou d'une autre source de données. Bookmark, Form, Stamp, PdfConverter et d'autres classes.