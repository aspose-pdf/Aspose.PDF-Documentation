---
title: Extraer imágenes de PDF usando Java
linktitle: Extraer imágenes de PDF
type: docs
weight: 20
url: /es/java/extract-images-from-the-pdf-file/
description: Aprenda cómo extraer imágenes incrustadas de archivos PDF con Aspose.PDF for Java.
lastmod: "2026-09-03"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Cómo extraer imágenes de PDF mediante Java
Abstract: Este artículo explica cómo extraer imágenes incrustadas de un documento PDF con Aspose.PDF for Java. Muestra cómo abrir el PDF de origen, acceder a una imagen de la colección de recursos de la página y guardar la XImage extraída en un archivo externo.
---
Extraiga imágenes de páginas PDF cuando necesite reutilizar gráficos incrustados, inspeccionar los activos del documento o exportar imágenes para el procesamiento posterior.

1. Abra el PDF de origen en un [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) instancia y abra un flujo de salida para el archivo de imagen extraído.
1. Obtenga el objetivo [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) del documento y acceda a su `Resources.Images` colección.
1. Recuperar lo requerido [XImage](https://reference.aspose.com/pdf/java/com.aspose.pdf/ximage/) objeto de esa colección de imágenes por índice.
1. Llamar `image.save(outputImage)` para escribir los bytes de la imagen extraída al flujo de destino.

```java
public static void extractImage(Path inputFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString());
         OutputStream outputImage = Files.newOutputStream(outputFile)) {
        XImage image = document.getPages().get_Item(1).getResources().getImages().get_Item(1);
        image.save(outputImage);
    }
}
```
