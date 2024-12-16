---
title: PdfFileMend Class
type: docs
weight: 20
url: /pt/java/pdffilemend-class/
description: Esta seção explica como trabalhar com Aspose.PDF Facades usando a classe PdfFileMend.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Parece não ser uma tarefa difícil inserir [FormattedText](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormattedText) em um documento PDF, desde que você tenha a versão original editável deste documento. Suponha que você criou um documento e depois lembrou que precisa adicionar outra linha ou estamos falando de um volume maior de documentos, em ambos os casos, o Aspose.PDF Facades irá ajudá-lo. Vamos considerar a possibilidade de adicionar texto em um arquivo PDF existente com a classe [PdfFileMend](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileMend).

## Adicionar Texto em um Arquivo PDF Existente (facades)

Podemos adicionar texto de várias maneiras.
 Considere o primeiro. Pegamos o [FormattedText](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormattedText) e o adicionamos à Página. Depois, indicamos as coordenadas do canto inferior esquerdo e, em seguida, adicionamos nosso texto à Página.

```java
    public static void AddText01()
    {
        PdfFileMend mender = new PdfFileMend();
        mender.BindPdf(_dataDir + "sample.pdf");
        FormattedText message = new FormattedText("Bem-vindo ao Aspose!");

        mender.AddText(message, 1, 10, 750);

        // salvar o arquivo de saída
        mender.Save(_dataDir + "PdfFileMend01_output.pdf");
    }
```

Veja como fica:

![Add Text](/pdf/pt/net/images/add_text.png)

A segunda maneira de adicionar [FormattedText](https://reference.aspose.com/pdf//java/com.aspose.pdf.facades/formattedtext). Além disso, indicamos um retângulo no qual nosso texto deve caber.

```java
public static void AddText02()
    {
        PdfFileMend mender = new PdfFileMend();
        mender.BindPdf(_dataDir + "sample.pdf");
        FormattedText message = new FormattedText("Bem-vindo ao Aspose! Bem-vindo ao Aspose!");

        mender.AddText(message, 1, 10, 700, 55, 810);
        mender.WrapMode = WordWrapMode.ByWords;

        // salvar o arquivo de saída
        mender.Save(_dataDir + "PdfFileMend02_output.pdf");
    }
```

O terceiro exemplo fornece a capacidade de Adicionar Texto a páginas especificadas. Em nosso exemplo, vamos adicionar uma legenda nas páginas 1 e 3 do documento.

```java
public static void AddText03()
    {
        Document document = new Document(_dataDir + "sample.pdf");
        document.Pages.Add();
        document.Pages.Add();
        document.Pages.Add();
        PdfFileMend mender = new PdfFileMend();
        mender.BindPdf(document);
        FormattedText message = new FormattedText("Bem-vindo ao Aspose!");
        int[] pageNums = new int[] { 1, 3 };
        mender.AddText(message, pageNums, 10, 750, 310, 760);

        // salvar o arquivo de saída
        mender.Save(_dataDir + "PdfFileMend03_output.pdf");
    }
```

## Adicionar Imagem em um Arquivo PDF Existente (facades)

Você já tentou adicionar uma imagem a um arquivo PDF existente?
 Nós temos certeza de que você sabe que esta não é uma tarefa fácil. Talvez você esteja preenchendo um formulário online e precise anexar uma foto para identificação ou anexar sua foto a um currículo existente. Anteriormente, tal tarefa era resolvida criando uma foto, anexando-a a um documento, escaneando e enviando. Este processo envolvia muito trabalho e consumia tempo.

Adicionar imagens e texto em um arquivo PDF existente é uma necessidade comum e o namespace com.aspose.pdf.facades atende muito bem essa necessidade. Ele fornece uma classe [PdfFileMend](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileMend) que permite adicionar imagens no arquivo PDF.

Este artigo mostrará como inserir uma imagem em um PDF usando com.aspose.pdf.facades. Existem também várias opções para adicionar imagens ao PDF.

Insira a imagem no documento PDF definindo os parâmetros do retângulo.

```java
public static void AddImage01()
    {
        Document document = new Document(_dataDir + "sample.pdf");
        PdfFileMend mender = new PdfFileMend();

        // Carregar imagem no fluxo
        var imageStream = System.IO.File.OpenRead(_dataDir + "logo.png");
        mender.BindPdf(document);
        mender.AddImage(imageStream, 1, 10, 650, 110, 750);

        // salvar o arquivo de saída
        mender.Save(_dataDir + "PdfFileMend04_output.pdf");
    }
```

![Adicionar Imagem](/pdf/pt/net/images/add_image1.png)

Vamos considerar o segundo trecho de código. Usando variações dos parâmetros da classe [CompositingParameters](https://reference.aspose.com/pdf/java/com.aspose.pdf/CompositingParameters), podemos obter diferentes efeitos de design.
Nós tentamos um deles.

```java
 public static void AddImage02()
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
        CompositingParameters compositingParameters = new CompositingParameters(BlendMode.Multiply);
        mender.AddImage(imageStream, pageNum, lowerLeftX, lowerLeftY, upperRightX, upperRightY, compositingParameters);

        // salvar o arquivo de saída
        mender.Save(_dataDir + "PdfFileMend05_output.pdf");
    }
```


![Add Image](/pdf/pt/net/images/add_image2.png)

No trecho de código a seguir, usamos [ImageFilterType](https://reference.aspose.com/pdf/java/com.aspose.pdf/ImageFilterType). ImageFilterType indica o tipo de codec de fluxo que será usado para codificação, por padrão Jpeg. Se você carregar uma imagem do formato PNG, ela será salva no documento como JPEG (ou em outro formato que eu especifiquei).

```java
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


No próximo trecho de código, você pode notar o uso do método [IsMasked](https://reference.aspose.com/pdf/java/com.aspose.pdf/CompositingParameters#isMasked--).

[IsMasked](https://reference.aspose.com/pdf/java/com.aspose.pdf/CompositingParameters#isMasked--) é uma bandeira, que indica se deve aplicar uma máscara à imagem para alcançar transparência da imagem original.

```java
public static void AddImage04()
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
    CompositingParameters compositingParameters = new CompositingParameters(BlendMode.Multiply, ImageFilterType.Flate,false);
    mender.AddImage(imageStream, pageNum, lowerLeftX, lowerLeftY, upperRightX, upperRightY, compositingParameters);

    // salvar o arquivo de saída
    mender.Save(_dataDir + "PdfFileMend07_output.pdf");
}
```