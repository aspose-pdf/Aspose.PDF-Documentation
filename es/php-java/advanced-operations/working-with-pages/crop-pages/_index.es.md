---
title: Recortar Páginas de PDF usando PHP
linktitle: Recortar Páginas
type: docs
weight: 80
url: /php-java/crop-pages/
description: Puede obtener propiedades de la página, como el ancho, la altura, bleed-, crop- y trimbox usando Aspose.PDF para PHP vía Java.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Obtener Propiedades de la Página

Cada página en un archivo PDF tiene una serie de propiedades, como el ancho, la altura, bleed-, crop- y trimbox. Aspose.PDF para PHP vía Java le permite acceder a estas propiedades.

- **Caja de medios**: La caja de medios es la caja de página más grande. Corresponde al tamaño de la página (por ejemplo A4, A5, Carta US, etc.) seleccionado cuando el documento fue impreso en PostScript o PDF. En otras palabras, la caja de medios determina el tamaño físico del medio en el que se muestra o imprime el documento PDF.
- **Caja de sangrado**: Si el documento tiene sangrado, el PDF también tendrá una caja de sangrado.
 Bleed es la cantidad de color (o ilustración) que se extiende más allá del borde de una página. Se utiliza para asegurarse de que cuando el documento se imprima y corte al tamaño ("recortado"), la tinta llegue hasta el borde de la página. Incluso si la página se corta incorrectamente - cortada ligeramente fuera de las marcas de recorte - no aparecerán bordes blancos en la página.

- **Trim box**: El trim box indica el tamaño final de un documento después de imprimir y recortar.
- **Art box**: El art box es el cuadro dibujado alrededor del contenido real de las páginas en sus documentos. Este cuadro de página se utiliza al importar documentos PDF en otras aplicaciones.
- **Crop box**: El crop box es el tamaño de "página" en el que se muestra su documento PDF en Adobe Acrobat. En vista normal, solo se muestran los contenidos del crop box en Adobe Acrobat. Para descripciones detalladas de estas propiedades, lea la especificación Adobe.Pdf, particularmente 10.10.1 Límites de Página.
- **Page.Rect**: la intersección (comúnmente rectángulo visible) de MediaBox y DropBox. La imagen a continuación ilustra estas propiedades. Para más detalles, por favor visita [esta página](http://www.enfocus.com/manuals/ReferenceGuide/PP/10/enUS/en-us/concept/c_aa1095731.html).

El fragmento a continuación muestra cómo recortar la página:

```php

    // Abrir documento
    $document = new Document($inputFile);      

    $page = $document->getPages()->get_Item(1);

    $responseData = $page->getCropBox() . PHP_EOL;
    $responseData = $responseData . $page->getTrimBox() . PHP_EOL;
    $responseData = $responseData . $page->getArtBox() . PHP_EOL;
    $responseData = $responseData . $page->getBleedBox() . PHP_EOL;
    $responseData = $responseData . $page->getMediaBox() . PHP_EOL;

    // Crear nuevo Rectángulo Box
    $newBox = new Rectangle(200, 220, 2170, 1520);

    $page->setCropBox($newBox);
    $page->setTrimBox($newBox);
    $page->setArtBox($newBox);
    $page->setBleedBox($newBox);

    // Guardar documento de salida
    $document->save($outputFile);
    $document->close();
```

En este ejemplo usamos un archivo de muestra [aquí](crop_page.pdf). Initially nuestra página se ve como se muestra en la Figura 1.
![Figura 1. Página Recortada](crop_page.png)

Después del cambio, la página se verá como la Figura 2.
![Figura 2. Página Recortada](crop_page2.png)