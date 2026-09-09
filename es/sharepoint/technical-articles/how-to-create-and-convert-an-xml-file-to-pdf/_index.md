---
title: Cómo crear y convertir un archivo XML a PDF
linktitle: Cómo crear y convertir un archivo XML a PDF
type: docs
weight: 30
url: /es/sharepoint/how-to-create-and-convert-an-xml-file-to-pdf/
lastmod: "2026-09-09"
description: La API PDF SharePoint es capaz de crear y convertir archivos XML al formato PDF.
---

{{% alert color="primary" %}}

Aspose.PDF for SharePoint está construido sobre nuestro galardonado componente Aspose.PDF for .NET. Aspose.PDF for .NET ofrece características notables, desde la creación de documentos PDF desde cero hasta la manipulación de archivos PDF existentes. Entre estas características, la conversión de XML a PDF es una de las grandes funcionalidades admitidas por este producto. Por lo tanto, creemos que Aspose.PDF for SharePoint también será capaz de convertir archivos XML a formato PDF.

{{% /alert %}}

## Crear un archivo XML y convertirlo a PDF

{{% alert color="primary" %}}

Paso a paso, este artículo le guía a través del proceso de crear un archivo XML y convertirlo a PDF:

1. [Crear un archivo XML](/pdf/es/sharepoint/how-to-create-and-convert-an-xml-file-to-pdf/#step-1-create-xml-file).
2. [Crear una plantilla PDF](/pdf/es/sharepoint/how-to-create-and-convert-an-xml-file-to-pdf/#step-2-create-pdf-template).
3. [Cargar la plantilla XML](/pdf/es/sharepoint/how-to-create-and-convert-an-xml-file-to-pdf/#step-3-load-xml-template).
4. [Especificar la ruta de origen](/pdf/es/sharepoint/how-to-create-and-convert-an-xml-file-to-pdf/#step-4-specify-source-file-path).
5. [Especificar las propiedades del archivo](/pdf/es/sharepoint/how-to-create-and-convert-an-xml-file-to-pdf/#step-5-specify-file-properties).
6. [Exportar el archivo a PDF](/pdf/es/sharepoint/how-to-create-and-convert-an-xml-file-to-pdf/#step-6-export-to-pdf).
7. [Guardar el archivo PDF](/pdf/es/sharepoint/how-to-create-and-convert-an-xml-file-to-pdf/#step-7-save-pdf-document)

### Paso 1: Crear archivo XML

Primero crea un archivo XML basado en el modelo de objetos de documento de Aspose.PDF for .NET.

Según el DOM de Aspose.PDF for .NET, un documento PDF contiene una colección de objetos Section, y una Section contiene uno o más elementos Paragraph. Text es un objeto a nivel de Paragraph y puede contener uno o más segmentos. A continuación, una cadena de texto de ejemplo se agrega a un objeto Segment y se agrega a un objeto Text. Finalmente, el elemento Text se agrega a la colección de párrafos del objeto Section.

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

### Paso 2: Crear plantilla PDF

Antes de continuar, asegúrese de que el servidor SharePoint Foundation 2010 esté instalado y configurado correctamente en el sistema donde se realizará la conversión.

1. Inicie sesión en el sitio de SharePoint.
1. Seleccione **Site Action** y **All Items**.
1. Seleccione la opción **Create** y seleccione **PDF Template** de la lista.
1. Introduzca un nombre de plantilla.
1. Haga clic en **Create**.

![Crear PDF Template](how-to-create-and-convert-an-xml-file-to-pdf_1.png)

### Paso 3: Cargar plantilla XML

Una vez que la plantilla se ha creado, cargue [the XML file](/pdf/es/sharepoint/how-to-create-and-convert-an-xml-file-to-pdf/)

1. En la página de la plantilla PDF, seleccione **Add new item**.

![Cargar plantilla XML](how-to-create-and-convert-an-xml-file-to-pdf_2.png)

### Paso 4: Especificar la ruta del archivo fuente

En el cuadro de diálogo de carga de documentos:

1. Haga clic en **Browse** y localice el archivo XML en su sistema. Puede habilitar la casilla de verificación para sobrescribir la opción de archivo existente.
1. Presione el botón **OK**.

![Especifique la ruta del archivo de origen](how-to-create-and-convert-an-xml-file-to-pdf_3.png)

### Paso 5: Especifique las propiedades del archivo

Cuando se cargue el archivo, agregue información en los campos obligatorios (marcados con un asterisco rojo: *).

Para este ejemplo, se había añadido una descripción de muestra y se completaron los siguientes campos:

1. Una breve descripción del documento.
1. Introduzca **AllListTypes** en el campo **Assigned List Types**.
1. Seleccione **List** del menú **Type**.
   Asegúrese de que el estado permanezca **Active**.
1. Haga clic en **Save** para guardar las propiedades.

![Especifique las propiedades del archivo](how-to-create-and-convert-an-xml-file-to-pdf_4.png)

### Paso 6: Exportar a PDF

Cuando se ha añadido el archivo XML a la plantilla PDF:
O bien:

1. Haz clic derecho en el archivo test.xml.
1. Selecciona **Export to PDF** en el menú.

O:

1. Selecciona **Aspose Tools** del **Library Tools**.
1. Haz clic en **Export**.

![Exportar a PDF](how-to-create-and-convert-an-xml-file-to-pdf_5.png)

### Paso 7: Guardar documento PDF

1. En el cuadro de diálogo Exportar a PDF, selecciona **Template storage** (la ubicación donde se almacena el archivo origen).
1. Selecciona el archivo a exportar desde el menú **Template name**.
1. Haz clic en **Export to PDF** para guardar el documento PDF final.

![Guardar documento PDF](how-to-create-and-convert-an-xml-file-to-pdf_6.png)

## Abrir el PDF

El documento PDF ha sido guardado y puede abrirse. En la imagen siguiente, observe la frase \u0022Hello World\u0022 que estaba en la etiqueta de segmento en el XML. También observe que el productor de PDF es Aspose.PDF for SharePoint.

![Abrir el PDF](how-to-create-and-convert-an-xml-file-to-pdf_7.png)

{{% /alert %}}
