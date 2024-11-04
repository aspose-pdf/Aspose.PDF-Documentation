---
title:  Extraer datos de AcroForm 
linktitle:  Extraer datos de AcroForm
type: docs
weight: 50
url: /php-java/extract-data-from-acroform/
description: AcroForms existe en muchos documentos PDF. Este artículo tiene como objetivo ayudarle a entender cómo extraer datos de AcroForms usando PHP y Aspose.PDF.
lastmod: "2024-05-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Extraer campos de formulario de un documento PDF

Aspose.PDF para PHP no solo le permite crear y rellenar campos de formulario, sino que también facilita la extracción de datos de campos de formulario o información de campos de formulario de archivos PDF.

Supongamos que no conocemos los nombres de los campos del formulario de antemano. Entonces deberíamos iterar sobre cada página en el PDF para extraer información sobre todos los AcroForms en el PDF así como los valores de los campos del formulario. Para acceder al formulario necesitamos usar el método [getForm](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#getForm--).

```php

    // Crear una nueva instancia de la clase License y establecer el archivo de licencia
    $licenceObject = new License();
    $licenceObject->setLicense($license);

    // Establecer la ruta al directorio que contiene el documento PDF
    $dataDir = getcwd() . DIRECTORY_SEPARATOR . "samples";

    // Establecer la ruta al archivo PDF de entrada
    $inputFile = $dataDir . DIRECTORY_SEPARATOR . "StudentInfoFormElectronic.pdf";

    // Establecer el encabezado de respuesta para indicar que la respuesta estará en formato JSON
    header('Content-Type: application/json; charset=utf-8');

    // Inicializar la variable de datos de respuesta
    $responseData = "";

    try {
        // Crear una nueva instancia de la clase Document y cargar el archivo PDF de entrada
        $document = new Document($inputFile);

        // Obtener los campos del formulario del documento y convertirlos a valores de PHP
        $fields = java_values($document->getForm()->getFields());

        // Recorrer cada campo del formulario y extraer el nombre y el valor del campo
        foreach ($fields as $formField) {
            // Concatenar el nombre del campo y el valor a los datos de respuesta
            $responseData = $responseData . "(Nombre del Campo: " . $formField->getPartialName() . " |";
            $responseData = $responseData . " Valor: " . $formField->getValue() . "),";
        }

        // Cerrar el documento
        $document->close();
    }
```


Si conoces el nombre de los campos de formulario de los que deseas extraer valores, puedes usar el indexador en la colección Documents.Form para recuperar rápidamente estos datos.

## Extraer Datos a XML desde un Archivo PDF

La clase Form permite exportar datos a un archivo XML desde el archivo PDF usando el método ExportXml. Para exportar datos a XML, necesitas crear un objeto de la clase Form y luego llamar al método ExportXml usando el objeto FileStream. Finalmente, puedes cerrar el objeto FileStream y disponer del objeto Form. El siguiente fragmento de código muestra cómo exportar datos a un archivo XML.

```php

    // Abrir documento
    $form = new facades_Form();
    $form->bindPdf($inputFile);

    // Crear un objeto FileOutputStream para escribir el archivo de fuente.
    $xmlOutputStream = new java("java.io.FileOutputStream", "output.xml");

    // Exportar datos
    $form->exportXml($xmlOutputStream);

    // Cerrar el flujo de archivo
    $xmlOutputStream->close();

    // Cerrar el documento
    $form->close();
```

## Exportar Datos a FDF desde un Archivo PDF

Para exportar datos de formularios PDF a un archivo XFDF, podemos usar el método [exportFdf](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Form#exportFdf-java.io.OutputStream-) en la clase [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Form).

Por favor, tenga en cuenta que es una clase de `com.aspose.pdf.facades`. A pesar del nombre similar, esta clase tiene un propósito ligeramente diferente.

Para exportar datos a FDF, necesita crear un objeto de la clase `Form` y luego llamar al método `exportXfdf` usando el objeto `OutputStream`. El siguiente fragmento de código le muestra cómo exportar datos a un archivo XFDF.

```php

    // Abrir documento
    $form = new facades_Form();
    $form->bindPdf($inputFile);

    // Crear un objeto FileOutputStream para escribir el archivo de fuente.
    $xmlOutputStream = new java("java.io.FileOutputStream", "output.fdf");

    // Exportar datos
    $form->exportFdf($xmlOutputStream);

    // Cerrar flujo de archivo
    $xmlOutputStream->close();

    // Cerrar el documento
    $form->close();
```

## Exportar Datos a XFDF desde un Archivo PDF

Para exportar datos de formularios PDF a un archivo XFDF, podemos usar el método [exportXfdf](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Form#exportXfdf-java.io.OutputStream-) en la clase [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Form).

Para exportar datos a XFDF, necesitas crear un objeto de la clase `Form` y luego llamar al método `exportXfdf` usando el objeto `OutputStream`.
El siguiente fragmento de código te muestra cómo exportar datos a un archivo XFDF.

```php

    // Abrir documento
    $form = new facades_Form();
    $form->bindPdf($inputFile);

    // Crear un objeto FileOutputStream para escribir el archivo de fuentes.
    $xmlOutputStream = new java("java.io.FileOutputStream", "output.xfdf");

    // Exportar datos
    $form->exportXfdf($xmlOutputStream);

    // Cerrar el flujo de archivo
    $xmlOutputStream->close();

    // Cerrar el documento
    $form->close();
```