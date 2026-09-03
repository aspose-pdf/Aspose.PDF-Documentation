---
title: Recortar páginas PDF en Java
linktitle: Recortando páginas PDF
type: docs
weight: 70
url: /es/java/crop-pages/
description: Aprenda cómo recortar páginas PDF y ajustar las cajas crop, trim, bleed y media en Java.
lastmod: "2026-09-03"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Recorte páginas y ajuste las cajas de página en archivos PDF con Java.
Abstract: Este artículo explica cómo recortar páginas PDF usando Aspose.PDF for Java. Cubre la asignación de un nuevo rectángulo de recorte a las cajas crop, trim, art y bleed, y el recorte de una página de forma automática basado en el contenido de imagen detectado.
---
Aspose.PDF for Java le permite recortar páginas ya sea mediante coordenadas de caja explícitas o basándose en el contenido detectado.

## Recortar una página estableciendo los recuadros de página

Utilice este ejemplo cuando necesite aplicar la misma área de recorte a los recuadros principales de la página

1. Abra el PDF de origen [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Cree el nuevo recorte [Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf/rectangle/).
1. Aplicar el rectángulo a los recuadros de página relacionados con el recorte y guardar el documento.

```java
public static void cropPage(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Rectangle newBox = new Rectangle(200, 220, 2170, 1520, true);
        document.getPages().get_Item(1).setCropBox(newBox);
        document.getPages().get_Item(1).setTrimBox(newBox);
        document.getPages().get_Item(1).setArtBox(newBox);
        document.getPages().get_Item(1).setBleedBox(newBox);
        document.save(outputFile.toString());
    }
}
```

## Recortar una página según el contenido detectado

Utilice este ejemplo cuando el área de recorte debe derivarse de la primera imagen detectada en la página.

1. Abra el PDF de origen [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Usar [ImagePlacementAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/imageplacementabsorber/) para detectar la colocación de imágenes.
1. Establezca el cuadro de recorte al rectángulo de la imagen si se encuentra uno, luego guarde el documento.

```java
public static void cropPageByContent(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        ImagePlacementAbsorber absorber = new ImagePlacementAbsorber();
        document.getPages().get_Item(1).accept(absorber);
        if (absorber.getImagePlacements().size() > 0) {
            document.getPages().get_Item(1).setCropBox(absorber.getImagePlacements().get_Item(1).getRectangle());
        } else {
            System.out.println("No images found on the first page");
        }
        document.save(outputFile.toString());
    }
}
```
