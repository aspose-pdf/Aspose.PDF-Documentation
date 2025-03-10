---
title: Aspose.PDF Editor
linktitle: Aspose.PDF Editor
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /es/net/aspose-pdf-editor/
description: Aspose.PDF for .NET demuestra que el Editor PDF HTML5 es un editor PDF basado en la web de código abierto.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Aspose.PDF Editor",
    "alternativeHeadline": "HTML5 PDF Editor: Create, Edit, and Convert PDF Online",
    "abstract": "El Editor Aspose.PDF for .NET es una herramienta robusta de edición de PDF basada en la web y de código abierto para .NET que permite a los usuarios crear, editar y convertir documentos PDF sin problemas dentro de sus aplicaciones web. Con funcionalidades avanzadas como la fusión de archivos, el llenado de campos de formularios y el soporte para múltiples formatos, ofrece una interfaz de usuario simplificada diseñada para una gestión eficiente de documentos y una experiencia de usuario mejorada.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "3488",
    "proficiencyLevel": "Beginner",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF for .NET",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
        "alternateName": "Aspose",
        "sameAs": [
            "https://facebook.com/aspose.pdf/",
            "https://twitter.com/asposepdf",
            "https://www.youtube.com/channel/UCmV9sEg_QWYPi6BJJs7ELOg/featured",
            "https://www.linkedin.com/company/aspose",
            "https://stackoverflow.com/questions/tagged/aspose",
            "https://aspose.quora.com/",
            "https://aspose.github.io/"
        ],
        "contactPoint": [
            {
                "@type": "ContactPoint",
                "telephone": "+1 903 306 1676",
                "contactType": "sales",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "sales",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "sales",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "url": "/net/aspose-pdf-editor/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/aspose-pdf-editor/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF puede realizar no solo tareas simples y fáciles, sino también hacer frente a objetivos más complejos. Consulte la siguiente sección para usuarios avanzados y desarrolladores."
}
</script>

## ¿Qué es el Editor PDF Html5 de Aspose.PDF for .NET?

El Editor PDF HTML5 de Aspose.PDF for .NET es un editor PDF basado en la web de código abierto que permite a los usuarios crear, editar y convertir archivos PDF en línea, y los usuarios pueden integrar fácilmente el editor en sus propias aplicaciones web para ver y editar archivos PDF. El Editor PDF HTML5 se desarrolla utilizando HTML5, jQuery Ajax, ASP.NET, Bootstrap y el backend está impulsado por Aspose.PDF for .NET. La interfaz de usuario del editor se mantiene muy simple para facilitar la comprensión y la mejora de las características según los requisitos del usuario.

![Image](../images/aspose-pdf-editor.png)

## Características

Soporta las siguientes características:

- Crear nuevos archivos PDF.
- Cargar y ver archivos PDF.
- Cargar archivos PDF e imágenes desde Dropbox.
- Exportar archivos PDF a diferentes formatos de archivo.
- Anexar o fusionar archivos PDF.
- Insertar nuevas páginas.
- Eliminar páginas.
- Mover páginas en el archivo PDF.
- Insertar texto en PDF.
- Resaltar texto en PDF.
- Rotar texto insertado en PDF.
- Buscar texto en PDF.
- Reemplazar texto en PDF.
- Insertar imágenes.
- Redimensionar firmas e imágenes.
- Arrastrar y posicionar elementos insertados.
- Cargar archivos PDF con campos de formulario.
- Llenar campos de formulario usando el Editor.
- Guardar y exportar PDF con datos de campos de formulario.
- Resaltar campos de formulario requeridos.
- Agregar archivos adjuntos a archivos PDF.
- Cargar archivos adjuntos desde el archivo PDF de entrada.
- Descargar los archivos adjuntos.
- Eliminar los archivos adjuntos.
- Firmar PDF usando dibujo a mano alzada.

## Requisitos del sistema

Como el Editor PDF HTML5 es una aplicación web .NET que se desarrolla utilizando ASP.NET, C#, HTML5, jQuery, Javascript. Necesitarás el siguiente entorno del sistema para configurar el Editor PDF HTML5 en tu lado.

- Visual Studio 2010 (o superior).
- .NET Framework 3.5 (o superior).
- Aspose.PDF for .NET.
- jQuery 2.0.3.
- Bootstrap 3.2.0.

Puedes usar cualquiera de los siguientes navegadores para ejecutar la aplicación en tu lado:

- Mozilla Firefox (recomendado).
- Internet Explorer (versión 9 o posterior).
- Google Chrome.
- Apple Safari.

## Soporte

Nosotros, en Aspose, nos aseguramos de proporcionar el mejor soporte posible a nuestros clientes / usuarios para sus consultas de cualquier naturaleza, es decir, técnicas o de ventas. Por favor, utiliza los enlaces a continuación para cualquier consulta relacionada con licencias y ventas o consulta técnica.

## Guía del desarrollador del Editor PDF

### Crear nuevos archivos PDF

Además de editar documentos PDF existentes, el Editor PDF Html5 también admite la creación de nuevos archivos PDF desde cero, lo que puedes hacer utilizando la opción Crear nuevo archivo en la barra de menú. Usando esta característica, puedes crear un PDF en blanco en el editor, agregar algo de texto/imágenes y guardarlo en cualquier formato deseado. En nuestra próxima sección, discutiremos los detalles técnicos detrás de esta característica.

**HTML - Se hace clic en el elemento del menú "Crear nuevo archivo" en la página**

Cuando haces clic en el elemento del menú "Crear nuevo archivo", se llama al método onNewFileClicked en el archivo Editor.js.

**jQuery - Enviar solicitud Ajax al servidor para el método CreateNewFile.**

Consulta la pestaña Editor.js a continuación para el código fuente del método onNewFileClicked, que llama al método CreateNewFile en el archivo CanvasSave.aspx.cs.

**Método web ASP.NET maneja solicitudes del servidor**

Consulta la pestaña Canvas.aspx.cs a continuación con el código fuente del método CreateNewFile. Limpia cualquier dato existente sobre el archivo previamente cargado utilizando el método ResetData.

**Creación de un nuevo archivo PDF utilizando Aspose.PDF for .NET**

Después de limpiar los datos utilizando el método ResetData, el método CreateNewFile crea un nuevo archivo PDF utilizando la clase Document de Aspose.PDF for .NET. Como puedes ver en la pestaña a continuación, el objeto Document está generando un archivo con una página vacía. Después de que el archivo se genera en el servidor, el archivo se convierte en imagen utilizando el método ImageConverter para ser cargado en el lienzo.

**Cargando el archivo resultante en el lienzo.**

Después de que el archivo se convierte en imagen en el lado del servidor, el control se devuelve al método onNewFileClicked en Editor.js. El método onNewFileClicked restablece todas las colecciones del lado del cliente y carga el archivo de imagen generado en el lienzo utilizando el método resetData.

### Exportar PDF a diferentes formatos de archivo

El Editor PDF HTML5 admite la exportación de archivos PDF a diferentes formatos de archivo, lo que puedes hacer utilizando la opción Exportar archivo en la barra de menú. Usando esta característica, puedes exportar el archivo PDF a tu formato deseado. En nuestra próxima sección, discutiremos los detalles técnicos detrás de esta característica.

**HTML - Se hace clic en el elemento del menú "Exportar archivo" en la página.**

Cuando haces clic en el elemento del menú "Exportar archivo", puedes elegir el formato de exportación de la lista. Después de seleccionar el formato de exportación, se llama al método "ExportFile" en el archivo Editor.js.

**jQuery - Enviar solicitud Ajax al servidor para el método btnFileExport_Click**

Consulta la pestaña Editor.js a continuación para el código fuente del método "ExportFile". Envía una solicitud al método del servidor btnFileExport_Click con el parámetro de formato de archivo en el archivo CanvasSave.aspx.cs.

**Método web ASP.NET maneja solicitudes del servidor**

Consulta la pestaña Canvas.aspx.cs a continuación. Basado en el parámetro de formato de archivo pasado a btnFileExport_Click, el archivo PDF se convierte utilizando el método Save del objeto Document de Aspose.PDF.

**Exportar archivo para descargar en el navegador del cliente**

Después de que el archivo se genera en el servidor, el control se devuelve al método ExportFile en Editor.js desde donde el archivo se envía al navegador para que el usuario lo descargue utilizando el método ExportToBrowser.

### Anexar o fusionar archivos PDF

El Editor PDF Html5 admite la anexión o fusión de archivos PDF, lo que puedes hacer utilizando la opción Anexar archivo en la barra de menú. Usando esta característica, puedes anexar el archivo PDF a tu archivo de entrada. En nuestra próxima sección, discutiremos los detalles técnicos detrás de esta característica.

**HTML - Se hace clic en el elemento del menú "Anexar archivo" en la página.**

Cuando haces clic en el elemento del menú "Anexar archivo", puedes cargar el archivo utilizando el cuadro de diálogo de carga de archivos. Después de que el archivo se carga, se llama al método "fileSelected" en el archivo Editor.js.

**jQuery - Enviar solicitud al servidor para el método ProcessRequest**

Consulta la pestaña Editor.js a continuación para el código fuente del método "fileSelected". El archivo se publica en el servidor y se llama al método "ProcessRequest" en el archivo CanvasSave.aspx.cs.

**Método web ASP.NET maneja solicitudes del servidor**

Consulta la pestaña Canvas.aspx.cs a continuación. Basado en el parámetro de formulario pasado, el archivo que se va a anexar se guarda en el servidor y se llama al método "AppendFile". El método AppendFile anexa el archivo cargado utilizando Aspose.PDF for .NET, convierte el archivo resultante en imagen y devuelve el control al método "fileSelected" en Editor.js.

**Actualizar el contenido del lienzo después de anexar el archivo**

Después de que el archivo se genera en el servidor, el control se devuelve al método "fileSelected" en Editor.js, que actualiza los contenidos del editor.

### Cargar archivo PDF local

El Editor PDF HTML5 admite la carga de archivos PDF desde la máquina local utilizando la opción Abrir desde computadora en la barra de menú. Usando esta característica, puedes abrir un archivo PDF existente y realizar ediciones en tu archivo PDF. En nuestra próxima sección, discutiremos los detalles técnicos detrás de esta característica.

**HTML - Se hace clic en el elemento del menú "Abrir desde computadora" en la página.**

Cuando haces clic en el elemento del menú "Abrir desde computadora", puedes cargar el archivo de entrada que contiene los campos de formulario utilizando el cuadro de diálogo de carga de archivos. Después de que el archivo se carga, se llama al método "fileSelected" en el archivo Editor.js.

**jQuery - Enviar solicitud al servidor para el método ProcessRequest**

Consulta la pestaña Editor.js a continuación para el código fuente del método "fileSelected". El archivo se publica en el servidor y se llama al método "ProcessRequest" en el archivo CanvasSave.aspx.cs.

**Método web ASP.NET maneja solicitudes del servidor**

Consulta la pestaña Canvas.aspx.cs a continuación. Basado en el parámetro de formulario pasado, el archivo que se va a cargar se guarda en el servidor, restablece los datos utilizando el método "ResetData" y se llama al método "ImageConverter". El método ImageConverter convierte el archivo cargado en imágenes utilizando Aspose.PDF for .NET y devuelve el control al método "fileSelected" en Editor.js.

**Actualizar el contenido del lienzo después de cargar el archivo**

Después de que el archivo se genera en el servidor, el control se devuelve al método "fileSelected" en Editor.js, que actualiza los contenidos del editor, es decir, restablece el lienzo, carga el archivo recién cargado.

### Agregar página en archivo PDF

Usando el Editor PDF Html5, puedes agregar nuevas páginas en archivos PDF utilizando la opción Agregar página en la barra de menú. Usando esta característica, puedes agregar una página en blanco a tu archivo PDF. En nuestra próxima sección, discutiremos los detalles técnicos detrás de esta característica.

**HTML - Se hace clic en el elemento del menú "Agregar página" en la página**

Cuando haces clic en el elemento del menú "Agregar página", se llama al método "AddPage" en el archivo Editor.js.

**jQuery - Enviar solicitud Ajax al servidor para el método AddPage_Click.**

Consulta la pestaña Editor.js a continuación para el código fuente del método AddPage, que llama al método AddPage_Click en el archivo CanvasSave.aspx.cs.

**Método web ASP.NET maneja solicitudes del servidor**

Consulta la pestaña Canvas.aspx.cs a continuación con el código fuente del método AddPage_Click. Agrega una nueva página vacía en el archivo PDF utilizando la clase Aspose.Pdf.Document. Después de agregar la página al archivo PDF, convierte la página en imagen para ser mostrada en el editor. El control se devuelve al archivo Editor.js, que actualiza la numeración de páginas en el método AddPage.

### Eliminar página de archivo PDF

Usando el Editor PDF Html5, puedes eliminar una página de archivos PDF utilizando la opción Eliminar página en la barra de menú. En nuestra próxima sección, discutiremos los detalles técnicos detrás de esta característica.

**HTML - Se hace clic en el elemento del menú "Eliminar página" en la página**

Cuando haces clic en el elemento del menú "Eliminar página", se llama al método DeletePage en el archivo Editor.js.

**jQuery - Enviar solicitud Ajax al servidor para el método DeletePage_Click.**

Consulta la pestaña Editor.js a continuación para el código fuente del método DeletePage, que llama al método DeletePage_Click en el archivo CanvasSave.aspx.cs.

**Método web ASP.NET maneja solicitudes del servidor**

Consulta la pestaña Canvas.aspx.cs a continuación con el código fuente del método DeletePage_Click. Elimina la página seleccionada del archivo PDF utilizando el método Delete de la colección Aspose.Pdf.Document.Page.

**Actualizar contenido de edición**

Después de eliminar la página del archivo PDF, el control se devuelve al método DeletePage en el archivo Editor.js, que actualiza la numeración de páginas y elimina cualquier colección asociada con la página eliminada utilizando el método updateIndexesDelete.

### Mover páginas en archivo PDF

Usando el Editor PDF Html5, puedes mover páginas en archivos PDF utilizando la opción Mover página en la barra de menú. Una vez que presionas el elemento del menú Mover página, se te presenta un cuadro de diálogo de entrada para especificar la nueva ubicación de la página seleccionada. En nuestra próxima sección, discutiremos los detalles técnicos detrás de esta característica.

**HTML - Se hace clic en el elemento del menú "Mover página" en la página**

Cuando haces clic en el elemento del menú "Mover página", se muestra un cuadro de diálogo de entrada para obtener la nueva ubicación de la página seleccionada. Después de proporcionar el número de página y presionar el botón "Mover", se llama al método "Move" en el archivo Editor.js.

**jQuery - Enviar solicitud Ajax al servidor para el método MovePages.**

Consulta la pestaña Editor.js a continuación para el código fuente del método Move, que llama al método MovePage y pasa los detalles como mover desde, mover a, lista de páginas al método MovePages en el archivo CanvasSave.aspx.cs.

**Método web ASP.NET maneja solicitudes del servidor**

Consulta la pestaña Canvas.aspx.cs a continuación con el código fuente del método MovePages. Utiliza la colección Aspose.Pdf.Document.Pages para mover las páginas.

**Actualizar contenido de edición**

Después de mover la página, el control se devuelve al método MovePage en el archivo Editor.js, que actualiza los índices de página y la información relacionada con diferentes colecciones en el editor utilizando el método MoveUpdate.

### Insertar texto en archivo PDF

Usando el Editor PDF Html5, puedes insertar texto en archivos PDF utilizando la opción Modo de texto en la barra de menú. Una vez que seleccionas el elemento del menú Modo de texto y haces clic en cualquier ubicación en el editor donde deseas agregar el texto, se te presenta un cuadro de diálogo de entrada para ingresar y dar formato a tu texto deseado como se muestra a continuación:

En nuestra próxima sección, discutiremos los detalles técnicos detrás de esta característica.

**HTML - Se selecciona el elemento del menú "Modo de texto" en la página**

Cuando seleccionas el elemento del menú "Modo de texto" y haces clic en tu ubicación deseada en el editor para insertar texto en el archivo PDF, se muestra un cuadro de diálogo de entrada para obtener el texto que necesitas insertar en la página. Después de proporcionar el texto y presionar el botón "OK", se llama al método "saveTextFromArea" en el archivo Editor.js.

**Javascript - Obtener el texto de entrada del cuadro de diálogo de entrada y mostrarlo en el editor.**

Consulta la pestaña Editor.js a continuación para el código fuente del método saveTextFromArea, que obtiene el texto del cuadro de diálogo de entrada y lo muestra en el editor. Además, guarda los datos en la colección de formas que se utiliza más tarde en el lado del servidor para insertar texto en el archivo PDF. Puedes consultar el código fuente del método saveFile que se llama cuando se guarda el archivo.

**Método web ASP.NET maneja solicitudes del servidor**

Como se mencionó anteriormente, el texto se insertará realmente en nuestro archivo PDF fuente cuando realicemos la operación de guardado que utiliza el método GetTextStamp para crear el sello de texto que se insertará en el archivo PDF. Consulta la pestaña Canvas.aspx.cs a continuación con el código fuente del método GetTextStamp. Utiliza la clase Aspose.Pdf.TextStamp para insertar el texto en el archivo PDF.

### Resaltar texto en archivo PDF

Usando el Editor PDF Html5, puedes resaltar texto en archivos PDF utilizando la opción Modo de resaltado en la barra de menú. Una vez que seleccionas el elemento del menú Modo de resaltado, puedes resaltar cualquier texto y área utilizando la herramienta de resaltado rectangular. En nuestra próxima sección, discutiremos los detalles técnicos detrás de esta característica.

**HTML - Se selecciona el elemento del menú "Modo de resaltado" en la página**

Cuando seleccionas el elemento del menú "Modo de resaltado", puedes dibujar un resaltado rectangular alrededor de cualquier texto o elemento en tu archivo PDF. La implementación de este proceso se puede ver en el método "tools.rect" en el archivo Editor.js.

**Javascript - Dibujar un rectángulo de resaltado en el editor.**

Consulta la pestaña Editor.js a continuación para el código fuente del método tool.rect, que permite al usuario dibujar un rectángulo de resaltado en cualquier ubicación del editor. Además, guarda los datos en la colección de formas que se utiliza más tarde en el lado del servidor para insertar el resaltado en el archivo PDF fuente. Puedes consultar el código fuente del método saveFile que se llama cuando se guarda el archivo.

**Método web ASP.NET maneja solicitudes del servidor**

Como se mencionó anteriormente, el resaltado se inserta realmente en nuestro archivo PDF fuente cuando realizamos la operación de guardado que utiliza el método GetImageStamp para insertar el sello de imagen en el archivo PDF fuente en la ubicación especificada en el editor. Consulta la pestaña Canvas.aspx.cs a continuación con el código fuente del método GetImageStamp. Utiliza la clase Aspose.Pdf.ImageStamp para insertar el rectángulo de resaltado en el archivo PDF.

### Buscar texto en archivo PDF

Usando el Editor PDF Html5, puedes buscar texto en archivos PDF utilizando la opción Buscar texto en la barra de menú. Una vez que haces clic en el elemento del menú Buscar texto, se te presentará un cuadro de diálogo para ingresar el texto a buscar como se muestra a continuación:

Al proporcionar el texto y presionar buscar, todas las instancias de la palabra buscada se resaltarán como se muestra a continuación:

**HTML - Se hace clic en el elemento del menú "Buscar texto" en la página**

Cuando haces clic en el elemento del menú "Buscar texto", se te presenta un cuadro de diálogo de entrada para ingresar el texto que deseas buscar. Después de ingresar el texto y presionar el botón de búsqueda, se llama al método "Move", que verifica si se realiza la operación de mover página o la operación de búsqueda y luego llama al método performSearch en el archivo Editor.js.

**jQuery - Enviar solicitud Ajax al servidor para el método SearchData**

Consulta la pestaña Editor.js a continuación para el código fuente del método performSearch, que obtiene el texto de entrada y una solicitud al método del servidor SearchData en el archivo _CanvasSave.aspx.cs_.

**Método web ASP.NET maneja solicitudes del servidor**

Consulta la pestaña _Canvas.aspx.cs_ a continuación. Usando el texto de entrada pasado desde el método performSearch, el método SearchData utiliza la clase Aspose.Pdf.Text.TextFragmentAbsorber para buscar todas las instancias del texto de entrada en nuestro archivo PDF fuente y la clase System.Drawing.Brush para dibujar el resaltado contra el texto buscado. Una vez que se busca el dato, el archivo resultante se convierte nuevamente en imagen y se carga en el editor.

### Reemplazar texto en archivo PDF

Usando el Editor PDF Html5, puedes reemplazar el texto existente en archivos PDF utilizando la opción Reemplazar texto en la barra de menú. Una vez que haces clic en el elemento del menú Reemplazar texto, se te presentará un cuadro de diálogo para ingresar el texto a buscar y reemplazar.

**HTML - Se hace clic en el elemento del menú "Reemplazar texto" en la página**

Cuando haces clic en el elemento del menú "Reemplazar texto", se te presenta un cuadro de diálogo de entrada para ingresar el texto a buscar y reemplazar. Después de ingresar el texto y presionar el botón Reemplazar, se llama al método "ReplaceText" en el archivo Editor.js.

**jQuery - Enviar solicitud Ajax al servidor para el método ReplaceText**

Consulta la pestaña Editor.js a continuación para el código fuente del método ReplaceText, que obtiene el texto de entrada del cuadro de diálogo de texto de entrada y una solicitud al método del servidor ReplaceText en el archivo CanvasSave.aspx.cs.

**Método web ASP.NET maneja solicitudes del servidor**

Consulta la pestaña Canvas.aspx.cs a continuación. El método ReplaceText utiliza la clase Aspose.Pdf.Text.TextFragmentAbsorber para buscar todas las instancias del texto que se va a reemplazar en nuestro archivo PDF fuente y reemplaza todas las instancias con el texto reemplazado. Una vez que se reemplaza el texto, el archivo resultante se convierte nuevamente en imagen y se carga en el editor.

### Cargando archivo PDF con campos de formulario

Usando el Editor PDF Html5, puedes cargar y trabajar con un archivo PDF que contiene campos de formulario. Una vez que el archivo con campos de formulario se carga en el editor, todos los campos de formulario se cargan para su edición. En nuestra próxima sección, discutiremos los detalles técnicos detrás de esta característica.

**HTML - Se hace clic en el elemento del menú "Abrir desde computadora" en la página.**

Cuando haces clic en el elemento del menú "Abrir desde computadora", puedes cargar el archivo de entrada que contiene los campos de formulario utilizando el cuadro de diálogo de carga de archivos. Después de que el archivo se carga, se llama al método "fileSelected" en el archivo Editor.js.

**jQuery - Enviar solicitud al servidor para el método ProcessRequest**

El archivo se publica en el servidor y se llama al método "ProcessRequest" en el archivo CanvasSave.aspx.cs.

**Método web ASP.NET maneja solicitudes del servidor**

Consulta la pestaña Canvas.aspx.cs a continuación. Basado en el parámetro de formulario pasado, el archivo que se va a cargar se guarda en el servidor, el método ImageConverter convierte el archivo cargado en imágenes y se llama al método "CheckFields", que utiliza la clase Aspose.Pdf.InteractiveFeatures.Forms para verificar todos los campos de formulario y recopilar la información sobre los campos, es decir, FieldType, Location, etc., y devolver la colección de campos al método ImageConverter. El método ImageConverter devuelve el control al método "fileSelected" en Editor.js.

**Cargando campos de formulario en el lienzo**

Consulta la pestaña Editor.js a continuación, el método manageFields en Editor.js se utiliza para generar todos los campos en el lienzo basado en la información enviada desde el lado del servidor. Dibuja controles de campo HTML utilizando la información de tipo y ubicación del lado del servidor en el lienzo.

### Resaltando campos de formulario requeridos

Usando el Editor PDF Html5, puedes resaltar los campos de formulario requeridos en el editor. Una vez que el archivo con campos de formulario se carga en el editor, todos los campos de formulario requeridos se resaltan para ayudar a los usuarios en la edición. En nuestra próxima sección, discutiremos los detalles técnicos detrás de esta característica.

**HTML - Se hace clic en el elemento del menú "Abrir desde computadora" en la página.**

Cuando haces clic en el elemento del menú "Abrir desde computadora", puedes cargar el archivo de entrada que contiene los campos de formulario utilizando el cuadro de diálogo de carga de archivos. Después de que el archivo se carga, se llama al método "fileSelected" en el archivo Editor.js.

**jQuery - Enviar solicitud al servidor para el método ProcessRequest**

El archivo se publica en el servidor y se llama al método "ProcessRequest" en el archivo CanvasSave.aspx.cs.

**Método web ASP.NET maneja solicitudes del servidor**

Consulta la pestaña Canvas.aspx.cs a continuación. Basado en el parámetro de formulario pasado, el archivo que se va a cargar se guarda en el servidor, el método ImageConverter convierte el archivo cargado en imágenes y se llama al método "CheckFields", que utiliza la clase Aspose.Pdf.InteractiveFeatures.Forms para verificar todos los campos de formulario y recopilar la información sobre los campos, es decir, FieldType, Location, etc. Después de obtener los detalles de todos los campos de formulario, obtenemos la información de si un campo de formulario es un campo requerido utilizando el método Aspose.Pdf.Facades.IsRequiredField y devolvemos la colección de campos al método ImageConverter. El método ImageConverter devuelve el control al método "fileSelected" en Editor.js.

**Cargando campos de formulario en el lienzo**

Consulta la pestaña Editor.js a continuación, el método manageFields en Editor.js se utiliza para generar todos los campos en el lienzo basado en la información enviada desde el lado del servidor. Dibuja controles de campo HTML utilizando la información de tipo y ubicación del lado del servidor en el lienzo. Si un campo determinado es requerido, utiliza el div (llamado wrapper) alrededor del control y cambia la propiedad de color de fondo del div para mostrarlo como un campo requerido resaltado.