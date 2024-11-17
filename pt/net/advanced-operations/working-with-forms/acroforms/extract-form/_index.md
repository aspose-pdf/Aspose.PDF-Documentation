---
title: Extract AcroForm - Extrair Dados de Formulário de PDF em C#
linktitle: Extract AcroForm
type: docs
weight: 30
url: /pt/net/extract-form/
description: Extraia formulário do seu documento PDF com a biblioteca Aspose.PDF para .NET. Obtenha valor de um campo individual do arquivo PDF.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Extract AcroForm",
    "alternativeHeadline": "Como extrair AcroForm de PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "geração de documentos PDF",
    "keywords": "pdf, c#, extract acroform",
    "wordcount": "302",
    "proficiencyLevel":"Iniciante",
    "publisher": {
        "@type": "Organization",
        "name": "Equipe de Documentação Aspose.PDF",
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
                "contactType": "vendas",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "vendas",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "vendas",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "url": "/net/extract-form/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/extract-form/"
    },
    "dateModified": "2022-02-04",
    "description": "Extraia formulário do seu documento PDF com a biblioteca Aspose.PDF para .NET. Obtenha valor de um campo individual do arquivo PDF."
}
</script>
O seguinte trecho de código também funciona com a biblioteca [Aspose.PDF.Drawing](/pdf/pt/net/drawing/).

## Extrair dados do formulário

### Obter Valores de todos os Campos do Documento PDF

Para obter valores de todos os campos em um documento PDF, você precisa navegar por todos os campos do formulário e então obter o valor usando a propriedade Value. Obtenha cada campo da coleção Form, no tipo de campo base chamado Field e acesse sua propriedade Value.

Os seguintes trechos de código C# mostram como obter os valores de todos os campos de um documento PDF.

```csharp
// Para exemplos completos e arquivos de dados, por favor vá para https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

// Abrir documento
Document pdfDocument = new Document(dataDir + "GetValuesFromAllFields.pdf");

// Obter valores de todos os campos
foreach (Field formField in pdfDocument.Form)
{
    Console.WriteLine("Nome do Campo : {0} ", formField.PartialName);
    Console.WriteLine("Valor : {0} ", formField.Value);
}
```
### Obter Valor de um Campo Individual de Documento PDF

A propriedade Value do campo do formulário permite que você obtenha o valor de um campo específico. Para obter o valor, obtenha o campo do formulário da coleção Form do objeto Document. Este exemplo em C# seleciona um [TextBoxField](https://reference.aspose.com/pdf/net/aspose.pdf.forms/textboxfield) e recupera seu valor usando a propriedade Value.

```csharp
// Para exemplos completos e arquivos de dados, por favor vá para https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

// Abrir documento
Document pdfDocument = new Document(dataDir + "GetValueFromField.pdf");

// Obter um campo
TextBoxField textBoxField = pdfDocument.Form["textbox1"] como TextBoxField;

// Obter valor do campo
Console.WriteLine("PartialName : {0} ", textBoxField.PartialName);
Console.WriteLine("Value : {0} ", textBoxField.Value);
```

Para obter a URL do botão de envio, use as seguintes linhas de código.

```csharp
// Para exemplos completos e arquivos de dados, por favor vá para https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

// Abrir documento
Document pdfDocument = new Document(dataDir + "GetValueFromField.pdf");
SubmitFormAction act = pdfDocument.Form[1].OnActivated como SubmitFormAction;
if(act != null)
Console.WriteLine(act.Url.Name);
```
### Obter Campos de Formulário de uma Região Específica do Arquivo PDF

Às vezes, você pode saber onde em um documento um campo de formulário está, mas não ter o nome dele. Por exemplo, se tudo o que você tem é um esquemático de um formulário impresso. Com Aspose.PDF para .NET, isso não é um problema. Você pode descobrir quais campos estão em uma região específica de um arquivo PDF. Para obter campos de formulário de uma região específica de um arquivo PDF:

1. Abra o arquivo PDF usando o objeto [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).
1. Obtenha o formulário da coleção Forms do documento.
1. Especifique a região retangular e passe-a ao método GetFieldsInRect do objeto Form. Uma coleção Fields é retornada.
1. Use isso para manipular os campos.

O seguinte trecho de código C# mostra como obter campos de formulário em uma região retangular específica de um arquivo PDF.

```csharp
// Para exemplos completos e arquivos de dados, por favor, vá para https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

// Abrir arquivo pdf
Aspose.Pdf.Document doc = new Aspose.Pdf.Document(dataDir + "GetFieldsFromRegion.pdf");

// Criar objeto retângulo para obter campos nessa área
Aspose.Pdf.Rectangle rectangle = new Aspose.Pdf.Rectangle(35, 30, 500, 500);

// Obter o formulário PDF
Aspose.Pdf.Forms.Form form = doc.Form;

// Obter campos na área retangular
Aspose.Pdf.Forms.Field[] fields = form.GetFieldsInRect(rectangle);

// Exibir nomes e valores dos campos
foreach (Field field in fields)
{
    // Exibir propriedades de colocação de imagem para todas as colocações
    Console.Out.WriteLine("Nome do Campo: " + field.FullName + "-" + "Valor do Campo: " + field.Value);
}
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Biblioteca Aspose.PDF para .NET",
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
                "contactType": "vendas",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "vendas",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "vendas",
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
    "applicationCategory": "Biblioteca de Manipulação de PDF para .NET",
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
```

