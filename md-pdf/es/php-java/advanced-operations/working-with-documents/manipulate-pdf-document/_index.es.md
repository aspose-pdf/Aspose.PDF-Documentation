---
title: Manipular Documento PDF 
linktitle: Manipular Documento PDF
type: docs
weight: 30
url: /php-java/manipulate-pdf-document/
description: Este artículo contiene información sobre cómo validar un documento PDF para el estándar PDF A, cómo trabajar con TOC, cómo establecer la fecha de expiración del PDF y cómo determinar el progreso de la generación del archivo PDF.
lastmod: "2024-06-05"
---

## Validar Documento PDF para el Estándar PDF A (A 1A y A 1B)

Para validar un documento PDF para la compatibilidad con PDF/A-1a o PDF/A-1b, use el método [validate(...)](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/#validate-java.lang.String-com.aspose.pdf.PdfFormat-) de la clase [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document). Este método le permite especificar el nombre del archivo en el que se guardará el resultado y el tipo de validación requerido, la enumeración [PdfFormat](https://reference.aspose.com/pdf/java/com.aspose.pdf/PdfFormat): PDF_A_1A o PDF_A_1B.

El formato de salida XML es un formato personalizado de Aspose.
 El XML contiene una colección de etiquetas con el nombre Problem; cada etiqueta contiene los detalles de un problema en particular. El atributo ObjectID de la etiqueta Problem representa el ID del objeto específico al que este problema está relacionado. El atributo Clause representa una regla correspondiente en la especificación PDF.

```php

    // Abrir documento
    $document = new Document($inputFile);
    
    $pdfFormat =  (new PdfFormat())->PDF_A_1A;
    // Validar PDF para PDF/A-1a
    $document->validate($outputFile, $pdfFormat);
    $document->close();
```

## Trabajando con TOC

### Añadir TOC a un PDF Existente

Para añadir un TOC a un archivo PDF existente, use la clase [Heading](https://reference.aspose.com/pdf/java/com.aspose.pdf/Heading) en el paquete com.aspose.pdf. El paquete com.aspose.pdf puede tanto crear nuevos archivos PDF como manipular archivos PDF existentes. Para añadir un TOC a un PDF existente, use el paquete com.aspose.pdf.

Este fragmento de código PHP utiliza Aspose.PDF para añadir una Tabla de Contenidos (TOC) a un documento PDF existente:

```php
    // Abrir documento
    $document = new Document($inputFile);

    // Obtener acceso a la primera página del archivo PDF
    $tocPage = $document->getPages()->insert(1);

    // Crear objeto para representar la información del TOC
    $tocInfo = new TocInfo();

    $title = new TextFragment("Tabla de Contenidos");
    $title->getTextState()->setFontSize(20);
    $title->getTextState()->setFontStyle(FontStyles::$Bold);

    // Establecer el título para el TOC
    $tocInfo->setTitle($title);
    $tocPage->setTocInfo($tocInfo);

    // Crear objetos de cadena que serán utilizados como elementos del TOC
    $titles = ["Primera página", "Segunda página", "Tercera página", "Cuarta página"];

    for ($i = 0; $i < 4; $i++) {
        // Crear objeto Heading
        $heading2 = new Heading(1);

        $segment2 = new TextSegment();
        $heading2->setTocPage($tocPage);
        $heading2->getSegments()->add($segment2);

        // Especificar la página de destino para el objeto heading
        $page = $document->getPages()->get_Item($i + 2);
        $heading2->setDestinationPage($page);

        // Página de destino
        $heading2->setTop($page->getRect()->getHeight());

        // Coordenada de destino
        $segment2->setText($titles[$i]);

        // Añadir heading a la página que contiene el TOC
        $tocPage->getParagraphs()->add($heading2);
    }
    // Guardar el documento actualizado
    $document->save($outputFile);
    $document->close();
```

### Establecer diferentes TabLeaderType para diferentes niveles de TOC

Aspose.PDF también permite establecer diferentes TabLeaderType para diferentes niveles de TOC. Necesitas establecer la propiedad LineDash de FormatArray con el valor apropiado del enum TabLeaderType de la siguiente manera.

```php
    // Abrir documento
    $document = new Document($inputFile);
    $tocPage = $document->getPages()->add();

    $tocInfo = new TocInfo();

    // establecer LeaderType
    $tocInfo->setLineDash(TabLeaderType->Solid);

    $title = new TextFragment("Tabla de Contenidos");
    $title->getTextState()->setFontSize(30);
    $tocInfo->setTitle($title);

    // Agregar la sección de lista a la colección de secciones del documento Pdf
    $tocPage->setTocInfo($tocInfo);

    // Definir el formato de los cuatro niveles de lista estableciendo los márgenes izquierdos y
    // ajustes de formato de texto de cada nivel
    $fontStyles = new FontStyles();
    $tabLeaderTypes = new TabLeaderType();

    $tocInfo->setFormatArrayLength(4);
    $tocInfo->getFormatArray()[0]->getMargin()->setLeft(0);
    $tocInfo->getFormatArray()[0]->getMargin()->setRight(30);
    $tocInfo->getFormatArray()[0]->setLineDash($tabLeaderTypes->getDot());
    $tocInfo->getFormatArray()[0]->getTextState()->setFontStyle($fontStyles->getBold() | $fontStyles->getItalic());
    $tocInfo->getFormatArray()[1]->getMargin()->setLeft(10);
    $tocInfo->getFormatArray()[1]->getMargin()->setRight(30);
    $tocInfo->getFormatArray()[1]->setLineDash($tabLeaderTypes->getNone());
    $tocInfo->getFormatArray()[1]->getTextState()->setFontSize(10);
    $tocInfo->getFormatArray()[2]->getMargin()->setLeft(20);
    $tocInfo->getFormatArray()[2]->getMargin()->setRight(0);
    $tocInfo->getFormatArray()[2]->getTextState()->setFontStyle($fontStyles->getBold());
    $tocInfo->getFormatArray()[3]->setLineDash($tabLeaderTypes->getSolid());
    $tocInfo->getFormatArray()[3]->getMargin()->setLeft(30);
    $tocInfo->getFormatArray()[3]->getMargin()->setRight(30);
    $tocInfo->getFormatArray()[3]->getTextState()->setFontStyle($fontStyles->getBold());

    // Crear una sección en el documento Pdf
    $page = $document->getPages()->add();

    // Agregar cuatro encabezados en la sección
    for ($Level = 1; $Level <= 4; $Level++) {
      $heading2 = new Heading($Level);
      $segment2 = new TextSegment();

      $heading2->getSegments()->add($segment2);
      $heading2->setAutoSequence(true);
      $heading2->setTocPage($tocPage);

      $segment2->setText("Encabezado de Muestra" . $Level);
      $fontRepository = new FontRepository();
      $heading2->getTextState()->setFont($fontRepository->findFont("Arial UnicodeMS"));

      // Agregar el encabezado en la Tabla de Contenidos.
      $heading2->setInList(true);
      $page->getParagraphs()->add($heading2);
    }

    // Guardar el documento actualizado
    $document->save($outputFile);
    $document->close();
```


### Ocultar Números de Página en TOC

En caso de que no desee mostrar números de página, junto con los encabezados en TOC, puede usar la propiedad [ShowPageNumbers](https://reference.aspose.com/pdf/java/com.aspose.pdf/tocinfo/#setShowPageNumbers-boolean-) de la Clase [TOCInfo](https://reference.aspose.com/pdf/java/com.aspose.pdf/tocinfo) como falsa. Por favor revise el siguiente fragmento de código para ocultar los números de página en la tabla de contenido:

```php
    // Abrir documento
    $document = new Document();
    $tocPage = $document->getPages()->add();
    
    // Crear objeto para representar la información del TOC
    $tocInfo = new TocInfo();

    $title = new TextFragment("Tabla de Contenidos");
    $title->getTextState()->setFontSize(20);
    $title->getTextState()->setFontStyle(FontStyles::$Bold);

    // Establecer el título para el TOC
    $tocInfo->setTitle($title);

    // Agregar la sección de lista a la colección de secciones del documento Pdf
    $tocPage->setTocInfo($tocInfo);

    // Definir el formato de la lista de cuatro niveles estableciendo los márgenes izquierdos y
    // configuraciones de formato de texto de cada nivel

    $tocInfo->setShowPageNumbers(false);
    $tocInfo->setFormatArrayLength(4);
    $tocInfo->getFormatArray()[0]->getMargin()->setRight(0);
    $tocInfo->getFormatArray()[0]->getTextState()->setFontStyle(FontStyles::$Bold | FontStyles::$Italic);

    $tocInfo->getFormatArray()[1]->getMargin()->setLeft(30);
    $tocInfo->getFormatArray()[1]->getTextState()->setUnderline(true);
    $tocInfo->getFormatArray()[1]->getTextState()->setFontSize(10);

    $tocInfo->getFormatArray()[2]->getTextState()->setFontStyle(FontStyles::$Bold);
    $tocInfo->getFormatArray()[3]->getTextState()->setFontStyle(FontStyles::$Bold);

    $page = $document->getPages()->add();

    // Agregar cuatro encabezados en la sección
    for ($Level = 1; $Level < 5; $Level++) {
      $heading2 = new Heading($Level);
      $segment2 = new TextSegment();
      $heading2->setTocPage($tocPage);
      $heading2->getSegments()->add($segment2);
      $heading2->setAutoSequence(true);
      $segment2->setText("esto es encabezado de nivel " + $Level);
      $heading2->setInList(true);
      $page->getParagraphs()->add($heading2);
    }
     
    // Guardar el documento actualizado
    $document->save($outputFile);
    $document->close();
```


### Personalizar los Números de Página al agregar TOC

Es común personalizar la numeración de las páginas en el TOC al agregar TOC en un documento PDF. Por ejemplo, podemos necesitar añadir algún prefijo antes del número de página como P1, P2, P3 y así sucesivamente. En tal caso, Aspose.PDF para PHP vía Java proporciona la propiedad PageNumbersPrefix de la clase TocInfo que puede ser utilizada para personalizar los números de página como se muestra en el siguiente ejemplo de código.

```php

    // Abrir documento
    $document = new Document($inputFile);

    // Obtener acceso a la primera página del archivo PDF
    $tocPage = $document->getPages()->insert(1);

    // Crear objeto para representar la información del TOC
    $tocInfo = new TocInfo();

    $title = new TextFragment("Tabla de Contenidos");
    $title->getTextState()->setFontSize(20);
    $title->getTextState()->setFontStyle(FontStyles::$Bold);

    // Establecer el título para el TOC
    $tocInfo->setTitle($title);
    $tocInfo->setPageNumbersPrefix("P");
    $tocPage->setTocInfo($tocInfo);

    // Crear objetos de cadena que se usarán como elementos del TOC
    $titles = ["Primera página", "Segunda página", "Tercera página", "Cuarta página"];

    for ($i = 0; $i < 4; $i++) {
        // Crear objeto de Encabezado
        $heading2 = new Heading(1);

        $segment2 = new TextSegment();
        $heading2->setTocPage($tocPage);
        $heading2->getSegments()->add($segment2);

        // Especificar la página de destino para el objeto de encabezado
        $page = $document->getPages()->get_Item($i + 2);
        $heading2->setDestinationPage($page);

        // Página de destino
        $heading2->setTop($page->getRect()->getHeight());

        // Coordenada de destino
        $segment2->setText($titles[$i]);

        // Añadir encabezado a la página que contiene el TOC
        $tocPage->getParagraphs()->add($heading2);
    }
    // Guardar el documento actualizado
    $document->save($outputFile);
    $document->close();
```


## Añadir Capas al Archivo PDF

Las capas se pueden usar en documentos PDF de muchas maneras. Puede que tengas un archivo multilingüe que deseas distribuir y quieres que el texto en cada idioma aparezca en diferentes capas, con el diseño de fondo apareciendo en una capa separada. También puedes crear documentos con animación que aparece en una capa separada. Un ejemplo podría ser añadir un acuerdo de licencia a tu archivo, y no quieres que un usuario vea el contenido hasta que acepte los términos del acuerdo.

Aspose.PDF para PHP a través de Java admite la adición de capas a archivos PDF.

Para trabajar con capas en archivos PDF, usa los siguientes miembros de la API.

La clase [Layer](https://reference.aspose.com/pdf/java/com.aspose.pdf/Layer) representa una capa y contiene las siguientes propiedades:

- **Name** – el nombre de la capa.
- **Id** – el ID de la capa.
- **Contents** – una lista de operadores de la capa.

Una vez que los objetos [Layer](https://reference.aspose.com/pdf/java/com.aspose.pdf/Layer) han sido definidos, añádelos a la colección de capas del objeto [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page).
 El siguiente código muestra cómo agregar capas a un documento PDF.

```php
    // Abrir documento
    $document = new Document($inputFile);
    $page = $document->getPages()->add();
    $arrayList = new java("java.util.ArrayList");
    $page->setLayers($arrayList);

    $layer = new $layer("oc1", "Línea Roja");
    $layer->getContents()->add(new operators_SetRGBColorStroke(1, 0, 0));
    $layer->getContents()->add(new operators_MoveTo(500, 700));
    $layer->getContents()->add(new operators_LineTo(400, 700));
    $layer->getContents()->add(new operators_Stroke());    
    $page->getLayers()->add($layer);

    $layer = new $layer("oc2", "Línea Verde");
    $layer->getContents()->add(new operators_SetRGBColorStroke(0, 1, 0));
    $layer->getContents()->add(new operators_MoveTo(500, 750));
    $layer->getContents()->add(new operators_LineTo(400, 750));
    $layer->getContents()->add(new operators_Stroke());
    $page->getLayers()->add($layer);

    $layer = new $layer("oc3", "Línea Azul");
    $layer->getContents()->add(new operators_SetRGBColorStroke(0, 0, 1));
    $layer->getContents()->add(new operators_MoveTo(500, 800));
    $layer->getContents()->add(new operators_LineTo(400, 800));
    $layer->getContents()->add(new operators_Stroke());
    $page->getLayers()->add($layer);
    
    // Guardar el documento actualizado
    $document->save($outputFile);
    $document->close();
```

## Establecer la Expiración de PDF

La función de expiración de PDF establece cuánto tiempo es válido un archivo PDF. En una fecha particular, si alguien intenta acceder a él, se muestra un mensaje emergente explicando que el archivo ha expirado y que necesitan uno nuevo.

Aspose.PDF te permite establecer la expiración al crear y editar archivos PDF.

El fragmento de código a continuación muestra cómo establecer la fecha de expiración para un archivo PDF. Necesitas usar JavaScript ya que los archivos guardados por componentes de terceros (por ejemplo, OwnerGuard) no pueden ser vistos en otras estaciones de trabajo sin esa utilidad.

El archivo PDF puede ser creado usando PDF OwnerGuard usando un archivo existente con una fecha de expiración. Pero el nuevo archivo solo puede abrirse en una estación de trabajo que tenga instalado PDF OwnerGuard. Las estaciones de trabajo sin PDF OwnerGuard mostrarán un ExpirationFeatureError. Por ejemplo, PDF Reader abre el archivo si OwnerGuard está instalado, pero Adobe Acrobat devuelve un error.

```php

    // Abrir documento
    $document = new Document($inputFile);
       
    $javaScript = new JavascriptAction(
      "var year=2020;" + 
      "var month=4;" + 
      "var today = new Date(); today = new Date(today.getFullYear(), today.getMonth());" +
      "var expiry = new Date(year, month);" +
      "if (today.getTime() > expiry.getTime())" + 
      "app.alert('El archivo ha expirado. Necesitas uno nuevo.');"
      );
    $document->setOpenAction($javaScript);
    $document->save($outputFile);
    $document->close();
```