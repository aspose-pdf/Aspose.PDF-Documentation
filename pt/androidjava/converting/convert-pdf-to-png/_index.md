---
title: Converter PDF para PNG 
linktitle: Converter PDF para PNG 
type: docs
weight: 20
url: /pt/androidjava/convert-pdf-to-png/
lastmod: "2021-06-05"
description: Esta página descreve como converter páginas PDF para imagem PNG, converter todas as páginas e páginas únicas para imagens PNG com Aspose.PDF para Android via Java.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Use a biblioteca **Aspose.PDF para Android via Java** para converter páginas PDF em imagens <abbr title="Portable Network Graphics">PNG</abbr> de maneira acessível e conveniente.

A classe PngDevice permite converter páginas PDF em imagens PNG. Esta classe fornece um método chamado Process, que permite converter uma página específica do arquivo PDF para o formato de imagem PNG.

## Converter Páginas PDF em Imagens PNG

Para converter todas as páginas de um arquivo PDF em arquivos PNG, itere através das páginas individuais e converta cada uma para o formato PNG. O trecho de código a seguir mostra como percorrer todas as páginas de um arquivo PDF e converter cada uma em uma imagem PNG.

{{% alert color="primary" %}}

Tente online. Você pode verificar a qualidade da conversão do Aspose.PDF e visualizar os resultados online neste link [products.aspose.app/pdf/conversion/pdf-to-png](https://products.aspose.app/pdf/conversion/pdf-to-png)

{{% /alert %}}

## Converter uma única página PDF para imagem PNG

Passe o índice da página como argumento para o método Process(..). O trecho de código a seguir mostra os passos para converter a primeira página do PDF para o formato PNG.

```java
   public void convertPDFtoPNG() {
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        File file = new File(fileStorage, "PDF-to-PNG.png");
        // Criar objeto de stream para salvar a imagem de saída
        try {
            OutputStream imageStream =
                    new FileOutputStream(file.toString());

            // Criar objeto de Resolução
            Resolution resolution = new Resolution(300);

            // Criar objeto PngDevice com resolução específica
            PngDevice PngDevice = new PngDevice(resolution);

            // Converter uma página específica e salvar a imagem no stream
            PngDevice.process(document.getPages().get_Item(1), imageStream);

            // Fechar o stream
            imageStream.close();
            resultMessage.setText(file.toString());
        } catch (IOException e) {
            resultMessage.setText(e.getMessage());
        }
    }

```


## Converter todas as páginas de PDF para imagem PNG

Aspose.PDF para Android via Java mostra como converter todas as páginas de um arquivo PDF em imagens:

1. Percorra todas as páginas do arquivo.
1. Converta cada página individualmente:
    1. Crie um objeto da classe Document para carregar o documento PDF.
    1. Obtenha a página que você deseja converter.
    1. Chame o método Process para converter a página em Png.

O trecho de código a seguir mostra como converter todas as páginas de PDF em imagens PNG.

```java
 public void convertPDFtoPNG_AllPages() {
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Percorra todas as páginas do arquivo PDF
        for (int pageCount = 1; pageCount <= document.getPages().size(); pageCount++) {
            // Crie um objeto de stream para salvar a imagem de saída
            File file = new File(fileStorage, "PDF-to-PNG"+pageCount+".png");
            java.io.OutputStream imageStream;
            try {
                imageStream = new java.io.FileOutputStream(file.toString());
            } catch (FileNotFoundException e) {
                resultMessage.setText(e.getMessage());
                return;
            }

            // Crie um objeto de Resolução
            Resolution resolution = new Resolution(300);
            // Crie um objeto JpegDevice com resolução específica
            PngDevice JpegDevice = new PngDevice(resolution);

            // Converta uma página específica e salve a imagem no stream
            JpegDevice.process(document.getPages().get_Item(pageCount), imageStream);

            // Feche o stream
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


## Converter uma página específica de PDF para imagem PNG

Aspose.PDF para Android via Java mostra como converter uma página específica para o formato PNG:

```java
public void convertPDFtoPNG_ParticularPageRegion() {
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        // Obter o retângulo de uma região específica da página
        //x=0,y=0, w=200, h=125;
        Rectangle pageRect = new Rectangle(0, 0, 200, 125);
        // definir valor de CropBox conforme o retângulo da região desejada da página
        document.getPages().get_Item(1).setCropBox(pageRect);
        // salvar documento recortado em stream
        ByteArrayOutputStream outStream = new ByteArrayOutputStream();
        document.save(outStream);

        // abrir documento PDF recortado de stream e converter para imagem
        document = new Document(new ByteArrayInputStream(outStream.toByteArray()));
        // Criar objeto de Resolução
        Resolution resolution = new Resolution(300);
        // Criar dispositivo Jpeg com atributos especificados
        PngDevice PngDevice = new PngDevice(resolution);

        File file = new File(fileStorage, "PDF-to-PNG.png");
        try {
            // Converter uma página específica e salvar a imagem em stream
            PngDevice.process(document.getPages().get_Item(1), file.toString());
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
        }
    }
```