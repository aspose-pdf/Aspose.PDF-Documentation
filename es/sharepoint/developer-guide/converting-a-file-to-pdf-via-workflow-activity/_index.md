---
title: Convirtiendo un archivo a PDF mediante una actividad de flujo de trabajo
linktitle: Convirtiendo un archivo a PDF mediante una actividad de flujo de trabajo
type: docs
weight: 50
url: /es/sharepoint/converting-a-file-to-pdf-via-workflow-activity/
lastmod: "2026-09-09"
description: La API PDF SharePoint se puede usar en un flujo de trabajo de SharePoint que convierte un documento a PDF.
---

{{% alert color="primary" %}}

El soporte para flujos de trabajo es una funcionalidad clave de Microsoft Office SharePoint Server. Los flujos de trabajo ayudan a automatizar el movimiento de documentos según la lógica empresarial y a optimizar el costo y el tiempo de la organización de documentos. Este artículo muestra cómo usar Aspose.PDF for SharePoint en un flujo de trabajo que convierte un documento a PDF.

{{% /alert %}}

## Configuración de un flujo de trabajo

Este ejemplo crea un flujo de trabajo que convierte cualquier elemento nuevo en una biblioteca de documentos al formato PDF y lo almacena en otra biblioteca de documentos. El ejemplo utiliza la biblioteca **Personal Documents** como la biblioteca de origen y la subcarpeta **Pdf** en la biblioteca **Shared Documents** como la biblioteca de destino.

Aspose.PDF for SharePoint admite la conversión de archivos HTML, de texto y de imagen.

### Diseña el flujo de trabajo usando SharePoint Designer

1. Abre **SharePoint Designer** y conéctate al sitio donde se implementará el flujo de trabajo.
1. Selecciona **Workflows** de **site objects** y luego abre **List Workflow**.
1. Selecciona la biblioteca **Personal Documents** para crear y adjuntar un nuevo flujo de trabajo de lista a la biblioteca de documentos.

   **Selecting Personal Documents from the menu**

![Convirtiendo archivo a PDF mediante la actividad de flujo de trabajo_1](converting-a-file-to-pdf-via-workflow-activity_1.png)

1. Cree y adjunte el flujo de trabajo de lista a la biblioteca **Personal Documents** escribiendo un nombre y una descripción para el flujo de trabajo.
1. Haga clic en **OK** para completar este paso.

   **Creating a list workflow**

![Convirtiendo archivo a PDF mediante la actividad de flujo de trabajo_2](converting-a-file-to-pdf-via-workflow-activity_2.png)

Aparece un editor de pasos de flujo de trabajo. Se utiliza para definir condiciones y acciones para los flujos de trabajo. Ahora añada una acción para convertir un nuevo documento a PDF sin ninguna condición, desde **Aspose Actions**.

1. Seleccione la acción **Convert file to PDF via Aspose.PDF** del menú **Action**.

   **Selecting and action**

![Convirtiendo archivo a PDF vía Workflow Activity_3](converting-a-file-to-pdf-via-workflow-activity_3.png)

1. Configure los parámetros de la acción:
   1. Establezca el parámetro **this folder** a la carpeta de destino.
   1. Deje los demás parámetros de la acción con sus valores predeterminados o configúrelos mediante la ventana de propiedades de la acción. El valor predeterminado del parámetro **Overwrite** es false.

      **The Workflow Editor**

![Convirtiendo el archivo a PDF mediante Workflow Activity_4](converting-a-file-to-pdf-via-workflow-activity_4.png)

**Setting the destination library**

![Convirtiendo el archivo a PDF mediante Workflow Activity_5](converting-a-file-to-pdf-via-workflow-activity_5.png)

**Setting the properties**

![Convertir archivo a PDF mediante la actividad de flujo de trabajo_6](converting-a-file-to-pdf-via-workflow-activity_6.png)

1. Desde el menú **Workflow**, seleccione **Workflow Settings**.
1. Seleccione **start workflow automatically when a new item created** y desmarque otras opciones de **Start Options**.

   **Setting the start options**

![Convertir archivo a PDF mediante la actividad de flujo de trabajo_7](converting-a-file-to-pdf-via-workflow-activity_7.png)

El diseño del flujo de trabajo ha finalizado.

1. Guarde y publique el flujo de trabajo para implementarlo en el sitio de SharePoint.

### Probar el flujo de trabajo

Para probar el flujo de trabajo:

1. Abra el sitio de SharePoint y cargue un nuevo documento en la biblioteca de documentos **Personal Documents**.
   Aspose.PDF for SharePoint admite la conversión de archivos HTML, archivos de texto y imágenes (JPG, PNG, GIF, TIFF y BMP*) a PDF. El flujo de trabajo está configurado para iniciarse automáticamente cuando se crea un nuevo elemento, por lo que los archivos se procesan automáticamente.
1. Actualice el navegador.
   El estado del flujo de trabajo aparece en la columna de flujo de trabajo, **Aspose.PDF Workflow** en este caso.

   **Adding a document to the source library**

![Convirtiendo archivo a PDF mediante Workflow Activity_8](converting-a-file-to-pdf-via-workflow-activity_8.png)

1. Abra la biblioteca de documentos de destino para ver el documento convertido. **Shared Documents/Pdf** es la ruta en este ejemplo.

   **The destination library**

![Convirtiendo archivo a PDF mediante Workflow Activity_9](converting-a-file-to-pdf-via-workflow-activity_9.png)
