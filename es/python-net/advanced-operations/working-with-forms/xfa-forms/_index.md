---
title: Trabajando con formularios XFA
linktitle: Formularios XFA
type: docs
weight: 20
url: /es/python-net/xfa-forms/
description: Aspose.PDF for Python via .NET API le permite trabajar con campos XFA y XFA Acroform en un documento PDF.
lastmod: "2025-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Convertir XFA a Acroform

{{% alert color="primary" %}}

Probar en línea
Puede verificar la calidad de la conversión de Aspose.PDF y ver los resultados en línea en este enlace: [products.aspose.app/pdf/xfa/acroform](https://products.aspose.app/pdf/xfa/acroform)

{{% /alert %}}

El siguiente fragmento de código muestra cómo convertir un formulario XFA (XML Forms Architecture) dinámico a un AcroForm estándar.

**Los pasos clave incluyen:**

1. Cargando el documento PDF de entrada.
1. Cambiando el tipo de formulario a ESTÁNDAR.
1. Guardando el PDF convertido en un archivo nuevo.

Esta conversión permite una mejor compatibilidad y un manejo coherente de formularios en diferentes lectores y aplicaciones de PDF.

```python
import aspose.pdf as ap
import sys
from os import path

def convert_dynamic_xfa_to_acroform(infile: str, outfile: str):
    """Convert dynamic XFA form to standard AcroForm."""
    with ap.Document(infile) as document:
        document.form.type = ap.forms.FormType.STANDARD
        document.save(outfile)
```

## Uso de IgnoreNeedsRendering

Este ejemplo muestra cómo convertir un formulario XFA dinámico a un AcroForm estándar usando Aspose.PDF for Python. El código verifica si el PDF de entrada contiene un formulario XFA y anula la renderización si es necesario. Luego establece el tipo de formulario como STANDARD y guarda el PDF actualizado.

```python
import aspose.pdf as ap
import sys
from os import path

def convert_xfa_form_with_ignore_needs_rendering(infile: str, outfile: str):
    """Convert XFA form ignoring needs rendering flag."""
    with ap.Document(infile) as document:
        if not document.form.needs_rendering and document.form.has_xfa:
            document.form.ignore_needs_rendering = True
        document.form.type = ap.forms.FormType.STANDARD
        document.save(outfile)
```
