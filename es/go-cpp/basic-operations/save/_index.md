---
title: Guardar documento PDF programáticamente
linktitle: Guardar PDF
type: docs
weight: 30
url: /es/go-cpp/save-pdf-document/
description: Aprenda cómo guardar un archivo PDF con Aspose.PDF for Go a través de C++.
lastmod: "2026-07-04"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Guardar documento PDF con Aspose.PDF for Go a través de C++
Abstract: Aspose.PDF for Go a través de C++ ofrece una funcionalidad integral para guardar documentos PDF en varios formatos y ubicaciones con alta eficiencia y flexibilidad. La biblioteca permite a los desarrolladores guardar PDFs en sistemas de archivos, flujos de memoria, o exportarlos en formatos alternativos como DOCX, XLSX e imágenes. Proporciona opciones para personalizar los parámetros de guardado, optimizar el tamaño del archivo y garantizar la integridad de los datos. La documentación incluye instrucciones detalladas y ejemplos de código para ayudar a los desarrolladores a implementar de manera eficiente las capacidades de guardado de PDF en sus aplicaciones.
SoftwareApplication: go-cpp
---

## Guardar documento PDF en el sistema de archivos

El ejemplo demuestra el [New](https://reference.aspose.com/pdf/go-cpp/core/new/) método para crear un nuevo documento PDF, que es una característica fundamental para generar documentos de forma dinámica, como informes o facturas.

El código es sencillo y puede servir como plantilla para funciones más avanzadas como agregar texto, imágenes o anotaciones al PDF.

Este ejemplo demuestra el uso sencillo de la biblioteca Aspose.PDF Go, mostrando su potencial para crear, modificar y guardar documentos.

```go

    package main

    import "github.com/aspose-pdf/aspose-pdf-go-cpp"
    import "log"

    func main() {
        // New creates a new PDF-document
        pdf, err := asposepdf.New()
        if err != nil {
            log.Fatal(err)
        }
        // SaveAs(filename string) saves previously opened PDF-document with new filename
        err = pdf.SaveAs("sample_New_SaveAs.pdf")
        if err != nil {
            log.Fatal(err)
        }
        // Close() releases allocated resources for PDF-document
        defer pdf.Close()
    }
```
