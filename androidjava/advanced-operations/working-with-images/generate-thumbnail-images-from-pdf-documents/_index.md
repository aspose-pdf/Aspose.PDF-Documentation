---
title: Generate Thumbnail Images from PDF Documents
linktitle: Generate Thumbnail Images
type: docs
weight: 100
url: /androidjava/generate-thumbnail-images-from-pdf-documents/
description: This section describes how to generate thumbnail images from PDF documents using Aspose.PDF for Java.
lastmod: "2021-06-05"
---

## Aspose.PDF for Java Approach

Aspose.PDF for Java provides extensive support for dealing with PDF documents. It also supports the capability to convert the pages of PDF documents to a variety of image formats. The functionality described above can easily be achieved using Aspose.PDF for Java.

Aspose.PDF has distinct benefits:

- You don't need to have Adobe Acrobat installed on your system to work with PDF files.
- Using Aspose.PDF for Java is simple and easy to understand as compared to Acrobat Automation.

If we need to convert PDF pages into JPEGs, the [com.aspose.pdf.devices](https://apireference.aspose.com/pdf/java/com.aspose.pdf.devices/package-frame) namespace provides a class named [JpegDevice](https://apireference.aspose.com/pdf/java/com.aspose.pdf.devices/JpegDevice) for rendering PDF pages into JPEG images. Please take a look over the following code snippet.

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.Document;
import com.aspose.pdf.devices.JpegDevice;
import com.aspose.pdf.devices.Resolution;

import java.io.FileOutputStream;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.List;
import java.util.stream.Collectors;

public class ExampleGenerateThumbnails {
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void GenerateThumbnails() throws IOException {
        // Retrieve names of all the PDF files in a particular directory
        List<String> fileEntries = null;
        try {
            fileEntries = Files.list(Paths.get(_dataDir)).filter(Files::isRegularFile)
                    .filter(path -> path.toString().endsWith(".pdf")).map(path -> path.toString())
                    .collect(Collectors.toList());

        } catch (IOException e) {
            // Error while reading the directory
        }

        // Iterate through all the files entries in array
        for (int counter = 0; counter < fileEntries.size(); counter++) {
            // Open document
            Document pdfDocument = new Document(fileEntries.get(counter));

            for (int pageCount = 1; pageCount <= 4; pageCount++) {
                FileOutputStream imageStream = new FileOutputStream(
                        _dataDir + "\\Thumbnails" + counter + "_" + pageCount + ".jpg");
                // Create Resolution object
                Resolution resolution = new Resolution(300);
                JpegDevice jpegDevice = new JpegDevice(45, 59, resolution, 100);
                // Convert a particular page and save the image to stream
                jpegDevice.process(pdfDocument.getPages().get_Item(pageCount), imageStream);
                // Close stream
                imageStream.close();
            }
        }

    }
}
```