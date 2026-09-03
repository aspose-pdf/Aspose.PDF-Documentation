---
title: Convertir HTML a PDF en Java
linktitle: Convertir archivo HTML a PDF
type: docs
weight: 40
url: /java/convert-html-to-pdf/
lastmod: "2026-06-16"
description: Aprenda a convertir HTML, MHTML y páginas web a PDF en Java con Aspose.PDF, incluida la configuración de medios, reglas de página CSS, incrustación de fuentes, contenido SVG y salida de una sola página.
sitemap:
    changefreq: "monthly"
    priority: 0.8
TechArticle: true
AlternativeHeadline: Cómo convertir HTML a PDF en Java con Aspose.PDF
Abstract: Este artículo explica cómo convertir archivos HTML y MHTML a PDF usando Aspose.PDF para Java. Cubre el flujo de trabajo básico de HTML a PDF y muestra cómo controlar la representación con tipos de medios, prioridad de reglas de página CSS, fuentes incrustadas, contenido SVG, salida de una sola página y conversión directa desde una página web en vivo.
---
Aspose.PDF para Java puede convertir archivos HTML locales, contenido MHTML archivado y páginas web en vivo en documentos PDF. Puede controlar el proceso de conversión con `HtmlLoadOptions` y `MhtLoadOptions` para influir en la escala del diseño, el manejo de medios CSS, la prioridad de las reglas de página, la incrustación de fuentes, la resolución de recursos y el comportamiento de representación de una sola página.


## 
Convertir HTML a PDF



Utilice este ejemplo cuando un archivo HTML local deba convertirse directamente en un documento PDF.


1. Cree una instancia [`HtmlLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlloadoptions/) para configurar cómo se interpreta la fuente HTML durante la importación.

1. Establezca [`HtmlPageLayoutOption`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlpagelayoutoption/) en `ScaleToPageWidth` para que el contenido HTML ancho se escale al ancho de la página PDF de destino en lugar de recortarse.
1. Abra el archivo HTML de origen pasando su ruta y las opciones de carga configuradas al constructor [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. Guarde el [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) generado como un archivo PDF en la ruta de salida de destino.


```java
public static void convertHtmlToPdf(Path inputFile, Path outputFile) {
    HtmlLoadOptions loadOptions = new HtmlLoadOptions();
    loadOptions.setPageLayoutOption(HtmlPageLayoutOption.ScaleToPageWidth);
    try (Document document = new Document(inputFile.toString(), loadOptions)) {
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## 
Convierta HTML a PDF con opciones de tipo de medio



Utilice este ejemplo cuando el manejo de tipos de medios CSS deba controlarse durante la conversión HTML.


1. Cree una instancia [`HtmlLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlloadoptions/) para la configuración de conversión.
1. Establezca [`HtmlMediaType`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlmediatype/) en `Screen` cuando el HTML deba representarse con reglas CSS destinadas a la visualización en pantalla en lugar de medios impresos.

1. Abra el archivo HTML con las opciones de carga configuradas para que se apliquen estilos dependientes de la consulta de medios durante la conversión.

1. Guarde el [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) resultante como un archivo PDF.


```java
public static void convertHtmlToPdfMediaType(Path inputFile, Path outputFile) {
    HtmlLoadOptions loadOptions = new HtmlLoadOptions();
    loadOptions.setHtmlMediaType(HtmlMediaType.Screen);
    try (Document document = new Document(inputFile.toString(), loadOptions)) {
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## 
Convierta HTML a PDF con prioridad de regla de página CSS



Utilice este ejemplo cuando las reglas CSS `@page` deban influir en el diseño final de la página PDF.

1. Cree una instancia [`HtmlLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlloadoptions/) antes de abrir el archivo HTML.

1. Configure `setPriorityCssPageRule(false)` cuando otras configuraciones de diseño deban tener prioridad sobre las declaraciones CSS `@page` en el marcado de origen.

1. Cargue el contenido HTML en un [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) con las opciones configuradas para que el diseño de la página se resuelva durante la importación.

1. Guarde el archivo PDF generado.


```java
public static void convertHtmlToPdfPriorityCssPageRule(Path inputFile, Path outputFile) {
    HtmlLoadOptions loadOptions = new HtmlLoadOptions();
    loadOptions.setPriorityCssPageRule(false);
    try (Document document = new Document(inputFile.toString(), loadOptions)) {
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## 
Convierta HTML a PDF con fuentes incrustadas

Utilice este ejemplo cuando el PDF de salida deba conservar las fuentes HTML incrustándolas.


1. Cree una instancia [`HtmlLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlloadoptions/) para la configuración de importación HTML.

1. Habilite `setEmbedFonts(true)` para que las fuentes resueltas durante la representación HTML se almacenen en el PDF de salida.

1. Abra la fuente HTML con estas opciones de carga para mantener la tipografía original disponible en el documento final.

1. Guarde el [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) como un PDF con los recursos de fuentes incrustados incluidos.

```java
public static void convertHtmlToPdfEmbedFonts(Path inputFile, Path outputFile) {
    HtmlLoadOptions loadOptions = new HtmlLoadOptions();
    loadOptions.setEmbedFonts(true);
    try (Document document = new Document(inputFile.toString(), loadOptions)) {
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Renderice contenido HTML en una sola página PDF



Utilice este ejemplo cuando el contenido HTML extenso deba mantenerse en una página PDF en lugar de fluir en varias páginas.


1. Cree una instancia [`HtmlLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlloadoptions/) para la configuración de conversión.

1. Habilite `setRenderToSinglePage(true)` para que el HTML importado se presente en una página PDF en lugar de dividirse en varias páginas.

1. Abra el HTML de origen con las opciones de carga configuradas y deje que Aspose.PDF cree el diseño de la página en un [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Guarde el archivo PDF de salida.


```java
public static void convertHtmlToPdfRenderContentToSamePage(Path inputFile, Path outputFile) {
    HtmlLoadOptions loadOptions = new HtmlLoadOptions();
    loadOptions.setRenderToSinglePage(true);
    try (Document document = new Document(inputFile.toString(), loadOptions)) {
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## 
Convertir HTML que contenga SVG en línea



Utilice este ejemplo cuando la fuente HTML incluya datos SVG en línea que deban representarse en el PDF.


1. Cree una instancia [`HtmlLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlloadoptions/) con el directorio principal del archivo HTML como ruta base para que los recursos relacionados se puedan resolver de manera consistente durante la conversión.

1. Abra el archivo HTML que contiene marcado SVG en línea pasando la ruta de origen y cargue las opciones en el constructor [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Deje que Aspose.PDF represente el HTML DOM junto con los elementos SVG incrustados en el contenido de la página PDF.

1. Guarde el documento PDF generado.


```java
public static void convertHtmlToPdfWithSvgData(Path inputFile, Path outputFile) {
    HtmlLoadOptions loadOptions = new HtmlLoadOptions(inputFile.getParent().toString());
    try (Document document = new Document(inputFile.toString(), loadOptions)) {
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## 
Convertir una página web a PDF



Utilice este ejemplo cuando una URL web activa deba representarse y guardarse como un documento PDF.


1. Cree una instancia [`HtmlLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlloadoptions/) con la URL de destino para que los recursos relativos, como hojas de estilo e imágenes, se puedan resolver en esa dirección.
1. Convierta la cadena URL en un objeto `URL` y abra su flujo de entrada para recuperar el contenido HTML en vivo.

1. Cree un [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) a partir del flujo de respuesta y las opciones de carga configuradas para que la página descargada se procese con la URL base correcta.

1. Guarde la página web renderizada como un archivo PDF y cierre los recursos de transmisión automáticamente con try-with-resources.


```java
public static void convertWebPageToPdf(String urlString, Path outputFile) {
    HtmlLoadOptions loadOptions = new HtmlLoadOptions(urlString);
    try {
        URL url = URI.create(urlString).toURL();

        try (InputStream inputStream = url.openStream()) {
            try (Document document = new Document(inputStream, loadOptions)) {
                document.save(outputFile.toString());
            }
        }
        System.out.println(url + " converted into " + outputFile);
    } catch (Exception e) {
        e.printStackTrace();
    }
}
```

## 
Convertir MHTML a PDF



Utilice este ejemplo cuando un archivo MHTML archivado deba convertirse en un documento PDF.

1. Cree una instancia [`MhtLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/mhtloadoptions/) para indicarle a Aspose.PDF que cargue la fuente como contenido HTML MIME.

1. Abra el archivo `.mht` o `.mhtml` pasando su ruta y las opciones de carga MHTML al constructor [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. Deje que Aspose.PDF analice el contenido HTML archivado y sus recursos incrustados en el modelo de documento PDF.

1. Guarde el archivo PDF generado.

```java
public static void convertMhtmlToPdf(Path inputFile, Path outputFile) {
    MhtLoadOptions loadOptions = new MhtLoadOptions();
    try (Document document = new Document(inputFile.toString(), loadOptions)) {
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```
