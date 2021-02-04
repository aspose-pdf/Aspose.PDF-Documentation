
Computer Graphics Metafile (CGM) is an ISO standard that provides a vector-based 2D image file format for the storage and retrieval of graphics information. CGM is a device-independent format. CGM is a vector graphics format that supports three different encoding methods: binary (best for program read speed), character-based (produces the smallest file size and allows for faster data transfers) or cleartext encoding (allows users to read and modify the file with a text editor)

The following code snippet shows you how to convert CGM files to PDF format using Aspose.PDF for Java.

1. Create a CGM [`LoadOptions`](https://apireference.aspose.com/pdf/java/com.aspose.pdf.class-use/loadoptions) class.
1. Create an instance of [`Document`](https://apireference.aspose.com/page/java/com.aspose.page/Document) class with mention source filename and options.
1. Save the document with the desired file name.

```java
package com.aspose.pdf.examples;

import java.io.FileNotFoundException;
import java.nio.file.Path;
import java.nio.file.Paths;

import com.aspose.pdf.*;

public final class ConvertCGMtoPDF {

    private ConvertCGMtoPDF() {
    }

    private static Path _dataDir = Paths.get("/home/admin1/pdf-examples/Samples");

    public static void main(String[] args) throws FileNotFoundException {
        
        // Create a CGM LoadOptions
        CgmLoadOptions options = new CgmLoadOptions();

        // Initialize document object
        String cgmFileName = Paths.get(_dataDir.toString(), "corvette.cgm").toString();
        Document document = new Document(cgmFileName, options);

        // Save output PDF document
        document.save(Paths.get(_dataDir.toString(),"CGMtoPDF.pdf").toString());
    }
}
```
