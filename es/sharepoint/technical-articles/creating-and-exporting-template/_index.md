---
title: Crear y Exportar Plantilla
linktitle: Crear y Exportar Plantilla
type: docs
weight: 10
url: /es/sharepoint/creating-and-exporting-template/
lastmod: "2026-09-09"
description: Puede crear y exportar plantillas a PDF en SharePoint usando la API PDF SharePoint.
---

{{% alert color="primary" %}}

Este artículo muestra cómo crear y exportar plantillas usando Aspose.PDF for SharePoint.

A partir de Aspose.PDF for SharePoint 1.9.2, la compatibilidad con plantillas PDF también cubre los subsitios de SharePoint.

{{% /alert %}}

## Crear y Exportar Plantillas

{{% alert color="primary" %}}

Para usar la función de exportación de Aspose.PDF for SharePoint, primero cree una lista que utilice “PDF Templates”.

Crear una lista que utilice PDF Templates:

![Crear Lista de Plantillas PDF](creating-and-exporting-template_1.png)

Se crean dos plantillas de documento, Task Form Templates y Task List Templates:

![Plantillas de Documentos](creating-and-exporting-template_2.png)

El formulario de plantilla le permite ingresar la siguiente información:

- **Name**: el nombre de archivo de la plantilla.
- **Title**: el título de la plantilla. (Por defecto, el mismo que el nombre de archivo.)
- **Description**: una descripción de la plantilla. Una buena descripción hace que la plantilla sea más fácil de usar.
- **Assigned List Types**: IDs de lista separados por comas (relacionados con la plantilla. Este campo también puede contener el valor
- **AllListTypes**. Este campo solo es aplicable cuando el campo **Type** está configurado como **List**).
- **Assigned Content Types**: IDs de tipos de contenido separados por comas relacionados con la plantilla. Este campo puede establecerse en **AllListTypes**. Este campo solo es aplicable cuando el campo **Type** está configurado como **Item**.
- **Type**: ya sea una plantilla de lista o una plantilla de elemento.
- **Status**: las opciones son activo, inactivo (invisible para todos) y depuración (visible solo para administradores).

El formulario Task List Templates:

![Plantillas de lista de tareas](creating-and-exporting-template_3.png)

El formulario Task Form Templates:

![Plantillas de formularios de tareas](creating-and-exporting-template_4.png)

Cuando se han guardado, las nuevas plantillas aparecen en la lista de plantillas, listas para ser usadas:

Dos plantillas de lista de tareas:*

![Plantillas de lista de tareas](creating-and-exporting-template_5.png)

Una plantilla de formularios de tarea:

![Plantillas de formularios de tareas](creating-and-exporting-template_6.png)

### Desarrollo de plantillas

Una plantilla es un archivo XML basado en Aspose XML PDF. Para crear una plantilla para una lista, coloque marcadores especiales relacionados con el nombre interno del campo del tipo de contenido objetivo de SharePoint en el archivo XML PDF.

### Marcadores

- **SPListItemsCount** – reemplazado por el recuento de elementos de la lista.
- **SPListTitle** – reemplazado por el título de la lista.
- **SPTableIterator** – colocado en la primera celda de la tabla y marca la tabla para una iteración completa.
- **SPRowIterator** – colocado en la primera celda de la tabla y marca la tabla para la iteración de filas.
- **SPField** – reemplazado por el valor del campo del elemento.

Para referencia, por favor descargue [template XML files](attachments/8421394/8618082.zip).

### Exportar a PDF

Cuando una plantilla está completamente configurada, estás listo para exportar listas o elementos a archivos PDF.

Exportando una lista a PDF usando una plantilla de lista de tareas:

![Exportar a PDF](creating-and-exporting-template_7.png)

{{% /alert %}}
