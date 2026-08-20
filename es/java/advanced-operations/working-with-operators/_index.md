---
title: Trabajar con operadores de PDF en Java
linktitle: Trabajar con operadores
type: docs
weight: 90
url: /java/working-with-operators/
description: Aprenda a utilizar operadores PDF de bajo nivel en Java para la manipulación de flujos de contenido, colocación de imágenes, reutilización de XForm y limpieza de gráficos.
lastmod: "2026-06-25"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Utilice operadores PDF de bajo nivel para controlar el flujo de contenido en Java
Abstract: Este artículo explica cómo trabajar con operadores de PDF de bajo nivel en Aspose.PDF para Java. Aprenda a colocar imágenes con precisión, dibujar contenido XForm reutilizable y eliminar operadores gráficos de páginas PDF.
---
## Introducción a los operadores PDF y su uso



Un operador es una palabra clave de PDF que especifica alguna acción que se realizará, como pintar una forma gráfica en la página. Una palabra clave de operador se distingue de un objeto con nombre por la ausencia de un carácter sólido inicial (2Fh). Los operadores sólo son significativos dentro del flujo de contenido.



Un flujo de contenido es un objeto de flujo PDF cuyos datos consisten en instrucciones que describen los elementos gráficos que se pintarán en una página. Puede encontrar más detalles sobre los operadores de PDF en la [especificación de PDF](https://opensource.adobe.com/dc-acrobat-sdk-docs/).



Utilice esta página cuando necesite control directo sobre un flujo de contenido PDF en Java, como colocar una imagen con matemáticas matriciales explícitas, reutilizar el mismo gráfico varias veces a través de un XForm o eliminar instrucciones de dibujo de bajo nivel de una página.


## 
Agregar una imagen con operadores de PDF

Utilice operadores de bajo nivel cuando la ubicación de la imagen deba controlarse con precisión en el nivel del flujo de contenido en lugar de a través de API de diseño de nivel superior.


1. 
Abra el PDF de origen con [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) y obtenga la [Página] de destino(https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).

1. 
Agregue la secuencia de imágenes de entrada a los recursos de la página y mantenga el nombre del recurso devuelto.

1. 
Cree un [Rectángulo](https://reference.aspose.com/pdf/java/com.aspose.pdf/rectangle/) que defina el área objetivo y construya una [Matriz](https://reference.aspose.com/pdf/java/com.aspose.pdf/matrix/) a partir de sus límites.

1. 
Utilice [GSave](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/gsave/) para preservar el estado actual de los gráficos, [ConcatenateMatrix](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/concatenatematrix/) para colocar la imagen, [Do](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/do/) para pintarla y [GRestore](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/grestore/) para restaurar el estado anterior.
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

## 
Dibujar contenido XForm reutilizable en una página



Utilice este enfoque cuando la misma imagen o gráfico deba renderizarse más de una vez sin duplicar el recurso en el archivo PDF.


1. 
Abra el PDF de origen con [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/), obtenga la [Página] de destino(https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) y acceda a su [OperatorCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/operatorcollection/).

1. 
Envuelva el contenido de la página existente con [GSave](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/gsave/) y [GRestore](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/grestore/) para que las transformaciones posteriores no se filtren en el flujo de contenido original.
1. Cree un recurso [XForm](https://reference.aspose.com/pdf/java/com.aspose.pdf/xform/), agregue la imagen a los recursos del formulario y use [ConcatenateMatrix](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/concatenatematrix/) más [Do](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/do/) para dibujar la imagen dentro del formulario.

1. 
Coloque el mismo formulario en varias coordenadas de página agregando una matriz de traducción y ejecutando el nombre del formulario con el operador `Do`.

1. 
Restaure el estado de los gráficos y guarde el PDF de salida.


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

## 
Eliminar operadores gráficos de una página



Utilice este ejemplo cuando una página contenga operadores de dibujo vectorial que deban eliminarse directamente del flujo de contenido.

1. Abra el PDF de origen con [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) y obtenga la [Página] de destino(https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).

1. 
Itere a través de los operadores de contenido de la página y recopile instancias de [Stroke](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/stroke/), [ClosePathStroke](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/closepathstroke/) y [Fill](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/fill/).

1. 
Elimine los operadores recopilados del contenido de la página y guarde el PDF actualizado.



Esta técnica elimina únicamente las instrucciones de dibujo específicas. Si la página también contiene etiquetas de texto relacionadas u otros operadores no gráficos, esos elementos permanecen en el flujo de contenido y es posible que necesiten una pasada de limpieza por separado.


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

## 
Temas relacionados

- [Operaciones avanzadas de PDF en Java](/pdf/java/advanced-operations/)

- 
[Trabajar con imágenes en PDF usando Java](/pdf/java/working-with-images/)

- 
[Trabajar con páginas PDF en Java](/pdf/java/working-with-pages/)

- 
[Trabajar con gráficos vectoriales en Java](/pdf/java/working-with-vector-graphics/)
