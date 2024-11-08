---
title: Buscar y Obtener Texto de las Páginas de un Documento PDF
linktitle: Buscar y Obtener Texto
type: docs
weight: 60
url: /es/java/search-and-get-text-from-pdf/
description: Este artículo explica cómo usar varias herramientas para buscar y obtener texto de documentos PDF. Podemos buscar con expresiones regulares en páginas particulares o en todo el documento.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Buscar y Obtener Texto de Todas las Páginas de un Documento PDF

TextFragmentAbsorber te permite encontrar texto que coincide con una frase particular de todas las páginas de un documento PDF.

Para buscar texto en todo el documento, llama al método accept() de la colección [Pages](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page).
 El método [accept()](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFragmentAbsorber) toma un objeto TextFragmentAbsorber como parámetro, el cual devuelve una colección de objetos TextFragment. Recorre todos los fragmentos para obtener sus propiedades, por ejemplo Texto, Posición, XIndent, YIndent, FontName, FontSize, IsAccessible, IsEmbedded, IsSubset, ForegroundColor, etc.

El siguiente fragmento de código muestra cómo buscar en todo el documento y mostrar todas las coincidencias en una consola.

```java
// Abrir documento
Document pdfDocument = new Document("input.pdf");

// Crear objeto TextAbsorber para encontrar todas las instancias de la frase de búsqueda de entrada
TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("sample");

// Aceptar el absorbedor para todas las páginas
pdfDocument.getPages().accept(textFragmentAbsorber);

// Obtener los fragmentos de texto extraídos en la colección
TextFragmentCollection textFragmentCollection = textFragmentAbsorber.getTextFragments();

// Recorrer los fragmentos
for (TextFragment textFragment : (Iterable<TextFragment>) textFragmentCollection) {
    System.out.println("Texto :- " + textFragment.getText());
    System.out.println("Posición :- " + textFragment.getPosition());
    System.out.println("XIndent :- " + textFragment.getPosition().getXIndent());
    System.out.println("YIndent :- " + textFragment.getPosition().getYIndent());
    System.out.println("Fuente - Nombre :- " + textFragment.getTextState().getFont().getFontName());
    System.out.println("Fuente - IsAccessible :- " + textFragment.getTextState().getFont().isAccessible());
    System.out.println("Fuente - IsEmbedded - " + textFragment.getTextState().getFont().isEmbedded());
    System.out.println("Fuente - IsSubset :- " + textFragment.getTextState().getFont().isSubset());
    System.out.println("Tamaño de Fuente :- " + textFragment.getTextState().getFontSize());
    System.out.println("Color de Primer Plano :- " + textFragment.getTextState().getForegroundColor());
}
```

Para buscar texto en una página en particular y obtener propiedades asociadas con él, proporcione el índice de la página:

```java
// Aceptar el absorbedor para la primera página del documento
pdfDocument.getPages().get_Item(1).accept(textFragmentAbsorber);
```

## Buscar y Obtener Segmentos de Texto de las Páginas de un PDF

Para buscar segmentos de texto en todas las páginas de un documento, obtenga los objetos TextFragment de un documento.

TextFragmentAbsorber te permite encontrar texto, coincidiendo con una frase en particular, de todas las páginas en un documento PDF. Para buscar texto en todo el documento, llame al método [accept()](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFragmentAbsorber) de la colección [Pages](https://reference.aspose.com/pdf//java/com.aspose.pdf/pagecollection). El método [accept()](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFragmentAbsorber) toma un objeto TextFragmentAbsorber como parámetro, que devuelve una colección de objetos TextFragment.

{{% alert color="primary" %}}

Cuando se ha obtenido la colección TextFragmentCollection del documento, recorra el bucle para obtener la colección TextSegmentCollection de cada objeto TextFragment.
 Después de eso, puedes obtener las propiedades del objeto TextSegment individual.

{{% /alert %}}

El siguiente fragmento de código muestra cómo buscar segmentos de texto en todas las páginas.

```java
// Abrir documento
Document pdfDocument = new Document("input.pdf");

// Crear objeto TextAbsorber para encontrar todas las instancias de la frase de búsqueda de entrada
TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("sample");

// Aceptar el absorber para la primera página del documento
pdfDocument.getPages().accept(textFragmentAbsorber);

// Obtener los fragmentos de texto extraídos en una colección
TextFragmentCollection textFragmentCollection = textFragmentAbsorber.getTextFragments();

// Recorrer los fragmentos de texto
for (TextFragment textFragment : (Iterable<TextFragment>) textFragmentCollection) {
    // Iterar a través de los segmentos de texto
    for (TextSegment textSegment : (Iterable<TextSegment>) textFragment.getSegments()) {
        System.out.println("Texto :- " + textSegment.getText());
        System.out.println("Posición :- " + textSegment.getPosition());
        System.out.println("XIndentación :- " + textSegment.getPosition().getXIndent());
        System.out.println("YIndentación :- " + textSegment.getPosition().getYIndent());
        System.out.println("Fuente - Nombre :- " + textSegment.getTextState().getFont().getFontName());
        System.out.println("Fuente - EsAccesible :- " + textSegment.getTextState().getFont().isAccessible());
        System.out.println("Fuente - EstáIncorporada - " + textSegment.getTextState().getFont().isEmbedded());
        System.out.println("Fuente - EsSubconjunto :- " + textSegment.getTextState().getFont().isSubset());
        System.out.println("Tamaño de Fuente :- " + textSegment.getTextState().getFontSize());
        System.out.println("Color de Primer Plano :- " + textSegment.getTextState().getForegroundColor());
    }
}
```

Para buscar un segmento de texto específico y obtener las propiedades asociadas, especifique el índice de página para la página que desea buscar:

```java
// Aceptar el absorbedor para la primera página del documento.
pdfDocument.getPages().get_Item(1).accept(textFragmentAbsorber);
```

## Buscar y Obtener Texto de las páginas usando Expresión Regular

TextFragmentAbsorber te ayuda a buscar y recuperar texto de todas las páginas en un documento, basado en una expresión regular.

Para buscar y obtener texto de un documento:

1. Pase el término de búsqueda como una expresión regular al constructor de TextFragmentAbsorber.
1. Establezca la propiedad TextSearchOptions del objeto TextFragmentAbsorber.
   Esta propiedad requiere un objeto TextSearchOptions: pase true a su constructor al crear un nuevo objeto.
1. Para recuperar el texto coincidente de todas las páginas, llame al método [accept()](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFragmentAbsorber) de la colección [Pages](https://reference.aspose.com/pdf//java/com.aspose.pdf/pagecollection).

   TextFragmentAbsorber devuelve un TextFragmentCollection que contiene todos los fragmentos que coinciden con los criterios especificados por la expresión regular.

El siguiente fragmento de código muestra cómo buscar todas las páginas en un documento y obtener texto basado en una expresión regular.

```java
// Abrir un documento
Document pdfDocument = new Document("source.pdf");

// Crear un objeto TextAbsorber para encontrar todas las instancias de la frase de búsqueda de entrada
TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("\\d{4}-\\d{4}"); // como 1999-2000

// Establecer la opción de búsqueda de texto para especificar el uso de expresiones regulares
TextSearchOptions textSearchOptions = new TextSearchOptions(true);
textFragmentAbsorber.setTextSearchOptions(textSearchOptions);

// Aceptar el absorbente para la primera página del documento
pdfDocument.getPages().accept(textFragmentAbsorber);

// Obtener los fragmentos de texto extraídos en una colección
TextFragmentCollection textFragmentCollection = textFragmentAbsorber.getTextFragments();

// Bucle a través de los fragmentos
for (TextFragment textFragment : (Iterable<TextFragment>) textFragmentCollection) {
    System.out.println("Texto :- " + textFragment.getText());
    System.out.println("Posición :- " + textFragment.getPosition());
    System.out.println("XIndent :- " + textFragment.getPosition().getXIndent());
    System.out.println("YIndent :- " + textFragment.getPosition().getYIndent());
    System.out.println("Fuente - Nombre :- " + textFragment.getTextState().getFont().getFontName());
    System.out.println("Fuente - EsAccesible :- " + textFragment.getTextState().getFont().isAccessible());
    System.out.println("Fuente - EstáIncrustada - " + textFragment.getTextState().getFont().isEmbedded());
    System.out.println("Fuente - EsSubconjunto :- " + textFragment.getTextState().getFont().isSubset());
    System.out.println("Tamaño de Fuente :- " + textFragment.getTextState().getFontSize());
    System.out.println("Color de Primer Plano :- " + textFragment.getTextState().getForegroundColor());
}
```


Para buscar texto en una página en particular y obtener sus propiedades, especifique el índice de la página:

```java
// Aceptar el absorbedor para la primera página del documento.
pdfDocument.getPages().get_Item(1).accept(textFragmentAbsorber)
```

Para buscar una cadena en mayúsculas o minúsculas, puede considerar usar una expresión regular.

```java
TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("(?i)Line", new TextSearchOptions(true));
```

Ejemplo:

```java
TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("[\\S]+");
```