---
title: Trabalhando com Rotação de Página
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /pt/net/working-with-page-rotation/
description: Esta seção explica como trabalhar com Rotação de Página usando a Classe PdfPageEditor.
lastmod: "2021-07-07"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Working with Page Rotation",
    "alternativeHeadline": "Effortlessly Rotate PDF Pages with PdfPageEditor",
    "abstract": "Descubra o poderoso recurso de Rotação de Página na classe PdfPageEditor, permitindo a manipulação precisa das páginas do documento através de ângulos de rotação personalizáveis. Com opções para especificar rotações de páginas individuais ou aplicar uma rotação uniforme em páginas selecionadas, essa funcionalidade aprimora as capacidades de edição de PDF, oferecendo maior flexibilidade e controle para os usuários.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "202",
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
    "url": "/net/working-with-page-rotation/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/working-with-page-rotation/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF pode realizar não apenas tarefas simples e fáceis, mas também lidar com objetivos mais complexos. Confira a próxima seção para usuários e desenvolvedores avançados."
}
</script>

{{% alert color="primary" %}}

A classe [PdfPageEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor) fornece a facilidade de girar uma página.

{{% /alert %}}

## Girar página usando PageRotations

Para girar páginas no documento, podemos usar [PageRotations](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor/properties/pagerotations).
`PageRotations` contém o número da página e o grau de rotação, a chave representa o número da página, o valor da chave representa a rotação em graus.

```csharp
 // For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
 private static void RotatePages1()
 {
    // The path to the documents directory
     var dataDir = RunExamples.GetDataDir_AsposePdf();

     using (var editor = new Aspose.Pdf.Facades.PdfPageEditor())
     {
         // Bind PDF document
         editor.BindPdf(dataDir + "sample.pdf");

         // Specify the page rotation dictionary
         editor.PageRotations = new System.Collections.Generic.Dictionary<int, int>
         {
             { 1, 90 },
             { 2, 180 },
             { 3, 270 }
         };

         // Save PDF document
         editor.Save(dataDir + "sample-rotate-a.pdf");
     }
 }
```

## Girar página usando Rotation

Também podemos usar a propriedade [Rotation](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor/properties/rotation). A rotação deve ser 0, 90, 180 ou 270.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void RotatePages2()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    using (var editor = new Aspose.Pdf.Facades.PdfPageEditor())
    {
        // Bind PDF document
        editor.BindPdf(dataDir + "sample.pdf");

        // Specify the pages to rotate and the rotation angle
        editor.ProcessPages = new int[] { 1, 3 };
        editor.Rotation = 90;

        // Save PDF document
        editor.Save(dataDir + "sample-rotate-a.pdf");
    }
}
```