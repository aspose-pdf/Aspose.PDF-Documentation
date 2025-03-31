---
title: Aparência e atributos do campo
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 40
url: /pt/net/changing-field-appearance-and-attributes/
description: Esta seção explica como você pode alterar a aparência e os atributos do campo com a classe FormEditor.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Field appearance and attributes",
    "alternativeHeadline": "Enhance Form Fields with Custom Appearance and Behavior",
    "abstract": "O recurso introduzido na classe FormEditor do namespace Aspose.Pdf.Facades permite que os usuários personalizem tanto a aparência quanto os atributos dos campos de formulário em PDFs. Ao utilizar métodos como SetFieldAppearance e SetFieldAttributes, os desenvolvedores podem facilmente modificar elementos visuais e comportamentos, incluindo limites de campo, para aprimorar a interação do usuário e a eficiência na entrada de dados. Essa funcionalidade oferece maior flexibilidade no design de campos de formulário adaptados às necessidades específicas da aplicação.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "259",
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
    "url": "/net/changing-field-appearance-and-attributes/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/changing-field-appearance-and-attributes/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF pode realizar não apenas tarefas simples e fáceis, mas também lidar com objetivos mais complexos. Confira a próxima seção para usuários e desenvolvedores avançados."
}
</script>

{{% alert color="primary" %}}

A classe [FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/FormEditor) do [namespace Aspose.Pdf.Facades](https://reference.aspose.com/pdf/net/aspose.pdf.facades) permite que você não apenas altere a aparência do campo de formulário, mas também o comportamento do campo. Neste artigo, veremos como podemos usar a classe FormEditor para alterar a aparência do campo, os atributos do campo e o limite do campo também.

{{% /alert %}}

## Detalhes da implementação

O método [SetFieldAppearance](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/setfieldappearance) é usado para alterar a aparência de um campo de formulário. Ele recebe AnnotationFlag como parâmetro. AnnotationFlag é uma enumeração que possui diferentes membros como Hidden ou NoRotate, etc.

O método [SetFieldAttributes](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/setfieldattribute) é usado para alterar o atributo de um campo de formulário. Um parâmetro passado para este método é a enumeração PropertyFlag, que contém membros como ReadOnly ou Required, etc.

A classe [FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/FormEditor) também fornece um método para definir o limite do campo. Ele informa ao campo quantos caracteres podem ser preenchidos. O trecho de código abaixo mostra como todos esses métodos podem ser usados.

```csharp
 // For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
 private static void AddFieldAndSetAttributes()
 {
     // The path to the documents directory
     var dataDir = RunExamples.GetDataDir_AsposePdf();

     // Open PDF document
     using (var doc = new Aspose.Pdf.Document(dataDir + "FilledForm.pdf"))
     {
         // Create an instance of FormEditor to manipulate form fields
         using (var formEditor = new Aspose.Pdf.Facades.FormEditor(doc))
         {
             // Add a new text field to the form on page 1 at the specified coordinates and size
             formEditor.AddField(Aspose.Pdf.Facades.FieldType.Text, "text1", 1, 200, 550, 300, 575);

             // Set the field attribute to make the text field required (user must fill it)
             formEditor.SetFieldAttribute("text1", Aspose.Pdf.Facades.PropertyFlag.Required);

             // Set a character limit for the field (maximum 20 characters)
             formEditor.SetFieldLimit("text1", 20);

             // Save PDF document
             formEditor.Save(dataDir + "ChangingFieldAppearance_out.pdf");
         }
     }
 }
```