---
title: Formateo del Documento PDF 
linktitle: Formateo del Documento PDF
type: docs
weight: 20
url: /es/php-java/formatting-pdf-document/
description: Formatear el Documento PDF con Aspose.PDF para PHP a través de Java. Use el siguiente fragmento de código para resolver sus tareas.
lastmod: "2024-06-05"
---

## Obtener Propiedades de la Ventana del Documento y la Visualización de Páginas

Este tema le ayuda a entender cómo obtener las propiedades de la ventana del documento, la aplicación del visor, y cómo se muestran las páginas.

Para establecer estas diferentes propiedades, abra el archivo PDF usando la clase [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document). Ahora puede obtener los métodos del objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document), tales como

- [isCenterWindow](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#isCenterWindow--) – Centrar la ventana del documento en la pantalla. Predeterminado: false.
- [setDirection](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#setDirection-int-) – Orden de lectura.
 Esto determina cómo se disponen las páginas cuando se muestran una al lado de la otra. Predeterminado: de izquierda a derecha.
- [isDisplayDocTitle](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#isDisplayDocTitle--) – Muestra el título del documento en la barra de título de la ventana del documento. Predeterminado: falso (el título se muestra).
- [isHideMenubar](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/#isHideMenubar--) – Obtiene el indicador que especifica si la barra de menú debe estar oculta cuando el documento está activo.
- [isHideToolBar](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/#isHideToolBar--) – Obtiene el indicador que especifica si la barra de herramientas debe estar oculta cuando el documento está activo.
- [isHideWindowUI](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/#isHideWindowUI--) – Obtiene el indicador que especifica si los elementos de la interfaz de usuario deben estar ocultos cuando el documento está activo.

- [getNonFullScreenPageMode](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/#getNonFullScreenPageMode--) – Obtiene el modo de página, especificando cómo mostrar el documento al salir del modo de pantalla completa.- [getPageLayout](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/#getPageLayout--) – El diseño de la página.
- [getPageMode](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/#getPageMode--) – Obtiene el modo de página, especificando cómo se debe mostrar el documento cuando se abre.

El siguiente fragmento de código te muestra cómo obtener las propiedades usando la clase [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).

```php  

    // Abrir documento
    $document = new Document($inputFile);

    // Obtener diferentes propiedades del documento
    // Posición de la ventana del documento - Predeterminado: false
    $responseData = "CenterWindow : " . $document->isCenterWindow();

    // Orden de lectura predominante; determina la posición de la página
    // cuando se muestra lado a lado - Predeterminado: L2R
    $responseData = $responseData . "Direction : " . $document->getDirection();

    // Si la barra de título de la ventana debe mostrar el título del documento.
    // Si es falso, la barra de título muestra el nombre del archivo PDF - Predeterminado: false
    $responseData = $responseData . "DisplayDocTitle : " . $document->isDisplayDocTitle();

    // Si redimensionar la ventana del documento para ajustar el tamaño de
    // la primera página mostrada - Predeterminado: false
    $responseData = $responseData . "FitWindow : " . $document->isFitWindow();

    // Si ocultar la barra de menú de la aplicación del visor - Predeterminado: false
    $responseData = $responseData . "HideMenuBar :" . $document->isHideMenubar();

    // Si ocultar la barra de herramientas de la aplicación del visor - Predeterminado: false
    $responseData = $responseData . "HideToolBar :" . $document->isHideToolBar();

    // Si ocultar elementos de la interfaz de usuario como barras de desplazamiento
    // dejando solo el contenido de la página mostrado - Predeterminado: false
    $responseData = $responseData . "HideWindowUI :" . $document->isHideWindowUI();

    // El modo de página del documento. Cómo mostrar el documento al salir
    // del modo de pantalla completa.
    $responseData = $responseData . "NonFullScreenPageMode :" . $document->getNonFullScreenPageMode();

    // El diseño de la página, es decir, página única, una columna
    $responseData = $responseData . "PageLayout :" . $document->getPageLayout();

    // Cómo debe mostrarse el documento cuando se abre.
    $responseData = $responseData . "Page Mode :" . $document->getPageMode();
    $document->close();  
```


## Establecer las Propiedades de la Ventana del Documento y la Visualización de la Página

Este tema explica cómo establecer las propiedades de la ventana del documento, la aplicación del visor y la visualización de la página.

Para establecer estas diferentes propiedades:

1. Abra el archivo PDF utilizando la clase [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).
1. Establezca las propiedades del objeto Document.
1. Guarde el archivo PDF actualizado utilizando el método Save.

Los métodos disponibles son:

- [setCenterWindow](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#setCenterWindow-boolean-)
- [setDirection](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#setDirection-int-)
- [setDisplayDocTitle](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#setDisplayDocTitle-boolean-)
- [setFitWindow](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#setFitWindow-boolean-)
- [setHideMenuBar](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#setHideMenubar-boolean-)

- [setHideToolBar](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#setHideToolBar-boolean-)
- [setHideWindowUI](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#setHideWindowUI-boolean-)
- [setNonFullScreenPageMode](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#setNonFullScreenPageMode-int-)
- [setPageLayout](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#setPageLayout-int-)
- [setPageMode](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#setPageMode-int-)

El siguiente fragmento de código te muestra cómo establecer las propiedades usando la clase [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).

```php

    // Abrir documento
    $document = new Document($inputFile);
    // Establecer diferentes propiedades del documento
    // especificar para posicionar la ventana del documento - Predeterminado: false
    $document->setCenterWindow(true);
    // Orden de lectura predominante; determinar la posición de la página
    // cuando se muestra lado a lado - Predeterminado: L2R
    $document->setDirection(Direction::$R2L);
    // Especificar si la barra de título de la ventana debe mostrar el título del documento
    // si es false, la barra de título muestra el nombre del archivo PDF - Predeterminado: false
    $document->setDisplayDocTitle(true);
    // Especificar si redimensionar la ventana del documento para ajustar el tamaño de
    // la primera página mostrada - Predeterminado: false
    $document->setFitWindow(true);
    // Especificar si ocultar la barra de menú de la aplicación del visor - Predeterminado:
    // false
    $document->setHideMenubar(true);
    // Especificar si ocultar la barra de herramientas de la aplicación del visor - Predeterminado:
    // false
    $document->setHideToolBar(true);
    // Especificar si ocultar elementos de la interfaz de usuario como barras de desplazamiento
    // dejando solo el contenido de la página mostrado - Predeterminado: false
    $document->setHideWindowUI(true);
    // Modo de página del documento. especificar cómo mostrar el documento al salir
    // del modo de pantalla completa.
    $document->setNonFullScreenPageMode(PageMode::$UseOC);
    // Especificar el diseño de página, es decir, página única, una columna
    $document->setPageLayout(PageLayout::$TwoColumnLeft);
    // Especificar cómo se debe mostrar el documento al abrirlo
    // es decir, mostrar miniaturas, pantalla completa, mostrar panel de adjuntos
    $document->setPageMode(PageMode::$UseThumbs);
    // Guardar archivo PDF actualizado
    $document->save($outputFile);
    $document->close();

```


## Incrustar Fuentes en un Archivo PDF Existente

Los lectores de PDF soportan [un núcleo de 14 fuentes](http://en.wikipedia.org/wiki/Portable_Document_Format#Fonts) para que los documentos puedan mostrarse de la misma manera independientemente de la plataforma en la que se muestre el documento. Cuando un PDF contiene una fuente que está fuera del núcleo de fuentes, incruste la fuente para evitar la sustitución de fuentes.

Aspose.PDF para PHP a través de Java soporta la incrustación de fuentes en documentos PDF existentes. Puede incrustar una fuente completa o un subconjunto. Para incrustar la fuente:

1. Abra un archivo PDF existente usando la clase [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).
1. Use la clase [com.aspose.pdf.Font](https://reference.aspose.com/pdf/java/com.aspose.pdf/Font) para incrustar la fuente.
   1. El método setEmbedded(true) incrusta la fuente completa.
   1. El [método isSubset(true)](https://reference.aspose.com/pdf/java/com.aspose.pdf/font/#isSubset--) incrusta un subconjunto de la fuente.

Un subconjunto de fuente incrusta solo los caracteres que se utilizan y es útil donde las fuentes se utilizan para oraciones cortas o eslóganes, por ejemplo, donde una fuente corporativa se utiliza para un logotipo, pero no para el texto del cuerpo.
 Usar un subconjunto reduce el tamaño del archivo del PDF de salida.

Sin embargo, si se utiliza una fuente personalizada para el texto del cuerpo, incrústala en su totalidad.

El siguiente fragmento de código muestra cómo incrustar una fuente en un archivo PDF.

```php

    // Abrir documento
    $document = new Document($inputFile);
    $pages = $document->getPages();
    for ($i = 1; $i <= $pages->size(); $i++) {
      $page = $pages->get_Item($i);
      $fonts = $page->getResources()->getFonts();
      if (!is_null($fonts)) {
        for ($fontIndex = 1; $fontIndex <= $fonts->size(); $fontIndex++) {
          $pageFont = $fonts->get_Item($fontIndex);
          // Verificar si la fuente ya está incrustada
          if (!$pageFont->isEmbedded())
            $pageFont->setEmbedded(true);
        }
      }
      $forms = $page->getResources()->getForms();
      // Verificar los objetos de Formulario
      for ($formIndex = 0; $formIndex < -$forms->size(); $formIndex++) {
        $formFonts = $forms->get_Item($formIndex)->getResources()->getFonts();
        if (!is_null($formFonts)) {
          for ($fontIndex = 1; $fontIndex <= $formFonts->size(); $fontIndex++) {
            $pageFont = $formFonts->get_Item($fontIndex);
            // Verificar si la fuente ya está incrustada
            if (!$pageFont->isEmbedded())
              $pageFont->setEmbedded(true);
          }
        }
      }
      $responseData = "Ok";
    }

    // Guardar archivo PDF actualizado
    $document->save($outputFile);
    $document->close();
```

## Incrustación de Fuentes al crear PDF

Si necesitas usar cualquier fuente diferente a las 14 fuentes principales soportadas por Adobe Reader, entonces debes incrustar la descripción de la fuente al generar un archivo PDF. Si la información de la fuente no está incrustada, Adobe Reader la tomará del Sistema Operativo si está instalada en el sistema, o construirá una fuente sustituta según el descriptor de fuente en el PDF. Ten en cuenta que la fuente incrustada debe estar instalada en la máquina anfitriona, es decir, en el caso del siguiente código, la fuente 'Univers Condensed' está instalada en el sistema.

Usamos la propiedad setEmbedded de la clase [Font](https://reference.aspose.com/pdf/java/com.aspose.pdf/Font) para incrustar la información de la fuente en el archivo PDF. Establecer el valor de esta propiedad a ‘true' incrustará el archivo completo de la fuente en el PDF, sabiendo que esto aumentará el tamaño del archivo PDF. A continuación se muestra el fragmento de código que se puede usar para incrustar la información de la fuente en el PDF.

```php

    // Crear una instancia del objeto PDF llamando a su constructor vacío
    $document = new Document();

    // Crear una sección en el objeto Pdf
    $page = $document->getPages()->add();
    $fragment = new TextFragment("");
    $segment = new TextSegment("Este es un texto de muestra usando una fuente personalizada.");

    $fontRepository = new FontRepository();

    $ts = new TextState();
    $ts->setFont($fontRepository->findFont("Univers Condensed"));
    $ts->getFont()->setEmbedded(true);
    $segment->setTextState($ts);
    $fragment->getSegments()->add($segment);
    $page->getParagraphs()->add($fragment);

    // Guardar el archivo PDF actualizado
    $document->save($outputFile);
    $document->close();
```


## Establecer el Nombre de Fuente Predeterminada al Guardar PDF

Cuando un documento PDF contiene fuentes que no están disponibles en el documento mismo ni en el dispositivo, la API reemplaza estas fuentes con la fuente predeterminada. Cuando una fuente está disponible (está instalada en el dispositivo o está incrustada en el documento), el PDF de salida debería tener la misma fuente (no debería ser reemplazada por la fuente predeterminada). El valor de la fuente predeterminada debe contener el nombre de la fuente (no la ruta a los archivos de fuente). Hemos implementado una característica para establecer el nombre de la fuente predeterminada al guardar un documento como PDF. El siguiente fragmento de código se puede usar para establecer la fuente predeterminada:

```php

    // Cargar un documento PDF existente
    $document = new Document($inputFile);
    $newName = "Arial";

    // Inicializar las opciones de guardado para el formato PDF
    $ops = new PdfSaveOptions();

    // Establecer el nombre de la fuente predeterminada
    $ops->setDefaultFontName($newName);

    // Guardar el archivo PDF
    $document->save($outputFile, $ops);
    // Guardar el archivo PDF actualizado
    $document->close();
```

## Obtener Todas las Fuentes del Documento PDF

En caso de que desee obtener todas las fuentes de un documento PDF, puede utilizar el método **Document.getFontUtilities().getAllFonts()** proporcionado en la clase [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).
 Por favor, revise el siguiente fragmento de código para obtener todas las fuentes de un documento PDF existente:

```php

    // Cargar un documento PDF existente
    $document = new Document($inputFile);

    // Obtener todas las fuentes del documento
    $fonts = $document->getFontUtilities()->getAllFonts();
    foreach ($fonts as $font) {
      $responseData = $responseData . $f->getFontName() . PHP_EOL;
    }

    // Guardar el archivo PDF actualizado
    $document->close();
```

## Obtener-Establecer Factor de Zoom del Archivo PDF

A veces, desea establecer u obtener el factor de zoom de un documento PDF. Puede lograr fácilmente este requisito con Aspose.PDF.

El objeto [GoToAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/GoToAction) le permite obtener el valor de zoom asociado con un archivo PDF. De manera similar, se puede usar para establecer el factor de Zoom de un archivo.

```php

    // Cargar un documento PDF existente
    $document = new Document($inputFile);

    // Crear objeto GoToAction
    $action = $document->getOpenAction();

    // Obtener el factor de Zoom del archivo PDF
    $responseData = $action->getDestination()->getZoom();

    // Guardar el archivo PDF actualizado
    $document->close();  
```

El siguiente fragmento de código muestra cómo obtener el factor de zoom de un archivo PDF.

```php

    // Cargar un documento PDF existente
    $document = new Document($inputFile);
    $zoom = 0.5;
    // establecer el factor de zoom del documento
    $page = $document->getPages()->get_Item(1);
    $actionzoom = new GoToAction(
      new XYZExplicitDestination($page, $page->getMediaBox()->getWidth(), $page->getMediaBox()->getHeight(), $zoom)
    );

    // establecer acción para ajustar al ancho de página con zoom
    $actionFitToWidth = new GoToAction(
      new FitHExplicitDestination($page, $page->getMediaBox()->getWidth())
    );

    // establecer acción para ajustar al alto de página con zoom
    $actionFittoHeight = new GoToAction(
      new FitVExplicitDestination( $page, $page->getMediaBox()->getHeight())
    );

    $document->setOpenAction($actionzoom);
    $document->setOpenAction($actionFittoWidth);
    $document->setOpenAction($actionFittoHeight);

    // Guardar archivo PDF actualizado
    $document->save($outputFile);
    $document->close();  
```