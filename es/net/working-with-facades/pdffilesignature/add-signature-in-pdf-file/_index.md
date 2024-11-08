---
title: Agregar Firma en Archivo PDF
type: docs
weight: 10
url: /es/net/add-signature-in-pdf/
description: Esta sección explica cómo agregar firma a un archivo PDF usando la clase PdfFileSignature.
lastmod: "2021-06-05"
draft: false
---

## Agregar Firma Digital en un Archivo PDF

[PdfFileSignature](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature) class permite agregar firma en un archivo PDF. Necesitas crear un objeto de la clase [PdfFileSignature](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature) usando archivos PDF de entrada y salida. También necesitas crear un objeto [Rectangle](https://reference.aspose.com/pdf/net/aspose.pdf/rectangle) en el cual deseas agregar la firma y para establecer la apariencia puedes especificar una imagen usando la propiedad [SignatureAppearance](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature/properties/signatureappearance) del objeto [PdfFileSignature](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature). Aspose.Pdf.Facades también proporciona diferentes tipos de firmas como PKCS#1, PKCS#7 y PKCS#7Detached. Para crear una firma de un tipo específico, necesitas crear un objeto de la clase particular como **PKCS1**, **PKCS7** o **PKCS7Detached** usando el archivo de certificado y la contraseña.

Una vez que se crea el objeto de un tipo de firma particular, puedes usar el método [Sign](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature/methods/sign/index) de la clase [PdfFileSignature](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature) para firmar el PDF y pasar el objeto de firma particular a esta clase. Puedes especificar otros atributos para este método. Finalmente, necesitas guardar el PDF firmado usando el método [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save/index) de la clase [PdfFileSignature](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature). El siguiente fragmento de código te muestra cómo agregar una firma en un archivo PDF.

```csharp
public static void AddPdfFileSignature()
        {
            PdfFileSignature pdfSign = new PdfFileSignature();
            pdfSign.BindPdf(_dataDir + "sample01.pdf");

            // Crear un rectángulo para la ubicación de la firma
            System.Drawing.Rectangle rect = new System.Drawing.Rectangle(10, 10, 300, 50);
            // Establecer apariencia de la firma
            pdfSign.SignatureAppearance = _dataDir + "aspose-logo.png";

            // Crear cualquiera de los tres tipos de firma
            PKCS1 signature = new PKCS1(_dataDir + "test01.pfx", "Aspose2021"); // PKCS#1

            pdfSign.Sign(1, "Soy el autor del documento", "test01@aspose-pdf-demo.local", "Aspose Pdf Demo, Australia", true, rect, signature);
            // Guardar el archivo PDF de salida
            pdfSign.Save(_dataDir + "DigitallySign.pdf");
        }
```
El siguiente ejemplo de código nos muestra la capacidad de firmar un documento con dos firmas. En nuestro ejemplo, colocamos la primera firma en la primera página y la segunda en la segunda página. Puedes especificar las páginas que necesitas.

```csharp
 public static void AddTwoSignature()
        {
            PdfFileSignature pdfSign = new PdfFileSignature();

            // Firmar con la 1ª firma

            pdfSign.BindPdf(_dataDir + "sample01.pdf");

            // Crear un rectángulo para la ubicación de la 1ª firma
            System.Drawing.Rectangle rect1 = new System.Drawing.Rectangle(10, 10, 300, 50);

            // Crear el objeto de la 1ª firma
            PKCS1 signature1 = new PKCS1(_dataDir + "test01.pfx", "Aspose2021"); // PKCS#1

            pdfSign.Sign(1, "Soy el autor del documento", "test@aspose-pdf-demo.local", "Aspose Pdf Demo, Australia", true, rect1, signature1);
            pdfSign.Save(_dataDir + "DigitallySign.pdf");


            // Firmar con la 2ª firma

            pdfSign.BindPdf(_dataDir + "DigitallySign.pdf");

            // Crear un rectángulo para la ubicación de la 2ª firma
            System.Drawing.Rectangle rect2 = new System.Drawing.Rectangle(10, 10, 300, 50);

            // Crear el objeto de la 2ª firma
            PKCS1 signature2 = new PKCS1(_dataDir + "test02.pfx", "Aspose2021"); // PKCS#1

            pdfSign.Sign(2, "Soy el revisor del documento", "test02@aspose-pdf-demo.local", "Aspose Pdf Demo, Australia", true, rect2, signature2);

            // Guardar el archivo PDF de salida
            pdfSign.Save(_dataDir + "DigitallySign.pdf");
        }
```

For a document with forms or acroforms that needs to be signed, see the following example. You need to create an object of [PdfFileSignature](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature) class using input and output PDF files. Use [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffilesignature/bindpdf/methods/1) for binding. Create a signature with the ability to add the required properties. In our example they are 'Reason' and 'CustomAppearance'.

Para un documento con formularios o acroformularios que necesita ser firmado, vea el siguiente ejemplo. Necesita crear un objeto de la clase [PdfFileSignature](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature) utilizando archivos PDF de entrada y salida. Use [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffilesignature/bindpdf/methods/1) para la vinculación. Cree una firma con la capacidad de agregar las propiedades requeridas. En nuestro ejemplo, son 'Reason' y 'CustomAppearance'.

```csharp
 public static void AddPdfFileSignatureField()
        {
            PdfFileSignature pdfSign = new PdfFileSignature();
            pdfSign.BindPdf(_dataDir + "sample02.pdf");

            // Crear cualquiera de los tres tipos de firma
            PKCS1 signature = new PKCS1(_dataDir + "test02.pfx", "Aspose2021")
            {
                Reason = "Firmar como Autor",
                CustomAppearance = new SignatureCustomAppearance
                {
                    FontSize = 6,
                    FontFamilyName = "Calibri"
                }
            }; // PKCS#1
            pdfSign.Sign("Signature1", signature);
            // Guardar el archivo PDF de salida
            pdfSign.Save(_dataDir + "DigitallySign.pdf");
        }
```

Si nuestro documento tiene dos campos, el algoritmo para firmarlo es similar al primer ejemplo.

```csharp
public static void AddPdfFileSignatureField2()
        {
            PdfFileSignature pdfSign = new PdfFileSignature();
            pdfSign.BindPdf(_dataDir + "sample03.pdf");

            // Crear cualquiera de los tres tipos de firma
            PKCS1 signature1 = new PKCS1(_dataDir + "test01.pfx", "Aspose2021")
            {
                Reason = "Firmar como Autor",
                CustomAppearance = new SignatureCustomAppearance
                {
                    FontSize = 6
                }
            }; // PKCS#1
            pdfSign.Sign("Signature1", signature1);
            // Guardar el archivo PDF de salida
            pdfSign.Save(_dataDir + "DigitallySign.pdf");

            pdfSign.BindPdf(_dataDir + "DigitallySign.pdf");

            // Crear cualquiera de los tres tipos de firma
            PKCS1 signature2 = new PKCS1(_dataDir + "test02.pfx", "Aspose2021")
            {
                Reason = "Firmar como Revisor",
                CustomAppearance = new SignatureCustomAppearance
                {
                    FontSize = 6
                }
            }; // PKCS#1
            pdfSign.Sign("Signature2", signature2);
            // Guardar el archivo PDF de salida
            pdfSign.Save(_dataDir + "DigitallySign.pdf");
        }
```