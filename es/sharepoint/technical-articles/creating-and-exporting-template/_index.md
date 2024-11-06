---
title: Creación y Exportación de Plantillas
type: docs
weight: 10
url: es/sharepoint/creating-and-exporting-template/
lastmod: "2020-12-16"
description: Puede crear y exportar plantillas a PDF en SharePoint utilizando la API de PDF para SharePoint.
---

{{% alert color="primary" %}}

Este artículo muestra cómo crear y exportar plantillas utilizando Aspose.PDF para SharePoint.

A partir de Aspose.PDF para SharePoint 1.9.2, el soporte de plantillas PDF también cubre subsitios de SharePoint.

{{% /alert %}}

## **Creación y Exportación de Plantillas**
{{% alert color="primary" %}}

Para usar la función de exportación de Aspose.PDF para SharePoint, primero cree una lista que use "Plantillas PDF".

Creación de una lista que use Plantillas PDF:

![todo:image_alt_text](creating-and-exporting-template_1.png)

Se crean dos plantillas de documento, Plantillas de Formulario de Tarea y Plantillas de Lista de Tareas:

![todo:image_alt_text](creating-and-exporting-template_2.png)

El formulario de plantilla le permite ingresar la siguiente información:

- **Name**: el nombre de archivo de la plantilla.
- **Title**: el título de la plantilla.
 - **Descripción**: una descripción de la plantilla. Una buena descripción hace que la plantilla sea más fácil de usar.
- **Tipos de Lista Asignados**: IDs de listas separados por comas (relacionados con la plantilla. Este campo también puede contener el valor **AllListTypes**. Este campo solo es aplicable cuando el campo **Type** está configurado en **List**).
- **Tipos de Contenido Asignados**: IDs de tipos de contenido separados por comas (relacionados con la plantilla. Este campo puede estar configurado en **AllListTypes**. Este campo solo es aplicable cuando el campo **Type** está configurado en **Item**.
- **Type**: plantilla de lista o plantilla de elemento.
- **Status**: las opciones son activo, inactivo (invisible para todos) y depuración (visible solo para administradores).

**El formulario de Plantillas de Lista de Tareas:**

![todo:texto_alt_de_imagen](creating-and-exporting-template_3.png)

**El formulario de Plantillas de Formulario de Tareas:**

![todo:texto_alt_de_imagen](creating-and-exporting-template_4.png)

Cuando se han guardado, las nuevas plantillas aparecen en la lista de plantillas, listas para ser usadas:

**Dos plantillas de lista de tareas:**
![todo:image_alt_text](creating-and-exporting-template_5.png)

**Una plantilla de formularios de tareas:**

![todo:image_alt_text](creating-and-exporting-template_6.png)

#### **Desarrollo de Plantillas**
Una plantilla es un archivo XML basado en Aspose XML PDF. Para crear una plantilla para una lista, coloca marcadores especiales relacionados con el nombre interno del campo del tipo de contenido de destino de SharePoint en el archivo XML PDF.
##### **Marcadores**
- **SPListItemsCount** – reemplazado por el conteo de elementos de la lista.
- **SPListTitle** – reemplazado por el título de la lista.
- **SPTableIterator** – colocado en la primera celda de la tabla y marca la tabla para una iteración completa.
- **SPRowIterator** – colocado en la primera celda de la tabla y marca la tabla para la iteración de filas.
- **SPField** – reemplazado por el valor del campo del elemento.

Para referencia, por favor descarga [archivos XML de plantillas](attachments/8421394/8618082.zip).
#### **Exportar a PDF**
Cuando una plantilla está completamente configurada, estás listo para exportar listas o elementos a archivos PDF.

**Exportar una lista a PDF usando una plantilla de lista de tareas:**
![todo:image_alt_text](creating-and-exporting-template_7.png)

{{% /alert %}}