---
title: Anotaciones y texto especial usando Java
linktitle: Anotaciones y texto especial
type: docs
weight: 40
url: /es/java/annotation-and-special-text/
description: Aprenda cómo extraer texto de anotaciones de sello, texto resaltado y contenido en superíndice o subíndice en documentos PDF usando Aspose.PDF for Java.
lastmod: "2026-09-03"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
## Extraer texto resaltado

Iterar a través de las anotaciones de la página y leer el texto marcado de `HighlightAnnotation`.

1. Abra el PDF de origen en un [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) instancia.
1. Iterar a través del [Anotación](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotation/) objetos en el objetivo [Página](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
1. Verifique si cada anotación es una [HighlightAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/highlightannotation/) antes de convertirla a la clase de anotación tipada.
1. Lea el texto marcado de cada anotación de resaltado y imprímalo en la consola.

```java
public static void extractHighlightedText(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation instanceof HighlightAnnotation) {
                HighlightAnnotation highlightAnnotation = (HighlightAnnotation) annotation;
                System.out.println(highlightAnnotation.getMarkedText());
            }
        }
    }
}
```

## Extraer texto de anotaciones de sello

Lea el flujo de apariencia normal de una anotación de sello y páselo `TextAbsorber`.

1. Abra el PDF de origen en un [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) instancia.
1. Iterar a través del [Anotación](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotation/) objetos en el objetivo [Página](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
1. Filtra las anotaciones a aquellas cuyo tipo es `Stamp`.
1. Crear un [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/textabsorber/) y solicite la entrada de apariencia normal del diccionario de apariencia de la anotación de sello.
1. Visite la apariencia [XForm](https://reference.aspose.com/pdf/java/com.aspose.pdf/xform/) y imprima el texto extraído.

```java
public static void extractStampText(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.Stamp) {
                TextAbsorber absorber = new TextAbsorber();
                Object[] xforms = new Object[1];
                if (annotation.getAppearance().tryGetValue("N", xforms) && xforms[0] instanceof XForm) {
                    absorber.visit((XForm) xforms[0]);
                    System.out.println(absorber.getText());
                }
            }
        }
    }
}
```

## Extraer los detalles de texto en superíndice y subíndice

Usar `TextFragmentAbsorber` cuando necesites tanto el texto extraído como las banderas de superíndice o subíndice en cada fragmento.

1. Abra el PDF de origen en un [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) instancia.
1. Crear un [TextFragmentAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragmentabsorber/) para análisis de texto a nivel de fragmento.
1. Visite el objetivo [Página](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) y recógelos [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/) objetos.
1. Itera a través de esos fragmentos y lee el texto junto con las banderas de superíndice y subíndice desde `fragment.getTextState()`.
1. Escriba los detalles extraídos en el archivo de salida.

```java
public static void extractSuperSubDetails(Path inputFile, Path outputFile, int pageNumber) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        TextFragmentAbsorber absorber = new TextFragmentAbsorber();
        document.getPages().get_Item(pageNumber).accept(absorber);
        StringBuilder details = new StringBuilder();
        for (TextFragment fragment : absorber.getTextFragments()) {
            details.append("Text: '").append(fragment.getText())
                    .append("' | Superscript: ").append(fragment.getTextState().isSuperscript())
                    .append(" | Subscript: ").append(fragment.getTextState().isSubscript())
                    .append(System.lineSeparator());
        }
        Files.writeString(outputFile, details.toString());
    }
}
```
