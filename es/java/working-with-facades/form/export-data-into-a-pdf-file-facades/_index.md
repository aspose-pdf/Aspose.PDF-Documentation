---
title: Exportar Datos a XML desde un Archivo PDF (Facades)
type: docs
weight: 20
url: es/java/export-data-into-a-pdf-file-facades/
description: Esta sección explica cómo exportar Datos a XML desde un Archivo PDF con Aspose.PDF Facades utilizando la Clase Form.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

La clase [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Form) te permite exportar datos a un archivo XML desde el archivo PDF usando el método exportXml. Para exportar datos a XML, necesitas crear un objeto de la clase [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Form), abrir el formulario PDF de origen usando el método bindPDF y luego llamar al método exportXml usando el objeto OutputStream. Finalmente, puedes cerrar el objeto OutputStream y liberar el objeto Form. El siguiente fragmento de código te muestra cómo exportar datos a un archivo XML.

{{< gist "aspose-pdf" "474c352a71ac9477aa0d604fd32e1c6a" "Examples-src-main-java-com-aspose-pdf-examples-facades-Forms-ExportDataToXMLFromAPDFFile-.java" >}}