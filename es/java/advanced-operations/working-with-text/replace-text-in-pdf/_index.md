---
title: Reemplazar Texto en PDF
linktitle: Reemplazar Texto en PDF
type: docs
weight: 40
url: /es/java/replace-text-in-a-pdf-document/
description: Aprende más sobre varias maneras de reemplazar y eliminar texto de un PDF. Aspose.PDF permite reemplazar texto en una región particular o con una expresión regular.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Reemplazar Texto en todas las páginas del documento PDF

{{% alert color="primary" %}}

Puede intentar buscar y reemplazar el texto en el documento usando Aspose.PDF y obtener los resultados en línea en este [enlace](https://products.aspose.app/pdf/redaction)

{{% /alert %}}

Para reemplazar texto en todas las páginas de un documento PDF usando [Aspose.PDF for Java](https://products.aspose.com/pdf/java):

1. Primero use [TextFragmentAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFragmentAbsorber) para encontrar la frase particular que se va a reemplazar.

1. Luego, revise todos los [TextFragments](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFragmentAbsorber#getTextFragments--) para reemplazar el texto y cambiar cualquier otro atributo.
1. Finalmente, guarde el PDF de salida utilizando el método [save](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#save--) de la clase Document.

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;

public class ExampleReplaceText {
    
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";
    public static void ReplaceTextOnAllPages() {
        Document pdfDocument = new Document(_dataDir+"sample.pdf");

        // Crear objeto TextAbsorber para encontrar todas las instancias de la frase de búsqueda de entrada
        TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("Web");
        
        // Aceptar el absorber para la primera página del documento
        pdfDocument.getPages().accept(textFragmentAbsorber);
        
        // Obtener los fragmentos de texto extraídos en la colección
        TextFragmentCollection textFragmentCollection = textFragmentAbsorber.getTextFragments();
        
        // Recorrer los fragmentos
        for (TextFragment textFragment : (Iterable<TextFragment>) textFragmentCollection) {
            // Actualizar texto y otras propiedades
            textFragment.setText("World Wide Web");
            textFragment.getTextState().setFont(FontRepository.findFont("Verdana"));
            textFragment.getTextState().setFontSize(12);
            textFragment.getTextState().setForegroundColor(Color.getBlue());
            textFragment.getTextState().setBackgroundColor(Color.getGray());
        }
        // Guardar el archivo PDF actualizado
        pdfDocument.save(_dataDir+"Updated_Text.pdf");
    }
}
```


## Reemplazar texto en una región particular de la página

Para reemplazar texto en una región particular de la página, primero necesitamos instanciar el objeto TextFragmentAbsorber, especificar la región de la página usando [TextSearchOptions.setRectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextSearchOptions#setRectangle-com.aspose.pdf.Rectangle-) y luego iterar a través de todos los TextFragments para reemplazar el texto. Una vez que estas operaciones se completen, solo necesitamos guardar el PDF de salida usando el método save del objeto Document.

El siguiente fragmento de código te muestra cómo reemplazar texto en todas las páginas del documento PDF.

```java
 public static void ReplaceTextInParticularRegion(){
    // cargar archivo PDF
    Document pdfDocument = new Document(_dataDir+"sample.pdf");

    // instanciar objeto TextFragment Absorber
    TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("PDF");

    // buscar texto dentro de los límites de la página
    textFragmentAbsorber.getTextSearchOptions().setLimitToPageBounds(true);

    // especificar la región de la página para las opciones de búsqueda de texto
    textFragmentAbsorber.getTextSearchOptions().setRectangle(new Rectangle(100, 700, 400, 770));

    // buscar texto desde la primera página del archivo PDF
    pdfDocument.getPages().get_Item(1).accept(textFragmentAbsorber);

    // iterar a través de cada TextFragment
    for(TextFragment tf : textFragmentAbsorber.getTextFragments())
    {
        // reemplazar texto con "---"
        tf.setText("---");
    }

    // Guardar el archivo PDF actualizado
    pdfDocument.save(_dataDir+"Updated_Text.pdf");
}
```


## Reemplazar Texto Basado en una Expresión Regular

Si deseas reemplazar algunas frases basadas en una expresión regular, primero necesitas encontrar todas las frases que coincidan con esa expresión regular en particular usando TextFragmentAbsorber. Tendrás que pasar la expresión regular como un parámetro al constructor de TextFragmentAbsorber. También necesitas crear un objeto TextSearchOptions que especifique si se está utilizando la expresión regular o no. Una vez que obtengas las frases coincidentes en TextFragments, necesitas iterar a través de todas ellas y actualizar según sea necesario. Finalmente, necesitas guardar el PDF actualizado utilizando el método Save del objeto Document.

El siguiente fragmento de código te muestra cómo reemplazar texto basado en una expresión regular.

```java
public static void ReplaceTextWithRegularExpression() {
    // cargar archivo PDF
    Document pdfDocument = new Document(_dataDir + "sample.pdf");
    // Crear objeto TextAbsorber para encontrar todas las instancias de la frase de búsqueda de entrada
    TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("\\d{4}-\\d{4}"); 
    // como 1999-2000

    // Establecer opción de búsqueda de texto para especificar el uso de expresión regular
    TextSearchOptions textSearchOptions = new TextSearchOptions(true);
    textFragmentAbsorber.setTextSearchOptions(textSearchOptions);

    // Aceptar el absorbedor para la primera página del documento
    pdfDocument.getPages().accept(textFragmentAbsorber);

    // Obtener los fragmentos de texto extraídos en la colección
    TextFragmentCollection textFragmentCollection = textFragmentAbsorber.getTextFragments();

    // Iterar a través de los fragmentos
    for (TextFragment textFragment : (Iterable<TextFragment>) textFragmentCollection) {
        // Actualizar texto y otras propiedades
        textFragment.setText("ABCD-EFGH");
        textFragment.getTextState().setFont(FontRepository.findFont("Verdana"));
        textFragment.getTextState().setFontSize(12);
        textFragment.getTextState().setForegroundColor(Color.getBlue());
        textFragment.getTextState().setBackgroundColor(Color.getGray());
    }

    // Guardar el archivo PDF actualizado
    pdfDocument.save(_dataDir + "Updated_Text.pdf");
}
```


## Reemplazar fuentes en un archivo PDF existente

Aspose.PDF para Java admite la capacidad de reemplazar texto en un documento PDF. Sin embargo, a veces tienes el requisito de reemplazar solo la fuente que se utiliza dentro del documento PDF. Así que en lugar de reemplazar el texto, solo se reemplaza la fuente utilizada. Una de las sobrecargas del constructor de TextFragmentAbsorber acepta un objeto TextEditOptions como argumento y podemos usar el valor RemoveUnusedFonts de la enumeración TextEditOptions.FontReplace para cumplir con nuestros requisitos.

El siguiente fragmento de código muestra cómo reemplazar la fuente dentro del documento PDF.

```java
public static void ReplaceFonts() {
    // Instanciar objeto Document
    Document pdfDocument = new Document(_dataDir + "sample.pdf");

    // Buscar fragmentos de texto y establecer opción de edición como eliminar fuentes no usadas
    TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber(
            new TextEditOptions(TextEditOptions.FontReplace.RemoveUnusedFonts));

    // Aceptar el absorbedor para todas las páginas del documento
    pdfDocument.getPages().accept(textFragmentAbsorber);

    // recorrer todos los TextFragments
    TextFragmentCollection textFragmentCollection = textFragmentAbsorber.getTextFragments();
    for (TextFragment textFragment : (Iterable<TextFragment>) textFragmentCollection)
    {
        String fontName = textFragment.getTextState().getFont().getFontName();
        // si el nombre de la fuente es ArialMT, reemplazar el nombre de la fuente con Arial
        if (fontName.equals("ArialMT")) {
            textFragment.getTextState().setFont(FontRepository.findFont("Arial"));
        }
    }

    // Guardar el archivo PDF actualizado
    pdfDocument.save(_dataDir + "Updated_Text.pdf");
}
```


### Usar Fuente No Inglesa (Japonesa) Al Reemplazar Texto

El siguiente fragmento de código muestra cómo reemplazar texto con caracteres japoneses. Tenga en cuenta que para agregar texto japonés, necesita usar una fuente que soporte caracteres japoneses (por ejemplo, MSGothic).

```java
public static void UseNonEnglishFontWhenReplacingText() {

    // Instanciar objeto Documento
    Document pdfDocument = new Document(_dataDir + "sample.pdf");

    // Vamos a cambiar cada palabra "page" por algún texto en japonés con una fuente específica
    // TakaoMincho que podría estar instalada en el SO
    // Además, puede ser otra fuente que soporte ideogramas
    TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("page");

    // Crear instancia de opciones de búsqueda de texto
    TextSearchOptions searchOptions = new TextSearchOptions(true);
    textFragmentAbsorber.setTextSearchOptions(searchOptions);

    // Aceptar el absorbedor para todas las páginas del documento
    pdfDocument.getPages().accept(textFragmentAbsorber);

    // Obtener los fragmentos de texto extraídos en una colección
    TextFragmentCollection textFragmentCollection = textFragmentAbsorber.getTextFragments();
    
    // Recorrer los fragmentos
    for (TextFragment textFragment : (Iterable<TextFragment>) textFragmentCollection) {
        // Actualizar texto y otras propiedades
        textFragment.setText("ファイル");
        textFragment.getTextState().setFont(FontRepository.findFont("MSGothic"));
        textFragment.getTextState().setFontSize(12);
        textFragment.getTextState().setForegroundColor(Color.getBlue());
        textFragment.getTextState().setBackgroundColor(Color.getGray());
    }
    // Guardar el documento actualizado
    pdfDocument.save(_dataDir + "Japanese_Text.pdf");
}
```


## El Reemplazo de Texto debería reordenar automáticamente los Contenidos de la Página

Aspose.PDF para Java admite la función de buscar y reemplazar texto dentro del archivo PDF. Sin embargo, recientemente algunos clientes encontraron problemas durante el reemplazo de texto cuando un TextFragment particular se reemplaza con contenidos más pequeños y se muestran algunos espacios adicionales en el PDF resultante o en caso de que el TextFragment se reemplace con una cadena más larga, entonces las palabras se superponen con los contenidos existentes de la página. Por lo tanto, se requería introducir un mecanismo que, una vez que el texto dentro de un documento PDF sea reemplazado, los contenidos deben ser reordenados.

Con el fin de abordar los escenarios mencionados, Aspose.PDF para Java ha sido mejorado para que no aparezcan tales problemas al reemplazar texto dentro del archivo PDF. El siguiente fragmento de código muestra cómo reemplazar texto dentro de un archivo PDF y los contenidos de la página deben ser reordenados automáticamente.

```java
public static void RearrangeContent() {
    // Cargar archivo PDF de origen
    Document pdfDocument = new Document(_dataDir + "sample.pdf");

    // Crear objeto TextFragment Absorber con expresión regular
    TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("[PDF,Web]");

    TextSearchOptions textSearchOptions = new TextSearchOptions(true);
    textFragmentAbsorber.setTextSearchOptions(textSearchOptions);
    
    //También puede especificar la opción ReplaceAdjustment.WholeWordsHyphenation para ajustar el texto en la siguiente o actual línea 
    //si la línea actual se vuelve demasiado larga o corta después del reemplazo:
    //textFragmentAbsorber.getTextReplaceOptions().setReplaceAdjustmentAction(TextReplaceOptions.ReplaceAdjustment.WholeWordsHyphenation);

    // Aceptar el absorbedor para todas las páginas del documento
    pdfDocument.getPages().accept(textFragmentAbsorber);

    // Obtener los fragmentos de texto extraídos en la colección
    TextFragmentCollection textFragmentCollection = textFragmentAbsorber.getTextFragments();

    // Reemplazar cada TextFragment
    for (TextFragment textFragment : (Iterable<TextFragment>) textFragmentCollection) {
        // Establecer la fuente del fragmento de texto que se está reemplazando
        textFragment.getTextState().setFont(FontRepository.findFont("Arial"));
        // Establecer tamaño de fuente
        textFragment.getTextState().setFontSize(10);
        textFragment.getTextState().setForegroundColor(Color.getBlue());
        textFragment.getTextState().setBackgroundColor(Color.getGray());
        // Reemplazar el texto con una cadena más grande que el marcador de posición
        textFragment.setText("Esta es una cadena más grande para la prueba de esta función");
    }
    // Guardar PDF resultante
    pdfDocument.save(_dataDir + "RearrangeContentsUsingTextReplacement_out.pdf");
}
```


## Renderización de Símbolos Reemplazables durante la creación de PDF

Los símbolos reemplazables son símbolos especiales en una cadena de texto que pueden ser reemplazados con contenido correspondiente en tiempo de ejecución. Los símbolos reemplazables actualmente soportados por el nuevo Modelo de Objeto de Documento del espacio de nombres Aspose.PDF son `$P`, `$p,` `\n`, `\r`. El `$p` y `$P` se utilizan para manejar la numeración de páginas en tiempo de ejecución. `$p` se reemplaza con el número de la página donde la clase de Párrafo actual está. `$P` se reemplaza con el número total de páginas en el documento. Al agregar [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/TeXFragment) a la colección de párrafos de documentos PDF, no soporta el salto de línea dentro del texto. Sin embargo, para agregar texto con un salto de línea, por favor use [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/TeXFragment) con [TextParagraph](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextParagraph):

- use "\r\n" o Environment.NewLine en TextFragment en lugar de un solo "\n";
- cree un objeto TextParagraph.
 Se añadirá texto con división de líneas;
- añadir el TextFragment con TextParagraph.AppendLine;
- añadir el TextParagraph con TextBuilder.AppendParagraph.

```java
public static void RenderingReplaceableSymbols() {
    // cargar archivo PDF
    Document pdfDocument = new Document(_dataDir + "sample.pdf");
    Page page = pdfDocument.getPages().add();

    // Inicializar nuevo TextFragment con texto que contiene los marcadores de nueva línea requeridos
    TextFragment textFragment = new TextFragment("Applicant Name: " + System.lineSeparator() + " Joe Smoe");

    // Establecer propiedades del fragmento de texto si es necesario
    textFragment.getTextState().setFontSize(12);
    textFragment.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));
    textFragment.getTextState().setBackgroundColor(Color.getLightGray());
    textFragment.getTextState().setForegroundColor(Color.getRed());

    // Crear objeto TextParagraph
    TextParagraph par = new TextParagraph();

    // Añadir nuevo TextFragment al párrafo
    par.appendLine(textFragment);

    // Establecer la posición del párrafo
    par.setPosition (new Position(100, 600));

    // Crear objeto TextBuilder
    TextBuilder textBuilder = new TextBuilder(page);
    // Añadir el TextParagraph usando TextBuilder
    textBuilder.appendParagraph(par);

    _dataDir = _dataDir + "RenderingReplaceableSymbols_out.pdf";
    pdfDocument.save(_dataDir);
}
```

## Símbolos reemplazables en el área de Encabezado/Pie de página

Los símbolos reemplazables también se pueden colocar dentro de la sección de Encabezado/Pie de página de un archivo PDF. Por favor, revise el siguiente fragmento de código para obtener detalles sobre cómo agregar un símbolo reemplazable en la sección de pie de página.

```java
public static void ReplaceableSymbolsInHeaderFooterArea() {
    Document doc = new Document();
    Page page = doc.getPages().add();

    MarginInfo marginInfo = new MarginInfo();
    marginInfo.setTop(90);
    marginInfo.setBottom(50);
    marginInfo.setLeft(50);
    marginInfo.setRight(50);

    // Asignar la instancia de marginInfo a la propiedad Margin de sec1.PageInfo
    page.getPageInfo().setMargin(marginInfo);

    HeaderFooter hfFirst = new HeaderFooter();
    page.setHeader(hfFirst);
    hfFirst.getMargin().setLeft(50);
    hfFirst.getMargin().setRight(50);

    // Instanciar un párrafo de texto que almacenará el contenido para mostrar como encabezado
    TextFragment t1 = new TextFragment("título del informe");
    t1.getTextState().setFont(FontRepository.findFont("Arial"));
    t1.getTextState().setFontSize(16);
    t1.getTextState().setForegroundColor(Color.getBlack());
    t1.getTextState().setFontStyle(FontStyles.Bold);
    t1.getTextState().setHorizontalAlignment(HorizontalAlignment.Center);
    t1.getTextState().setLineSpacing(5f);
    hfFirst.getParagraphs().add(t1);

    TextFragment t2 = new TextFragment("Nombre_Informe");
    t2.getTextState().setFont(FontRepository.findFont("Arial"));
    t2.getTextState().setForegroundColor(Color.getBlack());
    t2.getTextState().setHorizontalAlignment(HorizontalAlignment.Center);
    t2.getTextState().setLineSpacing(5f);
    t2.getTextState().setFontSize(12);
    hfFirst.getParagraphs().add(t2);

    // Crear un objeto HeaderFooter para la sección
    HeaderFooter hfFoot = new HeaderFooter();

    // Configurar el objeto HeaderFooter para pie de página par e impar
    page.setFooter(hfFoot);
    hfFoot.getMargin().setLeft(50);
    hfFoot.getMargin().setRight(50);

    // Agregar un párrafo de texto que contenga el número de página actual del total de páginas
    TextFragment t3 = new TextFragment("Generado en la fecha de prueba");
    TextFragment t4 = new TextFragment("nombre del informe ");
    TextFragment t5 = new TextFragment("Página $p de $P");

    // Instanciar un objeto de tabla
    Table tab2 = new Table();

    // Agregar la tabla en la colección de párrafos de la sección deseada
    hfFoot.getParagraphs().add(tab2);

    // Establecer anchos de columna de la tabla
    tab2.setColumnWidths("165 172 165");

    // Crear filas en la tabla y luego celdas en las filas
    Row row3 = tab2.getRows().add();

    row3.getCells().add();
    row3.getCells().add();
    row3.getCells().add();

    // Establecer la alineación vertical del texto como alineado al centro
    row3.getCells().get_Item(0).setAlignment(HorizontalAlignment.Left);
    row3.getCells().get_Item(1).setAlignment(HorizontalAlignment.Center);
    row3.getCells().get_Item(2).setAlignment(HorizontalAlignment.Right);

    row3.getCells().get_Item(0).getParagraphs().add(t3);
    row3.getCells().get_Item(1).getParagraphs().add(t4);
    row3.getCells().get_Item(2).getParagraphs().add(t5);

    Table table = new Table();

    table.setColumnWidths("33% 33% 34%");
    table.setDefaultCellPadding(new MarginInfo());
    table.getDefaultCellPadding().setTop(10);
    table.getDefaultCellPadding().setBottom(10);

    // Agregar la tabla en la colección de párrafos de la sección deseada
    page.getParagraphs().add(table);

    // Establecer borde de celda predeterminado usando un objeto BorderInfo
    table.setDefaultCellBorder(new BorderInfo(BorderSide.All, 0.1f));

    // Establecer borde de tabla usando otro objeto personalizado BorderInfo
    table.setBorder(new BorderInfo(BorderSide.All, 1f));

    table.setRepeatingRowsCount(1);

    // Crear filas en la tabla y luego celdas en las filas
    Row row1 = table.getRows().add();

    row1.getCells().add("col1");
    row1.getCells().add("col2");
    row1.getCells().add("col3");
    String CRLF = "\r\n";

    for (int i = 0; i <= 10; i++) {
        Row row = table.getRows().add();
        row.setRowBroken(true);
        for (int c = 0; c <= 2; c++) {
            Cell c1;
            if (c == 2)
                c1 = row.getCells().add(
                        "Aspose.Total for Java es una compilación de cada componente Java ofrecido por Aspose. Se compila en un"
                                + CRLF
                                + "base diaria para asegurar que contiene las versiones más actualizadas de cada uno de nuestros componentes Java. "
                                + CRLF
                                + "base diaria para asegurar que contiene las versiones más actualizadas de cada uno de nuestros componentes Java. "
                                + CRLF
                                + "Usando Aspose.Total para Java, los desarrolladores pueden crear una amplia gama de aplicaciones.");
            else
                c1 = row.getCells().add("elemento1" + c);
            c1.setMargin(new MarginInfo());
            c1.getMargin().setLeft(30);
            c1.getMargin().setTop(10);
            c1.getMargin().setBottom(10);
        }
    }

    _dataDir = _dataDir + "ReplaceableSymbolsInHeaderFooter_out.pdf";
    doc.save(_dataDir);
}
```


## Eliminar Todo el Texto del Documento PDF

### Eliminar Todo el Texto usando Operadores

En algunas operaciones de texto, necesitas eliminar todo el texto de un documento PDF y para eso, usualmente necesitas establecer el texto encontrado como un valor de cadena vacía. El punto es que cambiar el texto para una multitud de fragmentos de texto invoca una serie de operaciones de comprobación y ajuste de posición de texto. Son esenciales en los escenarios de edición de texto. La dificultad es que no puedes determinar cuántos fragmentos de texto serán eliminados en el escenario donde son procesados en un bucle.

Por lo tanto, recomendamos usar otro enfoque para el escenario de eliminar todo el texto de las páginas PDF. Por favor, considera el siguiente fragmento de código que funciona muy rápido.

```java
public static void RemoveAllTextUsingOperators() {
    // Abrir documento
    Document pdfDocument = new Document(_dataDir + "sample.pdf");

    // Recorrer todas las páginas del Documento PDF
    for (int i = 1; i <= pdfDocument.getPages().size(); i++) {
        Page page = pdfDocument.getPages().get_Item(i);
        OperatorSelector operatorSelector = new OperatorSelector(new com.aspose.pdf.operators.TextShowOperator());
        // Seleccionar todo el texto en la página
        page.getContents().accept(operatorSelector);
        // Eliminar todo el texto
        page.getContents().delete(operatorSelector.getSelected());
    }
    // Guardar el documento
    pdfDocument.save(_dataDir + "RemoveAllText_out.pdf");
}
```