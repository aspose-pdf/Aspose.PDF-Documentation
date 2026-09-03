---
title: Extraiga datos vectoriales de un archivo PDF usando Java
linktitle: Extraer datos vectoriales de PDF
type: docs
weight: 80
url: /java/extract-vector-data-from-pdf/
description: Aspose.PDF facilita la extracción de datos vectoriales de un archivo PDF. Puede obtener los datos vectoriales, como la posición, los límites del rectángulo y la salida SVG.
lastmod: "2026-06-16"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
## 
Acceda a datos vectoriales desde un documento PDF



Utilice `GraphicsAbsorber` para inspeccionar elementos gráficos vectoriales en una página y escribir su geometría básica en un archivo de texto.

1. Abra el PDF de origen en una instancia de [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. Cree un [GraphicsAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf.vector/graphicsabsorber/) y visite la [Página](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) de destino para recopilar operaciones de gráficos vectoriales.

1. Itere a través de los objetos [GraphicElement](https://reference.aspose.com/pdf/java/com.aspose.pdf.vector/graphicelement/) extraídos y lea sus colecciones de rectángulos, posiciones y operadores.

1. Cree el texto de salida con geometría y detalles de recuento de operadores para cada elemento.

1. Escriba los datos vectoriales extraídos en el archivo de salida.

```java
public static void extractGraphicsElements(Path inputFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        GraphicsAbsorber absorber = new GraphicsAbsorber();
        absorber.visit(document.getPages().get_Item(1));

        StringBuilder text = new StringBuilder();
        int index = 1;
        for (GraphicElement element : absorber.getElements()) {
            text.append("Element ").append(index)
                    .append(": Rectangle = ").append(element.getRectangle())
                    .append(", Position = ").append(element.getPosition())
                    .append(", Operators = ").append(element.getOperators().size())
                    .append("\n");
            index++;
        }
        Files.writeString(outputFile, text.toString());
    }
}
```

## Guarde los gráficos vectoriales de la página en SVG


1. Abra el PDF de origen en una instancia de [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. Obtenga la [Página] de destino(https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) del documento.

1. Llame a `page.trySaveVectorGraphics(outputFile.toString())` para exportar el contenido de gráficos vectoriales de esa página directamente a SVG.


```java
public static void saveVectorGraphicsToSvg(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page page = document.getPages().get_Item(1);
        page.trySaveVectorGraphics(outputFile.toString());
    }
}
```

## 
Guarde cada elemento extraído en un SVG separado

1. Abra el PDF de origen en una instancia de [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. Cree un [GraphicsAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf.vector/graphicsabsorber/) y visite la [Página] de destino(https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).

1. Cree el directorio de salida para las subrutas extraídas antes de escribir cualquier archivo.

1. Itere a través de los objetos [GraphicElement](https://reference.aspose.com/pdf/java/com.aspose.pdf.vector/graphicelement/) extraídos y llame a `saveToSvg(...)` para cada elemento.

1. Guarde cada elemento extraído en un archivo SVG separado.

```java
public static void extractSubpathsToSvgs(Path inputFile, Path outputDir) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        GraphicsAbsorber absorber = new GraphicsAbsorber();
        absorber.visit(document.getPages().get_Item(1));
        Path subpathsDir = outputDir.resolve("subpaths");
        Files.createDirectories(subpathsDir);

        int index = 1;
        for (GraphicElement element : absorber.getElements()) {
            element.saveToSvg(subpathsDir.resolve("subpath_" + index + ".svg").toString());
            index++;
        }
    }
}
```

## Combina elementos extraídos en un solo SVG


1. Abra el PDF de origen en una instancia de [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. Cree un [GraphicsAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf.vector/graphicsabsorber/) y visite la [Página] de destino(https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).

1. Cree el marcado contenedor SVG que contendrá los fragmentos vectoriales combinados.

1. Itere a través de los objetos [GraphicElement](https://reference.aspose.com/pdf/java/com.aspose.pdf.vector/graphicelement/) extraídos y agregue cada fragmento SVG generado.
1. Escriba la salida SVG combinada en el archivo de destino.


```java
public static void extractListOfElementsToSingleImage(Path inputFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        GraphicsAbsorber absorber = new GraphicsAbsorber();
        absorber.visit(document.getPages().get_Item(1));

        StringBuilder svg = new StringBuilder();
        svg.append("<svg xmlns=\"http://www.w3.org/2000/svg\">\n");
        for (GraphicElement element : absorber.getElements()) {
            svg.append(element.saveToSvg()).append("\n");
        }
        svg.append("</svg>\n");
        Files.writeString(outputFile, svg.toString());
    }
}
```

## 
Extraer un único elemento vectorial


1. Abra el PDF de origen en una instancia de [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. Cree un [GraphicsAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf.vector/graphicsabsorber/) y visite la [Página] de destino(https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).

1. Obtenga el [GraphicElement](https://reference.aspose.com/pdf/java/com.aspose.pdf.vector/graphicelement/) requerido de la colección de elementos extraídos.
1. Compruebe si el elemento seleccionado es un [XFormPlacement](https://reference.aspose.com/pdf/java/com.aspose.pdf.vector/xformplacement/) y descienda a sus elementos anidados cuando sea necesario.

1. Guarde el elemento vectorial seleccionado en el archivo SVG de salida.

```java
public static void extractSingleVectorElement(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        GraphicsAbsorber graphicsAbsorber = new GraphicsAbsorber();
        Page page = document.getPages().get_Item(1);
        graphicsAbsorber.visit(page);
        if (graphicsAbsorber.getElements().size() > 1) {
            GraphicElement xformPlacement = graphicsAbsorber.getElements().get_Item(1);
            if (xformPlacement instanceof XFormPlacement) {
                XFormPlacement placement = (XFormPlacement) xformPlacement;
                if (placement.getElements().size() > 2) {
                    placement.getElements().get_Item(2).saveToSvg(outputFile.toString());
                }
            } else {
                xformPlacement.saveToSvg(outputFile.toString());
            }
        }
    }
}
```
