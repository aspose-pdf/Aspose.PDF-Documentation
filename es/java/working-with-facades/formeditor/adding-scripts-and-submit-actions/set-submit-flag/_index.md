---
title: Establecer bandera de envío
linktitle: Establecer bandera de envío
type: docs
weight: 40
url: /es/java/set-submit-flag/
description: Revisar la cobertura actual de Java para establecer una bandera de envío en un botón de formulario PDF con la fachada FormEditor en Aspose.PDF.
lastmod: "2026-09-03"
TechArticle: true
AlternativeHeadline: Configuración de la bandera de envío en ejemplos de FormEditor en Java
Abstract: El conjunto de muestras actual de Java no expone la configuración de la bandera de envío como un método de ejemplo independiente. En su lugar, se demuestra junto con la configuración de la URL de envío en `setSubmitUrl(...)`.
---
El Java `FormEditorExamples.setSubmitUrl(...)` método incluye:

## Configurar una bandera de envío

1. Vincula el PDF de origen al `FormEditor` fachada.
2. Establece la URL de envío para el campo de botón.
3. Establece la bandera de envío para el formato requerido.
4. Guarda el documento actualizado.

```java
editor.setSubmitUrl("Script_Demo_Button", "http://www.example.com/submit");
editor.setSubmitFlag("Script_Demo_Button", SubmitFormFlag.Xfdf);
```

Utilice ese ejemplo combinado como el flujo de trabajo Java respaldado por origen para configurar una bandera de envío en este repositorio.
