---
title: Extrair Imagens do PDF
linktitle: Extrair Imagens
type: docs
weight: 20
url: pt/java/extract-images-from-the-pdf-file/
description: Como extrair uma parte da imagem do PDF usando Aspose.PDF para Java
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Cada página no documento PDF contém recursos (imagens, formulários e fontes). Podemos acessar esses recursos chamando o método [getResources](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page#getResources--). A classe [Resources](https://reference.aspose.com/pdf/java/com.aspose.pdf/Resources) contém [XImageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/XImageCollection) e podemos obter a lista de imagens chamando o método [getImages](https://reference.aspose.com/pdf/java/com.aspose.pdf/Resources#getImages--).

Assim, para extrair a imagem de uma página, precisamos obter referência à página, em seguida aos recursos da página e por último à coleção de imagens. Podemos extrair uma imagem específica, por exemplo, pelo índice.

O índice da imagem retorna um objeto [XImage](https://reference.aspose.com/pdf/java/com.aspose.pdf/XImage).
Este objeto fornece um método [Save](https://reference.aspose.com/pdf/java/com.aspose.pdf/XImage#save-java.io.OutputStream-) que pode ser usado para salvar a imagem extraída. O trecho de código a seguir mostra como extrair imagens de um arquivo PDF.

```java
public static void Extract_Images(){
       // O caminho para o diretório de documentos.
       String _dataDir = "/home/admin1/pdf-examples/Samples/";
       String filePath = _dataDir + "ExtractImages.pdf";

       // Carregar documento PDF
       com.aspose.pdf.Document pdfDocument = new com.aspose.pdf.Document(filePath);

       com.aspose.pdf.Page page = pdfDocument.getPages().get_Item(1);
       com.aspose.pdf.XImageCollection xImageCollection = page.getResources().getImages();
       // Extrair uma imagem específica
       com.aspose.pdf.XImage xImage = xImageCollection.get_Item(1);

       try {
           java.io.FileOutputStream outputImage = new java.io.FileOutputStream(_dataDir + "output.jpg");
           // Salvar imagem de saída
           xImage.save(outputImage);
           outputImage.close();
       } catch (java.io.FileNotFoundException e) {
           // TODO: tratar exceção
           e.printStackTrace();
       } catch (java.io.IOException e) {
           // TODO: tratar exceção
           e.printStackTrace();
       }
   }
```