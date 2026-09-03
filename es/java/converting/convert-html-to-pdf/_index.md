---
title: Convertir HTML a PDF en Java
linktitle: Convertir HTML a archivo PDF
type: docs
weight: 40
url: /es/java/convert-html-to-pdf/
lastmod: "2026-09-03"
description: Aprenda a convertir HTML, MHTML y páginas web a PDF en Java con Aspose.PDF, incluyendo configuraciones de medios, reglas de página CSS, incrustación de fuentes, contenido SVG y salida de una sola página.
sitemap:
    changefreq: "monthly"
    priority: 0.8
TechArticle: true
AlternativeHeadline: Cómo convertir HTML a PDF en Java con Aspose.PDF
Abstract: Este artículo explica cómo convertir archivos HTML y MHTML a PDF usando Aspose.PDF for Java. Cubre el flujo de trabajo básico de HTML-a-PDF y muestra cómo controlar la renderización con tipos de medios, prioridad de reglas de página CSS, fuentes incrustadas, contenido SVG, salida de una sola página y conversión directa desde una página web en vivo.
---
Aspose.PDF for Java puede convertir archivos HTML locales, contenido MHTML archivado y páginas web en vivo en documentos PDF. Puedes controlar la canalización de conversión con `HtmlLoadOptions` y `MhtLoadOptions` para influir en el escalado del diseño, el manejo de medios CSS, la prioridad de reglas de página, la incrustación de fuentes, la resolución de recursos y el comportamiento de renderizado de una sola página.

## Convertir HTML a PDF

Utilice este ejemplo cuando un archivo HTML local deba convertirse directamente en un documento PDF.

1. Crear un [`HtmlLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlloadoptions/) instancia para configurar cómo se interpreta la fuente HTML durante la importación.
1. Establecer [`HtmlPageLayoutOption`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlpagelayoutoption/) a `ScaleToPageWidth` por lo que el contenido HTML tan ancho se escala al ancho de la página PDF de destino en lugar de ser recortado.
1. Abra el archivo HTML de origen pasando su ruta y las opciones de carga configuradas al [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) constructor.
1. Guardar lo generado [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) como un archivo PDF en la ruta de salida de destino.

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

## Convertir HTML a PDF con opciones de tipo de medio

Utilice este ejemplo cuando el manejo del tipo de medio CSS deba controlarse durante la conversión HTML.

1. Crear un [`HtmlLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlloadoptions/) instancia para la configuración de conversión.
1. Establecer [`HtmlMediaType`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlmediatype/) a `Screen` cuando el HTML debe renderizarse con reglas CSS destinadas a la visualización en pantalla en lugar de los medios de impresión.
1. Abra el archivo HTML con las opciones de carga configuradas para que los estilos dependientes de consultas de medios se apliquen durante la conversión.
1. Guardar el resultado [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) como un archivo PDF.

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

## Convertir HTML a PDF con prioridad de regla de página CSS

Utilice este ejemplo cuando CSS `@page` Las reglas deberían influir en el diseño final de la página PDF.

1. Crear un [`HtmlLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlloadoptions/) instancia antes de abrir el archivo HTML.
1. Configurar `setPriorityCssPageRule(false)` cuando otras configuraciones de diseño deben tener prioridad sobre CSS `@page` declaraciones en el marcado de origen.
1. Cargar el contenido HTML en un [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) con las opciones configuradas para que el diseño de página se resuelva durante la importación.
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

## Convertir HTML a PDF con fuentes incrustadas

Utilice este ejemplo cuando el PDF de salida deba conservar las fuentes HTML incrustándolas.

1. Crear un [`HtmlLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlloadoptions/) instancia para la configuración de importación HTML.
1. Habilitar `setEmbedFonts(true)` por lo tanto, las fuentes resueltas durante la renderización HTML se almacenan en el PDF de salida.
1. Abra la fuente HTML con estas opciones de carga para mantener la tipografía original disponible en el documento final.
1. Guardar el [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) como un PDF con los recursos de fuentes incrustados incluidos.

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

## Renderizar contenido HTML en una sola página PDF

Utilice este ejemplo cuando el contenido HTML largo debe mantenerse en una sola página PDF en lugar de fluir a través de varias páginas.

1. Crear un [`HtmlLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlloadoptions/) instancia para la configuración de conversión.
1. Habilitar `setRenderToSinglePage(true)` por lo que el HTML importado se muestra en una sola página PDF en lugar de dividirse en varias páginas.
1. Abra el HTML de origen con las opciones de carga configuradas y permita que Aspose.PDF construya el diseño de página en un [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
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

## Convertir HTML que contiene SVG en línea

Utilice este ejemplo cuando la fuente HTML incluya datos SVG en línea que deben renderizarse en el PDF.

1. Crear un [`HtmlLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlloadoptions/) instancia con el directorio principal del archivo HTML como ruta base para que los recursos relacionados se resuelvan de manera consistente durante la conversión.
1. Abra el archivo HTML que contiene marcado SVG inline pasando la ruta de origen y las opciones de carga al [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) constructor.
1. Permita que Aspose.PDF renderice el DOM HTML junto con los elementos SVG incrustados en el contenido de la página PDF.
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

## Convertir una página web a PDF

Utilice este ejemplo cuando se deba renderizar y guardar como documento PDF una URL web en vivo.

1. Crear un [`HtmlLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlloadoptions/) instancia con la URL de destino para que los recursos relativos, como hojas de estilo e imágenes, puedan resolverse contra esa dirección.
1. Convertir la cadena URL en un `URL` objeto y abrir su flujo de entrada para obtener el contenido HTML en vivo.
1. Crear un [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) del flujo de respuesta y las opciones de carga configuradas para que la página descargada se procese con la URL base correcta.
1. Guarde la página web renderizada como un archivo PDF y cierre los recursos de flujo automáticamente con try-with-resources.

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

## Convertir MHTML a PDF

Utilice este ejemplo cuando un archivo MHTML archivado deba convertirse en un documento PDF.

1. Crear un [`MhtLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/mhtloadoptions/) instancia para indicarle a Aspose.PDF que cargue el origen como contenido HTML MIME.
1. Abrir el `.mht` o `.mhtml` archivo pasando su ruta y las opciones de carga MHTML en el [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) constructor.
1. Permita que Aspose.PDF analice el contenido HTML archivado y sus recursos incrustados en el modelo de documento PDF.
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
