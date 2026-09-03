---
title: Eliminar imágenes de un archivo PDF usando Java
linktitle: Eliminar imágenes
type: docs
weight: 20
url: /java/delete-images-from-pdf-file/
description: Aprenda a eliminar imágenes incrustadas de archivos PDF en Java.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Eliminar imágenes incrustadas de archivos PDF con Java
Abstract: Este artículo muestra cómo eliminar imágenes de documentos PDF usando Aspose.PDF para Java. El ejemplo elimina un recurso de imagen de la primera página por su índice en la colección de imágenes de la página y luego guarda el documento modificado.
---
Utilice la colección de recursos de imágenes de páginas cuando necesite eliminar imágenes incrustadas de una página PDF.


## 
Eliminar una imagen incrustada por índice


1. Abra el PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. Acceda a los recursos de imágenes en la [Página] de destino(https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).

1. Elimine la imagen de destino de la colección de recursos de la página por su índice.
1. Guarde el [Documento] PDF actualizado(https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

```java
public static void deleteImage(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getPages().get_Item(1).getResources().getImages().delete(1);
        document.save(outputFile.toString());
    }
}
```
