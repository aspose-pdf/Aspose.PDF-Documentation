---
title: Remove Signature from PDF File
type: docs
weight: 20
url: /net/remove-signature-from-pdf/
description: Esta sección explica cómo eliminar la firma de un archivo PDF usando la clase PdfFileSignature.
lastmod: "2021-06-05"
draft: false
---

## Remove Digital Signature from the PDF File

Cuando se ha añadido una firma a un archivo PDF, es posible eliminarla. Puedes eliminar una firma en particular, o todas las firmas en un archivo. El método más rápido para eliminar la firma también elimina el campo de firma, pero es posible simplemente eliminar la firma, manteniendo el campo de firma para que el archivo pueda ser firmado nuevamente.

El método RemoveSignature de la clase [PdfFileSignature](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature) te permite eliminar una firma de un archivo PDF. Este método toma el nombre de la firma como entrada. Ya sea especificar el nombre de la firma directamente, para eliminar todas las firmas, obtenga los nombres de las firmas utilizando el método [GetSignNames](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature/methods/getsignername).

El siguiente fragmento de código muestra cómo eliminar una firma digital del archivo PDF.

```csharp
 public static void RemoveSignature()
        {
            // Crear objeto PdfFileSignature
            PdfFileSignature pdfSign = new PdfFileSignature();
            // Abrir documento PDF
            pdfSign.BindPdf(_dataDir + "DigitallySign.pdf");
            // Obtener lista de nombres de firmas
            var sigNames = pdfSign.GetSignNames();
            // Eliminar todas las firmas del archivo PDF
            for (int index = 0; index < sigNames.Count; index++)
            {
                Console.WriteLine($"Removed {sigNames[index]}");
                pdfSign.RemoveSignature(sigNames[index]);
            }
            // Guardar archivo PDF actualizado
            pdfSign.Save(_dataDir + "RemoveSignature_out.pdf");
        }
```
### Eliminar firma pero mantener el campo de firma

Como se muestra arriba, la clase [PdfFileSignature](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature) método [RemoveSignature](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature/methods/removesignature) le permite eliminar campos de firma de archivos PDF. Al usar este método con versiones anteriores a la 9.3.0, tanto la firma como el campo de firma se eliminan. Algunos desarrolladores quieren eliminar solo la firma y mantener el campo de firma para que pueda usarse para volver a firmar el documento. Para mantener el campo de firma y solo eliminar la firma, utilice el siguiente fragmento de código.

```csharp
public static void RemoveSignatureButKeepField()
        {
            // Crear objeto PdfFileSignature
            PdfFileSignature pdfSign = new PdfFileSignature();

            // Abrir documento PDF
            pdfSign.BindPdf(_dataDir + "DigitallySign.pdf");

            pdfSign.RemoveSignature("Signature1", false);

            // Guardar archivo PDF actualizado
            pdfSign.Save(_dataDir + "RemoveSignature_out.pdf");
        }
```

El siguiente ejemplo muestra cómo eliminar todas las firmas de los campos.

```csharp
public static void RemoveSignatureButKeepField2()
        {
            // Crear objeto PdfFileSignature
            PdfFileSignature pdfSign = new PdfFileSignature();

            // Abrir documento PDF
            pdfSign.BindPdf(_dataDir + "DigitallySign.pdf");

            var sigNames = pdfSign.GetSignNames();
            foreach (var sigName in sigNames)
            {
                pdfSign.RemoveSignature(sigName, false);
            }

            // Guardar archivo PDF actualizado
            pdfSign.Save(_dataDir + "RemoveSignature_out.pdf");
        }

```