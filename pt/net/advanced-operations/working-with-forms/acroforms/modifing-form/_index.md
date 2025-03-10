---
title: Modificando AcroForm
linktitle: Modificando AcroForm
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 40
url: /pt/net/modifing-form/
description: Modificando o formulário no seu arquivo PDF com a biblioteca Aspose.PDF for .NET. Você pode adicionar ou remover campos em um formulário existente, obter e definir limites de campo, etc.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Modifing AcroForm",
    "alternativeHeadline": "Modify and Manage AcroForm Fields in PDF",
    "abstract": "O novo recurso de Modificação de AcroForm na biblioteca Aspose.PDF for .NET permite que os usuários adicionem ou removam campos de formulários PDF existentes de forma contínua. Essa funcionalidade também inclui a definição de limites de campo e a personalização das aparências de fonte para uma experiência de usuário refinada, melhorando o gerenciamento e a interação com formulários PDF.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "Modifing AcroForm, Aspose.PDF for .NET, PDF form fields, SetFieldLimit, custom font, Add/remove fields, Document Form collection, DefaultAppearance, manage form fields, PDF manipulation",
    "wordcount": "601",
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
    "url": "/net/modifing-form/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/modifing-form/"
    },
    "dateModified": "2024-11-25",
    "description": "Modificando o formulário no seu arquivo PDF com a biblioteca Aspose.PDF for .NET. Você pode adicionar ou remover campos em um formulário existente, obter e definir limites de campo, etc."
}
</script>

O seguinte trecho de código também funciona com a biblioteca [Aspose.PDF.Drawing](/pdf/net/drawing/).

## Obter ou Definir Limite de Campo

O método SetFieldLimit(field, limit) da classe FormEditor permite que você defina um limite de campo, o número máximo de caracteres que podem ser inseridos em um campo.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SetFieldLimit()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Create FormEditor instance
    using (var form = new Aspose.Pdf.Facades.FormEditor())
    {
        // Bind PDF document
        form.BindPdf(dataDir + "input.pdf");

        // Set field limit for "textbox1"
        form.SetFieldLimit("textbox1", 15);

        // Save PDF document
        form.Save(dataDir + "SetFieldLimit_out.pdf");
    }
}
```

Da mesma forma, o Aspose.PDF possui um método que obtém o limite de campo usando a abordagem DOM. O seguinte trecho de código mostra os passos.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GetFieldLimitUsingDOM()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "FieldLimit.pdf"))
    {
        // Get the field and its maximum limit
        if (document.Form["textbox1"] is Aspose.Pdf.Forms.TextBoxField textBoxField)
        {
            Console.WriteLine("Limit: " + textBoxField.MaxLen);
        }
    }
}
```

Você também pode obter o mesmo valor usando o namespace *Aspose.Pdf.Facades* com o seguinte trecho de código.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GetFieldLimitUsingFacades()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Create Form instance
    using (var form = new Aspose.Pdf.Facades.Form())
    {
        // Bind PDF document
        form.BindPdf(dataDir + "FieldLimit.pdf");

        // Get the field limit for "textbox1"
        Console.WriteLine("Limit: " + form.GetFieldLimit("textbox1"));
    }
}
```

## Definir Fonte Personalizada para o Campo do Formulário

Os campos de formulário em arquivos PDF da Adobe podem ser configurados para usar fontes padrão específicas. Nas versões iniciais do Aspose.PDF, apenas as 14 fontes padrão eram suportadas. Versões posteriores permitiram que os desenvolvedores aplicassem qualquer fonte. Para definir e atualizar a fonte padrão usada para campos de formulário, use a classe DefaultAppearance(Font font, double size, Color color). Esta classe pode ser encontrada no namespace Aspose.Pdf.InteractiveFeatures. Para usar este objeto, utilize a propriedade DefaultAppearance da classe Field.

O seguinte trecho de código mostra como definir a fonte padrão para campos de formulário PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SetFormFieldFont()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "FormFieldFont14.pdf"))
    {
        // Get particular form field from document
        if (document.Form["textbox1"] is Aspose.Pdf.Forms.Field field)
        {
            // Create font object
            var font = Aspose.Pdf.Text.FontRepository.FindFont("ComicSansMS");

            // Set the font information for form field
            field.DefaultAppearance = new Aspose.Pdf.Annotations.DefaultAppearance(font, 10, System.Drawing.Color.Black);
        }

        // Save PDF document
        document.Save(dataDir + "FormFieldFont14_out.pdf");
    }
}
```

## Adicionar/remover campos em formulário existente

Todos os campos de formulário estão contidos na coleção Form do objeto Document. Esta coleção fornece diferentes métodos que gerenciam campos de formulário, incluindo o método Delete. Se você quiser excluir um campo específico, passe o nome do campo como um parâmetro para o método Delete e, em seguida, salve o documento PDF atualizado. O seguinte trecho de código mostra como excluir um campo específico de um documento PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void DeleteFormField()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "DeleteFormField.pdf"))
    {
        // Delete a particular field by name
        document.Form.Delete("textbox1");

        // Save PDF document
        document.Save(dataDir + "DeleteFormField_out.pdf");
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