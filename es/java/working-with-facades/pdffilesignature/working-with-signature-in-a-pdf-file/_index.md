---
title: Trabajando con Firma en Archivo PDF
type: docs
weight: 40
url: /es/java/working-with-signature-in-a-pdf-file/
description: Esta sección explica cómo trabajar con Firma en un Archivo PDF usando la clase PdfFileSignature.
lastmod: "2021-06-05"
draft: false
---

## Cómo Extraer Información de la Firma

Aspose.PDF para Java admite la función de firmar digitalmente archivos PDF usando la clase PdfFileSignature. Actualmente, también es posible determinar la validez de un certificado, pero no podemos extraer el certificado completo. La información que se puede extraer es la clave pública, huella digital, emisor, etc.

Para extraer información de la firma, hemos introducido el método extractCertificate(..) a la clase PdfFileSignature. Por favor, observe el siguiente fragmento de código que demuestra los pasos para extraer el certificado del objeto PdfFileSignature:

```java
public static void ExtractSignatureInfo() {
        String input = _dataDir + "DigitallySign.pdf";
        String certificateFileName = "extracted_cert.pfx";
        PdfFileSignature pdfFileSignature = new PdfFileSignature();
        pdfFileSignature.bindPdf(input);
        List<String> sigNames = pdfFileSignature.getSignNames();

        if (sigNames.size() > 0) {
            String sigName = sigNames.get(0);
            if (sigName != "") {
                InputStream cerStream = pdfFileSignature.extractCertificate(sigName);
                if (cerStream != null) {
                    FileOutputStream fs;
                    try {
                        fs = new FileOutputStream(_dataDir + certificateFileName);
                        cerStream.transferTo(fs);
                    } catch (IOException e) {
                        e.printStackTrace();
                    }

                }
            }
        }
    }
```


## Extrayendo Imagen del Campo de Firma (PdfFileSignature)

Aspose.PDF para Java soporta la funcionalidad de firmar digitalmente los archivos PDF usando la clase PdfFileSignature y mientras se firma el documento, también puedes establecer una imagen para SignatureAppearance. Ahora esta API también proporciona la capacidad de extraer información de la firma así como la imagen asociada con el campo de firma.

Para extraer información de la firma, hemos introducido el método [extractImage(..)](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSignature#extractImage-java.lang.String-) a la clase PdfFileSignature. Por favor, echa un vistazo al siguiente fragmento de código que demuestra los pasos para extraer la imagen del objeto PdfFileSignature:

```java
 public static void ExtractSignatureImage() {
        PdfFileSignature signature = new PdfFileSignature();
        signature.bindPdf(_dataDir + "DigitallySign.pdf");
        if (signature.containsSignature()) {
            for (String sigName : signature.getSignNames()) {
                String outFile = _dataDir + sigName + "_ExtractImages_out.jpg";
                InputStream imageStream = signature.extractImage(sigName);
                if (imageStream != null) {
                    FileOutputStream fs;
                    try {
                        fs = new FileOutputStream(outFile);
                        imageStream.transferTo(fs);
                    } catch (IOException e) {
                        e.printStackTrace();
                    }
                }
            }
        }
    }
```


## Suprimir Ubicación y Razón

La funcionalidad de Aspose.PDF permite una configuración flexible para la instancia de firma digital. La clase [PdfFileSignature ](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSignature) proporciona la capacidad de firmar un archivo PDF. La implementación del método Sign permite firmar el PDF y pasar el objeto de firma particular a esta clase. El método Sign contiene un conjunto de atributos para la personalización de la firma digital de salida. En caso de que necesites suprimir algunos atributos de texto de la firma resultante, puedes dejarlos vacíos. El siguiente fragmento de código demuestra cómo suprimir las dos filas de Ubicación y Razón del bloque de firma:

```java
public static void SupressLocationReason() {
        PdfFileSignature pdfSign = new PdfFileSignature();
        pdfSign.bindPdf(_dataDir + "sample01.pdf");

        // Crear un rectángulo para la ubicación de la firma
        java.awt.Rectangle rect = new java.awt.Rectangle(10, 10, 300, 50);

        // Establecer la apariencia de la firma
        pdfSign.setSignatureAppearance(_dataDir + "aspose-logo.png");

        // Crear cualquiera de los tres tipos de firma
        PKCS1 signature = new PKCS1(_dataDir + "test01.pfx", "Aspose2021"); // PKCS#1

        pdfSign.sign(1, "", "test01@aspose-pdf-demo.local", "", true, rect, signature);
        // Guardar el archivo PDF de salida
        pdfSign.save(_dataDir + "DigitallySign.pdf");
    }
```


## Características de Personalización para Firma Digital

Aspose.PDF para Java permite características de personalización para una firma digital. El método Sign de la clase SignatureCustomAppearance se implementa con 6 sobrecargas para su uso cómodo. Por ejemplo, puede configurar la firma resultante solo mediante una instancia de la clase SignatureCustomAppearance y los valores de sus propiedades. El siguiente fragmento de código demuestra cómo ocultar el texto "Firmado digitalmente por" de la firma digital de salida de su PDF.

```java
    public static void CustomizationFeaturesForDigitalSign() {
        PdfFileSignature pdfSign = new PdfFileSignature();
        pdfSign.bindPdf(_dataDir + "sample01.pdf");

        // Crear un rectángulo para la ubicación de la firma
        java.awt.Rectangle rect = new java.awt.Rectangle(10, 10, 300, 50);

        // Crear cualquiera de los tres tipos de firma
        PKCS1 signature = new PKCS1(_dataDir + "test01.pfx", "Aspose2021"); // PKCS#1

        SignatureCustomAppearance signatureCustomAppearance = new SignatureCustomAppearance();
        signatureCustomAppearance.setFontSize(6);
        signatureCustomAppearance.setFontFamilyName("Times New Roman");
        signatureCustomAppearance.setDigitalSignedLabel("FIRMADO POR:");
        signature.setCustomAppearance(signatureCustomAppearance);

        pdfSign.sign(1, true, rect, signature);
        // Guardar el archivo PDF de salida
        pdfSign.save(_dataDir + "DigitallySign.pdf");
    }
```


## Cambiar Idioma En Texto De Firma Digital

Usando Aspose.PDF para la API de Java, puede firmar un archivo PDF utilizando cualquiera de los siguientes tres tipos de firmas:

- PKCS#1
- PKCS#7
- PKCS#7

Cada una de las firmas proporcionadas contiene un conjunto de propiedades de configuración implementadas para su conveniencia (localización, formato de fecha y hora, familia de fuentes, etc.). La clase SignatureCustomAppearance proporciona la funcionalidad correspondiente. El siguiente fragmento de código demuestra cómo cambiar el idioma en el texto de la firma digital:

```java
     public static void ChangeLanguageInDigitalSignText() {
        String inFile = _dataDir + "sample01.pdf";
        String outFile = _dataDir + "DigitallySign.pdf";

        PdfFileSignature pdfSign = new PdfFileSignature();

        pdfSign.bindPdf(inFile);
        // crear un rectángulo para la ubicación de la firma
        java.awt.Rectangle rect = new java.awt.Rectangle(310, 45, 200, 50);

        // crear cualquiera de los tres tipos de firma
        PKCS7 pkcs = new PKCS7(_dataDir + "test01.pfx", "Aspose2021");
        pkcs.setReason("Pruebas Firma");
        pkcs.setContactInfo("Contacto Pruebas");
        pkcs.setLocation("Población (Provincia)");
        pkcs.setDate(new Date());
        SignatureCustomAppearance signatureCustomAppearance = new SignatureCustomAppearance();
        signatureCustomAppearance.setDateSignedAtLabel("Fecha");
        signatureCustomAppearance.setDigitalSignedLabel("Digitalmente firmado por");
        signatureCustomAppearance.setReasonLabel("Razón");
        signatureCustomAppearance.setLocationLabel("Localización");
        signatureCustomAppearance.setFontFamilyName("Arial");
        signatureCustomAppearance.setFontSize(10);
        signatureCustomAppearance.setCulture(new Locale("es", "ES"));
        // signatureCustomAppearance.setCulture (Locale.ROOT);
        signatureCustomAppearance.setDateTimeFormat("yyyy.MM.dd HH:mm:ss");
        pkcs.setCustomAppearance(signatureCustomAppearance);
        // firmar el archivo PDF
        pdfSign.sign(1, true, rect, pkcs);
        // guardar el archivo PDF de salida
        pdfSign.save(outFile);
    }
```