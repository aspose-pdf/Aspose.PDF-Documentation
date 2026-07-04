---
title: Extraer texto de PDF usando Go
linktitle: Extraer texto de PDF
type: docs
weight: 30
url: /es/go-cpp/extract-text-from-pdf/
description: Este artículo describe varias formas de extraer texto de documentos PDF usando Aspose.PDF for Go.
lastmod: "2026-07-04"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Extraer texto con Aspose.PDF for Go
Abstract: Aspose.PDF for Go via C++ proporciona una forma potente y eficiente de extraer texto de documentos PDF. La biblioteca admite múltiples técnicas de extracción, lo que permite a los usuarios recuperar texto de documentos completos, páginas específicas o áreas predefinidas dentro de un PDF.
SoftwareApplication: go-cpp
---

## Extraer texto de documento PDF

Extraer texto del documento PDF es una tarea muy común y útil. Los PDFs a menudo contienen información crítica que necesita ser accedida, analizada o procesada para diversos propósitos. Extraer texto permite una reutilización más fácil en bases de datos, informes u otros documentos.

Extraer texto hace que el contenido del PDF sea buscable, lo que permite a los usuarios localizar información específica rápidamente sin revisar manualmente todo el documento.

En caso de que desees extraer texto del documento PDF, puedes usar [ExtractText](https://reference.aspose.com/pdf/go-cpp/core/extracttext/) función.
Por favor, revisa el siguiente fragmento de código para extraer texto de un archivo PDF usando Go.

1. Abra un documento PDF con el nombre de archivo proporcionado.
1. [ExtractText](https://reference.aspose.com/pdf/go-cpp/core/extracttext/) extrae el contenido de texto del documento PDF.
1. Imprima el texto extraído en la consola.

```go

    package main

    import "github.com/aspose-pdf/aspose-pdf-go-cpp"
    import "log"
    import "fmt"

    func main() {
        // Open(filename string) opens a PDF-document with filename
        pdf, err := asposepdf.Open("sample.pdf")
        if err != nil {
            log.Fatal(err)

        }
        // ExtractText() returns PDF-document contents as plain text
        txt, err := pdf.ExtractText()
        if err != nil {
            log.Fatal(err)
        }
        // Print
        fmt.Println("Extracted text:\n", txt)
        // Close() releases allocated resources for PDF-document
        defer pdf.Close()
    }
```