---
title: Print PDF document in WPF application using Aspose.PDF for .NET
linktitle: Print PDF document in WPF application
type: docs
weight: 50
url: /net/print-pdf-document-in-wpf-application/
description: C# Print PDF documents from a WPF application. This code sample shows how to print PDF documents from a WPF application using C#.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Direct print

The Aspose.PDF library has the ability to convert PDF files to XPS. We can use this function to organize the printing of documents.
Let's consider the example for direct printing:

```csharp
    private void Print_OnClick(object sender, RoutedEventArgs e)
    {
        var openFileDialog = new OpenFileDialog
        {
            Filter = "PDF Documents|*.pdf"
        };
        openFileDialog.ShowDialog();

        Aspose.Pdf.Document document = new Document(openFileDialog.FileName);
        var memoryStream = new MemoryStream();
        document.Save(memoryStream, SaveFormat.Xps);
        var package = Package.Open(memoryStream);

        //Create URI for Xps Package
        //Any Uri will actually be fine here. It acts as a place holder for the
        //Uri of the package inside of the PackageStore
        var inMemoryPackageName = $"memorystream://{Guid.NewGuid()}.xps";
        var packageUri = new Uri(inMemoryPackageName);

        //Add package to PackageStore
        PackageStore.AddPackage(packageUri, package);

        var xpsDoc = new XpsDocument(package, CompressionOption.Maximum, inMemoryPackageName);
        var fixedDocumentSequence = xpsDoc.GetFixedDocumentSequence();

        var printDialog = new PrintDialog();
        if (printDialog.ShowDialog() == true)
        {
            if (fixedDocumentSequence != null)
                printDialog.PrintDocument(fixedDocumentSequence.DocumentPaginator, "A fixed document");
            else
                throw new NullReferenceException();
        }
        PackageStore.RemovePackage(packageUri);
        xpsDoc.Close();

    }
```

In this case, we will follow these steps:

1. Open PDF file using OpenFileDialog
1. Convert PDF to XPS and store it in MemoryStream object
1. Associate MemoryStream object with Xps Package
1. Add the package to the Package Store
1. Create an XpsDocument based on package
1. Get an instance of the FixedDocumentSequence
1. Send this sequence to the printer using PrintDialog

## View and print document

In many cases, users want to see the document before printing. To implement a view, we can use a DocViewer class.
Most of the steps for implementing this approach are similar to the previous example.

```csharp
private void OpenFile_OnClick(object sender, RoutedEventArgs e)
{
    var openFileDialog = new OpenFileDialog
    {
        Filter = "PDF Documents|*.pdf"
    };

    if (openFileDialog.ShowDialog() == true)
    {
        var document = new Document(openFileDialog.FileName);
        var memoryStream = new MemoryStream();
        document.Save(memoryStream, SaveFormat.Xps);

        var package = Package.Open(memoryStream);

        var inMemoryPackageName = $"memorystream://{Guid.NewGuid()}.xps";
        var packageUri = new Uri(inMemoryPackageName);

        //Add package to PackageStore
        PackageStore.AddPackage(packageUri, package);

        var xpsDoc = new XpsDocument(package, CompressionOption.Maximum, inMemoryPackageName);
        DocViewer.Document = xpsDoc.GetFixedDocumentSequence();
        xpsDoc.Close();
    };
}
```
