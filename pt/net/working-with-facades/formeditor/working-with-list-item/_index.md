---
title: Trabalhando com Item de Lista
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 50
url: /pt/net/working-with-list-item/
description: Esta seção explica como trabalhar com Item de Lista usando a Classe FormEditor do Aspose.PDF Facades.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Working with List Item",
    "alternativeHeadline": "Enhance PDF Forms with List Item Management",
    "abstract": "Melhore seus formulários PDF com o recurso de Item de Lista em Aspose.PDF for .NET. Adicione ou exclua facilmente itens de campos ListBox usando a classe FormEditor, permitindo uma entrada de usuário dinâmica e personalizável. Essa funcionalidade simplifica o gerenciamento de formulários, tornando mais fácil adaptar o conteúdo às suas necessidades",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "325",
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
    "url": "/net/working-with-list-item/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/working-with-list-item/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF pode realizar não apenas tarefas simples e fáceis, mas também lidar com objetivos mais complexos. Confira a próxima seção para usuários e desenvolvedores avançados."
}
</script>

## Adicionar Item de Lista em um Arquivo PDF Existente

[AddListItem](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/addlistitem) método permite que você adicione um item em um campo [ListBox](https://reference.aspose.com/pdf/net/aspose.pdf.forms/listboxfield). O primeiro argumento é o nome do campo e o segundo argumento é o item do campo. Você pode passar um único item de campo ou pode passar um array de strings que contém uma lista de itens. Este método é fornecido pela classe [FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor). O seguinte trecho de código mostra como adicionar itens de lista em um arquivo PDF.

```csharp
 // For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
 private static void AddListItem()
 {
     // The path to the documents directory
     var dataDir = RunExamples.GetDataDir_AsposePdf();

     // Create an instance of FormEditor to manipulate form fields
     using (var formEditor = new Aspose.Pdf.Facades.FormEditor())
     {
         // Bind PDF document
         formEditor.BindPdf(dataDir + "Sample-Form-01.pdf");

         // Add a ListBox field for selecting country, placed at the specified coordinates on page 1
         formEditor.AddField(Aspose.Pdf.Facades.FieldType.ListBox, "Country", 1, 232.56f, 476.75f, 352.28f,
             514.03f);

         // Add list items to the 'Country' ListBox field
         formEditor.AddListItem("Country", "USA");
         formEditor.AddListItem("Country", "Canada");
         formEditor.AddListItem("Country", "France");
         formEditor.AddListItem("Country", "Spain");

         // Save PDF document
         formEditor.Save(dataDir + "Sample-Form-01-mod.pdf");
     }
 }
```

## Excluir Item de Lista de um Arquivo PDF Existente

[DelListItem](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/dellistitem) método permite que você exclua um item específico do [ListBox](https://reference.aspose.com/pdf/net/aspose.pdf.forms/listboxfield). O primeiro parâmetro é o nome do campo, enquanto o segundo parâmetro é o item que você deseja excluir da lista. Este método é fornecido pela classe [FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor). O seguinte trecho de código mostra como excluir um item de lista do arquivo PDF.

```csharp
 // For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
 private static void DelListItem()
 {
     // The path to the documents directory
     var dataDir = RunExamples.GetDataDir_AsposePdf();

     // Create an instance of FormEditor to manipulate form fields
     using (var formEditor = new Aspose.Pdf.Facades.FormEditor())
     {
         // Bind PDF document
         formEditor.BindPdf(dataDir + "Sample-Form-04.pdf");

         // Delete the list item "France" from the 'Country' ListBox field
         formEditor.DelListItem("Country", "France");

         // Save PDF document
         formEditor.Save(dataDir + "Sample-Form-04-mod.pdf");
     }
 }
```