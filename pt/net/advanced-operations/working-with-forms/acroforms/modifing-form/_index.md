---
title: Modifing AcroForm
linktitle: Modifing AcroForm
type: docs
weight: 40
url: pt/net/modifing-form/
description: Modificando formulário em seu arquivo PDF com a biblioteca Aspose.PDF para .NET. Você pode adicionar ou remover campos no formulário existente, obter e definir limite de campo e etc.
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
    "alternativeHeadline": "How to Modifing AcroForm",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "pdf, c#, modifing acroform",
    "wordcount": "302",
    "proficiencyLevel":"Beginner",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF Doc Team",
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
    "dateModified": "2022-02-04",
    "description": "Modificando formulário em seu arquivo PDF com a biblioteca Aspose.PDF para .NET. Você pode adicionar ou remover campos no formulário existente, obter e definir limite de campo e etc."
}
</script>
O seguinte trecho de código também funciona com a biblioteca [Aspose.PDF.Drawing](/pdf/net/drawing/).

## Obter ou Definir Limite de Campo

O método SetFieldLimit(campo, limite) da classe FormEditor permite que você defina um limite de campo, o número máximo de caracteres que podem ser inseridos em um campo.

```csharp
// Para exemplos completos e arquivos de dados, por favor, vá para https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

// Adicionando campo com limite
FormEditor form = new FormEditor();

form.BindPdf(dataDir + "input.pdf");
form.SetFieldLimit("textbox1", 15);
dataDir = dataDir + "SetFieldLimit_out.pdf";
form.Save(dataDir);
```

Da mesma forma, Aspose.PDF tem um método que obtém o limite do campo usando a abordagem DOM. O seguinte trecho de código mostra os passos.

```csharp
// Para exemplos completos e arquivos de dados, por favor, vá para https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Forms();
// Obtendo limite máximo de campo usando DOM
Document doc = new Document(dataDir + "FieldLimit.pdf");
Console.WriteLine("Limite: " + (doc.Form["textbox1"] as TextBoxField).MaxLen);
```
Você também pode obter o mesmo valor usando o namespace *Aspose.PDF.Facades* utilizando o seguinte trecho de código.

```csharp
// Para exemplos completos e arquivos de dados, por favor, visite https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Forms();
// Obtendo o limite máximo do campo usando Facades
Aspose.Pdf.Facades.Form form = new Aspose.Pdf.Facades.Form();
form.BindPdf(dataDir + "FieldLimit.pdf");
Console.WriteLine("Limite: " + form.GetFieldLimit("textbox1"));
```

## Definir Fonte Personalizada para o Campo do Formulário

Os campos de formulário em arquivos PDF da Adobe podem ser configurados para usar fontes padrão específicas.
Os campos de formulário em arquivos Adobe PDF podem ser configurados para usar fontes padrão específicas.

O seguinte trecho de código mostra como definir a fonte padrão para campos de formulário PDF.

```csharp
// Para exemplos completos e arquivos de dados, por favor acesse https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

// Abrir documento
Document pdfDocument = new Document(dataDir + "FormFieldFont14.pdf");

// Obter um campo de formulário específico do documento
Aspose.Pdf.Forms.Field field = pdfDocument.Form["textbox1"] as Aspose.Pdf.Forms.Field;

// Criar objeto de fonte
Aspose.Pdf.Text.Font font = FontRepository.FindFont("ComicSansMS");

// Definir a informação de fonte para o campo de formulário
// Field.DefaultAppearance = new Aspose.Pdf.Forms.in.DefaultAppearance(font, 10, System.Drawing.Color.Black);

dataDir = dataDir + "FormFieldFont14_out.pdf";
// Salvar documento atualizado
pdfDocument.Save(dataDir);
```

## Adicionar/remover campos em formulário existente

Todos os campos de formulário estão contidos na coleção Form do objeto Document.
Todos os campos do formulário estão contidos na coleção Form do objeto Document.

```csharp
// Para exemplos completos e arquivos de dados, por favor acesse https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório dos documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

// Abrir documento
Document pdfDocument = new Document(dataDir + "DeleteFormField.pdf");

// Deletar um campo específico pelo nome
pdfDocument.Form.Delete("textbox1");
dataDir = dataDir + "DeleteFormField_out.pdf";
// Salvar documento modificado
pdfDocument.Save(dataDir);
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

