---
title: Travailler avec les opérateurs
linktitle: Travailler avec les opérateurs
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 90
url: /fr/net/working-with-operators/
description: Ce sujet explique comment utiliser les opérateurs avec Aspose.PDF. Les classes d'opérateurs offrent d'excellentes fonctionnalités pour la manipulation de PDF.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Working with Operators",
    "alternativeHeadline": "Empowered PDF Manipulation with Operators Integration",
    "abstract": "La fonctionnalité des opérateurs dans Aspose.PDF for .NET améliore les capacités de manipulation de PDF en permettant aux utilisateurs d'utiliser des classes d'opérateurs spécifiques pour des tâches telles que l'ajout d'images et la suppression de graphiques. Cette fonctionnalité simplifie le processus de définition des éléments graphiques et de leurs états dans un PDF, fournissant aux développeurs des outils puissants pour un montage et un traitement de documents précis.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "operators, Aspose.PDF, PDF manipulation, GSave operator, ConcatenateMatrix operator, Do operator, GRestore operator, graphics state, remove graphics",
    "wordcount": "1233",
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
    "url": "/net/working-with-operators/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/working-with-operators/"
    },
    "dateModified": "2024-11-26",
    "description": "Ce sujet explique comment utiliser les opérateurs avec Aspose.PDF. Les classes d'opérateurs offrent d'excellentes fonctionnalités pour la manipulation de PDF."
}
</script>

## Introduction aux opérateurs PDF et leur utilisation

Un opérateur est un mot-clé PDF spécifiant une action qui doit être effectuée, comme peindre une forme graphique sur la page. Un mot-clé d'opérateur se distingue d'un objet nommé par l'absence d'un caractère solide initial (2Fh). Les opérateurs n'ont de sens que dans le flux de contenu.

Un flux de contenu est un objet de flux PDF dont les données consistent en des instructions décrivant les éléments graphiques à peindre sur une page. Plus de détails sur les opérateurs PDF peuvent être trouvés dans la [spécification PDF](https://opensource.adobe.com/dc-acrobat-sdk-docs/).

### Détails de mise en œuvre

Ce sujet explique comment utiliser les opérateurs avec Aspose.PDF. L'exemple sélectionné ajoute une image dans un fichier PDF pour illustrer le concept. Pour ajouter une image dans un fichier PDF, différents opérateurs sont nécessaires. Cet exemple utilise [GSave](https://reference.aspose.com/pdf/net/aspose.pdf.ioperatorselector/visit/methods/28), [ConcatenateMatrix](https://reference.aspose.com/pdf/net/aspose.pdf.ioperatorselector/visit/methods/10), [Do](https://reference.aspose.com/pdf/net/aspose.pdf.ioperatorselector/visit/methods/14), et [GRestore](https://reference.aspose.com/pdf/net/aspose.pdf.ioperatorselector/visit/methods/26).

- L'opérateur **GSave** enregistre l'état graphique actuel du PDF.
- L'opérateur **ConcatenateMatrix** (matrice de concaténation) est utilisé pour définir comment une image doit être placée sur la page PDF.
- L'opérateur **Do** dessine l'image sur la page.
- L'opérateur **GRestore** restaure l'état graphique.

Pour ajouter une image dans un fichier PDF :

1. Créez un objet [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) et ouvrez le document PDF d'entrée.
1. Obtenez la page particulière à laquelle l'image va être ajoutée.
1. Ajoutez l'image dans la collection de ressources de la page.
1. Utilisez les opérateurs pour placer l'image sur la page :
   - Tout d'abord, utilisez l'opérateur GSave pour enregistrer l'état graphique actuel.
   - Ensuite, utilisez l'opérateur ConcatenateMatrix pour spécifier où l'image doit être placée.
   - Utilisez l'opérateur Do pour dessiner l'image sur la page.
1. Enfin, utilisez l'opérateur GRestore pour enregistrer l'état graphique mis à jour.

Le code suivant fonctionne également avec la bibliothèque [Aspose.PDF.Drawing](/pdf/fr/net/drawing/).

Le code suivant montre comment utiliser les opérateurs PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddImageUsingPDFOperators()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "PDFOperators.pdf"))
    {
        // Set coordinates for the image placement
        int lowerLeftX = 100;
        int lowerLeftY = 100;
        int upperRightX = 200;
        int upperRightY = 200;

        // Get the page where the image needs to be added
        var page = document.Pages[1];

        // Load the image into a file stream
        using (var imageStream = new FileStream(dataDir + "PDFOperators.jpg", FileMode.Open))
        {
            // Add the image to the page's Resources collection
            page.Resources.Images.Add(imageStream);
        }

        // Save the current graphics state using the GSave operator
        page.Contents.Add(new Aspose.Pdf.Operators.GSave());

        // Create a rectangle and matrix for positioning the image
        var rectangle = new Aspose.Pdf.Rectangle(lowerLeftX, lowerLeftY, upperRightX, upperRightY);
        var matrix = new Aspose.Pdf.Matrix(new double[]
        {
            rectangle.URX - rectangle.LLX, 0,
            0, rectangle.URY - rectangle.LLY,
            rectangle.LLX, rectangle.LLY
        });

        // Define how the image must be placed using the ConcatenateMatrix operator
        page.Contents.Add(new Aspose.Pdf.Operators.ConcatenateMatrix(matrix));

        // Get the image from the Resources collection
        var ximage = page.Resources.Images[page.Resources.Images.Count];

        // Draw the image using the Do operator
        page.Contents.Add(new Aspose.Pdf.Operators.Do(ximage.Name));

        // Restore the graphics state using the GRestore operator
        page.Contents.Add(new Aspose.Pdf.Operators.GRestore());

        // Save PDF document
        document.Save(dataDir + "PDFOperators_out.pdf");
    }
}
```

## Dessiner un XForm sur la page en utilisant des opérateurs

Ce sujet démontre comment utiliser les opérateurs GSave/GRestore, l'opérateur ConcatenateMatrix pour positionner un xForm et l'opérateur Do pour dessiner un xForm sur une page.

Le code ci-dessous enveloppe le contenu existant d'un fichier PDF avec la paire d'opérateurs GSave/GRestore. Cette approche aide à obtenir l'état graphique initial à la fin des contenus existants. Sans cette approche, des transformations indésirables pourraient rester à la fin de la chaîne d'opérateurs existante.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void DrawXFormOnPage()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "DrawXFormOnPage.pdf"))
    {
        var pageContents = document.Pages[1].Contents;

        // Wrap existing contents with GSave/GRestore operators to preserve graphics state
        pageContents.Insert(1, new Aspose.Pdf.Operators.GSave());
        pageContents.Add(new Aspose.Pdf.Operators.GRestore());

        // Add GSave operator to start new graphics state
        pageContents.Add(new Aspose.Pdf.Operators.GSave());

        // Create an XForm
        var form = Aspose.Pdf.XForm.CreateNewForm(document.Pages[1], document);
        document.Pages[1].Resources.Forms.Add(form);

        form.Contents.Add(new Aspose.Pdf.Operators.GSave());
        // Define image width and height
        form.Contents.Add(new Aspose.Pdf.Operators.ConcatenateMatrix(200, 0, 0, 200, 0, 0));

        // Load image into stream
        using (var imageStream = new FileStream(dataDir + "aspose-logo.jpg", FileMode.Open))
        {
            // Add the image to the XForm's resources
            form.Resources.Images.Add(imageStream);
        }

        var ximage = form.Resources.Images[form.Resources.Images.Count];
        // Draw the image on the XForm
        form.Contents.Add(new Aspose.Pdf.Operators.Do(ximage.Name));
        form.Contents.Add(new Aspose.Pdf.Operators.GRestore());

        // Place and draw the XForm at two different coordinates

        // Draw the XForm at (100, 500)
        pageContents.Add(new Aspose.Pdf.Operators.GSave());
        pageContents.Add(new Aspose.Pdf.Operators.ConcatenateMatrix(1, 0, 0, 1, 100, 500));
        pageContents.Add(new Aspose.Pdf.Operators.Do(form.Name));
        pageContents.Add(new Aspose.Pdf.Operators.GRestore());

        // Draw the XForm at (100, 300)
        pageContents.Add(new Aspose.Pdf.Operators.GSave());
        pageContents.Add(new Aspose.Pdf.Operators.ConcatenateMatrix(1, 0, 0, 1, 100, 300));
        pageContents.Add(new Aspose.Pdf.Operators.Do(form.Name));
        pageContents.Add(new Aspose.Pdf.Operators.GRestore());

        // Restore graphics state
        pageContents.Add(new Aspose.Pdf.Operators.GRestore());

        // Save PDF document
        document.Save(dataDir + "DrawXFormOnPage_out.pdf");
    }
}
```

## Supprimer des objets graphiques en utilisant des classes d'opérateurs

Les classes d'opérateurs offrent d'excellentes fonctionnalités pour la manipulation de PDF. Lorsqu'un fichier PDF contient des graphiques qui ne peuvent pas être supprimés en utilisant la méthode [DeleteImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/deleteimage) de la classe [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor), les classes d'opérateurs peuvent être utilisées pour les supprimer à la place.

Le code suivant montre comment supprimer des graphiques. Veuillez noter que si le fichier PDF contient des étiquettes de texte pour les graphiques, elles pourraient persister dans le fichier PDF en utilisant cette approche. Par conséquent, recherchez les opérateurs graphiques pour une méthode alternative pour supprimer de telles images.

```csharp
  // For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
  private static void RemoveGraphicsObjects()
  {
      // The path to the documents directory
      var dataDir = RunExamples.GetDataDir_AsposePdf();

      // Open PDF document
      using (var document = new Aspose.Pdf.Document(dataDir + "RemoveGraphicsObjects.pdf"))
      {
          // Get the specific page (page 2 in this case)
          var page = document.Pages[2];

          // Get the operator collection from the page contents
          var oc = page.Contents;

          // Define the path-painting operators to be removed
          var operators = new Aspose.Pdf.Operator[]
          {
              new Aspose.Pdf.Operators.Stroke(),
              new Aspose.Pdf.Operators.ClosePathStroke(),
              new Aspose.Pdf.Operators.Fill()
          };

          // Delete the specified operators from the page contents
          oc.Delete(operators);

          // Save PDF document
          document.Save(dataDir + "NoGraphics_out.pdf");
      }
  }
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF for .NET Library",
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
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": "PDF Manipulation Library for .NET",
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