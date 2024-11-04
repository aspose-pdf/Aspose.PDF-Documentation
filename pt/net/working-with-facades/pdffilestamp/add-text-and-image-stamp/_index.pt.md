---
title: Adicionar Carimbo de Texto e Imagem
type: docs
weight: 20
url: /net/add-text-and-image-stamp/
description: Esta seção explica como adicionar Carimbo de Texto e Imagem com Aspose.PDF Facades usando a Classe PdfFileStamp.
lastmod: "2021-06-05"
draft: false
---

## Adicionar Carimbo de Texto em Todas as Páginas de um Arquivo PDF

A classe [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) permite que você adicione um carimbo de texto em todas as páginas de um arquivo PDF. In order to add text stamp, you first need to create objects of [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) and [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) classes.

Para adicionar uma marca de texto, você primeiro precisa criar objetos das classes [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) e [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp). Você também precisa criar o carimbo de texto usando o método [BindLogo](https://reference.aspose.com/pdf/net/aspose.pdf.facades/stamp/methods/bindlogo) da classe [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp). Você pode definir outros atributos como origem, rotação, fundo etc. usando o objeto [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) também. Então, você pode adicionar o carimbo no arquivo PDF usando o método [AddStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/methods/addstamp) da classe [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp). Finalmente, salve o arquivo PDF de saída usando o método [Close](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/close) da classe [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp). O trecho de código a seguir mostra como adicionar um carimbo de texto em todas as páginas de um arquivo PDF.

```csharp
 public static void AddTextStampOnAllPagesInPdfFile()
        {
            // Create PdfFileStamp object
            PdfFileStamp fileStamp = new PdfFileStamp();

            // Open Document
            fileStamp.BindPdf(_dataDir + "sample.pdf");

            // Create stamp
            Stamp stamp = new Stamp();
            stamp.BindLogo(new FormattedText("Hello World!", System.Drawing.Color.Blue, System.Drawing.Color.Gray, Aspose.Pdf.Facades.FontStyle.Helvetica, EncodingType.Winansi, true, 14));
            stamp.SetOrigin(10, 400);
            stamp.Rotation = 90.0F;
            stamp.IsBackground = true;

            // Add stamp to PDF file
            fileStamp.AddStamp(stamp);

            // Save updated PDF file
            fileStamp.Save(_dataDir + "AddTextStamp-All_out.pdf");

            // Close fileStamp
            fileStamp.Close();
        }
```
## Adicionar Carimbo de Texto em Páginas Específicas em um Arquivo PDF

A classe [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) permite adicionar carimbo de texto em páginas específicas de um arquivo PDF. 
Para adicionar uma marca de texto, você primeiro precisa criar objetos das classes [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) e [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp). Você também precisa criar o carimbo de texto usando o método [BindLogo](https://reference.aspose.com/pdf/net/aspose.pdf.facades/stamp/methods/bindlogo) da classe [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp). Você pode definir outros atributos como origem, rotação, fundo etc. 
usando o objeto [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) também.
``` Como você deseja adicionar uma marca de texto em páginas específicas do arquivo PDF, você também precisa definir a propriedade [Pages](https://reference.aspose.com/pdf/net/aspose.pdf.facades/stamp/properties/pages) da classe [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp). Esta propriedade requer um array de inteiros contendo os números das páginas nas quais você deseja adicionar a marca. Em seguida, você pode adicionar a marca no arquivo PDF usando o método [AddStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/methods/addstamp) da classe [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp). Finalmente, salve o arquivo PDF de saída usando o método [Close](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/close) da classe [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp). O trecho de código a seguir mostra como adicionar uma marca de texto em páginas específicas em um arquivo PDF.

```csharp
 public static void AddTextStampOnParticularPagesInPdfFile()
        {
            // Create PdfFileStamp object
            PdfFileStamp fileStamp = new PdfFileStamp();

            // Open Document
            fileStamp.BindPdf(_dataDir + "sample.pdf");

            // Create stamp
            Aspose.Pdf.Facades.Stamp stamp = new Aspose.Pdf.Facades.Stamp();
            stamp.BindLogo(new FormattedText("Hello World!", System.Drawing.Color.Blue, System.Drawing.Color.Gray, Aspose.Pdf.Facades.FontStyle.Helvetica, EncodingType.Winansi, true, 14));
            stamp.SetOrigin(10, 400);
            stamp.Rotation = 90.0F;
            stamp.IsBackground = true;

            // Set particular pages
            stamp.Pages = new int[] { 2 };

            // Add stamp to PDF file
            fileStamp.AddStamp(stamp);

            // Save updated PDF file
            fileStamp.Save(_dataDir + "AddTextStamp-Page_out.pdf");

            // Close fileStamp
            fileStamp.Close();
        }
```
## Adicionar Carimbo de Imagem em Todas as Páginas de um Arquivo PDF

A classe [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) permite adicionar carimbo de imagem em todas as páginas de um arquivo PDF. In order to add image stamp, you first need to create objects of [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) e [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) classes. Você também precisa criar o carimbo de imagem usando o método [BindImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/stamp/methods/bindimage/index) da classe [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp). Você pode definir outros atributos como origem, rotação, plano de fundo etc. usando o objeto [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) também. Em seguida, você pode adicionar o carimbo no arquivo PDF usando o método [AddStamp](https://reference.aspose.com/pdf/net/aspose.pdf/page/methods/addstamp) da classe [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp). Finalmente, salve o arquivo PDF de saída usando o método [Close](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/close) da classe [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp). O trecho de código a seguir mostra como adicionar um carimbo de imagem em todas as páginas de um arquivo PDF.

```csharp
public static void AddImageStampOnAllPagesInPdfFile()
        {
            // Criar objeto PdfFileStamp
            PdfFileStamp fileStamp = new PdfFileStamp();

            // Abrir documento
            fileStamp.BindPdf(_dataDir + "sample.pdf");

            // Criar carimbo
            Aspose.Pdf.Facades.Stamp stamp = new Aspose.Pdf.Facades.Stamp();
            stamp.BindImage(_dataDir + "aspose-logo.png");
            stamp.SetOrigin(10, 200);
            stamp.Rotation = 90.0F;
            stamp.IsBackground = true;

            // Definir páginas específicas
            stamp.Pages = new int[] { 2 };

            // Adicionar carimbo ao arquivo PDF
            fileStamp.AddStamp(stamp);

            // Salvar arquivo PDF atualizado
            fileStamp.Save(_dataDir + "AddImageStamp-Page_out.pdf");

            // Fechar fileStamp
            fileStamp.Close();
        }
```
### Controlar a qualidade da imagem ao adicionar como carimbo

Ao adicionar uma imagem como objeto de carimbo, você também pode controlar a qualidade da imagem. Para atender a esse requisito, a propriedade Quality foi adicionada à classe [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp). Ela indica a qualidade da imagem em porcentagem (valores válidos são de 0 a 100).

## Adicionar Carimbo de Imagem em Páginas Específicas em um Arquivo PDF

A classe [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) permite que você adicione um carimbo de imagem em páginas específicas de um arquivo PDF. In order to add image stamp, you first need to create objects of [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) and [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) classes.

Para adicionar uma marca d'água de imagem, primeiro você precisa criar objetos das classes [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) e [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp). Você também precisa criar o carimbo de imagem usando o método [BindImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/stamp/methods/bindimage/index) da classe [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp). Você pode definir outros atributos como origem, rotação, fundo etc. usando o objeto [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) também. Como você quer adicionar um carimbo de imagem em páginas específicas do arquivo PDF, você também precisa definir a propriedade [Pages](https://reference.aspose.com/pdf/net/aspose.pdf.facades/stamp/properties/pages) da classe [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp). Esta propriedade requer um array de inteiros contendo os números das páginas nas quais você deseja adicionar o carimbo. Em seguida, você pode adicionar o carimbo no arquivo PDF usando o método [AddStamp](https://reference.aspose.com/pdf/net/aspose.pdf/page/methods/addstamp) da classe [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp). Finalmente, salve o arquivo PDF de saída usando o método [Close](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/close) da classe [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp). O trecho de código a seguir mostra como adicionar um carimbo de imagem em páginas específicas em um arquivo PDF.

```csharp
 public static void AddImageStampOnParticularPagesInPdfFile()
        {
            // Create PdfFileStamp object
            PdfFileStamp fileStamp = new PdfFileStamp();

            // Open Document
            fileStamp.BindPdf(_dataDir + "sample.pdf");

            // Create stamp
            Aspose.Pdf.Facades.Stamp stamp = new Aspose.Pdf.Facades.Stamp();
            stamp.BindImage(_dataDir + "aspose-logo.png");
            stamp.SetOrigin(10, 200);
            stamp.Rotation = 90.0F;
            stamp.IsBackground = true;

            // Add stamp to PDF file
            fileStamp.AddStamp(stamp);

            // Save updated PDF file
            fileStamp.Save(_dataDir + "AddImageStamp-All_out.pdf");

            // Close fileStamp
            fileStamp.Close();
        }
```