---
title: Añadir sellos de texto en PDF programáticamente
linktitle: Sellos de texto en archivo PDF
type: docs
weight: 20
url: /php-java/text-stamps-in-the-pdf-file/
description: Añadir un sello de texto a un archivo PDF usando la clase TextStamp con PHP.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Añadir sello de texto con Java

Aspose.PDF para PHP a través de Java proporciona la clase [TextStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextStamp) para añadir un sello de texto en un archivo PDF.
 La clase [TextStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextStamp) proporciona los métodos necesarios para especificar el tamaño de fuente, el estilo de fuente y el color de fuente, etc., para el objeto de sello. Para agregar un sello de texto, primero necesitas crear un objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) y un objeto [TextStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextStamp) usando los métodos requeridos. Después de eso, puedes llamar al método [addStamp(..)](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page#addStamp-com.aspose.pdf.Stamp-) de la clase [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) para agregar el sello en el documento PDF.

El siguiente fragmento de código te muestra cómo agregar un sello de texto en el archivo PDF.

```php

    // Abrir documento
    $document = new Document($inputFile);        
    $pages = $document->getPages();
    $colors = new Color();
    // crear sello de texto
    $textStamp = new TextStamp("Sello de Muestra");
    // establecer si el sello es de fondo
    $textStamp->setBackground(true);
    // establecer origen
    $textStamp->setXIndent(100);
    $textStamp->setYIndent(100);
    // rotar sello
    $textStamp->setRotate((new Rotation())->On90);    
    // establecer propiedades de texto
    $fontRepository = new FontRepository();
    $fontStyles = new FontStyles();
    $textStamp->getTextState()->setFont($fontRepository->findFont("Arial"));
    $textStamp->getTextState()->setFontSize(14);
    $textStamp->getTextState()->setFontStyle($fontStyles->Bold | $fontStyles->Italic);
    $textStamp->getTextState()->setForegroundColor($colors->getGreen());

    // agregar sello a la página particular
    $pages->get_Item(1)->addStamp($textStamp);

    // Guardar documento de salida
    $document->save($outputFile);
    $document->close();
```

## Definir alineación para el objeto TextStamp

Agregar marcas de agua a documentos PDF es una de las características frecuentemente demandadas y Aspose.PDF para PHP a través de Java es totalmente capaz de agregar marcas de agua de imagen así como de texto. La clase [TextStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextStamp) proporciona la funcionalidad para agregar sellos de texto sobre el archivo PDF. Recientemente ha habido un requisito para soportar la función de especificar la alineación del texto al usar el objeto [TextStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextStamp). Así que para satisfacer este requisito, hemos introducido el método setTextAlignment(..) en la clase [TextStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextStamp). Usando este método, puede especificar la alineación horizontal del texto.

Los siguientes fragmentos de código muestran un ejemplo de cómo cargar un documento PDF existente y agregar [TextStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextStamp) sobre él.

```php

    // Abrir documento
    $document = new Document($inputFile);        
    $pages = $document->getPages();
    $colors = new Color();

    // instanciar objeto FormattedText con cadena de muestra
    $text = new FormattedText("This");

    // agregar nueva línea de texto a FormattedText
    $text->addNewLineText("es un ejemplo");
    $text->addNewLineText("Centrado");
    $text->addNewLineText("TextStamp");
    $text->addNewLineText("Objeto");
    
    // crear sello de texto
    $textStamp = new TextStamp($text);

    // especificar la alineación horizontal del sello de texto como centrado
    $textStamp->setHorizontalAlignment((new HorizontalAlignment)->getCenter());
    // especificar la alineación vertical del sello de texto como centrado
    $textStamp->setVerticalAlignment((new VerticalAlignment())->getCenter);
    // especificar la alineación horizontal del texto del TextStamp como centrado
    $textStamp->setTextAlignment((new HorizontalAlignment)->getCenter());
    // establecer margen superior para el objeto sello
    $textStamp->setTopMargin(20);
    
    // agregar sello a una página en particular
    $pages->get_Item(1)->addStamp($textStamp);

    // Guardar documento de salida
    $document->save($outputFile);
    $document->close();  
```


## Rellenar el Texto de Trazo como Sello en un Archivo PDF

Hemos implementado la configuración del modo de renderizado para escenarios de adición y edición de texto. Para renderizar texto de trazo, por favor crea un objeto [TextState](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextState) y establece RenderingMode a TextRenderingMode.StrokeText y también selecciona el color para la propiedad StrokingColor. Luego, vincula TextState al sello usando el método bindTextState().

El siguiente fragmento de código demuestra cómo agregar Texto de Relleno de Trazo:

```php

   // Crear objeto TextState para transferir propiedades avanzadas
    $ts = new TextState();
        
    // Establecer color para el trazo
    $ts->setStrokingColor((new Color())->getGray());

    // Establecer modo de renderizado de texto
    $ts->setRenderingMode(TextRenderingMode::$StrokeText);

    // Cargar un documento PDF de entrada
    $fileStamp = new PdfFileStamp(new Document($inputFile));

    $stamp = new Stamp();
    $stamp->bindLogo(
        new FormattedText("PAGADO EN SU TOTALIDAD",
            (new Color())->getGray(), "Arial",
            facades_EncodingType::$WinAnsi,
            true, 78));

    // Vincular TextState
    $stamp->bindTextState($ts);
    
    // Establecer origen X,Y
    $stamp->setOrigin(100, 100);
    $stamp->setOpacity (5);
    $stamp->setBlendingSpace(BlendingColorSpace::$DeviceRGB);
    $stamp->setRotation (45.0);
    $stamp->setBackground(false);

    // Añadir Sello
    $fileStamp->addStamp($stamp);
    $fileStamp->save($outputFile);
    $fileStamp->close();
```