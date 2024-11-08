---
title: Extra Annotations using C#
linktitle: Extra Annotations
type: docs
weight: 60
url: /pt/net/extra-annotations/
description: Esta seção descreve como adicionar, obter e excluir tipos extras de anotações do seu documento PDF.
lastmod: "2023-09-12"
sitemap:
    changefreq: "monthly"
    priority: 0.5
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Extra Annotations using C#",
    "alternativeHeadline": "How to add Extra Annotations in PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "geração de documentos em PDF",
    "keywords": "pdf, c#, link annotation, caret annotation",
    "wordcount": "302",
    "proficiencyLevel":"Iniciante",
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
    "url": "/net/extra-annotations/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/extra-annotations/"
    },
    "dateModified": "2022-02-04",
    "description": "Esta seção descreve como adicionar, obter e excluir tipos extras de anotações do seu documento PDF."
}
</script>
## Como adicionar Anotação de Caret em um arquivo PDF existente

A Anotação de Caret é um símbolo que indica a edição de texto. A Anotação de Caret também é uma anotação de marcação, então a classe Caret deriva da classe Markup e também fornece funções para obter ou definir propriedades da Anotação de Caret e reiniciar o fluxo da aparência da Anotação de Caret.

O seguinte trecho de código também funciona com a biblioteca [Aspose.PDF.Drawing](/pdf/pt/net/drawing/).

Etapas com as quais criamos a anotação de Caret:

1. Carregar o arquivo PDF - novo [Documento](https://reference.aspose.com/pdf/net/aspose.pdf/document).
1. Criar uma nova [Anotação de Caret](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/caretannotation) e definir os parâmetros do Caret (novo Retângulo, título, Assunto, Flags, cor, largura, Estilo de Início e Estilo de Final). Esta anotação é usada para indicar a inserção de texto.
1. Crie uma nova [StrikeOutAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/strikeoutannotation) e defina os parâmetros (novo Rectangle, título, cor, novos QuadPoints e novos pontos, Assunto, InReplyTo, ReplyType).
1. Após, podemos adicionar anotações à página.

O seguinte trecho de código mostra como adicionar uma Anotação Caret a um arquivo PDF:

```csharp
using Aspose.Pdf.Annotations;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Aspose.Pdf.Examples.Advanced
{
    class ExampleCaretAnnotation
    {
        // O caminho para o diretório de documentos.
        private const string _dataDir = "..\\..\\..\\..\\Samples";
        public static void AddCaretAnnotation()
        {
            // Carregar o arquivo PDF
            Document document = new Document(System.IO.Path.Combine(_dataDir, "sample.pdf"));
            // Esta anotação é usada para indicar a inserção de texto
            var caretAnnotation1 = new CaretAnnotation(document.Pages[1], new Rectangle(299.988, 713.664, 308.708, 720.769))
            {
                Title = "Usuário Aspose",
                Subject = "Texto inserido 1",
                Flags = AnnotationFlags.Print,
                Color = Color.Blue
            };
            // Esta anotação é usada para indicar a substituição de texto
            var caretAnnotation2 = new CaretAnnotation(document.Pages[1], new Rectangle(361.246, 727.908, 370.081, 735.107))
            {
                Flags = AnnotationFlags.Print,
                Subject = "Texto inserido 2",
                Title = "Usuário Aspose",
                Color = Color.Blue
            };

            var strikeOutAnnotation = new StrikeOutAnnotation(document.Pages[1],
                new Rectangle(318.407, 727.826, 368.916, 740.098))
            {
                Color = Color.Blue,
                QuadPoints = new[] {
                new Point(321.66, 739.416),
                new Point(365.664, 739.416),
                new Point(321.66, 728.508),
                new Point(365.664, 728.508)
            },
                Subject = "Riscado",
                InReplyTo = caretAnnotation2,
                ReplyType = ReplyType.Group
            };

            document.Pages[1].Annotations.Add(caretAnnotation1);
            document.Pages[1].Annotations.Add(caretAnnotation2);
            document.Pages[1].Annotations.Add(strikeOutAnnotation);

            document.Save(System.IO.Path.Combine(_dataDir, "sample_caret.pdf"));
        }
```

### Obter Anotação de Caret

Por favor, tente usar o seguinte trecho de código para Obter Anotação de Caret em documento PDF

```csharp
public static void GetCaretAnnotation()
{
    // Carregar o arquivo PDF
    Document document = new Document(System.IO.Path.Combine(_dataDir, "sample_caret.pdf"));
    var caretAnnotations = document.Pages[1].Annotations
        .Where(a => a.AnnotationType == AnnotationType.Caret)
        .Cast<CaretAnnotation>();
    foreach (var ca in caretAnnotations)
    {
        Console.WriteLine($"{ca.Rect}");
    }
}
```

### Excluir Anotação de Caret

O seguinte trecho de código mostra como Excluir Anotação de Caret de um arquivo PDF.

```csharp
public static void DeleteCaretAnnotation()
{
    // Carregar o arquivo PDF
    Document document = new Document(System.IO.Path.Combine(_dataDir, "sample_caret.pdf"));
    var caretAnnotations = document.Pages[1].Annotations
        .Where(a => a.AnnotationType == AnnotationType.Caret)
        .Cast<CaretAnnotation>();

    foreach (var ca in caretAnnotations)
    {
        document.Pages[1].Annotations.Delete(ca);
    }
    document.Save(System.IO.Path.Combine(_dataDir, "sample_caret_del.pdf"));
}
```
## Reduzir certa região da página com Anotação de Redação usando Aspose.PDF para .NET

Aspose.PDF para .NET suporta a funcionalidade de adicionar e manipular Anotações em um arquivo PDF existente. Recentemente, alguns de nossos clientes postaram uma necessidade de redigir (remover texto, imagem, etc elementos de) uma certa região da página de um documento PDF. Para atender a essa necessidade, uma classe chamada RedactionAnnotation é fornecida, que pode ser usada para redigir certas regiões da página ou pode ser usada para manipular RedactionAnnotations existentes e redigi-las (ou seja, achatar a anotação e remover o texto sob ela).

```csharp
// Para exemplos completos e arquivos de dados, por favor vá para https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

// Abrir documento
Document doc = new Document(dataDir + "input.pdf");

// Criar instância de RedactionAnnotation para região específica da página
RedactionAnnotation annot = new RedactionAnnotation(doc.Pages[1], new Aspose.Pdf.Rectangle(200, 500, 300, 600));
annot.FillColor = Aspose.Pdf.Color.Green;
annot.BorderColor = Aspose.Pdf.Color.Yellow;
annot.Color = Aspose.Pdf.Color.Blue;
// Texto a ser impresso na anotação de redação
annot.OverlayText = "REDACTED";
annot.TextAlignment = Aspose.Pdf.HorizontalAlignment.Center;
// Repetir texto de sobreposição sobre a Anotação de Redação
annot.Repeat = true;
// Adicionar anotação à coleção de anotações da primeira página
doc.Pages[1].Annotations.Add(annot);
// Achata a anotação e redige o conteúdo da página (ou seja, remove texto e imagem
// Sob a anotação redigida)
annot.Redact();
dataDir = dataDir + "RedactPage_out.pdf";
doc.Save(dataDir);
```
### Abordagem de Fachadas

O namespace Aspose.PDF.Facades também possui uma classe chamada [PdfAnnotationEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor) que oferece a funcionalidade de manipular Anotações existentes dentro de arquivos PDF. Esta classe contém um método chamado [RedactArea(..)](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor/methods/redactarea) que proporciona a capacidade de remover certas regiões da página.

```csharp
// Para exemplos completos e arquivos de dados, por favor, visite https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

Aspose.Pdf.Facades.PdfAnnotationEditor editor = new Aspose.Pdf.Facades.PdfAnnotationEditor();
// Reduzir uma certa região da página
editor.RedactArea(1, new Aspose.Pdf.Rectangle(100, 100, 20, 70), System.Drawing.Color.White);
editor.BindPdf(dataDir + "input.pdf");
editor.Save(dataDir + "FacadesApproach_out.pdf");
```

<script type="application/ld+json">

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF para Biblioteca .NET",
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

