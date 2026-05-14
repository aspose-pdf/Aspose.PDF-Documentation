---
title: Obtener privilegios del documento
linktitle: Obtener privilegios del documento
type: docs
weight: 10
url: /es/python-net/get-document-privileges/
description: Aprenda cómo verificar programáticamente los privilegios de un documento PDF usando Aspose.PDF for Python. Este tutorial muestra cómo usar la clase PdfFileInfo para leer la configuración de seguridad del documento, como los permisos de impresión, copia o modificación.
lastmod: "2026-03-05"
draft: false
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Recuperar privilegios del documento PDF usando Aspose.PDF for Python
Abstract: Los documentos PDF pueden tener restricciones de seguridad que limitan acciones como imprimir, copiar, modificar o rellenar formularios. Al acceder a estos privilegios programáticamente, los desarrolladores pueden determinar qué operaciones están permitidas en un PDF. Esta guía muestra cómo usar la clase PdfFileInfo para recuperar los privilegios del documento PDF y mostrarlos en Python.
---

Los privilegios PDF controlan lo que los usuarios pueden y no pueden hacer con un documento. Los permisos comunes incluyen:

- Impresión del documento
- Copiar contenido
- Modificar anotaciones o contenidos
- Rellenar campos de formulario
- Usar lectores de pantalla
- Ensambla o fusiona documentos

Con Aspose.PDF for Python, puedes inspeccionar estas configuraciones programáticamente usando el [PdfFileInfo](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileinfo/) clase. Esto es especialmente útil al trabajar con múltiples PDF en flujos de trabajo automatizados, verificando el cumplimiento o controlando el manejo de documentos en aplicaciones.

1. Cargar un archivo PDF.
1. Recuperar sus privilegios de documento.
1. Mostrar qué acciones están permitidas para el documento.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
from io import FileIO

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def get_document_privileges(input_file_name):
    pdf_metadata = pdf_facades.PdfFileInfo(input_file_name)

    privileges = pdf_metadata.get_document_privilege()

    print("Document Privileges:")
    print(f"  Can Print: {privileges.allow_print}")
    print(f"  Can Degraded Print: {privileges.allow_degraded_printing}")
    print(f"  Can Copy: {privileges.allow_copy}")
    print(f"  Can Modify Contents: {privileges.allow_modify_contents}")
    print(f"  Can Modify Annotations: {privileges.allow_modify_annotations}")
    print(f"  Can Fill In: {privileges.allow_fill_in}")
    print(f"  Can Screen Readers: {privileges.allow_screen_readers}")
    print(f"  Can Assembly: {privileges.allow_assembly}")
```
