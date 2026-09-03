---
title: Extraer imágenes de archivo PDF usando Java
linktitle: Extraer imágenes
type: docs
weight: 30
url: /es/java/extract-images-from-pdf-file/
description: Aprenda cómo extraer imágenes incrustadas de archivos PDF en Java.
lastmod: "2026-09-03"
TechArticle: true
AlternativeHeadline: Extraer imágenes de archivos PDF con Java
Abstract: Este artículo muestra cómo extraer imágenes de documentos PDF usando Aspose.PDF for Java. Cubre el guardado de un recurso de imagen específico de una página y la exportación de imágenes que se encuentren dentro de una región rectangular seleccionada.
---
Aspose.PDF for Java admite la extracción directa de recursos de imagen y el filtrado basado en la ubicación.

## Extraer una imagen incrustada por índice

Utilice este ejemplo cuando necesite guardar un recurso de imagen específico de una página PDF.

1. Abrir el PDF de origen [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Acceder al objetivo [XImage](https://reference.aspose.com/pdf/java/com.aspose.pdf/ximage/) de los recursos de la página.
1. Guarde el flujo de imagen en un archivo de salida.

```java
public static void extractImage(Path inputFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString());
         OutputStream outputImage = Files.newOutputStream(outputFile)) {
        XImage image = document.getPages().get_Item(1).getResources().getImages().get_Item(1);
        image.save(outputImage);
    }
}
```

## Extraer imágenes de una región específica de la página

Utilice este ejemplo cuando solo se deben exportar las imágenes ubicadas dentro de un rectángulo seleccionado.

1. Defina el objetivo [Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf/rectangle/) y abra el PDF de origen.
1. Usar [ImagePlacementAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/imageplacementabsorber/) para inspeccionar la ubicación de las imágenes en la página.
1. Guarde solo las imágenes cuya ubicación encaje dentro de la región seleccionada.

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
