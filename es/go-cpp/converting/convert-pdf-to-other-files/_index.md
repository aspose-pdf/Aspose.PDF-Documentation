---
title: Convertir PDF a EPUB, TeX, Texto, XPS en Go
linktitle: Convertir PDF a otros formatos
type: docs
weight: 90
url: /es/go-cpp/convert-pdf-to-other-files/
lastmod: "2026-07-04"
description: Este tema le muestra cómo convertir un archivo PDF a otros formatos de archivo como EPUB, LaTeX, Texto, XPS, etc., usando Go.
sitemap:
    changefreq: "monthly"
    priority: 0.8
TechArticle: true
AlternativeHeadline: Herramienta Golang para convertir PDF a EPUB, TeX, Texto y XPS
Abstract: Aspose.PDF for Go via C++ ofrece capacidades potentes para convertir documentos PDF a varios formatos de archivo, incluidos DOCX, PPTX, HTML, EPUB, SVG y más. Esta funcionalidad permite a los desarrolladores extraer y reutilizar el contenido PDF de manera fluida mientras se mantiene el formato, la estructura y la calidad en los diferentes formatos de salida. La biblioteca proporciona opciones flexibles para personalizar el proceso de conversión según requisitos específicos. La documentación incluye directrices integrales y ejemplos de código para ayudar a los desarrolladores a implementar de manera eficiente la conversión de PDF a archivo dentro de sus aplicaciones.
SoftwareApplication: go-cpp
---

## Convertir PDF a EPUB

**<abbr title="Electronic Publication">EPUB</abbr>** es un estándar de libros electrónicos gratuito y abierto del International Digital Publishing Forum (IDPF). Los archivos tienen la extensión .epub.
EPUB está diseñado para contenido refluible, lo que significa que un lector EPUB puede optimizar el texto para un dispositivo de visualización específico. EPUB también soporta contenido de diseño fijo. El formato está pensado como un formato único que los editores y casas de conversión pueden usar internamente, así como para distribución y venta. Reemplaza el estándar Open eBook.

El fragmento de código Go proporcionado demuestra cómo convertir un documento PDF en un EPUB usando la biblioteca Aspose.PDF:

1. Abrir un documento PDF.
1. Convertir un archivo PDF a EPUB usando [GuardarEpub]() función.
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
      // SaveEpub(filename string) saves previously opened PDF-document as Epub-document with filename
      err = pdf.SaveEpub("sample.epub")
      if err != nil {
        log.Fatal(err)
      }
      // Close() releases allocated resources for PDF-document
      defer pdf.Close()
    }
```

{{% alert color="success" %}}
**Intenta convertir PDF a EPUB en línea**

Aspose.PDF for Go le presenta una aplicación en línea gratuita ["PDF a EPUB"](https://products.aspose.app/pdf/conversion/pdf-to-epub), donde puede intentar investigar la funcionalidad y la calidad con la que funciona.

[![Conversión de PDF a EPUB con la aplicación gratuita de Aspose.PDF](pdf_to_epub.png)](https://products.aspose.app/pdf/conversion/pdf-to-epub)
{{% /alert %}}

## Convertir PDF a TeX

**Aspose.PDF for Go** admite convertir PDF a TeX.
El formato de archivo LaTeX es un formato de archivo de texto con un marcado especial y se utiliza en un sistema de preparación de documentos basado en TeX para una composición tipográfica de alta calidad.

El fragmento de código Go proporcionado muestra cómo convertir un documento PDF a TeX usando la biblioteca Aspose.PDF:

1. Abrir un documento PDF.
1. Convertir un archivo PDF a TeX usando [SaveTeX](https://reference.aspose.com/pdf/go-cpp/convert/savetex/) función.
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
      // SaveTeX(filename string) saves previously opened PDF-document as TeX-document with filename
      err = pdf.SaveTeX("sample.tex")
      if err != nil {
        log.Fatal(err)
      }
      // Close() releases allocated resources for PDF-document
      defer pdf.Close()
    }
```

{{% alert color="success" %}}
**Intenta convertir PDF a LaTeX/TeX en línea**

Aspose.PDF for Go le presenta una aplicación en línea gratuita ["PDF a LaTeX"](https://products.aspose.app/pdf/conversion/pdf-to-tex), donde puede intentar investigar la funcionalidad y la calidad con la que funciona.

[![Aspose.PDF Conversión de PDF a LaTeX/TeX con App Gratuita](pdf_to_latex.png)](https://products.aspose.app/pdf/conversion/pdf-to-tex)
{{% /alert %}}

## Convertir PDF a TXT

El fragmento de código Go proporcionado demuestra cómo convertir un documento PDF a TXT utilizando la biblioteca Aspose.PDF:

1. Abrir un documento PDF.
1. Convertir un archivo PDF a TXT usando [GuardarTxt](https://reference.aspose.com/pdf/go-cpp/convert/savetxt/) función.
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
      // SaveTxt(filename string) saves previously opened PDF-document as Txt-document with filename
      err = pdf.SaveTxt("sample.txt")
      if err != nil {
        log.Fatal(err)
      }
      // Close() releases allocated resources for PDF-document
      defer pdf.Close()
    }
```

{{% alert color="success" %}}
**Intenta convertir PDF a Texto en línea**

Aspose.PDF for Go le presenta una aplicación en línea gratuita ["PDF a Texto"](https://products.aspose.app/pdf/conversion/pdf-to-txt), donde puede intentar investigar la funcionalidad y la calidad con la que funciona.

[![Aspose.PDF Conversión de PDF a Texto con Aplicación Gratuita](pdf_to_text.png)](https://products.aspose.app/pdf/conversion/pdf-to-txt)
{{% /alert %}}

## Convertir PDF a XPS

El tipo de archivo XPS está asociado principalmente con la Especificación de Papel XML de Microsoft Corporation. La Especificación de Papel XML (XPS), anteriormente con el nombre en código Metro y que subsume el concepto de marketing Ruta de Impresión de Próxima Generación (NGPP), es la iniciativa de Microsoft para integrar la creación y visualización de documentos en el sistema operativo Windows.

**Aspose.PDF for Go** da la posibilidad de convertir archivos PDF a <abbr title="XML Paper Specification">XPS</abbr> formato. Intentemos usar el fragmento de código presentado para convertir archivos PDF a formato XPS con Go.

El fragmento de código Go proporcionado muestra cómo convertir un documento PDF a XPS utilizando la biblioteca Aspose.PDF:

1. Abrir un documento PDF.
1. Convertir un archivo PDF a XPS usando [GuardarXps](https://reference.aspose.com/pdf/go-cpp/convert/savexps/) función.
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
      // SaveXps(filename string) saves previously opened PDF-document as Xps-document with filename
      err = pdf.SaveXps("sample.xps")
      if err != nil {
        log.Fatal(err)
      }
      // Close() releases allocated resources for PDF-document
      defer pdf.Close()
    }
```

{{% alert color="success" %}}
**Intenta convertir PDF a XPS en línea**

Aspose.PDF for Go le presenta una aplicación en línea gratuita ["PDF a XPS"](https://products.aspose.app/pdf/conversion/pdf-to-xps), donde puede intentar investigar la funcionalidad y la calidad con la que funciona.

[![Aspose.PDF Conversión de PDF a XPS con aplicación gratuita](pdf_to_xps.png)](https://products.aspose.app/pdf/conversion/pdf-to-xps)
{{% /alert %}}

## Convertir PDF a PDF en escala de grises

El fragmento de código Go proporcionado muestra cómo convertir la primera página de un documento PDF a un PDF en escala de grises usando la biblioteca Aspose.PDF:

1. Abrir un documento PDF.
1. Convertir una página PDF a PDF en escala de grises usando [Página en escala de grises](https://reference.aspose.com/pdf/go-cpp/organize/pagegrayscale/) función.
1. Cierre el documento PDF y libere los recursos asignados.

Este ejemplo convierte una página específica de su PDF a escala de grises:

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
      // PageGrayscale(num int32) converts page to black and white
      err = pdf.PageGrayscale(1)
      if err != nil {
        log.Fatal(err)
      }
      // SaveAs(filename string) saves previously opened PDF-document with new filename
      err = pdf.SaveAs("sample_page1_Grayscale.pdf")
      if err != nil {
        log.Fatal(err)
      }
      // Close() releases allocated resources for PDF-document
      defer pdf.Close()
    }
```

Este ejemplo convertirá todo el documento PDF a escala de grises:

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
      // Grayscale() converts PDF-document to black and white
      err = pdf.Grayscale()
      if err != nil {
        log.Fatal(err)
      }
      // SaveAs(filename string) saves previously opened PDF-document with new filename
      err = pdf.SaveAs("sample_Grayscale.pdf")
      if err != nil {
        log.Fatal(err)
      }
      // Close() releases allocated resources for PDF-document
      defer pdf.Close()
    }
```