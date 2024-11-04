---
title: Reemplazar Texto en PDF usando C++
linktitle: Reemplazar Texto en PDF
type: docs
weight: 40
url: /cpp/replace-text-in-pdf/
description: Aprende más sobre varias formas de reemplazar y eliminar texto de un PDF. Aspose.PDF permite reemplazar texto en una región particular o con una expresión regular.
lastmod: "2021-12-13"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

A veces surge la tarea de corregir o reemplazar texto en un documento PDF. Intentar hacerlo manualmente será una tarea desalentadora, así que aquí está la solución a ese problema.

Honestamente, editar un archivo PDF no es una tarea fácil. Así que, una situación donde necesites encontrar y reemplazar una palabra por otra mientras editas un archivo PDF, será muy difícil ya que te tomará mucho tiempo hacerlo. Además, puedes encontrarte con muchos problemas con tu resultado, como problemas de formato o fuentes rotas. Si deseas encontrar y reemplazar texto fácilmente en archivos PDF, te recomendamos que utilices el software de la biblioteca Aspose.Pdf, ya que hará el trabajo en minutos.

En este artículo, te mostraremos cómo encontrar y reemplazar texto exitosamente en tus archivos PDF usando Aspose.PDF para C++.

## Reemplazar texto en todas las páginas de un documento PDF

{{% alert color="primary" %}}

Puede intentar encontrar y reemplazar el texto en el documento usando Aspose.PDF y obtener los resultados en línea en este [enlace](https://products.aspose.app/pdf/redaction)

{{% /alert %}}

Para reemplazar texto en todas las páginas de un documento PDF, primero necesita usar TextFragmentAbsorber para encontrar la frase particular que desea reemplazar. Después de eso, debe pasar por todos los TextFragments para reemplazar el texto y cambiar cualquier otro atributo. Una vez hecho esto, solo necesita guardar el PDF de salida usando el método Save del objeto Document. El siguiente fragmento de código le muestra cómo reemplazar texto en todas las páginas de un documento PDF.

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void ReplaceTextOnAllPages() {

    String _dataDir("C:\\Samples\\");

    auto document = MakeObject<Document>(_dataDir + u"sample.pdf");

    // Crear objeto TextAbsorber para encontrar todas las instancias de la frase de búsqueda de entrada
    auto textFragmentAbsorber = MakeObject<TextFragmentAbsorber>("Web");

    // Aceptar el absorber para la primera página del documento
    document->get_Pages()->Accept(textFragmentAbsorber);

    // Obtener los fragmentos de texto extraídos en la colección
    auto textFragmentCollection = textFragmentAbsorber->get_TextFragments();

    // Recorrer los fragmentos
    for (auto textFragment : textFragmentCollection) {
        // Actualizar texto y otras propiedades
        textFragment->set_Text(u"World Wide Web");
        textFragment->get_TextState()->set_Font(FontRepository::FindFont(u"Verdana"));
        textFragment->get_TextState()->set_FontSize(12);
        textFragment->get_TextState()->set_ForegroundColor(Color::get_Blue());
        textFragment->get_TextState()->set_BackgroundColor(Color::get_Gray());
    }
    // Guardar el archivo PDF actualizado
    document->Save(_dataDir + u"Updated_Text.pdf");
}
```

## Reemplazar texto en una región específica de la página

Para reemplazar texto en una región específica de la página, primero necesitamos instanciar el objeto TextFragmentAbsorber, especificar la región de la página usando la propiedad TextSearchOptions.Rectangle y luego iterar a través de todos los TextFragments para reemplazar el texto. Una vez completadas estas operaciones, solo necesitamos guardar el PDF de salida usando el método Save del objeto Document. El siguiente fragmento de código te muestra cómo reemplazar texto en todas las páginas de un documento PDF.

```cpp
void ReplaceTextInParticularRegion() {

    String _dataDir("C:\\Samples\\");

    // cargar archivo PDF
    auto document = MakeObject<Document>(_dataDir + u"sample.pdf");

    // instanciar objeto TextFragment Absorber
    auto textFragmentAbsorber = MakeObject<TextFragmentAbsorber>("PDF");

    // buscar texto dentro del límite de la página
    textFragmentAbsorber->get_TextSearchOptions()->set_LimitToPageBounds(true);

    // especificar la región de la página para las opciones de búsqueda de texto
    textFragmentAbsorber->get_TextSearchOptions()->set_Rectangle(new Rectangle(100, 700, 400, 770));

    // buscar texto desde la primera página del archivo PDF
    document->get_Pages()->idx_get(1)->Accept(textFragmentAbsorber);

    // iterar a través de cada TextFragment
    for (auto tf : textFragmentAbsorber->get_TextFragments()) {
        // reemplazar texto con "---"
        tf->set_Text(u"---");
    }

    // Guardar el archivo PDF actualizado
    document->Save(_dataDir + u"Updated_Text.pdf");
}
```

## Reemplazar Texto Basado en una Expresión Regular

Si deseas reemplazar algunas frases basadas en una expresión regular, primero necesitas encontrar todas las frases que coincidan con esa expresión regular en particular usando TextFragmentAbsorber. Tendrás que pasar la expresión regular como un parámetro al constructor de TextFragmentAbsorber. También necesitas crear un objeto TextSearchOptions que especifique si se está utilizando la expresión regular o no. Una vez que obtengas las frases coincidentes en TextFragments, necesitas iterar a través de todas ellas y actualizar según sea necesario. Finalmente, necesitas guardar el PDF actualizado utilizando el método Save del objeto Document. El siguiente fragmento de código te muestra cómo reemplazar texto basado en una expresión regular.

```cpp
void ReplaceTextWithRegularExpression() {

    String _dataDir("C:\\Samples\\");

    // carga el archivo PDF
    auto document = MakeObject<Document>(_dataDir + u"Sample.pdf");
    // Crear objeto TextAbsorber para encontrar todas las instancias de la frase de búsqueda de entrada
    auto textFragmentAbsorber = MakeObject<TextFragmentAbsorber>("\\d{4}-\\d{4}");
    // como 1999-2000

    // Establecer la opción de búsqueda de texto para especificar el uso de expresión regular
    auto textSearchOptions = new TextSearchOptions(true);
    textFragmentAbsorber->set_TextSearchOptions(textSearchOptions);

    // Aceptar el absorbedor para la primera página del documento
    document->get_Pages()->Accept(textFragmentAbsorber);

    // Obtener los fragmentos de texto extraídos en la colección
    auto textFragmentCollection = textFragmentAbsorber->get_TextFragments();

    // Iterar a través de los fragmentos
    for (auto textFragment : textFragmentCollection) {
        // Actualizar texto y otras propiedades
        textFragment->set_Text(u"ABCD-EFGH");
        textFragment->get_TextState()->set_Font(FontRepository::FindFont(u"Verdana"));
        textFragment->get_TextState()->set_FontSize(12);
        textFragment->get_TextState()->set_ForegroundColor(Color::get_Blue());
        textFragment->get_TextState()->set_BackgroundColor(Color::get_Gray());
    }

    // Guardar el archivo PDF actualizado
    document->Save(_dataDir + u"Updated_Text.pdf");
}
```

## Reemplazar fuentes en un archivo PDF existente

Aspose.PDF para C++ admite la capacidad de reemplazar texto en un documento PDF. Sin embargo, a veces tiene el requisito de solo reemplazar la fuente que se está utilizando dentro del documento PDF. Entonces, en lugar de reemplazar el texto, solo se reemplaza la fuente que se está utilizando. Una de las sobrecargas del constructor TextFragmentAbsorber acepta un objeto TextEditOptions como argumento y podemos usar el valor RemoveUnusedFonts de la enumeración TextEditOptions.FontReplace para cumplir con nuestros requisitos. El siguiente fragmento de código muestra cómo reemplazar la fuente dentro de un documento PDF.

```cpp
void ReplaceFonts() {
    String _dataDir("C:\\Samples\\");

    // Instanciar objeto Document
    auto document = MakeObject<Document>(_dataDir + u"sample.pdf");

    // Buscar fragmentos de texto y establecer la opción de edición como eliminar fuentes no utilizadas
    auto textFragmentAbsorber = MakeObject<TextFragmentAbsorber>(
        MakeObject<TextEditOptions>(TextEditOptions::FontReplace::RemoveUnusedFonts));

    // Aceptar el absorbedor para todas las páginas del documento
    document->get_Pages()->Accept(textFragmentAbsorber);

    // recorrer todos los TextFragments
    auto textFragmentCollection = textFragmentAbsorber->get_TextFragments();
    for (auto textFragment : textFragmentCollection) {
        String fontName = textFragment->get_TextState()->get_Font()->get_FontName();
        // si el nombre de la fuente es ArialMT, reemplazar el nombre de la fuente por Arial
        if (fontName.Equals(u"ArialMT")) {
            textFragment->get_TextState()->set_Font(FontRepository::FindFont(u"Arial"));
        }
    }

    // Guardar el archivo PDF actualizado
    document->Save(_dataDir + u"Updated_Text.pdf");
}
```

En el siguiente fragmento de código, verá cómo usar una fuente no inglesa al reemplazar texto:

```cpp
void UseNonEnglishFontWhenReplacingText() {

    String _dataDir("C:\\Samples\\");

    // Instanciar objeto Documento
    auto document = MakeObject<Document>(_dataDir + u"sample.pdf");

    // Vamos a cambiar cada palabra "PDF" a algún texto en japonés con una fuente específica
    // MSGothic que podría estar instalada en el sistema operativo
    // Además, podría ser otra fuente que soporte jeroglíficos
    auto textFragmentAbsorber = MakeObject<TextFragmentAbsorber>("PDF");

    // Crear instancia de opciones de búsqueda de texto
    auto searchOptions = MakeObject<TextSearchOptions>(true);
    textFragmentAbsorber->set_TextSearchOptions(searchOptions);

    // Aceptar el absorbedor para todas las páginas del documento
    document->get_Pages()->Accept(textFragmentAbsorber);

    // Obtener los fragmentos de texto extraídos en la colección
    auto textFragmentCollection = textFragmentAbsorber->get_TextFragments();

    // Recorrer los fragmentos
    for (auto textFragment : textFragmentCollection) {
        // Actualizar texto y otras propiedades
        textFragment->set_Text(u"ファイル");
        textFragment->get_TextState()->set_Font(FontRepository::FindFont(u"TakaoMincho"));
        textFragment->get_TextState()->set_FontSize(12);
        textFragment->get_TextState()->set_ForegroundColor(Color::get_Blue());
        textFragment->get_TextState()->set_BackgroundColor(Color::get_Gray());
    }
    // Guardar el documento actualizado
    document->Save(_dataDir + u"Japanese_Text.pdf");
}
```

## El reemplazo de texto debe reorganizar automáticamente el contenido de la página

Aspose.PDF para C++ admite encontrar y reemplazar texto dentro de un archivo PDF. Sin embargo, recientemente, algunos clientes han tenido problemas al reemplazar texto, donde un TextFragment particular es reemplazado con contenido más pequeño y se muestra un espacio en blanco adicional en el PDF resultante, o si el TextFragment es reemplazado con una cadena más larga, las palabras se superponen al contenido existente de la página. Por lo tanto, fue necesario introducir un mecanismo que, después de reemplazar el texto dentro del documento PDF, reorganizara su contenido.

Para atender los escenarios mencionados, Aspose.PDF para C++ ha sido mejorado para que tales problemas no ocurran al reemplazar texto dentro de un archivo PDF. El siguiente fragmento de código demuestra cómo reemplazar texto dentro de un archivo PDF y el contenido de la página debe ser reordenado automáticamente.

```cpp
void RearrangeContent() {
    String _dataDir("C:\\Samples\\");

    // Instanciar objeto Document
    auto document = MakeObject<Document>(_dataDir + u"sample.pdf");

    // Crear objeto TextFragment Absorber con expresión regular
    auto textFragmentAbsorber = MakeObject<TextFragmentAbsorber>("[PDF,Web]");

    auto textSearchOptions = MakeObject<TextSearchOptions>(true);
    textFragmentAbsorber->set_TextSearchOptions(textSearchOptions);

    // También puede especificar la opción ReplaceAdjustment.WholeWordsHyphenation para
    // ajustar el texto en la siguiente o actual línea si la línea actual se vuelve demasiado larga o
    // corta después del reemplazo:
    //textFragmentAbsorber->get_TextReplaceOptions()->set_ReplaceAdjustmentAction(TextReplaceOptions::ReplaceAdjustment::WholeWordsHyphenation);

    // Aceptar el absorbente para todas las páginas del documento
    document->get_Pages()->Accept(textFragmentAbsorber);

    // Obtener los fragmentos de texto extraídos en la colección
    auto textFragmentCollection = textFragmentAbsorber->get_TextFragments();

    // Reemplazar cada TextFragment
    for (auto textFragment : textFragmentCollection) {
        // Establecer fuente del fragmento de texto que se reemplaza
        textFragment->get_TextState()->set_Font(FontRepository::FindFont(u"Arial"));
        // Establecer tamaño de fuente
        textFragment->get_TextState()->set_FontSize(10);
        textFragment->get_TextState()->set_ForegroundColor(Color::get_Blue());
        textFragment->get_TextState()->set_BackgroundColor(Color::get_Gray());
        // Reemplazar el texto con una cadena más larga que el marcador de posición
        textFragment->set_Text(u"This is a larger string for the testing of this feature");
    }
    // Guardar PDF resultante
    document->Save(_dataDir + u"RearrangeContentsUsingTextReplacement_out.pdf");
}
```

## Renderización de Símbolos Reemplazables durante la creación de PDF

Los símbolos reemplazables son símbolos especiales en una cadena de texto que pueden ser reemplazados con el contenido correspondiente en tiempo de ejecución. Los símbolos reemplazables actualmente soportados por el nuevo Modelo de Objeto de Documento del espacio de nombre Aspose.PDF son `$P`, `$p,` `\n`, `\r`. Los símbolos `$p` y `$P` se utilizan para manejar la numeración de páginas en tiempo de ejecución. `$p` se reemplaza con el número de la página donde se encuentra la clase Paragraph actual. `$P` se reemplaza con el número total de páginas en el documento. Al agregar `TextFragment` a la colección de párrafos de documentos PDF, no soporta el salto de línea dentro del texto. Sin embargo, para agregar texto con un salto de línea, utilice `TextFragment` con `TextParagraph`:

- use "\r\n" o Environment.NewLine en TextFragment en lugar de un único "\n";
- cree un objeto TextParagraph. Añadirá texto con división de líneas;
- agregue el TextFragment con TextParagraph.AppendLine;
- agregue el TextParagraph con TextBuilder.AppendParagraph.

## Símbolos reemplazables en el área de Encabezado/Pie de página

El símbolo reemplazable también se puede colocar dentro de la sección de encabezado/pie de página del archivo PDF. Revise el siguiente fragmento de código para ver cómo agregar un símbolo reemplazable a una sección de pie de página.

```csharp
void ReplaceableSymbolsInHeaderFooterArea() {

    auto document = MakeObject<Document>();
    auto page = doc.getPages().add();

    auto marginInfo = MakeObject<MarginInfo>();
    marginInfo->set_Top(90);
    marginInfo->set_Bottom(50);
    marginInfo->set_Left(50);
    marginInfo->set_Right(50);

    // Asignar la instancia de marginInfo a la propiedad Margin de PageInfo
    page.getPageInfo()->set_Margin(marginInfo);

    auto hfFirst = MakeObject<HeaderFooter>();
    page->set_Header(hfFirst);
    hfFirst->get_Margin()->set_Left(50);
    hfFirst->get_Margin()->set_Right(50);

    // Instanciar un párrafo de texto que almacenará el contenido para mostrar como encabezado
    auto t1 = MakeObject<TextFragment>("título del informe");
    t1->get_TextState()->set_Font(FontRepository::FindFont(u"Arial"));
    t1->get_TextState()->set_FontSize(16);
    t1->get_TextState()->set_ForegroundColor(Color::get_Black());
    t1->get_TextState()->set_FontStyle(FontStyles::Bold);
    t1->get_TextState()->set_HorizontalAlignment(HorizontalAlignment::Center);
    t1->get_TextState()->set_LineSpacing(5.0f);
    hfFirst->get_Paragraphs()->Add(t1);

    auto t2 = MakeObject<TextFragment>("Nombre_Informe");
    t2->get_TextState()->set_Font(FontRepository::FindFont(u"Arial"));
    t2->get_TextState()->set_ForegroundColor(Color::get_Black());
    t2->get_TextState()->set_HorizontalAlignment(HorizontalAlignment::Center);
    t2->get_TextState()->set_LineSpacing(5.0f);
    t2->get_TextState()->set_FontSize(12);
    hfFirst->get_Paragraphs()->Add(t2);

    // Crear un objeto HeaderFooter para la sección
    auto hfFoot = MakeObject<HeaderFooter>();

    // Establecer el objeto HeaderFooter para pie de página impar y par
    page->set_Footer(hfFoot);
    hfFoot->get_Margin()->set_Left(50);
    hfFoot->get_Margin()->set_Right(50);

    // Agregar un párrafo de texto que contenga el número de página actual del total de páginas
    auto t3 = MakeObject<TextFragment>("Generado en fecha de prueba");
    auto t4 = MakeObject<TextFragment>("nombre del informe ");
    auto t5 = MakeObject<TextFragment>("Página $p de $P");

    // Instanciar un objeto tabla
    auto tab2 = MakeObject<Table>();

    // Agregar la tabla en la colección de párrafos de la sección deseada
    hfFoot->get_Paragraphs()->Add(tab2);

    // Establecer anchos de columna de la tabla
    tab2->set_ColumnWidths(u"165 172 165");

    // Crear filas en la tabla y luego celdas en las filas
    auto row3 = tab2->get_Rows()->Add();

    row3->get_Cells()->Add();
    row3->get_Cells()->Add();
    row3->get_Cells()->Add();

    // Establecer la alineación vertical del texto como centrada
    row3->get_Cells()->idx_get(0)->set_Alignment(HorizontalAlignment::Left);
    row3->get_Cells()->idx_get(1)->set_Alignment(HorizontalAlignment::Center);
    row3->get_Cells()->idx_get(2)->set_Alignment(HorizontalAlignment::Right);

    row3->get_Cells()->idx_get(0)->get_Paragraphs()->Add(t3);
    row3->get_Cells()->idx_get(1)->get_Paragraphs()->Add(t4);
    row3->get_Cells()->idx_get(2)->get_Paragraphs()->Add(t5);

    auto table = MakeObject<Table>();

    table->set_ColumnWidths(u"33% 33% 34%");
    table->set_DefaultCellPadding(new MarginInfo());
    table->get_DefaultCellPadding()->set_Top(10);
    table->get_DefaultCellPadding()->set_Bottom(10);

    // Agregar la tabla en la colección de párrafos de la sección deseada
    page.getParagraphs().add(table);

    // Establecer el borde de celda predeterminado usando el objeto BorderInfo
    table->set_DefaultCellBorder(MakeObject<BorderInfo>(BorderSide::All, 0.1f));

    // Establecer el borde de la tabla usando otro objeto BorderInfo personalizado
    table->set_Border(MakeObject<BorderInfo>(BorderSide::All, 1.0f));

    table->set_RepeatingRowsCount(1);

    // Crear filas en la tabla y luego celdas en las filas
    auto row1 = table->get_Rows()->Add();

    row1->get_Cells()->Add(u"col1");
    row1->get_Cells()->Add(u"col2");
    row1->get_Cells()->Add(u"col3");

    String CRLF ("\r\n");

    for (int i = 0; i <= 10; i++) {
        auto row = table->get_Rows()->Add();
        row->set_IsRowBroken(true);
        for (int c = 0; c <= 2; c++) {
            SharedPtr<Cell> c1;
            if (c == 2)
                c1 = row->get_Cells()->Add(
                    u"Aspose.Total for C++ es una compilación de todos los componentes de Java ofrecidos por Aspose. Se compila en una"
                    + CRLF
                    + u"base diaria para asegurar que contiene las versiones más actualizadas de cada uno de nuestros componentes de Java. "
                    + CRLF
                    + u"base diaria para asegurar que contiene las versiones más actualizadas de cada uno de nuestros componentes de Java. "
                    + CRLF
                    + u"Usando Aspose.Total for C++ los desarrolladores pueden crear una amplia gama de aplicaciones.");
            else
                c1 = row->get_Cells()->Add(u"elemento1" + c);
            c1->set_Margin(new MarginInfo());
            c1->get_Margin()->set_Left(30);
            c1->get_Margin()->set_Top(10);
            c1->get_Margin()->set_Bottom(10);
        }
    }

    _dataDir = _dataDir + "ReplaceableSymbolsInHeaderFooter_out.pdf";
    doc.save(_dataDir);
}
```

## Remove All Text from PDF Document

### Remove All Text using Operators

En algunas operaciones de texto, necesitas eliminar todo el texto del documento PDF, y para eso, usualmente necesitas establecer el texto encontrado como un valor de cadena vacío. El hecho es que cambiar el texto para un conjunto de fragmentos de texto provoca una serie de operaciones para verificar y ajustar la posición del texto. Son necesarias en los scripts de edición de texto. La dificultad radica en el hecho de que no puedes determinar cuántos fragmentos de texto serán eliminados en el script donde se procesan en el bucle.

Por lo tanto, recomendamos usar un enfoque diferente para el escenario de eliminar todo el texto de las páginas PDF.

El siguiente fragmento de código muestra cómo resolver esta tarea rápidamente.

```cpp
void RemoveAllTextUsingOperators() {

    String _dataDir("C:\\Samples\\");

    // Open document
    auto document = MakeObject<Document>(_dataDir + u"sample.pdf");

    // Loop through all pages of PDF Document
    for (int i = 1; i <= document->get_Pages()->get_Count(); i++) {
        auto page = document->get_Pages()->idx_get(i);
        auto operatorSelector = MakeObject<OperatorSelector>(MakeObject<Aspose::Pdf::Operators::TextShowOperator>());
        // Select all text on the page
        page->get_Contents()->Accept(operatorSelector);
        // Delete all text
        page->get_Contents()->Delete(operatorSelector->get_Selected());
    }
    // Save the document
    document->Save(_dataDir + u"RemoveAllText_out.pdf");
}
```