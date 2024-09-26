---
title: Using Aspose.Pdf for .NET with Coldfusion
type: docs
weight: 300
url: /net/using-aspose-pdf-for-net-with-coldfusion/
description: Deberías trabajar con Aspose.Pdf para .NET con Coldfusion usando la clase PdfFileInfo
lastmod: "2021-07-14"
draft: false
---

{{% alert color="primary" %}}

En este artículo, explicaremos cómo usar Aspose.PDF para .NET con Coldfusion. Te ayudará a entender los detalles de la integración de Aspose.PDF para .Net y Coldfusion. Con la ayuda de un ejemplo simple, te mostraré el proceso de incorporación de la funcionalidad de Aspose.PDF para .Net en tus aplicaciones Coldfusion.

{{% /alert %}}

## Antecedentes

Aspose.PDF para .NET es un componente que también proporciona la capacidad de editar y manipular archivos PDF existentes.
Aspose.PDF para .NET es un componente que también proporciona la capacidad de editar y manipular archivos PDF existentes.

## Prerrequisito

Para poder ejecutar Aspose.PDF para .Net con Coldfusion, necesitarás IIS, .Net 2.0 y Coldfusion. He probado el componente usando IIS 5, .Net 2.0 y Coldfusion 8. Hay dos cosas más que necesitas asegurar mientras instalas Coldfusion. Primero, tienes que especificar qué sitio(s) bajo IIS estarán ejecutando Coldfusion. En segundo lugar, tendrás que seleccionar 'Servicios de Integración .Net' del instalador de Coldfusion. Los Servicios de Integración .Net te permiten acceder al ensamblado de componentes .Net en aplicaciones Coldfusion; en este caso el componente será Aspose.PDF para .NET.

## Explicación

Primero que todo, tienes que copiar el DLL (Aspose.PDF.dll) a un lugar desde donde lo estarás accediendo para uso posterior; esto se establecerá como una ruta y se asignará al atributo de ensamblaje de la etiqueta cfobject como se muestra a continuación:

```html
<cfobject type = ".NET" name = "fileinfo" 
        class = "Aspose.PDF.Facades.PdfFileInfo" 
        assembly = "C:/Aspose/Net/Assembly/Aspose.PDF.dll">
```
El atributo class en la etiqueta anterior apunta a Aspose.PDF. La clase Facades, que en este caso es PdfFileInfo. El atributo name es el nombre de la instancia de la clase y se utilizará más adelante en el código para acceder a métodos o propiedades de la clase. El atributo type especifica el tipo de componente - en nuestro caso es .Net.

Un punto importante que deberás tener en cuenta al usar el componente .Net en Coldfusion es que, cuando obtienes o estableces cualquier propiedad del objeto de la clase, debes seguir una estructura específica. Para establecer una propiedad usarás la sintaxis Set_propertyname, y para obtener un valor de propiedad usarás Get_propertyname.

Por ejemplo

Establecer un valor de propiedad:

```html
<cfset FilePath = ExpandPath("guia.pdf")>
```

Obtener un valor de propiedad:

```html
<cfoutput>#fileinfo.Get_title()#</cfoutput>
```

Un ejemplo básico pero completo para ayudarte a entender el proceso de uso de Aspose.PDF para .NET en Coldfusion se da a continuación.

### Mostremos la información del archivo PDF

```html
<!--- crear una instancia de la clase PdfFileInfo --->

<cfobject type = ".NET" name = "fileinfo" class = "Aspose.PDF.Facades.PdfFileInfo"

assembly = "C:/Aspose/Net/Assembly/Aspose.PDF.dll">

<!--- obtener la ruta del archivo pdf --->

<cfset FilePath = ExpandPath("guia.pdf")>

<!--- asignar la ruta del archivo pdf al objeto de la clase estableciendo su propiedad inputfile--->

<cfset fileinfo.Set_inputfile(FilePath)>

<!--- Mostrar información del archivo --->

<cfoutput><b>Título:</b>#fileinfo.Get_title()#</cfoutput><br/>
<cfoutput><b>Asunto:</b>#fileinfo.Get_subject()#</cfoutput><br/>
<cfoutput><b>Autor:</b>#fileinfo.Get_author()#</cfoutput><br/>
<cfoutput><b>Creador:</b>#fileinfo.Get_Creator()#</cfoutput><br/>

```
## Conclusión

{{% alert color="primary" %}}
En este artículo, hemos visto que si seguimos algunas reglas básicas de integración de Coldfusion y .Net, podemos incorporar mucha funcionalidad y flexibilidad relacionadas con la manipulación de documentos PDF, utilizando Aspose.PDF para .NET en nuestras aplicaciones Coldfusion.
{{% /alert %}}
