---
title: Establecer metadatos XMP de un PDF existente
type: docs
weight: 20
url: /es/net/set-xmp-metadata-of-an-existing-pdf/
description: Esta sección explica cómo establecer metadatos XMP de un PDF existente con Aspose.PDF Facades.
lastmod: "2021-06-05"
draft: false
---

Para establecer metadatos XMP en un archivo PDF, necesita crear un objeto [PdfXmpMetadata](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfxmpmetadata) y vincular el archivo PDF usando el método [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/bindpdf/index). Puedes utilizar el método [Add](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfxmpmetadata/methods/add/index) de la clase [PdfXmpMetadata](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfxmpmetadata) para agregar diferentes propiedades. Finalmente, llama al método [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save/index) de la clase [PdfXmpMetadata](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfxmpmetadata). El siguiente fragmento de código te muestra cómo agregar metadatos XMP en un archivo PDF.

```csharp
// Para ejemplos completos y archivos de datos, por favor visita https://github.com/aspose-pdf/Aspose.Pdf-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdfFacades_WorkingDocuments();

// Crear objeto PdfXmpMetadata
PdfXmpMetadata xmpMetaData = new PdfXmpMetadata();

// Vincular archivo pdf al objeto
xmpMetaData.BindPdf(dataDir+ "SetXMPMetadata.pdf");

// Agregar fecha de creación
xmpMetaData.Add(DefaultMetadataProperties.CreateDate, System.DateTime.Now.ToString());

// Cambiar fecha de metadatos
xmpMetaData[DefaultMetadataProperties.MetadataDate] = System.DateTime.Now.ToString();

// Agregar herramienta de creación
xmpMetaData.Add(DefaultMetadataProperties.CreatorTool, "Nombre de la herramienta de creación");

// Eliminar fecha de modificación
xmpMetaData.Remove(DefaultMetadataProperties.ModifyDate);

// Agregar propiedad definida por el usuario
// Paso #1: registrar prefijo de espacio de nombres y URI
xmpMetaData.RegisterNamespaceURI("customNamespace", "http:// Www.customNameSpaces.com/ns/");
// Paso #2: agregar propiedad de usuario con el prefijo
xmpMetaData.Add("customNamespace:UserPropertyName", "UserPropertyValue");

// Cambiar propiedad definida por el usuario
xmpMetaData["customNamespace:UserPropertyName"] = "UserPropertyValue2";

// Guardar metadatos xmp en el archivo pdf
xmpMetaData.Save(dataDir+ "SetXMPMetadata_out.pdf");

// Cerrar el objeto
xmpMetaData.Close();
```