---
title: Trabalhando com Operadores
linktitle: Trabalhando com Operadores
type: docs
weight: 170
url: /pt/net/operators/
description: Este tópico explica como usar operadores com Aspose.PDF. As classes de operadores oferecem ótimas funcionalidades para manipulação de PDF.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Trabalhando com Operadores",
    "alternativeHeadline": "Como usar operadores em PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "geração de documento pdf",
    "keywords": "pdf, c#, operadores em pdf, usar operadores em pdf",
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
    "url": "/net/operators/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/operators/"
    },
    "dateModified": "2022-02-04",
    "description": "Este tópico explica como usar operadores com Aspose.PDF. As classes de operadores oferecem ótimas funcionalidades para manipulação de PDF."
}
</script>
## Introdução aos Operadores PDF e Seu Uso

Um operador é uma palavra-chave PDF que especifica alguma ação que deve ser realizada, como pintar uma forma gráfica na página. Uma palavra-chave de operador é distinguida de um objeto nomeado pela ausência de um caractere sólido inicial (2Fh). Os operadores são significativos apenas dentro do fluxo de conteúdo.

Um fluxo de conteúdo é um objeto de fluxo PDF cujos dados consistem em instruções que descrevem os elementos gráficos a serem pintados em uma página. Mais detalhes sobre os operadores PDF podem ser encontrados na [especificação PDF](https://opensource.adobe.com/dc-acrobat-sdk-docs/).

### Detalhes da Implementação

Este tópico explica como usar operadores com Aspose.PDF.
Este tópico explica como usar operadores com Aspose.PDF.

- O operador **GSave** salva o estado gráfico atual do PDF.
- O operador **ConcatenateMatrix** (concatenar matriz) é usado para definir como uma imagem deve ser colocada na página do PDF.
- O operador **Do** desenha a imagem na página.
- O operador **GRestore** restaura o estado gráfico.

Para adicionar uma imagem em um arquivo PDF:

1. Crie um objeto [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) e abra o documento PDF de entrada.
1. Obtenha a página específica onde a imagem será adicionada.
1. Adicione a imagem na coleção de Recursos da página.
1. Use os operadores para colocar a imagem na página:
   - Primeiro, use o operador GSave para salvar o estado gráfico atual.
   - Em seguida, use o operador ConcatenateMatrix para especificar onde a imagem deve ser colocada.
   - Use o operador Do para desenhar a imagem na página.
1. Finalmente, use o operador GRestore para salvar o estado gráfico atualizado.

O seguinte trecho de código também funciona com a biblioteca [Aspose.PDF.Drawing](/pdf/pt/net/drawing/).
O seguinte trecho de código também funciona com a biblioteca [Aspose.PDF.Drawing](/pdf/pt/net/drawing/).

O seguinte trecho de código mostra como usar operadores PDF.

```csharp
// Para exemplos completos e arquivos de dados, por favor vá para https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Operators();

// Abrir documento
Document pdfDocument = new Document(dataDir+ "PDFOperators.pdf");

// Definir coordenadas
int lowerLeftX = 100;
int lowerLeftY = 100;
int upperRightX = 200;
int upperRightY = 200;

// Obter a página onde a imagem precisa ser adicionada
Page page = pdfDocument.Pages[1];
// Carregar imagem em stream
FileStream imageStream = new FileStream(dataDir + "PDFOperators.jpg", FileMode.Open);
// Adicionar imagem à coleção de Imagens dos Recursos da Página
page.Resources.Images.Add(imageStream);
// Usando o operador GSave: este operador salva o estado gráfico atual
page.Contents.Add(new Aspose.Pdf.Operators.GSave());
// Criar objetos Retângulo e Matriz
Aspose.Pdf.Rectangle rectangle = new Aspose.Pdf.Rectangle(lowerLeftX, lowerLeftY, upperRightX, upperRightY);
Matrix matrix = new Matrix(new double[] { rectangle.URX - rectangle.LLX, 0, 0, rectangle.URY - rectangle.LLY, rectangle.LLX, rectangle.LLY });
// Usando o operador ConcatenateMatrix (concatenar matriz): define como a imagem deve ser colocada
page.Contents.Add(new Aspose.Pdf.Operators.ConcatenateMatrix(matrix));
XImage ximage = page.Resources.Images[page.Resources.Images.Count];
// Usando o operador Do: este operador desenha a imagem
page.Contents.Add(new Aspose.Pdf.Operators.Do(ximage.Name));
// Usando o operador GRestore: este operador restaura o estado gráfico
page.Contents.Add(new Aspose.Pdf.Operators.GRestore());
dataDir = dataDir + "PDFOperators_out.pdf";
// Salvar documento atualizado
pdfDocument.Save(dataDir);
```
## Desenhar XForm na Página usando Operadores

Este tópico demonstra como usar os operadores GSave/GRestore, o operador ContatenateMatrix para posicionar um xForm e o operador Do para desenhar um xForm em uma página.

O código abaixo envolve o conteúdo existente de um arquivo PDF com o par de operadores GSave/GRestore. Esta abordagem ajuda a obter o estado gráfico inicial no final do conteúdo existente. Sem essa abordagem, transformações indesejáveis podem permanecer no final da cadeia de operadores existente.

```csharp
// Para exemplos completos e arquivos de dados, por favor, vá para https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Operators();


string imageFile = dataDir+ "aspose-logo.jpg";
string inFile = dataDir + "DrawXFormOnPage.pdf";
string outFile = dataDir + "blank-sample2_out.pdf";

using (Document doc = new Document(inFile))
{
    OperatorCollection pageContents = doc.Pages[1].Contents;

    // A amostra demonstra
    // Uso dos operadores GSave/GRestore
    // Uso do operador ContatenateMatrix para posicionar xForm
    // Uso do operador Do para desenhar xForm na página

    // Envolve o conteúdo existente com o par de operadores GSave/GRestore
    //        isso é para obter o estado gráfico inicial no final do conteúdo existente
    //        caso contrário, podem permanecer algumas transformações indesejáveis no final da cadeia de operadores existente
    pageContents.Insert(1, new Aspose.Pdf.Operators.GSave());
    pageContents.Add(new Aspose.Pdf.Operators.GRestore());

    // Adiciona operador de salvar estado gráfico para limpar adequadamente o estado gráfico após novos comandos
    pageContents.Add(new Aspose.Pdf.Operators.GSave());

    #region criar xForm

    // Criar xForm
    XForm form = XForm.CreateNewForm(doc.Pages[1], doc);
    doc.Pages[1].Resources.Forms.Add(form);
    form.Contents.Add(new Aspose.Pdf.Operators.GSave());
    // Definir largura e altura da imagem
    form.Contents.Add(new Aspose.Pdf.Operators.ConcatenateMatrix(200, 0, 0, 200, 0, 0));
    // Carregar imagem em stream
    Stream imageStream = new FileStream(imageFile, FileMode.Open);
    // Adicionar imagem à coleção de Imagens dos Recursos XForm
    form.Resources.Images.Add(imageStream);
    XImage ximage = form.Resources.Images[form.Resources.Images.Count];
    // Usando o operador Do: este operador desenha a imagem
    form.Contents.Add(new Aspose.Pdf.Operators.Do(ximage.Name));
    form.Contents.Add(new Aspose.Pdf.Operators.GRestore());

    #endregion

    pageContents.Add(new Aspose.Pdf.Operators.GSave());
    // Posicionar o formulário nas coordenadas x=100 y=500
    pageContents.Add(new Aspose.Pdf.Operators.ConcatenateMatrix(1, 0, 0, 1, 100, 500));
    // Desenhar formulário com o operador Do
    pageContents.Add(new Aspose.Pdf.Operators.Do(form.Name));
    pageContents.Add(new Aspose.Pdf.Operators.GRestore());

    pageContents.Add(new Aspose.Pdf.Operators.GSave());
    // Posicionar o formulário nas coordenadas x=100 y=300
    pageContents.Add(new Aspose.Pdf.Operators.ConcatenateMatrix(1, 0, 0, 1, 100, 300));
    // Desenhar formulário com o operador Do
    pageContents.Add(new Aspose.Pdf.Operators.Do(form.Name));
    pageContents.Add(new Aspose.Pdf.Operators.GRestore());

    // Restaurar estado gráfico com GRestore após o GSave
    pageContents.Add(new Aspose.Pdf.Operators.GRestore());
    doc.Save(outFile);
}
```
## Remover Objetos Gráficos usando Classes de Operador

As classes de operador oferecem ótimas funcionalidades para manipulação de PDF. Quando um arquivo PDF contém gráficos que não podem ser removidos usando o método [DeleteImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/deleteimage) da classe [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor), as classes de operador podem ser usadas para removê-los.

O seguinte trecho de código mostra como remover gráficos. Por favor, note que se o arquivo PDF contiver rótulos de texto para os gráficos, eles podem persistir no arquivo PDF, usando essa abordagem. Portanto, procure os operadores gráficos por um método alternativo para deletar tais imagens.

```csharp
// Para exemplos completos e arquivos de dados, por favor, vá para https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// O caminho para o diretório de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Operators();

Document doc = new Document(dataDir+ "RemoveGraphicsObjects.pdf");
Page page = doc.Pages[2];
OperatorCollection oc = page.Contents;

// Operadores de pintura de caminho usados
Operator[] operators = new Operator[] {
        new Aspose.Pdf.Operators.Stroke(),
        new Aspose.Pdf.Operators.ClosePathStroke(),
        new Aspose.Pdf.Operators.Fill()
};

oc.Delete(operators);
doc.Save(dataDir+ "No_Graphics_out.pdf");
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF para .NET Library",
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

