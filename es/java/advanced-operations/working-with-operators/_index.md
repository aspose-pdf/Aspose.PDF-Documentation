---
title: Trabajar con operadores PDF en Java
linktitle: Trabajando con operadores
type: docs
weight: 90
url: /es/java/working-with-operators/
description: Aprenda a usar operadores PDF de bajo nivel en Java para la manipulación de flujos de contenido, colocación de imágenes, reutilización de XForm y limpieza de gráficos.
lastmod: "2026-09-03"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Use operadores PDF de bajo nivel para el control de flujos de contenido en Java
Abstract: Este artículo explica cómo trabajar con operadores PDF de bajo nivel en Aspose.PDF for Java. Aprende cómo colocar imágenes con precisión, dibujar contenido XForm reutilizable y eliminar operadores gráficos de las páginas PDF.
---
## Introducción a los operadores PDF y su uso

Un operador es una palabra clave PDF que especifica alguna acción que debe realizarse, como pintar una forma gráfica en la página. Una palabra clave de operador se distingue de un objeto con nombre por la ausencia de un carácter de barra inicial (2Fh). Los operadores solo tienen significado dentro del flujo de contenido.

Un flujo de contenido es un objeto de flujo PDF cuyos datos consisten en instrucciones que describen los elementos gráficos que se pintarán en una página. Se pueden encontrar más detalles sobre los operadores PDF en el [PDF specification](https://opensource.adobe.com/dc-acrobat-sdk-docs/).

Utilice esta página cuando necesite control directo sobre un flujo de contenido PDF en Java, como colocar una imagen con matemáticas de matriz explícitas, reutilizar el mismo gráfico varias veces mediante un XForm, o eliminar instrucciones de dibujo de bajo nivel de una página.

## Agregar una imagen con operadores PDF

Utilice operadores de bajo nivel cuando la ubicación de la imagen deba controlarse con precisión a nivel del flujo de contenido en lugar de mediante API de diseño de nivel superior.

1. Abrir el PDF de origen con [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) y obtener el objetivo [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
1. Agregue la secuencia de imagen de entrada a los recursos de la página y conserve el nombre del recurso devuelto.
1. Cree un [Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf/rectangle/) que define el área objetivo y construya un [Matrix](https://reference.aspose.com/pdf/java/com.aspose.pdf/matrix/) desde sus límites.
1. Usar [GSave](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/gsave/) para preservar el estado gráfico actual, [ConcatenateMatrix](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/concatenatematrix/) para posicionar la imagen, [Do](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/do/) pintarlo, y [GRestore](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/grestore/) restaurar el estado anterior.
1. Guarde el documento PDF actualizado.

```java
public static void addImageUsingPdfOperators(Path inputFile, Path imageFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString());
         InputStream imageStream = Files.newInputStream(imageFile)) {
        Page page = document.getPages().get_Item(1);
        String imageName = page.getResources().getImages().add(imageStream);

        Rectangle rectangle = new Rectangle(100, 100, 200, 200, true);
        Matrix matrix = new Matrix(new double[]{
                rectangle.getURX() - rectangle.getLLX(),
                0,
                0,
                rectangle.getURY() - rectangle.getLLY(),
                rectangle.getLLX(),
                rectangle.getLLY()
        });

        page.getContents().add(new GSave());
        page.getContents().add(new ConcatenateMatrix(matrix));
        page.getContents().add(new Do(imageName));
        page.getContents().add(new GRestore());
        document.save(outputFile.toString());
    }
    System.out.println("Image added with PDF operators to " + outputFile);
}
```

## Dibujar contenido XForm reutilizable en una página

Utilice este enfoque cuando la misma imagen o gráfico debe renderizarse más de una vez sin duplicar el recurso en el archivo PDF.

1. Abrir el PDF de origen con [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/), obtener el objetivo [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/), y acceda a su [OperatorCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/operatorcollection/).
1. Envuelve el contenido de la página existente con [GSave](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/gsave/) y [GRestore](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/grestore/) para que las transformaciones posteriores no se filtren al flujo de contenido original.
1. Crear un [XForm](https://reference.aspose.com/pdf/java/com.aspose.pdf/xform/) recurso, agregue la imagen a los recursos del formulario, y use [ConcatenateMatrix](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/concatenatematrix/) más [Do](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/do/) para dibujar la imagen dentro del formulario.
1. Coloque el mismo formulario en múltiples coordenadas de página añadiendo una matriz de translación y ejecutando el nombre del formulario con el `Do` operador.
1. Restaure el estado gráfico y guarde el PDF de salida.

```java
public static void drawXFormOnPage(Path inputFile, Path imageFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString());
         InputStream imageStream = Files.newInputStream(imageFile)) {
        Page page = document.getPages().get_Item(1);
        OperatorCollection pageContents = page.getContents();

        pageContents.insert(1, new GSave());
        pageContents.add(new GRestore());
        pageContents.add(new GSave());

        XForm form = XForm.createNewForm(page, document);
        page.getResources().getForms().add(form);

        form.getContents().add(new GSave());
        form.getContents().add(new ConcatenateMatrix(200, 0, 0, 200, 0, 0));
        String imageName = form.getResources().getImages().add(imageStream);
        form.getContents().add(new Do(imageName));
        form.getContents().add(new GRestore());

        addFormAt(pageContents, form.getName(), 100, 500);
        addFormAt(pageContents, form.getName(), 100, 300);

        pageContents.add(new GRestore());
        document.save(outputFile.toString());
    }
    System.out.println("XForm drawn on page in " + outputFile);
}

private static void addFormAt(OperatorCollection pageContents, String formName, double x, double y) {
    pageContents.add(new GSave());
    pageContents.add(new ConcatenateMatrix(1, 0, 0, 1, x, y));
    pageContents.add(new Do(formName));
    pageContents.add(new GRestore());
}
```

## Eliminar operadores gráficos de una página

Utilice este ejemplo cuando una página contenga operadores de dibujo vectorial que deben eliminarse directamente del flujo de contenido.

1. Abrir el PDF de origen con [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) y obtener el objetivo [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
1. Iterar a través de los operadores de contenido de la página y recopilar instancias de [Stroke](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/stroke/), [ClosePathStroke](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/closepathstroke/), y [Fill](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/fill/).
1. Eliminar los operadores recopilados del contenido de la página y guardar el PDF actualizado.

Esta técnica elimina solo las instrucciones de dibujo dirigidas. Si la página también contiene etiquetas de texto relacionadas u otros operadores no gráficos, esos elementos permanecen en el flujo de contenido y pueden requerir una pasada de limpieza separada.

```java
public static void removeGraphicsObjects(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page page = document.getPages().get_Item(1);
        List<Operator> operatorsToRemove = new ArrayList<>();
        for (Object item : page.getContents()) {
            Operator operator = (Operator) item;
            if (operator instanceof Stroke || operator instanceof ClosePathStroke || operator instanceof Fill) {
                operatorsToRemove.add(operator);
            }
        }
        page.getContents().delete(operatorsToRemove);
        document.save(outputFile.toString());
    }
    System.out.println("Graphics operators removed in " + outputFile);
}
```

## Temas relacionados

- [Advanced PDF operations in Java](/pdf/es/java/advanced-operations/)
- [Work with images in PDF using Java](/pdf/es/java/working-with-images/)
- [Work with PDF pages in Java](/pdf/es/java/working-with-pages/)
- [Work with Vector Graphics in Java](/pdf/es/java/working-with-vector-graphics/)
