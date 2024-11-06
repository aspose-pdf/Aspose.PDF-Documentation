---
title: Trabajando con AcroForms en PDF 
linktitle: AcroForms
type: docs
weight: 10
url: es/java/acroforms/
description: Con Aspose.PDF para Java puedes crear un formulario desde cero, llenar el campo del formulario en un documento PDF, extraer datos del formulario, agregar o eliminar campos en el formulario existente.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Fundamentos de AcroForms

**AcroForms** son la tecnología original de formularios PDF. AcroForms es un formulario orientado a la página. Fueron introducidos por primera vez en 1998. Aceptan entrada en Formato de Datos de Formularios o FDF y Formato de Datos de Formularios XML o xFDF. Proveedores de terceros soportan AcroForms. Cuando Adobe introdujo los AcroForms, se referían a ellos como "formulario PDF que se crea con Adobe Acrobat Pro/Standard y que no es un tipo especial de formulario XFA estático o dinámico". Los Acroforms son portátiles y funcionan en todas las plataformas.

Puedes usar AcroForms para agregar páginas adicionales al documento de formulario PDF.
 Gracias al concepto de Plantillas, puedes usar AcroForms para soportar la población del formulario con múltiples registros de base de datos.

PDF 1.7 admite dos métodos diferentes para integrar datos y formularios PDF.

*AcroForms (también conocidos como formularios Acrobat)*, introducidos e incluidos en la especificación del formato PDF 1.2.

*Formularios de Arquitectura de Formularios XML de Adobe (XFA)*, introducidos en la especificación del formato PDF 1.5 como una característica opcional (La especificación XFA no está incluida en la especificación PDF, solo es referenciada).

Para entender **Acroforms** vs formularios **XFA**, necesitamos entender los conceptos básicos primero. Para empezar, ambos son formularios PDF que puedes usar. Acroforms es el más antiguo, creado en 1998, y todavía se le refiere como el formulario PDF clásico. Los formularios XFA son páginas web que puedes guardar como un PDF, y aparecieron en 2003. Pasó algún tiempo antes de que PDF comenzara a aceptar formularios XFA.

AcroForms tienen capacidades no encontradas en XFA y, a su vez, XFA tiene algunas capacidades no encontradas en AcroForms. Por ejemplo:

- AcroForms soportan el concepto de "Plantillas", permitiendo que se añadan páginas adicionales al documento de formulario PDF para soportar la población del formulario con múltiples registros de base de datos.- XFA admite el concepto de reflujo de documentos que permite que un campo cambie de tamaño si es necesario para acomodar los datos.

Por lo tanto, los PDFs son el mejor formato de archivo para formularios, ya que se pueden distribuir electrónicamente y tener la información completada dentro del documento y enviada de vuelta al remitente sin necesidad de imprimir o enviar por correo tradicional.

Para un estudio más detallado de las posibilidades de trabajar con formularios, estudie los siguientes artículos en la sección:

-[Crear AcroForm](/pdf/java/create-form/) - crear formulario desde cero, agregando RadioButtonField, TextBoxField, Caption Field usando Java.

-[Rellenar AcroForm](/pdf/java/fill-form/) - para llenar un campo de formulario, obtenga el campo de la colección de Formularios del objeto Document.

-[Extraer Datos AcroForm](/pdf/java/extract-form/) - obtener valores de todos y cada uno de los campos, etc.

-[Modificar AcroForm](/pdf/java/modifing-form/) - obtener/establecer FieldLimit, eliminar campos en un formulario existente, establecer la fuente del campo del formulario diferente a las 14 fuentes principales de PDF con Java.