---
title: Adicionar Carimbo de Página PDF
type: docs
weight: 10
url: /net/add-pdf-page-stamp/
description: Esta seção explica como trabalhar com Aspose.PDF Facades usando a Classe PdfFileStamp.
lastmod: "2021-06-05"
draft: false
---

## Adicionar Carimbo de Página PDF em Todas as Páginas de um Arquivo PDF

A classe [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) permite que você adicione um carimbo de página PDF em todas as páginas de um arquivo PDF. In order to add PDF page stamp, you first need to create objects of [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) and [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) classes.

Para adicionar um carimbo na página PDF, você primeiro precisa criar objetos das classes [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) e [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp). Você também precisa criar o carimbo de página em PDF usando o método [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) da classe [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp). Você pode definir outros atributos como origem, rotação, fundo etc. usando o objeto [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) também. Em seguida, você pode adicionar o carimbo no arquivo PDF usando o método [AddStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/methods/addstamp) da classe [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp). Finalmente, salve o arquivo PDF de saída usando o método [Close](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/close) da classe [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp). O snippet de código a seguir mostra como adicionar um carimbo de página em PDF em todas as páginas de um arquivo PDF.

```csharp
public static void AddPageStampOnAllPages()
        {
            // Create PdfFileStamp object
            PdfFileStamp fileStamp = new PdfFileStamp();

            // Open Document
            fileStamp.BindPdf(_dataDir + "sample.pdf");

            // Create stamp
            Aspose.Pdf.Facades.Stamp stamp = new Aspose.Pdf.Facades.Stamp();
            stamp.BindPdf(_dataDir + "pagestamp.pdf", 1);
            stamp.SetOrigin(20, 20);
            stamp.Rotation = 90.0F;
            stamp.IsBackground = true;

            // Add stamp to PDF file
            fileStamp.AddStamp(stamp);

            // Save updated PDF file
            fileStamp.Save(_dataDir + "PageStampOnAllPages.pdf");

            // Close fileStamp
            fileStamp.Close();
        }
```
## Adicionar Carimbo de Página PDF em Páginas Específicas em um Arquivo PDF

A classe [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) permite que você adicione um carimbo de página PDF em páginas específicas de um arquivo PDF. In order to add PDF page stamp, you first need to create objects of [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) and [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) classes.

Para adicionar uma marca d'água em uma página PDF, você primeiro precisa criar objetos das classes [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) e [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp). Você também precisa criar o carimbo de página PDF usando o método [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3) da classe [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp). Você pode definir outros atributos como origem, rotação, fundo etc. using [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) objeto também. Como você deseja adicionar uma marca de página em PDF em páginas específicas do arquivo PDF, você também precisa definir a propriedade [Pages](https://reference.aspose.com/pdf/net/aspose.pdf.facades/stamp/properties/pages) da classe [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp). Esta propriedade requer uma matriz de inteiros contendo os números das páginas nas quais você deseja adicionar a marca. Em seguida, você pode adicionar a marca no arquivo PDF usando o método [AddStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/methods/addstamp) da classe [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp). Finalmente, salve o arquivo PDF de saída usando o método [Close](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/close) da classe [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp). O trecho de código a seguir mostra como adicionar uma marca de página em PDF em páginas específicas em um arquivo PDF.

```csharp
public static void AddPageStampOnCertainPages()
        {
            // Create PdfFileStamp object
            PdfFileStamp fileStamp = new PdfFileStamp();

            // Open Document
            fileStamp.BindPdf(_dataDir + "sample.pdf");

            // Create stamp
            Aspose.Pdf.Facades.Stamp stamp = new Aspose.Pdf.Facades.Stamp();
            stamp.BindPdf(_dataDir + "pagestamp.pdf", 1);
            stamp.SetOrigin(20, 20);
            stamp.Rotation = 90.0F;
            stamp.IsBackground = true;
            stamp.Pages = new[] { 1, 3 };
            // Add stamp to PDF file
            fileStamp.AddStamp(stamp);

            // Save updated PDF file
            fileStamp.Save(_dataDir + "PageStampOnAllPages.pdf");

            // Close fileStamp
            fileStamp.Close();
        }

        // Add PDF Page Numbers
        public enum PageNumPosition
        {
            PosBottomMiddle, PosBottomRight, PosUpperRight, PosSidesRight, PosUpperMiddle, PosBottomLeft, PosSidesLeft, PosUpperLeft
        }
```
## Adicionar Número de Página em um Arquivo PDF

A classe [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) permite adicionar números de página em um arquivo PDF. In order to add page numbers, you first need to create object of [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) class.

Para adicionar números de página, você primeiro precisa criar um objeto da classe [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp). If you want to show page number like “Page X of N” while X being the current page number and N the total number of pages in the PDF file then you first need to get the page count using [NumberOfpages](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileinfo/properties/numberofpages) property of [PdfFileInfo](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileinfo) class.

Se você quiser mostrar o número da página como "Página X de N", onde X é o número da página atual e N o número total de páginas no arquivo PDF, então primeiro você precisa obter a contagem de páginas usando a propriedade [NumberOfpages](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileinfo/properties/numberofpages) da classe [PdfFileInfo](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileinfo). Para obter o número da página atual, você pode usar o sinal **#** em seu texto onde quiser. Você pode formatar o texto do número da página usando a classe [FormattedText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formattedtext). Se você quiser iniciar a numeração de páginas a partir de um número específico, pode definir a propriedade [StartingNumber](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/properties/startingnumber). Quando estiver pronto para adicionar o número da página no arquivo, você precisará chamar o método [AddPageNumber](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffilestamp/addpagenumber/methods/7) da classe [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffilestamp). Finalmente, salve o arquivo PDF de saída usando o método [Close](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/close) da classe [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffilestamp). O trecho de código a seguir mostra como adicionar um número de página em um arquivo PDF.

```csharp
 public static void AddPageNumberInPdfFile()
        {
            // Criar objeto PdfFileStamp
            PdfFileStamp fileStamp = new PdfFileStamp();

            // Abrir Documento
            fileStamp.BindPdf(_dataDir + "sample.pdf");

            // Obter número total de páginas
            int totalPages = new PdfFileInfo(_dataDir + "sample.pdf").NumberOfPages;

            // Criar texto formatado para número de página
            FormattedText formattedText = new FormattedText($"Página # de {totalPages}",
                System.Drawing.Color.AntiqueWhite,
                System.Drawing.Color.Gray,
                FontStyle.TimesBoldItalic,
                EncodingType.Winansi, false, 12);

            // Definir número inicial para a primeira página; você pode querer começar a partir de 2 ou mais
            fileStamp.StartingNumber = 1;

            // Adicionar número de página
            fileStamp.AddPageNumber(formattedText, (int)PageNumPosition.PosUpperRight);

            // Salvar arquivo PDF atualizado
            fileStamp.Save(_dataDir + "AddPageNumber_out.pdf");

            // Fechar fileStamp
            fileStamp.Close();
        }
```
### Estilo de Numeração Personalizado

A classe PdfFileStamp oferece o recurso de adicionar informações de Número de Página como um objeto de carimbo dentro do documento PDF. Antes deste lançamento, a classe suportava apenas 1,2,3,4 como estilo de numeração de páginas. No entanto, houve uma exigência de alguns clientes para usar um estilo de numeração personalizado ao colocar o carimbo de número de página dentro do documento PDF. Para atender a essa exigência, a propriedade [NumberingStyle](https://reference.aspose.com/pdf/net/aspose.pdf/numberingstyle) foi introduzida, a qual aceita os valores da enumeração [NumberingStyle](https://reference.aspose.com/pdf/net/aspose.pdf/numberingstyle). Abaixo estão especificados os valores oferecidos nesta enumeração.

- LettersLowercase
- LettersUppercase
- NumeralsArabic
- NumeralsRomanLowercase
- NumeralsRomanUppercase

```csharp
 public static void AddCustomPageNumberInPdfFile()
        {
            // Criar objeto PdfFileStamp
            PdfFileStamp fileStamp = new PdfFileStamp();

            // Abrir Documento
            fileStamp.BindPdf(_dataDir + "sample.pdf");

            // Obter número total de páginas
            int totalPages = new PdfFileInfo(_dataDir + "sample.pdf").NumberOfPages;

            // Criar texto formatado para número de página
            FormattedText formattedText = new FormattedText($"Página # de {totalPages}",
                System.Drawing.Color.AntiqueWhite,
                System.Drawing.Color.Gray,
                FontStyle.TimesBoldItalic,
                EncodingType.Winansi, false, 12);

            // Especificar estilo de numeração como Números Romanos Maiúsculos
            fileStamp.NumberingStyle = Aspose.Pdf.NumberingStyle.NumeralsRomanUppercase;

            // Definir número inicial para a primeira página; você pode querer começar a partir de 2 ou mais
            fileStamp.StartingNumber = 1;

            // Adicionar número de página
            fileStamp.AddPageNumber(formattedText, (int)PageNumPosition.PosUpperRight);

            // Salvar arquivo PDF atualizado
            fileStamp.Save(_dataDir + "AddPageNumber_out.pdf");

            // Fechar fileStamp
            fileStamp.Close();
        }
```