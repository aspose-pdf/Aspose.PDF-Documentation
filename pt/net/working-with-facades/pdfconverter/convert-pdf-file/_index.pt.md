---
title: Convert PDF File
type: docs
weight: 30
url: /net/convert-pdf-file/
description: Esta seção explica como converter arquivo PDF com Aspose.PDF Facades usando a classe PdfConverter.
lastmod: "2021-06-05"
draft: false
---

## Converter Páginas PDF para Diferentes Formatos de Imagem (Facades)

Para converter páginas PDF para diferentes formatos de imagem, você precisa criar um objeto [PdfConverter](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfconverter) e abrir o arquivo PDF usando o método [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3). Após isso, você precisa chamar o método [DoConvert](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfconverter/methods/doconvert) para tarefas de inicialização. Em seguida, você pode percorrer todas as páginas usando os métodos [HasNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfconverter/methods/hasnextimage) e [GetNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfconverter/getnextimage/methods/6). O método [GetNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfconverter/getnextimage/methods/6) permite que você crie uma imagem de uma página específica. Você também precisa passar o ImageFormat para este método a fim de criar uma imagem de um tipo específico, ou seja, JPEG, GIF ou PNG etc. Finalmente, chame o método [Close](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfconverter/methods/close) da classe [PdfConverter](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfconverter). O trecho de código a seguir mostra como converter páginas de PDF em imagens.

```csharp
 public static void ConvertPdfPagesToImages01()
        {
            // Create PdfConverter object
            PdfConverter converter = new PdfConverter();

            // Bind input pdf file
            converter.BindPdf(_dataDir + "Sample-Document-01.pdf");

            // Initialize the converting process
            converter.DoConvert();

            // Check if pages exist and then convert to image one by one
            while (converter.HasNextImage())
                converter.GetNextImage(_dataDir + System.DateTime.Now.Ticks.ToString() + "_out.jpg", System.Drawing.Imaging.ImageFormat.Jpeg);

            // Close the PdfConverter object
            converter.Close();
        }
```
No próximo trecho de código, mostraremos como você pode alterar alguns parâmetros. Com [CoordinateType](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfconverter/properties/coordinatetype) definimos o quadro 'CropBox'. Também podemos alterar a [Resolution](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfconverter/properties/resolution) especificando o número de pontos por polegada. O próximo é [FormPresentationMode](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfconverter/properties/formpresentationmode) - modo de apresentação de formulário. Em seguida, indicamos a [StartPage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfconverter/properties/startpage) com a qual o número da página do início da conversão é definido. Também podemos especificar a última página definindo um intervalo.

```csharp
  public static void ConvertPdfPagesToImages02()
        {
            // Criar objeto PdfConverter
            PdfConverter converter = new PdfConverter();

            // Vincular arquivo pdf de entrada
            converter.BindPdf(_dataDir + "Sample-Document-01.pdf");

            // Iniciar o processo de conversão
            converter.DoConvert();
            converter.CoordinateType = PageCoordinateType.CropBox;
            converter.Resolution = new Devices.Resolution(600);
            converter.FormPresentationMode = Devices.FormPresentationMode.Production;
            converter.StartPage = 2;
            // converter.EndPage = 3;
            // Verificar se as páginas existem e, em seguida, converter em imagem uma a uma
            while (converter.HasNextImage())
                converter.GetNextImage(_dataDir + System.DateTime.Now.Ticks.ToString() + "_out.jpg", System.Drawing.Imaging.ImageFormat.Jpeg);

            // Fechar o objeto PdfConverter
            converter.Close();
        }
```

## See also

Aspose.PDF for .NET permite converter documentos PDF para vários formatos e também converter de outros formatos para PDF. Além disso, você pode verificar a qualidade da conversão do Aspose.PDF e visualizar os resultados online com o aplicativo de conversão Aspose.PDF. Saiba mais na seção [Converting](/pdf/net/converting/) para resolver suas tarefas.