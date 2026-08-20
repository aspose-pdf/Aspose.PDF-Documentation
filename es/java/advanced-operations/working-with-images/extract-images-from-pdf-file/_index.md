---
title: Extraiga imágenes de un archivo PDF usando Java
linktitle: Extraer imágenes
type: docs
weight: 30
url: /java/extract-images-from-pdf-file/
description: Aprenda a extraer imágenes incrustadas de archivos PDF en Java.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Extrae imágenes de archivos PDF con Java
Abstract: Este artículo muestra cómo extraer imágenes de documentos PDF usando Aspose.PDF para Java. Cubre guardar un recurso de imagen específico de una página y exportar imágenes que se encuentran dentro de una región rectangular seleccionada.
---
Aspose.PDF para Java admite la extracción directa de recursos de imágenes y el filtrado basado en ubicación.


## 
Extraer una imagen incrustada por índice



Utilice este ejemplo cuando necesite guardar un recurso de imagen específico desde una página PDF.


1. 
Abra el PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Acceda al objetivo [XImage](https://reference.aspose.com/pdf/java/com.aspose.pdf/ximage/) desde los recursos de la página.
1. Guarde la secuencia de imágenes en un archivo de salida.


```java
public static void extractImage(Path inputFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString());
         OutputStream outputImage = Files.newOutputStream(outputFile)) {
        XImage image = document.getPages().get_Item(1).getResources().getImages().get_Item(1);
        image.save(outputImage);
    }
}
```

## 
Extraer imágenes de una región de página específica



Utilice este ejemplo cuando solo se deban exportar imágenes colocadas dentro de un rectángulo seleccionado.


1. 
Defina el [Rectángulo] de destino(https://reference.aspose.com/pdf/java/com.aspose.pdf/rectangle/) y abra el PDF de origen.

1. 
Utilice [ImagePlacementAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/imageplacementabsorber/) para inspeccionar la ubicación de las imágenes en la página.
1. Guarde solo las imágenes cuya ubicación se ajuste dentro de la región seleccionada.

```java
public static void extractImageFromSpecificRegion(Path inputFile, Path outputFile) throws Exception {
    Rectangle rectangle = new Rectangle(0, 0, 590, 590, true);

    try (Document document = new Document(inputFile.toString())) {
        ImagePlacementAbsorber absorber = new ImagePlacementAbsorber();
        document.getPages().get_Item(1).accept(absorber);
        int index = 1;
        for (ImagePlacement imagePlacement : absorber.getImagePlacements()) {
            Point point1 = new Point(imagePlacement.getRectangle().getLLX(), imagePlacement.getRectangle().getLLY());
            Point point2 = new Point(imagePlacement.getRectangle().getURX(), imagePlacement.getRectangle().getURX());
            if (rectangle.contains(point1, true) && rectangle.contains(point2, true)) {
                Path indexedOutputFile = Path.of(outputFile.toString().replace("index", String.valueOf(index)));
                try (OutputStream outputImage = Files.newOutputStream(indexedOutputFile)) {
                    imagePlacement.getImage().save(outputImage);
                }
                index++;
            }
        }
    }
}
```
