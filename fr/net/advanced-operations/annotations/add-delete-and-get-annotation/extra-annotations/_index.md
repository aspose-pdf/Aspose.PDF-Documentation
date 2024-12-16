---
title: Extra Annotations using C#
linktitle: Extra Annotations
type: docs
weight: 60
url: /fr/net/extra-annotations/
description: Cette section décrit comment ajouter, obtenir et supprimer des types supplémentaires d'annotations de votre document PDF.
lastmod: "2023-09-12"
sitemap:
    changefreq: "monthly"
    priority: 0.5
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Extra Annotations using C#",
    "alternativeHeadline": "How to add Extra Annotations in PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "pdf, c#, link annotation, caret annotation",
    "wordcount": "302",
    "proficiencyLevel":"Beginner",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF Doc Team",
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
    "url": "/net/extra-annotations/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/extra-annotations/"
    },
    "dateModified": "2022-02-04",
    "description": "Cette section décrit comment ajouter, obtenir et supprimer des types supplémentaires d'annotations de votre document PDF."
}
</script>
## Comment ajouter une annotation de point d'insertion dans un fichier PDF existant

L'annotation de point d'insertion est un symbole qui indique l'édition de texte. L'annotation de point d'insertion est également une annotation de balisage, donc la classe Caret dérive de la classe Markup et fournit également des fonctions pour obtenir ou définir les propriétés de l'annotation de point d'insertion et réinitialiser le flux de l'apparence de l'annotation de point d'insertion.

Le code suivant fonctionne également avec la bibliothèque [Aspose.PDF.Drawing](/pdf/fr/net/drawing/).

Étapes avec lesquelles nous créons une annotation de point d'insertion :

1. Charger le fichier PDF - nouveau [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).
1. Créer une nouvelle [Annotation de point d'insertion](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/caretannotation) et définir les paramètres du point d'insertion (nouveau Rectangle, titre, sujet, drapeaux, couleur, largeur, style de début et style de fin). Cette annotation est utilisée pour indiquer l'insertion de texte.
1.
1. Créer une nouvelle [StrikeOutAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/strikeoutannotation) et définir les paramètres (nouveau Rectangle, titre, couleur, nouveaux QuadPoints et nouveaux points, Sujet, InReplyTo, ReplyType).
1. Ensuite, nous pouvons ajouter des annotations à la page.

Le code suivant montre comment ajouter une annotation Caret à un fichier PDF :

```csharp
using Aspose.Pdf.Annotations;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Aspose.Pdf.Examples.Advanced
{
    class ExampleCaretAnnotation
    {
        // Le chemin vers le répertoire des documents.
        private const string _dataDir = "..\\..\\..\\..\\Samples";
        public static void AddCaretAnnotation()
        {
            // Charger le fichier PDF
            Document document = new Document(System.IO.Path.Combine(_dataDir, "sample.pdf"));
            // Cette annotation est utilisée pour indiquer l'insertion de texte
            var caretAnnotation1 = new CaretAnnotation(document.Pages[1], new Rectangle(299.988, 713.664, 308.708, 720.769))
            {
                Title = "Utilisateur Aspose",
                Subject = "Texte inséré 1",
                Flags = AnnotationFlags.Print,
                Color = Color.Blue
            };
            // Cette annotation est utilisée pour indiquer le remplacement de texte
            var caretAnnotation2 = new CaretAnnotation(document.Pages[1], new Rectangle(361.246, 727.908, 370.081, 735.107))
            {
                Flags = AnnotationFlags.Print,
                Subject = "Texte inséré 2",
                Title = "Utilisateur Aspose",
                Color = Color.Blue
            };

            var strikeOutAnnotation = new StrikeOutAnnotation(document.Pages[1],
                new Rectangle(318.407, 727.826, 368.916, 740.098))
            {
                Color = Color.Blue,
                QuadPoints = new[] {
                new Point(321.66, 739.416),
                new Point(365.664, 739.416),
                new Point(321.66, 728.508),
                new Point(365.664, 728.508)
            },
                Subject = "Barré",
                InReplyTo = caretAnnotation2,
                ReplyType = ReplyType.Group
            };

            document.Pages[1].Annotations.Add(caretAnnotation1);
            document.Pages[1].Annotations.Add(caretAnnotation2);
            document.Pages[1].Annotations.Add(strikeOutAnnotation);

            document.Save(System.IO.Path.Combine(_dataDir, "sample_caret.pdf"));
        }
```
### Obtenir l'annotation de l'insertion

Veuillez essayer d'utiliser l'extrait de code suivant pour obtenir l'annotation de l'insertion dans un document PDF

```csharp
public static void GetCaretAnnotation()
{
    // Charger le fichier PDF
    Document document = new Document(System.IO.Path.Combine(_dataDir, "sample_caret.pdf"));
    var caretAnnotations = document.Pages[1].Annotations
        .Where(a => a.AnnotationType == AnnotationType.Caret)
        .Cast<CaretAnnotation>();
    foreach (var ca in caretAnnotations)
    {
        Console.WriteLine($"{ca.Rect}");
    }
}
```

### Supprimer l'annotation de l'insertion

L'extrait de code suivant montre comment supprimer l'annotation de l'insertion d'un fichier PDF.

```csharp
public static void DeleteCaretAnnotation()
{
    // Charger le fichier PDF
    Document document = new Document(System.IO.Path.Combine(_dataDir, "sample_caret.pdf"));
    var caretAnnotations = document.Pages[1].Annotations
        .Where(a => a.AnnotationType == AnnotationType.Caret)
        .Cast<CaretAnnotation>();

    foreach (var ca in caretAnnotations)
    {
        document.Pages[1].Annotations.Delete(ca);
    }
    document.Save(System.IO.Path.Combine(_dataDir, "sample_caret_del.pdf"));
}
```
## Masquer certaines régions de la page avec l'annotation de rédaction en utilisant Aspose.PDF pour .NET

Aspose.PDF pour .NET prend en charge la fonctionnalité d'ajouter ainsi que de manipuler des annotations dans un fichier PDF existant. Récemment, certains de nos clients ont exprimé le besoin de masquer (supprimer le texte, l'image, etc. des éléments de) une certaine région de la page d'un document PDF. Pour répondre à cette exigence, une classe nommée RedactionAnnotation est fournie, qui peut être utilisée pour masquer certaines régions de la page ou elle peut être utilisée pour manipuler des RedactionAnnotations existantes et les masquer (c'est-à-dire aplatir l'annotation et supprimer le texte sous celle-ci).

```csharp
// Pour des exemples complets et des fichiers de données, veuillez aller à https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

// Ouvrir le document
Document doc = new Document(dataDir + "input.pdf");

// Créer une instance de RedactionAnnotation pour une région spécifique de la page
RedactionAnnotation annot = new RedactionAnnotation(doc.Pages[1], new Aspose.Pdf.Rectangle(200, 500, 300, 600));
annot.FillColor = Aspose.Pdf.Color.Green;
annot.BorderColor = Aspose.Pdf.Color.Yellow;
annot.Color = Aspose.Pdf.Color.Blue;
// Texte à imprimer sur l'annotation de rédaction
annot.OverlayText = "REDACTED";
annot.TextAlignment = Aspose.Pdf.HorizontalAlignment.Center;
// Répéter le texte de superposition sur l'annotation de rédaction
annot.Repeat = true;
// Ajouter l'annotation à la collection d'annotations de la première page
doc.Pages[1].Annotations.Add(annot);
// Aplatit l'annotation et masque le contenu de la page (c'est-à-dire supprime le texte et l'image
// Sous l'annotation masquée)
annot.Redact();
dataDir = dataDir + "RedactPage_out.pdf";
doc.Save(dataDir);
```
### Approche des Facades

L'espace de noms Aspose.PDF.Facades contient également une classe nommée [PdfAnnotationEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor) qui offre la fonctionnalité de manipuler les Annotations existantes dans un fichier PDF. Cette classe contient une méthode nommée [RedactArea(..)](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor/methods/redactarea) qui permet de supprimer certaines régions de page.

```csharp
// Pour des exemples complets et des fichiers de données, veuillez aller à https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

Aspose.Pdf.Facades.PdfAnnotationEditor editor = new Aspose.Pdf.Facades.PdfAnnotationEditor();
// Masquer une certaine région de la page
editor.RedactArea(1, new Aspose.Pdf.Rectangle(100, 100, 20, 70), System.Drawing.Color.White);
editor.BindPdf(dataDir + "input.pdf");
editor.Save(dataDir + "FacadesApproach_out.pdf");
```

<script type="application/ld+json">

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF pour la bibliothèque .NET",
    "image": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
    "url": "https://www.aspose.com/",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF",
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
                "contactType": "ventes",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "ventes",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "ventes",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": "Bibliothèque de manipulation de PDF pour .NET",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/net/create-pdf-document/screenshot.png",
    "softwareVersion": "2022.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>
```

