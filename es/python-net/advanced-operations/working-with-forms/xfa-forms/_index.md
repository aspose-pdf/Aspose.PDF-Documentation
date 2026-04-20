---
title: Trabajar con formularios XFA
linktitle: Formularios XFA
type: docs
weight: 20
url: /es/python-net/xfa-forms/
description: La API de Aspose.PDF para Python a traves de .NET le permite trabajar con campos XFA y XFA AcroForm en un documento PDF.
lastmod: "2025-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Convertir XFA a AcroForm

{{% alert color="primary" %}}

Prueba en línea
Puede comprobar la calidad de la conversión de Aspose.PDF y ver los resultados en línea en este enlace: [products.aspose.app/pdf/xfa/acroform](https://products.aspose.app/pdf/xfa/acroform)

{{% /alert %}}

El siguiente fragmento de código demuestra cómo convertir un formulario XFA (XML Forms Architecture) dinámico a un AcroForm estándar.

**Los pasos clave incluyen:**

1. Cargando el documento PDF de entrada.
1. Cambiar el tipo de formulario a STANDARD.
1. Guardando el PDF convertido en un nuevo archivo.

Esta conversión permite una mejor compatibilidad y un manejo consistente de formularios en diferentes lectores y aplicaciones PDF.

```python

    import aspose.pdf as ap


    path_infile = self.data_dir + "DynamicXFAToAcroForm.pdf.pdf"
    path_outfile = self.data_dir + "StandardAcroForm_out.pdf"

    # Load dynamic XFA form
    with ap.Document(path_infile) as document:
        # Set the form fields type as standard AcroForm
        document.form.type = ap.forms.FormType.STANDARD
        # Save PDF document
        document.save(path_outfile)
```

## Uso de IgnoreNeedsRendering

Este ejemplo demuestra cómo convertir un formulario XFA dinámico a un AcroForm estándar usando Aspose.PDF for Python. El código verifica si el PDF de entrada contiene un formulario XFA y anula el renderizado si es necesario. Luego establece el tipo de formulario a STANDARD y guarda el PDF actualizado.

```python

    import aspose.pdf as ap


    path_infile = self.data_dir + "DynamicXFAToAcroForm.pdf.pdf"
    path_outfile = self.data_dir + "StandardAcroForm_out.pdf"

    # Load dynamic XFA form
    with ap.Document(path_infile) as document:
        # check if XFA is present & if rendering should be overwritten
        if not document.form.needs_rendering and document.form.has_xfa:
            document.form.ignore_needs_rendering = True
        # Set the form fields type as standard AcroForm
        document.form.type = ap.forms.FormType.STANDARD
        # Save the resultant PDF
        document.save(path_outfile)
```
