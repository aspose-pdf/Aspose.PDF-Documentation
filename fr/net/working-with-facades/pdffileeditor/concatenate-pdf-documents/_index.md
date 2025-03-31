---
title: Concaténer des documents PDF en C#
linktitle: Concaténer des documents PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /fr/net/concatenate-pdf-documents/
description: Cette section explique comment concaténer des documents PDF avec Aspose.PDF Facades en utilisant la classe PdfFileEditor.
lastmod: "2021-06-05"
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Concatenate PDF documents in C#",
    "alternativeHeadline": "Effortlessly Merge PDF Files in C#",
    "abstract": "La fonctionnalité dans Aspose.PDF for .NET permet aux développeurs de concaténer efficacement plusieurs documents PDF en utilisant la classe PdfFileEditor en C#. Cette fonctionnalité prend en charge la fusion de fichiers via des chemins de fichiers et des MemoryStreams, la création de noms de champs uniques dans les formulaires PDF, et même la génération d'une table des matières dans le document final, offrant une solution rationalisée pour la gestion et l'intégration des documents.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "1615",
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
    "url": "/net/concatenate-pdf-documents/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/concatenate-pdf-documents/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF peut effectuer non seulement des tâches simples et faciles mais aussi faire face à des objectifs plus complexes. Consultez la section suivante pour les utilisateurs avancés et les développeurs."
}
</script>

## **Aperçu**

Cet article explique comment fusionner, combiner ou concaténer différents fichiers PDF en un seul PDF en utilisant C#. Il couvre des sujets tels que :

- [C# Fusionner des fichiers PDF](#concatenate-pdf-files-using-file-paths)
- [C# Combiner des fichiers PDF](#concatenate-pdf-files-using-file-paths)
- [C# Fusionner plusieurs fichiers PDF en un PDF](#concatenate-array-of-pdf-files-using-file-paths)
- [C# Combiner plusieurs fichiers PDF en un PDF](#concatenate-array-of-pdf-files-using-file-paths)
- [C# Fusionner tous les fichiers PDF dans un dossier](#concatenating-all-pdf-files-in-particular-folder)
- [C# Combiner tous les fichiers PDF dans un dossier](#concatenating-all-pdf-files-in-particular-folder)
- [C# Fusionner des fichiers PDF en utilisant des chemins de fichiers](#concatenate-pdf-files-using-file-paths)
- [C# Combiner des fichiers PDF en utilisant des flux](#concatenate-array-of-pdf-files-using-streams)
- [C# Concaténer tous les fichiers PDF dans un dossier](#concatenate-pdf-files-in-folder)

## Concaténer des fichiers PDF en utilisant des chemins de fichiers

[PdfFileEditor](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades/pdffileeditor) est la classe dans le [namespace Aspose.Pdf.Facades](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades) qui vous permet de concaténer plusieurs fichiers PDF. Vous pouvez non seulement concaténer des fichiers en utilisant des FileStreams mais aussi en utilisant des MemoryStreams. Dans cet article, le processus de concaténation des fichiers en utilisant des MemoryStreams sera expliqué et ensuite montré à l'aide d'un extrait de code.

La méthode [Concaténer](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades/pdffileeditor/methods/concatenate/index) de la classe [PdfFileEditor](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades/pdffileeditor) peut être utilisée pour concaténer deux fichiers PDF. La méthode [Concaténer](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades/pdffileeditor/methods/concatenate/index) vous permet de passer trois paramètres : le premier PDF d'entrée, le deuxième PDF d'entrée et le PDF de sortie. Le PDF de sortie final contient les deux fichiers PDF d'entrée.

L'extrait de code C# suivant vous montre comment concaténer des fichiers PDF en utilisant des chemins de fichiers.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConcatenatePdfFilesUsingFilePaths()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Concatenate();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Concatenate files
    pdfEditor.Concatenate(dataDir + "ConcatenatePdfFilesUsingFilePaths1.pdf", dataDir + "ConcatenatePdfFilesUsingFilePaths2.pdf", dataDir + "ConcatenateUsingPath_out.pdf");
}
```

Dans certains cas, lorsqu'il y a beaucoup de contours, les utilisateurs peuvent les désactiver en définissant CopyOutlines sur false et améliorer les performances de concaténation.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConcatenatePdfFilesUsingFilePaths_CopyOutlinesDisabled()
{ 
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Concatenate();
    // Create PdfFileEditor object
    var pfe = new Aspose.Pdf.Facades.PdfFileEditor();
    // Setting CopyOutlines to false
    pfe.CopyOutlines = false;
    // Concatenate files
    pfe.Concatenate(dataDir + "ConcatenatePdfFilesUsingFilePaths_CopyOutlinesDisabled1.pdf", dataDir + "ConcatenatePdfFilesUsingFilePaths_CopyOutlinesDisabled2.pdf", dataDir + "ConcatenateUsingPath_CopyOutlinesDisabled_out.pdf");
}
```

## Concaténer plusieurs fichiers PDF en utilisant des MemoryStreams

La méthode [Concaténer](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades/pdffileeditor/methods/concatenate/index) de la classe [PdfFileEditor](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades/pdffileeditor) prend les fichiers PDF source et le fichier PDF de destination comme paramètres. Ces paramètres peuvent être soit des chemins vers les fichiers PDF sur le disque, soit des MemoryStreams. Maintenant, pour cet exemple, nous allons d'abord créer deux flux de fichiers pour lire les fichiers PDF depuis le disque. Ensuite, nous allons convertir ces fichiers en tableaux d'octets. Ces tableaux d'octets des fichiers PDF seront convertis en MemoryStreams. Une fois que nous avons les MemoryStreams des fichiers PDF, nous pourrons les passer à la méthode de concaténation et les fusionner en un seul fichier de sortie.

L'extrait de code C# suivant vous montre comment concaténer plusieurs fichiers PDF en utilisant des MemoryStreams :

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConcatenateMultiplePdfFilesUsingMemoryStreams()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Concatenate();

    string document1Path = dataDir + "ConcatenateMultiplePdfFilesUsingMemoryStreams1.pdf";
    string document2Path = dataDir + "ConcatenateMultiplePdfFilesUsingMemoryStreams2.pdf";
    string resultPdfPath = dataDir + "concatenated_out.pdf";
    
    // Create two file streams to read PDF files
    using (var fs1 = new FileStream(document1Path, FileMode.Open, FileAccess.Read))
    {
        using (var fs2 = new FileStream(document2Path, FileMode.Open, FileAccess.Read))
        {
            // Create byte arrays to keep the contents of PDF files
            var buffer1 = new byte[Convert.ToInt32(fs1.Length)];
            var buffer2 = new byte[Convert.ToInt32(fs2.Length)];

            var i = 0;
            // Read PDF file contents into byte arrays
            i = fs1.Read(buffer1, 0, Convert.ToInt32(fs1.Length));
            i = fs2.Read(buffer2, 0, Convert.ToInt32(fs2.Length));

            // Now, first convert byte arrays into MemoryStreams and then concatenate those streams
            using (var pdfStream = new MemoryStream())
            {
                using (var fileStream1 = new MemoryStream(buffer1))
                {
                    using (var fileStream2 = new MemoryStream(buffer2))
                    {
                        // Create instance of PdfFileEditor class to concatenate streams
                        var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
                        // Concatenate both input MemoryStreams and save to output MemoryStream
                        pdfEditor.Concatenate(fileStream1, fileStream2, pdfStream);
                        // Convert MemoryStream back to byte array
                        var data = pdfStream.ToArray();
                        // Create a FileStream to save the output PDF file
                        using (var output = new FileStream(resultPdfPath, FileMode.Create, FileAccess.Write))
                        {
                            // Write byte array contents in the output file stream
                            output.Write(data, 0, data.Length);
                        }
                    }
                }
            }
        }
    }
}
```

## Concaténer un tableau de fichiers PDF en utilisant des chemins de fichiers

Si vous souhaitez concaténer plusieurs fichiers PDF, vous pouvez utiliser la surcharge de la méthode [Concaténer](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades/pdffileeditor/methods/concatenate/index), qui vous permet de passer un tableau de fichiers PDF. Le fichier de sortie final est enregistré en tant que fichier fusionné créé à partir de tous les fichiers du tableau. L'extrait de code C# suivant vous montre comment concaténer un tableau de fichiers PDF en utilisant des chemins de fichiers.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConcatenateArrayOfPdfFilesUsingFilePaths()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Concatenate();
    // Create PdfFileEditor
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Array of files
    var filesArray = new string[2];
    filesArray[0] = dataDir + "Concatenate1.pdf";
    filesArray[1] = dataDir + "Concatenate2.pdf";
    // Concatenate files
    pdfEditor.Concatenate(filesArray, dataDir + "ConcatenateArrayOfPdfFilesUsingFilePaths_out.pdf");
}
```

## Concaténer un tableau de fichiers PDF en utilisant des flux

La concaténation d'un tableau de fichiers PDF n'est pas limitée uniquement aux fichiers résidant sur le disque. Vous pouvez également concaténer un tableau de fichiers PDF à partir de flux. Si vous souhaitez concaténer plusieurs fichiers PDF, vous pouvez utiliser la surcharge appropriée de la méthode [Concaténer](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades/pdffileeditor/methods/concatenate/index). Tout d'abord, vous devez créer un tableau de flux d'entrée et un flux pour le PDF de sortie, puis appeler la méthode [Concaténer](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades/pdffileeditor/methods/concatenate/index). La sortie sera enregistrée dans le flux de sortie. L'extrait de code C# suivant vous montre comment concaténer un tableau de fichiers PDF en utilisant des flux.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConcatenateArrayOfPdfFilesUsingStreams()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Concatenate();

    var document1Path = dataDir + "Concatenate1.pdf";
    var document2Path = dataDir + "Concatenate2.pdf";
    var resultPdfPath = dataDir + "ConcatenateArrayOfPdfUsingStreams_out.pdf";

    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Output stream
    using (var outputStream = new FileStream(resultPdfPath, FileMode.Create))
    {
        using (var stream1 = new FileStream(document1Path, FileMode.Open))
        {
            using (var stream2 = new FileStream(document2Path, FileMode.Open))
            {
                // Array of streams
                var inputStreams = new Stream[2];
                inputStreams[0] = stream1;
                inputStreams[1] = stream2;
                // Concatenate file
                pdfEditor.Concatenate(inputStreams, outputStream);
            }   
        }
    }
}
```

## Concaténer tous les fichiers PDF dans un dossier particulier

Vous pouvez même lire tous les fichiers PDF dans un dossier particulier à l'exécution et les concaténer, sans même connaître les noms de fichiers. Il suffit de fournir le chemin du répertoire qui contient les documents PDF que vous souhaitez concaténer.

Veuillez essayer d'utiliser l'extrait de code C# suivant pour réaliser cette fonctionnalité.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConcatenatingAllPdfFilesInParticularFolder()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Concatenate();
    // Retrieve names of all the Pdf files in a particular Directory
    var fileEntries = Directory.GetFiles(dataDir, "*.pdf");
    var resultPdfPath = dataDir + "ConcatenatingAllPdfFilesInParticularFolder_out.pdf";
    // Instantiate PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Call Concatenate method of PdfFileEditor object to concatenate all input files
    // Into a single output file
    pdfEditor.Concatenate(fileEntries, resultPdfPath);
}
```

## Concaténer des formulaires PDF et garder les noms de champs uniques

La classe [PdfFileEditor](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades/pdffileeditor) dans le [namespace Aspose.Pdf.Facades](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades) offre la capacité de concaténer les fichiers PDF. Maintenant, si les fichiers PDF qui doivent être concaténés ont des champs de formulaire avec des noms de champs similaires, Aspose.PDF fournit la fonctionnalité de garder les champs dans le fichier PDF résultant uniques et vous pouvez également spécifier le suffixe pour rendre les noms de champs uniques. La propriété [KeepFieldsUnique](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades/pdffileeditor/properties/keepfieldsunique) de [PdfFileEditor](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades/pdffileeditor) définie sur true rendra les noms de champs uniques lorsque les formulaires PDF sont concaténés. De plus, la propriété [UniqueSuffix](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades/pdffileeditor/properties/uniquesuffix) de PdfFileEditor peut être utilisée pour spécifier le format défini par l'utilisateur du suffixe qui est ajouté au nom de champ pour le rendre unique lorsque les formulaires sont concaténés. Cette chaîne doit contenir la sous-chaîne `%NUM%` qui sera remplacée par des chiffres dans le fichier résultant.

Veuillez consulter l'extrait de code simple suivant pour réaliser cette fonctionnalité.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConcatenatePdfFormsAndKeepFieldsUnique()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Concatenate();
    // Set input and output file paths
    var inputFile1 = dataDir + "ConcatenatePdfFormsAndKeepFieldsUnique1.pdf";
    var inputFile2 = dataDir + "ConcatenatePdfFormsAndKeepFieldsUnique2.pdf";
    var outFile = dataDir + "ConcatenatePDFForms_out.pdf";
    // Open PDF documents
    var fileEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // To keep unique field Id for all the fields 
    fileEditor.KeepFieldsUnique = true;
    // Format of the suffix which is added to field name to make it unique when forms are concatenated.
    fileEditor.UniqueSuffix = "_%NUM%";
    // Concatenate the files into a resultant Pdf file
    fileEditor.Concatenate(inputFile1, inputFile2, outFile);
}
```

## Concaténer des fichiers PDF et créer une table des matières

## Concaténer des fichiers PDF

Veuillez jeter un œil à l'extrait de code suivant pour des informations sur la façon de fusionner les fichiers PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConcatenatePdfFiles()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Concatenate();
    // Set input and output file paths
    var inputFile1 = dataDir + "ConcatenateInput1.pdf";
    var inputFile2 = dataDir + "ConcatenateInput2.pdf";
    var outFile = dataDir + "ConcatenatePdfFilesAndCreateTOC_out.pdf";
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();

    // Open PDF documents
    using (var outputStream = new FileStream(outFile, FileMode.Create))
    {
        using (var stream1 = new FileStream(inputFile1, FileMode.Open))
        {
            using (var stream2 = new FileStream(inputFile2, FileMode.Open))
            {
                // Save concatenated output file
                pdfEditor.Concatenate(stream1, stream2, outputStream);
            }
        }
    }
}
```

### Insérer une page blanche

Une fois que les fichiers PDF ont été fusionnés, nous pouvons insérer une page blanche au début du document sur laquelle nous pouvons créer une table des matières. Pour accomplir cette exigence, nous pouvons charger le fichier fusionné dans un objet **Document** et nous devons appeler la méthode Page.Insert(...) pour insérer une page blanche.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void InsertBlankPage()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Concatenate();
    // Insert a blank page at the beginning of concatenated file to display Table of Contents
    using (var document = new Aspose.Pdf.Document(dataDir + "ConcatenatePdfFilesAndCreateTOC_out.pdf"))
    {
        // Insert a blank page in a PDF
        document.Pages.Insert(1);
    }
}
```

### Ajouter des tampons de texte

Pour créer une table des matières, nous devons ajouter des tampons de texte sur la première page en utilisant [PdfFileStamp](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades/pdffilestamp) et des objets [Stamp](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades/stamp). La classe Stamp fournit la méthode `BindLogo(...)` pour ajouter [FormattedText](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades/formattedtext) et nous pouvons également spécifier l'emplacement pour ajouter ces tampons de texte en utilisant la méthode `SetOrigin(..)`. Dans cet article, nous concaténons deux fichiers PDF, donc nous devons créer deux objets de tampon de texte pointant vers ces documents individuels.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddTextStampForTableOfContents()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Concatenate();
    var inputPdfFile = Path.Combine(dataDir, "ConcatenateInput1.pdf");
    // Set Text Stamp to display string Table Of Contents
    var stamp = new Aspose.Pdf.Facades.Stamp();
    stamp.BindLogo(new Aspose.Pdf.Facades.FormattedText("Table Of Contents", System.Drawing.Color.Maroon, System.Drawing.Color.Transparent, Aspose.Pdf.Facades.FontStyle.Helvetica, Aspose.Pdf.Facades.EncodingType.Winansi, true, 18));
    // Specify the origin of Stamp. We are getting the page width and specifying the X coordinate for stamp
    stamp.SetOrigin(new Aspose.Pdf.Facades.PdfFileInfo(inputPdfFile).GetPageWidth(1) / 3, 700);
    // Set particular pages
    stamp.Pages = new[] { 1 };
}
```

### Créer des liens locaux

Maintenant, nous devons ajouter des liens vers les pages à l'intérieur du fichier concaténé. Pour accomplir cette exigence, nous pouvons utiliser la méthode `CreateLocalLink(..)` de la classe [PdfContentEditor](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades/pdfcontenteditor). Dans l'extrait de code suivant, nous avons passé Transparent comme 4ème argument afin que le rectangle autour du lien ne soit pas visible.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CreateLocalLinks()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Concatenate();
    // Now we need to add Heading for Table Of Contents and links for documents
    var contentEditor = new Aspose.Pdf.Facades.PdfContentEditor();
    // Bind PDF document
    contentEditor.BindPdf(dataDir + "ConcatenatePdfFilesAndCreateTOC_out.pdf");
    // Create link for first document
    contentEditor.CreateLocalLink(new System.Drawing.Rectangle(150, 650, 100, 20), 2, 1, System.Drawing.Color.Transparent);
}
```

### Code complet

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CompleteCode()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Concatenate();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Create a MemoryStream object to hold the resultant PDf file
    using (var concatenatedStream = new MemoryStream())
    {
        using (var fs1 = new FileStream(dataDir + "ConcatenateInput1.pdf", FileMode.Open))
        {
            using (var fs2 = new FileStream(dataDir + "ConcatenateInput2.pdf", FileMode.Open))
            {
                // Save concatenated output file
                pdfEditor.Concatenate(fs1, fs2, concatenatedStream);
            }
        }

        using (var concatenatedPdfDocument = new Aspose.Pdf.Document(concatenatedStream))
        {
            // Insert a blank page at the beginning of concatenated file to display Table of Contents
            concatenatedPdfDocument.Pages.Insert(1);

            // Hold the result file with empty page added
            using (var documentWithBlankPage = new MemoryStream())
            {
                // Save PDF document
                concatenatedPdfDocument.Save(documentWithBlankPage);

                using (var documentWithTocHeading = new MemoryStream())
                {
                    // Add Table Of Contents logo as stamp to PDF file
                    var fileStamp = new Aspose.Pdf.Facades.PdfFileStamp();
                    // Bind PDF document
                    fileStamp.BindPdf(documentWithBlankPage);

                    // Set Text Stamp to display string Table Of Contents
                    var stamp = new Aspose.Pdf.Facades.Stamp();
                    stamp.BindLogo(new Aspose.Pdf.Facades.FormattedText("Table Of Contents", System.Drawing.Color.Maroon, System.Drawing.Color.Transparent,
                        Aspose.Pdf.Facades.FontStyle.Helvetica, Aspose.Pdf.Facades.EncodingType.Winansi, true, 18));
                    // Specify the origin of Stamp. We are getting the page width and specifying the X coordinate for stamp
                    stamp.SetOrigin(new Aspose.Pdf.Facades.PdfFileInfo(documentWithBlankPage).GetPageWidth(1) / 3, 700);
                    // Set particular pages
                    stamp.Pages = new[] { 1 };
                    // Add stamp to PDF file
                    fileStamp.AddStamp(stamp);

                    // Create stamp text for first item in Table Of Contents
                    var document1Link = new Aspose.Pdf.Facades.Stamp();
                    document1Link.BindLogo(new Aspose.Pdf.Facades.FormattedText("1 - Link to Document 1", System.Drawing.Color.Black, System.Drawing.Color.Transparent,
                        Aspose.Pdf.Facades.FontStyle.Helvetica, Aspose.Pdf.Facades.EncodingType.Winansi, true, 12));
                    // Specify the origin of Stamp. We are getting the page width and specifying the X coordinate for stamp
                    document1Link.SetOrigin(150, 650);
                    // Set particular pages on which stamp should be displayed
                    document1Link.Pages = new[] { 1 };
                    // Add stamp to PDF file
                    fileStamp.AddStamp(document1Link);

                    // Create stamp text for second item in Table Of Contents
                    var document2Link = new Aspose.Pdf.Facades.Stamp();
                    document2Link.BindLogo(new Aspose.Pdf.Facades.FormattedText("2 - Link to Document 2", System.Drawing.Color.Black, System.Drawing.Color.Transparent,
                        Aspose.Pdf.Facades.FontStyle.Helvetica, Aspose.Pdf.Facades.EncodingType.Winansi, true, 12));
                    // Specify the origin of Stamp. We are getting the page width and specifying the X coordinate for stamp
                    document2Link.SetOrigin(150, 620);
                    // Set particular pages on which stamp should be displayed
                    document2Link.Pages = new[] { 1 };
                    // Add stamp to PDF file
                    fileStamp.AddStamp(document2Link);

                    // Save PDF document
                    fileStamp.Save(documentWithTocHeading);
                    fileStamp.Close();

                    // Now we need to add Heading for Table Of Contents and links for documents
                    var contentEditor = new Aspose.Pdf.Facades.PdfContentEditor();
                    // Bind PDF document
                    contentEditor.BindPdf(documentWithTocHeading);
                    // Create link for first document
                    contentEditor.CreateLocalLink(new System.Drawing.Rectangle(150, 650, 100, 20), 2, 1, System.Drawing.Color.Transparent);
                    // Create link for Second document
                    // We have used   new PdfFileInfo("d:/pdftest/Input1.pdf").NumberOfPages + 2   as PdfFileInfo.NumberOfPages(..) returns the page count for first document
                    // And 2 is because, second document will start at Input1+1 and 1 for the page containing Table Of Contents.
                    contentEditor.CreateLocalLink(new System.Drawing.Rectangle(150, 620, 100, 20),
                        new Aspose.Pdf.Facades.PdfFileInfo(dataDir + "ConcatenateInput1.pdf").NumberOfPages + 2, 1, System.Drawing.Color.Transparent);
                    // Save PDF document
                    contentEditor.Save(dataDir + "Concatenated_Table_Of_Contents_out.pdf");
                }
            }
        }
    }
}
```

## Concaténer des fichiers PDF dans un dossier

La classe [PdfFileEditor](https://reference.aspose.com/pdf/fr/net/aspose.pdf.facades/pdffileeditor) dans le namespace Aspose.Pdf.Facades vous offre la capacité de concaténer le fichier PDF. Vous pouvez même lire tous les fichiers PDF dans un dossier particulier à l'exécution et les concaténer, sans même connaître les noms de fichiers. Il suffit de fournir le chemin du répertoire qui contient les documents PDF que vous souhaitez concaténer.

Veuillez essayer d'utiliser l'extrait de code C# suivant pour réaliser cette fonctionnalité à partir d'Aspose.PDF :

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConcatenatePdfFilesInFolder()
{ 
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Concatenate();
    // Retrieve names of all the Pdf files in a particular Directory
    string[] fileEntries = Directory.GetFiles(dataDir, "*.pdf");
    // Create PdfFileEditor
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Call Concatenate method of PdfFileEditor object to concatenate all input files
    // Into a single output file
    pdfEditor.Concatenate(fileEntries, dataDir + "ConcatenatePdfFilesInFolder_out.pdf");
}
```