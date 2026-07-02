---
title: Extrair imagens de PDF
linktitle: Extrair imagens
type: docs
weight: 20
url: /pt/androidjava/extract-images-from-the-pdf-file/
description: Como extrair uma parte da imagem de um PDF usando Aspose.PDF for Android via Java
lastmod: "2026-07-01"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Cada página em um documento PDF contém recursos (imagens, formulários e fontes). Podemos acessar esses recursos chamando [getResources](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page#getResources--) método. Classe [Recursos](https://reference.aspose.com/pdf/java/com.aspose.pdf/Resources) contém [XImageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/XImageCollection) e podemos obter lista de imagens chamando [getImages](https://reference.aspose.com/pdf/java/com.aspose.pdf/Resources#getImages--) método.

Assim, para extrair a imagem da página, precisamos obter referência à página, em seguida aos recursos da página e, por último, à coleção de imagens.
Imagem específica que podemos extrair, por exemplo, por índice.

O índice da imagem retorna um [XImage](https://reference.aspose.com/pdf/java/com.aspose.pdf/XImage) objeto.
Este objeto fornece um [Save](https://reference.aspose.com/pdf/java/com.aspose.pdf/XImage#save-java.io.OutputStream-) método que pode ser usado para salvar a imagem extraída. O trecho de código a seguir mostra como extrair imagens de um arquivo PDF.

 ```java
 public void extractImage () {
        // Open document
        try {
            document=new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        com.aspose.pdf.Page page=document.getPages().get_Item(1);
        com.aspose.pdf.XImageCollection xImageCollection=page.getResources().getImages();
        // Extract a particular image
        com.aspose.pdf.XImage xImage=xImageCollection.get_Item(1);
        File file=new File(fileStorage, "extracted-image.jpeg");
        try {
            java.io.FileOutputStream outputImage=new java.io.FileOutputStream(file.toString());
            // Save output image
            xImage.save(outputImage, ImageType.getJpeg());
            outputImage.close();
        } catch (java.io.IOException e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.
          }
```

