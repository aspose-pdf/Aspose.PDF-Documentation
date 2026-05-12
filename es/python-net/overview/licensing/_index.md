---
title: Licencia Aspose PDF
linktitle: Licenciamiento y limitaciones
type: docs
weight: 50
url: /es/python-net/licensing/
description: Aspose.PDF for Python invita a sus clientes a obtener una licencia Classic. Así como usar una licencia limitada para explorar mejor el producto.
lastmod: "2025-02-21"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Licenciamiento de Aspose.PDF for Python
Abstract: El artículo analiza las limitaciones y opciones de licenciamiento para Aspose.PDF for Python. Destaca que la versión de evaluación permite probar la funcionalidad completa pero agrega una marca de agua a los PDFs generados, mostrando "Evaluation Only" junto con información de derechos de autor. Para los usuarios que deseen probar sin estas limitaciones, está disponible una Licencia Temporal de 30 días. El artículo también explica cómo implementar una licencia classic cargándola desde un archivo o flujo, recomendando colocar el archivo de licencia en el mismo directorio que el archivo Aspose.PDF.dll y establecer la licencia usando la clase `Aspose.Pdf.License`. Se proporcionan fragmentos de código para ilustrar el proceso de licenciamiento.
---

## Limitación de una versión de evaluación

Queremos que nuestros clientes prueben nuestros componentes a fondo antes de comprar, por lo que la versión de evaluación le permite usarlo como lo haría normalmente.

- **PDF creado con una marca de agua de evaluación.** La versión de evaluación de Aspose.PDF for Python proporciona la funcionalidad completa del producto, pero todas las páginas en los documentos PDF generados llevan una marca de agua con "Evaluation Only. Created with Aspose.PDF. Copyright 2002-2020 Aspose Pty Ltd" en la parte superior.

>Si desea probar Aspose.PDF sin las limitaciones de la versión de evaluación, también puede solicitar una Licencia Temporal de 30 días. Por favor, consulte a [¿Cómo obtener una Licencia Temporal?](https://purchase.aspose.com/temporary-license)

## Licencia clásica

La licencia se puede cargar desde un archivo o un objeto de flujo. La forma más sencilla de establecer una licencia es colocar el archivo de licencia en la misma carpeta que el archivo Aspose.PDF.dll y especificar el nombre del archivo sin ruta, como se muestra en el ejemplo a continuación.

Si utiliza cualquier otro componente Aspose para Python junto con Aspose.PDF for Python, por favor especifique el espacio de nombres para License como [Clase Aspose.Pdf.License]().

```python

    license_file = LICENSE_FILE
    license = ap.License()
    license.set_license(license_file)
```
