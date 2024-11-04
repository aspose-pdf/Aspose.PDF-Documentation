---
title: Convertir varios formatos de archivo a PDF 
linktitle: Convertir otros formatos de archivo a PDF 
type: docs
weight: 80
url: /php-java/convert-other-files-to-pdf/
lastmod: "2024-05-20"
description: Este tema muestra cómo Aspose.PDF permite convertir otros formatos de archivo a documento PDF.
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

## Convertir EPUB a PDF

**Aspose.PDF para PHP** te permite convertir fácilmente archivos EPUB a formato PDF.

<abbr title="electronic publication">EPUB</abbr> es un estándar de libro electrónico libre y abierto de la International Digital Publishing Forum (IDPF). Los archivos tienen la extensión .epub. EPUB está diseñado para contenido refluible, lo que significa que un lector EPUB puede optimizar el texto para un dispositivo de visualización particular.

Para convertir archivos EPUB a formato PDF, Aspose.PDF para PHP tiene una clase llamada [EpubLoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/EpubLoadOptions) que se utiliza para cargar el archivo EPUB de origen.
 Después de eso, el objeto se pasa como un argumento para la inicialización del objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document), ya que ayuda al motor de renderizado PDF a determinar el formato de entrada del documento fuente.

El siguiente fragmento de código muestra el proceso de conversión de un archivo EPUB al formato PDF.

1. Crear un [LoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/epubloadoptions/) de EPUB.
1. Inicializar el objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/document).
1. Guardar el documento PDF de salida.

```php
// Crear una nueva instancia de EpubLoadOptions
$loadOption = new EpubLoadOptions();

// Crear un nuevo objeto Document y cargar el archivo EPUB
$document = new Document($inputFile, $loadOption);

// Guardar el documento como un archivo PDF
$document->save($outputFile);
```

{{% alert color="success" %}}
**Intenta convertir EPUB a PDF en línea**

Aspose.PDF para PHP te presenta la aplicación gratuita en línea ["EPUB to PDF"](https://products.aspose.app/pdf/conversion/epub-to-pdf), donde puedes intentar investigar la funcionalidad y la calidad con la que trabaja.
[![Aspose.PDF Convertion EPUB to PDF with Free App](epub.png)](https://products.aspose.app/pdf/conversion/epub-to-pdf)
{{% /alert %}}

## Convertir Markdown a PDF

{{% alert color="success" %}}
**Intente convertir Markdown a PDF en línea**

Aspose.PDF para PHP le presenta la aplicación gratuita en línea ["Markdown to PDF"](https://products.aspose.app/pdf/conversion/md-to-pdf), donde puede intentar investigar la funcionalidad y calidad con la que trabaja.

[![Aspose.PDF Convertion Markdown to PDF with Free App](markdown.png)](https://products.aspose.app/pdf/conversion/md-to-pdf)
{{% /alert %}}

Markdown es una herramienta de conversión de texto a HTML para autores web. Markdown le permite escribir en un formato de texto plano fácil de leer y escribir y luego convertirlo en XHTML (o HTML) estructuralmente válido.

El siguiente fragmento de código muestra cómo usar esta funcionalidad con Aspose.PDF para PHP:

```php
// Crear una nueva instancia de MdLoadOptions
$loadOption = new MdLoadOptions();

// Crear una nueva instancia de Document y cargar el archivo Markdown de entrada
$document = new Document($inputFile, $loadOption);

// Guardar el documento como un archivo PDF
$document->save($outputFile);
```


## Convertir PCL a PDF

<abbr title="Printer Command Language">PCL</abbr> (Printer Command Language) es un lenguaje de impresora de Hewlett-Packard desarrollado para acceder a las características estándar de la impresora. Los niveles de PCL del 1 al 5e/5c son lenguajes basados en comandos que utilizan secuencias de control procesadas e interpretadas en el orden en que se reciben. A nivel de consumidor, los flujos de datos PCL son generados por un controlador de impresión. La salida PCL también puede ser fácilmente generada por aplicaciones personalizadas.

{{% alert color="success" %}}
**Intenta convertir PCL a PDF en línea**

Aspose.PDF para PHP te presenta la aplicación gratuita en línea ["PCL a PDF"](https://products.aspose.app/pdf/conversion/pcl-to-pdf), donde puedes intentar investigar la funcionalidad y la calidad con la que trabaja.

[![Conversión de Aspose.PDF de PCL a PDF con Aplicación Gratuita](pcl_to_pdf.png)](https://products.aspose.app/pdf/conversion/pcl-to-pdf)
{{% /alert %}}

**Actualmente, solo se admiten PCL5 y versiones anteriores.**

|**Conjuntos de Comandos**|**Soporte**|**Excepciones**|**Descripción**|

| :- | :- | :- | :- |
|Comandos de control de trabajos|+|Modo de impresión a doble cara|Controlar el proceso de impresión: número de copias, bandeja de salida, impresión simple/doble cara, desplazamientos izquierdo y superior, etc.|
|Comandos de control de página|+|Comando de salto de perforación|Especificar un tamaño de página, márgenes, orientación de la página, interlineado, distancias entre caracteres, etc.|
|Comandos de posicionamiento del cursor|+| |Especificar la posición del cursor y, por lo tanto, los orígenes del texto, imágenes raster o vectoriales y detalles.|

|Comandos de selección de fuente|+|<p>1. Comando de Datos de Impresión Transparente.</p><p>2. Fuentes embebidas. En la versión actual, en lugar de crear una fuente suave, nuestra biblioteca selecciona una fuente adecuada de las fuentes TrueType "duras" existentes instaladas en una máquina objetivo. <br>   La idoneidad se define por la relación ancho/alto. <br>   Esta característica solo funciona para fuentes Bitmap y TrueType y no garantiza que el texto impreso con la fuente suave sea relevante para el del archivo fuente. <br>   Porque los códigos de caracteres en la fuente suave pueden no coincidir con los predeterminados.</p><p>3. Conjuntos de Símbolos Definidos por el Usuario.</p>|Permitir cargar fuentes suaves (embebidas) desde el archivo PCL y gestionarlas en memoria.|
|Comandos de gráficos rasterizados|+|Solo blanco y negro|Permitir cargar imágenes rasterizadas desde el archivo PCL a la memoria, especificar parámetros rasterizados <br>tales como ancho, alto, tipo de compresión, resolución, etc.|
|Comandos de color|+| |Permitir el color para todos los objetos imprimibles.|
|Comandos del modelo de impresión|+| |Permitir rellenar texto, imágenes rasterizadas y áreas rectangulares con patrones rasterizados predefinidos y definidos por el usuario, especificar el modo de transparencia para patrones y la imagen rasterizada fuente.|
 <br>Los patrones predefinidos son de rayado, cruzado y sombreado.|
|Comandos de relleno de área rectangular|+| |Permiten la creación y el relleno de áreas rectangulares con patrones.|
|Comandos de gráficos vectoriales HP-GL/2|+|El comando de vector con trama (SV), el comando de modo de transparencia (TR), el comando de datos transparentes (TD), RO (Sistema de Coordenadas de Rotación), comando de fuentes escalables o de mapa de bits (SB), comando de inclinación de caracteres (SL) y espacio extra (ES) no están implementados y los comandos DV (Definir ruta de texto variable) se realizan en versión beta.|<p>- Permitir la carga de imágenes vectoriales HP-GL/2 desde el archivo PCL en la memoria. Vector image tiene un origen en la esquina inferior izquierda del área imprimible, puede ser escalada, trasladada, rotada y recortada.</p><p>- Una imagen vectorial puede contener texto, como etiquetas, y figuras geométricas como rectángulo, círculo, elipse, línea, arco, curva de bezier y figuras complejas compuestas por las simples.</p><p>- Las figuras cerradas, incluidas las letras de las etiquetas, pueden rellenarse con relleno sólido o patrón vectorial.</p><p>- El patrón puede ser sombreado, cruzado, sombreado, rasterizado definido por el usuario, sombreado PCL o cruzado y definido por el usuario PCL. Los patrones PCL son rasterizados. Las etiquetas pueden ser rotadas, escaladas y dirigidas individualmente en cuatro direcciones: arriba, abajo, izquierda y derecha. Las direcciones Izquierda y Derecha implican una disposición de letras una tras otra. Las direcciones Arriba y Abajo implican una disposición de letras una debajo de otra.</p>|
|Macross|―| |Permitir cargar una secuencia de comandos PCL en la memoria y usar esta secuencia muchas veces, por ejemplo, para imprimir encabezados de página o establecer un formato para un conjunto de páginas.|
|Unicode text|―| |Permitir la impresión de caracteres no ASCII. No se implementó debido a la falta de archivos de muestra con texto Unicode.  
|PCL6 (PCL-XL)| |Realizado solo en la versión Beta debido a la falta de archivos de prueba. Las fuentes incrustadas tampoco son compatibles. La extensión JetReady no es compatible porque es imposible tener la especificación de JetReady. Formato de archivo binario.|

### Convertir un archivo PCL a formato PDF

Para permitir la conversión de PCL a PDF, [Aspose.PDF para PHP](https://products.aspose.com/pdf/php-java) tiene la clase [PclLoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/PclLoadOptions) que se utiliza para inicializar el objeto [LoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/LoadOptions). Este objeto luego se pasa como un argumento durante la inicialización del objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document) y ayuda al motor de renderizado de PDF a determinar el formato de entrada del documento fuente.

El siguiente fragmento de código muestra el proceso de conversión de un archivo PCL a formato PDF.

```php
// Crear una nueva instancia de PclLoadOptions
$loadOption = new PclLoadOptions();

// Crear una nueva instancia de Document y cargar el archivo PCL
$document = new Document($inputFile, $loadOption);

// Guardar el documento como un archivo PDF
$document->save($outputFile);
```

### Problemas Conocidos

1. El origen de las cadenas de texto e imágenes puede diferir ligeramente de las del archivo PCL fuente si la dirección de impresión no es 0º. Lo mismo se aplica a las imágenes vectoriales si el sistema de coordenadas del gráfico vectorial está rotado (precedido por el comando RO).
1. El origen de las etiquetas en imágenes vectoriales puede diferir de las del archivo PCL fuente si las etiquetas están influenciadas por una secuencia de comandos: Origen de Etiqueta (LO), Definir Ruta de Texto Variable (DV), Dirección Absoluta (DI) o Dirección Relativa (DR).
1. Un texto puede leerse incorrectamente si debe ser renderizado con una fuente de mapa de bits o TrueType suave (incrustada), porque actualmente estas fuentes solo están parcialmente soportadas (ver excepciones en "Tabla de características soportadas"). En esta situación, el texto puede leerse correctamente solo si los códigos de caracteres en una fuente suave corresponden a los predeterminados. El estilo del texto leído también puede diferir del del archivo PCL fuente porque no es necesario establecer el estilo en el encabezado de la fuente suave.

1. Si el archivo PCL analizado contiene fuentes Intellifont o Universal soft, se lanzará una excepción, porque las fuentes Intellifont y Universal no son compatibles en absoluto.
1. Si el archivo PCL analizado contiene comandos de macros, el resultado del análisis diferirá significativamente del archivo fuente, porque los comandos de macros no son compatibles.

## Convertir Texto a PDF

**Aspose.PDF para PHP** proporciona la capacidad de convertir archivos de texto a formato PDF. En este artículo, demostramos cuán fácil y eficientemente podemos convertir un archivo de texto a PDF usando Aspose.PDF.

Cuando necesites convertir un archivo de texto a PDF, inicialmente lee el archivo de texto fuente en algún lector. Hemos utilizado StringBuilder para leer los contenidos del archivo de texto. Instancia un objeto Document y añade una nueva página en la colección Pages. Crea un nuevo objeto de TextFragment y pasa el objeto StringBuilder a su constructor. Agrega un nuevo párrafo en la colección Paragraphs usando el objeto TextFragment y guarda el archivo PDF resultante usando el método Save de la clase Document.
**Intenta convertir TEXTO a PDF en línea**
{{% alert color="success" %}}

Aspose.PDF para PHP te presenta la aplicación gratuita en línea ["Texto a PDF"](https://products.aspose.app/pdf/conversion/txt-to-pdf), donde puedes intentar investigar la funcionalidad y calidad con la que trabaja.

[![Aspose.PDF Conversión TEXTO a PDF con Aplicación Gratuita](text_to_pdf.png)](https://products.aspose.app/pdf/conversion/txt-to-pdf)
{{% /alert %}}

### Convertir archivo de texto plano a PDF

```php
// Crear un nuevo objeto Document.
$document = new Document();

// Agregar una nueva página al documento.
$page = $document->getPages()->add();

// Leer el contenido del archivo de texto de entrada.
$text = file_get_contents($inputFile);

// Crear un nuevo objeto FontRepository.
$fontRepository = new FontRepository();

// Encontrar la fuente "Courier" en el repositorio.
$font = $fontRepository->findFont("Courier");

// Crear un nuevo objeto TextFragment con el texto de entrada.
$textFragment = new TextFragment($text);

// Establecer la fuente del fragmento de texto en "Courier".
$textFragment->getTextState()->setFont($font);

// Agregar el fragmento de texto a la página.
$page->getParagraphs()->add($textFragment);

// Guardar el documento en el archivo de salida.
$document->save($outputFile);
```


## Convertir XPS a PDF

**Aspose.PDF para PHP** admite la función de convertir archivos <abbr title="XML Paper Specification">XPS</abbr> al formato PDF. Consulte este artículo para resolver sus tareas.

XPS, XML Paper Specification, es un formato de archivo de Microsoft utilizado para integrar la creación y visualización de documentos en Windows. Con Aspose.PDF para PHP, es posible convertir archivos XPS a PDF, el formato de archivo portátil de Adobe.

El formato de archivo es básicamente un archivo XML comprimido, utilizado principalmente para distribución y almacenamiento. Es muy difícil de editar y mayormente implementado por Microsoft.

Para convertir un archivo XPS a PDF utilizando [Aspose.PDF para PHP](https://products.aspose.com/pdf/php-java), use la clase [XpsLoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/XpsLoadOptions).
 Este se utiliza para inicializar un objeto [LoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/LoadOptions). Más tarde, este objeto se pasa como argumento durante la inicialización del objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document) y ayuda al motor de renderizado de PDF a determinar el formato de entrada del documento fuente.

El siguiente fragmento de código muestra el proceso de conversión del archivo XPS en formato PDF.

```php
// Crear una nueva instancia de la clase XpsLoadOptions
$loadOption = new XpsLoadOptions();

// Crear una nueva instancia de la clase Document y cargar el archivo XPS
$document = new Document($inputFile, $loadOption);

// Guardar el documento como un archivo PDF
$document->save($outputFile);
```

{{% alert color="success" %}}
**Intenta convertir el formato XPS a PDF en línea**

Aspose.PDF para PHP te presenta la aplicación en línea gratuita ["XPS a PDF"](https://products.aspose.app/pdf/conversion/xps-to-pdf/), donde puedes intentar investigar la funcionalidad y la calidad con la que funciona.


[![Conversión de Aspose.PDF de XPS a PDF con Aplicación Gratuita](xps_to_pdf.png)](https://products.aspose.app/pdf/conversion/xps-to-pdf/){{% /alert %}}

## Convertir PostScript a PDF

**Aspose.PDF para PHP** admite características de conversión de archivos PostScript a formato PDF. Una de las características de Aspose.PDF es que puedes establecer un conjunto de carpetas de fuentes para ser utilizadas durante la conversión.

Para convertir un archivo PostScript a formato PDF, Aspose.PDF para PHP ofrece la clase [PsLoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/PsLoadOptions) que se utiliza para inicializar el objeto LoadOptions. Luego, este objeto puede pasarse como un argumento al constructor del objeto Document, lo cual ayudará al motor de renderizado de PDF a determinar el formato del documento fuente.

El siguiente fragmento de código puede usarse para convertir un archivo PostScript en formato PDF:

```php
// Crear un nuevo objeto PsLoadOptions.
$loadOption = new PsLoadOptions();

// Crear un nuevo objeto Document y cargar el archivo PS de entrada.
$document = new Document($inputFile, $loadOption);

// Guardar el documento como un archivo PDF.
$document->save($outputFile);
```

## Convertir XML a PDF

El formato XML se utiliza para almacenar datos estructurados.
 Existen varias formas de convertir <abbr title="Extensible Markup Language">XML</abbr> a PDF en Aspose.PDF.

{{% alert color="success" %}}
**Intenta convertir XML a PDF en línea**

Aspose.PDF para PHP te presenta una aplicación gratuita en línea ["XML a PDF"](https://products.aspose.app/pdf/conversion/xml-to-pdf), donde puedes investigar la funcionalidad y la calidad con la que trabaja.

[![Conversión de Aspose.PDF de XML a PDF con Aplicación Gratuita](xml_to_pdf.png)](https://products.aspose.app/pdf/conversion/xml-to-pdf)
{{% /alert %}}

Considera la opción de usar un documento XML basado en el estándar XSL-FO.

### Convertir XSL-FO a PDF

La conversión de archivos XSL-FO a PDF se puede implementar usando el objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/document) con [XslFoLoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/xslfoloadoptions).

```php
// Establecer la ruta a los archivos de muestra
$dataDir = getcwd() . DIRECTORY_SEPARATOR . "samples";
$inputFoFile = $dataDir . DIRECTORY_SEPARATOR . "sample.xslt";
$inputFile = $dataDir . DIRECTORY_SEPARATOR . "sample.xml";
$outputFile = $dataDir . DIRECTORY_SEPARATOR . "results" . DIRECTORY_SEPARATOR . 'result-xmlfo-to-pdf.pdf';

// Crear una nueva instancia de la clase XslFoLoadOptions y pasar la ruta del archivo XSL-FO de entrada
$loadOption = new XslFoLoadOptions($inputFoFile);

// Crear una nueva instancia de la clase Document y pasar el archivo XML de entrada y las opciones de carga XSL-FO
$document = new Document($inputFile, $loadOption);

// Guardar el documento PDF convertido en la ruta del archivo de salida
$document->save($outputFile);
```

## Convertir LaTeX/TeX a PDF

El formato de archivo LaTeX es un formato de archivo de texto con marcado en el derivado LaTeX de la familia de lenguajes TeX y LaTeX es un formato derivado del sistema TeX. LaTeX (ˈleɪtɛk/ lay-tek o lah-tek) es un sistema de preparación de documentos y un lenguaje de marcado de documentos. Es ampliamente utilizado para la comunicación y publicación de documentos científicos en muchos campos, incluyendo matemáticas, física y ciencias de la computación. También tiene un papel destacado en la preparación y publicación de libros y artículos que contienen materiales multilingües complejos, como sánscrito y árabe, incluyendo ediciones críticas. LaTeX utiliza el programa de composición tipográfica TeX para formatear su salida y está escrito en el lenguaje de macros TeX.

**Aspose.PDF para PHP** soporta la función de convertir archivos TeX a formato PDF y para lograr este requisito, el paquete com.aspose.pdf tiene una clase llamada [LatexLoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/LatexLoadOptions) que proporciona las capacidades para cargar archivos LaTeX y renderizar la salida en formato PDF usando la clase [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document).
 El siguiente fragmento de código muestra el proceso de conversión de un archivo LaTex a formato PDF.

```php
// Crear una nueva instancia de la clase LatexLoadOptions
$loadOption = new LatexLoadOptions();

// Crear una nueva instancia de la clase Document y cargar el archivo TeX usando TeXLoadOptions
$document = new Document($inputFile, $loadOption);

// Guardar el documento como un archivo PDF
$document->save($outputFile);
```

{{% alert color="success" %}}
**Intenta convertir LaTeX/TeX a PDF en línea**

Aspose.PDF para PHP te presenta una aplicación gratuita en línea ["LaTex a PDF"](https://products.aspose.app/pdf/conversion/tex-to-pdf), donde puedes intentar investigar la funcionalidad y la calidad con la que trabaja.

[![Aspose.PDF Conversión LaTeX/TeX a PDF con Aplicación Gratuita](latex.png)](https://products.aspose.app/pdf/conversion/tex-to-pdf)
{{% /alert %}}