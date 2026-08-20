---
title: Establecer bandera de envío
linktitle: Establecer bandera de envío
type: docs
weight: 40
url: /java/set-submit-flag/
description: Revise la cobertura actual de Java para configurar un indicador de envío en un botón de formulario PDF con la fachada FormEditor en Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Enviar configuración de indicador en ejemplos de Java FormEditor
Abstract: El conjunto de muestra de Java actual no expone la configuración de envío de bandera como un método de ejemplo independiente. En cambio, se demuestra junto con la configuración de envío de URL en `setSubmitUrl(...)`.
---
El método Java `FormEditorExamples.setSubmitUrl(...)` incluye:


## 
Configurar una bandera de envío


1. 
Vincule el PDF de origen a la fachada `FormEditor`.

2. 
Establezca la URL de envío para el campo del botón.

3. 
Establezca el indicador de envío para el formato requerido.
4. Guarde el documento actualizado.


```java
editor.setSubmitUrl("Script_Demo_Button", "http://www.example.com/submit");
editor.setSubmitFlag("Script_Demo_Button", SubmitFormFlag.Xfdf);
```


Utilice ese ejemplo combinado como flujo de trabajo Java respaldado por el código fuente para configurar un indicador de envío en este repositorio.
