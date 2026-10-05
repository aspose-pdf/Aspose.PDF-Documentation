---
title: Establecer bandera de envío
linktitle: Establecer bandera de envío
type: docs
weight: 40
url: /es/java/set-submit-flag/
description: Revise la cobertura actual de Java para establecer una bandera de envío en un botón de formulario PDF con la fachada FormEditor en Aspose.PDF.
lastmod: "2026-09-28"
TechArticle: true
AlternativeHeadline: Configuración de la bandera de envío en ejemplos de FormEditor Java
Abstract: El conjunto actual de ejemplos en Java no expone la configuración de la bandera de envío como un método de ejemplo independiente. En su lugar, se muestra junto con la configuración de la URL de envío en `setSubmitUrl(...)`.
---
El Java `FormEditorExamples.setSubmitUrl(...)` el método incluye:

## Configurar una bandera de envío

1. Vincule el PDF de origen a la fachada `FormEditor`.
2. Establezca la URL de envío para el campo del botón.
3. Establezca el indicador de envío para el formato requerido.
4. Guarde el documento actualizado.

```java
editor.setSubmitUrl("Script_Demo_Button", "http://www.example.com/submit");
editor.setSubmitFlag("Script_Demo_Button", SubmitFormFlag.Xfdf);
```

Utilice ese ejemplo combinado como el flujo de trabajo Java respaldado por el código fuente para configurar una bandera de envío en este repositorio.
