---
title: Adicionar Carimbo de Página em PDF
type: docs
weight: 10
url: /java/add-pdf-page-stamp/
description: Esta seção explica como trabalhar com Aspose.PDF Facades usando a Classe PdfFileStamp.
lastmod: "2021-06-05"
draft: false
---

## Adicionar Carimbo de Página em PDF em Todas as Páginas de um Arquivo PDF

A classe [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) permite adicionar um carimbo de página em PDF em todas as páginas de um arquivo PDF.
 In order to add PDF page stamp, you first need to create objects of [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) e [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp) classes. Você também precisa criar o carimbo da página PDF usando o método [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) da classe [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp). Você pode definir outros atributos como origem, rotação, fundo etc. usando o objeto [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp) também. Em seguida, você pode adicionar o carimbo no arquivo PDF usando o método [addStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#addStamp-com.aspose.pdf.facades.Stamp-) da classe [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp). Finalmente, salve o arquivo PDF de saída usando o método [close](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#close--) da classe [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp). O trecho de código a seguir mostra como adicionar um carimbo de página PDF em todas as páginas de um arquivo PDF.

```csharp
public static void AddPageStampOnAllPages()
        {
            // Criar objeto PdfFileStamp
            PdfFileStamp fileStamp = new PdfFileStamp();

            // Abrir Documento
            fileStamp.BindPdf(_dataDir + "sample.pdf");

            // Criar carimbo
            Aspose.Pdf.Facades.Stamp stamp = new Aspose.Pdf.Facades.Stamp();
            stamp.BindPdf(_dataDir + "pagestamp.pdf", 1);
            stamp.SetOrigin(20, 20);
            stamp.Rotation = 90.0F;
            stamp.IsBackground = true;

            // Adicionar carimbo ao arquivo PDF
            fileStamp.AddStamp(stamp);

            // Salvar arquivo PDF atualizado
            fileStamp.Save(_dataDir + "PageStampOnAllPages.pdf");

            // Fechar fileStamp
            fileStamp.Close();
        }
```

## Adicionar Carimbo de Página em PDF em Páginas Específicas de um Arquivo PDF

A classe [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) permite adicionar um carimbo de página em PDF em páginas específicas de um arquivo PDF.
 Para adicionar uma marca de página em PDF, você precisa primeiro criar objetos das classes [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) e [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp). Você também precisa criar o carimbo de página em PDF usando o método [bindPdf](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp#bindPdf-java.lang.String-int-) da classe [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp). Você pode definir outros atributos como origem, rotação, fundo etc. usando o objeto [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp) também. Como você deseja adicionar um carimbo de página em PDF em páginas específicas do arquivo PDF, você também precisa definir a propriedade [Pages](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp#setPages-int:A-) da classe [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp). Esta propriedade requer um array de inteiros contendo os números das páginas nas quais você deseja adicionar o carimbo. Em seguida, você pode adicionar o carimbo no arquivo PDF usando o método [addStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#addStamp-com.aspose.pdf.facades.Stamp-) da classe [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp). Finalmente, salve o arquivo PDF de saída usando o método [close](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#close--) da classe [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp). O trecho de código a seguir mostra como adicionar um carimbo de página em PDF em páginas específicas em um arquivo PDF.

```csharp
public static void AddPageStampOnCertainPages()
        {
            // Criar objeto PdfFileStamp
            PdfFileStamp fileStamp = new PdfFileStamp();

            // Abrir Documento
            fileStamp.BindPdf(_dataDir + "sample.pdf");

            // Criar carimbo
            Aspose.Pdf.Facades.Stamp stamp = new Aspose.Pdf.Facades.Stamp();
            stamp.BindPdf(_dataDir + "pagestamp.pdf", 1);
            stamp.SetOrigin(20, 20);
            stamp.Rotation = 90.0F;
            stamp.IsBackground = true;
            stamp.Pages = new[] { 1, 3 };
            // Adicionar carimbo ao arquivo PDF
            fileStamp.AddStamp(stamp);

            // Salvar arquivo PDF atualizado
            fileStamp.Save(_dataDir + "PageStampOnAllPages.pdf");

            // Fechar fileStamp
            fileStamp.Close();
        }

        // Adicionar Números de Página em PDF
        public enum PageNumPosition
        {
            PosBottomMiddle, PosBottomRight, PosUpperRight, PosSidesRight, PosUpperMiddle, PosBottomLeft, PosSidesLeft, PosUpperLeft
        }
```

## Adicionar Número de Página em um Arquivo PDF (facades)

A classe [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) permite que você adicione números de página em um arquivo PDF.
 Para adicionar números de página, você primeiro precisa criar um objeto da classe [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp). Se você quiser mostrar o número da página como "Página X de N", sendo X o número da página atual e N o número total de páginas no arquivo PDF, então você primeiro precisa obter a contagem de páginas usando a propriedade getNumberOfpages da classe [PdfFileInfo](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileInfo). Para obter o número da página atual, você pode usar o sinal **#** em seu texto onde quiser. Você pode formatar o texto do número da página usando a classe [FormattedText](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormattedText). Se você quiser começar a numeração das páginas a partir de um número específico, então você pode definir a propriedade setStartingNumber. Quando estiver pronto para adicionar o número da página no arquivo, você precisará chamar o método addPageNumber da classe [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp). Finalmente, salve o arquivo PDF de saída usando o método Save da classe [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp).

O trecho de código a seguir mostra como adicionar o número da página em um arquivo PDF.
```java
 public static void AddPageNumberInPdfFile() {
        // Criar objeto PdfFileStamp
        PdfFileStamp fileStamp = new PdfFileStamp();

        // Abrir Documento
        fileStamp.bindPdf(_dataDir + "sample.pdf");

        // Obter o número total de páginas
        int totalPages = new PdfFileInfo(_dataDir + "sample.pdf").getNumberOfPages();

        // Criar texto formatado para número de página
        FormattedText formattedText = new FormattedText("Página # de " + totalPages, java.awt.Color.WHITE,
                java.awt.Color.GRAY, FontStyle.TimesBoldItalic, EncodingType.Winansi, false, 12);

        // Definir número inicial para a primeira página; você pode querer começar do 2 ou mais
        fileStamp.setStartingNumber(1);

        // Adicionar número da página
        fileStamp.addPageNumber(formattedText, (int) PageNumPosition.PosUpperRight.ordinal());

        // Salvar arquivo PDF atualizado
        fileStamp.save(_dataDir + "AddPageNumber_out.pdf");

        // Fechar fileStamp
        fileStamp.close();
    }
```


### Estilo de Numeração Personalizado

A classe [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) oferece a funcionalidade de adicionar informações de Número de Página como objeto de carimbo dentro de um documento PDF. Antes deste lançamento, a classe só suportava 1,2,3,4 como estilo de numeração de páginas. No entanto, houve uma exigência de alguns clientes para usar um estilo de numeração personalizado ao colocar o carimbo de número de página dentro do documento PDF. Para atender a essa necessidade, a propriedade [NumberingStyle](https://reference.aspose.com/pdf/java/com.aspose.pdf/numberingstyle) foi introduzida, a qual aceita os valores da enumeração [NumberingStyle](https://reference.aspose.com/pdf/java/com.aspose.pdf/numberingstyle). Abaixo estão especificados os valores oferecidos nesta enumeração.

```java
 public static void AddCustomPageNumberInPdfFile() {
        // Criar objeto PdfFileStamp
        PdfFileStamp fileStamp = new PdfFileStamp();

        // Abrir Documento
        fileStamp.bindPdf(_dataDir + "sample.pdf");

        // Obter número total de páginas
        int totalPages = new PdfFileInfo(_dataDir + "sample.pdf").getNumberOfPages();

        // Criar texto formatado para número de página
        FormattedText formattedText = new FormattedText("Página # de " + totalPages, java.awt.Color.WHITE,
                java.awt.Color.GRAY, FontStyle.TimesBoldItalic, EncodingType.Winansi, false, 12);

        // Especificar estilo de numeração como Numerais Romanos Maiúsculos
        fileStamp.setNumberingStyle(NumberingStyle.NumeralsRomanUppercase);

        // Definir número inicial para a primeira página; você pode querer começar a partir de 2 ou mais
        fileStamp.setStartingNumber(1);

        // Adicionar número de página
        fileStamp.addPageNumber(formattedText, PageNumPosition.PosUpperRight.ordinal());

        // Salvar arquivo PDF atualizado
        fileStamp.save(_dataDir + "AddPageNumber_out.pdf");

        // Fechar fileStamp
        fileStamp.close();
    }
```