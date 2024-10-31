---
title: Trabajando con AcroForms en PDF
linktitle: AcroForms
type: docs
weight: 10
url: /php-java/acroforms/
description: Con Aspose.PDF para PHP a través de Java, puedes crear un formulario desde cero, llenar el campo del formulario en un documento PDF, extraer datos del formulario, agregar o eliminar campos en el formulario existente.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Fundamentos de AcroForms

**AcroForms** son la tecnología original de formularios PDF. AcroForms es un formulario orientado a páginas. Fueron introducidos por primera vez en 1998. Aceptan entrada en el Formato de Datos de Formularios o FDF y en el Formato de Datos de Formularios XML o xFDF. Proveedores de terceros soportan AcroForms. Cuando Adobe introdujo los AcroForms, se refirieron a ellos como “formulario PDF que se crea con Adobe Acrobat Pro/Standard y que no es un tipo especial de formulario XFA estático o dinámico. Los Acroforms son portátiles y funcionan en todas las plataformas.

Puedes usar AcroForms para agregar páginas adicionales al documento del formulario PDF.
 Gracias al concepto de Plantillas, puedes usar AcroForms para apoyar el llenado del formulario con múltiples registros de base de datos.

PDF 1.7 admite dos métodos diferentes para integrar datos y formularios PDF.

*AcroForms (también conocidos como formularios de Acrobat)*, introducidos e incluidos en la especificación de formato PDF 1.2.

*Adobe XML Forms Architecture (XFA) forms*, introducidos en la especificación de formato PDF 1.5 como una característica opcional. La especificación XFA no está incluida en la especificación PDF, solo se hace referencia a ella.

Para entender los formularios **Acroforms** vs **XFA**, primero debemos entender lo básico. Para empezar, ambos son formularios PDF que puedes usar. Acroforms es el más antiguo, creado en 1998, y todavía se refiere como el formulario PDF clásico. Los formularios XFA son páginas web que puedes guardar como un PDF, y aparecieron en 2003. Pasó un tiempo antes que PDF comenzara a aceptar formularios XFA.

AcroForms tiene capacidades no encontradas en XFA y, a su vez, XFA tiene algunas capacidades no encontradas en AcroForms. Por ejemplo:

- AcroForms admite el concepto de "Plantillas", permitiendo que se añadan páginas adicionales al documento del formulario PDF para apoyar el llenado del formulario con múltiples registros de base de datos.- XFA soporta el concepto de reflujo de documentos, permitiendo que un campo cambie de tamaño si es necesario para acomodar los datos.

Por lo tanto, los PDFs son el mejor formato de archivo para formularios ya que pueden ser distribuidos electrónicamente y tener información completada dentro del documento y enviada de vuelta al remitente sin necesidad de imprimir o enviar por correo tradicional.

Para un estudio más detallado de las posibilidades de trabajar con formularios, estudia los siguientes artículos en la sección:

-[Create AcroForm](/pdf/php-java/create-form/) - crear un formulario desde cero, agregando RadioButtonField, TextBoxField, Caption Field usando PHP.

-[Fill AcroForm](/pdf/php-java/fill-form/) - para llenar un campo de formulario, obtener el campo de la colección de formularios del objeto Documento.

-[Extract Data AcroForm](/pdf/php-java/extract-form/) - obtener valores de todos y cada uno de los campos, etc.

-[Modifing AcroForm](/pdf/php-java/modifing-form/) - obtener/establecer FieldLimit, eliminar campos en un formulario existente, establecer la fuente del campo del formulario diferente a las 14 fuentes principales de PDF con PHP.