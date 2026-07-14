---
title: Convertir PDF a documentos Word en Go
linktitle: Convertir PDF a Word
type: docs
weight: 10
url: /es/go-cpp/convert-pdf-to-doc/
lastmod: "2026-07-04"
description: Aprenda cómo escribir código Go para la conversión de PDF a DOC(DOCX).
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Herramienta para convertir PDF a Word con Aspose.PDF para Go
Abstract: Aspose.PDF for Go a través de C++ permite la conversión fluida de documentos PDF al formato DOC mientras preserva el texto original, las imágenes, las tablas y la estructura general del documento. Esta función permite a los desarrolladores transformar PDFs estáticos en archivos Word editables para su posterior modificación y procesamiento. La biblioteca ofrece varias opciones de personalización para controlar la salida de la conversión, garantizando alta fidelidad y precisión. La documentación incluye instrucciones detalladas y código de ejemplo para ayudar a los desarrolladores a implementar de manera eficiente la conversión de PDF a DOC en sus aplicaciones.
SoftwareApplication: go-cpp
---

Para editar el contenido de un archivo PDF en Microsoft Word u otros procesadores de texto que soportan los formatos DOC y DOCX. Los archivos PDF son editables, pero los archivos DOC y DOCX son más flexibles y personalizables.

## Convertir PDF a DOC

El fragmento de código Go proporcionado demuestra cómo convertir un documento PDF a DOC utilizando la biblioteca Aspose.PDF:

1. Abrir un documento PDF.
1. Convertir un archivo PDF a DOC usando [SaveDoc](https://reference.aspose.com/pdf/go-cpp/convert/savedoc/) función.
1. Cierre el documento PDF y libere los recursos asignados.

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
      // SaveDoc(filename string) saves previously opened PDF-document as Doc-document with filename
      err = pdf.SaveDoc("sample.doc")
      if err != nil {
        log.Fatal(err)
      }
      // Close() releases allocated resources for PDF-document
      defer pdf.Close()
    }
```

{{% alert color="success" %}}
**Intenta convertir PDF a DOC en línea**

Aspose.PDF for Go te presenta una aplicación gratuita en línea [“PDF a DOC”](https://products.aspose.app/pdf/conversion/pdf-to-doc), donde puede intentar investigar la funcionalidad y la calidad con la que funciona.

[![Convertir PDF a DOC](pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-doc) 
{{% /alert %}}

## Convertir PDF a DOCX

Aspose.PDF for Go API le permite leer y convertir documentos PDF a DOCX. DOCX es un formato bien conocido para documentos de Microsoft Word cuya estructura cambió de binario puro a una combinación de archivos XML y binarios. Los archivos DOCX pueden abrirse con Word 2007 y versiones posteriores, pero no con las versiones anteriores de MS Word que solo admiten extensiones de archivo DOC.

El fragmento de código Go proporcionado muestra cómo convertir un documento PDF a DOCX usando la biblioteca Aspose.PDF:

1. Abrir un documento PDF.
1. Convertir un archivo PDF a DOCX usando [SaveDocX](https://reference.aspose.com/pdf/go-cpp/convert/savedocx/) función.
1. Cierre el documento PDF y libere los recursos asignados.

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
      // SaveDocX(filename string) saves previously opened PDF-document as DocX-document with filename
      err = pdf.SaveDocX("sample.docx")
      if err != nil {
        log.Fatal(err)
      }
      // Close() releases allocated resources for PDF-document
      defer pdf.Close()
    }
```

{{% alert color="success" %}}
**Intenta convertir PDF a DOCX en línea**

Aspose.PDF for Go te presenta una aplicación gratuita en línea [\"PDF a Word\"](https://products.aspose.app/pdf/conversion/pdf-to-docx), donde puede intentar investigar la funcionalidad y la calidad con la que funciona.

[![Aspose.PDF Conversión PDF a Word Aplicación gratuita](pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-docx)

{{% /alert %}}