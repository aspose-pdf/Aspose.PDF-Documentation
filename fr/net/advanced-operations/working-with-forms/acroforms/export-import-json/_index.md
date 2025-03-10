---
title: Importer et Exporter des Données en JSON
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 80
url: /fr/net/import-export-json/
description: Cette section explique comment importer et exporter des données en JSON
lastmod: "2024-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Import and Export Data in JSON",
    "alternativeHeadline": "Enhance PDF Form Management with JSON Import/Export",
    "abstract": "La nouvelle fonctionnalité permet l'importation et l'exportation sans faille des données de formulaire PDF au format JSON, offrant un moyen simple de manipuler les champs de formulaire à travers les documents. Les utilisateurs peuvent utiliser diverses méthodes, y compris FileStream et MemoryStream, pour gérer les données efficacement, garantissant flexibilité qu'ils travaillent avec des documents complets ou des champs spécifiques. Cette fonctionnalité améliore les flux de travail de traitement des données, rendant la gestion des formulaires PDF plus simple et plus efficace.",
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
    "description": "Aspose.PDF peut effectuer non seulement des tâches simples et faciles mais aussi faire face à des objectifs plus complexes. Consultez la section suivante pour les utilisateurs avancés et les développeurs."
}
</script>

## Importer et Exporter des Données des Formulaires en JSON

Manipuler les champs de formulaire dans les documents PDF peut être crucial lors de la gestion des opérations d'entrée et de sortie de données dans diverses applications. La bibliothèque Aspose.PDF offre une fonctionnalité robuste pour exporter et importer des champs de formulaire au format JSON. Ci-dessous, nous explorons plusieurs extraits de code démontrant comment effectuer ces tâches en utilisant différentes approches.

Depuis la version 24.7, il est possible d'ajouter l'importation et l'exportation de données des formulaires au format JSON :

### Exporter les champs de formulaire vers et depuis le fichier JSON

Cette approche exporte tous les champs de formulaire d'un document PDF existant vers un fichier JSON et les importe dans un nouveau document PDF.

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

### Importer les champs de formulaire depuis le fichier JSON et les insérer dans le document PDF créé

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

### Exporter les champs de formulaire vers et depuis le fichier JSON en utilisant FileStream

Cet extrait exporte les champs vers un fichier JSON en utilisant 'FileStream' pour gérer l'entrée et la sortie de fichiers.

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

### Importer les champs de formulaire depuis le fichier JSON en utilisant FileStream et les insérer dans le document PDF créé

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

### Exporter les champs de formulaire au format JSON en utilisant MemoryStream

Dans certains scénarios, vous pourriez préférer travailler avec des données en mémoire plutôt qu'avec des fichiers sur disque. Cette approche utilise 'MemoryStream' pour gérer les processus d'exportation et d'importation entièrement en mémoire.

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

### Importer les champs de formulaire au format JSON en utilisant MemoryStream

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

### Exporter le champ spécifié vers et depuis le fichier JSON

Parfois, vous pouvez avoir besoin d'exporter ou d'importer uniquement un champ spécifique plutôt que tous les champs du document.

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

### Importer le champ spécifié vers et depuis le fichier JSON

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

### Exporter le champ spécifié vers et depuis le fichier JSON en utilisant FileStream

Cet exemple est similaire à celui ci-dessus mais utilise 'FileStream' pour gérer les opérations d'exportation et d'importation pour un champ spécifique.

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

### Importer le champ spécifié vers et depuis le fichier JSON en utilisant FileStream

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

### Exporter le champ spécifié au format JSON en utilisant MemoryStream

Cet extrait de code démontre comment exporter un champ de formulaire spécifique d'un document PDF au format JSON en utilisant un 'MemoryStream' puis l'importer dans un nouveau document PDF.

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

### Importer le champ spécifié au format JSON en utilisant MemoryStream

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

### Exporter la valeur du champ spécifié vers le fichier JSON en utilisant FileStream

Cet extrait de code montre comment exporter la valeur d'un champ de formulaire spécifique d'un document PDF vers un fichier JSON en utilisant FileStream.

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

### Importer la valeur vers le champ spécifié depuis le fichier JSON en utilisant FileStream

Cet extrait de code démontre comment importer une valeur depuis un fichier JSON dans un champ de formulaire spécifique d'un document PDF en utilisant FileStream.

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

### Importer la valeur d'un autre champ vers le champ spécifié depuis le fichier JSON en utilisant FileStream

Cet extrait de code démontre comment importer la valeur d'un autre champ vers le champ spécifié depuis le fichier JSON en utilisant FileStream et Aspose.PDF.

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

## Gestion des erreurs

Cet exemple démontre comment exporter des champs de formulaire d'un PDF vers un fichier JSON en utilisant Aspose.PDF, y compris la gestion des différents statuts pour chaque champ pendant le processus d'exportation.

Décomposons cet exemple Aspose.PDF étape par étape :

1. Chargement du Document. Nous chargeons un document PDF nommé "Sample.pdf" depuis un répertoire spécifié.
1. Définition des Options d'Exportation. Ici, nous créons une instance de ExportFieldsToJsonOptions avec deux paramètres :
    * `ExportPasswordValue` : Cela inclut les champs de mot de passe dans l'exportation.
    * `WriteIndented` : Cela formate la sortie JSON pour être indentée pour la lisibilité.
1. Exporter les champs de formulaire vers JSON. Nous exportons les champs de formulaire du fichier PDF vers un fichier JSON appelé "export.json" en utilisant les paramètres spécifiés.
1. Traitement des Résultats d'Exportation :
    Cette boucle itère à travers les résultats d'exportation et imprime le statut de chaque champ :

    * Succès : Indique que le champ a été exporté avec succès.
    * Avertissement : Imprime tout message d'avertissement lié au champ.
    * Erreur : Imprime tout message d'erreur lié au champ.

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