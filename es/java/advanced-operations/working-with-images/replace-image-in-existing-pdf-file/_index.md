---
title: Reemplazar imagen en un archivo PDF existente usando Java
linktitle: Reemplazar imagen
type: docs
weight: 70
url: /java/replace-image-in-existing-pdf-file/
description: Aprenda cómo reemplazar imágenes incrustadas en archivos PDF existentes en Java.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Reemplazar imágenes en archivos PDF existentes con Java
Abstract: Este artículo muestra cómo reemplazar imágenes en documentos PDF usando Aspose.PDF para Java. Cubre el reemplazo de una imagen por su índice de recursos y el reemplazo de la primera ubicación de imagen coincidente encontrada con ImagePlacementAbsorber.
---
Utilice la colección de imágenes de la página o la búsqueda basada en ubicación, dependiendo de la precisión con la que necesite orientar la imagen.


## 
Reemplazar una imagen por índice de recursos


1. Abra el PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. Acceda a los recursos de imágenes en la [Página] de destino(https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).

1. Reemplace el recurso de imagen de destino con el nuevo archivo de imagen.
1. Guarde el [Documento] PDF actualizado(https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).


```java
public static void replaceImage(Path inputFile, Path imageFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString());
         InputStream imageStream = Files.newInputStream(imageFile)) {
        document.getPages().get_Item(1).getResources().getImages().replace(1, imageStream);
        document.save(outputFile.toString());
    }
}
```

## 
Reemplazar una imagen usando `ImagePlacementAbsorber`


1. Abra el PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. Cree un [ImagePlacementAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/imageplacementabsorber/) y visite la [Página] de destino(https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).

1. Obtenga el objetivo [ImagePlacement](https://reference.aspose.com/pdf/java/com.aspose.pdf/imageplacement/) y reemplácelo con la nueva secuencia de imágenes.
1. Guarde el [Documento] PDF actualizado(https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

```java
public static void replaceImageWithAbsorber(Path inputFile, Path imageFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        ImagePlacementAbsorber absorber = new ImagePlacementAbsorber();
        document.getPages().get_Item(1).accept(absorber);

        if (absorber.getImagePlacements().size() > 0) {
            ImagePlacement imagePlacement = absorber.getImagePlacements().get_Item(1);
            try (InputStream imageStream = Files.newInputStream(imageFile)) {
                imagePlacement.replace(imageStream);
            }
        }

        document.save(outputFile.toString());
    }
}
```
