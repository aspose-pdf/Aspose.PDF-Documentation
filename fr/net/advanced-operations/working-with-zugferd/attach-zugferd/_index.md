---
title: Création de PDF conforme à PDF/3-A et attachement de la facture ZUGFeRD en C#
linktitle: Attacher ZUGFeRD au PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /fr/net/attach-zugferd/
description: Apprenez à générer un document PDF avec ZUGFeRD en Aspose.PDF for .NET
lastmod: "2023-11-22"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Creating PDF/3-A compliant PDF and attaching ZUGFeRD invoice in C#",
    "alternativeHeadline": "Attach ZUGFeRD Invoices to PDF in C#",
    "abstract": "Découvrez la nouvelle fonctionnalité qui permet aux développeurs de générer des documents PDF conformes à PDF/A-3B et d'attacher facilement des factures ZUGFeRD en utilisant C#. Cette fonctionnalité simplifie le processus d'intégration des métadonnées de factures dans les fichiers PDF, garantissant la préservation à long terme des documents et la conformité aux normes de facturation électronique.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "429",
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
    "url": "/net/attach-zugferd/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/attach-zugferd/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF peut effectuer non seulement des tâches simples et faciles, mais aussi faire face à des objectifs plus complexes. Consultez la section suivante pour les utilisateurs et développeurs avancés."
}
</script>

## Attacher ZUGFeRD au PDF

Le code suivant fonctionne également avec la bibliothèque [Aspose.PDF.Drawing](/pdf/fr/net/drawing/).

Nous recommandons de suivre les étapes suivantes pour attacher ZUGFeRD au PDF :

* Définir une variable de chemin qui pointe vers un dossier où se trouvent les fichiers PDF d'entrée et de sortie.
* Créer un objet document en chargeant un fichier PDF existant (par exemple, "ZUGFeRD-test.pdf") depuis le chemin.
* Créer un objet [FileSpecification](https://reference.aspose.com/pdf/net/aspose.pdf/filespecification/) en fournissant le chemin et la description d'un autre fichier nommé "factur-x.xml", qui contient des métadonnées de facturation conformes à la norme ZUGFeRD.
* Ajouter des propriétés à l'objet de spécification de fichier, telles que la description, le type MIME et la relation AF. La relation AF indique comment le fichier intégré est lié au document PDF. Dans ce cas, elle est définie sur "Alternative", ce qui signifie que le fichier intégré est une représentation alternative du contenu PDF.
* Ajouter l'objet de spécification de fichier à la collection de fichiers intégrés du document. Le nom du fichier doit être spécifié selon la norme ZUGFeRD, par exemple "factur-x.xml".
* Convertir le document au format PDF/A-3B, un sous-ensemble de PDF qui garantit la préservation à long terme des documents électroniques. PDF/A-3B permet d'intégrer des fichiers de tout format dans des documents PDF.
* Enregistrer le document converti en tant que nouveau fichier PDF (par exemple, "ZUGFeRD-res.pdf").

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AttachZUGFeRD()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();
    
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ZUGFeRD-testInput.pdf"))
    {
        // Setup new file to be added as attachment
        var description = "Invoice metadata conforming to ZUGFeRD standard";
        var fileSpecification = new Aspose.Pdf.FileSpecification(dataDir + "ZUGFeRD-testXmlInput.xml", description)
        {
            Description = "Zugferd",
            MIMEType = "text/xml",
            Name = "factur-x.xml"
        };
        // Add attachment to document's attachment collection
        document.EmbeddedFiles.Add(fileSpecification);
        document.Convert(new MemoryStream(), Aspose.Pdf.PdfFormat.ZUGFeRD, Aspose.Pdf.ConvertErrorAction.Delete);
        // Save PDF document
        document.Save(dataDir + "AttachZUGFeRD_out.pdf");
    }
}
```

La méthode de conversion prend un flux, un format PDF et une action d'erreur de conversion comme paramètres. Le paramètre de flux peut être utilisé pour enregistrer le journal de conversion. Le paramètre d'action d'erreur de conversion spécifie quoi faire si des erreurs se produisent pendant la conversion. Dans ce cas, il est défini sur "Supprimer", ce qui signifie que tout élément qui n'est pas conforme au format PDF/A-3B sera supprimé du document.