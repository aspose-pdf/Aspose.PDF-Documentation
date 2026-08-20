---
title: Anotaciones y texto especial usando Java
linktitle: Anotaciones y texto especial
type: docs
weight: 40
url: /java/annotation-and-special-text/
description: Aprenda a extraer texto de anotaciones de sellos, texto resaltado y contenido en superíndice o subíndice en documentos PDF utilizando Aspose.PDF para Java.
lastmod: "2026-06-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
## 
Extraer texto resaltado



Itere a través de las anotaciones de la página y lea el texto marcado de `HighlightAnnotation`.

1. Abra el PDF de origen en una instancia de [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Itere a través de los objetos [Anotación](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotation/) en la [Página] de destino(https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).

1. 
Compruebe si cada anotación es una [HighlightAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/highlightannotation/) antes de enviarla a la clase de anotación escrita.

1. 
Lea el texto marcado de cada anotación resaltada e imprímalo en la consola.


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

## 
Extraer texto de anotaciones de sellos

Lea la secuencia de apariencia normal de una anotación de sello y pásela a través de `TextAbsorber`.


1. 
Abra el PDF de origen en una instancia de [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Itere a través de los objetos [Anotación](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotation/) en la [Página] de destino(https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).

1. 
Filtre las anotaciones a aquellas cuyo tipo sea `Stamp`.

1. 
Cree un [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/textabsorber/) y solicite la entrada de apariencia normal del diccionario de apariencia de anotaciones de sellos.
1. Visite la apariencia [XForm](https://reference.aspose.com/pdf/java/com.aspose.pdf/xform/) e imprima el texto extraído.


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

## 
Extraiga detalles de texto en superíndice y subíndice



Utilice `TextFragmentAbsorber` cuando necesite tanto el texto extraído como los indicadores de superíndice o subíndice en cada fragmento.


1. 
Abra el PDF de origen en una instancia de [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Cree un [TextFragmentAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragmentabsorber/) para el análisis de texto a nivel de fragmento.
1. Visite la [Página](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) de destino y recopile sus objetos [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/).

1. 
Repita esos fragmentos y lea el texto junto con los indicadores de superíndice y subíndice de `fragment.getTextState()`.

1. 
Escriba los detalles extraídos en el archivo de salida.

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
