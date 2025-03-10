---
title: JSONでのデータのインポートとエクスポート
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 80
url: /ja/net/import-export-json/
description: このセクションでは、JSONでのデータのインポートとエクスポートの方法を説明します
lastmod: "2024-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Import and Export Data in JSON",
    "alternativeHeadline": "Enhance PDF Form Management with JSON Import/Export",
    "abstract": "この新機能により、JSON形式を使用してPDFフォームデータのシームレスなインポートとエクスポートが可能になり、ドキュメント間でフォームフィールドを操作する簡単な方法を提供します。ユーザーは、FileStreamやMemoryStreamなどのさまざまな方法を利用してデータを効率的に管理でき、完全なドキュメントや特定のフィールドで作業する際の柔軟性を確保します。この機能はデータ処理ワークフローを強化し、PDFフォーム管理をより簡単かつ効果的にします。",
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
    "description": "Aspose.PDFは、単純で簡単なタスクだけでなく、より複雑な目標にも対応できます。次のセクションでは、上級ユーザーと開発者向けの情報を確認してください。"
}
</script>

## JSON形式でのフォームからのデータのインポートとエクスポート

PDFドキュメント内のフォームフィールドを操作することは、さまざまなアプリケーションでのデータ入力および出力操作を扱う際に重要です。Aspose.PDFライブラリは、JSON形式でフォームフィールドをエクスポートおよびインポートするための強力な機能を提供します。以下では、さまざまなアプローチを使用してこれらのタスクを実行する方法を示すいくつかのコードスニペットを探ります。

24.7以降、JSON形式でフォームからのデータのインポートとエクスポートが可能になりました：

### JSONファイルへのフォームフィールドのエクスポートとインポート

このアプローチでは、既存のPDFドキュメントからすべてのフォームフィールドをJSONファイルにエクスポートし、それを新しいPDFドキュメントにインポートします。

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

### JSONファイルからフォームフィールドをインポートし、作成したPDFドキュメントに挿入する

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

### FileStreamを使用してJSONファイルへのフォームフィールドのエクスポートとインポート

このスニペットは、ファイルの入出力を管理するために'FileStream'を利用してJSONファイルにフィールドをエクスポートします。

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

### FileStreamを使用してJSONファイルからフォームフィールドをインポートし、作成したPDFドキュメントに挿入する

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

### MemoryStreamを使用してJSON形式でフォームフィールドをエクスポート

いくつかのシナリオでは、ディスク上のファイルではなく、メモリ内のデータで作業することを好む場合があります。このアプローチでは、'MemoryStream'を使用してエクスポートおよびインポートプロセスを完全にメモリ内で処理します。

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

### MemoryStreamを使用してJSON形式でフォームフィールドをインポート

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

### 特定のフィールドをJSONファイルにエクスポートおよびインポート

場合によっては、ドキュメント内のすべてのフィールドではなく、特定のフィールドのみをエクスポートまたはインポートする必要があります。

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

### JSONファイルから特定のフィールドをインポート

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

### FileStreamを使用して特定のフィールドをJSONファイルにエクスポートおよびインポート

この例は上記のものと似ていますが、特定のフィールドのエクスポートおよびインポート操作を処理するために'FileStream'を使用します。

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

### FileStreamを使用して特定のフィールドをJSONファイルからインポート

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

### MemoryStreamを使用してJSON形式で特定のフィールドをエクスポート

このコードスニペットは、PDFドキュメントから特定のフォームフィールドをJSON形式にエクスポートし、それを新しいPDFドキュメントにインポートする方法を示しています。

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

### MemoryStreamを使用してJSON形式で特定のフィールドをインポート

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

### FileStreamを使用して特定のフィールドの値をJSONファイルにエクスポート

このコードスニペットは、PDFドキュメントから特定のフォームフィールドの値をJSONファイルにエクスポートする方法を示しています。

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

### FileStreamを使用してJSONファイルから特定のフィールドに値をインポート

このコードスニペットは、JSONファイルからPDFドキュメント内の特定のフォームフィールドに値をインポートする方法を示しています。

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

### FileStreamを使用してJSONファイルから特定のフィールドに別のフィールドの値をインポート

このコードスニペットは、JSONファイルから特定のフィールドに別のフィールドの値をインポートする方法を示しています。

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

## エラーハンドリング

この例では、Aspose.PDFを使用してPDFからJSONファイルにフォームフィールドをエクスポートする方法を示し、エクスポートプロセス中の各フィールドの異なるステータスを処理します。

このAspose.PDFの例をステップバイステップで分解してみましょう：

1. ドキュメントの読み込み。指定されたディレクトリから「Sample.pdf」というPDFドキュメントを読み込みます。
1. エクスポートオプションの設定。ここでは、2つの設定を持つExportFieldsToJsonOptionsのインスタンスを作成します：
    * `ExportPasswordValue` : エクスポートにパスワードフィールドを含めます。
    * `WriteIndented` : 読みやすさのためにJSON出力をインデント形式にします。
1. JSONへのフォームフィールドのエクスポート。指定されたパラメータを使用して、PDFファイルから「export.json」というJSONファイルにフォームフィールドをエクスポートします。
1. エクスポート結果の処理：
    このループはエクスポート結果を反復処理し、各フィールドのステータスを印刷します：

    * 成功：フィールドが正常にエクスポートされたことを示します。
    * 警告：フィールドに関連する警告メッセージを印刷します。
    * エラー：フィールドに関連するエラーメッセージを印刷します。

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