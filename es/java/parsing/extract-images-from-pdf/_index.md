---
title: Extraer imágenes de PDF usando Java
linktitle: Extraer imágenes de PDF
type: docs
weight: 20
url: /java/extract-images-from-the-pdf-file/
description: Aprenda a extraer imágenes incrustadas de archivos PDF con Aspose.PDF para Java.
lastmod: "2026-06-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Cómo extraer imágenes de PDF a través de Java
Abstract: Este artículo explica cómo extraer imágenes incrustadas de un documento PDF con Aspose.PDF para Java. Muestra cómo abrir el PDF de origen, acceder a una imagen de la colección de recursos de la página y guardar el XImage extraído en un archivo externo.
---
Extraiga imágenes de páginas PDF cuando necesite reutilizar gráficos incrustados, inspeccionar activos de documentos o exportar imágenes para su procesamiento posterior.


1. Abra el PDF de origen en una instancia de [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) y abra una secuencia de salida para el archivo de imagen extraído.

1. Obtenga la [Página](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) de destino del documento y acceda a su colección `Resources.Images`.

1. Recupere el objeto [XImage](https://reference.aspose.com/pdf/java/com.aspose.pdf/ximage/) requerido de esa colección de imágenes por índice.

1. Llame a `image.save(outputImage)` para escribir los bytes de la imagen extraída en la secuencia de destino.

```java
public static void extractImage(Path inputFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString());
         OutputStream outputImage = Files.newOutputStream(outputFile)) {
        XImage image = document.getPages().get_Item(1).getResources().getImages().get_Item(1);
        image.save(outputImage);
    }
}
```
