---
title: Eliminar páginas PDF con Go
linktitle: Eliminar páginas PDF
type: docs
weight: 30
url: /es/go-cpp/delete-pages/
description: Puede eliminar páginas de su archivo PDF utilizando Aspose.PDF for Go a través de C++.
lastmod: "2026-07-04"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Eliminar páginas PDF con Aspose.PDF for Go
Abstract: Aspose.PDF for Go a través de C++ ofrece una funcionalidad eficiente para eliminar páginas de documentos PDF, lo que permite a los desarrolladores eliminar páginas no deseadas o innecesarias con facilidad. La biblioteca permite la eliminación de una o varias páginas especificando números de página o rangos, garantizando modificaciones precisas del documento. Esta característica ayuda a optimizar los archivos PDF al eliminar contenido redundante y mejorar la estructura del documento. La documentación proporciona instrucciones paso a paso y ejemplos de código para ayudar a los desarrolladores a implementar la funcionalidad de eliminación de páginas de manera eficaz en sus aplicaciones.
SoftwareApplication: go-cpp
---

Puede eliminar páginas de un archivo PDF usando **Aspose.PDF for Go a través de C++**. El siguiente fragmento de código muestra cómo manipular un documento PDF eliminando una página específica. Este método es eficiente para tareas de manipulación de documentos PDF, específicamente para eliminar páginas, guardar el documento modificado y garantizar una gestión adecuada de los recursos.

1. Abriendo un archivo PDF.
1. Eliminando una página específica con [PageDelete](https://reference.aspose.com/pdf/go-cpp/core/pagedelete/) función.
1. Guardando el documento usando [Guardar](https://reference.aspose.com/pdf/go-cpp/core/save/) método.

```go

    package main

    import "github.com/aspose-pdf/aspose-pdf-go-cpp"
    import "log"

    func main() {
      // Open(filename string) opens a PDF-document with filename
      pdf, err := asposepdf.Open("sample.pdf")
      if err != nil {
        log.Fatal(err)
      }
      // PageDelete(num int32) deletes specified page in PDF-document
      err = pdf.PageDelete(1)
      if err != nil {
        log.Fatal(err)
      }
      // Save() saves previously opened PDF-document
      err = pdf.Save()
      if err != nil {
        log.Fatal(err)
      }
      // Close() releases allocated resources for PDF-document
      defer pdf.Close()
    }
```
