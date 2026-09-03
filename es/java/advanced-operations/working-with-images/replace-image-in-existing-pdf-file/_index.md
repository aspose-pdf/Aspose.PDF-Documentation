---
title: Reemplazar imagen en archivo PDF existente usando Java
linktitle: Reemplazar imagen
type: docs
weight: 70
url: /es/java/replace-image-in-existing-pdf-file/
description: Aprenda cómo reemplazar imágenes incrustadas en archivos PDF existentes en Java.
lastmod: "2026-09-03"
TechArticle: true
AlternativeHeadline: Reemplazar imágenes en archivos PDF existentes con Java
Abstract: Este artículo muestra cómo reemplazar imágenes en documentos PDF usando Aspose.PDF for Java. Cubre cómo reemplazar una imagen por su índice de recurso y cómo reemplazar la primera ubicación de imagen coincidente encontrada con ImagePlacementAbsorber.
---
Utilice la colección de imágenes de la página o la búsqueda basada en ubicaciones según la precisión con la que necesite apuntar a la imagen.

## Reemplazar una imagen por índice de recurso

1. Abrir el PDF de origen [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Acceder a los recursos de imagen en el objetivo [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
1. Reemplazar el recurso de imagen del objetivo con el nuevo archivo de imagen.
1. Guarde el PDF actualizado [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

```java
public static void replaceImage(Path inputFile, Path imageFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString());
         InputStream imageStream = Files.newInputStream(imageFile)) {
        document.getPages().get_Item(1).getResources().getImages().replace(1, imageStream);
        document.save(outputFile.toString());
    }
}
```

## Reemplazar una imagen usando `ImagePlacementAbsorber`

1. Abrir el PDF de origen [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Crear un [ImagePlacementAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/imageplacementabsorber/) y visitar el objetivo [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
1. Obtener el objetivo [ImagePlacement](https://reference.aspose.com/pdf/java/com.aspose.pdf/imageplacement/) y reemplázalo con el nuevo flujo de imagen.
1. Guarde el PDF actualizado [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

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
