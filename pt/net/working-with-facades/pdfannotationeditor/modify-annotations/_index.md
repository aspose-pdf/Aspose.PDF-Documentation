---
title: Modificar Anotações no seu PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 50
url: /pt/net/modify-annotations/
description: Esta seção explica como modificar anotações de um arquivo PDF para XFDF com Aspose.PDF Facades.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Modify Annotations in your PDF",
    "alternativeHeadline": "Enhance Your PDF Annotations with New Modifications",
    "abstract": "O recurso Modificar Anotações permite que os usuários editem facilmente atributos-chave das anotações em arquivos PDF usando Aspose.PDF Facades. Essa funcionalidade inclui a alteração do assunto, autor, cor e mais, juntamente com opções para excluir anotações por tipo, simplificando o processo de gerenciamento de anotações em PDF. Otimize seu fluxo de trabalho em PDF aproveitando essas poderosas capacidades de modificação de anotações.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "290",
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
    "url": "/net/modify-annotations/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/modify-annotations/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF pode realizar não apenas tarefas simples e fáceis, mas também lidar com objetivos mais complexos. Confira a próxima seção para usuários e desenvolvedores avançados."
}
</script>

## Modificar anotação

O método [ModifyAnnotations](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor/methods/modifyannotations) permite que você altere atributos básicos de uma anotação, ou seja, Assunto, Data de modificação, Autor, Cor da anotação e Sinalizador de abertura. Você também pode definir o Autor diretamente usando o método ModifyAnnotations. Esta classe também fornece dois métodos sobrecarregados para excluir anotações. O primeiro método chamado DeleteAnnotations exclui todas as anotações de um arquivo PDF.  

Por exemplo, no código a seguir, considere alterar o autor em nossa anotação usando [ModifyAnnotationsAuthor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor/methods/modifyannotationsauthor).

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ModifyAnnotationsAuthor()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Annotations();
    // Create PdfAnnotationEditor
    using (var annotationEditor = new Aspose.Pdf.Facades.PdfAnnotationEditor())
    {
        // Bind PDF document
        annotationEditor.BindPdf(dataDir + "AnnotationsInput.pdf");
        // Modify annotations author
        annotationEditor.ModifyAnnotationsAuthor(1, 2, "Aspose User", "Aspose.PDF user");
        // Save PDF document
        annotationEditor.Save(dataDir + "ModifyAnnotationsAuthor_out.pdf");
    }
}
```

O segundo método permite que você modifique anotações.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ModifyAnnotations()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Annotations();
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "AnnotationsInput.pdf"))
    {
        // Create PdfAnnotationEditor
        using (var annotationEditor = new Aspose.Pdf.Facades.PdfAnnotationEditor())
        {
            // Bind PDF document
            annotationEditor.BindPdf(document);
            // Create a new object of type Annotation
            TextAnnotation newTextAnnotation = new TextAnnotation(document.Pages[1], new Aspose.Pdf.Rectangle(200, 400, 400, 600));
            newTextAnnotation.Title = "Updated title";
            newTextAnnotation.Subject = "Updated subject";
            newTextAnnotation.Contents = "Updated sample contents for the annotation";
            // Modify annotations in the PDF file
            annotationEditor.ModifyAnnotations(1, 1, newTextAnnotation);
            // Save PDF document
            annotationEditor.Save(dataDir + "ModifyAnnotations_out.pdf");
        }
    }
}
```