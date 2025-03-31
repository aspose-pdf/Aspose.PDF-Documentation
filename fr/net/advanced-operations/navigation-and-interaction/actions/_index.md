---
title: Travailler avec des actions dans un PDF
linktitle: Actions
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /fr/net/actions/
description: Cette section explique comment ajouter des actions au document et aux champs de formulaire par programmation avec C#.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Working with Actions in PDF",
    "alternativeHeadline": "Programmatic Actions in PDF with C#",
    "abstract": "La nouvelle fonctionnalité dans Aspose.PDF for .NET permet aux développeurs d'ajouter des actions aux PDF par programmation, améliorant l'interactivité au sein des documents. Les utilisateurs peuvent implémenter des hyperliens pour naviguer à l'intérieur du document ou vers des URL externes, ainsi que manipuler les actions d'ouverture de document pour contrôler comment les PDF sont affichés lorsqu'ils sont ouverts. Cette fonctionnalité puissante rationalise la création et l'interaction des documents pour les applications C#",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "C#, PDF actions, hyperlink creation, LinkAnnotation, LocalHyperlink, FreeTextAnnotation, document open action, XYZExplicitDestination, Aspose.PDF, PDF manipulation",
    "wordcount": "2007",
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
    "url": "/net/actions/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/actions/"
    },
    "dateModified": "2024-11-25",
    "description": "Cette section explique comment ajouter des actions au document et aux champs de formulaire par programmation avec C#."
}
</script>

Le code suivant fonctionne également avec la bibliothèque [Aspose.PDF.Drawing](/pdf/fr/net/drawing/).

## Ajouter un hyperlien dans un fichier PDF

Il est possible d'ajouter des hyperliens aux fichiers PDF, soit pour permettre aux lecteurs de naviguer vers une autre partie du PDF, soit vers un contenu externe.

Pour ajouter des hyperliens web aux documents PDF :

1. Créez un objet de classe [Document](https://reference.aspose.com/pdf/fr/net/aspose.pdf/document).
1. Obtenez la classe [Page](https://reference.aspose.com/pdf/fr/net/aspose.pdf/page) à laquelle vous souhaitez ajouter le lien.
1. Créez un objet [LinkAnnotation](https://reference.aspose.com/pdf/fr/net/aspose.pdf.annotations/linkannotation) en utilisant les objets Page et [Rectangle](https://reference.aspose.com/pdf/fr/net/aspose.pdf/rectangle). L'objet rectangle est utilisé pour spécifier l'emplacement sur la page où le lien doit être ajouté.
1. Définissez la propriété Action sur l'objet [GoToURIAction](https://reference.aspose.com/pdf/fr/net/aspose.pdf.annotations/gotouriaction) qui spécifie l'emplacement de l'URI distant.
1. Pour afficher un texte d'hyperlien, ajoutez une chaîne de texte à un emplacement similaire à celui où l'objet [LinkAnnotation](https://reference.aspose.com/pdf/fr/net/aspose.pdf.annotations/linkannotation) est placé.
1. Pour ajouter un texte libre :

- Instanciez un objet [FreeTextAnnotation](https://reference.aspose.com/pdf/fr/net/aspose.pdf.annotations/freetextannotation). Il accepte également les objets Page et Rectangle comme arguments, il est donc possible de fournir les mêmes valeurs que celles spécifiées pour le constructeur LinkAnnotation.
- À l'aide de la propriété Contents de l'objet [FreeTextAnnotation](https://reference.aspose.com/pdf/fr/net/aspose.pdf.annotations/freetextannotation), spécifiez la chaîne qui doit être affichée dans le PDF de sortie.
- En option, définissez la largeur de la bordure des objets [LinkAnnotation](https://reference.aspose.com/pdf/fr/net/aspose.pdf.annotations/linkannotation) et FreeTextAnnotation à 0 afin qu'ils n'apparaissent pas dans le document PDF.
- Une fois que les objets [LinkAnnotation](https://reference.aspose.com/pdf/fr/net/aspose.pdf.annotations/linkannotation) et [FreeTextAnnotation](https://reference.aspose.com/pdf/fr/net/aspose.pdf.annotations/freetextannotation) ont été définis, ajoutez ces liens à la collection Annotations de l'objet [Page](https://reference.aspose.com/pdf/fr/net/aspose.pdf/page).
- Enfin, enregistrez le PDF mis à jour à l'aide de la méthode [Save](https://reference.aspose.com/pdf/fr/net/aspose.pdf/document/methods/save) de l'objet [Document](https://reference.aspose.com/pdf/fr/net/aspose.pdf/document).

Le code suivant montre comment ajouter un hyperlien à un fichier PDF.

{{< tabs tabID="1" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddHyperlink()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "AddHyperlink.pdf"))
    {
        // Get page
        var page = document.Pages[1];
        // Create Link annotation object
        var link = new Aspose.Pdf.Annotations.LinkAnnotation(page, new Aspose.Pdf.Rectangle(100, 100, 300, 300));
        // Create border object for LinkAnnotation
        var border = new Aspose.Pdf.Annotations.Border(link);
        // Set the border width value as 0
        border.Width = 0;
        // Set the border for LinkAnnotation
        link.Border = border;
        // Specify the link type as remote URI
        link.Action = new Aspose.Pdf.Annotations.GoToURIAction("www.aspose.com");
        // Add link annotation to annotations collection of first page of PDF file
        page.Annotations.Add(link);

        // Create Free Text annotation
        var textAnnotation = new Aspose.Pdf.Annotations.FreeTextAnnotation(document.Pages[1], new Aspose.Pdf.Rectangle(100, 100, 300, 300), new Aspose.Pdf.Annotations.DefaultAppearance(Aspose.Pdf.Text.FontRepository.FindFont("TimesNewRoman"), 10, System.Drawing.Color.Blue));
        // String to be added as Free text
        textAnnotation.Contents = "Link to Aspose website";
        // Set the border for Free Text Annotation
        textAnnotation.Border = border;
        // Add FreeText annotation to annotations collection of first page of Document
        document.Pages[1].Annotations.Add(textAnnotation);

        // Save PDF document
        document.Save(dataDir + "AddHyperlink_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddHyperlink()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();

    // Open PDF document
    using var document = new Aspose.Pdf.Document(dataDir + "AddHyperlink.pdf");
    // Get page
    var page = document.Pages[1];
    // Create Link annotation object
    var link = new Aspose.Pdf.Annotations.LinkAnnotation(page, new Aspose.Pdf.Rectangle(100, 100, 300, 300));
    // Create border object for LinkAnnotation
    var border = new Aspose.Pdf.Annotations.Border(link);
    // Set the border width value as 0
    border.Width = 0;
    // Set the border for LinkAnnotation
    link.Border = border;
    // Specify the link type as remote URI
    link.Action = new Aspose.Pdf.Annotations.GoToURIAction("www.aspose.com");
    // Add link annotation to annotations collection of first page of PDF file
    page.Annotations.Add(link);

    // Create Free Text annotation
    var textAnnotation = new Aspose.Pdf.Annotations.FreeTextAnnotation(document.Pages[1], new Aspose.Pdf.Rectangle(100, 100, 300, 300), new Aspose.Pdf.Annotations.DefaultAppearance(Aspose.Pdf.Text.FontRepository.FindFont("TimesNewRoman"), 10, System.Drawing.Color.Blue));
    // String to be added as Free text
    textAnnotation.Contents = "Link to Aspose website";
    // Set the border for Free Text Annotation
    textAnnotation.Border = border;
    // Add FreeText annotation to annotations collection of first page of Document
    document.Pages[1].Annotations.Add(textAnnotation);

    // Save PDF document
    document.Save(dataDir + "AddHyperlink_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

## Créer un hyperlien vers des pages dans le même PDF

Aspose.PDF for .NET offre une excellente fonctionnalité pour la création de PDF ainsi que sa manipulation. Il propose également la fonctionnalité d'ajouter des liens vers des pages PDF et un lien peut soit diriger vers des pages dans un autre fichier PDF, une URL web, un lien pour lancer une application ou même un lien vers des pages dans le même fichier PDF. Pour ajouter des hyperliens locaux (liens vers des pages dans le même fichier PDF), une classe nommée [LocalHyperlink](https://reference.aspose.com/pdf/fr/net/aspose.pdf/localhyperlink) a été ajoutée à l'espace de noms Aspose.PDF et cette classe a une propriété nommée TargetPageNumber, qui est utilisée pour spécifier la page cible/destination pour l'hyperlien.

Pour ajouter l'hyperlien local, nous devons créer un TextFragment afin que le lien puisse être associé au TextFragment. La classe [TextFragment](https://reference.aspose.com/pdf/fr/net/aspose.pdf.text/textfragment) a une propriété nommée Hyperlink qui est utilisée pour associer une instance de LocalHyperlink. Le code suivant montre les étapes pour accomplir cette exigence.

{{< tabs tabID="2" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddHyperlink()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();
        // Create Text Fragment instance
        var text = new Aspose.Pdf.Text.TextFragment("link page number test to page 7");
        // Create local hyperlink instance
        var link = new Aspose.Pdf.LocalHyperlink();
        // Set target page for link instance
        link.TargetPageNumber = 7;
        // Set TextFragment hyperlink
        text.Hyperlink = link;
        // Add text to paragraphs collection of Page
        page.Paragraphs.Add(text);
        // Create new TextFragment instance
        text = new Aspose.Pdf.Text.TextFragment("link page number test to page 1");
        // TextFragment should be added over new page
        text.IsInNewPage = true;
        // Create another local hyperlink instance
        link = new Aspose.Pdf.LocalHyperlink();
        // Set Target page for second hyperlink
        link.TargetPageNumber = 1;
        // Set link for second TextFragment
        text.Hyperlink = link;
        // Add text to paragraphs collection of page object
        page.Paragraphs.Add(text);

        // Save PDF document
        document.Save(dataDir + "CreateLocalHyperlink_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddHyperlink()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();

    // Create PDF document
    using var document = new Aspose.Pdf.Document();
    // Add page
    var page = document.Pages.Add();
    // Create Text Fragment instance
    var text = new Aspose.Pdf.Text.TextFragment("link page number test to page 7");
    // Create local hyperlink instance
    var link = new Aspose.Pdf.LocalHyperlink();
    // Set target page for link instance
    link.TargetPageNumber = 7;
    // Set TextFragment hyperlink
    text.Hyperlink = link;
    // Add text to paragraphs collection of Page
    page.Paragraphs.Add(text);
    // Create new TextFragment instance
    text = new Aspose.Pdf.Text.TextFragment("link page number test to page 1");
    // TextFragment should be added over new page
    text.IsInNewPage = true;
    // Create another local hyperlink instance
    link = new Aspose.Pdf.LocalHyperlink();
    // Set Target page for second hyperlink
    link.TargetPageNumber = 1;
    // Set link for second TextFragment
    text.Hyperlink = link;
    // Add text to paragraphs collection of page object
    page.Paragraphs.Add(text);

    // Save PDF document
    document.Save(dataDir + "CreateLocalHyperlink_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

## Obtenir la destination d'hyperlien PDF (URL)

Les liens sont représentés comme des annotations dans un fichier PDF et ils peuvent être ajoutés, mis à jour ou supprimés. Aspose.PDF for .NET prend également en charge l'obtention de la destination (URL) de l'hyperlien dans le fichier PDF.

Pour obtenir l'URL d'un lien :

1. Créez un objet [Document](https://reference.aspose.com/pdf/fr/net/aspose.pdf/document).
1. Obtenez la [Page](https://reference.aspose.com/pdf/fr/net/aspose.pdf/page) dont vous souhaitez extraire les liens.
1. Utilisez la classe [AnnotationSelector](https://reference.aspose.com/pdf/fr/net/aspose.pdf.annotations/annotationselector) pour extraire tous les objets [LinkAnnotation](https://reference.aspose.com/pdf/fr/net/aspose.pdf.annotations/linkannotation) de la page spécifiée.
1. Passez l'objet [AnnotationSelector](https://reference.aspose.com/pdf/fr/net/aspose.pdf.annotations/annotationselector) à la méthode Accept de l'objet [Page](https://reference.aspose.com/pdf/fr/net/aspose.pdf/page).
1. Obtenez toutes les annotations de lien sélectionnées dans un objet IList à l'aide de la propriété Selected de l'objet [AnnotationSelector](https://reference.aspose.com/pdf/fr/net/aspose.pdf.annotations/annotationselector).
1. Enfin, extrayez l'action LinkAnnotation comme GoToURIAction.

Le code suivant montre comment obtenir les destinations d'hyperliens (URL) d'un fichier PDF.

{{< tabs tabID="3" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GetHyperlink()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Traverse through all the page of PDF
        foreach (var page in document.Pages)
        {
            // Get the link annotations from particular page
            var selector = new Aspose.Pdf.Annotations.AnnotationSelector(new Aspose.Pdf.Annotations.LinkAnnotation(page, Aspose.Pdf.Rectangle.Trivial));

            page.Accept(selector);

            // Create list holding all the links
            var list = selector.Selected;

            // Iterate through individual item inside list
            foreach (var a in list)
            {
                // Print the destination URL
                Console.WriteLine("\nDestination: " + (a.Action as Aspose.Pdf.Annotations.GoToURIAction).URI + "\n");
            }
        }
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GetHyperlink()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();

    // Open PDF document
    using var document = new Aspose.Pdf.Document(dataDir + "input.pdf");

    // Traverse through all the page of PDF
    foreach (var page in document.Pages)
    {
        // Get the link annotations from particular page
        var selector = new Aspose.Pdf.Annotations.AnnotationSelector(new Aspose.Pdf.Annotations.LinkAnnotation(page, Aspose.Pdf.Rectangle.Trivial));

        page.Accept(selector);

        // Create list holding all the links
        var list = selector.Selected;

        // Iterate through individual item inside list
        foreach (var a in list)
        {
            // Print the destination URL
            Console.WriteLine("\nDestination: " + (a.Action as Aspose.Pdf.Annotations.GoToURIAction).URI + "\n");
        }
    }
}
```
{{< /tab >}}
{{< /tabs >}}

## Obtenir le texte de l'hyperlien

Un hyperlien a deux parties : le texte qui s'affiche dans le document et l'URL de destination. Dans certains cas, c'est le texte plutôt que l'URL dont nous avons besoin.

Le texte et les annotations/actions dans un fichier PDF sont représentés par différentes entités. Le texte sur une page est juste un ensemble de mots et de caractères, tandis que les annotations apportent une certaine interactivité, comme celle inhérente à un hyperlien.

Pour trouver le contenu de l'URL, vous devez travailler à la fois avec l'annotation et le texte. L'objet [Annotation](https://reference.aspose.com/pdf/fr/net/aspose.pdf.annotations/annotation) n'a pas lui-même le texte mais se trouve sous le texte sur la page. Donc, pour obtenir le texte, l'annotation donne les limites de l'URL, tandis que l'objet Text donne le contenu de l'URL. Veuillez voir le code suivant.

{{< tabs tabID="4" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ShowLinkAnnotationText()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Iterate through each page of PDF
        foreach (var page in document.Pages)
        {
            // Show link annotation
            ShowLinkAnnotations(page);
        }
    }
}

private static void ShowLinkAnnotations(Aspose.Pdf.Page page)
{
    foreach (var annot in page.Annotations)
    {
        if (annot is Aspose.Pdf.Annotations.LinkAnnotation)
        {
            // Print the URL of each Link Annotation
            Console.WriteLine("URI: " + ((annot as Aspose.Pdf.Annotations.LinkAnnotation).Action as Aspose.Pdf.Annotations.GoToURIAction).URI);
            var absorber = new Aspose.Pdf.Text.TextAbsorber();
            absorber.TextSearchOptions.LimitToPageBounds = true;
            absorber.TextSearchOptions.Rectangle = annot.Rect;
            page.Accept(absorber);
            string extractedText = absorber.Text;
            // Print the text associated with hyperlink
            Console.WriteLine(extractedText);
        }
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ShowLinkAnnotationText()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();

    // Open PDF document
    using var document = new Aspose.Pdf.Document(dataDir + "input.pdf");

    // Iterate through each page of PDF
    foreach (var page in document.Pages)
    {
        // Show link annotation
        ShowLinkAnnotations(page);
    }
}

private static void ShowLinkAnnotations(Aspose.Pdf.Page page)
{
    foreach (var annot in page.Annotations)
    {
        if (annot is Aspose.Pdf.Annotations.LinkAnnotation)
        {
            // Print the URL of each Link Annotation
            Console.WriteLine("URI: " + ((annot as Aspose.Pdf.Annotations.LinkAnnotation).Action as Aspose.Pdf.Annotations.GoToURIAction).URI);
            var absorber = new Aspose.Pdf.Text.TextAbsorber();
            absorber.TextSearchOptions.LimitToPageBounds = true;
            absorber.TextSearchOptions.Rectangle = annot.Rect;
            page.Accept(absorber);
            string extractedText = absorber.Text;
            // Print the text associated with hyperlink
            Console.WriteLine(extractedText);
        }
    }
}
```
{{< /tab >}}
{{< /tabs >}}

## Supprimer l'action d'ouverture de document d'un fichier PDF

[Comment spécifier la page PDF lors de la visualisation du document](#how-to-specify-pdf-page-when-viewing-document) a expliqué comment indiquer à un document de s'ouvrir sur une page différente de la première. Lors de la concaténation de plusieurs documents, et si un ou plusieurs ont une action GoTo définie, vous voudrez probablement les supprimer. Par exemple, si vous combinez deux documents et que le second a une action GoTo qui vous amène à la deuxième page, le document de sortie s'ouvrira sur la deuxième page du deuxième document au lieu de la première page du document combiné. Pour éviter ce comportement, supprimez la commande d'action d'ouverture.

Pour supprimer une action d'ouverture :

1. Définissez la propriété [OpenAction](https://reference.aspose.com/pdf/fr/net/aspose.pdf/document/properties/openaction) de l'objet [Document](https://reference.aspose.com/pdf/fr/net/aspose.pdf/document) sur null.
1. Enregistrez le PDF mis à jour à l'aide de la méthode [Save](https://reference.aspose.com/pdf/fr/net/aspose.pdf/document/methods/save) de l'objet Document.

Le code suivant montre comment supprimer une action d'ouverture de document du fichier PDF.

{{< tabs tabID="5" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void RemoveOpenAction()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "RemoveOpenAction.pdf"))
    {
        // Remove document open action
        document.OpenAction = null;

        // Save PDF document
        document.Save(dataDir + "RemoveOpenAction_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void RemoveOpenAction()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();

    // Open PDF document
    using var document = new Aspose.Pdf.Document(dataDir + "RemoveOpenAction.pdf");

    // Remove document open action
    document.OpenAction = null;

    // Save PDF document
    document.Save(dataDir + "RemoveOpenAction_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

## Comment spécifier la page PDF lors de la visualisation du document {#how-to-specify-pdf-page-when-viewing-document}

Lors de la visualisation de fichiers PDF dans un visualiseur PDF tel qu'Adobe Reader, les fichiers s'ouvrent généralement sur la première page. Cependant, il est possible de définir le fichier pour qu'il s'ouvre sur une page différente.

La classe [XYZExplicitDestination](https://reference.aspose.com/pdf/fr/net/aspose.pdf.annotations/xyzexplicitdestination) vous permet de spécifier une page dans un fichier PDF que vous souhaitez ouvrir. En passant la valeur de l'objet GoToAction à la propriété OpenAction de la classe [Document](https://reference.aspose.com/pdf/fr/net/aspose.pdf/document), le document s'ouvre à la page spécifiée contre l'objet XYZExplicitDestination. Le code suivant montre comment spécifier une page comme action d'ouverture du document.

{{< tabs tabID="6" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SpecifyPage()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "SpecifyPageWhenViewing.pdf"))
    {
        // Get the instance of second page of document
        var page2 = document.Pages[2];
        // Create the variable to set the zoom factor of target page
        double zoom = 1;
        // Create GoToAction instance
        var action = new Aspose.Pdf.Annotations.GoToAction(document.Pages[2]);
        // Go to 2 page
        action.Destination = new Aspose.Pdf.Annotations.XYZExplicitDestination(page2, 0, page2.Rect.Height, zoom);
        // Set the document open action
        document.OpenAction = action;
        // Save PDF document
        document.Save(dataDir + "Goto2page_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SpecifyPage()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();

    // Open PDF document
    using var document = new Aspose.Pdf.Document(dataDir + "SpecifyPageWhenViewing.pdf");
    // Get the instance of second page of document
    var page2 = document.Pages[2];
    // Create the variable to set the zoom factor of target page
    double zoom = 1;
    // Create GoToAction instance
    var action = new Aspose.Pdf.Annotations.GoToAction(document.Pages[2]);
    // Go to 2 page
    action.Destination = new Aspose.Pdf.Annotations.XYZExplicitDestination(page2, 0, page2.Rect.Height, zoom);
    // Set the document open action
    document.OpenAction = action;
    // Save PDF document
    document.Save(dataDir + "Goto2page_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

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