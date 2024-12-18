---
title: Adicionar Carimbo de Texto e Imagem
type: docs
weight: 20
url: /pt/java/add-text-and-image-stamp/
description: Esta seção explica como adicionar Carimbo de Texto e Imagem com com.aspose.pdf.facades usando a Classe PdfFileStamp.
lastmod: "2021-06-05"
draft: false
---

## Adicionar Carimbo de Texto em Todas as Páginas de um Arquivo PDF

A classe [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) permite que você adicione carimbo de texto em todas as páginas de um arquivo PDF.
 Para adicionar uma marca de texto, você primeiro precisa criar objetos das classes [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) e [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp). Você também precisa criar o carimbo de texto usando o método BindLogo da classe [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp). Você pode definir outros atributos como origem, rotação, fundo etc. usando o objeto [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp) também. Em seguida, você pode adicionar o carimbo no arquivo PDF usando o método [addStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#addStamp-com.aspose.pdf.facades.Stamp-) da classe [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp). Finalmente, salve o arquivo PDF de saída usando o método [close](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#close--) da classe [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp). O seguinte trecho de código mostra como adicionar um carimbo de texto em todas as páginas de um arquivo PDF.

```java
 public static void AddTextStampOnAllPagesInPdfFile() {
        // Criar objeto PdfFileStamp
        PdfFileStamp fileStamp = new PdfFileStamp();

        // Abrir Documento
        fileStamp.bindPdf(_dataDir + "sample.pdf");

        // Criar carimbo
        Stamp stamp = new Stamp();
        stamp.bindLogo(new FormattedText("Hello World!", java.awt.Color.BLUE, java.awt.Color.GRAY, FontStyle.Helvetica,
                EncodingType.Winansi, true, 14));
        stamp.setOrigin(10, 400);
        stamp.setRotation(90.0F);
        stamp.setBackground(true);

        // Adicionar carimbo ao arquivo PDF
        fileStamp.addStamp(stamp);

        // Salvar arquivo PDF atualizado
        fileStamp.save(_dataDir + "AddTextStamp-All_out.pdf");

        // Fechar fileStamp
        fileStamp.close();
    }
```

## Adicionar Carimbo de Texto em Páginas Específicas em um Arquivo PDF

A classe [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) permite que você adicione um carimbo de texto em páginas específicas de um arquivo PDF.
 Em ordem para adicionar uma marca de texto, você primeiro precisa criar objetos das classes [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) e [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp). Você também precisa criar a marca de texto usando o método [bindPdf](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp#bindPdf-java.lang.String-int-) da classe [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp). Você pode definir outros atributos como origem, rotação, fundo etc. usando o objeto [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp) também. Como você deseja adicionar uma marca de texto em páginas específicas do arquivo PDF, você também precisa definir a propriedade [Pages](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp#setPages-int:A-) da classe [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp). Esta propriedade requer um array de inteiros contendo os números das páginas nas quais você deseja adicionar a marca. Em seguida, você pode adicionar a marca no arquivo PDF usando o método [addStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#addStamp-com.aspose.pdf.facades.Stamp-) da classe [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp). Finalmente, salve o arquivo PDF de saída usando o método [close](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#close--) da classe [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp). O trecho de código a seguir mostra como adicionar uma marca de texto em páginas específicas em um arquivo PDF.

```java
 public static void AddTextStampOnParticularPagesInPdfFile() {
        // Criar objeto PdfFileStamp
        PdfFileStamp fileStamp = new PdfFileStamp();

        // Abrir Documento
        fileStamp.bindPdf(_dataDir + "sample.pdf");

        // Criar marca
        Stamp stamp = new Stamp();
        stamp.bindLogo(new FormattedText("Hello World!", java.awt.Color.BLUE, java.awt.Color.GRAY, FontStyle.Helvetica,
                EncodingType.Winansi, true, 14));
        stamp.setOrigin(10, 400);
        stamp.setRotation(90.0F);
        stamp.setBackground(true);

        // Definir páginas específicas
        stamp.setPages(new int[] { 2 });

        // Adicionar marca ao arquivo PDF
        fileStamp.addStamp(stamp);

        // Salvar arquivo PDF atualizado
        fileStamp.save(_dataDir + "AddTextStamp-Page_out.pdf");

        // Fechar fileStamp
        fileStamp.close();
    }
```

## Adicionar Carimbo de Imagem em Todas as Páginas de um Arquivo PDF

A classe [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) permite que você adicione um carimbo de imagem em todas as páginas de um arquivo PDF.
 Para adicionar um carimbo de imagem, você primeiro precisa criar objetos das classes [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) e [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp). Você também precisa criar o carimbo de imagem usando o método [bindPdf](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp#bindPdf-java.lang.String-int-) da classe [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp). Você pode definir outros atributos como origem, rotação, fundo etc. usando também o objeto [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp). Em seguida, você pode adicionar o carimbo no arquivo PDF usando o método [addStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#addStamp-com.aspose.pdf.facades.Stamp-) da classe [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp). Finalmente, salve o arquivo PDF de saída usando o método [close](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#close--) da classe [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp). O trecho de código a seguir mostra como adicionar um carimbo de imagem em todas as páginas de um arquivo PDF.

```java
public static void AddImageStampOnParticularPagesInPdfFile() {
        // Criar objeto PdfFileStamp
        PdfFileStamp fileStamp = new PdfFileStamp();

        // Abrir Documento
        fileStamp.bindPdf(_dataDir + "sample.pdf");

        // Criar carimbo
        Stamp stamp = new Stamp();
        stamp.bindImage(_dataDir + "aspose-logo.png");
        stamp.setOrigin(10, 200);
        stamp.setRotation(90.0F);
        stamp.setBackground(true);

        // Adicionar carimbo ao arquivo PDF
        fileStamp.addStamp(stamp);

        // Salvar arquivo PDF atualizado
        fileStamp.save(_dataDir + "AddImageStamp-All_out.pdf");

        // Fechar fileStamp
        fileStamp.close();
    }
```

### Controlar a qualidade da imagem ao adicionar como carimbo

Ao adicionar uma imagem como objeto carimbo, você também pode controlar a qualidade da imagem. Para cumprir este requisito, a propriedade Quality foi adicionada à classe [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp). Ela indica a qualidade da imagem em porcentagem (valores válidos são 0..100).

## Adicionar Carimbo de Imagem em Páginas Específicas em um Arquivo PDF

A classe [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) permite que você adicione um carimbo de imagem em páginas específicas de um arquivo PDF.
 Em ordem para adicionar um carimbo de imagem, você primeiro precisa criar objetos das classes [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) e [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp). Você também precisa criar o carimbo de imagem usando o método [bindPdf](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp#bindPdf-java.lang.String-int-) da classe [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp). Você pode definir outros atributos como origem, rotação, fundo, etc. using [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp) objeto também. Como você deseja adicionar um carimbo de imagem em páginas específicas do arquivo PDF, você também precisa definir a propriedade [Pages](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp#setPages-int:A-) da classe [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp). Esta propriedade requer um array de inteiros contendo os números das páginas nas quais você deseja adicionar o carimbo. Em seguida, você pode adicionar o carimbo no arquivo PDF usando o método [addStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#addStamp-com.aspose.pdf.facades.Stamp-) da classe [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp). Finalmente, salve o arquivo PDF de saída usando o método [close](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#close--) da classe [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp). O trecho de código a seguir mostra como adicionar um carimbo de imagem em páginas específicas em um arquivo PDF.

```java
  public static void AddImageStampOnAllPagesInPdfFile() {
        // Criar objeto PdfFileStamp
        PdfFileStamp fileStamp = new PdfFileStamp();

        // Abrir Documento
        fileStamp.bindPdf(_dataDir + "sample.pdf");

        // Criar carimbo
        Stamp stamp = new Stamp();
        stamp.bindImage(_dataDir + "aspose-logo.png");
        stamp.setOrigin(10, 200);
        stamp.setRotation(90.0F);
        stamp.setBackground(true);

        // Definir páginas específicas
        stamp.setPages(new int[] { 2 });

        // Adicionar carimbo ao arquivo PDF
        fileStamp.addStamp(stamp);

        // Salvar arquivo PDF atualizado
        fileStamp.save(_dataDir + "AddImageStamp-Page_out.pdf");

        // Fechar fileStamp
        fileStamp.close();
    }
```