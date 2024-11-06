---
title: Introducción
type: docs
weight: 10
url: es/reportingservices/introduction/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

Aspose.PDF para Reporting Services ha sido muy notable para la generación de PDF a través de SQL Reporting Services durante muchos años y proporciona diversas opciones de configuración y parametrización que no son compatibles por defecto en SQL Reporting Services. Recientemente hemos recibido algunas solicitudes sobre la integración de Aspose.PDF para Reporting Services con SharePoint. Para este artículo, nos vamos a centrar en MS SharePoint 2010. Antes de continuar, asumimos que ya tienes una configuración de SharePoint Farm. En este ejemplo vamos a usar el completo SharePoint Cloud. Sin embargo, los pasos son similares para SharePoint Foundation Server.

{{% /alert %}}

{{% alert color="primary" %}}

Antes de continuar, echemos un vistazo a los temas de referencia que hemos consultado durante la preparación de este artículo.

- [Visión general de la integración de Reporting Services y tecnología SharePoint](http://msdn.microsoft.com/en-us/library/bb326358.aspx)
- [Deployment Topologies for Reporting Services in SharePoint Integrated Mode](http://msdn.microsoft.com/en-us/library/bb510781.aspx)
- [Configuring Reporting Services for SharePoint 2010 Integration](http://msdn.microsoft.com/en-us/library/bb326356.aspx)

{{% /alert %}}

## Configuración del Entorno

Nuestra configuración consiste en 4 servidores. Incluye un Controlador de Dominio, un Servidor SQL, un Servidor SharePoint y un servidor para Servicios de Reportes. Puedes optar por tener SharePoint y Servicios de Reportes en la misma máquina, lo cual simplificará esto un poco y señalaré algunas de las diferencias.

## Pre-Requisitos de Instalación

{{% alert color="primary" %}}

El complemento de Servicios de Reportes para SharePoint es uno de los componentes clave para que la integración funcione correctamente. El complemento necesita ser instalado en cualquiera de los Web Front Ends (WFE) que se encuentran en tu granja de SharePoint junto con el servidor de Administración Central. Uno de los nuevos cambios con SQL 2008 R2 y SharePoint 2010 es que el complemento 2008 R2 ahora es un requisito previo para la instalación de SharePoint. Esto significa que el complemento RS se instalará cuando procedas a instalar SharePoint. Esto se ha mostrado y destacado en la figura a continuación. Esto en realidad evita muchos problemas que vimos con SP 2007 y RS 2008 al instalar el complemento.

![todo:image_alt_text](introduction_1.png)

**Imagen1 :- Complemento de Servicios de Reportes para SharePoint**
{{% /alert %}}

## Autenticación de SharePoint

**Antes de que nos adentremos en las partes de integración de RS, una cosa que quiero señalar sobre la Granja de SharePoint es cómo configuras el Sitio. Más específicamente, cómo configuras la autenticación para el sitio. Si será Clásica o Basada en Reclamaciones. Esta elección es importante al principio. No creo que puedas cambiar esta opción una vez que esté hecha. Si puedes cambiarla, no sería un proceso simple.

NOTA: ***Reporting Services 2008 R2 NO es consciente de Reclamaciones***

Incluso si eliges que tu sitio de SharePoint use Reclamaciones, Reporting Services en sí no es consciente de Reclamaciones. Dicho esto, afecta cómo funciona la autenticación con Reporting Services. Entonces, ¿cuál es la diferencia desde la perspectiva de Reporting Services? Se reduce a si deseas reenviar las Credenciales de Usuario a la fuente de datos. Clásica:- Puede usar Kerberos y reenviar las credenciales del usuario a su fuente de datos de back-end (necesitarás usar Kerberos para eso). Reclamaciones:- Se utiliza un token de Reclamaciones y no un token de Windows. RS siempre usará Autenticación Confiable en este escenario y solo tendrá acceso al token SPUser. Necesitarás almacenar tus credenciales dentro de tu fuente de datos.

Clásica :- Puede usar Kerberos y reenviar las credenciales del usuario a su fuente de datos de back-end (necesitarás usar Kerberos para eso).
Claims :- Se utiliza un token de Claims y no un token de Windows. RS siempre usará Autenticación Confiable en este escenario y solo tendrá acceso al token SPUser. Necesitarás almacenar tus credenciales dentro de tu fuente de datos.

Por ahora solo queremos centrarnos en la configuración de RS. En este punto, SharePoint está instalado en mi servidor de SharePoint y configurado con un sitio de autenticación clásica en el puerto 80. En el servidor RS, acabo de instalar Reporting Services y eso es todo.