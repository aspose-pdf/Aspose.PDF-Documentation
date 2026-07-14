---
title: Convertir PDF a formatos de imagen en Go
linktitle: Convertir PDF a imágenes
type: docs
weight: 70
url: /es/go-cpp/convert-pdf-to-images-format/
lastmod: "2026-07-04"
description: Este tema le muestra cómo usar Aspose.PDF for Go para convertir PDF a varios formatos de imagen, p. ej. TIFF, BMP, JPEG, PNG, SVG, con unas pocas líneas de código.
sitemap:
    changefreq: "monthly"
    priority: 0.5
TechArticle: true
AlternativeHeadline: Herramienta para convertir PDF a formato de imágenes con Aspose.PDF for Go
Abstract: Aspose.PDF for Go via C++ permite una conversión fluida de documentos PDF a varios formatos de imagen, incluidos JPEG, PNG, BMP y TIFF. Esta función permite a los desarrolladores generar imágenes de alta calidad mientras preservan el contenido, el diseño y la resolución del documento original. La biblioteca ofrece opciones flexibles para la configuración de salida, como resolución, calidad de imagen y profundidad de color. La documentación proporciona instrucciones paso a paso y ejemplos de código para ayudar a los desarrolladores a integrar de manera eficiente la conversión de PDF a imagen en sus aplicaciones.
SoftwareApplication: go-cpp
---

## Ir Convertir PDF a Imagen

En este artículo, le mostraremos las opciones para convertir PDF a formatos de imagen.

Los documentos escaneados previamente a menudo se guardan en el formato de archivo PDF. Sin embargo, ¿necesita editarlos en un editor gráfico o enviarlos posteriormente en formato de imagen? Tenemos una herramienta universal para usted que convierte PDF a imágenes usando **Aspose.PDF for Go via C++**.
La tarea más común es cuando necesitas guardar un documento PDF completo o algunas páginas específicas de un documento como un conjunto de imágenes. **Aspose.PDF for Go via C++** permite convertir PDF a formatos JPG y PNG para simplificar los pasos necesarios para obtener tus imágenes de un archivo PDF específico.

**Aspose.PDF for Go via C++** soporta la conversión de PDF a varios formatos de imagen. Por favor, revisa la sección [Formatos de archivo compatibles con Aspose.PDF](https://docs.aspose.com/pdf/go-cpp/supported-file-formats/).

## Convertir PDF a JPEG

El fragmento de código Go proporcionado demuestra cómo convertir la primera página de un documento PDF en una imagen JPEG utilizando la biblioteca Aspose.PDF:

1. Abre un documento PDF.
1. Convertir una página a JPEG usando [PageToJpg](https://reference.aspose.com/pdf/go-cpp/convert/pagetojpg/) función.
1. Cierre el documento PDF y libere cualquier recurso asignado.

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
      // PageToJpg(num int32, resolution_dpi int32, filename string) saves the specified page as Jpg-image file
      err = pdf.PageToJpg(1, 100, "sample_page1.jpg")
      if err != nil {
        log.Fatal(err)
      }
      // Close() releases allocated resources for PDF-document
      defer pdf.Close()
    }
```

{{% alert color="success" %}}
**Intenta convertir PDF a JPEG en línea**

Aspose.PDF for Go le presenta una aplicación gratuita en línea ["PDF a JPEG"](https://products.aspose.app/pdf/conversion/pdf-to-jpg), donde puedes intentar investigar la funcionalidad y la calidad con la que funciona.

[![Conversión de PDF a JPEG con la aplicación gratuita Aspose.PDF](pdf_to_jpg.png)](https://products.aspose.app/pdf/conversion/pdf-to-jpg)
{{% /alert %}}

## Convertir PDF a TIFF

El fragmento de código Go proporcionado muestra cómo convertir la primera página de un documento PDF en una imagen TIFF utilizando la biblioteca Aspose.PDF:

1. Abre un documento PDF.
1. Convertir una página a TIFF usando [PageToTiff](https://reference.aspose.com/pdf/go-cpp/convert/pagetotiff/) función.
1. Cierre el documento PDF y libere cualquier recurso asignado.

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
      // PageToTiff(num int32, resolution_dpi int32, filename string) saves the specified page as Tiff-image file
      err = pdf.PageToTiff(1, 100, "sample_page1.tiff")
      if err != nil {
        log.Fatal(err)
      }
      // Close() releases allocated resources for PDF-document
      defer pdf.Close()
    }
```

{{% alert color="success" %}}
**Intenta convertir PDF a TIFF en línea**

Aspose.PDF for Go le presenta una aplicación gratuita en línea ["PDF a TIFF"](https://products.aspose.app/pdf/conversion/pdf-to-tiff), donde puedes intentar investigar la funcionalidad y la calidad con la que funciona.

[![Conversión PDF a TIFF con Aspose.PDF y aplicación gratuita](pdf_to_tiff.png)](https://products.aspose.app/pdf/conversion/pdf-to-tiff)
{{% /alert %}}

## Convertir PDF a PNG

El fragmento de código Go proporcionado demuestra cómo convertir la primera página de un documento PDF en una imagen PNG usando la biblioteca Aspose.PDF:

1. Abre un documento PDF.
1. Convertir una página a PNG usando [PageToPng](https://reference.aspose.com/pdf/go-cpp/convert/pagetopng/) función.
1. Cierre el documento PDF y libere cualquier recurso asignado.

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
      // PageToPng(num int32, resolution_dpi int32, filename string) saves the specified page as Png-image file
      err = pdf.PageToPng(1, 100, "sample_page1.png")
      if err != nil {
        log.Fatal(err)
      }
      // Close() releases allocated resources for PDF-document
      defer pdf.Close()
    }
```

{{% alert color="success" %}}
**Intenta convertir PDF a PNG en línea**

Como ejemplo de cómo funcionan nuestras aplicaciones gratuitas, por favor revise la siguiente característica.

Aspose.PDF for Go le presenta una aplicación gratuita en línea ["PDF a PNG"](https://products.aspose.app/pdf/conversion/pdf-to-png), donde puedes intentar investigar la funcionalidad y la calidad con la que funciona.

[![Cómo convertir PDF a PNG usando una aplicación gratuita](pdf_to_png.png)](https://products.aspose.app/pdf/conversion/pdf-to-png)
{{% /alert %}}

**Scalable Vector Graphics (SVG)** es una familia de especificaciones de un formato de archivo basado en XML para gráficos vectoriales bidimensionales, tanto estáticos como dinámicos (interactivos o animados). La especificación SVG es un estándar abierto que ha estado en desarrollo por el Consorcio World Wide Web (W3C) desde 1999.

## Convertir PDF a SVG

El fragmento de código Go proporcionado demuestra cómo convertir la primera página de un documento PDF en una imagen SVG utilizando la biblioteca Aspose.PDF:

1. Abre un documento PDF.
1. Convertir una página a SVG usando [PageToSvg](https://reference.aspose.com/pdf/go-cpp/convert/pagetosvg/) función.
1. Cierre el documento PDF y libere cualquier recurso asignado.

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
      // PageToSvg(num int32, filename string) saves the specified page as Svg-image file
      err = pdf.PageToSvg(1, "sample_page1.svg")
      if err != nil {
        log.Fatal(err)
      }
      // Close() releases allocated resources for PDF-document
      defer pdf.Close()
    }
```

{{% alert color="success" %}}
**Intenta convertir PDF a SVG en línea**

Aspose.PDF for Go le presenta una aplicación gratuita en línea ["PDF a SVG"](https://products.aspose.app/pdf/conversion/pdf-to-svg), donde puedes intentar investigar la funcionalidad y la calidad con la que funciona.

[![Aspose.PDF Conversión de PDF a SVG con aplicación gratuita](pdf_to_svg.png)](https://products.aspose.app/pdf/conversion/pdf-to-svg)
{{% /alert %}}

## Convertir PDF a DICOM

El fragmento de código Go proporcionado muestra cómo convertir la primera página de un documento PDF en una imagen DICOM utilizando la biblioteca Aspose.PDF:

1. Abre un documento PDF.
1. Convertir una página a DICOM usando [PageToDICOM](https://reference.aspose.com/pdf/go-cpp/convert/pagetodicom/) función.
1. Cierre el documento PDF y libere cualquier recurso asignado.

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
      // PageToDICOM(num int32, resolution_dpi int32, filename string) saves the specified page as DICOM-image file
      err = pdf.PageToDICOM(1, 100, "sample_page1.dcm")
      if err != nil {
        log.Fatal(err)
      }
      // Close() releases allocated resources for PDF-document
      defer pdf.Close()
    }
```

## Convertir PDF a BMP

El fragmento de código Go proporcionado demuestra cómo convertir la primera página de un documento PDF en una imagen BMP usando la librería Aspose.PDF:

1. Abre un documento PDF.
1. Convertir una página a BMP usando [PageToBmp](https://reference.aspose.com/pdf/go-cpp/convert/pagetobmp/) función.
1. Cierre el documento PDF y libere cualquier recurso asignado.

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
      // PageToBmp(num int32, resolution_dpi int32, filename string) saves the specified page as Bmp-image file
      err = pdf.PageToBmp(1, 100, "sample_page1.bmp")
      if err != nil {
        log.Fatal(err)
      }
      // Close() releases allocated resources for PDF-document
      defer pdf.Close()
    }
```