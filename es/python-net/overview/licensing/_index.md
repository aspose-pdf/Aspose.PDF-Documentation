---
title: Aspose PDF License
linktitle: Licensing and limitations
type: docs
weight: 50
url: /es/python-net/licensing/
description: Aspose. PDF para Python invita a sus clientes a obtener una licencia Clásica. Así como utilizar una licencia limitada para explorar mejor el producto.
lastmod: "2022-12-21"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Limitación de una versión de evaluación

Queremos que nuestros clientes prueben a fondo nuestros componentes antes de comprarlos, por lo que la versión de evaluación le permite usarlo como lo haría normalmente.

- **PDF creado con una marca de agua de evaluación.** La versión de evaluación de Aspose.PDF para Python proporciona toda la funcionalidad del producto, pero todas las páginas en los documentos PDF generados están marcadas con agua con "Solo Evaluación. Creado con Aspose.PDF. Copyright 2002-2020 Aspose Pty Ltd" en la parte superior.

>Si desea probar Aspose.PDF sin las limitaciones de la versión de evaluación, también puede solicitar una Licencia Temporal de 30 días.
 ## Licencia clásica

La licencia se puede cargar desde un archivo o un objeto de flujo. La forma más fácil de establecer una licencia es colocar el archivo de licencia en la misma carpeta que el archivo Aspose.PDF.dll y especificar el nombre del archivo sin una ruta, como se muestra en el ejemplo a continuación.

Si utiliza cualquier otro componente de Aspose para Python junto con Aspose.PDF para Python, por favor especifique el espacio de nombres para License como [Aspose.Pdf.License class]().

```python

    license_file = LICENSE_FILE
    license = ap.License()
    license.set_license(license_file)
```