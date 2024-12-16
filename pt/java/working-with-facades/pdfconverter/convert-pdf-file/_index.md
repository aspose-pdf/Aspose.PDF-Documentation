---
title: Converter Arquivo PDF
type: docs
weight: 20
url: /pt/java/convert-pdf-file/
description: Esta seção explica como converter Arquivo PDF com Aspose.PDF Facades usando a classe PdfConverter.
lastmod: "2021-06-05"
draft: false
---

## Converter Páginas de PDF para Diferentes Formatos de Imagem (Facades)

Para converter páginas de PDF para diferentes formatos de imagem, você precisa criar um objeto [PdfConverter](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfConverter) e abrir o arquivo PDF usando o método [bindPdf](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfConverter#bindPdf-java.lang.String-).

Depois disso, você precisa chamar o método [doConvert](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfConverter#doConvert--) para tarefas de inicialização.
 Então, você pode percorrer todas as páginas usando os métodos [hasNextImage](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfConverter#hasNextImage--) e [getNextImage](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfConverter#getNextImage-java.io.OutputStream-). O método getNextImage permite que você crie uma imagem de uma página específica. Você também precisa passar o ImageType para este método a fim de criar uma imagem de um tipo específico, ou seja, JPEG, GIF ou PNG, etc.

Finalmente, chame o método close da classe [PdfConverter](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfConverter).

O trecho de código a seguir mostra como converter páginas de PDF em imagens.

```java
public static void ConvertPdfPagesToImages01() {
        // Criar objeto PdfConverter
        PdfConverter converter = new PdfConverter();

        // Vincular arquivo PDF de entrada
        converter.bindPdf(_dataDir + "Sample-Document-01.pdf");

        // Inicializar o processo de conversão
        converter.doConvert();
        
        int count=0;

        // Verificar se existem páginas e então converter para imagem uma por uma
        while (converter.hasNextImage())
            converter.getNextImage(_dataDir + "page" + count + "_out.jpg", ImageType.getJpeg());
        // Fechar o objeto PdfConverter
        converter.close();
    }
```

No próximo trecho de código, mostraremos como você pode alterar alguns parâmetros. Com [setCoordinateType](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfConverter#setCoordinateType-int-) definimos o quadro [CropBox](https://reference.aspose.com/pdf/java/com.aspose.pdf/PageCoordinateType#CropBox). Além disso, podemos alterar [setResolution](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfConverter#setResolution-com.aspose.pdf.devices.Resolution-) especificando o número de pontos por polegada. O próximo [setFormPresentationMode](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfConverter#setFormPresentationMode-int-) - modo de apresentação de formulário. Em seguida, indicamos o [setStartPage](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfConverter#setStartPage-int-) com o qual o número da página do início da conversão é definido. Também podemos especificar a última página definindo um intervalo.

```java
public static void ConvertPdfPagesToImages02()
    {
        // Criar objeto PdfConverter
        PdfConverter converter = new PdfConverter();

        // Vincular arquivo pdf de entrada
        converter.bindPdf(_dataDir + "sample.pdf");

        // Inicializar o processo de conversão
        converter.doConvert();
        converter.setCoordinateType(PageCoordinateType.CropBox);
        converter.setResolution (new Resolution(600));
        converter.setFormPresentationMode(FormPresentationMode.Editor);
        converter.setStartPage(2);
        int count=0;
        // Verifique se as páginas existem e, em seguida, converta para imagem uma por uma
        while (converter.hasNextImage())
            converter.getNextImage(_dataDir + "page" + count + "_out.jpg", ImageType.getJpeg());
        // Fechar o objeto PdfConverter
        converter.close();
    }
```