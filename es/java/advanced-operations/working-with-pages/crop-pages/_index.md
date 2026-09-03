---
title: Recortar páginas PDF en Java
linktitle: Recortar páginas PDF
type: docs
weight: 70
url: /java/crop-pages/
description: Aprenda a recortar páginas PDF y ajustar cuadros de recorte, recorte, sangrado y medios en Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Recorte páginas y ajuste cuadros de página en archivos PDF con Java
Abstract: Este artículo explica cómo recortar páginas PDF usando Aspose.PDF para Java. Cubre la asignación de un nuevo rectángulo de recorte a los cuadros de recorte, recorte, arte y sangrado, y el recorte de una página automáticamente según el contenido de la imagen detectada.
---
Aspose.PDF para Java le permite recortar páginas mediante coordenadas de cuadro explícitas o según el contenido detectado.


## 
Recortar una página configurando cuadros de página



Utilice este ejemplo cuando necesite aplicar la misma área de recorte a los cuadros de la página principal.


1. Abra el PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. Cree el nuevo recorte [Rectángulo](https://reference.aspose.com/pdf/java/com.aspose.pdf/rectangle/).
1. Aplique el rectángulo a los cuadros de página relacionados con el recorte y guarde el documento.


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

## 
Recortar una página por contenido detectado



Utilice este ejemplo cuando el área de recorte deba derivarse de la primera imagen detectada en la página.


1. Abra el PDF de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. Utilice [ImagePlacementAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/imageplacementabsorber/) para detectar ubicaciones de imágenes.
1. Configure el cuadro de recorte en el rectángulo de la imagen si se encuentra uno y luego guarde el documento.

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
