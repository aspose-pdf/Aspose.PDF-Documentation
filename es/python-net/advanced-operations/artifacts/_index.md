---
title: Trabajar con artefactos PDF en Python
linktitle: Trabajando con artefactos
type: docs
weight: 170
url: /es/python-net/artifacts/
description: Aprenda cómo trabajar con artefactos PDF en Python para agregar fondos, marcas de agua y numeración Bates, y contar tipos de artefactos con Aspose.PDF for Python via .NET.
lastmod: "2026-05-08"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Agregar artefactos de fondos, marcas de agua y numeración Bates en Python
Abstract: Este artículo explica cómo trabajar con artefactos PDF en Aspose.PDF for Python via .NET. Aprenda qué son los artefactos, por qué son importantes para la accesibilidad y el diseño de documentos, y cómo agregar imágenes de fondo, aplicar marcas de agua, agregar numeración Bates y examinar los tipos de artefactos en archivos PDF con Python.
---

Los artefactos en PDF son objetos gráficos u otros elementos que no forman parte del contenido real del documento. Normalmente se utilizan para decoración, diseño o propósitos de fondo. Ejemplos de artefactos incluyen encabezados y pies de página, separadores o imágenes que no transmiten ningún significado.

El propósito de los artefactos en PDF es permitir la distinción entre elementos de contenido y elementos que no forman parte del contenido. Esto es importante para la accesibilidad, ya que los lectores de pantalla y otras tecnologías de asistencia pueden ignorar los artefactos y centrarse en el contenido relevante. Los artefactos también pueden mejorar el rendimiento y la calidad de los documentos PDF, ya que pueden omitirse en la impresión, la búsqueda o la copia.

Utilice esta sección cuando necesite crear o inspeccionar elementos PDF que no forman parte del contenido en Python, como fondos de documentos, marcas de agua de página y marcas de numeración Bates. Las siguientes guías muestran los principales flujos de trabajo de artefactos compatibles con Aspose.PDF for Python via .NET.

Para crear un elemento como artefacto en PDF, necesita usar la clase [Artifact](https://reference.aspose.com/pdf/python-net/aspose.pdf/artifact/).
Esta clase contiene las siguientes propiedades útiles:

- **custom_type** - Obtiene el nombre del tipo de artefacto. Puede usarse si el tipo de artefacto no es estándar.
- **custom_subtype** - Obtiene el nombre del subtipo de artefacto. Puede usarse si el subtipo de artefacto no es un subtipo estándar.
- **type** - Obtiene el tipo de artefacto.
- **subtype** - Obtiene el subtipo de artefacto. Si el artefacto tiene un subtipo no estándar, el nombre del subtipo puede leerse a través de CustomSubtype.
- **contents** - Obtiene la colección de operadores internos del artefacto.
- **form** - Obtiene el XForm del artefacto (si se usa XForm).
- **rectangle** - Obtiene el rectángulo del artefacto.
- **position** - Obtiene o establece la posición del artefacto. Si se especifica esta propiedad, entonces los márgenes y alineaciones se ignoran.
- **right_margin** - Margen derecho del artefacto. Si la posición se especifica explícitamente (en la propiedad Position) este valor se ignora.
- **left_margin** - Margen izquierdo del artefacto. Si la posición se especifica explícitamente (en la propiedad Position) este valor se ignora.
- **top_margin** - Margen superior del artefacto. Si la posición se especifica explícitamente (en la propiedad Position) este valor se ignora.
- **bottom_margin** - Margen inferior del artefacto. Si la posición se especifica explícitamente (en la propiedad Position) este valor se ignora.
- **artifact_horizontal_alignment** - Alineación horizontal del artefacto. Si la posición se especifica explícitamente (en la propiedad Position) este valor se ignora.
- **artifact_vertical_alignment** - Alineación vertical del artefacto. Si la posición se especifica explícitamente (en la propiedad Position) este valor se ignora.
- **rotation** - Obtiene o establece el ángulo de rotación del artefacto.
- **text** - Obtiene el texto del artefacto.
- **image** - Obtiene la imagen del artefacto (si está presente).
- **opacity** - Obtiene o establece la opacidad del artefacto. Los valores posibles están en el rango 0..1.
- **lines** - Líneas del artefacto de texto multilínea.
- **text_state** - Estado de texto para el texto del artefacto.
- **is_background** - Si es verdadero, el Artefacto se coloca detrás del contenido de la página.

Las siguientes clases también pueden ser útiles para trabajar con artefactos:

- [ArtifactCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/artifactcollection/)
- [BackgroundArtifact](https://reference.aspose.com/pdf/python-net/aspose.pdf/backgroundartifact/)
- [HeaderArtifact](https://reference.aspose.com/pdf/python-net/aspose.pdf/headerartifact/)
- [FooterArtifact](https://reference.aspose.com/pdf/python-net/aspose.pdf/footerartifact/)
- [WatermarkArtifact](https://reference.aspose.com/pdf/python-net/aspose.pdf/watermarkartifact/)
- [BatesNArtifact](https://reference.aspose.com/pdf/python-net/aspose.pdf/batesnartifact/)

## Flujos de trabajo de artefactos cubiertos en esta sección

Por favor revise las siguientes secciones del artículo:

- [Agregar fondos](/pdf/es/python-net/add-backgrounds/) - agregue una imagen de fondo a su archivo PDF con Python.
- [Agregar numeración Bates](/pdf/es/python-net/add-bates-numbering/) - agregar numeración Bates al PDF.
- [Agregar marca de agua](/pdf/es/python-net/add-watermarks/) - cómo agregar una marca de agua al PDF con Python.
- [Contar artefactos](/pdf/es/python-net/counting-artifacts/) - contar artefactos en PDF usando Python.
- [Administrar encabezados y pies de página de PDF](/pdf/es/python-net/artifacts-header-footer/) - gestionar encabezados y pies de página en documentos PDF.

Estos tutoriales son útiles cuando necesitas gestionar elementos decorativos o estructurales del PDF sin cambiar el flujo de contenido principal del documento.
