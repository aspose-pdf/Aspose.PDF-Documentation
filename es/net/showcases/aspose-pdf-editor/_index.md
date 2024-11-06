---
title: Aspose.PDF Editor
linktitle: Aspose.PDF Editor
type: docs
weight: 10
url: es/net/aspose-pdf-editor/
description: Aspose.PDF para .NET demuestra que el HTML5 PDF Editor es un editor de PDF basado en web de código abierto.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## ¿Qué es el Editor de PDF HTML5 de Aspose.PDF para .NET?

El Editor de PDF HTML5 de Aspose.PDF para .NET es un editor de PDF basado en web de código abierto que permite a los usuarios crear, editar y convertir archivos PDF en línea, y los usuarios pueden integrar fácilmente el editor en sus propias aplicaciones web para visualizar y editar archivos PDF. El Editor de PDF HTML5 está desarrollado utilizando HTML5, jQuery Ajax, ASP.NET, Bootstrap y el backend está potenciado por Aspose.PDF para .NET. La interfaz de usuario del editor es muy simple para facilitar la comprensión y la mejora de las características según los requisitos del usuario.

![Image](../images/aspose-pdf-editor.png)

## Características

Actualmente, soporta las siguientes características:

- Crear nuevos archivos PDF
- Cargar y visualizar archivos PDF
- Cargar archivos PDF e imágenes desde Dropbox
- Cargar archivos PDF e imágenes desde Dropbox
- Exportar archivo PDF a diferentes formatos de archivo
- Añadir o Fusionar archivos PDF
- Insertar Nuevas Páginas
- Eliminar Páginas
- Mover Páginas en el archivo PDF
- Insertar Texto en PDF
- Resaltar Texto en PDF
- Rotar Texto Insertado en PDF
- Buscar Texto en PDF
- Reemplazar Texto en PDF
- Insertar Imágenes
- Redimensionar Firma e Imágenes
- Arrastrar y Posicionar elementos insertados
- Cargar archivos PDF con campos de formulario
- Rellenar campos de formulario usando el Editor
- Guardar y Exportar PDF con datos de campos de formulario
- Resaltar campos de formulario requeridos
- Añadir Adjuntos a archivos PDF
- Cargar Adjuntos desde archivo PDF de entrada
- Descargar los archivos Adjuntos
- Eliminar los archivos Adjuntos
- Firmar PDF usando Dibujo a Mano Alzada

## Requisitos del Sistema

Como el Editor de PDF HTML5 es una aplicación web .NET desarrollada usando ASP.NET, C#, HTML5, jQuery, Javascript. Necesitarás el siguiente entorno de sistema para configurar el Editor de PDF HTML5 en tu equipo.

- Visual Studio 2010 (o superior)
- .NET Framework 3.5 (o superior)
- Aspose.PDF para .NET
- Aspose.PDF para .NET
- jQuery 2.0.3
- Bootstrap 3.2.0

Puedes usar cualquiera de los siguientes navegadores para ejecutar la aplicación en tu lado:

- Mozilla Firefox (recomendado)
- Internet Explorer (versión 9 o posterior)
- Google Chrome
- Apple Safari

## Soporte

En Aspose, nos aseguramos de proporcionar el mejor soporte posible a nuestros clientes / usuarios para sus consultas de cualquier naturaleza, ya sea técnica o de ventas. Utiliza los siguientes enlaces para cualquier consulta relacionada con licencias y ventas o consultas técnicas.

# Guía del Desarrollador de Editor de PDF

## Crear Nuevos Archivos PDF

Además de editar documentos PDF existentes, el Editor de PDF Html5 también admite la creación de nuevos archivos PDF desde cero, lo que puedes hacer utilizando la opción Crear Nuevo Archivo desde la barra de menú. Usando esta característica, puedes crear un PDF en blanco en el editor, agregarle texto/imágenes y guardarlo en cualquier formato deseado. En nuestra siguiente sección, discutiremos los detalles técnicos detrás de esta característica.

### ¿Cómo funciona?

**HTML - Se hace clic en el elemento del menú "Crear Nuevo Archivo" en la página**

Cuando haces clic en el elemento del menú "Crear Nuevo Archivo", se llama al método onNewFileClicked en el archivo Editor.js.
Cuando haces clic en el elemento del menú "Crear nuevo archivo", se llama al método onNewFileClicked en el archivo Editor.js.

**jQuery - Envía una solicitud Ajax al servidor para el método CreateNewFile.**

Consulta la pestaña Editor.js a continuación para ver el código fuente del método onNewFileClicked, llama al método CreateNewFile en el archivo CanvasSave.aspx.cs.

**El método web ASP.NET maneja las solicitudes del servidor**

Consulta la pestaña Canvas.aspx.cs a continuación con el código fuente del método CreateNewFile. Elimina cualquier dato existente respecto al archivo cargado anteriormente usando el método ResetData.

**Creación de un nuevo archivo PDF utilizando Aspose.PDF para .NET**

Después de limpiar los datos usando el método ResetData, el método CreateNewFile crea un nuevo archivo PDF utilizando la clase Document de Aspose.PDF para .NET.
Como puedes ver en la pestaña de abajo, el objeto Document está generando un archivo con una página vacía. Después de que el archivo se genera en el servidor, el archivo se convierte a imagen utilizando el método ImageConverter para ser cargado en el lienzo.

**Cargando el archivo resultante en el lienzo.**

Después de que el archivo se convierte a imagen en el lado del servidor, el control se devuelve al método onNewFileClicked en Editor.js.
Después de que el archivo se convierte a imagen en el servidor, el control regresa al método onNewFileClicked en Editor.js.

## Exportación de PDF a Diferentes Formatos de Archivo

El Editor PDF HTML5 soporta la exportación de archivos PDF a diferentes formatos de archivo, lo cual puedes hacer utilizando la opción Exportar Archivo del menú. Usando esta característica, puedes exportar el archivo PDF al formato deseado. En nuestra próxima sección, discutiremos los detalles técnicos detrás de esta característica.

### ¿Cómo funciona?

**HTML - Se hace clic en el ítem del menú "Exportar Archivo".**

Cuando haces clic en el ítem del menú "Exportar Archivo", puedes elegir el formato de exportación de la lista. Después de seleccionar el formato de exportación, se llama al método "ExportFile" en el archivo Editor.js.

**jQuery - Envía una solicitud Ajax al servidor para el método btnFileExport_Click**

Consulta la pestaña Editor.js a continuación para ver el código fuente del método "ExportFile". Envía una solicitud al método del servidor btnFileExport_Click con el parámetro de formato de archivo en el archivo CanvasSave.aspx.cs.

**Método web ASP.NET maneja las solicitudes del servidor**

Consulta la pestaña Canvas.aspx.cs a continuación.
**Exportar archivo para descargar en el navegador del cliente**

Después de que el archivo se genera en el servidor, el control vuelve al método ExportFile en Editor.js desde donde el archivo se envía al navegador para que el usuario lo descargue usando el método ExportToBrowser.

## Añadiendo o Fusionando Archivos PDF

El Editor PDF Html5 soporta la adición o fusión de archivos PDF que puedes realizar utilizando la opción de Añadir Archivo desde la barra de menú. Usando esta característica, puedes añadir el archivo PDF a tu archivo de entrada. En nuestra próxima sección, discutiremos los detalles técnicos detrás de esta característica.

### ¿Cómo funciona?

**HTML - Se hace clic en el elemento de menú "Añadir Archivo" en la página.**

Cuando haces clic en el elemento de menú "Añadir Archivo", puedes subir el archivo usando el diálogo de subida de archivos. Después de que el archivo se haya subido, se llama al método "fileSelected" en el archivo Editor.js.

**jQuery - Enviar solicitud al servidor para el método ProcessRequest**

Consulta la pestaña Editor.js a continuación para ver el código fuente del método "fileSelected".
Vea la pestaña Editor.js a continuación para ver el código fuente del método "fileSelected".

**Método web de ASP.NET maneja solicitudes del servidor**

Vea la pestaña Canvas.aspx.cs a continuación. Basado en el parámetro del formulario pasado, el archivo a ser añadido se guarda en el servidor y se llama al método "AppendFile". El método AppendFile, añade el archivo subido usando Aspose.PDF para .NET, convierte el archivo resultante a imagen y devuelve el control al método "fileSelected" en Editor.js

**Actualizar el contenido del lienzo después de añadir el archivo**

Después de que el archivo se genera en el servidor, el control se devuelve al método "fileSeleceted" en Editor.js que actualiza los contenidos del editor.

## Subir Archivo PDF Local

El editor PDF HTML5 soporta la subida de archivos PDF desde la máquina local utilizando la opción Abrir Desde Computadora de la barra de menú. Utilizando esta característica, puedes abrir un archivo PDF existente y realizar ediciones en tu archivo PDF. En nuestra próxima sección, discutiremos los detalles técnicos detrás de esta característica.

### ¿Cómo funciona?

**HTML - Se hace clic en el elemento del menú "Abrir Desde Computadora" en la página.**
**HTML - "Abrir desde el ordenador" se clickea en la página.**

Cuando haces clic en el elemento del menú "Abrir desde el ordenador", puedes subir el archivo de entrada utilizando el diálogo de carga de archivos. Después de que el archivo se haya cargado, se llama al método "fileSelected" en el archivo Editor.js.

**jQuery - Enviar solicitud al servidor para el método ProcessRequest**

Consulta la pestaña Editor.js a continuación para ver el código fuente del método "fileSelected". El archivo se publica en el servidor y se llama al método "ProcessRequest" en el archivo CanvasSave.aspx.cs.

**Método web ASP.NET maneja las solicitudes del servidor**

Consulta la pestaña Canvas.aspx.cs a continuación. Basado en el parámetro de formulario pasado, el archivo a subir se guarda en el servidor, reinicia los datos utilizando el método "ResetData" y se llama al método "ImageConverter". El método ImageConverter, convierte el archivo subido a imágenes utilizando Aspose.PDF para .NET y devuelve el control al método "fileSelected" en Editor.js

**Actualizar el contenido del lienzo después de subir el archivo**

Después de que el archivo se genera en el servidor, el control se devuelve al método "fileSelected" en Editor.js que actualiza los contenidos del editor.
## Agregando Página en Archivo PDF

Usando el Editor de PDF Html5, puedes agregar nuevas páginas en archivos PDF utilizando la opción Agregar Página desde la barra de menú. Usando esta característica, puedes agregar una página en blanco a tu archivo PDF. En nuestra siguiente sección, discutiremos los detalles técnicos detrás de esta característica.

### ¿Cómo funciona?

**HTML - Se hace clic en el elemento del menú "Agregar Página"**

Cuando haces clic en el elemento del menú "Agregar Página", se llama al método "AddPage" en el archivo Editor.js.

**jQuery - Enviar solicitud Ajax al servidor para el método AddPage_Click.**

Ver la pestaña Editor.js a continuación para el código fuente del método AddPage, llama al método AddPage_Click en el archivo CanvasSave.aspx.cs.

**Método web ASP.NET maneja las solicitudes del servidor**

Ver la pestaña Canvas.aspx.cs a continuación con el código fuente del método AddPage_Click.
## Eliminación de una página de un archivo PDF

Utilizando el Editor PDF Html5, puedes eliminar una página de archivos PDF utilizando la opción Eliminar Página del menú. En nuestra próxima sección, discutiremos los detalles técnicos detrás de esta característica.

### ¿Cómo funciona?

**HTML - Se hace clic en el elemento del menú "Eliminar Página"**

Cuando haces clic en el elemento del menú "Eliminar Página", se llama al método DeletePage en el archivo Editor.js.

**jQuery - Envía solicitud Ajax al servidor para el método DeletePage_Click.**

Ver la pestaña Editor.js a continuación para el código fuente del método DeletePage, llama al método DeletePage_Click en el archivo CanvasSave.aspx.cs.

**Método web de ASP.NET maneja las solicitudes del servidor**

Ver la pestaña Canvas.aspx.cs a continuación con el código fuente del método DeletePage_Click. Elimina la página seleccionada del archivo PDF utilizando el método Delete de la colección Aspose.PDF.Document.Page.

**Actualizando el contenido de edición**

Después de eliminar la página del archivo PDF, el control se devuelve al método DeletePage en el archivo Editor.js que actualiza la numeración de páginas, elimina cualquier colección asociada con la página eliminada usando el método updateIndexesDelete.
Después de eliminar la página del archivo PDF, el control se devuelve al método DeletePage en el archivo Editor.js, el cual actualiza la numeración de las páginas, elimina cualquier colección asociada con la página eliminada usando el método updateIndexesDelete.

## Mover Páginas en Archivo PDF

Utilizando el Editor PDF Html5, puedes mover páginas en archivos PDF utilizando la opción Mover Página desde la barra de menú. Una vez que presionas el ítem del menú Mover Página, se presenta un diálogo de entrada para especificar la nueva ubicación de la página seleccionada. En nuestra próxima sección, discutiremos los detalles técnicos detrás de esta característica.

### ¿Cómo funciona?

**HTML - Se hace clic en el ítem del menú "Mover Página"**

Cuando haces clic en el ítem del menú "Mover Página", se muestra un diálogo de entrada para obtener la nueva ubicación de la página seleccionada. Después de proporcionar el número de página y presionar el botón "Mover", se llama al método "Move" en el archivo Editor.js.

**jQuery - Enviar solicitud Ajax al servidor para el método MovePages.**

Vea la pestaña Editor.js a continuación para el código fuente del método Move, que llama al método MovePage y pasa detalles como mover de, mover a, lista de páginas al método MovePages en el archivo CanvasSave.aspx.cs.
Vea la pestaña Editor.js a continuación para ver el código fuente del método Move, que llama al método MovePage y pasa los detalles como mover de, mover a, lista de páginas al método MovePages en el archivo CanvasSave.aspx.cs.

**El método web de ASP.NET maneja las solicitudes del servidor**

Vea la pestaña Canvas.aspx.cs a continuación con el código fuente del método MovePages. Utiliza la colección Aspose.PDF.Document.Pages para mover las páginas.

**Actualizando contenido de edición**

Después de mover la página, el control se devuelve al método MovePage en el archivo Editor.js que actualiza los índices de las páginas y la información relacionada con diferentes colecciones en el editor utilizando el método MoveUpdate.

## Insertar texto en archivo PDF

Usando el Editor de PDF Html5, puedes insertar texto en archivos PDF utilizando la opción Modo Texto de la barra de menú. Una vez que selecciones el elemento de menú Modo Texto y hagas clic en cualquier ubicación del editor donde quieras agregar el texto, se te presentará un cuadro de diálogo de entrada para ingresar y formatear el texto deseado como se muestra a continuación:

En nuestra próxima sección, discutiremos los detalles técnicos detrás de esta característica.
En nuestra próxima sección, discutiremos los detalles técnicos detrás de esta característica.

### ¿Cómo funciona?

**HTML - Se selecciona el elemento del menú "Modo Texto" en la página**

Cuando seleccionas el elemento del menú "Modo Texto" y haces clic en la ubicación deseada en el editor para insertar texto en el archivo PDF, se muestra un cuadro de diálogo de entrada para obtener el texto que necesitas insertar en la página. Después de proporcionar el texto y presionar el botón "OK", se llama al método "saveTextFromArea" en el archivo Editor.js.

**Javascript - Obtener el texto de entrada del cuadro de diálogo y mostrarlo en el editor.**

Consulta la pestaña Editor.js a continuación para ver el código fuente del método saveTextFromArea, que obtiene el texto del cuadro de diálogo de entrada y lo muestra en el editor. Además, guarda los datos en la colección de formas que luego se utiliza en el lado del servidor para insertar texto en el archivo PDF. Puedes verificar el código fuente del método saveFile que se llama cuando se guarda el archivo.

**El método web ASP.NET maneja las solicitudes del servidor**

Como se mencionó anteriormente, el texto se insertará en nuestro archivo PDF fuente cuando realicemos la operación de guardar que utiliza el método GetTextStamp para crear el sello de texto para insertar en el archivo PDF.
Como se mencionó anteriormente, el texto se insertará en nuestro archivo PDF fuente cuando realicemos la operación de guardado, que utiliza el método GetTextStamp para crear el sello de texto para insertar en el archivo PDF.

## Resaltar texto en archivo PDF

Usando el Editor PDF Html5, puedes resaltar texto en archivos PDF utilizando la opción Modo de Resaltado del menú. Una vez que seleccionas el elemento del menú Modo de Resaltado, puedes resaltar cualquier texto y área usando la herramienta de resaltado rectangular. En nuestra próxima sección, discutiremos los detalles técnicos detrás de esta característica.

### ¿Cómo funciona?

**HTML - Se selecciona el elemento del menú "Modo de Resaltado" en la página**

Cuando seleccionas el elemento del menú "Modo de Resaltado", puedes dibujar un resaltado rectangular alrededor de cualquier texto o elemento en tu archivo PDF. La implementación de este proceso se puede ver en el método "tools.rect" en el archivo Editor.js.

**Javascript - Dibujar rectángulo de resaltado en el editor.**

Consulta la pestaña Editor.js a continuación para ver el código fuente del método tool.rect, que permite al usuario dibujar un rectángulo de resaltado en cualquier ubicación del editor.
Vea la pestaña Editor.js a continuación para ver el código fuente del método tool.rect, que permite al usuario dibujar un rectángulo de resaltado en cualquier ubicación del editor.

**El método web de ASP.NET maneja las solicitudes del servidor**

Como se mencionó anteriormente, el resaltado se inserta en nuestro archivo PDF fuente cuando realizamos la operación de guardar que utiliza el método GetImageStamp para insertar el sello de imagen en el archivo PDF fuente en la ubicación especificada en el editor. Vea la pestaña Canvas.aspx.cs a continuación con el código fuente del método GetImageStamp. Utiliza la clase Aspose.PDF.ImageStamp para insertar el rectángulo de resaltado en el archivo PDF.

## Buscando texto en archivo PDF

Usando el Editor PDF Html5, puedes buscar texto en archivos PDF usando la opción Buscar Texto desde la barra de menú. Una vez que hagas clic en el elemento del menú Buscar Texto, se te presentará un cuadro de diálogo para ingresar el texto a buscar como se muestra a continuación:

Al proporcionar el texto y presionar buscar, todas las instancias de la palabra buscada se resaltarán como se muestra a continuación:

### ¿Cómo funciona?

**HTML - Se hace clic en el elemento del menú "Buscar Texto" en la página**
**HTML - Se hace clic en el elemento del menú "Buscar texto"**

Cuando haces clic en el elemento del menú "Buscar texto", se te presenta un cuadro de diálogo de entrada para ingresar el texto que deseas buscar. Después de ingresar el texto y presionar el botón de búsqueda, se llama al método "Mover", que verifica si se realiza la operación de mover página o la operación de búsqueda y luego llama al método performSearch en el archivo Editor.js.

**jQuery - Envía una solicitud de servidor Ajax para el método SearchData**

Consulta la pestaña Editor.js a continuación para ver el código fuente del método performSearch, que obtiene el texto de entrada y una solicitud al método del servidor SearchData en el archivo _CanvasSave.aspx.cs_.

**El método web ASP.NET maneja las solicitudes del servidor**

Consulta la pestaña _Canvas.aspx.cs_ a continuación.
Ver la pestaña _Canvas.aspx.cs_ a continuación.

## Reemplazo de texto en archivo PDF

Utilizando el Editor de PDF Html5, puedes reemplazar el texto existente en los archivos PDF usando la opción Reemplazar Texto desde la barra de menús. Una vez que hagas clic en el elemento del menú Reemplazar Texto, se te presentará un cuadro de diálogo para introducir el texto a buscar y reemplazar.

### ¿Cómo funciona?

**HTML - Se hace clic en el elemento del menú "Reemplazar Texto" en la página**

Cuando haces clic en el elemento del menú "Reemplazar Texto", se te presenta un cuadro de diálogo de entrada para ingresar el texto a buscar y reemplazar. Después de ingresar el texto y presionar el botón Reemplazar, se llama al método "ReplaceText" en el archivo Editor.js.

**jQuery - Enviar solicitud de servidor Ajax para el método ReplaceText**

Ver la pestaña Editor.js a continuación para el código fuente del método ReplaceText, que obtiene el texto de entrada del cuadro de diálogo de texto de entrada y una solicitud al método de servidor ReplaceText en el archivo CanvasSave.aspx.cs.

**Método web ASP.NET maneja las solicitudes del servidor**

Ver la pestaña Canvas.aspx.cs a continuación.
## Cargando Archivo PDF con Campos de Formulario

Usando el Editor de PDF Html5, puedes cargar y trabajar con un archivo PDF que contiene campos de formulario. Una vez que el archivo con campos de formulario se carga en el editor, todos los campos de formulario se cargan para su edición. En nuestra próxima sección, discutiremos los detalles técnicos detrás de esta característica.

### ¿Cómo funciona?

**HTML - Se hace clic en el elemento del menú "Abrir Desde Computadora".**

Cuando haces clic en el elemento del menú "Abrir Desde Computadora", puedes subir el archivo de entrada que contiene los campos de formulario utilizando el diálogo de carga de archivos. Después de que el archivo se haya subido, se llama al método "fileSelected" en el archivo Editor.js.

**jQuery - Enviar solicitud al servidor para el método ProcessRequest**

El archivo se publica en el servidor y se llama al método "ProcessRequest" en el archivo CanvasSave.aspx.cs.

**Método web ASP.NET maneja las solicitudes del servidor**

Ver pestaña Canvas.aspx.cs a continuación.
**Cargando campos de formulario en el lienzo**

Vea la pestaña Editor.js a continuación, el método manageFields en Editor.js se utiliza para generar todos los campos en el lienzo basándose en la información enviada desde el lado del servidor. Dibuja controles de campo HTML utilizando la información de tipo y ubicación del lado del servidor en el lienzo.

## Resaltando Campos de Formulario Requeridos

Usando Html5 PDF Editor, puedes resaltar los campos de formulario requeridos en el editor. Una vez que el archivo con campos de formulario se carga en el editor, todos los campos de formulario requeridos son resaltados para los usuarios para asistir en la edición. En nuestra próxima sección, discutiremos los detalles técnicos detrás de esta característica.

### ¿Cómo funciona?

**HTML - Se hace clic en el elemento de menú "Abrir Desde Computadora".**

Cuando haces clic en el elemento de menú "Abrir Desde Computadora", puedes subir el archivo de entrada que contiene los campos de formulario utilizando el diálogo de carga de archivos. Después de que el archivo se sube, se llama al método "fileSelected" en el archivo Editor.js.

**jQuery - Envía solicitud al servidor para el método ProcessRequest**
**jQuery - Envío de solicitud de servidor para el método ProcessRequest**

El archivo se publica en el servidor y se llama al método "ProcessRequest" en el archivo CanvasSave.aspx.cs.

**Método web ASP.NET maneja solicitudes del servidor**

Vea la pestaña Canvas.aspx.cs a continuación. Basado en el parámetro del formulario pasado, el archivo a subir se guarda en el servidor, el método ImageConverter convierte el archivo subido en imágenes y se llama al método "CheckFields", que utiliza la clase Aspose.PDF.InteractiveFeatures.Forms para verificar todos los campos del formulario y recopilar la información sobre los campos, es decir, Tipo de Campo, Ubicación, etc. Después de obtener los detalles de todos los campos del formulario, obtenemos la información de si un campo del formulario es requerido usando el método Aspose.PDF.Facades.IsRequiredField y devolvemos la colección de campos al método ImageConverter. El método ImageConverter devuelve el control al método "fileSelected" en Editor.js

**Carga de campos de formulario en el lienzo**

Vea la pestaña Editor.js a continuación, el método manageFields en Editor.js se utiliza para generar todos los campos en el lienzo basado en la información enviada desde el lado del servidor.
Vea la pestaña Editor.js a continuación, el método manageFields en Editor.js se utiliza para generar todos los campos en el lienzo basado en la información enviada desde el lado del servidor.
