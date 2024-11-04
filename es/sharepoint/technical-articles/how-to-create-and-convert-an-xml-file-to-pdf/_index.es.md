---
title: Cómo Crear y Convertir un Archivo XML a PDF
type: docs
weight: 30
url: /sharepoint/how-to-create-and-convert-an-xml-file-to-pdf/
lastmod: "2020-12-16"
description: La API de PDF SharePoint es capaz de crear y convertir archivos XML en formato PDF.
---

{{% alert color="primary" %}}

Aspose.PDF para SharePoint está construido sobre nuestro premiado componente Aspose.PDF para .NET. Aspose.PDF para .NET proporciona características notables, desde la creación de documentos PDF desde cero hasta la manipulación de archivos PDF existentes. Entre estas características, la conversión de XML a PDF es una de las grandes características soportadas por este producto. Así que creemos que Aspose.PDF para SharePoint también será capaz de convertir archivos XML al formato PDF.

{{% /alert %}}

## **Creación de un Archivo XML y Conversión a PDF**

{{% alert color="primary" %}}

Paso a paso, este artículo te guía a través del proceso de creación de un archivo XML y su conversión a PDF:
1. [Crear un archivo XML](/pdf/sharepoint/how-to-create-and-convert-an-xml-file-to-pdf/#step-1-create-xml-file).
2. [Crear una plantilla PDF](/pdf/sharepoint/how-to-create-and-convert-an-xml-file-to-pdf/#step-2-create-pdf-template).
3. [Cargar la plantilla XML](/pdf/sharepoint/how-to-create-and-convert-an-xml-file-to-pdf/#step-3-load-xml-template).
4. [Especificar la ruta al archivo fuente](/pdf/sharepoint/how-to-create-and-convert-an-xml-file-to-pdf/#step-4-specify-source-file-path).
5. [Especificar propiedades del archivo](/pdf/sharepoint/how-to-create-and-convert-an-xml-file-to-pdf/#step-5-specify-file-properties).
6. [Exportar el archivo a PDF](/pdf/sharepoint/how-to-create-and-convert-an-xml-file-to-pdf/#step-6-export-to-pdf).
7. [Guardar el archivo PDF](/pdf/sharepoint/how-to-create-and-convert-an-xml-file-to-pdf/#step-7-save-pdf-document).
#### **Paso 1: Crear Archivo XML**
Primero crea un archivo XML basado en el Modelo de Objetos de Documento de Aspose.PDF para .NET.

De acuerdo con el DOM de Aspose.PDF para .NET, un documento PDF contiene una colección de objetos Section, y una Section contiene uno o más elementos Paragraph.
 El texto es un objeto de nivel Párrafo y puede contener uno o más segmentos. A continuación, se añade una cadena de texto de ejemplo a un objeto Segmento y se añade a un objeto Texto. Finalmente, el elemento Texto se añade a la colección de párrafos del objeto Sección.

**XML**

{{< highlight csharp >}}



<?xml version="1.0" encoding="utf-8" ?>

  <Pdf xmlns="Aspose.PDF">

   <Section>

    <Text>

            <Segment>Hola Mundo</Segment>

    </Text>

   </Section>

  </Pdf>



{{< /highlight >}}
#### **Paso 2: Crear Plantilla PDF**
Antes de continuar, asegúrese de que el servidor SharePoint Foundation 2010 está correctamente instalado y configurado en el sistema donde se realizará la conversión.

1. Inicie sesión en el sitio de SharePoint.
1. Seleccione **Acción del Sitio** y **Todos los Elementos**.
1. Seleccione la opción **Crear** y seleccione **Plantilla PDF** de la lista.
1. Ingrese un nombre para la plantilla.
1. Haga clic en **Crear**.




![todo:image_alt_text](how-to-create-and-convert-an-xml-file-to-pdf_1.png)
#### **Paso 3: Cargar Plantilla XML**

Una vez creada la plantilla, cargue [el archivo XML](/pdf/sharepoint/how-to-create-and-convert-an-xml-file-to-pdf/):
1. En la página de plantilla PDF, selecciona **Agregar nuevo elemento**.




![todo:image_alt_text](how-to-create-and-convert-an-xml-file-to-pdf_2.png)
#### **Paso 4: Especificar la Ruta del Archivo de Origen**
En el cuadro de diálogo de carga de documentos:

1. Haz clic en **Examinar** y localiza el archivo XML en tu sistema. Puedes habilitar la casilla de verificación para sobrescribir la opción de archivo existente.
1. Presiona el botón **OK**.




![todo:image_alt_text](how-to-create-and-convert-an-xml-file-to-pdf_3.png)
#### **Paso 5: Especificar Propiedades del Archivo**
Cuando el archivo se carga, agrega información en los campos obligatorios (marcados con un asterisco rojo: *).

Para este ejemplo, se ha agregado una descripción de muestra y se han completado los siguientes campos:

1. Una breve descripción del documento.
1. Ingresa **AllListTypes** para el campo **Tipos de Lista Asignados**.
1. Selecciona **Lista** del menú **Tipo**.
   Asegúrate de que el estado permanezca **Activo**.
1. Haz clic en **Guardar** para guardar las propiedades.




![todo:image_alt_text](how-to-create-and-convert-an-xml-file-to-pdf_4.png)
#### **Paso 6: Exportar a PDF**

Cuando el archivo XML ha sido agregado a la plantilla PDF:
Either:

1. Haz clic derecho en el archivo test.xml.
1. Selecciona **Exportar a PDF** del menú.

O:

1. Selecciona **Aspose Tools** de **Library Tools**.
1. Haz clic en **Exportar**.




![todo:image_alt_text](how-to-create-and-convert-an-xml-file-to-pdf_5.png)
#### **Paso 7: Guardar documento PDF**
1. En el diálogo Exportar a PDF, selecciona **Almacenamiento de plantillas** (la ubicación donde se guarda el archivo fuente).
1. Selecciona el archivo para exportar del menú **Nombre de plantilla**.
1. Haz clic en **Exportar a PDF** para guardar el documento PDF final.




![todo:image_alt_text](how-to-create-and-convert-an-xml-file-to-pdf_6.png)
#### **Abrir el PDF**
El documento PDF ha sido guardado y puede ser abierto. En la imagen de abajo, nota la frase "Hello World" que estaba en la etiqueta {segment] en el XML. También nota que el productor del PDF es Aspose.PDF para SharePoint.




![todo:image_alt_text](how-to-create-and-convert-an-xml-file-to-pdf_7.png)

{{% /alert %}}