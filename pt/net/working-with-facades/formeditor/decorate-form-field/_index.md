---
title: Decorar Campo de Formulário em PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 30
url: /pt/net/decorate-form-field/
description: Explore como decorar campos de formulário em um documento PDF, adicionando melhorias visuais como bordas, em .NET com Aspose.PDF.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Decorate Form Field in PDF",
    "alternativeHeadline": "Enhance PDF Forms with Custom Field Decorations",
    "abstract": "Apresentando um recurso poderoso que melhora a gestão de formulários PDF: a capacidade de decorar campos de formulário individuais ou todos os campos de formulário usando a Classe FormEditor. Essa funcionalidade permite que os usuários personalizem atributos de campo, como estilo de fonte, tamanho, cor da borda e alinhamento, simplificando o processo de criação de formulários PDF visualmente atraentes e bem estruturados. Melhore seus fluxos de trabalho em PDF com este método de decoração intuitivo para uma apresentação de documento mais polida.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "609",
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
    "url": "/net/decorate-form-field/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/decorate-form-field/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF pode realizar não apenas tarefas simples e fáceis, mas também lidar com objetivos mais complexos. Confira a próxima seção para usuários e desenvolvedores avançados."
}
</script>

## Decorar um Campo de Formulário Particular em um Arquivo PDF Existente

O método [DecorateField](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/decoratefield) presente na classe [FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor) permite decorar um campo de formulário particular em um arquivo PDF. Se você deseja decorar um campo específico, precisa passar o nome do campo para este método. No entanto, antes de chamar este método, você precisa criar objetos das classes [FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor) e [FormFieldFacade](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formfieldfacade). Você também precisa atribuir o objeto [FormFieldFacade](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formfieldfacade) à propriedade [Facade](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/properties/index) do objeto [FormEditor](https://reference.aspose.com/html/net/aspose.html.forms/formeditor). Depois disso, você pode definir quaisquer atributos fornecidos pelo objeto [FormFieldFacade](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formfieldfacade). Uma vez que você tenha definido os atributos, pode chamar o método [DecorateField](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/decoratefield) e, finalmente, salvar o PDF atualizado usando o método [Save](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/methods/save/index) da classe [FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor). O seguinte trecho de código mostra como decorar um campo de formulário particular.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void DecorateField()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Create an instance of FormEditor to manipulate form fields
    using (var editor = new Aspose.Pdf.Facades.FormEditor())
    {
        // Bind PDF document
        editor.BindPdf(dataDir + "Sample-Form-01.pdf");

        // Create a FormFieldFacade object to define decoration properties for the field
        var cityDecoration = new Aspose.Pdf.Facades.FormFieldFacade
        {
            // Set the font style to Courier
            Font = Aspose.Pdf.Facades.FontStyle.Courier,
            // Set the font size to 12
            FontSize = 12,
            // Set the border color to black
            BorderColor = System.Drawing.Color.Black,
            // Set the border width to 2
            BorderWidth = 2
        };

        // Assign the decoration facade to the FormEditor
        editor.Facade = cityDecoration;

        // Apply the decoration to the field named "City"
        editor.DecorateField("City");

        // Save PDF document
        editor.Save(dataDir + "Sample-Form-02.pdf");
    }
}
```

## Decorar Todos os Campos de um Tipo Particular em um Arquivo PDF Existente

O método [DecorateField](https://reference.aspose.com/pdf/net/aspose.pdf.facades.formeditor/decoratefield/methods/1) permite decorar todos os campos de formulário de um tipo particular em um arquivo PDF de uma só vez. Se você deseja decorar todos os campos de um tipo específico, precisa passar o tipo de campo para este método. No entanto, antes de chamar este método, você precisa criar objetos das classes [FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor) e [FormFieldFacade](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formfieldfacade). Você também precisa atribuir o objeto [FormFieldFacade](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formfieldfacade) à propriedade [Facade](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/properties/index) do objeto [FormEditor](https://reference.aspose.com/html/net/aspose.html.forms/formeditor). Depois disso, você pode definir quaisquer atributos fornecidos pelo objeto [FormFieldFacade](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formfieldfacade). Uma vez que você tenha definido os atributos, pode chamar o método [DecorateField](https://reference.aspose.com/pdf/net/aspose.pdf.facades.formeditor/decoratefield/methods/1) e, finalmente, salvar o PDF atualizado usando o método [Save](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/methods/save/index) da classe [FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor). O seguinte trecho de código mostra como decorar todos os campos de um tipo particular.

```csharp
 // For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void DecorateField2()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Create an instance of FormEditor to manipulate form fields
    using (var editor = new Aspose.Pdf.Facades.FormEditor())
    {
        // Bind PDF document
        editor.BindPdf(dataDir + "Sample-Form-01.pdf");

        // Create a FormFieldFacade object to define alignment properties for text fields
        var textFieldDecoration = new Aspose.Pdf.Facades.FormFieldFacade
        {
            // Set text alignment to center
            Alignment = Aspose.Pdf.Facades.FormFieldFacade.AlignCenter
        };

        // Assign the decoration facade to the FormEditor
        editor.Facade = textFieldDecoration;

        // Apply the alignment decoration to all text fields in the PDF
        editor.DecorateField(Aspose.Pdf.Facades.FieldType.Text);

        // Save PDF document
        editor.Save(dataDir + "Sample-Form-01-align-text.pdf");
    }
}
```