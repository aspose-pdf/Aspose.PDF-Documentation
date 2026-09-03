---
title: Eliminar imágenes de archivo PDF usando Java
linktitle: Eliminar imágenes
type: docs
weight: 20
url: /es/java/delete-images-from-pdf-file/
description: Aprenda cómo eliminar imágenes incrustadas de archivos PDF en Java.
lastmod: "2026-09-03"
TechArticle: true
AlternativeHeadline: Eliminar imágenes incrustadas de archivos PDF con Java
Abstract: Este artículo muestra cómo eliminar imágenes de documentos PDF usando Aspose.PDF for Java. El ejemplo elimina un recurso de imagen de la primera página por su índice en la colección de imágenes de la página y luego guarda el documento modificado.
---
Utilice la colección de recursos de imágenes de la página cuando necesite eliminar imágenes incrustadas de una página PDF.

## Eliminar una imagen incrustada por índice

1. Abrir el PDF de origen [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Acceder a los recursos de imagen en el objetivo [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
1. Eliminar la imagen del objetivo de la colección de recursos de la página por su índice.
1. Guarda el PDF actualizado [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

```java
public static void deleteImage(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getPages().get_Item(1).getResources().getImages().delete(1);
        document.save(outputFile.toString());
    }
}
```
