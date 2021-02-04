package com.aspose.pdf.examples;

import java.io.IOException;
import java.nio.file.Path;
import java.nio.file.Paths;

import com.aspose.pdf.*;

public final class ConvertPDFtoXML {

    private ConvertPDFtoXML() {

    }

    private static Path _dataDir = Paths.get("/home/admin1/pdf-examples/Samples");

    public static void main(String[] args) throws IOException {
        String pdfDocumentFileName = Paths.get(_dataDir.toString(), "PDFtoXML.pdf").toString();
        String mobiXmlDocumentFileName = Paths.get(_dataDir.toString(), "PDFtoXML_out.xml").toString();
        
        // Create Document object
        Document doc = new Document(pdfDocumentFileName);

        // Save output in XML format
        doc.save(mobiXmlDocumentFileName, SaveFormat.MobiXml);
    }

}
