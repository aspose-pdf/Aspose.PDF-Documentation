
{{% alert color="primary" %}} 

EPUB (short for electronic publication) is a free and open e-book standard from the International Digital Publishing Forum (IDPF). Files have the extension .epub. EPUB is designed for reflowable content, meaning that an EPUB reader can optimize text for a particular display device. EPUB also supports fixed-layout content. The format is intended as a single format that publishers and conversion houses can use in-house, as well as for distribution and sale. It supersedes the Open eBook standard.

{{% /alert %}} 

In order to convert EPUB files to PDF format, Aspose.PDF for Java has a class named [EpubLoadOptions](https://apireference.aspose.com/java/pdf/com.aspose.pdf/EpubLoadOptions) which is used to load source EPUB file. After that, the object is passed as an argument to [Document](https://apireference.aspose.com/java/pdf/com.aspose.pdf/document) object initialization, as it helps the PDF rendering engine to determine the source document's input format.

{{% alert color="primary" %}} 

Try online. You can check the quality of Aspose.PDF conversion and view the results online at this link [products.aspose.app/pdf/conversion/epub-to-pdf](https://products.aspose.app/pdf/conversion/epub-to-pdf)

{{% /alert %}}

The following code snippet shows the process of converting an EPUB file into PDF format.

1. Create a EPUB [`LoadOptions`](https://apireference.aspose.com/pdf/java/com.aspose.pdf.class-use/loadoptions).
1. Initialize [`Document`](https://apireference.aspose.com/pdf/java/com.aspose.pdf.class-use/document) object.
1. Save output PDF document.

```java
package com.aspose.pdf.examples;

import java.io.FileNotFoundException;
import java.nio.file.Path;
import java.nio.file.Paths;

import com.aspose.pdf.*;

public final class ConvertEPUBtoPDF {

    private ConvertEPUBtoPDF() {
    }

    private static Path _dataDir = Paths.get("/home/admin1/pdf-examples/Samples");

    public static void main(String[] args) throws FileNotFoundException {
        
        // Create a EPUB LoadOptions
        EpubLoadOptions options = new EpubLoadOptions();

        // Initialize document object
        String epubFileName = Paths.get(_dataDir.toString(), "aliceDynamic.epub").toString();
        Document document = new Document(epubFileName, options);

        // Save output PDF document
        document.save(Paths.get(_dataDir.toString(),"EPUBtoPDF.pdf").toString());
    }
}
```

