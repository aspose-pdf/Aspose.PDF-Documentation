---

title: Converting a File to PDF via Workflow Activity  
type: docs  
weight: 50  
url: es/sharepoint/converting-a-file-to-pdf-via-workflow-activity/  
lastmod: "2020-12-16"  
description: PDF SharePoint API can be used in a SharePoint workflow that converts a document to PDF.  

---

{{% alert color="primary" %}}

El soporte para flujos de trabajo es una funcionalidad clave de Microsoft Office SharePoint Server. Los flujos de trabajo ayudan a automatizar el movimiento de documentos de acuerdo con la lógica empresarial y optimizan el costo y tiempo de organización de documentos. Este artículo demuestra cómo usar Aspose.PDF para SharePoint en un flujo de trabajo que convierte un documento a PDF.

{{% /alert %}}

## **Configuración de un Flujo de Trabajo**

Este ejemplo crea un flujo de trabajo que convierte cualquier nuevo elemento en una biblioteca de documentos al formato PDF y lo almacena en otra biblioteca de documentos. El ejemplo utiliza la biblioteca **Documentos Personales** como la biblioteca de origen y la subcarpeta **Pdf** en la biblioteca **Documentos Compartidos** como la biblioteca de destino.

Aspose.PDF para SharePoint admite la conversión de archivos HTML, de texto e imágenes.

### **Diseñar el Flujo de Trabajo usando SharePoint Designer**

1. Abre **SharePoint Designer** y conéctate al sitio donde se implementará el flujo de trabajo.
1. Selecciona **Workflows** de **site objects** y luego abre **List Workflow**.
1. Selecciona la biblioteca **Personal Documents** para crear y adjuntar un nuevo flujo de trabajo de lista a la biblioteca de documentos.

   **Seleccionando Personal Documents del menú**

![todo:image_alt_text](converting-a-file-to-pdf-via-workflow-activity_1.png)


1. Crea y adjunta el flujo de trabajo de lista a la biblioteca **Personal Documents** escribiendo un nombre y descripción del flujo de trabajo.
1. Haz clic en **OK** para completar este paso.

   **Creando un flujo de trabajo de lista**

![todo:image_alt_text](converting-a-file-to-pdf-via-workflow-activity_2.png)



Aparece un editor de pasos de flujo de trabajo. Este se usa para definir condiciones y acciones para los flujos de trabajo. Ahora agrega una acción para convertir un nuevo documento a PDF sin ninguna condición, desde **Aspose Actions**.
1. Seleccione la acción **Convertir archivo a PDF a través de Aspose.PDF** del menú **Acción**.

   **Seleccionando una acción**

![todo:image_alt_text](converting-a-file-to-pdf-via-workflow-activity_3.png)


1. Configure los parámetros de la acción:
   1. Establezca el parámetro **esta carpeta** en la carpeta de destino.
   1. Deje los otros parámetros de la acción con los valores predeterminados o configúrelos usando la ventana de propiedades de la acción. El valor predeterminado para el parámetro **Sobrescribir** es falso.

      **El Editor de Flujos de Trabajo**

![todo:image_alt_text](converting-a-file-to-pdf-via-workflow-activity_4.png)



**Estableciendo la biblioteca de destino**

![todo:image_alt_text](converting-a-file-to-pdf-via-workflow-activity_5.png)



**Estableciendo las propiedades**

![todo:image_alt_text](converting-a-file-to-pdf-via-workflow-activity_6.png)




1. Desde el menú **Flujo de Trabajo**, seleccione **Configuración del Flujo de Trabajo**.
1. Seleccione **iniciar flujo de trabajo automáticamente cuando se crea un nuevo elemento** y desmarque otras opciones en **Opciones de Inicio**.

   **Estableciendo las opciones de inicio**
![todo:image_alt_text](converting-a-file-to-pdf-via-workflow-activity_7.png)

El diseño del flujo de trabajo está terminado.

1. Guarda y publica el flujo de trabajo para implementarlo en el sitio de SharePoint.

### **Probar el Flujo de Trabajo**

Para probar el flujo de trabajo:

1. Abre el sitio de SharePoint y sube un nuevo documento a la biblioteca de documentos **Documentos Personales**. Aspose.PDF para SharePoint soporta la conversión de archivos HTML, archivos de texto e imágenes (JPG, PNG, GIF, TIFF y BMP*) a PDF. El flujo de trabajo está configurado para comenzar automáticamente cuando se crea un nuevo elemento, por lo que los archivos se procesan automáticamente.
1. Actualiza el navegador.
   El estado del flujo de trabajo aparece en la columna de flujo de trabajo, **Aspose.PDF Workflow** en este caso.

   **Agregar un documento a la biblioteca de origen**

![todo:image_alt_text](converting-a-file-to-pdf-via-workflow-activity_8.png)

1. Abre la biblioteca de documentos de destino para ver el documento convertido. **Documentos Compartidos/Pdf** es la ruta en este ejemplo.

   **La biblioteca de destino**
![todo:image_alt_text](converting-a-file-to-pdf-via-workflow-activity_9.png)