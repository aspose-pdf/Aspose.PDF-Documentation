---
title: Introducción
linktitle: Introducción
type: docs
weight: 10
url: /es/reportingservices/introduction/
lastmod: "2026-06-19"
---

{{% alert color="primary" %}}

Aspose.PDF for Reporting Services ha sido muy notable para la generación de PDF a través de SQL Reporting Services durante muchos años y proporciona diversas opciones de configuración y parametrización que no son compatibles por defecto en SQL Reporting Services. Recientemente hemos recibido algunas solicitudes respecto a la integración de Aspose.PDF for Reporting Services con SharePoint. Para este artículo, nos centraremos en MS SharePoint 2010. Antes de continuar, asumimos que ya tiene una granja de SharePoint configurada. En este ejemplo usaremos SharePoint Cloud completo. Sin embargo, los pasos son similares para SharePoint Foundation Server.

{{% /alert %}}

{{% alert color="primary" %}}

Antes de continuar, echemos un vistazo a los temas de referencia que hemos consultado durante la preparación de este artículo.

- [Visión general de Reporting Services y la integración tecnológica de SharePoint](http://msdn.microsoft.com/en-us/library/bb326358.aspx)
- [Topologías de implementación para Reporting Services en modo integrado de SharePoint](http://msdn.microsoft.com/en-us/library/bb510781.aspx)
- [Configuración de Reporting Services para la integración de SharePoint 2010](http://msdn.microsoft.com/en-us/library/bb326356.aspx)

{{% /alert %}}

## Configuración del entorno

Nuestra configuración consta de 4 servidores. Incluye un controlador de dominio, un SQL Server, un SharePoint Server y un servidor para Reporting Services. Puede optar por tener SharePoint y Reporting Services en el mismo equipo, lo que simplificará un poco esto y señalaré algunas de las diferencias.

## Requisitos previos de instalación

{{% alert color="primary" %}}

El Reporting Services Add-In para SharePoint es uno de los componentes clave para que la integración funcione correctamente. El Add-In necesita instalarse en cualquiera de los Web Front Ends (WFE) que formen parte de su granja de SharePoint junto con el servidor Central Admin. Una de las nuevas modificaciones con SQL 2008 R2 & SharePoint 2010 es que el Add-In 2008 R2 ahora es un requisito previo para la instalación de SharePoint. Esto significa que el RS Add-In se desplegará cuando proceda a instalar SharePoint. Se ha mostrado y resaltado en la figura a continuación. Esto realmente evita muchos problemas que vimos con SP 2007 y RS 2008 al instalar el Add-In.

![todo:image_alt_text](introduction_1.png)

**Image1 :- Complemento de Reporting Services para Share Point**
{{% /alert %}}

## Autenticación de SharePoint

**Antes de sumergirnos en los componentes de integración de RS, una cosa que quiero destacar sobre la granja de SharePoint es cómo configuras el sitio. Más específicamente, cómo configuras la autenticación del sitio. Si será Clásica o Reclamos. Esta elección es importante al principio. No creo que puedas cambiar esta opción una vez que esté hecha. Si puedes cambiarla, no sería un proceso sencillo.**

NOTA: ***Reporting Services 2008 R2 no es compatible con Claims***

Incluso si eliges que tu sitio SharePoint utilice Claims, Reporting Services en sí no es consciente de Claims. Dicho esto, sí afecta cómo funciona la autenticación con Reporting Services. Entonces, ¿cuál es la diferencia desde la perspectiva de Reporting Services? Se reduce a si deseas reenviar las credenciales del usuario al origen de datos. Classic:- Puede usar Kerberos y reenviar las credenciales del usuario a tu origen de datos backend (será necesario usar Kerberos para ello). Claims:- Se utiliza un token Claims y no un token de Windows. RS siempre usará Trusted Authentication en este escenario y solo tendrá acceso al token SPUser. Necesitarás almacenar tus credenciales dentro de tu origen de datos.

Classic :- Puede usar Kerberos y reenviar las credenciales del usuario a tu origen de datos backend (será necesario usar Kerberos para ello).

Claims :- Se utiliza un token Claims y no un token de Windows. RS siempre usará Trusted Authentication en este escenario y solo tendrá acceso al token SPUser. Necesitarás almacenar tus credenciales dentro de tu origen de datos.

Por ahora solo queremos centrarnos en la configuración de RS. En este punto SharePoint está instalado en mi SharePoint Box y configurado con un sitio de autenticación clásica en el puerto 80. En el servidor RS acabo de instalar Reporting Services y eso es todo.


