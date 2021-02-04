
DICOM (Digital Imaging and Communications in Medicine) is a standard for handling, storing, printing, and transmitting information in medical imaging. It includes a file format definition and a network communications protocol.

Aspsoe.PDF for Java allows you to convert DICOM files to PDF format, check next code snippet:

1. Load image into stream
1. Initialize [`Document object`](https://apireference.aspose.com/pdf/java/com.aspose.pdf/document)
1. Load sample DICOM image file
1. Save output PDF document

```java
package com.aspose.pdf.examples;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.nio.file.Path;
import java.nio.file.Paths;

import com.aspose.pdf.*;

public final class ConvertDICOMtoPDF {

    private ConvertDICOMtoPDF() {
    }

    private static Path _dataDir = Paths.get("/home/admin1/pdf-examples/Samples");

    public static void main(String[] args) throws FileNotFoundException {
        
        // Load image into stream
        FileInputStream imageStream = new FileInputStream(
            new java.io.File(Paths.get(_dataDir.toString(),"0002.dcm").toString()));

        // Initialize document object
        Document document = new Document();
        document.getPages().add();
        
        // Load sample DICOM image file
        Image image = new Image();
        image.setFileType(ImageFileType.Dicom);
        image.setImageStream(imageStream);

        document.getPages().get_Item(1).getParagraphs().add(image);

        // Save output PDF document
        document.save(Paths.get(_dataDir.toString(),"CGMtoPDF.pdf").toString());
    }
}
```
