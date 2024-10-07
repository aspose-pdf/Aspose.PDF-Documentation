---
title: Trabajando con Firma en Archivo PDF
type: docs
weight: 40
url: /net/working-with-signature-in-a-pdf-file/
description: Esta sección explica cómo extraer información de la firma, extraer imagen de la firma, cambiar el idioma, etc. usando la clase PdfFileSignature.
lastmod: "2021-06-05"
draft: false
---

## Cómo Extraer Información de la Firma

Aspose.PDF para .NET admite la función de firmar digitalmente archivos PDF usando la clase PdfFileSignature. Actualmente, también es posible determinar la validez de un certificado, pero no podemos extraer el certificado completo. La información que se puede extraer es la clave pública, la huella digital y el emisor, etc.

Para extraer información de la firma, hemos introducido el método ExtractCertificate(..) en la clase PdfFileSignature. Por favor, eche un vistazo al siguiente fragmento de código que demuestra los pasos para extraer el certificado del objeto PdfFileSignature:

```csharp
public static void ExtractSignatureInfo()
        {
            string input = _dataDir + "DigitallySign.pdf";
            string certificateFileName = "extracted_cert.pfx";
            using (PdfFileSignature pdfFileSignature = new PdfFileSignature())
            {
                pdfFileSignature.BindPdf(input);
                var sigNames = pdfFileSignature.GetSignNames();
                if (sigNames.Count > 0)
                {
                    string sigName = sigNames[0];
                    if (!string.IsNullOrEmpty(sigName))
                    {
                        Stream cerStream = pdfFileSignature.ExtractCertificate(sigName);
                        if (cerStream != null)
                        {
                            using (cerStream)
                            {
                                using (FileStream fs = new FileStream(_dataDir + certificateFileName, FileMode.CreateNew))
                                {
                                    cerStream.CopyTo(fs);
                                }
                            }
                        }
                    }
                }
            }
        }
```

## Extrayendo Imagen del Campo de Firma (PdfFileSignature)

Aspose.PDF para .NET admite la función de firmar digitalmente los archivos PDF utilizando la clase PdfFileSignature y, al firmar el documento, también puedes establecer una imagen para SignatureAppearance. Ahora esta API también proporciona la capacidad de extraer la información de la firma, así como la imagen asociada con el campo de firma.

Para extraer la información de la firma, hemos introducido el método ExtractImage(..) en la clase PdfFileSignature. Por favor, echa un vistazo al siguiente fragmento de código que demuestra los pasos para extraer la imagen del objeto PdfFileSignature:

```csharp
public static void ExtractSignatureImage()
        {
            using (PdfFileSignature signature = new PdfFileSignature())
            {
                signature.BindPdf(_dataDir + "DigitallySign.pdf");

                if (signature.ContainsSignature())
                {
                    foreach (string sigName in signature.GetSignNames())
                    {
                        string outFile = _dataDir + "ExtractImages_out.jpg";
                        using (Stream imageStream = signature.ExtractImage(sigName))
                        {
                            if (imageStream != null)
                            {
                                imageStream.Position = 0;
                                using (FileStream fs = new FileStream(outFile, FileMode.OpenOrCreate))
                                {
                                    imageStream.CopyTo(fs);
                                }
                            }
                        }
                    }
                }
            }
        }
```

## Suprimir Ubicación y Razón

La funcionalidad de Aspose.PDF permite una configuración flexible para la instancia de firma digital. La clase [PdfFileSignature](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature) proporciona la capacidad de firmar archivos PDF. La implementación del método Sign permite firmar el PDF y pasar el objeto de firma particular a esta clase. El método Sign contiene un conjunto de atributos para la personalización de la firma digital de salida. En caso de que necesite suprimir algunos atributos de texto de la firma resultante, puede dejarlos vacíos. El siguiente fragmento de código demuestra cómo suprimir las dos filas de Ubicación y Razón del bloque de firma:

```csharp
public static void SupressLocationReason()
        {
            PdfFileSignature pdfSign = new PdfFileSignature();
            pdfSign.BindPdf(_dataDir + "sample01.pdf");

            // Create a rectangle for signature location
            System.Drawing.Rectangle rect = new System.Drawing.Rectangle(10, 10, 300, 50);
            // Set signature appearance
            pdfSign.SignatureAppearance = _dataDir + "aspose-logo.png";

            // Create any of the three signature types
            PKCS1 signature = new PKCS1(_dataDir + "test01.pfx", "Aspose2021"); // PKCS#1

            pdfSign.Sign(1, string.Empty, "test01@aspose-pdf-demo.local", string.Empty, true, rect, signature);
            // Save output PDF file
            pdfSign.Save(_dataDir + "DigitallySign.pdf");
        }
```

## Funciones de Personalización para Firmas Digitales

Aspose.PDF para .NET permite funciones de personalización para una firma digital. El método Sign de la clase [SignatureCustomAppearance](https://reference.aspose.com/pdf/net/aspose.pdf.forms/signaturecustomappearance) se implementa con 6 sobrecargas para su uso cómodo. Por ejemplo, puede configurar el resultado de la firma solo mediante la instancia de la clase SignatureCustomAppearance y los valores de sus propiedades. El siguiente fragmento de código demuestra cómo ocultar la leyenda "Firmado digitalmente por" de la firma digital de salida de su PDF.

```csharp
  public static void CustomizationFeaturesForDigitalSign()
        {
            PdfFileSignature pdfSign = new PdfFileSignature();
            pdfSign.BindPdf(_dataDir + "sample01.pdf");

            // Crear un rectángulo para la ubicación de la firma
            System.Drawing.Rectangle rect = new System.Drawing.Rectangle(10, 10, 300, 50);

            // Crear cualquiera de los tres tipos de firma
            PKCS1 signature = new PKCS1(_dataDir + "test01.pfx", "Aspose2021"); // PKCS#1

            SignatureCustomAppearance signatureCustomAppearance = new SignatureCustomAppearance
            {
                FontSize = 6,
                FontFamilyName = "Times New Roman",
                DigitalSignedLabel = "Firmado por:"
            };
            signature.CustomAppearance = signatureCustomAppearance;

            pdfSign.Sign(1, true, rect, signature);
            // Guardar archivo PDF de salida
            pdfSign.Save(_dataDir + "DigitallySign.pdf");
        }
```

## Cambiar Idioma En Texto De Firma Digital

Usando Aspose.PDF para la API .NET, puedes firmar un archivo PDF utilizando cualquiera de los siguientes tres tipos de firmas:

- PKCS#1
- PKCS#7
- PKCS#7

Cada una de las firmas proporcionadas contiene un conjunto de propiedades de configuración implementadas para tu conveniencia (localización, formato de fecha y hora, familia de fuentes, etc.). La clase [SignatureCustomAppearance](https://reference.aspose.com/pdf/net/aspose.pdf.forms/signaturecustomappearance) proporciona la funcionalidad correspondiente. El siguiente fragmento de código demuestra cómo cambiar el idioma en el texto de firma digital:

```csharp
     public static void ChangeLanguageInDigitalSignText()
        {
            string inFile = _dataDir + "sample01.pdf";
            string outFile = _dataDir + "DigitallySign.pdf";

            using (Aspose.Pdf.Facades.PdfFileSignature pdfSign = new Aspose.Pdf.Facades.PdfFileSignature())
            {
                pdfSign.BindPdf(inFile);
                //crear un rectángulo para la ubicación de la firma
                System.Drawing.Rectangle rect = new System.Drawing.Rectangle(310, 45, 200, 50);

                //crear cualquiera de los tres tipos de firma
                PKCS7 pkcs = new PKCS7(_dataDir + "test01.pfx", "Aspose2021")
                {
                    Reason = "Pruebas Firma",
                    ContactInfo = "Contacto Pruebas",
                    Location = "Población (Provincia)",
                    Date = DateTime.Now
                };
                SignatureCustomAppearance signatureCustomAppearance = new SignatureCustomAppearance
                {
                    DateSignedAtLabel = "Fecha",
                    DigitalSignedLabel = "Digitalmente firmado por",
                    ReasonLabel = "Razón",
                    LocationLabel = "Localización",
                    FontFamilyName = "Arial",
                    FontSize = 10d,
                    Culture = System.Globalization.CultureInfo.InvariantCulture,
                    DateTimeFormat = "yyyy.MM.dd HH:mm:ss"
                };
                pkcs.CustomAppearance = signatureCustomAppearance;
                // firmar el archivo PDF
                pdfSign.Sign(1, true, rect, pkcs);
                //guardar el archivo PDF de salida
                pdfSign.Save(outFile);
            }
        }
```