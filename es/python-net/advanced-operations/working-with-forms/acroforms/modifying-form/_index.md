---
title: Modificar AcroForm
linktitle: Modificar AcroForm
type: docs
weight: 45
url: /es/python-net/modifying-form/
description: Modifique formularios en su archivo PDF con Aspose.PDF para Python a traves de .NET. Puede agregar o eliminar campos en un formulario existente, y obtener o establecer limites de campo, entre otras operaciones.
lastmod: "2025-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Gestión y personalización de campos de formulario PDF
Abstract: Esta colección de ejemplos muestra diversas técnicas para gestionar y personalizar campos de formulario PDF utilizando Aspose.PDF for Python via .NET. Incluye métodos para borrar texto de campos de formulario de estilo Typewriter‑style usando TextFragmentAbsorber, establecer y recuperar límites de caracteres con FormEditor, aplicar fuentes y estilos personalizados a campos de cuadro de texto, y eliminar campos de formulario específicos por nombre. Estas operaciones permiten a los desarrolladores sanitizar, formatear y adaptar formularios PDF para redistribución, branding o validación de datos, respaldando tanto el refinamiento estético como funcional en flujos de trabajo automatizados de documentos.
---

## Borrar texto en Form

Este ejemplo demuestra cómo borrar texto de los campos de formulario Typewriter en un PDF usando Aspose.PDF for Python via .NET. Escanea la primera página del PDF, identifica los formularios Typewriter, elimina su contenido y guarda el documento actualizado. Este enfoque es útil para restablecer o desinfectar los campos de formulario antes de redistribuir un PDF.

1. Cargue el documento PDF de entrada.
1. Acceda a los formularios en la primera página.
1. Itera sobre cada formulario y verifica si es un `Typewriter` Form.
1. Utilice TextFragmentAbsorber para encontrar fragmentos de texto en el formulario.
1. Borre el texto de cada fragmento.
1. Guarde el PDF modificado en el archivo de salida.

```python
import aspose.pdf as ap
from aspose.pycore import cast, is_assignable

dataDir = "path/to/your/data/dir/"
path_infile = dataDir + infile
path_outfile = dataDir + outfile
document = ap.Document(path_infile)

# Get the forms from the first page
forms = document.pages[1].resources.forms

for form in forms:
    # Check if the form is of type "Typewriter" and subtype "Form"
    if form.it == "Typewriter" and form.subtype == "Form":
        # Create a TextFragmentAbsorber to find text fragments
        absorber = ap.Text.TextFragmentAbsorber()
        absorber.visit(form)

        # Clear the text in each fragment
        for fragment in absorber.text_fragments:
            fragment.Text = ""

# Save PDF document
document.save(path_outfile)
```

## Obtener o Establecer Límite de Campo

El método set_field_limit(field, limit) de la clase FormEditor permite establecer un límite de campo, el número máximo de caracteres que se pueden ingresar en un campo.

```python
import aspose.pdf as ap
from aspose.pycore import cast, is_assignable

# The path to the documents directory
data_dir = "/path/to/your/pdf/files/"
path_infile = os.path.join(work_dir, infile)
path_outfile = os.path.join(work_dir, outfile)

# Create FormEditor instance
form = ap.facades.FormEditor()

# Bind PDF document
form.bind_pdf(path_infile)

# Set field limit for "First Name"
form.set_field_limit("First Name", 15)

# Save PDF document
form.save(path_outfile)
```

Del mismo modo, Aspose.PDF tiene un método que obtiene el límite del campo.

```python
import aspose.pdf as ap
from aspose.pycore import cast, is_assignable

# The path to the documents directory
data_dir = "/path/to/your/pdf/files/"
path_infile = os.path.join(work_dir, infile)

document = ap.Document(path_infile)
if is_assignable(document.form[1], ap.forms.TextBoxField):
    textBoxField = cast(ap.forms.TextBoxField, document.form[1])
    print(f"Limit: {textBoxField.max_len}")
```

## Establecer fuente personalizada para el campo del formulario

Los campos de formulario en archivos PDF de Adobe pueden configurarse para usar fuentes predeterminadas específicas. En las primeras versiones de Aspose.PDF, solo se admitían las 14 fuentes predeterminadas. Las versiones posteriores permitieron a los desarrolladores aplicar cualquier fuente.

Este código actualiza la apariencia de un campo de cuadro de texto en un formulario PDF estableciendo una fuente personalizada, tamaño y color, y luego guarda el documento modificado usando Aspose.PDF for Python via .NET.

El siguiente fragmento de código muestra cómo establecer la fuente predeterminada para los campos de formulario PDF.

```python
import aspose.pdf as ap
from aspose.pycore import cast, is_assignable

data_dir = "/path/to/your/pdf/files/"
path_infile = os.path.join(work_dir, infile)
path_outfile = os.path.join(work_dir, outfile)

document = ap.Document(path_infile)
if is_assignable(document.form[1], ap.forms.TextBoxField):
    textBoxField = cast(ap.forms.TextBoxField, document.form[1])
    font = ap.text.FontRepository.find_font("Calibri")
    textBoxField.default_appearance = ap.annotations.DefaultAppearance(
        font, 10, ap.Color.black.to_rgb()
    )

document.save(path_outfile)
```

## Eliminar campos en el formulario existente

Este código elimina un campo de formulario específico (por su nombre) de un documento PDF y guarda el archivo actualizado utilizando Aspose.PDF for Python via .NET.

1. Cargar el documento PDF.
1. Eliminar un campo de formulario por nombre.
1. Guardar el PDF actualizado.

```python
import aspose.pdf as ap
from aspose.pycore import cast, is_assignable

data_dir = "/path/to/your/pdf/files/"
path_infile = os.path.join(work_dir, infile)
path_outfile = os.path.join(work_dir, outfile)

document = ap.Document(path_infile)
# Delete a particular field by name
document.form.delete("First Name")
# Save PDF document
document.save(path_outfile)
```
