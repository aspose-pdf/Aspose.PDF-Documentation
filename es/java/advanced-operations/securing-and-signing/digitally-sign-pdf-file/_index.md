---
title: Cómo firmar digitalmente un PDF
linktitle: Firmar digitalmente PDF
type: docs
weight: 10
url: /es/java/digitally-sign-pdf-file/
description: Firme digitalmente documentos PDF usando Java. Verifique o valide los PDFs firmados digitalmente con una aplicación basada en Java con PDF Library. Puede certificar un archivo PDF con un certificado PKCS1.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Al firmar un documento PDF usando una firma, básicamente confirma que su contenido debe permanecer "tal cual". Por lo tanto, cualquier cambio realizado posteriormente invalida la firma y, por lo tanto, sabe si el documento ha sido alterado. Certificar un documento primero, le permite especificar los cambios que un usuario puede hacer al documento sin invalidar la certificación.

En otras palabras, el documento aún se consideraría como que mantiene su integridad y el destinatario aún podría confiar en el documento. Para más detalles, por favor visite Certificar y firmar un PDF.

Para cumplir con el requisito mencionado anteriormente, se han realizado los siguientes cambios en la API pública.

isCertified(…) método se añade a la clase PdfFileSignature.

## Firmar PDF con firmas digitales

```java
public class ExampleDigitallySign {

    private static String _dataDir = "/home/aspose/pdf-examples/Samples/Secure-Sign/";

    public static void SignDocument() {
        String inFile = _dataDir + "DigitallySign.pdf";
        String outFile = _dataDir + "DigitallySign_out.pdf";
        Document document = new Document(inFile);

        PdfFileSignature signature = new PdfFileSignature(document);

        PKCS7 pkcs = new PKCS7("/home/aspose/pdf-examples/Samples/test.pfx", "Pa$$w0rd2020"); // Usar objetos PKCS7/PKCS7Detached
        signature.sign(1, true, new java.awt.Rectangle(300, 100, 400, 200), pkcs);
        // Guardar archivo PDF de salida
        signature.save(outFile);
    }
```

## Añadir marca de tiempo a la firma digital

Aspose.PDF para Java soporta firmar digitalmente el PDF con un servidor de marca de tiempo o servicio web.

Para cumplir con este requisito, la clase [TimestampSettings](https://reference.aspose.com/pdf/java/com.aspose.pdf/TimestampSettings) ha sido añadida al espacio de nombres Aspose.PDF. Por favor, echa un vistazo al siguiente fragmento de código que obtiene una marca de tiempo y la añade al documento PDF:

```java
    public static void SignWithTimeStampServer() {
        Document document = new Document(_dataDir + "SimpleResume.pdf");
        PdfFileSignature signature = new PdfFileSignature(document);

        PKCS7 pkcs = new PKCS7("/home/aspose/pdf-examples/Samples/test.pfx", "Start2020");
        TimestampSettings timestampSettings = new TimestampSettings("https://freetsa.org/tsr", ""); // Usuario/Contraseña puede
                                                                                                    // ser omitido
        pkcs.setTimestampSettings(timestampSettings);
        java.awt.Rectangle rect = new java.awt.Rectangle(100, 100, 200, 100);
        // Crear cualquiera de los tres tipos de firma
        signature.sign(1, "Razón de la Firma", "Contacto", "Ubicación", true, rect, pkcs);
        // Guardar el archivo PDF de salida
        signature.save(_dataDir + "DigitallySignWithTimeStamp_out.pdf");
    }
```