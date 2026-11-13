---
title: Trabajar con artefactos PDF en Python
linktitle: Trabajando con artefactos
type: docs
weight: 170
url: /es/python-net/artifacts/
description: Agregar, inspeccionar y eliminar artefactos PDF en Python, incluidos fondos, marcas de agua, encabezados, pies de página y numeración Bates.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Administrar artefactos de página PDF en Python
Abstract: Encuentre guías para agregar y eliminar artefactos PDF, inspeccionar los detalles de las marcas de agua y contar los artefactos de paginación por subtipo con Aspose.PDF for Python via .NET.
---

Los artefactos PDF marcan elementos de página como fondos decorativos, encabezados y pies de página en ejecución, y marcas de agua. En un PDF etiquetado, las tecnologías de asistencia pueden omitir los artefactos y centrarse en el contenido significativo del documento.

## Elegir una guía

### Agregar artefactos

- [Agregar fondos](/pdf/es/python-net/add-backgrounds/)
- [Agregar marcas de agua](/pdf/es/python-net/add-watermarks/)
- [Agregar numeración Bates](/pdf/es/python-net/add-bates-numbering/)
- [Agregar encabezados y pies de página](/pdf/es/python-net/artifacts-header-footer/)

### Inspeccionar artefactos

- [Contar artefactos de paginación por subtipo](/pdf/es/python-net/counting-artifacts/)
- [Extraer detalles de marca de agua](/pdf/es/python-net/extract-watermarks/)

### Eliminar artefactos

- [Eliminar fondos](/pdf/es/python-net/remove-backgrounds/)
- [Eliminar marcas de agua](/pdf/es/python-net/remove-watermarks/)
- [Eliminar numeración Bates](/pdf/es/python-net/remove-bates-numbering/)
- [Eliminar encabezados y pies de página](/pdf/es/python-net/remove-headers-footers/)

## API de artefactos

La propiedad `artifacts` devuelve la colección [`ArtifactCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/artifactcollection/) de la página. La clase [`Artifact`](https://reference.aspose.com/pdf/python-net/aspose.pdf/artifact/) proporciona las propiedades comunes a las clases especializadas [`BackgroundArtifact`](https://reference.aspose.com/pdf/python-net/aspose.pdf/backgroundartifact/), [`WatermarkArtifact`](https://reference.aspose.com/pdf/python-net/aspose.pdf/watermarkartifact/), [`HeaderArtifact`](https://reference.aspose.com/pdf/python-net/aspose.pdf/headerartifact/), [`FooterArtifact`](https://reference.aspose.com/pdf/python-net/aspose.pdf/footerartifact/) y [`BatesNArtifact`](https://reference.aspose.com/pdf/python-net/aspose.pdf/batesnartifact/).

| Tarea | Propiedades |
| --- | --- |
| Identificar el artefacto | Usar `type` y `subtype` para clasificaciones estándar y `custom_type` y `custom_subtype` para nombres personalizados. |
| Inspecciona su contenido | Usar `text`, `image`, y `lines` para texto e imágenes, o `contents` y `form` para los operadores PDF y el XForm asociado. |
| Posiciónalo en la página | Usar `rectangle` para inspeccionar sus límites. Establecer `position` para colocación explícita o uso `left_margin`, `right_margin`, `top_margin`, `bottom_margin`, `artifact_horizontal_alignment`, y `artifact_vertical_alignment`. Una posición explícita anula los márgenes y la alineación. |
| Controla su apariencia | Usar `rotation`, `opacity` (de 0 a 1), y `text_state`. Establecer `is_background` colocar el artefacto detrás del contenido de la página. |
