---
title: Trabajando con Formularios XFA en PDF
linktitle: Formularios XFA
type: docs
weight: 20
url: es/java/xfa-forms/
description: Con Aspose.PDF para Java, puede crear un formulario desde cero, completar el campo del formulario en un documento PDF, extraer datos del formulario, agregar o eliminar campos en el formulario existente.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

XFA significa Arquitectura de Formularios XML. Es un conjunto de especificaciones XML propietarias creadas originalmente para su uso con formularios web en 1999, y desde entonces ha estado disponible para PDF.

## Convertir Formulario XFA Dinámico a AcroForm Estándar

Los formularios dinámicos se basan en una especificación XML conocida como XFA, la “Arquitectura de Formularios XML”. También puede convertir un formulario XFA dinámico a un Acroform estándar. La información sobre el formulario (en lo que respecta a PDF) es muy vaga: especifica que existen campos, con propiedades y eventos de JavaScript, pero no especifica ningún renderizado. Los objetos del formulario XFA se dibujan en el momento de cargar el documento.

Actualmente, PDF admite dos métodos diferentes para integrar datos y formularios PDF:

- AcroForms (también conocidos como formularios Acrobat), introducidos e incluidos en la especificación del formato PDF 1.2.

- Formularios de Adobe XML Forms Architecture (XFA), introducidos en la especificación del formato PDF 1.5 como una característica opcional. (La especificación XFA no está incluida en la especificación PDF, solo se hace referencia a ella.)

No es posible extraer o manipular páginas de formularios XFA, porque el contenido del formulario se genera en tiempo de ejecución (durante la visualización del formulario XFA) dentro de la aplicación que intenta mostrar o renderizar el formulario XFA. Aspose.PDF tiene una función que permite a los desarrolladores convertir formularios XFA a formularios AcroForms estándar.

```java
// Cargar formulario XFA dinámico
Document document = new Document("XFAform.pdf");
// Establecer el tipo de campos del formulario como AcroForm estándar
document.getForm().setType(FormType.Standard);
// Guardar el PDF resultante
document.save("Standard_AcroForm.pdf");
```