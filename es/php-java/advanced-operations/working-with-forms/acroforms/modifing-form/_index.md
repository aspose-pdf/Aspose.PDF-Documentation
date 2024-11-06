---
title: Modificando AcroForms
linktitle: Modificando AcroForms
type: docs
weight: 40
url: es/java/modifing-form/
description: Esta sección explica cómo modificar formularios en su documento PDF con Aspose.PDF para PHP vía Java.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Establecer Fuente de Campo de Formulario Personalizada

Los campos de formulario en archivos PDF de Adobe pueden configurarse para usar fuentes predeterminadas específicas. Aspose.PDF permite a los desarrolladores aplicar cualquier fuente como fuente predeterminada del campo, ya sea una de las 14 fuentes principales o una fuente personalizada.
Para establecer y actualizar la fuente predeterminada utilizada para los campos de formulario, Aspose.PDF tiene la clase DefaultAppearance (Font font, double size, Color color). Esta clase se puede acceder usando com.aspose.pdf.DefaultAppearance. Para usar este objeto, utilice el método setDefaultAppearance(..) de la clase Field.

El siguiente fragmento de código le muestra cómo establecer la fuente predeterminada para el campo de formulario PDF.

```php

    // Abrir un documento
    $document = new Document($inputFile);

    // Obtener un campo de formulario particular del documento
    $field = $document->getForm()->get("textbox1");

    // Crear objeto de fuente
    $fontRepository = new FontRepository();
    $font = $fontRepository->findFont("ComicSansMS");

    $colors = new Color();
    $blackColor = $colors->getBlack();

    // Establecer la información de la fuente para el campo de formulario
    $field->setDefaultAppearance(new DefaultAppearance($font, 10, $blackColor));

    // Guardar el documento actualizado
    $document->save($outputFile);
    $document->close();        

    $document->close();
```


## Get/Set FieldLimit

Este código demuestra el uso de la clase [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) para abrir un documento, recuperar un campo de formulario, establecer su longitud máxima, recuperar la longitud máxima con los métodos 'setMaxLen' y 'getMaxLen'.

```php

    // Abrir un documento
    $document = new Document($inputFile);

    // Obtener un campo de formulario particular del documento
    $field = $document->getForm()->get("textbox1");
    
    $field->setMaxLen(10);

    // Obtener el límite máximo del campo usando DOM
    $responseData = "Límite: " . $field->getMaxLen();          

    $document->close();
```

También puede obtener el mismo valor usando el espacio de nombres Aspose.PDF.Facades con el siguiente fragmento de código.

```php

    // Abrir un documento
    $document = new Document($inputFile);

    // Obtener un campo de formulario particular del documento
    $field = $document->getForm()->get("textbox1");

    // Obtener el límite máximo del campo usando DOM
    $responseData = "Límite: " . $field->getMaxLen();          

    $document->close();
```


Del mismo modo, Aspose.PDF tiene un método que obtiene el límite del campo utilizando el enfoque DOM. El siguiente fragmento de código muestra los pasos.

```php

    // Abrir un documento
    $document = new Document($inputFile);

    // Obtener un campo de formulario particular del documento
    $field = $document->getForm()->get("textbox1");

    // Eliminar campo
    $field->delete();
    
    $document->close();
```
## Eliminar un Campo de Formulario Particular de un Documento PDF

Todos los campos de formulario están contenidos en la colección de Form del objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document). Esta colección proporciona diferentes métodos que gestionan los campos de formulario, incluyendo el método delete. Si deseas eliminar un campo particular, pasa el nombre del campo como un parámetro al método delete y luego guarda el documento PDF actualizado.

El siguiente fragmento de código muestra cómo eliminar un campo nombrado de un documento PDF.

```php

    // Abrir un documento
    $document = new Document($inputFile);

    // Obtener un campo de formulario particular del documento
    $field = $document->getForm()->get("textbox1");

    // Eliminar campo
    $field->delete();
    
    $document->close();
```


## Modificar Campo de Formulario en un Documento PDF

La colección de Formularios del objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) te permite gestionar los campos de formulario en un documento PDF.

Para modificar un campo de formulario, obtén el campo de la colección de Formularios y establece sus propiedades. Luego guarda el documento PDF actualizado.

El siguiente fragmento de código muestra cómo modificar un campo de formulario existente en un documento PDF.

```php

    // Abrir un documento
    $document = new Document($inputFile);

    // Obtener un campo de formulario particular del documento
    $field = $document->getForm()->get("textbox1");

    // Modificar el valor del campo
    $field->setValue("Valor Actualizado");

    // Establecer el campo como solo lectura
    $field->setReadOnly(true);

    // Guardar el documento actualizado
    $document->save($outputFile);        
    $document->close();
```

### Mover Campo de Formulario a una Nueva Ubicación en un Archivo PDF

Si deseas mover un campo de formulario a una nueva ubicación en una página PDF, primero obtén el objeto del campo y luego especifica un nuevo valor para su método setRect.
 Un objeto [Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf/Rectangle) con nuevas coordenadas se asigna al método setRect(..). Luego, guarde el PDF actualizado usando el método save del objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).

El siguiente fragmento de código le muestra cómo mover un campo de formulario a una nueva ubicación.

```php

    // Abrir un documento
    $document = new Document($inputFile);

    // Obtener un campo de formulario en particular del documento
    $field = $document->getForm()->get("textbox1");

    // Modificar la ubicación del campo
    $field->setRect(new Rectangle(300, 400, 600, 500));

    // Guardar el documento actualizado
    $document->save($outputFile);        
    $document->close();
```