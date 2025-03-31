---
title: Extrair Anotações de PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 30
url: /pt/net/extract-annotation/
description: Esta seção explica como extrair anotações de um arquivo PDF para XFDF com Aspose.PDF Facades.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Extract Annotations from PDF",
    "alternativeHeadline": "Effortlessly Extract PDF Annotations to XFDF Format",
    "abstract": "Desbloqueie o potencial dos seus documentos PDF com o novo recurso de Extrair Anotações, que permite a extração contínua de anotações para o formato XFDF usando Aspose.PDF for .NET. Essa funcionalidade permite a recuperação fácil de tipos específicos de anotações, melhorando a gestão de documentos e a eficiência da colaboração. Descubra como simplificar seus fluxos de trabalho em PDF extraindo e salvando dados importantes de anotações sem esforço.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "254",
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
    "url": "/net/extract-annotation/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/extract-annotation/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF pode realizar não apenas tarefas simples e fáceis, mas também lidar com objetivos mais complexos. Confira a próxima seção para usuários e desenvolvedores avançados."
}
</script>

[ExtractAnnotations](https://reference.aspose.com/pdf/pt/net/aspose.pdf.facades.pdfannotationeditor/extractannotations/methods/1) método permite que você extraia anotações de um arquivo PDF. Para extrair anotações, você precisa criar um objeto [PdfAnnotationEditor](https://reference.aspose.com/pdf/pt/net/aspose.pdf.facades/pdfannotationeditor) e vincular o arquivo PDF usando o método [BindPdf](https://reference.aspose.com/pdf/pt/net/aspose.pdf.facades.facade/bindpdf/methods/3). Depois disso, você precisa criar uma enumeração dos tipos de anotações que deseja extrair do arquivo PDF.

Você pode então usar o método [ExtractAnnotations](https://reference.aspose.com/pdf/pt/net/aspose.pdf.facades.pdfannotationeditor/extractannotations/methods/1) para extrair as anotações para um ArrayList. Depois disso, você pode percorrer essa lista e obter anotações individuais. E finalmente, salve o arquivo PDF atualizado usando o método [Save](https://reference.aspose.com/pdf/pt/net/aspose.pdf/document/methods/save) do objeto [PdfAnnotationEditor](https://reference.aspose.com/pdf/pt/net/aspose.pdf.facades/pdfannotationeditor). O seguinte trecho de código mostra como extrair anotações de um arquivo PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractAnnotation()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "AnnotationsInput.pdf"))
    {
        using (var annotationEditor = new Aspose.Pdf.Facades.PdfAnnotationEditor())
        {
            // Bind PDF document
            annotationEditor.BindPdf(document);
            // Extract annotations
            var annotationTypes = new[] { Aspose.Pdf.Annotations.AnnotationType.FreeText, Aspose.Pdf.Annotations.AnnotationType.Text };
            var annotations = annotationEditor.ExtractAnnotations(1, 2, annotationTypes);
            foreach (var annotation in annotations)
            {
                Console.WriteLine(annotation.Contents);
            }
        }
    }
}
```