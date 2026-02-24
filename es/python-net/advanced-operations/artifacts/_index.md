---
title: Trabajando con artefactos en Python a través de .NET
linktitle: Trabajando con artefactos
type: docs
weight: 170
url: /es/python-net/artifacts/
description: Aspose.PDF para Python a través de .NET le permite añadir una imagen de fondo a las páginas PDF y obtener cada marca de agua usando la clase Artifact.
lastmod: "2025-11-13"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Añadir artefactos a PDF usando Python
Abstract: Este artículo explora el concepto y la aplicación de los artefactos en documentos PDF, centrándose particularmente en su papel para mejorar la accesibilidad y el rendimiento. Los artefactos son elementos no contenidos, como componentes decorativos o de diseño, que no transmiten el significado del documento. El artículo destaca el uso de la clase `Artifact` en la biblioteca Aspose.PDF para Python a través de .NET para gestionar estos elementos, ofreciendo propiedades como `custom_type`, `contents` y `opacity` para una personalización detallada. También presenta clases relacionadas para manejar tipos específicos de artefactos. Los ejemplos prácticos demuestran operaciones como la obtención de marcas de agua, la adición de imágenes de fondo, el recuento de tipos de artefactos y la implementación de numeración Bates.
---

Los artefactos en PDF son objetos gráficos u otros elementos que no forman parte del contenido real del documento. Normalmente se utilizan con fines de decoración, diseño o fondo. Ejemplos de artefactos incluyen encabezados de página, pies de página, separadores o imágenes que no transmiten ningún significado.

El propósito de los artefactos en PDF es permitir la distinción entre elementos de contenido y no contenido. Esto es importante para la accesibilidad, ya que los lectores de pantalla y otras tecnologías de asistencia pueden ignorar los artefactos y centrarse en el contenido relevante. Los artefactos también pueden mejorar el rendimiento y la calidad de los documentos PDF, ya que pueden omitirse en la impresión, búsqueda o copia.

Para crear un elemento como artefacto en PDF, necesita utilizar la clase [Artifact](https://reference.aspose.com/pdf/python-net/aspose.pdf/artifact/).
Contiene las siguientes propiedades útiles:

- **custom_type** - Obtiene el nombre del tipo de artefacto. Puede usarse si el tipo de artefacto no es estándar.
- **custom_subtype** - Obtiene el nombre del subtipo de artefacto. Puede usarse si el subtipo de artefacto no es un subtipo estándar.
- **type** - Obtiene el tipo de artefacto.
- **subtype** - Obtiene el subtipo de artefacto. Si el artefacto tiene un subtipo no estándar, el nombre del subtipo puede leerse a través de CustomSubtype.
- **contents** - Obtiene la colección de operadores internos del artefacto.
- **form** - Obtiene XForm del artefacto (si se usa XForm).
- **rectangle** - Obtiene el rectángulo del artefacto.
- **position** - Obtiene o establece la posición del artefacto. Si esta propiedad se especifica, los márgenes y alineaciones se ignoran.
- **right_margin** - Margen derecho del artefacto. Si la posición se especifica explícitamente (en la propiedad Position), este valor se ignora.
- **left_margin** - Margen izquierdo del artefacto. Si la posición se especifica explícitamente (en la propiedad Position), este valor se ignora.
- **top_margin** - Margen superior del artefacto. Si la posición se especifica explícitamente (en la propiedad Position), este valor se ignora.
- **bottom_margin** - Margen inferior del artefacto. Si la posición se especifica explícitamente (en la propiedad Position), este valor se ignora.
- **artifact_horizontal_alignment** - Alineación horizontal del artefacto. Si la posición se especifica explícitamente (en la propiedad Position), este valor se ignora.
- **artifact_vertical_alignment** - Alineación vertical del artefacto. Si la posición se especifica explícitamente (en la propiedad Position), este valor se ignora.
- **rotation** - Obtiene o establece el ángulo de rotación del artefacto.
- **text** - Obtiene el texto del artefacto.
- **image** - Obtiene la imagen del artefacto (si está presente).
- **opacity** - Obtiene o establece la opacidad del artefacto. Los valores posibles están en el rango 0..1.
- **lines** - Líneas del artefacto de texto multilínea.
- **text_state** - Estado de texto para el texto del artefacto.
- **is_background** - Si es verdadero, el artefacto se coloca detrás del contenido de la página.

Las siguientes clases también pueden ser útiles para trabajar con artefactos:

- [ArtifactCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/artifactcollection/)
- [BackgroundArtifact](https://reference.aspose.com/pdf/python-net/aspose.pdf/backgroundartifact/)
- [HeaderArtifact](https://reference.aspose.com/pdf/python-net/aspose.pdf/headerartifact/)
- [FooterArtifact](https://reference.aspose.com/pdf/python-net/aspose.pdf/footerartifact/)
- [WatermarkArtifact](https://reference.aspose.com/pdf/python-net/aspose.pdf/watermarkartifact/)
- [Numeración Bates](https://reference.aspose.com/pdf/python-net/aspose.pdf/)

Por favor, revise las siguientes secciones del artículo:

- [Añadiendo fondos](/pdf/python-net/add-backgrounds/) - añadir una imagen de fondo a su archivo PDF con Python.
- [Añadiendo numeración Bates](/pdf/python-net/add-bates-numbering/) - añadir numeración Bates a PDF.
- [Añadiendo marca de agua](/pdf/python-net/add-watermarks/) - cómo añadir una marca de agua a PDF con Python.
- [Contando artefactos](/pdf/python-net/counting-artifacts/) - contar artefactos en PDF usando Python.

