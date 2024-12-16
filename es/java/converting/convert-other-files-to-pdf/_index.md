---
title: Convertir varios formatos de archivo a PDF 
linktitle: Convertir otros formatos de archivo a PDF 
type: docs
weight: 80
url: /es/java/convert-other-files-to-pdf/
lastmod: "2021-11-19"
description: Este tema muestra cómo Aspose.PDF permite convertir otros formatos de archivo a documentos PDF.
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

## Convertir EPUB a PDF

**Aspose.PDF para Java** te permite convertir fácilmente archivos EPUB al formato PDF.

<abbr title="publicación electrónica">EPUB</abbr> (abreviatura de publicación electrónica) es un estándar gratuito y abierto de libros electrónicos del Foro Internacional de Publicación Digital (IDPF). Los archivos tienen la extensión .epub. EPUB está diseñado para contenido refluible, lo que significa que un lector EPUB puede optimizar el texto para un dispositivo de visualización en particular.

Para convertir archivos EPUB al formato PDF, Aspose.PDF para Java tiene una clase llamada [EpubLoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/EpubLoadOptions) que se utiliza para cargar el archivo EPUB de origen.
 Después de eso, el objeto se pasa como un argumento para la inicialización del objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document), ya que ayuda al motor de renderización de PDF a determinar el formato de entrada del documento fuente.

El siguiente fragmento de código muestra el proceso de conversión de un archivo EPUB a formato PDF.

1. Crear un [`LoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/loadoptions) de EPUB.
1. Inicializar objeto [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/document).
1. Guardar documento PDF de salida.

```java
package com.aspose.pdf.examples;

import java.io.FileNotFoundException;
import java.nio.file.Path;
import java.nio.file.Paths;

import com.aspose.pdf.*;

public final class ConvertEPUBtoPDF {

    private ConvertEPUBtoPDF() {
    }

    private static Path _dataDir = Paths.get("/home/admin1/pdf-examples/Samples");

    public static void main(String[] args) throws FileNotFoundException {
        
        // Crear un LoadOptions de EPUB
        EpubLoadOptions options = new EpubLoadOptions();

        // Inicializar objeto documento
        String epubFileName = Paths.get(_dataDir.toString(), "aliceDynamic.epub").toString();
        Document document = new Document(epubFileName, options);

        // Guardar documento PDF de salida
        document.save(Paths.get(_dataDir.toString(),"EPUBtoPDF.pdf").toString());
    }
}
```

{{% alert color="success" %}}
**Intenta convertir EPUB a PDF en línea**

Aspose.PDF para Java te presenta una aplicación gratuita en línea ["EPUB a PDF"](https://products.aspose.app/pdf/conversion/epub-to-pdf), donde puedes intentar investigar la funcionalidad y calidad con la que trabaja.

[![Conversión de Aspose.PDF de EPUB a PDF con aplicación gratuita](epub.png)](https://products.aspose.app/pdf/conversion/epub-to-pdf)
{{% /alert %}}

## Convertir Markdown a PDF

**Esta característica es soportada por la versión 19.6 o superior.**

{{% alert color="success" %}}
**Intenta convertir Markdown a PDF en línea**

Aspose.PDF para Java te presenta una aplicación gratuita en línea ["Markdown a PDF"](https://products.aspose.app/pdf/conversion/md-to-pdf), donde puedes intentar investigar la funcionalidad y calidad con la que trabaja.

[![Conversión de Aspose.PDF de Markdown a PDF con aplicación gratuita](markdown.png)](https://products.aspose.app/pdf/conversion/md-to-pdf)
{{% /alert %}}

Markdown es una herramienta de conversión de texto a HTML para autores web.
 Markdown te permite escribir en un formato de texto plano fácil de leer y escribir y luego convertirlo en XHTML (o HTML) estructuralmente válido.

El siguiente fragmento de código muestra cómo usar esta funcionalidad con Aspose.PDF para Java:

```java
package com.aspose.pdf.examples;

import java.io.FileNotFoundException;
import java.nio.file.Path;
import java.nio.file.Paths;

import com.aspose.pdf.*;

public final class ConvertMDtoPDF {

    private ConvertMDtoPDF() {
    }

    private static Path _dataDir = Paths.get("/home/admin1/pdf-examples/Samples");

    public static void main(String[] args) throws FileNotFoundException {
        
        // Instanciar objeto de opción de carga de Latex
        MdLoadOptions options = new MdLoadOptions();
        
        // Crear objeto Documento
        String markdownFileName = Paths.get(_dataDir.toString(), "samplefile.md").toString();
        Document document = new Document(markdownFileName, options);

        // Guardar documento PDF de salida
        document.save(Paths.get(_dataDir.toString(),"MarkdownToPDF.pdf").toString());
    }
}

```

## Convertir PCL a PDF

<abbr title="Printer Command Language">PCL</abbr> (Printer Command Language) es un lenguaje de impresora de Hewlett-Packard desarrollado para acceder a características estándar de impresoras. Los niveles PCL del 1 al 5e/5c son lenguajes basados en comandos que utilizan secuencias de control que se procesan e interpretan en el orden en que se reciben. A nivel de consumidor, los flujos de datos PCL son generados por un controlador de impresión. La salida PCL también puede ser fácilmente generada por aplicaciones personalizadas.

{{% alert color="success" %}}
**Intenta convertir PCL a PDF en línea**

Aspose.PDF para Java te presenta la aplicación en línea gratuita ["PCL a PDF"](https://products.aspose.app/pdf/conversion/pcl-to-pdf), donde puedes intentar investigar la funcionalidad y calidad con la que trabaja.

[![Aspose.PDF Conversión PCL a PDF con App Gratuita](pcl_to_pdf.png)](https://products.aspose.app/pdf/conversion/pcl-to-pdf)
{{% /alert %}}

**Actualmente, solo se admiten PCL5 y versiones anteriores.**

|**Conjuntos de Comandos**|**Soporte**|**Excepciones**|**Descripción**|

| :- | :- | :- | :- |
|Comandos de control de trabajos|+|Modo de impresión a doble cara|Controlar el proceso de impresión: número de copias, bandeja de salida, impresión simplex/dúplex, márgenes superior e izquierdo, etc.|
|Comandos de control de página|+|Comando de salto de perforación|Especificar un tamaño de página, márgenes, orientación de la página, interlineado, distancias entre caracteres, etc.|
|Comandos de posicionamiento del cursor|+| |Especificar la posición del cursor y, por lo tanto, los orígenes del texto, imágenes rasterizadas o vectoriales y detalles.|

|Comandos de selección de fuente|+|<p>1. Comando de Datos de Impresión Transparente.</p><p>2. Fuentes blandas incrustadas. En la versión actual, en lugar de crear una fuente blanda, nuestra biblioteca selecciona una fuente adecuada de las fuentes TrueType "duras" existentes instaladas en la máquina de destino. <br>   La idoneidad se define por la relación ancho/altura. <br>   Esta característica funciona solo para fuentes Bitmap y TrueType y no garantiza que el texto impreso con la fuente blanda sea relevante para el del archivo fuente. <br>   Porque los códigos de caracteres en la fuente blanda pueden no coincidir con los predeterminados.</p><p>3. Conjuntos de símbolos definidos por el usuario.</p>|Permitir cargar fuentes blandas (incrustadas) desde el archivo PCL y gestionarlas en memoria.|
|Comandos gráficos rasterizados|+|Solo blanco y negro|Permitir cargar imágenes rasterizadas del archivo PCL a la memoria, especificar parámetros de rasterización <br>como ancho, altura, tipo de compresión, resolución, etc.|
|Comandos de color|+| |Permitir colorear todos los objetos imprimibles.|
|Comandos del modelo de impresión|+| |Permitir rellenar texto, imágenes rasterizadas y áreas rectangulares con patrones predefinidos y definidos por el usuario, especificar el modo de transparencia para los patrones y la imagen rasterizada de origen.|
 <br>Los patrones predefinidos son rayado, cruzado y sombreado.|
|Comandos de relleno de área rectangular|+| |Permiten la creación y el relleno de áreas rectangulares con patrones.|
|Comandos de gráficos vectoriales HP-GL/2|+|El Comando de Vector Tamizado (SV), el Comando de Modo de Transparencia (TR), el Comando de Datos Transparentes (TD), RO (Rotar Sistema de Coordenadas), Comando de Fuentes Escalables o de Mapa de Bits (SB), Comando de Inclinación de Carácter (SL) y Espacio Extra (ES) no están implementados y los comandos DV (Definir Ruta de Texto Variable) se realizan en versión beta.|<p>- Permiten cargar imágenes vectoriales HP-GL/2 desde el archivo PCL en la memoria. Vector image has an origin at the lower-left corner of the printable area, can be scaled, translated, rotated and clipped.</p><p>- Una imagen vectorial tiene un origen en la esquina inferior izquierda del área imprimible, puede ser escalada, traducida, rotada y recortada.</p><p>- A vector image can contain text, as labels, and geometric figures such as rectangle, circle, ellipse, line, arc, bezier curve and complex figures composed from the simple ones.</p><p>- Una imagen vectorial puede contener texto, como etiquetas, y figuras geométricas como rectángulo, círculo, elipse, línea, arco, curva de Bézier y figuras complejas compuestas de las simples.</p><p>- Closed figures including letters of labels can be filled with solid fill or vector pattern.</p><p>- Las figuras cerradas, incluidas las letras de las etiquetas, pueden llenarse con un relleno sólido o un patrón vectorial.</p><p>- The pattern can be hatching, cross-hatch, shading, raster user-defined, PCL hatching or cross-hatch and PCL user-defined. PCL patterns are raster. Labels can be individually rotated, scaled, and directed in four directions: up, down, left and right. Left and Right directions involve one-after-another letter arrangement. Up and Down directions involve one-under-another letter arrangement.</p>|

|Macross|―| |Permitir cargar una secuencia de comandos PCL en la memoria y usar esta secuencia muchas veces, por ejemplo, para imprimir el encabezado de la página o establecer un formato único para un conjunto de páginas.|

|Unicode text|―| |Permitir imprimir caracteres no ASCII. No implementado debido a la falta de archivos de muestra con <br>texto Unicode|
|PCL6 (PCL-XL)| |Realizado solo en la versión Beta debido a la falta de archivos de prueba. Las fuentes incrustadas tampoco son compatibles. La extensión JetReady no es compatible porque es imposible tener la especificación JetReady.|Formato de archivo binario.|

### Convertir un archivo PCL en formato PDF

Para permitir la conversión de PCL a PDF, [Aspose.PDF for Java](https://products.aspose.com/pdf/java) tiene la clase [PclLoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/PclLoadOptions) que se utiliza para inicializar el objeto [LoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/LoadOptions). Este objeto se pasa luego como argumento durante la inicialización del objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document) y ayuda al motor de renderizado PDF a determinar el formato de entrada del documento fuente.

El siguiente fragmento de código muestra el proceso de convertir un archivo PCL en formato PDF.

```java
package com.aspose.pdf.examples;

import java.io.FileNotFoundException;
import java.nio.file.Path;
import java.nio.file.Paths;

import com.aspose.pdf.*;

public final class ConvertPCLtoPDF {

    private ConvertPCLtoPDF() {
        
    }

    private static Path _dataDir = Paths.get("/home/admin1/pdf-examples/Samples");

    public static void main(String[] args) throws FileNotFoundException {        
        ConvertPCLtoPDF_Simple();
        ConvertPCLtoPDF_Advanced();
    }

    public static void ConvertPCLtoPDF_Simple() {
        PclLoadOptions options = new PclLoadOptions();
        Document pdfDocument= new Document(_dataDir + "demo.pcl", options);
        pdfDocument.save(_dataDir + "epub_test.pdf");        
    }

    public static void ConvertPCLtoPDF_Advanced() {
        PclLoadOptions options = new PclLoadOptions();
        options.SupressErrors=true;
        Document pdfDocument= new Document(_dataDir + "demo.pcl", options);
        if (options.Exceptions!=null)
            for (Exception ex : options.Exceptions)
            {
                System.out.println(ex.getMessage());
            }
        pdfDocument.save(_dataDir + "pcl_test.pdf");        
    }
}
```

### Problemas Conocidos

1. El origen de las cadenas de texto y las imágenes puede diferir ligeramente de las del archivo PCL de origen si la dirección de impresión no es 0º. Lo mismo se aplica a las imágenes vectoriales si el sistema de coordenadas del gráfico vectorial está rotado (comando RO precedido).
2. El origen de las etiquetas en las imágenes vectoriales puede diferir de las del archivo PCL de origen si las etiquetas están influenciadas por una secuencia de comandos: Origen de Etiqueta (LO), Definir Ruta de Texto Variable (DV), Dirección Absoluta (DI) o Dirección Relativa (DR).
3. Un texto puede leerse incorrectamente si debe renderizarse con una fuente suave (incrustada) Bitmap o TrueType, porque actualmente estas fuentes solo son parcialmente compatibles (ver excepciones en la "tabla de características compatibles"). En esta situación, el texto solo puede leerse correctamente si los códigos de caracteres en una fuente suave corresponden a los predeterminados. Un estilo del texto leído también puede diferir del del archivo PCL de origen porque no es necesario establecer el estilo en el encabezado de la fuente suave.

1. Si el archivo PCL analizado contiene fuentes Intellifont o Universal soft, se lanzará una excepción, porque las fuentes Intellifont y Universal no son compatibles en absoluto.
1. Si el archivo PCL analizado contiene comandos de macros, el resultado del análisis diferirá considerablemente del archivo fuente, porque los comandos de macros no son compatibles.

## Convertir Texto a PDF

**Aspose.PDF para Java** proporciona la capacidad de convertir archivos de texto al formato PDF. En este artículo, demostramos lo fácil y eficientemente que podemos convertir un archivo de texto a PDF usando Aspose.PDF.

Cuando necesites convertir un archivo de texto a PDF, inicialmente lee el archivo de texto fuente en algún lector. Hemos utilizado StringBuilder para leer el contenido del archivo de texto. Instancia un objeto Document y añade una nueva página en la colección Pages. Crea un nuevo objeto de TextFragment y pasa el objeto StringBuilder a su constructor. Añade un nuevo párrafo en la colección Paragraphs usando el objeto TextFragment y guarda el archivo PDF resultante usando el método Save de la clase Document.
**Intenta convertir TEXTO a PDF en línea**

Aspose.PDF para Java te presenta la aplicación gratuita en línea ["Text to PDF"](https://products.aspose.app/pdf/conversion/txt-to-pdf), donde puedes intentar investigar la funcionalidad y calidad con la que trabaja.

{{% alert color="primary" %}}
[![Aspose.PDF Convertion TEXT to PDF with Free App](text_to_pdf.png)](https://products.aspose.app/pdf/conversion/txt-to-pdf)
{{% /alert %}}

### Convertir archivo de texto plano a PDF

```java
package com.aspose.pdf.examples;
/**
 * Convertir TXT a PDF
 */

import java.io.IOException;
import java.nio.charset.Charset;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;

import com.aspose.pdf.*;

public final class ConvertTextToPDF {

    private ConvertTextToPDF() {
    }

    final static Path _dataDir = Paths.get("/home/admin1/pdf-examples/Samples");
    final static Charset ENCODING = StandardCharsets.UTF_8;

    public static void main(String[] args) throws IOException {
        ConvertTXT_to_PDF_Simple();
    }

    public static void ConvertTXT_to_PDF_Simple() throws IOException {
        // Inicializar objeto de documento

        String pdfDocumentFileName = Paths.get(_dataDir.toString(), "demo_txt.pdf").toString();
        Path txtDocumentFileName = Paths.get(_dataDir.toString(), "rfc822.txt");

        // Instanciar un objeto Document llamando a su constructor vacío
        Document pdfDocument = new Document();

        // Agregar una nueva página en la colección de Pages del Document
        Page page = pdfDocument.getPages().add();

        // Crear una instancia de TextFragment y pasar el texto del objeto reader a su
        // constructor como argumento
        TextFragment text = new TextFragment(Files.readString(txtDocumentFileName, ENCODING));

        // Agregar un nuevo párrafo de texto en la colección de párrafos y pasar el objeto
        // TextFragment
        page.getParagraphs().add(text);

        // Guardar el archivo PDF resultante
        pdfDocument.save(pdfDocumentFileName);
    }
```


### Convertir archivo de texto preformateado a PDF

```java
    public static void ConvertPreFormattedTextToPdf() throws IOException {

        Path txtDocumentFileName = Paths.get(_dataDir.toString(), "rfc822.txt");
        String pdfDocumentFileName = Paths.get(_dataDir.toString(), "demo_txt.pdf").toString();

        // Leer el archivo de texto como un array de cadenas
        java.util.List<String> lines = Files.readAllLines(txtDocumentFileName, ENCODING);

        // Instanciar un objeto Document llamando a su constructor vacío
        Document pdfDocument = new Document();

        // Añadir una nueva página en la colección Pages del Document
        Page page = pdfDocument.getPages().add();

        // Establecer márgenes izquierdo y derecho para una mejor presentación
        page.getPageInfo().getMargin().setLeft(20);
        page.getPageInfo().getMargin().setRight(10);
        page.getPageInfo().getDefaultTextState().setFont(FontRepository.findFont("Courier New"));
        page.getPageInfo().getDefaultTextState().setFontSize(12);

        for (String line : lines) {
            // verificar si la línea contiene el carácter de "salto de página"
            // ver https://en.wikipedia.org/wiki/Page_break
            if (line.startsWith("\f")) {
                page = pdfDocument.getPages().add();
                page.getPageInfo().getMargin().setLeft(20);
                page.getPageInfo().getMargin().setRight(10);
                page.getPageInfo().getDefaultTextState().setFont(FontRepository.findFont("Courier New"));
                page.getPageInfo().getDefaultTextState().setFontSize(12);
            } else {
                // Crear una instancia de TextFragment y
                // pasar la línea a su
                // constructor como argumento
                TextFragment text = new TextFragment(line);

                // Añadir un nuevo párrafo de texto en la colección de párrafos y pasar el objeto TextFragment
                page.getParagraphs().add(text);
            }

            pdfDocument.save(pdfDocumentFileName);
        }
    }
}
```


## Convertir XPS a PDF

**Aspose.PDF para Java** admite la función de convertir archivos <abbr title="XML Paper Specification">XPS</abbr> a formato PDF. Consulte este artículo para resolver sus tareas.

XPS, Especificación de Papel XML, es un formato de archivo de Microsoft utilizado para integrar la creación y visualización de documentos en Windows. Con Aspose.PDF para Java, es posible convertir archivos XPS a PDF, el formato de archivo portátil de Adobe.

El formato de archivo es básicamente un archivo XML comprimido, utilizado principalmente para distribución y almacenamiento. Es muy difícil de editar y principalmente implementado por Microsoft.

Para convertir un archivo XPS a PDF usando [Aspose.PDF para Java](https://products.aspose.com/pdf/java), utilice la clase [XpsLoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/XpsLoadOptions).
 Este se utiliza para inicializar un objeto [LoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/LoadOptions). Más tarde, este objeto se pasa como argumento durante la inicialización del objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document) y ayuda al motor de renderizado de PDF a determinar el formato de entrada del documento fuente.

En tanto XP como Windows 7, deberías encontrar una impresora XPS preinstalada si miras en el Panel de Control y luego en Impresoras. Para crear archivos XPS puedes usar esa impresora como dispositivo de salida. En Windows 7, deberías poder simplemente hacer doble clic en el archivo para abrirlo en un visor de XPS. También puedes descargar el [visor XPS](http://windows.microsoft.com/en-US/windows-vista/what-is-the-xps-viewer) desde el sitio web de Microsoft.

El siguiente fragmento de código muestra el proceso de conversión del archivo XPS al formato PDF.

```java
public final class ConvertXPStoPDF {

    private ConvertXPStoPDF() {
    }

    final static Path _dataDir = Paths.get("/home/aspose/pdf-examples/Samples");

    public static void main(String[] args) throws IOException {
        Convert_XSLFO_to_PDF();
    }

    public static void Convert_XSLFO_to_PDF() throws IOException {
        // Inicializar objeto documento

        String pdfDocumentFileName = Paths.get(_dataDir.toString(), "demo_txt.pdf").toString();
        String xpsDocumentFileName = Paths.get(_dataDir.toString(), "demo.xml").toString();

        // Instanciar objeto LoadOption usando la opción de carga XPS
        LoadOptions options = new XpsLoadOptions();

        // Instanciar un objeto Document llamando a su constructor vacío
        Document pdfDocument = new Document(xpsDocumentFileName, options);

        // Guardar el archivo PDF resultante
        pdfDocument.save(pdfDocumentFileName);
    }
}
```

{{% alert color="success" %}}
**Intenta convertir el formato XPS a PDF en línea**

Aspose.PDF para Java te presenta la aplicación gratuita en línea ["XPS a PDF"](https://products.aspose.app/pdf/conversion/xps-to-pdf/), donde puedes investigar la funcionalidad y la calidad con la que trabaja.

[![Conversión de Aspose.PDF de XPS a PDF con App Gratis](xps_to_pdf.png)](https://products.aspose.app/pdf/conversion/xps-to-pdf/)
{{% /alert %}}

## Convertir PostScript a PDF

**Aspose.PDF para Java** admite funciones para convertir archivos PostScript al formato PDF. Una de las características de Aspose.PDF es que puedes establecer un conjunto de carpetas de fuentes para usar durante la conversión.

Para convertir un archivo PostScript a formato PDF, Aspose.PDF para Java ofrece la clase [PsLoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/PsLoadOptions) que se utiliza para inicializar el objeto LoadOptions. Más tarde, este objeto puede pasarse como argumento al constructor del objeto Document, lo que ayudará al Motor de Renderizado de PDF a determinar el formato del documento fuente.


El siguiente fragmento de código se puede usar para convertir un archivo PostScript en formato PDF:

```java
public static void ConvertPostScriptToPDF_Simple(){
        // Inicializar objeto documento

        String pdfDocumentFileName = Paths.get(_dataDir.toString(), "demo.pdf").toString();
        String psDocumentFileName = Paths.get(_dataDir.toString(), "demo.ps").toString();
        PsLoadOptions options = new PsLoadOptions();

        // Crear objeto Documento
        Document document = new Document(psDocumentFileName, options);

        // Guardar documento PDF de salida
        document.save(pdfDocumentFileName);
    }
```

Además, puedes configurar un conjunto de carpetas de fuentes que se usarán durante la conversión:

```java
public static void ConvertPostscriptToPDFAvdanced() {
        String pdfDocumentFileName = Paths.get(_dataDir.toString(), "demo.pdf").toString();
        String psDocumentFileName = Paths.get(_dataDir.toString(), "demo.ps").toString();
        PsLoadOptions options = new PsLoadOptions();
        
        options.setFontsFolders(new String[] { "c:\tmp\fonts1", "c:\tmp\fonts2" });

        // Crear objeto Documento
        Document document = new Document(psDocumentFileName, options);

        // Guardar documento PDF de salida
        document.save(pdfDocumentFileName);
    }
```


## Convertir XML a PDF

El formato XML se utiliza para almacenar datos estructurados. Hay varias maneras de convertir <abbr title="Extensible Markup Language">XML</abbr> a PDF en Aspose.PDF.

{{% alert color="success" %}}
**Intenta convertir XML a PDF en línea**

Aspose.PDF para Java te presenta una aplicación gratuita en línea ["XML to PDF"](https://products.aspose.app/pdf/conversion/xml-to-pdf), donde puedes intentar investigar la funcionalidad y la calidad de su funcionamiento.

[![Conversión de Aspose.PDF XML a PDF con Aplicación Gratuita](xml_to_pdf.png)](https://products.aspose.app/pdf/conversion/xml-to-pdf)
{{% /alert %}}

Considera la opción de usar un documento XML basado en el estándar XSL-FO.

### Convertir XSL-FO a PDF

La conversión de archivos XSL-FO a PDF se puede implementar utilizando el objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/document) con [XslFoLoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/xslfoloadoptions).

```java
package com.aspose.pdf.examples;
/**
 * Convertir XML a PDF
 */

import java.io.IOException;
import java.nio.file.Path;
import java.nio.file.Paths;

import com.aspose.pdf.*;

public final class ConvertXMLtoPDF {

    private ConvertXMLtoPDF() {
    }

    final static Path _dataDir = Paths.get("/home/admin1/pdf-examples/Samples");
    public static void main(String[] args) throws IOException {
        Convert_XSLFO_to_PDF();
        Convert_XSLFO_to_PDF_Adv();
    }

    public static void Convert_XSLFO_to_PDF() throws IOException {
        // Inicializar objeto documento

        String pdfDocumentFileName = Paths.get(_dataDir.toString(), "demo_txt.pdf").toString();
        String xmlDocumentFileName = Paths.get(_dataDir.toString(), "demo.xml").toString();
        String xsltDocumentFileName = Paths.get(_dataDir.toString(), "employees.xslt").toString();

        XslFoLoadOptions options = new XslFoLoadOptions(xsltDocumentFileName);

        // Instanciar un objeto Document llamando a su constructor vacío
        Document pdfDocument = new Document(xmlDocumentFileName,options);

        // Guardar archivo PDF resultante
        pdfDocument.save(pdfDocumentFileName);
    }
}
```


### Convertir XSL-FO a PDF con una estrategia de manejo de errores establecida

```java
// Inicializar objeto de documento

String documentFileName = Paths.get(DATA_DIR.toString(), "demo_txt.pdf").toString();
String xmlDocumentFileName = Paths.get(DATA_DIR.toString(), "demo.xml").toString();
String xsltDocumentFileName = Paths.get(DATA_DIR.toString(), "employees.xslt").toString();

XslFoLoadOptions options = new XslFoLoadOptions(xsltDocumentFileName);

// Establecer estrategia de manejo de errores
options.setParsingErrorsHandlingType(XslFoLoadOptions.ParsingErrorsHandlingTypes.ThrowExceptionImmediately);

// Instanciar un objeto Documento llamando a su constructor vacío
Document document = new Document(xmlDocumentFileName, options);

// Guardar archivo PDF resultante
document.save(documentFileName);
document.close();
```

## Convertir LaTeX/TeX a PDF

El formato de archivo LaTeX es un formato de archivo de texto con marcado en el derivado LaTeX de la familia de lenguajes TeX y LaTeX es un formato derivado del sistema TeX.
 LaTeX (ˈleɪtɛk/ lay-tek o lah-tek) es un sistema de preparación de documentos y un lenguaje de marcado de documentos. Es ampliamente utilizado para la comunicación y publicación de documentos científicos en muchos campos, incluyendo matemáticas, física e informática. También tiene un papel destacado en la preparación y publicación de libros y artículos que contienen materiales multilingües complejos, como sánscrito y árabe, incluyendo ediciones críticas. LaTeX utiliza el programa de composición tipográfica TeX para formatear su salida y está escrito en el lenguaje de macros TeX.

**Aspose.PDF for Java** admite la función de convertir archivos TeX a formato PDF y para cumplir con este requisito, el paquete com.aspose.pdf tiene una clase llamada [LatexLoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/LatexLoadOptions) que proporciona las capacidades para cargar archivos LaTex y renderizar la salida en formato PDF utilizando la clase [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document). El siguiente fragmento de código muestra el proceso de convertir un archivo LaTex al formato PDF.

```java
package com.aspose.pdf.examples;

import java.io.FileNotFoundException;
import java.nio.file.Path;
import java.nio.file.Paths;

import com.aspose.pdf.*;

public final class ConvertLATEXtoPDF {

    private ConvertLATEXtoPDF() {
    }

    private static Path _dataDir = Paths.get("/home/admin1/pdf-examples/Samples");

    public static void main(String[] args) throws FileNotFoundException {
        
        // Instanciar objeto de opción de carga de Latex
        TeXLoadOptions options = new TeXLoadOptions();
        
        // Crear objeto de Documento
        String latexFileName = Paths.get(_dataDir.toString(), "samplefile.tex").toString();
        Document document = new Document(latexFileName, options);

        // Guardar el documento PDF de salida
        document.save(Paths.get(_dataDir.toString(),"TEXtoPDF.pdf").toString());
    }
}
```

{{% alert color="success" %}}
**Intenta convertir LaTeX/TeX a PDF en línea**

Aspose.PDF para Java te presenta la aplicación gratuita en línea ["LaTex to PDF"](https://products.aspose.app/pdf/conversion/tex-to-pdf), donde puedes intentar investigar la funcionalidad y calidad con la que trabaja.
[![Aspose.PDF Conversión LaTeX/TeX a PDF con Aplicación Gratuita](latex.png)](https://products.aspose.app/pdf/conversion/tex-to-pdf)
{{% /alert %}}