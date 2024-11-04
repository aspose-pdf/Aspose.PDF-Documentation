---
title: Remove Signature from PDF File
type: docs
weight: 20
url: /java/remove-signature-from-pdf/
description: Esta sección explica cómo trabajar con la Firma en un archivo PDF usando la clase PdfFileSignature.
lastmod: "2021-06-05"
draft: false
---

## Eliminar la Firma Digital del Archivo PDF

Cuando se ha añadido una firma a un archivo PDF, es posible eliminarla. Puedes eliminar una firma en particular o todas las firmas en un archivo. El método más rápido para eliminar la firma también elimina el campo de la firma, pero es posible simplemente eliminar la firma, manteniendo el campo de la firma para que el archivo pueda ser firmado nuevamente.

El método RemoveSignature de la clase [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSignature) te permite eliminar una firma de un archivo PDF.
 Este método toma el nombre de la firma como entrada. Puede especificar el nombre de la firma directamente, para eliminar todas las firmas, obtenga los nombres de las firmas usando el método [getSignNames](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSignature#getSignNames--).

El siguiente fragmento de código muestra cómo eliminar la firma digital del archivo PDF.

```java
 public static void RemoveSignature() {
        // Crear objeto PdfFileSignature
        PdfFileSignature pdfSign = new PdfFileSignature();
        // Abrir documento PDF
        pdfSign.bindPdf(_dataDir + "DigitallySign.pdf");
        // Obtener lista de nombres de firmas
        List<String> sigNames = pdfSign.getSignNames();
        // Eliminar todas las firmas del archivo PDF
        for (int index = 0; index < sigNames.size(); index++) {
            System.out.println("Removed " + sigNames.get(index));
            pdfSign.removeSignature(sigNames.get(index));
        }
        // Guardar archivo PDF actualizado
        pdfSign.save(_dataDir + "RemoveSignature_out.pdf");
    }
```

### Eliminar la Firma pero Mantener el Campo de Firma

Como se muestra arriba, el método [removeSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSignature#removeSignature-java.lang.String-) de la clase [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSignature) permite eliminar campos de firma de archivos PDF. Al usar este método con versiones anteriores a la 9.3.0, tanto la firma como el campo de firma se eliminan. Algunos desarrolladores desean eliminar solo la firma y mantener el campo de firma para que se pueda volver a firmar el documento. Para mantener el campo de firma y solo eliminar la firma, por favor use el siguiente fragmento de código.

```java
 public static void RemoveSignatureButKeepField() {
        // Crear objeto PdfFileSignature
        PdfFileSignature pdfSign = new PdfFileSignature();

        // Abrir documento PDF
        pdfSign.bindPdf(_dataDir + "DigitallySign.pdf");

        pdfSign.removeSignature("Signature1", false);

        // Guardar archivo PDF actualizado
        pdfSign.save(_dataDir + "RemoveSignature_out.pdf");
    }
```


El siguiente ejemplo muestra cómo eliminar todas las firmas de los campos.

```java
public static void RemoveSignatureButKeepField2() {
        // Crear objeto PdfFileSignature
        PdfFileSignature pdfSign = new PdfFileSignature();

        // Abrir documento PDF
        pdfSign.bindPdf(_dataDir + "DigitallySign.pdf");

        List<String> sigNames = pdfSign.getSignNames();
        for (String sigName : sigNames) {
            pdfSign.removeSignature(sigName, false);
        }

        // Guardar archivo PDF actualizado
        pdfSign.save(_dataDir + "RemoveSignature_out.pdf");
    }
```