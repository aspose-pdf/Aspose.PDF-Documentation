---
title: Converter PDF para BMP 
linktitle: Converter PDF para BMP
type: docs
weight: 40
url: /pt/androidjava/convert-pdf-to-bmp/
lastmod: "2021-06-05"
description: Este artigo descreve como converter Páginas PDF para imagem BMP, converter todas as Páginas para imagens BMP e converter uma única página PDF para imagem BMP com Java.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

A classe [BmpDevice](https://reference.aspose.com/pdf/pt/net/aspose.pdf.devices/bmpdevice) permite converter páginas PDF em imagens <abbr title="Arquivo de Imagem Bitmap">BMP</abbr>. Esta classe fornece um método chamado [Process](https://reference.aspose.com/pdf/pt/net/aspose.pdf.devices/bmpdevice/methods/process) que permite converter uma página específica do arquivo PDF para o formato de imagem Bmp.

{{% alert color="primary" %}}

Experimente online. Você pode verificar a qualidade da conversão do Aspose.PDF e visualizar os resultados online neste link [products.aspose.app/pdf/conversion/pdf-to-bmp](https://products.aspose.app/pdf/conversion/pdf-to-bmp)

{{% /alert %}}

A classe BmpDevice permite converter páginas PDF em imagens BMP.
 Esta classe fornece um método chamado process(..) que permite converter uma página específica de um arquivo PDF para imagem BMP.

## Converter uma Página de PDF para Imagem BMP

Para converter uma página de PDF para uma imagem BMP:

1. Crie um objeto da classe Document, para obter a página específica que você deseja converter.
2. Chame o método process(..) para converter a página em BMP.

O seguinte trecho de código mostra como converter uma página específica para imagem BMP.

```java
//Converter PDF para BMP
    public void convertPDFtoBMP() {
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        File file = new File(fileStorage, "PDF-to-BMP.bmp");
        // Criar objeto de stream para salvar a imagem de saída
        try {
            OutputStream imageStream =
                    new FileOutputStream(file.toString());

            // Criar objeto Resolution
            Resolution resolution = new Resolution(300);

            // Criar objeto BmpDevice com resolução específica
            BmpDevice BmpDevice = new BmpDevice(resolution);

            // Converter uma página específica e salvar a imagem no stream
            BmpDevice.process(document.getPages().get_Item(1), imageStream);

            // Fechar o stream
            imageStream.close();
            resultMessage.setText(file.toString());
        } catch (IOException e) {
            resultMessage.setText(e.getMessage());
        }
    }
```

## Converter Todas as Páginas do PDF para Imagens BMP

Para converter todas as páginas de um arquivo PDF para o formato BMP, você precisa iterar para obter cada página individual e convertê-la para o formato BMP. O trecho de código a seguir mostra como percorrer todas as páginas de um arquivo PDF e convertê-las para BMP.

```java
public void convertPDFtoBMP_AllPages() {
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Percorrer todas as páginas do arquivo PDF
        for (int pageCount = 1; pageCount <= document.getPages().size(); pageCount++) {
            // Criar objeto de stream para salvar a imagem de saída
            File file = new File(fileStorage, "PDF-to-BMP"+pageCount+".BMP");
            java.io.OutputStream imageStream;
            try {
                imageStream = new java.io.FileOutputStream(file.toString());
            } catch (FileNotFoundException e) {
                resultMessage.setText(e.getMessage());
                return;
            }

            // Criar objeto Resolution
            Resolution resolution = new Resolution(300);
            // Criar objeto BmpDevice com resolução específica
            BmpDevice BmpDevice = new BmpDevice(resolution);

            // Converter uma página específica e salvar a imagem no stream
            BmpDevice.process(document.getPages().get_Item(pageCount), imageStream);

            // Fechar o stream
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


## Converter uma região específica da página para Imagem (DOM)

Podemos converter documentos PDF para diferentes formatos de imagem usando objetos de dispositivos de imagem do Aspose.PDF. No entanto, às vezes há a necessidade de converter uma região específica da página em formato de imagem. Podemos atender a essa necessidade em duas etapas. Inicialmente, recorte a página do PDF para a região desejada e, posteriormente, converta-a em imagem usando o objeto de dispositivo de imagem desejado.

O trecho de código a seguir mostra como converter páginas PDF em imagens.

```java
public void convertPDFtoBmp_ParticularPageRegion() {
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        // Obter retângulo de uma região específica da página
        //x=0,y=0, w=200, h=125;
        Rectangle pageRect = new Rectangle(0, 0, 200, 125);
        // definir valor de CropBox conforme o retângulo da região desejada da página
        document.getPages().get_Item(1).setCropBox(pageRect);
        // salvar documento recortado no stream
        ByteArrayOutputStream outStream = new ByteArrayOutputStream();
        document.save(outStream);

        // abrir documento PDF recortado do stream e converter para imagem
        document = new Document(new ByteArrayInputStream(outStream.toByteArray()));
        // Criar objeto Resolution
        Resolution resolution = new Resolution(300);
        // Criar dispositivo BMP com atributos especificados
        BmpDevice BmpDevice = new BmpDevice(resolution);

        File file = new File(fileStorage, "PDF-to-BMP.BMP");
        try {
            // Converter uma página específica e salvar a imagem no stream
            BmpDevice.process(document.getPages().get_Item(1), file.toString());
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
        }
        resultMessage.setText(R.string.success_message);
    }
```