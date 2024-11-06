---
title: Extrair Imagens do PDF 
linktitle: Extrair Imagens
type: docs
weight: 20
url: pt/androidjava/extract-images-from-the-pdf-file/
description: Como extrair uma parte da imagem do PDF usando Aspose.PDF para Android via Java
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Cada página em um documento PDF contém recursos (imagens, formulários e fontes). Podemos acessar esses recursos chamando o método [getResources](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page#getResources--). A classe [Resources](https://reference.aspose.com/pdf/java/com.aspose.pdf/Resources) contém [XImageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/XImageCollection) e podemos obter a lista de imagens chamando o método [getImages](https://reference.aspose.com/pdf/java/com.aspose.pdf/Resources#getImages--).

Assim, para extrair uma imagem de uma página, precisamos obter a referência para a página, em seguida para os recursos da página e por último para a coleção de imagens.

Podemos extrair uma imagem específica, por exemplo, pelo índice.

O índice da imagem retorna um objeto [XImage](https://reference.aspose.com/pdf/java/com.aspose.pdf/XImage). Este objeto fornece um método [Save](https://reference.aspose.com/pdf/java/com.aspose.pdf/XImage#save-java.io.OutputStream-) que pode ser usado para salvar a imagem extraída. O trecho de código a seguir mostra como extrair imagens de um arquivo PDF.

```java
public void extractImage () {
       // Abrir documento
       try {
           document=new Document(inputStream);
       } catch (Exception e) {
           resultMessage.setText(e.getMessage());
           return;
       }

       com.aspose.pdf.Page page=document.getPages().get_Item(1);
       com.aspose.pdf.XImageCollection xImageCollection=page.getResources().getImages();
       // Extrair uma imagem específica
       com.aspose.pdf.XImage xImage=xImageCollection.get_Item(1);
       File file=new File(fileStorage, "extracted-image.jpeg");
       try {
           java.io.FileOutputStream outputImage=new java.io.FileOutputStream(file.toString());
           // Salvar imagem de saída
           xImage.save(outputImage, ImageType.getJpeg());
           outputImage.close();
       } catch (java.io.IOException e) {
           resultMessage.setText(e.getMessage());
           return;
       }
       resultMessage.
         }
```