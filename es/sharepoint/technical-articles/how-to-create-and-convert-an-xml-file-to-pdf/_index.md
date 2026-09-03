---
title: Cómo crear y convertir un archivo XML a PDF
linktitle: Cómo crear y convertir un archivo XML a PDF
type: docs
weight: 30
url: /es/sharepoint/how-to-create-and-convert-an-xml-file-to-pdf/
lastmod: "2020-12-16"
description: PDF SharePoint API es capaz de crear y convertir archivos XML a formato PDF.
---

{{% alert color="primary" %}}

Aspose.PDF for SharePoint is built on top of our award winning Aspose.PDF for .NET component. Aspose.PDF for .NET provides remarkable features from the creation of PDF document from scratch to manipulation of existing PDF files. Among these features, XML to PDF conversion is one of the great features support by this product. So we believe that Aspose.PDF for SharePoint will also be capable of converting XML files into PDF format.

{{% /alert %}}

## Creación de un archivo XML y su conversión a PDF.

{{% alert color="primary" %}}

Paso a paso, este artículo lo guía a través del proceso de creación de un archivo XML y su conversión a PDF:

1. [Crear un archivo XML](/pdf/es/sharepoint/how-to-create-and-convert-an-xml-file-to-pdf/#step-1-create-xml-file).
2. [Crear una plantilla PDF](/pdf/es/sharepoint/how-to-create-and-convert-an-xml-file-to-pdf/#step-2-create-pdf-template).
3. [Cargue la plantilla XML](/pdf/es/sharepoint/how-to-create-and-convert-an-xml-file-to-pdf/#step-3-load-xml-template).
4. [Especifique la ruta a la ruta de origen](/pdf/es/sharepoint/how-to-create-and-convert-an-xml-file-to-pdf/#step-4-specify-source-file-path).
5. [Especificar propiedades del archivo](/pdf/es/sharepoint/how-to-create-and-convert-an-xml-file-to-pdf/#step-5-specify-file-properties).
6. [Exportar el archivo a PDF](/pdf/es/sharepoint/how-to-create-and-convert-an-xml-file-to-pdf/#step-6-export-to-pdf).
7. [Guarde el archivo PDF](/pdf/es/sharepoint/how-to-create-and-convert-an-xml-file-to-pdf/#step-7-save-pdf-document)

### Paso 1: crear un archivo XML

Primero, cree un archivo XML basado en el modelo de objetos de documento Aspose.PDF for .NET.

Según Aspose.PDF para .NET DOM, un documento PDF contiene una colección de objetos de Sección y una Sección contiene uno o más elementos de Párrafo. El texto es un objeto de nivel de párrafo y puede contener uno o más segmentos. A continuación, se agrega una cadena de texto de muestra a un objeto Segmento y se agrega a un objeto Texto. Finalmente, el elemento Texto se agrega a la colección de párrafos del objeto Sección.

```xml

<?xml version="1.0" encoding="utf-8" ?>

  <Pdf xmlns="Aspose.PDF">

   <Section>

    <Text>

            <Segment>Hello World</Segment>

    </Text>

   </Section>

  </Pdf>

```

### Paso 2: crear una plantilla PDF

Antes de continuar, asegúrese de que el servidor SharePoint Foundation 2010 esté correctamente instalado y configurado en el sistema donde se realizará la conversión.

1. Inicie sesión en el sitio de SharePoint.
1. Seleccione **Acción del sitio** y **Todos los elementos**.
1. Seleccione la opción **Crear** y seleccione **Plantilla PDF** de la lista.
1. Introduzca un nombre de plantilla.
1. Haga clic en **Crear**.

![Create PDF Template](how-to-create-and-convert-an-xml-file-to-pdf_1.png)

### Paso 3: cargar la plantilla XML

Una vez creada la plantilla, cargue [el archivo XML](/pdf/es/sharepoint/how-to-create-and-convert-an-xml-file-to-pdf/)

1. En la página de la plantilla PDF, seleccione **Agregar nuevo elemento**.

![Load XML Template](how-to-create-and-convert-an-xml-file-to-pdf_2.png)

### Paso 4: especificar la ruta del archivo fuente

En el cuadro de diálogo de carga de documentos:

1. Haga clic en **Examinar** y busque el archivo XML en su sistema. Puede habilitar la casilla de verificación para sobrescribir la opción de archivo existente.
1. Presione el botón **Aceptar**.

![Specify Source File Path](how-to-create-and-convert-an-xml-file-to-pdf_3.png)

### Paso 5: especificar las propiedades del archivo

Cuando el archivo esté cargado, agregue información en los campos obligatorios (marcados con un asterisco rojo: *).

Para este ejemplo, se agregó una descripción de muestra y se completaron los siguientes campos:

1. Una breve descripción del documento.
1. Ingrese **AllListTypes** para el campo **Tipos de lista asignados**.
1. Seleccione **Lista** en el menú **Tipo**.
   Asegúrese de que el estado permanezca **Activo**.
1. Haga clic en **Guardar** para guardar las propiedades.

![Specify File Properties](how-to-create-and-convert-an-xml-file-to-pdf_4.png)

### Paso 6: Exportar a PDF

Cuando el archivo XML se haya agregado a la plantilla PDF:
Cualquiera:

1. Haga clic derecho en el archivo test.xml.
1. Seleccione **Exportar a PDF** en el menú.

O:

1. Seleccione **Herramientas Aspose** de **Herramientas de biblioteca**.
1. Haga clic en **Exportar**.

![Export to PDF](how-to-create-and-convert-an-xml-file-to-pdf_5.png)

### Paso 7: guarde el documento PDF

1. En el cuadro de diálogo Exportar a PDF, seleccione **Almacenamiento de plantilla** (la ubicación donde se almacena el archivo fuente).
1. Seleccione el archivo para exportar desde el menú **Nombre de plantilla**.
1. Haga clic en **Exportar a PDF** para guardar el documento PDF final.

![Save PDF Document](how-to-create-and-convert-an-xml-file-to-pdf_6.png)

## Abre el PDF

El documento PDF se ha guardado y se puede abrir. En la imagen siguiente, observe la frase "Hello World" que estaba en la etiqueta de segmento en el XML. También tenga en cuenta que el productor de PDF es Aspose.PDF for SharePoint.

![Open the PDF](how-to-create-and-convert-an-xml-file-to-pdf_7.png)

{{% /alert %}}

