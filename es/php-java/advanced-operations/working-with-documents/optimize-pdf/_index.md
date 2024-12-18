---
title: Optimizar, Comprimir o Reducir el Tamaño del PDF en PHP
linktitle: Optimizar Documento PDF
type: docs
weight: 40
url: /es/php-java/optimize-pdf/
description: Optimizar archivo PDF, reducir todas las imágenes, reducir tamaño PDF, Desincrustar fuentes, Eliminar objetos no utilizados usando PHP.
lastmod: "2024-06-05"
---

Un documento PDF a veces puede contener datos adicionales. Reducir el tamaño de un archivo PDF te ayudará a optimizar la transferencia de red y el almacenamiento. Esto es especialmente útil para publicar en páginas web, compartir en redes sociales, enviar por correo electrónico o archivar en el almacenamiento. Podemos usar varias técnicas para optimizar PDF:

- Optimizar el contenido de la página para la navegación en línea
- Reducir o comprimir todas las imágenes
- Habilitar la reutilización del contenido de la página
- Fusionar flujos duplicados
- Desincrustar fuentes
- Eliminar objetos no utilizados
- Eliminar o aplanar campos de formulario
- Eliminar o aplanar anotaciones

## Optimizar Documento PDF para la Web

La optimización o linealización se refiere al proceso de hacer un archivo PDF adecuado para la navegación en línea usando un navegador web.
 Aspose.PDF admite este proceso.

Para optimizar un PDF para visualización web:

1. Abra el documento de entrada en un objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).
1. Utilice el método [optimize()](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#optimize--).
1. Guarde el documento optimizado usando el método save(..).

El siguiente fragmento de código muestra cómo optimizar un documento PDF para la web.

```php

    // Abrir documento
    $document = new Document($inputFile);

    // Optimizar para la web
    $document->optimize();

    // Guardar el documento actualizado
    $document->save($outputFile);
    $document->close();
```

## Reducir el tamaño del archivo PDF

Este tema explica los pasos para optimizar/reducir el tamaño del archivo PDF. Aspose.PDF API proporciona la clase [OptimizationOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf.optimization/class-use/OptimizationOptions) que ofrece la flexibilidad para optimizar el PDF de salida eliminando objetos innecesarios y comprimiendo archivos PDF que tienen imágenes. Ambas opciones se explican en las siguientes secciones.

### Eliminar Objetos Innecesarios

Podemos optimizar el tamaño de los documentos PDF eliminando objetos duplicados y no utilizados. El siguiente fragmento de código muestra cómo.

```php

    // Abrir documento
    $document = new Document($inputFile);
    
    // Optimizar el documento PDF. Sin embargo, tenga en cuenta que este método no puede garantizar
    // la reducción del documento
    $document->optimizeResources();

    // Guardar el documento actualizado
    $document->save($outputFile);
    $document->close();

```

## Reducir o Comprimir Todas las Imágenes

Si el archivo PDF fuente contiene imágenes, considere comprimir las imágenes y establecer su calidad. Para habilitar la compresión de imágenes, pase true como un argumento al método setCompressImages(..). Todas las imágenes en un documento serán re-comprimidas. La compresión se define por el método setImageQuality(..), que es el valor de la calidad en porcentaje. 100% es calidad y tamaño de imagen sin cambios. Para disminuir el tamaño de la imagen, pase un argumento de menos de 100 al método setImageQuality(..).

```php

    // Abrir documento
    $document = new Document($inputFile);
    
    // Inicializar OptimizationOptions
    $optimizationOptions = new OptimizationOptions();

    // Establecer opción CompressImages
    $optimizationOptions->getImageCompressionOptions()->setCompressImages(true);

    // Establecer opción ImageQuality
    $optimizationOptions->getImageCompressionOptions()->setImageQuality(50);

    // Optimizar documento PDF usando OptimizationOptions
    $document->optimizeResources($optimizationOptions);

    // Guardar el documento actualizado
    $document->save($outputFile);
    $document->close();
```

Otra forma es redimensionar las imágenes con una resolución más baja. En este caso, deberíamos establecer ResizeImages a true y MaxResolution al valor apropiado.

```php

    // Abrir documento
    $document = new Document($inputFile);
    
    // Inicializar OptimizationOptions
    $optimizationOptions = new OptimizationOptions();

    // Establecer opción CompressImages
    $optimizationOptions->getImageCompressionOptions()->setCompressImages(true);
    
    // Establecer opción ImageQuality
    $optimizationOptions->getImageCompressionOptions()->setImageQuality(75);

    // Establecer opción ResizeImage
    $optimizationOptions->getImageCompressionOptions()->setResizeImages(true);

    // Establecer opción MaxResolution
    $optimizationOptions->getImageCompressionOptions()->setMaxResolution(300);

    // Guardar el documento actualizado
    $document->save($outputFile);
    $document->close();
```

Otro asunto importante es el tiempo de ejecución. Pero nuevamente, podemos gestionar esta configuración también. Actualmente, podemos usar dos algoritmos: Estándar y Rápido. Para controlar el tiempo de ejecución debemos establecer una propiedad de Versión. El siguiente fragmento demuestra el algoritmo Rápido:

```php
    // Abrir documento
    $document = new Document($inputFile);
    
    // Inicializar OptimizationOptions
    $optimizationOptions = new optimization_OptimizationOptions();

    // Establecer opción CompressImages
    $optimizationOptions->getImageCompressionOptions()->setCompressImages(true);

    // Establecer opción ImageQuality
    $optimizationOptions->getImageCompressionOptions()->setImageQuality(75);
    $optimization_ImageCompressionVersion = new optimization_ImageCompressionVersion();

    // Establecer la versión de compresión de imágenes a rápida
    $optimizationOptions->getImageCompressionOptions()->setVersion($optimization_ImageCompressionVersion->Fast);

    // Optimizar documento PDF usando OptimizationOptions
    $document->optimizeResources($optimizationOptions);

    // Guardar el documento actualizado
    $document->save($outputFile);
    $document->close();
```

## Eliminando Objetos No Utilizados

Un documento PDF a veces contiene los objetos PDF que no están referenciados desde ningún otro objeto en el documento. Esto puede suceder, por ejemplo, cuando se elimina una página del árbol de páginas del documento pero el objeto de la página en sí no se elimina. Eliminar estos objetos no hace que el documento sea inválido, sino que lo reduce.

```php

    // Abrir documento
    $document = new Document($inputFile);
    
    // Inicializar OptimizationOptions
    $optimizationOptions = new OptimizationOptions();

    $optimizationOptions->setRemoveUnusedObjects(true);

    // Optimizar el documento PDF usando OptimizationOptions
    $document->optimizeResources($optimizationOptions);

    // Guardar el documento actualizado
    $document->save($outputFile);
    $document->close();
```

## Eliminando Flujos No Utilizados

A veces, un documento contiene flujos de recursos no utilizados.
 Estos flujos no son “objetos no utilizados” porque están referenciados desde el diccionario de recursos de una página. Esto puede suceder en casos donde una imagen ha sido eliminada de la página pero no de los recursos de la página. Además, esta situación ocurre a menudo cuando las páginas son extraídas del documento y las páginas del documento tienen recursos “comunes”, es decir, el mismo objeto Resources. Se analizan los contenidos de la página para determinar si un flujo de recursos se utiliza o no. Los flujos no utilizados son eliminados. A veces esto disminuye el tamaño del documento.

```php

    // Abrir documento
    $document = new Document($inputFile);
    
    // Inicializar OptimizationOptions
    $optimizationOptions = new OptimizationOptions();

    $optimizationOptions->setRemoveUnusedStreams(true);

    // Optimizar documento PDF usando OptimizationOptions
    $document->optimizeResources($optimizationOptions);

    // Guardar el documento actualizado
    $document->save($outputFile);
    $document->close();
```

## Vinculación de Flujos Duplicados

A veces un documento contiene varios flujos de recursos idénticos (por ejemplo, imágenes). Esto puede ocurrir, por ejemplo, cuando un documento se concatena consigo mismo. El documento de salida contiene dos copias independientes del mismo flujo de recursos. Analizamos todos los flujos de recursos y los comparamos. Si los flujos están duplicados, se fusionan, es decir, solo se deja una copia, las referencias se cambian adecuadamente y se eliminan las copias del objeto. A veces, esto disminuye el tamaño del documento.

```php
    // Abrir documento
    $document = new Document($inputFile);
    
    // Inicializar OptimizationOptions
    $optimizationOptions = new OptimizationOptions();
    
    $optimizationOptions->setLinkDuplcateStreams(true);
    
    // Optimizar documento PDF usando OptimizationOptions
    $document->optimizeResources($optimizationOptions);

    // Guardar el documento actualizado
    $document->save($outputFile);
    $document->close();
```

Adicionalmente, podemos usar la configuración AllowReusePageContent. Si esta propiedad se establece en true, el contenido de la página se reutilizará al optimizar el documento para páginas idénticas.

```php
    // Abrir documento
    $document = new Document($inputFile);
    
    // Inicializar OptimizationOptions
    $optimizationOptions = new OptimizationOptions();

    $optimizationOptions->setAllowReusePageContent(true);

    // Optimizar documento PDF usando OptimizationOptions
    $document->optimizeResources($optimizationOptions);

    // Guardar el documento actualizado
    $document->save($outputFile);
    $document->close();
```

## Desincrustar Fuentes

Si el documento utiliza fuentes incrustadas, significa que todos los datos de las fuentes se colocan en el documento. La ventaja es que el documento es visible independientemente de si la fuente está instalada en la máquina del usuario o no. Pero incrustar fuentes hace que el documento sea más grande. El método desincrustar fuentes elimina todas las fuentes incrustadas. Esto disminuye el tamaño del documento, pero el documento puede volverse ilegible si la fuente correcta no está instalada.

```php

    // Abrir documento
    $document = new Document($inputFile);
    
    // Inicializar OptimizationOptions
    $optimizationOptions = new OptimizationOptions();

    $optimizationOptions->setUnembedFonts(true);

    // Optimizar documento PDF usando OptimizationOptions
    $document->optimizeResources($optimizationOptions);

    // Guardar el documento actualizado
    $document->save($outputFile);
    $document->close();
```

## Eliminación o Aplanamiento de Anotaciones

Las anotaciones pueden ser eliminadas cuando son innecesarias.
 Cuando son necesarios pero no requieren edición adicional, pueden ser aplanados. Ambas técnicas reducirán el tamaño del archivo.

```php

    // Abrir documento
    $document = new Document($inputFile);
    $pages = $document->getPages();

    for ($i=1; $i < $pages->size() ; $i++) { 
        $page = $pages->get_Item($i);
        $annotations = $page->getAnnotations();
        for ($idx=0; $idx < $annotations->size(); $idx++) { 
            $annotation = $annotations->get_Item($idx);
            $annotation->flatten();
        }
    }
     
    // Guardar el documento actualizado
    $document->save($outputFile);
    $document->close();
```

## Eliminando Campos de Formulario

Si el documento PDF contiene AcroForms, podemos intentar reducir el tamaño del archivo aplanando los campos del formulario.

```php

    // Abrir documento
    $document = new Document($inputFile);
    
    // Aplanar Formularios
    $fields = $document->getForm()->getFields();
    foreach ($fields as $field) {
        $field->flatten();
    }            

    // Guardar el documento actualizado
    $document->save($outputFile);
    $document->close();
```

## Convertir un PDF de espacio de color RGB a escala de grises

Un archivo PDF se compone de Texto, Imagen, Anexo, Anotaciones, Gráficos y otros objetos. Puede encontrar un requisito para convertir un PDF de espacio de color RGB a escala de grises para que sea más rápido al imprimir esos archivos PDF. Además, cuando el archivo se convierte a escala de grises, el tamaño del documento también se reduce, pero con este cambio, la calidad del documento puede disminuir. Actualmente, esta característica es compatible con la función Pre-Flight de Adobe Acrobat, pero cuando se habla de automatización de Office, Aspose.PDF es una solución definitiva para proporcionar tales ventajas para la manipulación de documentos.

Para cumplir con este requisito, se puede utilizar el siguiente fragmento de código.

```php

    // Abrir documento
    $document = new Document($inputFile);
    
    $strategy = new RgbToDeviceGrayConversionStrategy();
    for ($idxPage = 1; $idxPage <= $document->getPages()->size(); $idxPage++) {
        $page = $document->getPages()->get_Item($idxPage);
        $strategy->convert($page);
    }          

    // Guardar el documento actualizado
    $document->save($outputFile);
    $document->close();
```


## Compresión FlateDecode

Aspose.PDF para PHP a través de Java proporciona soporte para la compresión FlateDecode para la funcionalidad de optimización de PDF. El siguiente fragmento de código muestra cómo usar la opción en Optimización para almacenar imágenes con compresión FlateDecode:

```php

    // Abrir documento
    $document = new Document($inputFile);

    // Inicializar OptimizationOptions
    $optimizationOptions = new OptimizationOptions();

    $optimizationOptions->setUnembedFonts(true);

    // Optimizar documento PDF usando OptimizationOptions
    $optimizationOptions->getImageCompressionOptions()->setEncoding(optimization_ImageEncoding::$Flate);

    // Guardar el documento actualizado
    $document->save($outputFile);
    $document->close();
```

## Almacenar imagen en XImageCollection

Aspose.PDF para PHP a través de Java proporciona la capacidad de almacenar nuevas imágenes en [XImageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/XImageCollection) con compresión FlateDecode.
 Para habilitar esta opción, puede utilizar la bandera ImageFilterType.Flate. El siguiente fragmento de código muestra cómo usar esta funcionalidad:

```php
    // Abrir documento
    $document = new Document($inputFile);

    // Inicializar Documento
    $page = $document->getPages()->get_Item(1);

    // Cargar imagen en el flujo
    $imageStream = new java("java.io.FileInputStream",$inputFile);
    $imageFilterType = new ImageFilterType();
    $page->getResources()->getImages()->add($imageStream, $imageFilterType->Flate);
    $idx = $page->getResources()->getImages()->size();
    $ximage = $page->getResources()->getImages()->get_Item($idx);
    $page->getContents()->add(new operators_GSave());

    // Establecer coordenadas
    $lowerLeftX = 0;
    $lowerLeftY = 0;
    $upperRightX = 600;
    $upperRightY = 600;
    $rectangle = new Rectangle($lowerLeftX, $lowerLeftY, $upperRightX, $upperRightY);
    $matrixData = [
        $rectangle->getURX() - $rectangle->getLLX(), 0, 
        0, $rectangle->getURY() - $rectangle->getLLY(), 
        $rectangle->getLLX(), $rectangle->getLLY()];
    $matrix = new Matrix($matrixData);

    // Usando el operador ConcatenateMatrix (concatenar matriz): define cómo debe colocarse la imagen
    $page->getContents()->add(new operators_ConcatenateMatrix($matrix));
    $page->getContents()->add(new operators_Do($ximage->getName()));
    $page->getContents()->add(new operators_GRestore());

    // Guardar el documento actualizado
    $document->save($outputFile);
    $document->close();
```