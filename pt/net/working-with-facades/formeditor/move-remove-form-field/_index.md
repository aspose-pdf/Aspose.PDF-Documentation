---
title: Mover e Remover Campo de Formulário
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 70
url: /pt/net/move-remove-form-field/
description: Explore como gerenciar campos de formulário em PDFs, incluindo movê-los ou removê-los, usando Aspose.PDF for .NET.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Move and Remove Form Field",
    "alternativeHeadline": "Move and Remove Fields in PDF Forms Efficiently",
    "abstract": "O recurso Mover e Remover Campo de Formulário na classe FormEditor permite que os usuários reposicionem e eliminem campos de formulário dentro de documentos PDF existentes de forma contínua. Ao utilizar os métodos MoveField e RemoveField, os usuários podem personalizar formulários de maneira eficiente, melhorando a usabilidade e a gestão de documentos. Essa funcionalidade capacita os usuários a otimizar seus layouts PDF sem exigir ampla expertise técnica.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "416",
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
    "url": "/net/move-remove-form-field/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/move-remove-form-field/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF pode realizar não apenas tarefas simples e fáceis, mas também lidar com objetivos mais complexos. Confira a próxima seção para usuários e desenvolvedores avançados."
}
</script>

## Mover Campo de Formulário para uma Nova Localização em um Arquivo PDF Existente

Se você deseja mover um campo de formulário para uma nova localização, pode usar o método [MoveField](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/movefield) da classe [FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor). Você só precisa fornecer o nome do campo e a nova localização desse campo para o método [MoveField](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/movefield). Você também precisa salvar o arquivo PDF atualizado usando o método [Save](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/methods/save/index) da classe [FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor). O seguinte trecho de código mostra como mover um campo de formulário para uma nova localização em um arquivo PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MoveField()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();
    using (var editor = new Aspose.Pdf.Facades.FormEditor())
    {
        // Bind PDF document
        editor.BindPdf(dataDir + "MoveField.pdf");
        editor.MoveField("textbox1", 262.56f, 496.75f, 382.28f, 514.03f);
        // Save PDF document
        editor.Save(dataDir + "MoveField_out.pdf");
    }
}
```

## Excluir Campo de Formulário de um Arquivo PDF Existente

Para excluir um campo de formulário de um arquivo PDF existente, você pode usar o método RemoveField da classe FormEditor. Este método aceita apenas um argumento: o nome do campo. Você precisa criar um objeto da classe FormEditor, chamar o método [RemoveField](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/removefield) para remover um campo específico do PDF e, em seguida, chamar o método Save para salvar o arquivo PDF atualizado. O seguinte trecho de código mostra como excluir campos de formulário de um arquivo PDF existente.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void RemoveFields()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();
    using (var editor = new Aspose.Pdf.Facades.FormEditor())
    {
        // Bind PDF document
        editor.BindPdf(dataDir + "ModifyFormField.pdf");
        editor.RemoveField("textbox1");
        // Save PDF document
        editor.Save(dataDir + "RemoveField_out.pdf");
    }
}
```

## Renomear Campos de Formulário em PDF

Você também pode renomear seu campo usando o método [RenameField](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/renamefield) da classe [FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor).

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void RenameFields()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();
    using (var editor = new Aspose.Pdf.Facades.FormEditor())
    {
        // Bind PDF document
        editor.BindPdf(dataDir + "ModifyFormField.pdf");
        editor.RenameField("textbox1", "FirstName");
        // Save PDF document
        editor.Save(dataDir + "RenameField_out.pdf");
    }
}
```