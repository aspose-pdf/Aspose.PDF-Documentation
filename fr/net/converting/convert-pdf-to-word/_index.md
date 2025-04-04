---
title: Convertir des fichiers PDF en documents Microsoft Word dans .NET
linktitle: Convertir PDF en Word
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /fr/net/convert-pdf-to-word/
lastmod: "2022-08-04"
description: Apprenez à écrire du code C# pour la conversion de PDF en formats Microsoft Word avec Aspose.PDF for .NET. et ajustez la conversion PDF en DOC(DOCX).
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Convert PDF to Microsoft Word Documents in .NET",
    "alternativeHeadline": "Seamlessly Convert PDFs to Word Documents with C#",
    "abstract": "Aspose.PDF for .NET introduit une fonctionnalité puissante pour convertir des fichiers PDF en formats Microsoft Word (DOC et DOCX) en utilisant C#. Cette fonctionnalité améliore non seulement l'édition de documents, mais offre également des options flexibles pour la reconnaissance de texte et le formatage, garantissant une haute fidélité entre le PDF source et le document Word résultant.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "1378",
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
    "url": "/net/convert-pdf-to-word/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/convert-pdf-to-word/"
    },
    "dateModified": "2025-04-04",
    "description": "Aspose.PDF peut effectuer non seulement des tâches simples et faciles, mais aussi faire face à des objectifs plus complexes. Consultez la section suivante pour les utilisateurs avancés et les développeurs."
}
</script>

## Aperçu

Cet article explique comment **convertir des fichiers PDF en documents Microsoft Word en utilisant C#**. Il couvre ces sujets.

- [Convertir PDF en DOC](#csharp-pdf-to-doc)
- [Convertir PDF en DOCX](#csharp-pdf-to-docx)

Le code suivant fonctionne également avec la bibliothèque [Aspose.PDF.Drawing](/pdf/fr/net/drawing/).

## Conversion PDF en DOC et DOCX

L'une des fonctionnalités les plus populaires est la conversion PDF en DOC Microsoft Word, qui facilite la gestion du contenu. **Aspose.PDF for .NET** vous permet de convertir des fichiers PDF en format DOC et DOCX rapidement et efficacement.

## Convertir un fichier PDF en DOC (Microsoft Word 97-2003)

Convertissez des fichiers PDF en format DOC avec facilité et contrôle total. Aspose.PDF for .NET est flexible et prend en charge une grande variété de conversions. Par exemple, la conversion de pages de documents PDF en images est une fonctionnalité très populaire.

Beaucoup de nos clients ont demandé une conversion de PDF en DOC : convertir un fichier PDF en document Microsoft Word. Les clients souhaitent cela car les fichiers PDF ne peuvent pas être facilement modifiés, tandis que les documents Word le peuvent. Certaines entreprises veulent que leurs utilisateurs puissent manipuler du texte, des tableaux et des images dans des fichiers qui ont commencé comme des PDF.

En gardant vivante la tradition de rendre les choses simples et compréhensibles, Aspose.PDF for .NET vous permet de transformer un fichier PDF source en un fichier DOC avec deux lignes de code. Pour réaliser cette fonctionnalité, nous avons introduit une énumération nommée SaveFormat et sa valeur .Doc vous permet d'enregistrer le fichier source au format Microsoft Word.

Le code C# suivant montre comment convertir un fichier PDF en format DOC.

<a name="csharp-pdf-to-doc" id="csharp-pdf-to-doc"><strong>Convertir PDF en DOC</strong></a>

1. Créez une instance de l'objet [Document](https://reference.aspose.com/pdf/fr/net/aspose.pdf/document/) avec le document PDF source.
2. Enregistrez-le au format **SaveFormat.Doc** en appelant la méthode **Document.Save()**.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPDFtoWord()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    usnig (var document = new Aspose.Pdf.Document(dataDir + "PDFToDOC.pdf"))
    {
        // Save the file into MS document format
        document.Save(dataDir + "PDFToDOC_out.doc", SaveFormat.Doc);
    }
}
```

### Utilisation de la classe DocSaveOptions

La classe [`DocSaveOptions`](https://reference.aspose.com/pdf/fr/net/aspose.pdf/docsaveoptions) fournit de nombreuses propriétés qui améliorent la conversion des fichiers PDF en format DOC. Parmi ces propriétés, Mode vous permet de spécifier le mode de reconnaissance pour le contenu PDF. Vous pouvez sélectionner n'importe quelle valeur de l'énumération RecognitionMode pour cette propriété. Chacune de ces valeurs a des avantages et des limitations spécifiques :

- Le mode [`Textbox`](https://reference.aspose.com/pdf/fr/net/aspose.pdf.docsaveoptions/recognitionmode) est rapide et bon pour préserver l'apparence originale du fichier PDF, mais l'éditabilité du document résultant pourrait être limitée. Chaque bloc de texte visuellement groupé dans le PDF original est converti en une zone de texte dans le document de sortie. Cela atteint une ressemblance maximale avec l'original, donc le document de sortie a une bonne apparence, mais il est entièrement composé de zones de texte, ce qui pourrait être difficile à modifier dans Microsoft Word.
- Le mode [`Flow`](https://reference.aspose.com/pdf/fr/net/aspose.pdf.docsaveoptions/recognitionmode) est un mode de reconnaissance complet, où le moteur effectue un regroupement et une analyse multi-niveaux pour restaurer le document original selon l'intention de l'auteur tout en produisant un document facilement modifiable. La limitation est que le document de sortie pourrait sembler différent de l'original.

La propriété [`RelativeHorizontalProximity`](https://reference.aspose.com/pdf/fr/net/aspose.pdf/docsaveoptions/properties/relativehorizontalproximity) peut être utilisée pour contrôler la proximité relative entre les éléments textuels. Cela signifie que la distance est normalisée par la taille de la police. Les polices plus grandes peuvent avoir des espaces plus grands entre les syllabes et être considérées comme un tout unique. Elle est spécifiée en pourcentage de la taille de la police ; par exemple, 1 = 100 %. Cela signifie que deux caractères de 12pt placés à 12 pt de distance sont proximaux.
- [`RecognitionBullets`](https://reference.aspose.com/pdf/fr/net/aspose.pdf/docsaveoptions/properties/recognizebullets) est utilisé pour activer la reconnaissance des puces lors de la conversion.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPDFtoWordDocAdvanced()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();
    
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "PDF-to-DOC.pdf"))
    {
        var saveOptions = new Aspose.Pdf.DocSaveOptions
        {
            // Set format to save MS document
            Format = Aspose.Pdf.DocSaveOptions.DocFormat.Doc,
            // Set the recognition mode as Flow
            Mode = Aspose.Pdf.DocSaveOptions.RecognitionMode.Flow,
            // Set the Horizontal proximity as 2.5
            RelativeHorizontalProximity = 2.5f,
            // Enable the value to recognize bullets during the conversion process
            RecognizeBullets = true
        };
        // Save the file into MS document with save options
        document.Save(dataDir + "PDFtoDOC_out.doc", saveOptions);
    }
}
```

{{% alert color="success" %}}
**Essayez de convertir PDF en DOC en ligne**

Aspose.PDF for .NET vous présente une application en ligne gratuite ["PDF to DOC"](https://products.aspose.app/pdf/conversion/pdf-to-doc), où vous pouvez essayer d'explorer la fonctionnalité et la qualité de son fonctionnement.

[![Convertir PDF en DOC](/pdf/fr/net/images/pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-doc)
{{% /alert %}}

## Convertir un fichier PDF en DOCX (Microsoft Word 2007-2024)

L'API Aspose.PDF for .NET vous permet de lire et de convertir des documents PDF en DOCX en utilisant C# et n'importe quel langage .NET. DOCX est un format bien connu pour les documents Microsoft Word dont la structure a été modifiée d'un binaire simple à une combinaison de fichiers XML et binaires. Les fichiers Docx peuvent être ouverts avec Word 2007 et les versions ultérieures, mais pas avec les versions antérieures de MS Word, qui prennent en charge les extensions de fichier DOC.

Le code C# suivant montre comment convertir un fichier PDF en format DOCX.

<a name="csharp-pdf-to-docx" id="csharp-pdf-to-docx"><strong>Convertir PDF en DOCX</strong></a>

1. Créez une instance de l'objet [Document](https://reference.aspose.com/pdf/fr/net/aspose.pdf/document/) avec le document PDF source.
2. Enregistrez-le au format **SaveFormat.DocX** en appelant la méthode **Document.Save()**.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPDFtoWord_DOCX_Format()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "PDFToDOC.pdf"))
    {
        // Save the file into MS document format
        document.Save(dataDir + "PDFtoDOC_out.docx", SaveFormat.DocX);
    }
}
```

### Convertir PDF en DOCX en mode amélioré

Pour obtenir de meilleurs résultats de conversion PDF en DOCX, vous pouvez utiliser le mode `EnhancedFlow`.
La principale différence entre Flow et Enhanced Flow est que les tableaux (avec et sans bordures) sont reconnus comme de véritables tableaux, et non comme du texte avec une image en arrière-plan.
Il y a également reconnaissance des listes numérotées et de nombreuses autres petites choses.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPDFtoWord_Advanced_DOCX_Format()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "PDFToDOC.pdf"))
    {
        // Instantiate DocSaveOptions object
        DocSaveOptions saveOptions = new Aspose.Pdf.DocSaveOptions
        {
            // Set format to save MS document
            Format = Aspose.Pdf.DocSaveOptions.DocFormat.DocX,
            // Set the recognition mode as EnhancedFlow
            Mode = Aspose.Pdf.DocSaveOptions.RecognitionMode.EnhancedFlow
        };

        // Save the file into MS document format
        document.Save(dataDir + "PDFToDOC_out.docx", saveOptions);
    }
}
```

{{% alert color="warning" %}}
**Essayez de convertir PDF en DOCX en ligne**

Aspose.PDF for .NET vous présente une application en ligne gratuite ["PDF to Word"](https://products.aspose.app/pdf/conversion/pdf-to-docx), où vous pouvez essayer d'explorer la fonctionnalité et la qualité de son fonctionnement.

[![Aspose.PDF Conversion PDF en Word Application Gratuite](/pdf/fr/net/images/pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-docx)

{{% /alert %}}