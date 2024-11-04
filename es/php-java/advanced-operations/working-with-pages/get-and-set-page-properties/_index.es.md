---
title: Obtener y Establecer Propiedades de Página
type: docs
weight: 30
url: /php-java/get-and-set-page-properties/
description: Este tema explica cómo obtener números en un archivo PDF, obtener propiedades de página y determinar el color de la página usando Aspose.PDF para PHP a través de Java.
lastmod: "2024-06-05"
---

Aspose.PDF para PHP a través de Java te permite leer y establecer propiedades de las páginas en un archivo PDF en tus aplicaciones Java. Esta sección muestra cómo obtener el número de páginas en un archivo PDF, obtener información sobre las propiedades de la página PDF como el color y establecer propiedades de página.

## Obtener el Número de Páginas en un Archivo PDF

Cuando trabajas con documentos, a menudo quieres saber cuántas páginas contienen. Con Aspose.PDF esto no toma más de dos líneas de código.

Para obtener el número de páginas en un archivo PDF:

1. Abre el archivo PDF usando la clase [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).
1. Luego se recuperan las páginas del documento. Se intenta obtener el conteo de páginas de las páginas recuperadas.

El siguiente fragmento de código muestra cómo obtener el número de páginas de un archivo PDF.

```php

    // Abrir documento
    $document = new Document($inputFile);      

    $pages = $document->getPages();

    // Obtener número de páginas
    $responseData = $responseData . "Número de páginas : " + $pages->size();
```

### Obtener el número de páginas sin guardar el documento

A menos que el archivo PDF esté guardado y todos los elementos estén realmente colocados dentro del archivo PDF, no podemos obtener el número de páginas para un documento en particular (porque no podemos estar seguros sobre el número de páginas en las que todos los elementos se acomodarán). Sin embargo, comenzando con el lanzamiento de Aspose.PDF para PHP a través de Java, hemos introducido un método llamado [processParagraphs(...)](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#processParagraphs--) que proporciona la función para obtener el número de páginas para un documento PDF, sin guardar el archivo. Así que podemos obtener información del número de páginas sobre la marcha. Por favor intente usar el siguiente fragmento de código para cumplir con este requisito.

```php

    // Abrir documento
    $document = new Document($inputFile);      

    // añadir página a la colección de páginas del archivo PDF
    $page = $document->getPages()->add();
    
    // crear un bucle para agregar 300 instancias de TextFragment
    for ($i=0; $i < 300; $i++) { 
       // agregar TextFragment a la colección de párrafos de la primera página del PDF
       $page->getParagraphs()->add(new TextFragment("Prueba de conteo de páginas"));
    }
    
    // procesar párrafos para obtener información del número de páginas
    $document->processParagraphs();

    $pages = $document->getPages();

    // Obtener número de páginas
    $responseData = $responseData . "Número de páginas : " + $pages->size();
```


## Obtener Propiedades de la Página

Cada página en un archivo PDF tiene una serie de propiedades, como el ancho, alto, caja de sangrado, recorte y caja de corte. Aspose.PDF te permite acceder a estas propiedades.

### **Comprendiendo las Propiedades de la Página: la Diferencia entre Artbox, BleedBox, CropBox, MediaBox, TrimBox y la propiedad Rect**

- **Caja de medios**: La caja de medios es la caja de página más grande. Corresponde al tamaño de la página (por ejemplo, A4, A5, Carta de EE. UU., etc.) seleccionado cuando el documento fue impreso a PostScript o PDF. En otras palabras, la caja de medios determina el tamaño físico del medio en el que se muestra o imprime el documento PDF.
- **Caja de sangrado**: Si el documento tiene sangrado, el PDF también tendrá una caja de sangrado.
 Bleed es la cantidad de color (o arte) que se extiende más allá del borde de una página. Se utiliza para asegurarse de que cuando el documento se imprima y se corte al tamaño (“recortado”), la tinta llegue hasta el borde de la página. Incluso si la página se corta mal - cortada ligeramente fuera de las marcas de recorte - no aparecerán bordes blancos en la página.
- **Trim box**: El trim box indica el tamaño final de un documento después de imprimirlo y recortarlo.
- **Art box**: El art box es el cuadro dibujado alrededor del contenido real de las páginas en sus documentos. Este cuadro de página se utiliza al importar documentos PDF en otras aplicaciones.
- **Crop box**: El crop box es el tamaño de “página” en el que su documento PDF se muestra en Adobe Acrobat. En vista normal, solo se muestran los contenidos del crop box en Adobe Acrobat.
  Para descripciones detalladas de estas propiedades, lea la especificación de Adobe.Pdf, particularmente 10.10.1 Límites de Página.
- **Page.Rect**: la intersección (comúnmente rectángulo visible) de MediaBox y DropBox. La imagen a continuación ilustra estas propiedades.

Para más detalles, por favor visite [esta página](http://www.enfocus.com/manuals/ReferenceGuide/PP/10/enUS/en-us/concept/c_aa1095731.html).

### Accediendo a las Propiedades de la Página

El siguiente fragmento de código obtiene propiedades como ArtBox, BleedBox, CropBox, MediaBox, TrimBox, Rect, Número de Página y Rotación para una página específica en el documento. Luego almacena los datos extraídos en variables separadas y los concatena en una cadena de respuesta.

1. Crea un nuevo objeto Document usando la variable $inputFile.
1. Obtiene la colección de páginas del documento usando el método getPages().
1. Obtiene una página específica de la colección de páginas usando el método get_Item().
1. Extrae varias propiedades (ArtBox, BleedBox, CropBox, MediaBox, TrimBox, Rect, Número de Página, Rotación) del objeto de página específico y las almacena en variables separadas.
1. El código concatena los valores de las propiedades extraídas en cadenas de respuesta separadas ($responseData1, $responseData2, etc.).
1. A continuación, intenta recuperar el conteo de páginas usando el método size() en el objeto $pages, pero la variable $pages no está definida.

El siguiente fragmento de código muestra cómo obtener propiedades de la página.

```php

   // Abrir documento
    $document = new Document($inputFile);

    // Obtener la colección de páginas
    $pageCollection = $document->getPages();

    // Obtener una página específica
    $page = $pageCollection->get_Item(1);

    // Obtener las propiedades de la página
    $responseData1 = "ArtBox : Altura = " . $page->getArtBox()->getHeight()
        . ", Ancho = " . $page->getArtBox()->getWidth()
        . ", LLX = " . $page->getArtBox()->getLLX()
        . ", LLY = " . $page->getArtBox()->getLLY()
        . ", URX = " . $page->getArtBox()->getURX()
        . ", URY = " . $page->getArtBox()->getURY()
        . PHP_EOL;

    $responseData2 = "BleedBox : Altura = " . $page->getBleedBox()->getHeight() . ", Ancho = "
        . $page->getBleedBox()->getWidth() . ", LLX = " . $page->getBleedBox()->getLLX() . ", LLY = "
        . $page->getBleedBox()->getLLY() . ", URX = " . $page->getBleedBox()->getURX() . ", URY = "
        . $page->getBleedBox()->getURY()
        . PHP_EOL;

    $responseData3 = "CropBox : Altura = " . $page->getCropBox()->getHeight() . ", Ancho = "
        . $page->getCropBox()->getWidth() . ", LLX = " . $page->getCropBox()->getLLX() . ", LLY = "
        . $page->getCropBox()->getLLY() . ", URX = " . $page->getCropBox()->getURX() . ", URY = "
        . $page->getCropBox()->getURY()
        . PHP_EOL;

    $responseData4 = " MediaBox : Altura = " . $page->getMediaBox()->getHeight() . ", Ancho = "
        . $page->getMediaBox()->getWidth() . ", LLX = " . $page->getMediaBox()->getLLX() . ", LLY = "
        . $page->getMediaBox()->getLLY() . ", URX = " . $page->getMediaBox()->getURX() . ", URY = "
        . $page->getMediaBox()->getURY()
        . PHP_EOL;

    $responseData5 = " TrimBox : Altura = " . $page->getTrimBox()->getHeight() . ", Ancho = "
        . $page->getTrimBox()->getWidth() . ", LLX = " . $page->getTrimBox()->getLLX() . ", LLY = "
        . $page->getTrimBox()->getLLY() . ", URX = " . $page->getTrimBox()->getURX() . ", URY = "
        . $page->getTrimBox()->getURY()
        . PHP_EOL;

    $responseData5 = " Rect : Altura = " . $page->getRect()->getHeight() . ", Ancho = " . $page->getRect()->getWidth()
        . ", LLX = " . $page->getRect()->getLLX() . ", LLY = " . $page->getRect()->getLLY() . ", URX = "
        . $page->getRect()->getURX() . ", URY = " . $page->getRect()->getURY()
        . PHP_EOL;
        
    $responseData6 = " Número de página :- " . $page->getNumber() . PHP_EOL;
    $responseData7 = " Rotación :-" . $page->getRotate() . PHP_EOL;

    // Obtener el conteo de páginas
    $responseData8 = $responseData8 . "Conteo de páginas : " . $pages->size();
```


## Determinar el Color de la Página

La clase [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) proporciona las propiedades relacionadas con una página particular en un documento PDF, incluyendo qué tipo de color - RGB, blanco y negro, escala de grises o indefinido - usa la página.

Todas las páginas de los archivos PDF están contenidas por la colección [PageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/PageCollection). La propiedad [ColorType](https://reference.aspose.com/pdf/java/com.aspose.pdf/ColorType) especifica el color de los elementos en la página. Para obtener o determinar la información del color para una página PDF en particular, use la propiedad [ColorType](https://reference.aspose.com/pdf/java/com.aspose.pdf/ColorType) del objeto de la clase [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page).

El siguiente fragmento de código muestra cómo iterar a través de páginas individuales de un archivo PDF para obtener información de color.

```php

    // Abrir documento
    $document = new Document($inputFile);

    // Iterar a través de todas las páginas del archivo PDF
    for ($pageCount = 1; $pageCount <= $document->getPages()->size(); $pageCount++) {

        // Obtener la información del tipo de color para una página PDF en particular
        $pageColorType = $document->getPages()->get_Item($pageCount)->getColorType();

        switch ($pageColorType) {
            case 2:
                $responseData ="Página # -" . $pageCount . " es Blanco y negro..";
                break;
            case 1:
                $responseData ="Página # -" . $pageCount . " es Escala de grises...";
                break;
            case 0:
                $responseData ="Página # -" . $pageCount . " es RGB..";
                break;
            case 3:
                $responseData ="Página # -" . $pageCount . " Color es indefinido..";
                break;
        }
    }
```