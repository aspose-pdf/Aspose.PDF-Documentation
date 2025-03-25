---
title: Importar y Exportar Datos en JSON
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 80
url: /es/net/import-export-json/
description: Esta sección explica cómo importar y exportar datos en JSON
lastmod: "2024-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Import and Export Data in JSON",
    "alternativeHeadline": "Enhance PDF Form Management with JSON Import/Export",
    "abstract": "La nueva función permite la importación y exportación sin problemas de datos de formularios PDF utilizando el formato JSON, proporcionando una forma sencilla de manipular campos de formularios en documentos. Los usuarios pueden utilizar varios métodos, incluidos FileStream y MemoryStream, para gestionar datos de manera eficiente, asegurando flexibilidad ya sea trabajando con documentos completos o campos específicos. Esta funcionalidad mejora los flujos de trabajo de procesamiento de datos, haciendo que la gestión de formularios PDF sea más simple y efectiva.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "Import Data, Export Data, JSON format, Form fields, Aspose.PDF library, FieldSerializationResult, ExportFieldsToJsonOptions, FileStream, MemoryStream, Specific field export/import",
    "wordcount": "1255",
    "proficiencyLevel": "Beginner",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF for .NET",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
        "alternateName": "Aspose",
        "sameAs": [
            "https://facebook.com/aspose.pdf/",
            "https://twitter.com/asposepdf",
            "https://www.youtube.com/channel/UCmV9sEg_QWYPi6BJJs7ELOg/featured",
            "https://www.linkedin.com/company/aspose",
            "https://stackoverflow.com/questions/tagged/aspose",
            "https://aspose.quora.com/",
            "https://aspose.github.io/"
        ],
        "contactPoint": [
            {
                "@type": "ContactPoint",
                "telephone": "+1 903 306 1676",
                "contactType": "sales",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "sales",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "sales",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "url": "/net/import-export-json/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/import-export-json/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF puede realizar no solo tareas simples y fáciles, sino también afrontar objetivos más complejos. Consulte la siguiente sección para usuarios y desarrolladores avanzados."
}
</script>

## Importar y Exportar Datos de Formularios en JSON

Manipular campos de formularios dentro de documentos PDF puede ser crucial al manejar operaciones de entrada y salida de datos en varias aplicaciones. La biblioteca Aspose.PDF ofrece una funcionalidad robusta para exportar e importar campos de formularios en formato JSON. A continuación, exploramos varios fragmentos de código que demuestran cómo realizar estas tareas utilizando diferentes enfoques.

Desde la versión 24.7 es posible agregar Importar y Exportar Datos de Formularios en Formato JSON:

### Exportar campos de formulario hacia y desde el archivo JSON

Este enfoque exporta todos los campos de formulario de un documento PDF existente a un archivo JSON e importarlos en un nuevo documento PDF.

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExportAllFieldsToJson(string inputPdfPath, string outputJsonPath, string outputPdfPath)
{
    // Create ExportFieldsToJsonOptions with indentation
    var options = new Aspose.Pdf.ExportFieldsToJsonOptions { WriteIndented = true };

    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "TextField.pdf"))
    {
        // Export fields to JSON
        var exportResult = document.Form.ExportToJson(outputJsonPath, options);

        // Optionally, save the document with fields to a new PDF
        document.Save(dataDir + "TextBox_out.pdf");
    }
}
```

### Importar campos de formulario desde el archivo JSON e insertarlos en el documento PDF creado

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ImportFieldsFromJsonAndInsertToPdf(string inputPdfPath, string outputJsonPath, string outputPdfPath)
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();
	
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "TextField.pdf"))
    {
        // Create PDF document to import fields into
        var newDocument = new Aspose.Pdf.Document();

        // Add page
        var page = newDocument.Pages.Add();

        // Import fields from JSON
        var importResult = newDocument.Form.ImportFromJson(outputJsonPath);

        // Save PDF document
        newDocument.Save(dataDir + "TextBox_out.pdf");
    }
}
```

### Exportar campos de formulario hacia y desde el archivo JSON utilizando FileStream

Este fragmento exporta campos a un archivo JSON utilizando 'FileStream' para gestionar la entrada y salida del archivo.

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExportFieldsToJson(string inputPdfPath, string outputJsonPath, string outputPdfPath)
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();
	
    // Create ExportFieldsToJsonOptions with indentation
    var options = new Aspose.Pdf.ExportFieldsToJsonOptions { WriteIndented = true };

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "TextField.pdf"))
    {
        // Create a FileStream to write the JSON output
        using (var fileStream = File.Create(outputJsonPath))
        {
            // Export fields to JSON using the FileStream
            var exportResult = document.Form.ExportToJson(fileStream, options);
        }
    }
}
```

### Importar campos de formulario desde el archivo JSON utilizando FileStream e insertarlos en el documento PDF creado

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ImportFieldsFromJsonToCreatedPdt(string inputPdfPath, string outputJsonPath, string outputPdfPath)
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "TextField.pdf"))
    {
        // Create PDF document to import fields into
        var newDocument = new Aspose.Pdf.Document();

        // Add page
        var page = newDocument.Pages.Add();

        // Open the JSON file for reading
        using (var fileStream = File.OpenRead(outputJsonPath))
        {
            // Import fields from JSON using the FileStream
            var importResult = newDocument.Form.ImportFromJson(fileStream);
        }

        // Save PDF document
        newDocument.Save(dataDir + "TextBox_out.pdf");
    }
}
```

### Exportar campos de formulario en formato JSON utilizando MemoryStream

En algunos escenarios, puede que prefiera trabajar con datos en memoria en lugar de con archivos en disco. Este enfoque utiliza 'MemoryStream' para manejar los procesos de exportación e importación completamente en memoria.

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExportFieldsToJsonUsingMemoryStream(string inputPdfPath, string outputPdfPath)
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Create a MemoryStream to hold the JSON data
    using (var memoryStream = new MemoryStream())
    {
        // Open PDF document
        using (var document = new Aspose.Pdf.Document(dataDir + "TextField.pdf"))
        {
            // Export fields to JSON and write to the MemoryStream
            var exportResult = document.Form.ExportToJson(memoryStream);
        }

        // Save the MemoryStream content to a file
        File.WriteAllBytes(outputPdfPath, memoryStream.ToArray());
    }
}
```

### Importar campos de formulario en formato JSON utilizando MemoryStream

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ImportFieldsFromJsonUsingMemoryStream(string inputPdfPath, string outputPdfPath)
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "TextField.pdf"))
    {
        // Create PDF document to import fields into
        var newDocument = new Aspose.Pdf.Document();

        // Add page
        var page = newDocument.Pages.Add();

        // Create a MemoryStream to hold the JSON data
        using (var memoryStream = new MemoryStream())
        {
            // Export fields from the original document to the MemoryStream
            document.Form.ExportToJson(memoryStream);

            // Reset the MemoryStream position to the beginning
            memoryStream.Position = 0;

            // Import fields from the MemoryStream into the new document
            var importResult = newDocument.Form.ImportFromJson(memoryStream);
        }

        // Save PDF document
        newDocument.Save(dataDir + "TextBox_out.pdf");
    }
}
```

### Exportar el campo específico hacia y desde el archivo JSON

A veces, puede que necesite exportar o importar solo un campo específico en lugar de todos los campos en el documento.

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExportFieldToJson(string inputPdfPath, string outputJsonPath, string outputPdfPath)
{
    // Create ExportFieldsToJsonOptions with indentation
    var options = new Aspose.Pdf.ExportFieldsToJsonOptions { WriteIndented = true };

    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "TextField.pdf"))
    {
        // Get the specific field (WidgetAnnotation) from the form
        if (document.Form[1] is Aspose.Pdf.Annotations.WidgetAnnotation field)
        {
            // Export the field to JSON
            var exportResult = field.ExportToJson(outputJsonPath, options);
        }
    }
}
```

### Importar el campo específico hacia y desde el archivo JSON

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ImportFieldFromJson(string inputPdfPath, string outputJsonPath, string outputPdfPath)
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "TextField.pdf"))
    {
        // Create PDF document to import fields into
        var newDocument = new Aspose.Pdf.Document();

        // Add page
        var page = newDocument.Pages.Add();

        // Import fields from JSON
        var importResult = newDocument.Form.ImportFromJson(outputJsonPath);

        // Save PDF document
        newDocument.Save(dataDir + "TextBox_out.pdf");
    }
}
```

### Exportar el campo específico hacia y desde el archivo JSON utilizando FileStream

Este ejemplo es similar al anterior, pero utiliza 'FileStream' para manejar las operaciones de exportación e importación para un campo específico.

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExportFieldToJson(string inputPdfPath, string outputJsonPath, string outputPdfPath)
{
    // Create ExportFieldsToJsonOptions with indentation
    var options = new Aspose.Pdf.ExportFieldsToJsonOptions { WriteIndented = true };
	
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();	

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "TextField.pdf"))
    {
        // Get the specific field (WidgetAnnotation) from the form
        if (document.Form[1] is Aspose.Pdf.Annotations.WidgetAnnotation field)
        {
            // Create a FileStream to write the JSON output
            using (var fileStream = File.Create(outputJsonPath))
            {
                // Export the field to JSON using the FileStream
                var exportResult = field.ExportToJson(fileStream, options);
            }
        }
    }
}
```

### Importar el campo específico hacia y desde el archivo JSON utilizando FileStream

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ImportFieldFromJson(string inputPdfPath, string outputJsonPath, string outputPdfPath)
{
    // Create PDF document to import fields into
    using (var newDocument = new Aspose.Pdf.Document())
    {
        // Add page
        var page = newDocument.Pages.Add();

        // Open the JSON file for reading
        using (var fileStream = File.OpenRead(outputJsonPath))
        {
            // Import fields from JSON using the FileStream
            var importResult = newDocument.Form.ImportFromJson(fileStream);
        }

        // Save PDF document
        newDocument.Save(dataDir + "TextBox_out.pdf");
    }
}
```

### Exportar el campo específico en formato JSON utilizando MemoryStream

Este fragmento de código demuestra cómo exportar un campo de formulario específico de un documento PDF en formato JSON utilizando un 'MemoryStream' y luego importarlo en un nuevo documento PDF.

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExportFieldToJsonUsingMemoryStream(string inputPdfPath, string outputPdfPath)
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Create a MemoryStream to hold the JSON data
    using (var memoryStream = new MemoryStream())
    {
        // Open PDF document
        using (var document = new Aspose.Pdf.Document(dataDir + "TextField.pdf"))
        {
            // Get the specific field (WidgetAnnotation) from the form
            if (document.Form[1] is Aspose.Pdf.Annotations.WidgetAnnotation field)
            {
                // Export the field to JSON and write to the MemoryStream
                var exportResult = field.ExportToJson(memoryStream);
            }
        }

        // Optionally, you can save the MemoryStream content to a file
        File.WriteAllBytes(outputPdfPath, memoryStream.ToArray());
    }
}
```

### Importar el campo específico en formato JSON utilizando MemoryStream

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ImportFieldFromJsonUsingMemoryStream(string inputPdfPath, string outputPdfPath)
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "TextField.pdf"))
    {
        // Create PDF document to import fields into
        var newDocument = new Aspose.Pdf.Document();

        // Add page
        var page = newDocument.Pages.Add();

        // Create a MemoryStream to hold the JSON data
        using (var memoryStream = new MemoryStream())
        {
            // Export fields from the original document to the MemoryStream
            document.Form.ExportToJson(memoryStream);

            // Reset the MemoryStream position to the beginning
            memoryStream.Position = 0;

            // Import fields from the MemoryStream into the new document
            var importResult = newDocument.Form.ImportFromJson(memoryStream);
        }

        // Save PDF document
        newDocument.Save(dataDir + "TextBox_out.pdf");
    }
}
```

### Exportar valor del campo específico hacia el archivo JSON utilizando FileStream

Este fragmento de código muestra cómo exportar el valor de un campo de formulario específico de un documento PDF a un archivo JSON utilizando FileStream.

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExportFieldValueToJson(string inputPdfPath, string outputJsonPath, string outputPdfPath)
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();
	
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "TextField.pdf"))
    {
        // Get the specific field from the form
        if (document.Form.Fields[1] is Aspose.Pdf.Forms.Field field)
        {
            // Create a FileStream to write the JSON output
            using (var fileStream = File.Create(outputJsonPath))
            {
                // Export the field value to JSON using the FileStream
                field.ExportValueToJson(fileStream);
            }
        }
    }
}
```

### Importar valor al campo específico desde el archivo JSON utilizando FileStream

Este fragmento de código demuestra cómo importar un valor desde un archivo JSON a un campo de formulario específico en un documento PDF utilizando FileStream.

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ImportFieldValueFromJson(string inputPdfPath, string outputJsonPath, string outputPdfPath)
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "TextField.pdf"))
    {
        // Get the specific field from the form
        if (document.Form.Fields[1] is Aspose.Pdf.Forms.Field field)
        {
            // Open the JSON file for reading
            using (var fileStream = File.OpenRead(outputJsonPath))
            {
                // Import the field value from JSON using the FileStream
                field.ImportValueFromJson(fileStream);
            }
        }

        // Save PDF document
        document.Save(dataDir + "TextBox_out.pdf");
    }
}
```

### Importar valor de otro campo al campo específico desde el archivo JSON utilizando FileStream

Este fragmento de código demuestra cómo importar un valor de otro campo al campo específico desde el archivo JSON utilizando FileStream y Aspose.PDF.

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ImportFieldValueFromJson(string inputPdfPath, string outputJsonPath, string outputPdfPath, string fullNameOfOtherFieldInJson)
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "TextField.pdf"))
    {
        // Get the specific field from the form
        if (document.Form.Fields[1] is Aspose.Pdf.Forms.Field field)
        {
            // Open the JSON file for reading
            using (var fileStream = File.OpenRead(outputJsonPath))
            {
                // Import the field value from JSON using the FileStream and the full name of the other field in JSON
                field.ImportValueFromJson(fileStream, fullNameOfOtherFieldInJson);
            }
        }

        // Save PDF document
        document.Save(dataDir + "TextBox_out.pdf");
    }
}
```

## Manejo de Errores

Este ejemplo demuestra cómo exportar campos de formulario de un PDF a un archivo JSON utilizando Aspose.PDF, incluyendo el manejo de diferentes estados para cada campo durante el proceso de exportación.

Desglosemos este ejemplo de Aspose.PDF paso a paso:

1. Cargando el Documento. Cargamos un documento PDF llamado "Sample.pdf" desde un directorio especificado.
2. Estableciendo Opciones de Exportación. Aquí, creamos una instancia de ExportFieldsToJsonOptions con dos configuraciones:
    * `ExportPasswordValue`: Esto incluye campos de contraseña en la exportación.
    * `WriteIndented`: Esto formatea la salida JSON para que esté indentada y sea legible.
3. Exportar campos de formulario a JSON. Exportamos los campos de formulario del archivo PDF a un archivo JSON llamado "export.json" utilizando los parámetros especificados.
4. Procesando Resultados de Exportación:
    Este bucle itera a través de los resultados de exportación e imprime el estado de cada campo:

    * Éxito: Indica que el campo fue exportado con éxito.
    * Advertencia: Imprime cualquier mensaje de advertencia relacionado con el campo.
    * Error: Imprime cualquier mensaje de error relacionado con el campo.

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExportFieldsToJsonWithOptions()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(Path.Combine(dataDir, "Forms", "Sample.pdf")))
    {
        // Create ExportFieldsToJsonOptions with specific settings
        var options = new Aspose.Pdf.ExportFieldsToJsonOptions
        {
            ExportPasswordValue = true,
            WriteIndented = true,
        };

        var exportResults = document.Form.ExportToJson(File.OpenWrite("export.json"), options);

        foreach (var result in exportResults)
        {
            Console.Write($"{result.FieldFullName} ");
            switch (result.FieldSerializationStatus)
            {
                case Aspose.Pdf.FieldSerializationStatus.Success:
                    Console.WriteLine("Success");
                    break;
                case Aspose.Pdf.FieldSerializationStatus.Warning:
                    foreach (var messages in result.WarningMessages)
                    {
                        Console.WriteLine(messages);
                    }
                    break;
                case Aspose.Pdf.FieldSerializationStatus.Error:
                    foreach (var messages in result.ErrorMessages)
                    {
                        Console.WriteLine(messages);
                    }
                    break;
            }
        }
    }
}
```