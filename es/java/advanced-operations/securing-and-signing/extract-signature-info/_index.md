---
title: Extraer Información de Imagen y Firma
linktitle: Extraer Información de Imagen y Firma
type: docs
weight: 30
url: /es/java/extract-image-and-signature-information/
description: Puede extraer imágenes del campo de firma y extraer información de la firma utilizando la clase SignatureField con Java.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Extrayendo Imagen del Campo de Firma

Aspose.PDF para Java admite la funcionalidad de firmar digitalmente los archivos PDF utilizando la clase [SignatureField](https://reference.aspose.com/pdf/java/com.aspose.pdf/SignatureField) y al firmar el documento, también puede establecer una imagen para SignatureAppearance. Ahora, esta API también proporciona la capacidad de extraer información de la firma, así como la imagen asociada con el campo de firma.

Para extraer información de la firma, hemos introducido el método [ExtractImage](https://reference.aspose.com/pdf/java/com.aspose.pdf/SignatureField#extractImage--) en la clase [SignatureField](https://reference.aspose.com/pdf/java/com.aspose.pdf/SignatureField).
 Por favor, echa un vistazo al siguiente fragmento de código que demuestra los pasos para extraer una imagen del objeto SignatureField:

```java
public class ExampleExtractImageAndSignature {

    private static String _dataDir = "/home/aspose/pdf-examples/Samples/Secure-Sign/";

    public static void ExtractingImageFromSignatureField() {
        Document pdfDocument = new Document(_dataDir + "ExtractingImage.pdf");

        int i = 0;
        try {
            for (WidgetAnnotation field : pdfDocument.getForm()) {
                SignatureField sf = (SignatureField) field;
                if (sf != null) {
                    FileOutputStream output = new FileOutputStream(_dataDir + "im" + i + ".jpeg");
                    InputStream tempStream = sf.extractImage();
                    byte[] b = new byte[tempStream.available()];
                    tempStream.read(b);
                    output.write(b);
                    output.close();
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
        } finally {
            if (pdfDocument != null)
                pdfDocument.dispose();
        }

    }
```

### Reemplazar imagen de firma

A veces puede haber un requisito para solo reemplazar la imagen de un campo de firma ya presente dentro de un archivo PDF. Para cumplir con este requisito, primero necesitamos buscar campos de formulario dentro del archivo PDF, identificar los campos de firma, obtener las dimensiones (dimensiones rectangulares) del campo de firma y luego estampar una imagen sobre las mismas dimensiones.

## Extraer información de la firma

Aspose.PDF para Java admite la función de firmar digitalmente los archivos PDF usando la clase [SignatureField](https://reference.aspose.com/pdf/java/com.aspose.pdf/SignatureField). Actualmente, también podemos determinar la validez del certificado, pero no podemos extraer el certificado completo. La información que se puede extraer es una clave pública, huella digital, emisor, etc.

Para extraer información de la firma, hemos introducido el método [ExtractCertificate](https://reference.aspose.com/pdf/java/com.aspose.pdf/SignatureField#extractCertificate--) a la clase [SignatureField](https://reference.aspose.com/pdf/java/com.aspose.pdf/SignatureField).
 Por favor, echa un vistazo al siguiente fragmento de código que demuestra los pasos para extraer el certificado del objeto SignatureField:

```java
    public static void ExtractSignatureInformation() throws IOException {
        String input = _dataDir + "ExtractSignatureInfo.pdf";
        Document pdfDocument = new Document(input);

        for (WidgetAnnotation field : pdfDocument.getForm()) {
            SignatureField sf = (SignatureField) field;
            if (sf != null) {
                InputStream cerStream = sf.extractCertificate();
                if (cerStream != null) {

                    byte[] buffer = new byte[cerStream.available()];
                    cerStream.read(buffer);

                    File targetFile = new File(_dataDir+"targetFile.cer");
                    OutputStream outStream = new FileOutputStream(targetFile);
                    outStream.write(buffer);
                    outStream.close();
                }
            }
        }
    }
}
```