---
title: Trabajar con artefactos PDF en Python
linktitle: Trabajar con artefactos
type: docs
weight: 170
url: /es/python-net/artifacts/
description: Aprenda a trabajar con artefactos PDF en Python para agregar fondos, marcas de agua y numeracion Bates, y contar tipos de artefactos con Aspose.PDF para Python a traves de .NET.
lastmod: "2026-04-15"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: Agregar fondos, marcas de agua y artefactos de numeracion Bates en Python
Abstract: Este articulo explica como trabajar con artefactos PDF en Aspose.PDF para Python a traves de .NET. Aprenda que son los artefactos, por que son importantes para la accesibilidad y el diseño del documento, y como agregar imagenes de fondo, aplicar marcas de agua, agregar numeracion Bates y examinar los tipos de artefactos en archivos PDF con Python.
---

Los artefactos en PDF son objetos gráficos u otros elementos que no forman parte del contenido real del documento. Normalmente se utilizan para decoración, diseño o propósitos de fondo. Ejemplos de artefactos incluyen encabezados de página, pies de página, separadores o imágenes que no transmiten ningún significado.

El proposito de los artefactos en PDF es permitir la distincion entre elementos de contenido y de no contenido. Esto es importante para la accesibilidad, ya que los lectores de pantalla y otras tecnologias de asistencia pueden ignorar los artefactos y centrarse en el contenido relevante. Los artefactos tambien pueden mejorar el rendimiento y la calidad de los documentos PDF, ya que pueden omitirse en la impresion, la busqueda o la copia.

Utilice esta seccion cuando necesite crear o inspeccionar elementos PDF que no forman parte del contenido en Python, como fondos de documento, marcas de agua de pagina y marcas de numeracion Bates. Las guias siguientes muestran los principales flujos de trabajo de artefactos compatibles con Aspose.PDF para Python a traves de .NET.

Para crear un elemento como artefacto en PDF, necesita usar la clase [Artifact](https://reference.aspose.com/pdf/python-net/aspose.pdf/artifact/).
Contiene las siguientes propiedades útiles:

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
- **text_state** - Estado del texto para el texto del artefacto.
- **is_background** - Si es verdadero, el artefacto se coloca detrás del contenido de la página.

Las siguientes clases también pueden ser útiles para trabajar con artefactos:

- [ArtifactCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/artifactcollection/)
- [BackgroundArtifact](https://reference.aspose.com/pdf/python-net/aspose.pdf/backgroundartifact/)
- [HeaderArtifact](https://reference.aspose.com/pdf/python-net/aspose.pdf/headerartifact/)
- [FooterArtifact](https://reference.aspose.com/pdf/python-net/aspose.pdf/footerartifact/)
- [WatermarkArtifact](https://reference.aspose.com/pdf/python-net/aspose.pdf/watermarkartifact/)
- [BatesNArtifact](https://reference.aspose.com/pdf/python-net/aspose.pdf/batesnartifact/)

## Flujos de trabajo de artefactos cubiertos en esta sección

Por favor revise las siguientes secciones del artículo:

- [Agregar fondos](/pdf/es/python-net/add-backgrounds/) - agregar una imagen de fondo a su archivo PDF con Python.
- [Agregar numeracion Bates](/pdf/es/python-net/add-bates-numbering/) - agregar numeracion Bates al PDF.
- [Agregar marca de agua](/pdf/es/python-net/add-watermarks/) - como agregar una marca de agua al PDF con Python.
- [Contar artefactos](/pdf/es/python-net/counting-artifacts/) - contar artefactos en PDF usando Python.

Estos tutoriales son útiles cuando necesitas gestionar elementos decorativos o estructurales del PDF sin cambiar el flujo de contenido principal del documento.
