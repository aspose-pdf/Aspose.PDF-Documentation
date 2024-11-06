---
title: Adicionando Imagens e Texto 
type: docs
weight: 10
url: pt/net/adding-images-and-text-using-pdffilemend-class/
description: Esta seção explica como Adicionar Imagens e Texto usando a classe PdfFileMend.
lastmod: "2021-06-05"
draft: false
---

A classe [PdfFileMend](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilemend) pode ajudar você a adicionar imagens e texto em um documento PDF existente, em um local especificado. It provides two methods with the names [AddImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilemend/methods/addimage/index) e [AddText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilemend/methods/addtext/index). [AddImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilemend/methods/addimage/index) método permite adicionar imagens do tipo JPG, GIF, PNG e BMP. [AddText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilemend/methods/addtext/index) método aceita um argumento do tipo classe [FormattedText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formattedtext) e o adiciona no arquivo PDF existente. As imagens e o texto podem ser adicionados em uma região retangular especificada pelas coordenadas dos pontos inferior esquerdo e superior direito. Ao adicionar imagens, você pode especificar o caminho do arquivo de imagem ou um fluxo de um arquivo de imagem. Para especificar o número da página na qual a imagem ou o texto precisam ser adicionados, ambos os métodos fornecem um argumento de número de página. Assim, você pode não apenas adicionar as imagens e o texto na localização especificada, mas também em uma página especificada.

As imagens são uma parte importante do conteúdo de um documento PDF. Manipular imagens em um arquivo PDF existente é um requisito comum para as pessoas que trabalham com arquivos PDF. Neste artigo, exploraremos como as imagens podem ser manipuladas, em um arquivo PDF existente, com a ajuda do [namespace Aspose.Pdf.Facades](https://reference.aspose.com/pdf/net/aspose.pdf.facades) do [Aspose.PDF for .NET](/pdf/net/). Todas as operações relacionadas a imagens do [namespace Aspose.Pdf.Facades](https://reference.aspose.com/pdf/net/aspose.pdf.facades) foram consolidadas neste artigo.

## Detalhes da implementação

[Namespace Aspose.Pdf.Facades](https://reference.aspose.com/pdf/net/aspose.pdf.facades) permite que você adicione novas imagens em um arquivo PDF existente. Você também pode substituir ou remover uma imagem existente. Um arquivo PDF também pode ser convertido em imagens. Você pode converter cada página individual em uma única imagem ou um arquivo PDF completo em uma imagem. Permite que você formate, ou seja, JPEG, BMP, PNG e TIFF, etc. Você também pode extrair as imagens de um arquivo PDF. Você pode usar quatro classes do [namespace Aspose.Pdf.Facades](https://reference.aspose.com/pdf/net/aspose.pdf.facades) para implementar essas operações, ou seja, [PdfFileMend](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilemend), [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor), [PdfExtractor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor) e [PdfConverter](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfconverter).

## Operações de Imagem

Nesta seção, teremos uma visão detalhada dessas operações de imagem. Nós também veremos os trechos de código para mostrar o uso das classes e métodos relacionados. Primeiro de tudo, vamos dar uma olhada em adicionar uma imagem em um arquivo PDF existente. Podemos usar o método [AddImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilemend/methods/addimage/index) da classe [PdfFileMend](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilemend) para adicionar uma nova imagem. Usando este método, você pode não apenas especificar o número da página na qual deseja adicionar a imagem, mas também a localização da imagem pode ser especificada.

## Adicionar Imagem em um Arquivo PDF Existente (Facades)

Você pode usar o método [AddImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilemend/methods/addimage) da classe [PdfFileMend](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilemend). O método [AddImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilemend/methods/addimage) requer a imagem a ser adicionada, o número da página em que a imagem precisa ser adicionada e a informação de coordenadas. Depois disso, salve o arquivo PDF atualizado usando o método [Close](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/close).

No exemplo a seguir, adicionamos uma imagem à página usando imageStream:

```csharp
public static void AddImage01()
        {
            Document document = new Document(_dataDir + "sample.pdf");
            PdfFileMend mender = new PdfFileMend();

            // Carregar imagem no stream
            var imageStream = System.IO.File.OpenRead(_dataDir + "logo.png");
            mender.BindPdf(document);
            mender.AddImage(imageStream, 1, 10, 650, 110, 750);

            // salvar o arquivo de saída
            mender.Save(_dataDir + "PdfFileMend04_output.pdf");
        }
```

![Adicionar Imagem](/pdf/net/images/add_image1.png)

Com a ajuda de [CompositingParameters](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffilemend/addimage/methods/1), podemos sobrepor uma imagem em cima de outra:
```csharp
public static void AddImage02()
        {
            Document document = new Document(_dataDir + "sample_color.pdf");
            PdfFileMend mender = new PdfFileMend();
            // Carregar imagem no fluxo
            var imageStream = System.IO.File.OpenRead(_dataDir + "logo.png");
            mender.BindPdf(document);
            int pageNum = 1;
            int lowerLeftX = 10;
            int lowerLeftY = 650;
            int upperRightX = 110;
            int upperRightY = 750;
            CompositingParameters compositingParameters = new CompositingParameters(BlendMode.Multiply);
            mender.AddImage(imageStream, pageNum, lowerLeftX, lowerLeftY, upperRightX, upperRightY, compositingParameters);

            // salvar o arquivo de saída
            mender.Save(_dataDir + "PdfFileMend05_output.pdf");
        }
```

![Add Image](/pdf/net/images/add_image2.png)

Existem várias maneiras de armazenar uma imagem em um arquivo PDF. Nós vamos demonstrar uma delas no exemplo a seguir:

```csharp
public static void AddImage03()
        {
            Document document = new Document(_dataDir + "sample_color.pdf");
            PdfFileMend mender = new PdfFileMend();
            // Carregar imagem no fluxo
            var imageStream = System.IO.File.OpenRead(_dataDir + "logo.png");
            mender.BindPdf(document);
            int pageNum = 1;
            int lowerLeftX = 10;
            int lowerLeftY = 650;
            int upperRightX = 110;
            int upperRightY = 750;
            CompositingParameters compositingParameters = new CompositingParameters(BlendMode.Exclusion, ImageFilterType.Flate);
            mender.AddImage(imageStream, pageNum, lowerLeftX, lowerLeftY, upperRightX, upperRightY, compositingParameters);

            // salvar o arquivo de saída
            mender.Save(_dataDir + "PdfFileMend06_output.pdf");
        }
```

```csharp
public static void AddImage04()
        {
            Document document = new Document(_dataDir + "sample_color.pdf");
            PdfFileMend mender = new PdfFileMend();
            // Carregar imagem no stream
            var imageStream = System.IO.File.OpenRead(_dataDir + "logo.png");
            mender.BindPdf(document);
            int pageNum = 1;
            int lowerLeftX = 10;
            int lowerLeftY = 650;
            int upperRightX = 110;
            int upperRightY = 750;
            CompositingParameters compositingParameters = new CompositingParameters(BlendMode.Multiply, ImageFilterType.Flate,false);
            mender.AddImage(imageStream, pageNum, lowerLeftX, lowerLeftY, upperRightX, upperRightY, compositingParameters);

            // salvar o arquivo de saída
            mender.Save(_dataDir + "PdfFileMend07_output.pdf");
        }
```

## Adicionar Texto em um Arquivo PDF Existente (facades)

Podemos adicionar texto de várias maneiras. Considere o primeiro. Pegamos o [FormattedText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formattedtext) e o adicionamos à Página. Depois, indicamos as coordenadas do canto inferior esquerdo, e então adicionamos nosso texto à Página.

```csharp
public static void AddText01()
        {
            PdfFileMend mender = new PdfFileMend();
            mender.BindPdf(_dataDir + "sample.pdf");
            FormattedText message = new FormattedText("Welcome to Aspose!");

            mender.AddText(message, 1, 10, 750);

            // save the output file
            mender.Save(_dataDir + "PdfFileMend01_output.pdf");
        }
```

Veja como fica:

![Add Text](/pdf/net/images/add_text.png)

A segunda maneira de adicionar [FormattedText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formattedtext). Além disso, indicamos um retângulo no qual nosso texto deve caber.

```csharp
public static void AddText02()
        {
            PdfFileMend mender = new PdfFileMend();
            mender.BindPdf(_dataDir + "sample.pdf");
            FormattedText message = new FormattedText("Welcome to Aspose! Welcome to Aspose!");

            mender.AddText(message, 1, 10, 700, 55, 810);
            mender.WrapMode = WordWrapMode.ByWords;

            // save the output file
            mender.Save(_dataDir + "PdfFileMend02_output.pdf");
        }
```
O terceiro exemplo fornece a capacidade de Adicionar Texto a páginas especificadas. Em nosso exemplo, vamos adicionar uma legenda nas páginas 1 e 3 do documento.

```csharp
public static void AddText03()
        {
            Document document = new Document(_dataDir + "sample.pdf");
            document.Pages.Add();
            document.Pages.Add();
            document.Pages.Add();
            PdfFileMend mender = new PdfFileMend();
            mender.BindPdf(document);
            FormattedText message = new FormattedText("Welcome to Aspose!");
            int[] pageNums = new int[] { 1, 3 };
            mender.AddText(message, pageNums, 10, 750, 310, 760);

            // save the output file
            mender.Save(_dataDir + "PdfFileMend03_output.pdf");
        }
```