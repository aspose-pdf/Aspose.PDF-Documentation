---
title: Add Signature in PDF File
type: docs
weight: 10
url: /es/java/add-signature-in-pdf/
description: Esta sección explica cómo trabajar con la firma en un archivo PDF usando la clase PdfFileSignature.
lastmod: "2021-06-05"
draft: false
---

## Añadir Firma Digital en un Archivo PDF (facades)

La clase [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSignature) permite añadir una firma en un archivo PDF. Necesitas crear un objeto de la clase [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSignature) utilizando archivos PDF de entrada y salida. También necesitas crear un objeto Rectangle en el cual deseas agregar la firma y para establecer la apariencia puedes especificar una imagen utilizando la propiedad setSignatureAppearance del objeto [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSignature).

Aspose.Pdf.Facades también proporciona diferentes tipos de firmas como PKCS#1, PKCS#7 y PKCS#7Detached.
 Para crear una firma de un tipo específico, necesitas crear un objeto de la clase particular como PKCS1, PKCS7 o PKCS7Detached usando el archivo de certificado y la contraseña.

Una vez que se crea el objeto de un tipo de firma particular, puedes usar el método sign de la clase [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSignature) para firmar el PDF y pasar el objeto de firma particular a esta clase. También puedes especificar otros atributos para este método. Finalmente, necesitas guardar el PDF firmado usando el método save de la clase [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSignature). El siguiente fragmento de código te muestra cómo agregar una firma en un archivo PDF.

```java
public static void AddPdfFileSignature() {
        PdfFileSignature pdfSign = new PdfFileSignature();
        pdfSign.bindPdf(_dataDir + "sample01.pdf");

        // Crear un rectángulo para la ubicación de la firma
        java.awt.Rectangle rect = new java.awt.Rectangle(10, 10, 300, 50);
        // Establecer la apariencia de la firma
        pdfSign.setSignatureAppearance(_dataDir + "aspose-logo.png");

        // Crear cualquiera de los tres tipos de firma
        PKCS1 signature = new PKCS1(_dataDir + "test01.pfx", "Aspose2021"); // PKCS#1

        pdfSign.sign(1, "Soy el autor del documento", "test01@aspose-pdf-demo.local", "Aspose Pdf Demo, Australia", true, rect,
                signature);
        // Guardar el archivo PDF de salida
        pdfSign.save(_dataDir + "DigitallySign.pdf");
    }
```

El siguiente ejemplo de código nos muestra la capacidad de firmar un documento con dos firmas. En nuestro ejemplo, colocamos la primera firma en la primera página y la segunda en la segunda página. Puede especificar las páginas que necesite.

```java
    public static void AddTwoSignature() {
        PdfFileSignature pdfSign = new PdfFileSignature();
        // Firmar con la 1ª firma

        pdfSign.bindPdf(_dataDir + "sample01.pdf");

        // Crear un rectángulo para la ubicación de la 1ª firma
        java.awt.Rectangle rect1 = new java.awt.Rectangle(10, 10, 300, 50);

        // Crear objeto de la 1ª firma
        PKCS1 signature1 = new PKCS1(_dataDir + "test01.pfx", "Aspose2021"); // PKCS#1

        pdfSign.sign(1, "Soy el autor del documento", "test@aspose-pdf-demo.local", "Aspose Pdf Demo, Australia", true, rect1,
                signature1);
        pdfSign.save(_dataDir + "DigitallySign.pdf");

        // Firmar con la 2ª firma

        pdfSign.bindPdf(_dataDir + "DigitallySign.pdf");

        // Crear un rectángulo para la ubicación de la 2ª firma
        java.awt.Rectangle rect2 = new java.awt.Rectangle(10, 10, 300, 50);

        // Crear objeto de la 2ª firma
        PKCS1 signature2 = new PKCS1(_dataDir + "test02.pfx", "Aspose2021"); // PKCS#1

        pdfSign.sign(2, "Soy el revisor del documento", "test02@aspose-pdf-demo.local", "Aspose Pdf Demo, Australia", true,
                rect2, signature2);

        // Guardar el archivo PDF de salida
        pdfSign.save(_dataDir + "DigitallySign.pdf");
    }
```


Para un documento con formularios o acroformulario que necesita ser firmado, vea el siguiente ejemplo.  
Necesita crear un objeto de la clase [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSignature) usando archivos PDF de entrada y salida. Utilice bindPdf para la vinculación. Cree una firma con la capacidad de agregar las propiedades necesarias. En nuestro ejemplo, son 'Reason' y 'CustomAppearance'.

```java
  public static void AddPdfFileSignatureField() {
        PdfFileSignature pdfSign = new PdfFileSignature();
        pdfSign.bindPdf(_dataDir + "sample02.pdf");

        // Crear cualquiera de los tres tipos de firma
        PKCS1 signature = new PKCS1(_dataDir + "test02.pfx", "Aspose2021");
        signature.setReason("Firmar como Autor");

        SignatureCustomAppearance sca = new SignatureCustomAppearance();
        signature.setCustomAppearance(sca);
        sca.setFontSize(6);
        sca.setFontFamilyName("Calibri");

        // PKCS#1
        pdfSign.sign("Signature1", signature);
        // Guardar archivo PDF de salida
        pdfSign.save(_dataDir + "DigitallySign.pdf");
    }
```


Si nuestro documento tiene dos campos, el algoritmo para firmarlo es similar al primer ejemplo.

```java
   public static void AddPdfFileSignatureField2() {
        PdfFileSignature pdfSign = new PdfFileSignature();
        pdfSign.bindPdf(_dataDir + "sample03.pdf");

        // Crear cualquiera de los tres tipos de firma
        PKCS1 signature1 = new PKCS1(_dataDir + "test01.pfx", "Aspose2021");
        SignatureCustomAppearance sca = new SignatureCustomAppearance();
        signature1.setCustomAppearance(sca);
        sca.setFontSize(6);
        sca.setFontFamilyName("Calibri");

        signature1.setReason("Firmar como Autor"); // PKCS#1
        pdfSign.sign("Signature1", signature1);

        // Guardar archivo PDF de salida
        pdfSign.save(_dataDir + "DigitallySign.pdf");

        pdfSign.bindPdf(_dataDir + "DigitallySign.pdf");

        // Crear cualquiera de los tres tipos de firma
        PKCS1 signature2 = new PKCS1(_dataDir + "test02.pfx", "Aspose2021");
        signature2.setReason("Firmar como Revisor"); // PKCS#1
        signature2.setCustomAppearance(sca);
        pdfSign.sign("Signature2", signature2);
        // Guardar archivo PDF de salida
        pdfSign.save(_dataDir + "DigitallySign.pdf");
    }
```