---
title: Opening a PDF document
type: docs
weight: 10
url: /net/opening-a-pdf-document/
---
# Opening a PDF document

## Opening an existing PDF document
There are several ways to open a document. The easiest is to specify a file name.

```csharp
public static void OpenDocument()
{
    var fileName = @"C:\tmp\tourguidev2_gb_tags.pdf";
    using (var pdfDocument = new Aspose.Pdf.Document(fileName))
    {
        Console.WriteLine($"Pages {pdfDocument.Pages.Count}");
    }
}
```

## Opening an existing PDF document from stream

```csharp
public static void OpenDocumentStream()
{
    const string fileName = "SJPR0033_Folder_Utland_16sid_ENG_web3.pdf";
    var remoteUri = "https://www.sj.se/content/dam/SJ/pdf/Engelska/";
    // Create a new WebClient instance.
    var webClient = new WebClient();
    // Concatenate the domain with the Web resource filename.
    var strWebResource = remoteUri + fileName;
    Console.WriteLine("Downloading File \"{0}\" from \"{1}\" .......\n\n", fileName, strWebResource);

    var stream = new MemoryStream();
    webClient.OpenRead(strWebResource)?.CopyTo(stream);

    using (var pdfDocument = new Aspose.Pdf.Document(stream))
    {
        Console.WriteLine($"Pages {pdfDocument.Pages.Count}");
    }
}
```

## Opening an encrypted PDF document

```csharp
    public static void OpenDocumentWithPassword()
    {
        const string fileName = @"C:\tmp\DocSite.pdf";
        const string password = "Aspose2020";
        try
        {
            using (var pdfDocument = new Aspose.Pdf.Document(fileName, password))
            {
                Console.WriteLine($"Pages {pdfDocument.Pages.Count}");
            }
        }
        catch (InvalidPasswordException e)
        {
            Console.WriteLine(e);
        }
    }
```
