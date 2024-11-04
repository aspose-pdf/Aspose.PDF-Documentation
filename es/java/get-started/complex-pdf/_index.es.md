---
title: Creación de un PDF complejo
linktitle: Creación de un PDF complejo
type: docs
weight: 60
url: /java/complex-pdf-example/
description: Aspose.PDF para Java te permite crear documentos más complejos que contienen imágenes, fragmentos de texto y tablas en un solo documento.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

El ejemplo de [Hola, Mundo](/pdf/java/hello-world-example/) mostró pasos simples para crear un documento PDF usando Java y Aspose.PDF. En este artículo, veremos cómo crear un documento más complejo con Java y Aspose.PDF para Java. Como ejemplo, tomaremos un documento de una empresa ficticia que opera servicios de ferry de pasajeros.  
Nuestro documento contendrá una imagen, dos fragmentos de texto (encabezado y párrafo), y una tabla. Para construir tal documento, utilizaremos un enfoque basado en DOM. Puedes leer más en la sección [Fundamentos de la API DOM](/pdf/java/basics-of-dom-api/).

Si creamos un documento desde cero, necesitamos seguir ciertos pasos:

1. Instanciar un objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document). En este paso crearemos un documento PDF vacío con algunos metadatos pero sin páginas.
1. Agregar una [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page) al objeto del documento. Así que ahora nuestro documento tendrá una página.
1. Agregar una [Image](https://reference.aspose.com/pdf/java/com.aspose.pdf/image). Es una operación compleja basada en acciones de bajo nivel con operadores PDF.
    - Cargar imagen desde el flujo
    - Agregar imagen a la colección de Imágenes de Recursos de la Página
    - Usar el operador GSave: este operador guarda el estado gráfico actual.
    - Crear un objeto [Matrix](https://reference.aspose.com/pdf/java/com.aspose.pdf/matrix/).
    - Usar el operador ConcatenateMatrix: define cómo debe colocarse la imagen.
    - Usar el operador Do: este operador dibuja la imagen.
    - Usar el operador GRestore: este operador restaura el estado gráfico.

1. Cree un [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFragment) para el encabezado. Para el encabezado usaremos la fuente Arial con tamaño de fuente 24pt y alineación centrada.
1. Agregue el encabezado a los [Paragraphs](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page#getParagraphs--).
1. Cree un [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFragment) para la descripción. Para la descripción usaremos la fuente Arial con tamaño de fuente 24pt y alineación centrada.
1. Agregue (descripción) a los párrafos de la página.
1. Cree una tabla, agregue propiedades de tabla.
1. Agregue (tabla) a los [Paragraphs](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page#getParagraphs--).
1. Guarde un documento "Complex.pdf".

```java
package com.aspose.pdf.examples;

/**
 * Ejemplo Complejo
 */

import java.io.FileNotFoundException;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.time.Duration;
import java.time.LocalTime;

import com.aspose.pdf.*;
import com.aspose.pdf.operators.ConcatenateMatrix;
import com.aspose.pdf.operators.Do;
import com.aspose.pdf.operators.GRestore;
import com.aspose.pdf.operators.GSave;

public final class ComplexExample {

    private ComplexExample() {
    }

    private static Path _dataDir = Paths.get("/home/admin1/pdf-examples/");

    public static void main(String[] args) throws FileNotFoundException {
        // Inicializar objeto documento
        Document document = new Document();
        // Agregar página
        Page page = document.getPages().add();

        // -------------------------------------------------------------
        // Agregar imagen
        Path imageFileName = Paths.get(_dataDir.toString(),"logo.png");
        java.io.FileInputStream imageStream = new java.io.FileInputStream(new java.io.File(imageFileName.toString()));
        // Agregar imagen a la colección de Imágenes de los Recursos de Página
        page.getResources().getImages().add(imageStream);

        // Usando el operador GSave: este operador guarda el estado gráfico actual
        page.getContents().add(new GSave());
        Rectangle _logoPlaceHolder = new Rectangle(20, 730, 120, 830);

        // Crear objeto Matrix
        Matrix matrix = new Matrix(new double[] {
            _logoPlaceHolder.getURX() - _logoPlaceHolder.getLLX(), 0, 0,
            _logoPlaceHolder.getURY() - _logoPlaceHolder.getLLY(),
            _logoPlaceHolder.getLLX(), _logoPlaceHolder.getLLY() });

        // Usando el operador ConcatenateMatrix (concatenar matriz): define cómo debe colocarse la imagen
        page.getContents().add(new ConcatenateMatrix(matrix));
        XImage ximage = page.getResources().getImages().get_Item(page.getResources().getImages().size());
        // Usando el operador Do: este operador dibuja la imagen
        page.getContents().add(new Do(ximage.getName()));
        // Usando el operador GRestore: este operador restaura el estado gráfico
        page.getContents().add(new GRestore());

        // -------------------------------------------------------------
        // Agregar Encabezado
        TextFragment header = new TextFragment("Nuevas rutas de ferry en otoño de 2020");
        header.getTextState().setFont(FontRepository.findFont("Arial"));
        header.getTextState().setFontSize(24);
        header.setHorizontalAlignment (HorizontalAlignment.Center);
        header.setPosition(new Position(130, 720));
        page.getParagraphs().add(header);

        // Agregar descripción
        String descriptionText = "Los visitantes deben comprar boletos en línea y los boletos están limitados a 5,000 por día. El servicio de ferry está operando a media capacidad y con un horario reducido. Espere filas.";
        TextFragment description = new TextFragment(descriptionText);
        description.getTextState().setFont(FontRepository.findFont("Times New Roman"));
        description.getTextState().setFontSize(14);
        description.setHorizontalAlignment(HorizontalAlignment.Left);
        page.getParagraphs().add(description);


        // Agregar tabla
        Table table = new Table();
        table.setColumnWidths("200");
        table.setBorder(new BorderInfo(BorderSide.Box, 1f, Color.getDarkSlateGray()));
        table.setDefaultCellBorder(new BorderInfo(BorderSide.Box, 0.5f, Color.getBlack()));
        table.getMargin().setBottom(10);
        table.getDefaultCellTextState().setFont(FontRepository.findFont("Helvetica"));

        Row headerRow = table.getRows().add();
        headerRow.getCells().add("Sale de la ciudad");
        headerRow.getCells().add("Sale de la isla");

        for (Cell headerRowCell : headerRow.getCells())
        {
            headerRowCell.setBackgroundColor(Color.getGray());
            headerRowCell.getDefaultCellTextState().setForegroundColor(Color.getWhiteSmoke());
        }

        LocalTime time = LocalTime.of(6,0);
        Duration incTime = Duration.ofMinutes(30);

        for (int i = 0; i < 10; i++)
        {
            Row dataRow = table.getRows().add();
            dataRow.getCells().add(time.toString());
            time=time.plus(incTime);
            dataRow.getCells().add(time.toString());
        }

        page.getParagraphs().add(table);

        document.save(Paths.get(_dataDir.toString(), "Complex.pdf").toString());
    }

}
```