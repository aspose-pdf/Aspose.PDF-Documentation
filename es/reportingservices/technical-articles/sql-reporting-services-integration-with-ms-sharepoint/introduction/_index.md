---
title: Introducción
linktitle: Introducción
type: docs
weight: 10
url: /reportingservices/introduction/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

Aspose.PDF para Reporting Services ha sido muy notable para la generación de PDF a través de SQL Reporting Services desde hace muchos años y proporciona diversas opciones de configuración y parametrización que no son compatibles de forma predeterminada en SQL Reporting Services. Recientemente hemos recibido algunas solicitudes relacionadas con Aspose.PDF para la integración de Reporting Services con SharePoint. Para este artículo, nos centraremos en MS SharePoint 2010. Antes de continuar, asumimos que ya tiene una configuración de SharePoint Farm. En este ejemplo vamos a utilizar SharePoint Cloud completo. Sin embargo, los pasos son similares para SharePoint Foundation Server.

{{% /alert %}}

{{% alert color="primary" %}}

Antes de continuar, echemos un vistazo a los temas de referencia que hemos consultado durante la preparación de este artículo.

- [Descripción general de Reporting Services y la integración de la tecnología SharePoint](http://msdn.microsoft.com/en-us/library/bb326358.aspx)
- [Topologías de implementación para Reporting Services en modo integrado de SharePoint](http://msdn.microsoft.com/en-us/library/bb510781.aspx)
- [Configuración de Reporting Services para la integración de SharePoint 2010](http://msdn.microsoft.com/en-us/library/bb326356.aspx)

{{% /alert %}}

## Configuración del entorno

Nuestra configuración consta de 4 servidores. Incluye un controlador de dominio, un servidor SQL, un servidor SharePoint y un servidor para Reporting Services. Puede optar por tener SharePoint y Reporting Services en el mismo cuadro, lo que simplificará un poco esto y señalaré algunas de las diferencias.

## Requisitos previos a la instalación

{{% alert color="primary" %}}

El complemento Reporting Services para SharePoint es uno de los componentes clave para que la integración funcione correctamente. El complemento debe instalarse en cualquiera de los front-end web (WFE) que se encuentran en su granja de SharePoint junto con el servidor de administración central. Uno de los nuevos cambios con SQL 2008 R2 y SharePoint 2010 es que el complemento 2008 R2 ahora es un requisito previo para la instalación de SharePoint. Esto significa que el complemento RS se instalará cuando vaya a instalar SharePoint. Se muestra y resalta en la figura siguiente. En realidad, esto evita muchos problemas que vimos con SP 2007 y RS 2008 al instalar el complemento.

![Introduction](introduction_1.png)

**Imagen 1: complemento de Reporting Services para Share Point**
{{% /alert %}}

## Autenticación de SharePoint

**Antes de pasar a los aspectos de la integración RS, una cosa que quiero señalar sobre SharePoint Farm es cómo se configura el sitio. Más específicamente cómo se configura la autenticación para el sitio. Ya sea Clásico o Claims. Esta elección es importante al principio. No creo que puedas cambiar esta opción una vez hecho. Si puedes cambiarlo, no sería un proceso sencillo.

NOTA: ***Reporting Services 2008 R2 NO reconoce reclamaciones***

Incluso si elige su sitio de SharePoint para usar Claims, Reporting Services en sí no reconoce Claims. Dicho esto, sí afecta el funcionamiento de la autenticación con Reporting Services. Entonces, ¿cuál es la diferencia desde la perspectiva de Reporting Services? Todo se reduce a si desea reenviar las credenciales de usuario a la fuente de datos. Clásico: puede usar Kerberos y reenviar las credenciales del usuario a su fuente de datos de back-end (necesitará usar Kerberos para eso). Reclamaciones: - Se utiliza un token de Reclamaciones y no un token de Windows. RS siempre utilizará la autenticación de confianza en este escenario y solo tendrá acceso al token SPUser. Deberá almacenar sus credenciales dentro de su fuente de datos.

Clásico: puede usar Kerberos y reenviar las credenciales del usuario a su fuente de datos de back-end (necesitará usar Kerberos para eso).

Reclamaciones: - Se utiliza un token de Reclamaciones y no un token de Windows. RS siempre utilizará la autenticación de confianza en este escenario y solo tendrá acceso al token SPUser. Deberá almacenar sus credenciales dentro de su fuente de datos.

Por ahora sólo queremos centrarnos en la configuración de RS. En este punto, SharePoint está instalado en mi SharePoint Box y configurado con un sitio de autenticación clásico en el puerto 80. En el servidor RS acabo de instalar Reporting Services y eso es todo.
