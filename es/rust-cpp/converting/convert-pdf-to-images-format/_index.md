---
title: Convertir PDF a formatos de imagen en Rust
linktitle: Convertir PDF a imágenes
type: docs
weight: 70
url: /es/rust-cpp/convert-pdf-to-images-format/
lastmod: "2026-07-20"
description: Este tema le muestra cómo usar Aspose.PDF for Rust para convertir PDF a varios formatos de imagen, p. ej., TIFF, BMP, JPEG, PNG, SVG con unas pocas líneas de código.
sitemap:
    changefreq: "monthly"
    priority: 0.5
TechArticle: true
AlternativeHeadline: Herramienta para convertir PDF a formato de imágenes con Aspose.PDF for Rust
Abstract: Aspose.PDF for Rust via C++ permite una conversión fluida de documentos PDF a varios formatos de imagen, incluidos JPEG, PNG, BMP y TIFF. Esta característica permite a los desarrolladores generar imágenes de alta calidad mientras se preserva el contenido, el diseño y la resolución del documento original. La biblioteca ofrece opciones flexibles para la configuración de salida, como resolución, calidad de imagen y profundidad de color. La documentación proporciona instrucciones paso a paso y ejemplos de código para ayudar a los desarrolladores a integrar de manera eficiente la conversión de PDF a imagen en sus aplicaciones.
SoftwareApplication: rust-cpp
---

## Convertir PDF a imagen

En este artículo, le mostraremos las opciones para convertir PDF a formatos de imagen.

Los documentos escaneados previamente a menudo se guardan en el formato de archivo PDF. Sin embargo, ¿necesita editarlos en un editor gráfico o enviarlos posteriormente en formato de imagen? Tenemos una herramienta universal para usted que convierte PDF a imágenes usando **Aspose.PDF for Rust via C++**.
La tarea más común es cuando necesitas guardar un documento PDF completo o algunas páginas específicas de un documento como un conjunto de imágenes. **Aspose.PDF for Rust via C\u002B\u002B** te permite convertir PDF a formatos JPG y PNG para simplificar los pasos necesarios para obtener tus imágenes de un archivo PDF específico.

**Aspose.PDF for Rust via C++** admite la conversión de varios formatos de PDF a imagen. Por favor, consulte la sección [Aspose.PDF Formatos de archivo compatibles](https://docs.aspose.com/pdf/rust-cpp/supported-file-formats/).

### Convertir PDF a JPEG

El fragmento de código Rust proporcionado muestra cómo convertir la primera página de un documento PDF en una imagen JPEG utilizando la biblioteca Aspose.PDF:

1. Abra un documento PDF.
1. Convertir una página a JPEG usando [page_to_jpg](https://reference.aspose.com/pdf/rust-cpp/convert/page_to_jpg/) función.

```rs

  use asposepdf::Document;

  fn main() -> Result<(), Box<dyn std::error::Error>> {
      // Open a PDF-document with filename
      let pdf = Document::open("sample.pdf")?;

      // Convert and save the specified page as Jpg-image
      pdf.page_to_jpg(1, 100, "sample_page1.jpg")?;

      Ok(())
  }
```

{{% alert color="success" %}}
**Intenta convertir PDF a JPEG en línea**

Aspose.PDF para Rust le presenta una aplicación gratuita en línea ["PDF a JPEG"](https://products.aspose.app/pdf/conversion/pdf-to-jpg), donde puedes intentar investigar la funcionalidad y la calidad con la que funciona.

[![Conversión de PDF a JPEG con Aspose.PDF y aplicación gratuita](pdf_to_jpg.png)](https://products.aspose.app/pdf/conversion/pdf-to-jpg)
{{% /alert %}}

### Convertir PDF a TIFF

El fragmento de código Rust proporcionado muestra cómo convertir la primera página de un documento PDF a una imagen TIFF utilizando la biblioteca Aspose.PDF:

1. Abra un documento PDF.
1. Convertir una página a TIFF usando [page_to_tiff](https://reference.aspose.com/pdf/rust-cpp/convert/page_to_tiff/) función.

```rs

  use asposepdf::Document;

  fn main() -> Result<(), Box<dyn std::error::Error>> {
      // Open a PDF-document with filename
      let pdf = Document::open("sample.pdf")?;

      // Convert and save the specified page as Tiff-image
      pdf.page_to_tiff(1, 100, "sample_page1.tiff")?;

      Ok(())
  }
```

{{% alert color="success" %}}
**Intenta convertir PDF a TIFF en línea**

Aspose.PDF para Rust le presenta una aplicación gratuita en línea ["PDF a TIFF"](https://products.aspose.app/pdf/conversion/pdf-to-tiff), donde puedes intentar investigar la funcionalidad y la calidad con la que funciona.

[![Conversión de Aspose.PDF de PDF a TIFF con aplicación gratuita](pdf_to_tiff.png)](https://products.aspose.app/pdf/conversion/pdf-to-tiff)
{{% /alert %}}

### Convertir PDF a PNG

El fragmento de código Rust proporcionado muestra cómo convertir la primera página de un documento PDF en una imagen PNG usando la biblioteca Aspose.PDF:

1. Abra un documento PDF.
1. Convertir una página a PNG usando [page_to_png](https://reference.aspose.com/pdf/rust-cpp/convert/page_to_png/) función.

```rs

  use asposepdf::Document;

  fn main() -> Result<(), Box<dyn std::error::Error>> {
      // Open a PDF-document with filename
      let pdf = Document::open("sample.pdf")?;

      // Convert and save the specified page as Png-image
      pdf.page_to_png(1, 100, "sample_page1.png")?;

      Ok(())
  }
```

{{% alert color="success" %}}
**Intenta convertir PDF a PNG en línea**

Como ejemplo de cómo funcionan nuestras aplicaciones gratuitas, por favor revise la siguiente funcionalidad.

Aspose.PDF para Rust le presenta una aplicación gratuita en línea ["PDF a PNG"](https://products.aspose.app/pdf/conversion/pdf-to-png), donde puedes intentar investigar la funcionalidad y la calidad con la que funciona.

[![Cómo convertir PDF a PNG usando una aplicación gratuita](pdf_to_png.png)](https://products.aspose.app/pdf/conversion/pdf-to-png)
{{% /alert %}}

**Scalable Vector Graphics (SVG)** es una familia de especificaciones de un formato de archivo basado en XML para gráficos vectoriales bidimensionales, tanto estáticos como dinámicos (interactivos o animados). La especificación SVG es un estándar abierto que ha estado en desarrollo por el Consorcio World Wide Web (W3C) desde 1999.

### Convertir PDF a SVG

El fragmento de código Rust proporcionado muestra cómo convertir la primera página de un documento PDF en una imagen SVG usando la biblioteca Aspose.PDF:

1. Abra un documento PDF.
1. Convertir una página a SVG usando [page_to_svg](https://reference.aspose.com/pdf/rust-cpp/convert/page_to_svg/) función.

```rs

  use asposepdf::Document;

  fn main() -> Result<(), Box<dyn std::error::Error>> {
      // Open a PDF-document with filename
      let pdf = Document::open("sample.pdf")?;

      // Convert and save the specified page as Svg-image
      pdf.page_to_svg(1, "sample_page1.svg")?;

      Ok(())
  }
```

{{% alert color="success" %}}
**Intenta convertir PDF a SVG en línea**

Aspose.PDF para Rust le presenta una aplicación gratuita en línea ["PDF a SVG"](https://products.aspose.app/pdf/conversion/pdf-to-svg), donde puedes intentar investigar la funcionalidad y la calidad con la que funciona.

[![Aspose.PDF Conversión de PDF a SVG con aplicación gratuita](pdf_to_svg.png)](https://products.aspose.app/pdf/conversion/pdf-to-svg)
{{% /alert %}}

### Convertir PDF a archivo ZIP de SVG

El siguiente ejemplo convierte un documento PDF en un archivo SVG, donde cada página se guarda como un archivo SVG separado dentro de un contenedor ZIP.

1. Abra el documento PDF de origen.
1. Guarde el documento como un archivo ZIP que contenga archivos SVG.

```rs

  use asposepdf::Document;

  fn main() -> Result<(), Box<dyn std::error::Error>> {
      // Open a PDF-document with filename
      let pdf = Document::open("sample.pdf")?;

      // Convert and save the previously opened PDF-document as SVG-archive
      pdf.save_svg_zip("sample_svg.zip")?;

      Ok(())
  }
```

### Convertir PDF a DICOM

El fragmento de código Rust proporcionado demuestra cómo convertir la primera página de un documento PDF en una imagen DICOM usando la biblioteca Aspose.PDF:

1. Abra un documento PDF.
1. Convertir una página a DICOM usando [page_to_dicom](https://reference.aspose.com/pdf/rust-cpp/convert/page_to_dicom/) función.

```rs

  use asposepdf::Document;

  fn main() -> Result<(), Box<dyn std::error::Error>> {
      // Open a PDF-document with filename
      let pdf = Document::open("sample.pdf")?;

      // Convert and save the specified page as DICOM-image
      pdf.page_to_dicom(1, 100, "sample_page1.dcm")?;

      Ok(())
  }
```

### Convertir PDF a BMP

El fragmento de código Rust proporcionado demuestra cómo convertir la primera página de un documento PDF en una imagen BMP usando la biblioteca Aspose.PDF:

1. Abra un documento PDF.
1. Convertir una Page a BMP usando [page_to_bmp](https://reference.aspose.com/pdf/rust-cpp/convert/page_to_bmp/) función.

```rs

  use asposepdf::Document;

  fn main() -> Result<(), Box<dyn std::error::Error>> {
      // Open a PDF-document with filename
      let pdf = Document::open("sample.pdf")?;

      // Convert and save the specified page as Bmp-image
      pdf.page_to_bmp(1, 100, "sample_page1.bmp")?;

      Ok(())
  }
```