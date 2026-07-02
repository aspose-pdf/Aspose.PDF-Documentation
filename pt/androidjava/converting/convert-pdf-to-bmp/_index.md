---
title: Converter PDF para BMP
linktitle: Converter PDF para BMP
type: docs
weight: 40
url: /pt/androidjava/convert-pdf-to-bmp/
lastmod: "2026-07-01"
description: Este artigo descreve como converter páginas de PDF para imagem BMP, converter todas as páginas para imagens BMP e converter uma única página de PDF para imagem BMP com Java.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

O [BmpDevice](https://reference.aspose.com/pdf/net/aspose.pdf.devices/bmpdevice) classe permite converter páginas PDF em <abbr title="Bitmap Image File">BMP</abbr> imagens. Esta classe fornece um método chamado [Process](https://reference.aspose.com/pdf/net/aspose.pdf.devices/bmpdevice/methods/process) que permite converter uma página específica do arquivo PDF para o formato de imagem Bmp.

{{% alert color="primary" %}}

Experimente online. Você pode verificar a qualidade da conversão Aspose.PDF e visualizar os resultados online neste link [products.aspose.app/pdf/conversion/pdf-to-bmp](https://products.aspose.app/pdf/conversion/pdf-to-bmp)

{{% /alert %}}

A classe BmpDevice permite converter páginas PDF em imagens BMP. Esta classe fornece um método chamado process(..) que permite converter uma página específica do arquivo PDF em imagem BMP.

## Converter uma página PDF para imagem BMP

Para converter uma página PDF para uma imagem BMP:

1. Crie um objeto da classe Document, para obter a página específica que você deseja converter.
1. Chame o método process(..) para converter a página para BMP.

O trecho de código a seguir mostra como converter uma página específica em imagem BMP.

```java
//Convert PDF to BMP
    public void convertPDFtoBMP() {
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        File file = new File(fileStorage, "PDF-to-BMP.bmp");
        // Create stream object to save the output image
        try {
            OutputStream imageStream =
                    new FileOutputStream(file.toString());

            // Create Resolution object
            Resolution resolution = new Resolution(300);

            // Create BmpDevice object with particular resolution
            BmpDevice BmpDevice = new BmpDevice(resolution);

            // Convert a particular page and save the image to stream
            BmpDevice.process(document.getPages().get_Item(1), imageStream);

            // Close the stream
            imageStream.close();
            resultMessage.setText(file.toString());
        } catch (IOException e) {
            resultMessage.setText(e.getMessage());
        }
    }
```

## Converter Todas as Páginas PDF em Imagens BMP

Para converter todas as páginas de um arquivo PDF para o formato BMP, você precisa iterar para obter cada página individual e convertê‑la para BMP. O trecho de código a seguir mostra como percorrer todas as páginas de um arquivo PDF e convertê‑las para BMP.

```java
public void convertPDFtoBMP_AllPages() {
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Loop through all the pages of PDF file
        for (int pageCount = 1; pageCount <= document.getPages().size(); pageCount++) {
            // Create stream object to save the output image
            File file = new File(fileStorage, "PDF-to-BMP"+pageCount+".BMP");
            java.io.OutputStream imageStream;
            try {
                imageStream = new java.io.FileOutputStream(file.toString());
            } catch (FileNotFoundException e) {
                resultMessage.setText(e.getMessage());
                return;
            }

            // Create Resolution object
            Resolution resolution = new Resolution(300);
            // Create BmpDevice object with particular resolution
            BmpDevice BmpDevice = new BmpDevice(resolution);

            // Convert a particular page and save the image to stream
            BmpDevice.process(document.getPages().get_Item(pageCount), imageStream);

            // Close the stream
            try {
                imageStream.close();
            } catch (Exception e) {
                resultMessage.setText(e.getMessage());
                return;
            }
        }
        resultMessage.setText(R.string.success_message);
    }
```

## Converter uma região de página específica para Imagem (DOM)

Podemos converter documentos PDF para diferentes formatos de imagem usando objetos de dispositivos de imagem do Aspose.PDF. No entanto, às vezes há a necessidade de converter uma região específica da página em formato de imagem. Podemos atender a essa necessidade em duas etapas. Inicialmente, recorte a página PDF para a região desejada e, posteriormente, converta-a em imagem usando o objeto de dispositivo de imagem desejado.

O seguinte trecho de código mostra como converter páginas PDF em imagens.

```java
public void convertPDFtoBmp_ParticularPageRegion() {
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        // Get rectangle of particular page region
        //x=0,y=0, w=200, h=125;
        Rectangle pageRect = new Rectangle(0, 0, 200, 125);
        // set CropBox value as per rectangle of desired page region
        document.getPages().get_Item(1).setCropBox(pageRect);
        // save cropped document into stream
        ByteArrayOutputStream outStream = new ByteArrayOutputStream();
        document.save(outStream);

        // open cropped PDF document from stream and convert to image
        document = new Document(new ByteArrayInputStream(outStream.toByteArray()));
        // Create Resolution object
        Resolution resolution = new Resolution(300);
        // Create BMP device with specified attributes
        BmpDevice BmpDevice = new BmpDevice(resolution);

        File file = new File(fileStorage, "PDF-to-BMP.BMP");
        try {
            // Convert a particular page and save the image to stream
            BmpDevice.process(document.getPages().get_Item(1), file.toString());
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
        }
        resultMessage.setText(R.string.success_message);
    }
```
