---
title: Импорт и экспорт данных в JSON
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 80
url: /ru/net/import-export-json/
description: Этот раздел объясняет, как импортировать и экспортировать данные в JSON
lastmod: "2024-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Import and Export Data in JSON",
    "alternativeHeadline": "Enhance PDF Form Management with JSON Import/Export",
    "abstract": "Новая функция позволяет бесшовно импортировать и экспортировать данные форм PDF, используя формат JSON, предоставляя простой способ манипулировать полями форм в различных документах. Пользователи могут использовать различные методы, включая FileStream и MemoryStream, для эффективного управления данными, обеспечивая гибкость как при работе с полными документами, так и с конкретными полями. Эта функциональность улучшает рабочие процессы обработки данных, делая управление PDF-формами проще и эффективнее.",
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
    "description": "Aspose.PDF может выполнять не только простые и легкие задачи, но и справляться с более сложными целями. Проверьте следующий раздел для продвинутых пользователей и разработчиков."
}
</script>

## Импорт и экспорт данных из форм в JSON

Манипулирование полями форм в PDF-документах может быть критически важным при обработке операций ввода и вывода данных в различных приложениях. Библиотека Aspose.PDF предлагает надежную функциональность для экспорта и импорта полей форм в формате JSON. Ниже мы рассмотрим несколько фрагментов кода, демонстрирующих, как выполнять эти задачи с использованием различных подходов.

С версии 24.7 стало возможным добавлять импорт и экспорт данных из форм в формате JSON:

### Экспорт полей форм в файл JSON и из него

Этот подход экспортирует все поля форм из существующего PDF-документа в файл JSON и импортирует их в новый PDF-документ.

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

### Импорт полей форм из файла JSON и вставка их в созданный PDF-документ

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

### Экспорт полей форм в файл JSON и из него с использованием FileStream

Этот фрагмент экспортирует поля в файл JSON, используя 'FileStream' для управления вводом и выводом файла.

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

### Импорт полей форм из файла JSON с использованием FileStream и вставка их в созданный PDF-документ

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

### Экспорт полей форм в формате JSON с использованием MemoryStream

В некоторых сценариях вы можете предпочесть работать с данными в памяти, а не с файлами на диске. Этот подход использует 'MemoryStream' для обработки процессов экспорта и импорта полностью в памяти.

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

### Импорт полей форм в формате JSON с использованием MemoryStream

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

### Экспорт указанного поля в файл JSON и из него

Иногда вам может понадобиться экспортировать или импортировать только конкретное поле, а не все поля в документе.

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

### Импорт указанного поля в файл JSON и из него

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

### Экспорт указанного поля в файл JSON и из него с использованием FileStream

Этот пример аналогичен предыдущему, но использует 'FileStream' для обработки операций экспорта и импорта для конкретного поля.

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

### Импорт указанного поля в файл JSON и из него с использованием FileStream

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

### Экспорт указанного поля в формате JSON с использованием MemoryStream

Этот фрагмент кода демонстрирует, как экспортировать конкретное поле формы из PDF-документа в формат JSON с использованием 'MemoryStream', а затем импортировать его в новый PDF-документ.

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

### Импорт указанного поля в формате JSON с использованием MemoryStream

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

### Экспорт значения из указанного поля в файл JSON с использованием FileStream

Этот фрагмент кода показывает, как экспортировать значение конкретного поля формы из PDF-документа в файл JSON с использованием FileStream.

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

### Импорт значения в указанное поле из файла JSON с использованием FileStream

Этот фрагмент кода демонстрирует, как импортировать значение из файла JSON в конкретное поле формы в PDF-документе с использованием FileStream.

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

### Импорт значения другого поля в указанное поле из файла JSON с использованием FileStream

Этот фрагмент кода демонстрирует, как импортировать значение другого поля в указанное поле из файла JSON с использованием FileStream и Aspose.PDF.

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

## Обработка ошибок

Этот пример демонстрирует, как экспортировать поля форм из PDF в файл JSON с использованием Aspose.PDF, включая обработку различных статусов для каждого поля в процессе экспорта.

Давайте разберем этот пример Aspose.PDF шаг за шагом:

1. Загрузка документа. Мы загружаем PDF-документ с именем "Sample.pdf" из указанного каталога.
1. Установка параметров экспорта. Здесь мы создаем экземпляр ExportFieldsToJsonOptions с двумя настройками:
    * `ExportPasswordValue` : Это включает поля паролей в экспорт.
    * `WriteIndented` : Это форматирует вывод JSON с отступами для удобочитаемости.
1. Экспорт полей форм в JSON. Мы экспортируем поля форм из PDF-файла в файл JSON с именем "export.json" с использованием указанных параметров.
1. Обработка результатов экспорта:
    Этот цикл проходит по результатам экспорта и выводит статус каждого поля:

    * Успех: Указывает, что поле было успешно экспортировано.
    * Предупреждение: Выводит любые предупреждающие сообщения, связанные с полем.
    * Ошибка: Выводит любые сообщения об ошибках, связанные с полем.

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