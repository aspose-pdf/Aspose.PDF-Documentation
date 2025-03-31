---
title: Mesclar arquivos PDF usando .NET 5
linktitle: Como mesclar PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 75
url: /pt/net/how-to-concatenate-pdf-files-in-different-ways/
description: Este artigo explica as possíveis maneiras de concatenar qualquer número de arquivos PDF existentes em um único arquivo PDF.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Merge PDF files",
    "alternativeHeadline": "Effortlessly Combine Multiple PDFs",
    "abstract": "Mescle vários arquivos PDF em um único documento de forma contínua com a nova funcionalidade em Aspose.PDF for .NET. Este recurso permite que os desenvolvedores concatenem qualquer número de PDFs por meio de chamadas de método simples, aumentando a produtividade na gestão e manipulação de PDFs. Integre essa capacidade sem esforço em várias aplicações .NET, incluindo ASP.NET e aplicações Windows, com abordagens versáteis que atendem a diferentes necessidades",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "840",
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
    "url": "/net/how-to-concatenate-pdf-files-in-different-ways/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/how-to-concatenate-pdf-files-in-different-ways/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF pode realizar não apenas tarefas simples e fáceis, mas também lidar com objetivos mais complexos. Confira a próxima seção para usuários e desenvolvedores avançados."
}
</script>

{{% alert color="primary" %}}

Este artigo descreve como você pode [Concatenar](https://reference.aspose.com/pdf/pt/net/aspose.pdf.facades/pdffileeditor/methods/concatenate/index) vários Documentos PDF em um Único Documento PDF com a ajuda do Componente [Aspose.PDF for .NET](/pdf/pt/net/). [Aspose.PDF for .NET](/pdf/pt/net/) torna esse trabalho fácil como um pedaço de bolo.

{{% /alert %}}

Tudo o que você precisa fazer é chamar o método [Concatenate](https://reference.aspose.com/pdf/pt/net/aspose.pdf.facades/pdffileeditor/methods/concatenate/index) da classe [PdfFileEditor](https://reference.aspose.com/pdf/pt/net/aspose.pdf.facades/pdffileeditor) e todos os seus arquivos PDF de entrada serão concatenados juntos e um único arquivo PDF será gerado. Vamos criar uma aplicação para praticar a concatenação de arquivos PDF. Criaremos uma aplicação usando o Visual Studio.NET 2019.

{{% alert color="primary" %}}

Aspose.PDF for .NET pode ser usado em qualquer tipo de aplicação que esteja rodando no .NET Framework, seja uma aplicação web ASP.NET ou uma Aplicação Windows.

{{% /alert %}}

## Como Concatenar Arquivos PDF de Diferentes Maneiras

No formulário, há três Caixas de Texto (textBox1, textBox2, textBox3) com seus respectivos Rótulos de Link (linkLabel1, linkLabel2, linkLabel3) para navegar pelos arquivos PDF. Ao clicar no Rótulo de Link "Procurar", um Diálogo de Arquivo de Entrada (inputFileDialog1) aparecerá, permitindo-nos escolher os arquivos PDF (a serem concatenados).

```csharp
private void linkLabel1_LinkClicked(object sender, System.Windows.Forms.LinkLabelLinkClickedEventArgs e)
{
    if (openFileDialog1.ShowDialog()==DialogResult.OK)
    {
        textBox1.Text=openFileDialog1.FileName;
    }
}
```

A visualização de uma aplicação de formulário do Windows é mostrada para a demonstração da classe [PdfFileEditor](https://reference.aspose.com/pdf/pt/net/aspose.pdf.facades/pdffileeditor) para a Concatenação de Arquivos PDF.

![Concatenar Arquivos PDF](how-to-concatenate-pdf-files-in-different-ways_1.png)

Depois de escolher o arquivo PDF e clicar no botão OK. O nome completo do arquivo com o caminho é atribuído à Caixa de Texto relacionada.

![Escolher o arquivo PDF](how-to-concatenate-pdf-files-in-different-ways_2.png)

Da mesma forma, podemos escolher dois ou três Arquivos PDF de Entrada para concatenar, conforme mostrado abaixo:

![Escolher dois ou três Arquivos PDF de Entrada](how-to-concatenate-pdf-files-in-different-ways_3.png)

A última Caixa de Texto (textBox4) receberá o Caminho de Destino do arquivo PDF de Saída com seu nome, onde este arquivo de saída será criado.

![Caminho de Destino do arquivo PDF de Saída](how-to-concatenate-pdf-files-in-different-ways_4.png)

![Método Concatenate](how-to-concatenate-pdf-files-in-different-ways_5.png)

## Método Concatenate()

O método Concatenate() pode ser usado de três maneiras. Vamos dar uma olhada mais de perto em cada uma delas:

### Abordagem 1

- Concatenate(string firstInputFile, string secInputFile, string outputFile)

Esta abordagem é boa apenas se você precisar juntar apenas dois arquivos PDF. Os dois primeiros argumentos (firstInputFile e secInputFile) fornecem os nomes completos dos arquivos com seus caminhos de armazenamento dos dois arquivos PDF de entrada que devem ser concatenados. O terceiro argumento (outputFile) fornece o nome desejado com o caminho do arquivo PDF de saída.

![Concatenar dois PDFs usando Nomes de Arquivos](how-to-concatenate-pdf-files-in-different-ways_6.png)

```csharp
private void button1_Click(object sender, System.EventArgs e)
{
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    pdfEditor.Concatenate(textBox1.Text,textBox2.Text,textBox4.Text);
}
```

### Abordagem 2

- Concatenate(Stream firstInputStream, Stream secInputStream, Stream outputStream)

Semelhante à abordagem acima, esta abordagem também permite juntar dois arquivos PDF. Os dois primeiros argumentos (firstInputStream e secInputStream) fornecem os dois arquivos PDF de entrada como Streams (um stream é um array de bits/bytes) que devem ser concatenados. O terceiro argumento (outputStream) fornece a representação em stream do arquivo PDF de saída desejado.

![Concatenar dois PDFs usando Streams de Arquivo](how-to-concatenate-pdf-files-in-different-ways_7.png)

```csharp
private void button2_Click(object sender, System.EventArgs e)
{
    using (var pdf1 = new FileStream(textBox1.Text, FileMode.Open))
    {
        using (var pdf2 = new FileStream(textBox2.Text, FileMode.Open))
        {
            using (var outputStream = new FileStream(textBox4.Text, FileMode.Create))
            {
                var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
                pdfEditor.Concatenate(pdf1, pdf2, outputStream);
            }
        }
    }
}
```

### Abordagem 3

- Concatenate(Stream inputStreams[], Stream outputStream)

Se você quiser juntar mais de dois arquivos PDF, então esta abordagem seria sua escolha definitiva. O primeiro argumento (inputStreams[]) fornece os arquivos PDF de entrada na forma de um Array de Streams que devem ser concatenados. O segundo argumento (outputStream) fornece a representação em stream do arquivo PDF de saída desejado.

![Concatenar múltiplos PDFs usando Array de Streams](how-to-concatenate-pdf-files-in-different-ways_8.png)

```csharp
private void button3_Click(object sender, System.EventArgs e)
{
    using (var pdf1 = new FileStream(textBox1.Text, FileMode.Open))
    {
        using (var pdf2 = new FileStream(textBox2.Text, FileMode.Open))
        {
            using (var pdf3 = new FileStream(textBox3.Text, FileMode.Open))
            {
                var pdfStreams = new Stream[] { pdf1, pdf2, pdf3 };
                using (var outputStream = new FileStream(textBox4.Text, FileMode.Create))
                {
                    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
                    pdfEditor.Concatenate(pdfStreams, outputStream);
                }
            }
        }
    }
}
```