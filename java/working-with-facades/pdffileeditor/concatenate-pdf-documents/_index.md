---
title: Concatenate PDF documents
type: docs
weight: 10
url: /java/concatenate-pdf-documents/
description: This section explains how to concatenate PDF documents with com.aspose.pdf.facades using PdfFileEditor class.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Concatenate PDF Files Using File Paths (Facades)

concatenate method of [PdfFileEditor](https://apireference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileEditor) class can be used to concatenate two PDF files. The concatenate method allows you to pass three parameters: first input PDF, second input PDF, and output PDF. The final output PDF contains both the input PDF files.

The following code snippet shows you how to concatenate PDF files using file paths.

```java
    public static void ConcatenatePDFfilesUsingFilePaths01() {
        // Create PdfFileEditor object
        PdfFileEditor pdfEditor = new PdfFileEditor();
        // Concatenate files
        pdfEditor.concatenate(_dataDir + "Sample-Document-01.pdf", _dataDir + "Sample-Document-02.pdf",
                _dataDir + "Concatenate_Result_01.pdf");
    }
```

In some cases, when there are a lot of outlines, users may disable them with setting **CopyOutlines** to false and improve performance of concatenation.

```java
  public static void ConcatenatePDFfilesUsingFilePaths02() {
        // Create PdfFileEditor object
        PdfFileEditor pdfEditor = new PdfFileEditor();
        // Concatenate files
        String[] inputFiles = Directory.GetFiles(_dataDir, "Sample-Document-0?.pdf");
        pdfEditor.CopyOutlines = false;
        var res = pdfEditor.Concatenate(inputFiles, _dataDir + "Concatenate_Result_02.pdf");
        Console.WriteLine(res);
    }

```

## Concatenate multiple PDF files using MemoryStreams

[Concatenate]https://apireference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileEditor#concatenate-com.aspose.pdf.IDocument:A-com.aspose.pdf.IDocument-) method of [PdfFileEditor](https://apireference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileEditor) class takes the source PDF files and the destination PDF file as parameters. These parameters can be either paths to the PDF files on the disk or they could be MemoryStreams. Now, for this example, we’ll first create two files streams to read the PDF files from the disk. Then we’ll convert these files into byte arrays. These byte arrays of the PDF files will be converted to MemoryStreams. Once we get the MemoryStreams out of PDF files, we’ll be able to pass them on to the concatenate method and merge into a single output file.

The following code snippet shows you how to concatenate multiple PDF files using MemoryStreams:

```java
    public static void ConcatenateMultiplePDFfilesUsingMemoryStreams()
        {
            // Create two file streams to read pdf files
            FileInputStream fs1 = new FileInputStream(_dataDir + "Sample-Document-01.pdf");
            FileInputStream fs2 = new FileInputStream(_dataDir + "Sample-Document-02.pdf");

            // Create byte arrays to keep the contents of PDF files
            byte[] buffer1 = new byte[Convert.ToInt32(fs1.le)];
            byte[] buffer2 = new byte[Convert.ToInt32(fs2.Length)];

            // Read PDF file contents into byte arrays
            fs1.Read(buffer1, 0, Convert.ToInt32(fs1.Length));
            fs2.Read(buffer2, 0, Convert.ToInt32(fs2.Length));

            // Now, first convert byte arrays into MemoryStreams and then concatenate those streams
            using (MemoryStream pdfStream = new MemoryStream())
            {
                using (MemoryStream fileStream1 = new MemoryStream(buffer1))
                {
                    using (MemoryStream fileStream2 = new MemoryStream(buffer2))
                    {
                        // Create instance of PdfFileEditor class to concatenate streams
                        PdfFileEditor pdfEditor = new PdfFileEditor();
                        // Concatenate both input MemoryStreams and save to putput MemoryStream
                        pdfEditor.Concatenate(fileStream1, fileStream2, pdfStream);
                        // Convert MemoryStream back to byte array
                        byte[] data = pdfStream.ToArray();
                        // Create a FileStream to save the output PDF file
                        FileStream output = new FileStream(_dataDir + "Concatenate_Result_03.pdf", FileMode.Create,
                        FileAccess.Write);
                        // Write byte array contents in the output file stream
                        output.Write(data, 0, data.Length);
                        // Close output file
                        output.Close();
                    }
                }
            }
            // Close input files
            fs1.Close();
            fs2.Close();
        }
```

## Concatenate Array of PDF Files Using File Paths (Facades)

If you want to concatenate multiple PDF files, you can use the overload of the concatenate method, which allows you to pass an array of PDF files path. The final output is saved as a merged file created from all the files in the array.

The following code snippet shows you how to concatenate array of PDF files using file paths.

```java
 public static void ConcatenateArrayOfPDFfilesUsingFilePaths() {
        // Create PdfFileEditor object
        PdfFileEditor pdfEditor = new PdfFileEditor();
        // Array of files
        string[] filesArray = new string[2];
        filesArray[0] = _dataDir + "Sample-Document-01.pdf";
        filesArray[1] = _dataDir + "Sample-Document-02.pdf";
        // Concatenate files
        pdfEditor.Concatenate(filesArray, _dataDir + "Concatenate_Result_04.pdf");
    }
```

## Concatenate Array of PDF Files Using Streams (Facades)

Concatenating an array of PDF files is not limited to only files residing on the disk. You can also concatenate an array of PDF files from streams. If you want to concatenate multiple PDF files, you can use the appropriate overload of the Concatenate method. First, you need to create an array of input streams and one stream for output PDF and then call the Concatenate method. The output will be saved in the output stream.

The following code snippet shows you how to concatenate array of PDF files using streams.

```java
   public static void ConcatenateArrayOfPDFfilesUsingStreams() {
        // Create PdfFileEditor object
        PdfFileEditor pdfEditor = new PdfFileEditor();
        // Array of streams
        FileStream[] inputStreams = new FileStream[2];
        inputStreams[0] = new FileStream(_dataDir + "Sample-Document-01.pdf", FileMode.Open);
        inputStreams[1] = new FileStream(_dataDir + "Sample-Document-02.pdf", FileMode.Open);
        // Output stream
        FileStream outputStream = new FileStream(_dataDir + "Concatenate_Result_05.pdf", FileMode.Create);
        // Concatenate file
        pdfEditor.Concatenate(inputStreams, outputStream);
    }
```

## Concatenate PDF Forms and keep fields names unique

P[PdfFileEditor](https://apireference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileEditor) class in [com.aspose.pdf.facades](https://apireference.aspose.com/pdf/java/com.aspose.pdf.facades/package-frame) namespace offers the capability to concatenate the PDF files. Now, if the Pdf files which are to be concatenated have form fields with similar field names, Aspose.PDF provides the feature to keep the fields in the resultant Pdf file as unique and also you can specify the suffix to make the field names unique. [KeepFieldsUnique](https://apireference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileEditor#getKeepFieldsUnique--) method of PdfFileEditor as true will make field names unique when Pdf forms are concatenated. Also, [UniqueSuffix](https://apireference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileEditor#getUniqueSuffix--) method of PdfFileEditor can be used to specify the user defined format of the suffix which is added to field name to make it unique when forms are concatenated. This string must contain %NUM% substring which will be replaced with numbers in the resultant file.

Please see the following simple code snippet to achieve this functionality.

```java
  public static void ConcatenatePDFformsAndKeepFieldsNamesUnique()
        {
            // Set input and output file paths

            string inputFile1 = _dataDir + "Sample-Form-01.pdf";
            string inputFile2 = _dataDir + "Sample-Form-02.pdf";
            string outFile = _dataDir + "ConcatenatePDFForms_out.pdf";

            // Instantiate PdfFileEditor Object
            PdfFileEditor fileEditor = new PdfFileEditor
            {
                // To keep unique field Id for all the fields
                KeepFieldsUnique = true,
                // Format of the suffix which is added to field name to make it unique when forms are concatenated.
                UniqueSuffix = "_%NUM%"
            };

            // Concatenate the files into a resultant Pdf file
            fileEditor.Concatenate(inputFile1, inputFile2, outFile);
        }
```

## Concatenate Insert blank page

Once the PDF files have been merged, we can insert a blank page at the beginning of document on which can can create Table Of contents. In order to accomplish this requirement, we can load the merged file into Document object and we need to call Page.Insert(…) method to insert a blank page.

```java
   public static void ConcatenatePDF_InsertBlankPage() {
        // Create PdfFileEditor object
        PdfFileEditor pdfEditor = new PdfFileEditor();
        var documents = new Aspose.Pdf.Document[3];
        documents[0] = new Aspose.Pdf.Document(_dataDir + "Sample-Document-01.pdf");
        documents[1] = new Aspose.Pdf.Document(_dataDir + "Sample-Document-02.pdf");
        var destinationDoc = new Aspose.Pdf.Document();
        destinationDoc.Pages.Add();
        // Concatenate files
        pdfEditor.Concatenate(documents, destinationDoc);
        destinationDoc.Save(_dataDir + "Concatenate_Result_06.pdf");
    }
```