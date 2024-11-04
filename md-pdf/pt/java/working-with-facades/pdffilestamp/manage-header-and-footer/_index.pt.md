---
title: Gerenciar Cabeçalho e Rodapé
type: docs
weight: 40
url: /java/manage-header-and-footer/
description: Esta seção explica como gerenciar Cabeçalho e Rodapé com Aspose.PDF Facades usando a Classe PdfFileStamp.
lastmod: "2021-06-05"
draft: false
---

## Adicionar Cabeçalho em um Arquivo PDF

A classe [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) permite que você adicione cabeçalho em um arquivo PDF.
 In order to add header, you first need to create object of [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) class.

Para adicionar um cabeçalho, você primeiro precisa criar um objeto da classe [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp). Você pode formatar o texto do cabeçalho usando a classe [FormattedText](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormattedText). Uma vez que você esteja pronto para adicionar o cabeçalho no arquivo, você precisa chamar o método [addHeader](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#addHeader-com.aspose.pdf.facades.FormattedText-float-) da classe [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp). Você também precisa especificar pelo menos a margem superior no método [addHeader](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#addHeader-com.aspose.pdf.facades.FormattedText-float-). Finalmente, salve o arquivo PDF de saída usando o método [close](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#close--) da classe [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp). O trecho de código a seguir mostra como adicionar um cabeçalho em um arquivo PDF.

```java
 public static void AddHeader() {
        // Criar objeto PdfFileStamp
        PdfFileStamp fileStamp = new PdfFileStamp();

        // Abrir Documento
        fileStamp.bindPdf(_dataDir + "sample.pdf");

        // Criar texto formatado para o número da página
        FormattedText formattedText = new FormattedText("Aspose - Seus Especialistas em Formato de Arquivo!", java.awt.Color.YELLOW,
                java.awt.Color.BLACK, FontStyle.Courier, EncodingType.Winansi, false, 14);

        // Adicionar cabeçalho
        fileStamp.addHeader(formattedText, 20);

        // Salvar arquivo PDF atualizado
        fileStamp.save(_dataDir + "AddHeader_out.pdf");

        // Fechar fileStamp
        fileStamp.close();
    }
```

## Adicionar Rodapé em um Arquivo PDF

A classe [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) permite que você adicione um rodapé em um arquivo PDF.
 In order to add footer, you first need to create object of [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) class.

Para adicionar um rodapé, você primeiro precisa criar um objeto da classe [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp). Você pode formatar o texto do rodapé usando a classe [FormattedText](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormattedText). Quando estiver pronto para adicionar o rodapé no arquivo, você precisa chamar o método [addFooter](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#addFooter-com.aspose.pdf.facades.FormattedText-float-) da classe [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp). Você também precisa especificar pelo menos a margem inferior no método [addFooter](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#addFooter-com.aspose.pdf.facades.FormattedText-float-). Finalmente, salve o arquivo PDF de saída usando o método [close](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#close--) da classe [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp). O trecho de código a seguir mostra como adicionar rodapé em um arquivo PDF.

```java
 public static void AddFooter() {
        // Criar objeto PdfFileStamp
        PdfFileStamp fileStamp = new PdfFileStamp();

        // Abrir Documento
        fileStamp.bindPdf(_dataDir + "sample.pdf");

        // Criar texto formatado para número de página
        FormattedText formattedText = new FormattedText("Aspose - Seus Especialistas em Formato de Arquivo!", java.awt.Color.BLUE,
                java.awt.Color.GRAY, FontStyle.Courier, EncodingType.Winansi, false, 14);

        // Adicionar rodapé
        fileStamp.addFooter(formattedText, 10);

        // Salvar arquivo PDF atualizado
        fileStamp.save(_dataDir + "AddFooter_out.pdf");

        // Fechar fileStamp
        fileStamp.close();
    }
```

## Adicionar Imagem no Cabeçalho de um Arquivo PDF Existente

A classe [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) permite adicionar uma imagem no cabeçalho de um arquivo PDF.
 Para adicionar uma imagem no cabeçalho, você primeiro precisa criar um objeto da classe [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp). Depois disso, você precisa chamar o método [addHeader](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#addHeader-com.aspose.pdf.facades.FormattedText-float-) da classe [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp). Você pode passar a imagem para o método [addHeader](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#addHeader-com.aspose.pdf.facades.FormattedText-float-). Finalmente, salve o arquivo PDF de saída usando o método [close](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#close--) da classe [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp). O trecho de código a seguir mostra como adicionar uma imagem no cabeçalho do arquivo PDF.

```java
public static void AddImageHeader() {
        // Criar objeto PdfFileStamp
        PdfFileStamp fileStamp = new PdfFileStamp();

        // Abrir Documento
        fileStamp.bindPdf(_dataDir + "sample.pdf");
        FileInputStream fs;
        try {
            fs = new FileInputStream(_dataDir + "aspose-logo.png");
            // Adicionar Cabeçalho
            fileStamp.addHeader(fs, 10);

            // Salvar arquivo PDF atualizado
            fileStamp.save(_dataDir + "AddImage-Header_out.pdf");
        } catch (FileNotFoundException e) {

            e.printStackTrace();
        }

        // Fechar fileStamp
        fileStamp.close();
    }
```

## Adicionar Imagem no Rodapé de um Arquivo PDF Existente

A classe [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) permite que você adicione uma imagem no rodapé de um arquivo PDF.
 In order to add image in footer, you first need to create object of [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) class. After that, you need to call [addFooter](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#addFooter-com.aspose.pdf.facades.FormattedText-float-) method of [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) class. You can pass the image to the [addFooter](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#addFooter-com.aspose.pdf.facades.FormattedText-float-) method. Finally, save the output PDF file using [close](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#close--) method of [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) class. The following code snippet shows you how to add image in the footer of PDF file.

```java
    public static void AddImageFooter() {
        // Criar objeto PdfFileStamp
        PdfFileStamp fileStamp = new PdfFileStamp();

        // Abrir Documento
        fileStamp.bindPdf(_dataDir + "sample.pdf");
        FileInputStream fs;
        try {
            fs = new FileInputStream(_dataDir + "aspose-logo.png");
            // Adicionar rodapé
            fileStamp.addFooter(fs, 10);

            // Salvar arquivo PDF atualizado
            fileStamp.save(_dataDir + "AddImage-Footer_out.pdf");
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }

        // Fechar fileStamp
        fileStamp.close();
    }
```