---
title: Establecer Privilegios en PDF
type: docs
weight: 50
url: /net/set-privileges/
description: Este tema explica cómo establecer privilegios en un archivo PDF existente utilizando la clase PdfFileSecurity.
lastmod: "2021-06-05"
draft: false
---

## Establecer Privilegios en un Archivo PDF Existente

Para establecer los privilegios de un archivo PDF, cree un objeto [PdfFileSecurity](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesecurity) y llame al método SetPrivilege. Puede especificar los privilegios utilizando el objeto DocumentPrivilege y luego pasar este objeto al método SetPrivilege. El siguiente fragmento de código muestra cómo establecer los privilegios de un archivo PDF.

```csharp
public static void SetPrivilege1()
 {
    // Crear objeto DocumentPrivileges
    DocumentPrivilege privilege = DocumentPrivilege.ForbidAll;
    privilege.ChangeAllowLevel = 1;
    privilege.AllowPrint = true;
    privilege.AllowCopy = true;

    // Crear objeto PdfFileSecurity
    PdfFileSecurity fileSecurity = new PdfFileSecurity();
    fileSecurity.BindPdf(_dataDir + "sample.pdf");
    fileSecurity.SetPrivilege(privilege);
    fileSecurity.Save(_dataDir + "sample_privileges.pdf");
}
```

Vea el siguiente método especificando una contraseña:

```csharp
 public static void SetPrivilege2()
 {
    // Crear objeto DocumentPrivileges
    DocumentPrivilege privilege = DocumentPrivilege.ForbidAll;
    privilege.ChangeAllowLevel = 1;
    privilege.AllowPrint = true;
    privilege.AllowCopy = true;

    // Crear objeto PdfFileSecurity
    PdfFileSecurity fileSecurity = new PdfFileSecurity();
    fileSecurity.BindPdf(_dataDir + "sample.pdf");
    fileSecurity.SetPrivilege(string.Empty, "P@ssw0rd", privilege);
    fileSecurity.Save(_dataDir + "sample_privileges.pdf");
}
```

## Eliminar la Función de Derechos Extendidos del PDF

Los documentos PDF admiten la función de derechos extendidos para permitir al usuario final completar datos en campos de formulario utilizando Adobe Acrobat Reader y luego guardar una copia del formulario completado. Sin embargo, asegura que el archivo PDF no sea modificado y si se realiza alguna modificación en la estructura del PDF, la función de derechos extendidos se pierde. Al ver un documento así, se muestra un mensaje de error que indica que los derechos extendidos se eliminaron porque el documento fue modificado. Recientemente, recibimos un requisito para eliminar los derechos extendidos de un documento PDF.

Para eliminar los derechos extendidos de un archivo PDF, se ha añadido un nuevo método llamado RemoveUsageRights() a la clase PdfFileSignature. Se ha añadido otro método llamado ContainsUsageRights() para determinar si el PDF fuente contiene derechos extendidos.

{{% alert color="primary" %}}
A partir de Aspose.PDF para .NET 9.5.0, se han actualizado los nombres de los siguientes métodos. Tenga en cuenta que los métodos anteriores todavía están en la API, pero han sido marcados como obsoletos y serán eliminados. Por lo tanto, se recomienda intentar usar los métodos actualizados.

- El método IsContainSignature(.) fue renombrado a ContainsSignature(..).

- El método IsCoversWholeDocument(..) fue renombrado a CoversWholeDocument(..).{{% /alert %}}

El siguiente código muestra cómo eliminar los derechos de uso del documento:

```csharp
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdfFacades_SecuritySignatures();
string input = dataDir + "DigitallySign.pdf";
using (PdfFileSignature pdfSign = new PdfFileSignature())
{
    pdfSign.BindPdf(input);
    if (pdfSign.ContainsUsageRights())
    {
        pdfSign.RemoveUsageRights();
    }

    pdfSign.Document.Save(dataDir + "RemoveRights_out.pdf");
}
```