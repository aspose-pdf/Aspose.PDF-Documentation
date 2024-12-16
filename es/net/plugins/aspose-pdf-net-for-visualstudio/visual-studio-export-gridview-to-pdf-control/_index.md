---
title: Visual Studio Export GridView To PDF Control
type: docs
weight: 10
url: /es/net/visual-studio-export-gridview-to-pdf-control/
---

## Introducción

Export GridView To Pdf Control es un control de servidor ASP.NET que permite exportar el contenido de GridView a un documento Pdf utilizando [Aspose.PDF](http://www.aspose.com/.net/pdf-component.aspx). Agrega un botón **Exportar a Pdf** en la parte superior del control GridView. Al hacer clic en el botón, se exporta dinámicamente el contenido del control GridView a un documento Pdf y luego descarga automáticamente el archivo exportado en la ubicación de disco seleccionada por el usuario en solo un par de segundos.

### Características del Módulo

Esta versión inicial del control ofrece las siguientes características:

- Obtén una copia sin conexión de tu contenido favorito de GridView en línea para editar, compartir e imprimir en un documento Pdf muy popular.
- Heredado del control GridView ASP.NET predeterminado y, por lo tanto, tiene todas sus características y propiedades.
- Funciona con todas las versiones de .NET a partir de .NET 2.0.
- Capacidad para personalizar/localizar el texto del botón de exportación.
- Capacidad para personalizar/localizar el texto del botón de exportación.
- Opción para exportar en modo paisaje en caso de que el contenido de GridView sea más ancho y no quepa en el modo retrato predeterminado.
- Aplicar la apariencia de su propio tema en el botón de exportación usando CSS.
- Opción para agregar un encabezado personalizado en la parte superior del documento exportado.
- Opción para guardar cada documento exportado en el servidor en una ruta de disco configurable.
- Opción para exportar la página actual o todas las páginas cuando la paginación está habilitada.

## Requisitos del Sistema y Plataformas Soportadas

### Requisitos del Sistema

El control Export GridView To Pdf para Visual Studio se puede usar en cualquier sistema que tenga IIS y .NET framework 2.0 o superior instalado.

### Plataformas Soportadas

El control Export GridView To Pdf para Visual Studio es compatible con todas las versiones de ASP.NET que se ejecutan en .NET framework 2.0 o superior. Puede usar cualquiera de las siguientes versiones de Visual Studio para usar este control en sus aplicaciones ASP.NET

- Visual Studio 2005
- Visual Studio 2008
- Visual Studio 2010
- Visual Studio 2012
- Visual Studio 2013

## Descargando
## Descarga

Puedes descargar el Control Exportar GridView a PDF desde una de las siguientes ubicaciones:

- [CodePlex](https://asposevs.codeplex.com/releases/view/617022)
- [Github](https://github.com/aspose-pdf/Aspose.PDF-for-.NET/releases/tag/AsposeExportGridViewToPdfControl_1.0)

## Instalación

Es muy simple y fácil instalar el Control Exportar GridView a PDF, por favor sigue estos pasos simples:

### **Para Visual Studio 2010, 2012 y 2013**

1. Extrae el archivo zip descargado, por ejemplo, Aspose.PDF.GridViewExport_1.0.zip
1. Haz doble clic en el archivo VSIX Aspose.PDF.GridViewExport.vsix
1. Aparecerá un diálogo mostrándote las versiones de Visual Studio disponibles y compatibles instaladas en tu máquina
1. Selecciona las que quieras añadir el Control Exportar GridView a PDF.
1. Haz clic en Instalar

Recibirás un diálogo de éxito una vez que la instalación se haya completado.

**Nota:** Por favor, asegúrate de reiniciar Visual Studio para que los cambios tengan efecto.

### **Para Visual Studio 2005, 2008 y ediciones Express**

Por favor sigue estos pasos para integrar el Control Exportar GridView a PDF en Visual Studio para un fácil arrastrar y soltar, justo como otros controles ASP.NET.
Por favor, siga estos pasos para integrar el control Export GridView To Pdf en Visual Studio para un fácil arrastrar y soltar, como otros controles de ASP.NET

1. Extraiga el archivo zip descargado, es decir, Aspose.PDF.GridViewExport.NET2.0_1.0.zip
1. Asegúrese de ejecutar Visual Studio como Administrador

En el menú Herramientas, haga clic en Elegir elementos del cuadro de herramientas.

1. Haga clic en Examinar.
   Aparece el cuadro de diálogo Abrir.
1. Navegue hasta la carpeta extraída y seleccione Aspose.PDF.GridViewExport.dll
1. Haga clic en Aceptar.

Cuando abra un control aspx o ascx en el cuadro de herramientas del lado izquierdo, verá ExportGridViewToPdf bajo la pestaña General

![todo:image_alt_text](visual-studio-export-gridview-to-pdf-control_2.png)

## Usando

Una vez instalado, es muy fácil comenzar a usar este control en sus aplicaciones ASP.NET

|**Para el marco .NET 4.0 y superior**|**Para el marco .NET 2.0 y superior**|** |
| :- | :- | :- |
|Para aplicaciones que se ejecutan en el marco .NET 4.0 y superior en Visual Studio 2010 y superior, debería ver el control **ExportGridViewToPdf** en la pestaña **Aspose** en la barra de herramientas como se muestra a continuación.
|Para aplicaciones que se ejecutan en el framework .NET 4.0 y superior en Visual Studio 2010 y superior, deberías ver el control **ExportGridViewToPdf** en la pestaña **Aspose** en la barra de herramientas como se muestra a continuación.

### Agregar manualmente el control ExportGridViewToPdf

Si tienes problemas usando los métodos anteriores que utilizan el Toolbox de Visual Studio, puedes agregar manualmente este control a tu aplicación ASP.NET que se ejecute en cualquier framework de .NET superior a 2.0

1. Si estás utilizando Visual Studio asegúrate de ejecutarlo como Administrador
1. Agrega una referencia a **Aspose.PDF.GridViewExport.dll** disponible en el paquete de descarga extraído en tu proyecto ASP.NET o aplicación web. Asegúrate de que tu aplicación web/Visual Studio tenga acceso completo a esta carpeta, de lo contrario, podrías obtener una excepción de Acceso denegado.
1. Agrega esta línea en la parte superior de la página, control o MasterPage

```csharp
 <%@ Register assembly="Aspose.PDF.GridViewExport" namespace="Aspose.PDF.GridViewExport" tagprefix="aspose" %>
```
```csharp
 <aspose:ExportGridViewToPdf ID="ExportGridViewToPdf1" runat="server"></aspose:ExportGridViewToPdf>
```

### Preguntas Frecuentes

Preguntas y problemas comunes que podrías enfrentar al usar este Control

<div class="schema-faq-code" itemscope="" itemtype="https://schema.org/FAQPage">
    <div itemscope="" itemprop="mainEntity" itemtype="https://schema.org/Question" class="faq-question">
        <h3 itemprop="name" class="faq-q">1. No puedo ver el control ExportGridViewToPdf en la caja de herramientas</h3>
        <div itemscope="" itemprop="acceptedAnswer" itemtype="https://schema.org/Answer">
             <div itemprop="text" class="faq-a">
               <p><strong>Visual Studio 2010 y superiores</strong></p>
<ol><li>Asegúrate de haber instalado este control utilizando el archivo de extensión VSIX que se encuentra en el paquete descargado. Para verificarlo, ve a Herramientas -&gt; Extensiones y Actualizaciones. Bajo Instalado deberías ver 'Aspose Export Export GridView To Pdf Control'. Si no lo ves, intenta reinstalarlo.</li>
<li>Asegúrate de que tu aplicación web esté ejecutándose en el marco .NET 4.0 o superior, para versiones inferiores del marco .NET, por favor verifica el método alternativo mencionado anteriormente.
<li>Asegúrate de que tu aplicación web esté ejecutándose en el marco de .NET 4.0 o superior. Para versiones inferiores del marco de .NET, consulta el método alternativo mencionado anteriormente.
Versiones Anteriores de Visual Studio</li>
<li>Asegúrate de haber agregado manualmente este control a tu caja de herramientas según las instrucciones anteriores.</li></ol>
          </div>
        </div>
    </div>

    <div itemscope="" itemprop="mainEntity" itemtype="https://schema.org/Question" class="faq-question">
        <h3 itemprop="name" class="faq-q">2. Estoy recibiendo un error de 'Acceso denegado' al ejecutar la aplicación</h3>
        <div itemscope="" itemprop="acceptedAnswer" itemtype="https://schema.org/Answer">
             <div itemprop="text" class="faq-a">
               <ol>
               <li>Si estás experimentando este problema en producción, asegúrate de copiar ambos Aspose.PDF.dll y Aspose.PDF.GridViewExport.dll en tu carpeta bin.</li>
               <li>Si estás utilizando Visual Studio, asegúrate de ejecutarlo como Administrador aunque ya estés registrado como administrador.</li>

<li>Si estás utilizando Visual Studio, asegúrate de ejecutarlo como Administrador incluso si ya has iniciado sesión como administrador.</li>
</ol>
</div>
</div>
</div>
</div>

### **Propiedades del Control Aspose .NET Export GridView To Pdf**

Las siguientes propiedades están disponibles para configurar y utilizar las características interesantes proporcionadas por este control

|**Nombre de la Propiedad**|**Tipo**|**Ejemplo/Valores Posibles**|**Descripción**|
| :- | :- | :- | :- |
|ExportButtonText|string|Exportar a Pdf|Puedes utilizar esta propiedad para sobrescribir el texto predeterminado existente|
|ExportButtonCssClass|string|btn btn-primary|Clase Css que se aplica al div exterior del botón de exportación. Para aplicar css en el botón puedes usar .yourClass input|
|ExportInLandscape|bool|verdadero o falso|Si es verdadero cambia la orientación del documento de salida a horizontal. La predeterminada es Vertical|
| | | | |
|ExportFileHeading|string|Ejemplo de Reporte de Exportación GridView|Puedes utilizar etiquetas html para añadir estilo a tu encabezado|
|ExportOutputPathOnServer|string|c:/temp|Ruta de disco local en el servidor donde se guarda automáticamente una copia de la exportación|
```

|ExportOutputPathOnServer|string|c:/temp|Ruta local en el disco del servidor donde se guarda automáticamente una copia de la exportación.
|ExportDataSource|object|allRowsDataTable|Establece el objeto del cual este control de enlace de datos recupera su lista de elementos de datos. El objeto debe tener todos los datos que necesitan ser exportados. Esta propiedad se utiliza en adición a la propiedad normal DataSource y es útil cuando la paginación personalizada está habilitada y la página actual solo recupera filas para ser mostradas en pantalla.|
|LicenseFilePath|string| |Ruta local en el servidor al archivo de licencia. Por ejemplo, c:/inetpub/Aspose.PDF.lic|

Un ejemplo de control Exportar GridView a Pdf con todas las propiedades utilizadas se muestra a continuación

```csharp
<aspose:ExportGridViewToPdf Width="800px" ID="ExportGridViewToPdf1" ExportButtonText="Exportar a Pdf"
    CssClass="table table-hover table-bordered" ExportButtonCssClass="myClass" ExportOutputFormat="Doc"
    ExportInLandscape="true" ExportOutputPathOnServer="c:\\temp" ExportFileHeading="<h4>Informe Ejemplo</h4>"
    OnPageIndexChanging="ExportGridViewToPdf1_PageIndexChanging" PageSize="5" AllowPaging="True"
    LicenseFilePath="c:\\inetpub\\Aspose.PDF.lic"
    runat="server" CellPadding="4" ForeColor="#333333" GridLines="Both">
</aspose:ExportGridViewToPdf>
```
## Demostración en Video

Por favor, revisa [el video](https://www.youtube.com/watch?v=WNJ7T8u4JlM) a continuación para ver el módulo en acción.

### Soporte

Desde los primeros días de Aspose, sabíamos que solo ofrecer buenos productos no sería suficiente. También necesitábamos proporcionar un buen servicio. Somos desarrolladores también y entendemos lo frustrante que es cuando un problema técnico o una peculiaridad en el software te impide hacer lo que necesitas hacer. Estamos aquí para resolver problemas, no para crearlos.

Es por eso que ofrecemos soporte gratuito. Cualquiera que use nuestro producto, ya sea que lo hayan comprado o estén utilizando una evaluación, merece toda nuestra atención y respeto.

Puedes registrar cualquier problema o sugerencia relacionada con este Pdf utilizando cualquiera de las siguientes plataformas:

- [CodePlex](https://asposevs.codeplex.com/workitem/list/basic)
- [Visual Studio Gallery - P y R](https://visualstudiogallery.msdn.microsoft.com/fb8b9944-cfe5-44a9-8aa7-c785d32d1066)
- [Github](https://github.com/aspose-pdf/Aspose.PDF-for-.NET/issues)
- [Red de Desarrolladores de Microsoft - P y R](https://code.msdn.microsoft.com/Aspose-NET-Export-GridView-caddbb6d/view/Discussions#content)
- [Red de Desarrolladores de Microsoft - Preguntas y Respuestas](https://code.msdn.microsoft.com/Aspose-NET-Export-GridView-caddbb6d/view/Discussions#content)

### Extender y Contribuir

Aspose .NET Export GridView To Pdf para Visual Studio es de código abierto y su código fuente está disponible en los principales sitios web de código social que se enumeran a continuación. Se anima a los desarrolladores a descargar el código fuente y extender la funcionalidad según sus propios requisitos.

#### Código Fuente

Puedes obtener el último código fuente de una de las siguientes ubicaciones

- [CodePlex](https://asposevs.codeplex.com/SourceControl/latest#Aspose.PDF.GridViewExport/)
- [Github](https://github.com/aspose-pdf/Aspose.PDF-for-.NET/tree/master/Plugins/Visual%20Studio/Aspose.PDF.GridViewExport)

#### Cómo configurar el código fuente

Necesitas tener lo siguiente instalado para abrir y extender el código fuente

- Visual Studio 2010

Por favor sigue estos pasos simples para comenzar

1. Descarga/Clona el código fuente.
1.
1. Navegue hasta el último código fuente que haya descargado y abra **Aspose.PDF.GridViewExport.sln**

#### Resumen del código fuente

Hay tres proyectos en la solución

- Aspose.PDF.GridViewExport - Contiene el paquete VSIX y Server Pdf para .NET 4.0.
- Aspose.PDF.GridViewExport_DotNet_2.0 - GridView Pdf extendido para .NET 2.0
- Aspose.PDF.GridViewExport.Website - Proyecto web para probar el GridView Pdf exportable a Word
