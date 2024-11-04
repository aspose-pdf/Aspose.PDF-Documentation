---
title: Creando un PDF complejo
linktitle: Creando un PDF complejo
type: docs
weight: 60
url: /php-java/complex-pdf-example/
description: Aspose.PDF para PHP a través de Java le permite crear documentos más complejos que contienen imágenes, fragmentos de texto y tablas en un solo documento.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

El ejemplo de [Hola, Mundo](/pdf/php-java/hello-world-example/) mostró pasos simples para crear un documento PDF usando Aspose.PDF. En este artículo, echaremos un vistazo a la creación de un documento más complejo con Aspose.PDF para PHP a través de Java. Como ejemplo, tomaremos un documento de una empresa ficticia que opera servicios de ferry para pasajeros.

Si creamos un documento desde cero, necesitamos seguir ciertos pasos:

1. Instanciar un objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document). En este paso crearemos un documento PDF vacío con algunos metadatos pero sin páginas.

1. Añadir una [Página](https://reference.aspose.com/pdf/java/com.aspose.pdf/page) al objeto documento. Así, ahora nuestro documento tendrá una página.
1. Añadir una [Imagen](https://reference.aspose.com/pdf/java/com.aspose.pdf/image). Es una operación compleja basada en acciones de bajo nivel con operadores PDF.
    - Cargar imagen desde el flujo
    - Añadir imagen a la colección de Imágenes de los Recursos de la Página
    - Usar el operador GSave: este operador guarda el estado gráfico actual.
    - Crear un objeto [Matriz](https://reference.aspose.com/pdf/java/com.aspose.pdf/matrix/).
    - Usar el operador ConcatenateMatrix: define cómo debe colocarse la imagen.
    - Usar el operador Do: este operador dibuja la imagen.
    - Usar el operador GRestore: este operador restaura el estado gráfico.
1. Crear un [FragmentoDeTexto](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFragment) para el encabezado. Para el encabezado usaremos la fuente Arial con tamaño de fuente 24pt y alineación centrada.

1. Agregar encabezado a la página [Párrafos](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page#getParagraphs--).
1. Crear un [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFragment) para la descripción. Para la descripción usaremos la fuente Arial con tamaño de fuente 24pt y alineación centrada.
1. Agregar (descripción) a los Párrafos de la página.
1. Crear una tabla, agregar propiedades de la tabla.
1. Agregar (tabla) a los [Párrafos](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page#getParagraphs--) de la página.
1. Guardar un documento "Complejo.pdf".

```php

    $document = new Document();
    //Agregar página
    $page = $document->getPages()->add();
    // -------------------------------------------------------------
    // Agregar imagen
    $imageFileName = $dataDir . DIRECTORY_SEPARATOR . 'logo.png';
    $page->AddImage($imageFileName, new Rectangle(20, 730, 120, 830));

    // -------------------------------------------------------------
    // Agregar Encabezado
    $fontRepository = new FontRepository();
    $fontArial = $fontRepository->findFont("Arial");

    $header = new TextFragment("Nuevas rutas de ferry en otoño 2020");
    $header->getTextState()->setFont($fontArial);
    $header->getTextState()->setFontSize(24);
    $header->setHorizontalAlignment(2);
    $header->setPosition(new Position(130, 720));
    $page->getParagraphs()->add($header);

    // Agregar descripción
    $descriptionText = "Los visitantes deben comprar boletos en línea y los boletos están limitados a 5,000 por día. El servicio de ferry está operando a media capacidad y con un horario reducido. Espere filas.";
    $description = new TextFragment($descriptionText);
    $description->getTextState()->setFont($fontRepository->findFont("Times New Roman"));
    $description->getTextState()->setFontSize(14);
    $header->setHorizontalAlignment(1);
    $page->getParagraphs()->add($description);

    // Agregar tabla
    $table = new Table();
    $table->setColumnWidths("200");

    $colors = new Color();
    $darkSlateGrayColor = $colors->getDarkSlateGray();
    $blackColor = $colors->getBlack();
    $grayColor = $colors->getGray();
    $whiteSmokeColor = $colors->getWhiteSmoke();

    $table->setBorder(new BorderInfo(BorderSide::$Box, 1.0, $darkSlateGrayColor));
    $table->setDefaultCellBorder(new BorderInfo(BorderSide::$Box, 0.5, $blackColor));
    $table->getMargin()->setBottom(10);
    $table->getDefaultCellTextState()->setFont($fontRepository->findFont("Helvetica"));

    $headerRow = $table->getRows()->add();

    $headerRowCell = $headerRow->getCells()->add("Sale de la ciudad");
    $headerRowCell->setBackgroundColor($grayColor);
    $headerRowCell->getDefaultCellTextState()->setForegroundColor($whiteSmokeColor);

    $headerRowCell = $headerRow->getCells()->add("Sale de la isla");
    $headerRowCell->setBackgroundColor($grayColor);
    $headerRowCell->getDefaultCellTextState()->setForegroundColor($whiteSmokeColor);

    $timenow = new DateTime('06:00');

    for ($i = 0; $i < 10; $i++) {
        $dataRow = $table->getRows()->add();
        $cell = $dataRow->getCells()->add($timenow->format('H:i'));
        $timenow->add(new DateInterval('PT30M'));
        $dataRow->getCells()->add($timenow->format('H:i'));
    }

    $page->getParagraphs()->add($table);

    $document->save($outputFile);
```