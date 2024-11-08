---
title: Como Criar PDF usando C#
linktitle: Criar Documento PDF
type: docs
weight: 10
url: /pt/net/create-pdf-document/
description: Criar e formatar o Documento PDF com Aspose.PDF para .NET.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Como Criar PDF usando C#",
    "alternativeHeadline": "Criar documento PDF do zero",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "geração de documento pdf",
    "keywords": "pdf, dotnet, criar documento pdf",
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
    "url": "/net/create-pdf-document/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/create-pdf-document/"
    },
    "dateModified": "2022-02-04",
    "description": "Criar e formatar o Documento PDF com Aspose.PDF para .NET."
}
</script>

Estamos sempre procurando uma maneira de gerar documentos PDF e trabalhar com eles em projetos C# de forma mais exata, precisa e eficaz. Ter funções fáceis de usar de uma biblioteca nos permite focar mais no trabalho e menos nos detalhes demorados de tentar gerar PDFs, seja em .NET.

O seguinte trecho de código também funciona com a biblioteca [Aspose.PDF.Drawing](/pdf/pt/net/drawing/).

## Criar (ou Gerar) documento PDF usando a linguagem C#

Aspose.PDF para .NET API permite criar e ler arquivos PDF usando C# e VB.NET. A API pode ser usada em uma variedade de aplicações .NET incluindo WinForms, ASP.NET, e várias outras. Neste artigo, vamos mostrar como usar a Aspose.PDF para .NET API para gerar e ler arquivos PDF facilmente em aplicações .NET.

### Como Criar um Arquivo PDF Simples

Para criar um arquivo PDF usando C#, os seguintes passos podem ser usados.

1. Criar um objeto da classe [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document)
1. Adicione [TextFragment](https://reference.aspose.com/pdf/net/aspose.pdf.text/textfragment) à coleção [Paragraphs](https://reference.aspose.com/pdf/net/aspose.pdf/page/properties/paragraphs) da página
1. Salve o documento PDF resultante

```csharp
// O caminho para o diretório de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_QuickStart();

// Inicialize o objeto do documento
Document document = new Document();
// Adiciona página
Page page = document.Pages.Add();
// Adiciona texto à nova página
page.Paragraphs.Add(new Aspose.Pdf.Text.TextFragment("Olá Mundo!"));
// Salva o PDF atualizado
document.Save(dataDir + "HelloWorld_out.pdf");
```

### Como Criar um Documento PDF Pesquisável

Aspose.PDF para .NET oferece o recurso de criar assim como manipular documentos PDF existentes.
Aspose.PDF para .NET oferece a funcionalidade de criar e manipular documentos PDF existentes.

A lógica especificada abaixo reconhece texto em imagens PDF. Para o reconhecimento, você pode usar suportes OCR externos que seguem o padrão HOCR. Para fins de teste, usamos o Google tesseract OCR gratuito. Portanto, primeiro você precisa instalar o Tesseract-OCR no seu sistema e terá o aplicativo de console do tesseract.

A seguir está o código completo para realizar essa exigência:

```csharp
using System;

namespace Aspose.Pdf.Examples.Advanced.WorkingWithDocuments
{
    class ExampleCreateDocument
    {
        private const string _dataDir = "C:\\Samples";
        public static void CreateSearchableDocuments(string file)
        {
            Aspose.Pdf.Document doc = new Aspose.Pdf.Document(file);
            bool convertResult = false;
            try
            {
                convertResult = doc.Convert(CallBackGetHocr);
            }
            catch (Exception ex)
            {
                Console.WriteLine(ex.Message);
            }
            doc.Save(file);
            doc.Dispose();
        }

        static string CallBackGetHocr(System.Drawing.Image img)
        {
            string tmpFile = System.IO.Path.GetTempFileName();
            try
            {
                System.Drawing.Bitmap bmp = new System.Drawing.Bitmap(img);

                bmp.Save(tmpFile, System.Drawing.Imaging.ImageFormat.Bmp);
                string inputFile = string.Concat('"', tmpFile, '"');
                string outputFile = string.Concat('"', tmpFile, '"');
                string arguments = string.Concat(inputFile, " ", outputFile, " -l eng hocr");
                string tesseractProcessName = @"C:\Program Files\Tesseract-OCR\Tesseract.exe";

                System.Diagnostics.ProcessStartInfo psi =
                    new System.Diagnostics.ProcessStartInfo(tesseractProcessName, arguments)
                    {
                        UseShellExecute = true,
                        CreateNoWindow = true,
                        WindowStyle = System.Diagnostics.ProcessWindowStyle.Hidden,
                        WorkingDirectory = System.IO.Path.GetDirectoryName(tesseractProcessName)
                    };

                System.Diagnostics.Process p = new System.Diagnostics.Process
                {
                    StartInfo = psi
                };
                p.Start();
                p.WaitForExit();

                System.IO.StreamReader streamReader = new System.IO.StreamReader(tmpFile + ".hocr");
                string text = streamReader.ReadToEnd();
                streamReader.Close();

                return text;
            }
            finally
            {
                if (System.IO.File.Exists(tmpFile))
                    System.IO.File.Delete(tmpFile);
                if (System.IO.File.Exists(tmpFile + ".hocr"))
                    System.IO.File.Delete(tmpFile + ".hocr");
            }
        }
    }
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
# Guia de Início Rápido

Bem-vindo ao Guia de Início Rápido! Este documento irá ajudá-lo a começar rapidamente com o uso do nosso software.

## Instalação

Para instalar o software, siga os passos abaixo:

1. Baixe o instalador da nossa página de downloads.
2. Execute o instalador e siga as instruções na tela.
3. Uma vez instalado, abra o software usando o ícone na sua área de trabalho.

## Configuração Inicial

Após instalar o software, você precisará configurá-lo:

```bash
$ config init
$ config set user.name "seu nome"
$ config set user.email "seu email"
```

## Como Usar

Para começar a usar o software, você pode seguir estes passos básicos:

1. Crie um novo projeto.
2. Adicione arquivos ao projeto.
3. Use as ferramentas disponíveis para modificar os arquivos.

## Ajuda

Se precisar de ajuda, consulte nossa documentação online ou entre em contato com o suporte técnico.

---
slug: /docs/quickstart
title: Guia de Início Rápido
description: Um guia para ajudá-lo a começar a usar o software rapidamente.
changefreq: "monthly"
type: docs
---

Esperamos que este guia rápido ajude você a começar a usar nosso software sem problemas. Para mais informações, consulte nossa documentação completa.
