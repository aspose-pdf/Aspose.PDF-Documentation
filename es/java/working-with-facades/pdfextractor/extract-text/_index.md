---
title: Extraer Imágenes de PDF (fachadas)
type: docs
weight: 30
url: /es/java/extract-images/
description: Esta sección explica cómo extraer imágenes con Aspose.PDF Facades usando la clase PdfExtractor.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

La clase [PdfExtractor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfExtractor) te permite extraer imágenes de un archivo PDF.
 Primeramente, necesitas crear un objeto de la clase [PdfExtractor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfExtractor) y vincular el archivo PDF de entrada usando el método bindPdf. Después de eso, llama al método [extractImage](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfExtractor#extractImage--) para extraer todas las imágenes en la memoria. Una vez que las imágenes son extraídas, puedes obtener esas imágenes con la ayuda de los métodos hasNextImage y getNextImage. Necesitas recorrer todas las imágenes extraídas usando un bucle while. Para guardar las imágenes en el disco, puedes llamar a la sobrecarga del método getNextImage que toma la ruta del archivo como argumento. El siguiente fragmento de código te muestra cómo extraer imágenes de todo el PDF a archivos.

```java   
public static void ExtractImages()
 {
    //Crear un extractor y vincularlo al documento
    Document document = new Document(_dataDir + "sample.pdf");
    PdfExtractor extractor = new PdfExtractor(document);
    extractor.setStartPage(1);
    extractor.setEndPage(3);            

    //Ejecutar el extractor
    extractor.extractImage();
    int imageNumber = 1;
    //Iterar a través de la colección de imágenes extraídas
    while (extractor.hasNextImage())
    {
        //Recuperar imagen de la colección y guardarla en un archivo
        extractor.getNextImage(_dataDir + String.format("image%03d.png", imageNumber++), ImageType.getPng());
    }
}
```