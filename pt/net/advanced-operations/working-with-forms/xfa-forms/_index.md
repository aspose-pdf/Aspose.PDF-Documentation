---
title: Trabalhando com Formulários XFA
linktitle: Formulários XFA
type: docs
weight: 20
url: pt/net/xfa-forms/
description: A API Aspose.PDF para .NET permite trabalhar com campos XFA e Acroform XFA em um documento PDF. As Aspose.PDF.Facades.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Trabalhando com Formulários XFA",
    "alternativeHeadline": "Preencher, Converter e Obter Formulários XFA em PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "geração de documento pdf",
    "keywords": "pdf, c#, preencher formulário xfa, obter formulário xfa, converter formulário xfa",
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
    "url": "/net/xfa-forms/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/xfa-forms/"
    },
    "dateModified": "2022-02-04",
    "description": "A API Aspose.PDF para .NET permite trabalhar com campos XFA e Acroform XFA em um documento PDF. As Aspose.PDF.Facades."
}
</script>

{{% alert color="primary" %}}

Formulários dinâmicos são baseados em uma especificação XML conhecida como XFA, a "Arquitetura de Formulários XML". Ele também pode converter formulário XFA dinâmico para Acroform padrão. As informações sobre o formulário (no que diz respeito ao PDF) são muito vagas – especifica que os campos existem, com propriedades e eventos JavaScript, mas não especifica qualquer renderização. Os objetos do formulário XFA são desenhados no momento do carregamento do documento.

{{% /alert %}}

A classe Form oferece a capacidade de lidar com AcroForm estático e você pode obter uma instância de campo específica usando o método GetFieldFacade(..) da classe Form. No entanto, os campos XFA não podem ser acessados ​​via método Form.GetFieldFacade(..). Em vez disso, use [Document.Form.XFA](https://reference.aspose.com/pdf/net/aspose.pdf.forms/form/properties/xfa) para obter/definir valores de campo e manipular o modelo de campo XFA (definir propriedades de campo).

O seguinte trecho de código também funciona com a biblioteca [Aspose.PDF.Drawing](/pdf/net/drawing/).

## Preencher campos XFA

O seguinte trecho de código mostra como preencher campos em um formulário XFA.
O seguinte trecho de código mostra como preencher campos em um formulário XFA.

```csharp
// Para exemplos completos e arquivos de dados, por favor, visite https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

// Carregar formulário XFA
Document doc = new Document(dataDir + "FillXFAFields.pdf");

// Obter nomes dos campos do formulário XFA
string[] names = doc.Form.XFA.FieldNames;

// Definir valores dos campos
doc.Form.XFA[names[0]] = "Campo 0";
doc.Form.XFA[names[1]] = "Campo 1";
dataDir = dataDir + "Filled_XFA_out.pdf";
// Salvar o documento atualizado
doc.Save(dataDir);
```

## Converter XFA para Acroform

{{% alert color="primary" %}}

Experimente online
Você pode verificar a qualidade da conversão de Aspose.PDF e ver os resultados online neste link: [products.aspose.app/pdf/xfa/](https://products.aspose.app/pdf/xfa/)

{{% /alert %}}

Formulários dinâmicos são baseados em uma especificação XML conhecida como XFA, a "Arquitetura de Formulários XML".
Formulários dinâmicos são baseados em uma especificação XML conhecida como XFA, a "Arquitetura de Formulários XML".

Atualmente, o PDF suporta dois métodos diferentes para integrar dados e formulários PDF:

- AcroForms (também conhecidos como formulários Acrobat), introduzidos e incluídos na especificação do formato PDF 1.2.
- Formulários Adobe XML Forms Architecture (XFA), introduzidos na especificação do formato PDF 1.5 como um recurso opcional (A especificação XFA não está incluída na especificação PDF, apenas referenciada.)

Não podemos extrair ou manipular páginas de Formulários XFA, porque o conteúdo do formulário é gerado em tempo de execução (durante a visualização do formulário XFA) dentro da aplicação que tenta exibir ou renderizar o formulário XFA. O Aspose.PDF tem um recurso que permite aos desenvolvedores converter formulários XFA para AcroForms padrão.

```csharp
// Para exemplos completos e arquivos de dados, por favor, vá para https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

// Carregar formulário XFA dinâmico
Document document = new Document(dataDir + "DynamicXFAToAcroForm.pdf");

// Definir o tipo de campos de formulário como AcroForm padrão
document.Form.Type = FormType.Standard;

dataDir = dataDir + "Standard_AcroForm_out.pdf";
// Salvar o PDF resultante
document.Save(dataDir);
```

## Obter propriedades do campo XFA

Para acessar as propriedades do campo, primeiro use Document.Form.XFA.Teamplate para acessar o template do campo. O trecho de código a seguir mostra os passos para obter as coordenadas X e Y de um campo de formulário XFA.

```csharp
// Para exemplos completos e arquivos de dados, por favor, visite https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

// Carregar o formulário XFA
Document doc = new Document(dataDir + "GetXFAProperties.pdf");

string[] names = doc.Form.XFA.FieldNames;

// Definir valores de campo
doc.Form.XFA[names[0]] = "Campo 0";
doc.Form.XFA[names[1]] = "Campo 1";

// Obter posição do campo
Console.WriteLine(doc.Form.XFA.GetFieldTemplate(names[0]).Attributes["x"].Value);

// Obter posição do campo
Console.WriteLine(doc.Form.XFA.GetFieldTemplate(names[0]).Attributes["y"].Value);

dataDir = dataDir + "Filled_XFA_out.pdf";
// Salvar o documento atualizado
doc.Save(dataDir);
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


