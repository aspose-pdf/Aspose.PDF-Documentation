---
title: Configuración de Reporting Services y SharePoint
linktitle: Configuración de Reporting Services y SharePoint
type: docs
weight: 40
url: /es/reportingservices/reporting-services-and-sharepoint-configuration/
lastmod: "2026-06-19"
---

{{% alert color="primary" %}}

Ahora que SharePoint está instalado y configurado en el servidor RS y RS está configurado a través del Reporting Services Configuration Manager, podemos pasar a la configuración dentro de Central Admin. RS 2008 R2 ha simplificado mucho este proceso. Antes teníamos un proceso de 3 pasos que debías realizar para que funcionara. Ahora solo tenemos un paso.

{{% /alert %}}

{{% alert color="primary" %}}

Queremos ir al sitio web del Administrador Central y luego a Configuración General de la Aplicación. Hacia la parte inferior veremos Reporting Services.

![todo:image_alt_text](reporting-services-and-sharepoint-configuration_1.png)
**Image1**:- diálogo de configuración de SharePoint

Seleccione el enlace "Reporting Services Integration". Se mostrará la siguiente pantalla.

![todo:image_alt_text](reporting-services-and-sharepoint-configuration_2.png)
**Image2**:- Especificar credenciales de integración de Reporting Services

{{% /alert %}}

## URL del servicio web:

**Proporcionaremos la URL del servidor de informes que encontramos en el Administrador de configuración de Reporting Services.**

## Modo de autenticación:

**También seleccionaremos un modo de autenticación. El siguiente enlace de MSDN detalla qué son estos.
Resumen de seguridad para Reporting Services en modo integrado de SharePoint**

{{% alert color="primary" %}}

**En resumen, si su sitio está usando autenticación de reclamos, siempre usará autenticación confiable independientemente de lo que elija aquí. Si desea pasar credenciales de Windows, debería elegir autenticación de Windows. Para la autenticación confiable, pasaremos el token SPUser y no dependeremos de la credencial de Windows. También querrá usar autenticación confiable si ha configurado sus sitios en modo clásico para NTLM y RS está configurado para NTLM. Kerberos sería necesario para usar autenticación de Windows y pasarla a su fuente de datos.**

{{% /alert %}}

## Activar característica:

{{% alert color="primary" %}}

**Esto le brinda una opción para activar los Reporting Services en todas las colecciones de sitios, o puede elegir en cuáles desea activarlos. Esto simplemente significa qué sitios podrán usar Reporting Services. Cuando esté listo, debería ver los siguientes resultados**

![todo:image_alt_text](reporting-services-and-sharepoint-configuration_3.png)

**Image3:**- Integración exitosa de Reporting Services con el entorno SharePoint
{{% /alert %}}

{{% alert color="primary" %}}

Volviendo a la URL de ReportServer, deberíamos ver algo similar a lo siguiente

![todo:image_alt_text](reporting-services-and-sharepoint-configuration_4.png)

**Image4:**- Reporting Services está conectado exitosamente con el entorno SharePoint

**NOTE:** ***Si su sitio SharePoint está configurado para SSL, no aparecerá en esta lista. Es un problema conocido y no significa que haya un problema. Sus informes deberían seguir funcionando.***
{{% /alert %}}

{{% alert color="primary" %}}

Ahora que hemos integrado con éxito ambos productos, estamos listos para usar Reporting Services en SharePoint 2010. Al igual que la versión anterior, tenemos una característica (activada cuando configuramos la integración de Reporting Services) en la "Site Collection Feature". Además, la instalación agregó 3 tipos de contenido a nuestro sitio. En la Imagen 7 podemos ver 2 de esos tipos de contenido añadidos en una biblioteca de documentos para crear un informe personalizado usando, como podemos ver en la Imagen 5 a continuación.

![todo:image_alt_text](reporting-services-and-sharepoint-configuration_5.png)

**Image5:**- Report Builder

El "Reporter Builder" es un control ActiveX, por lo que necesitamos descargarlo en el servidor, como podemos ver en la Imagen 6 a continuación.

![todo:image_alt_text](reporting-services-and-sharepoint-configuration_6.png)

**Image6:**- Descargar e instalar Report Builder
{{% /alert %}}

{{% alert color="primary" %}}

Una vez completado el proceso de descarga, cargue el control “Report Builder”. Ahora estamos listos para diseñar nuestro primer informe, como se muestra en Image7 a continuación.

![todo:image_alt_text](reporting-services-and-sharepoint-configuration_7.png)

**Image7:**- Report Builder – Asistente de generación de nuevo informe
{{% /alert %}}

{{% alert color="primary" %}}

Después de crear nuestro informe, podemos guardarlo en la biblioteca de documentos creada para colocar los informes en nuestro SharePoint 2010. El otro tipo de contenido debe usarse para crear una conexión compartida como fuente de datos y guardarla en una biblioteca de documentos en SharePoint. Podemos crear una biblioteca de documentos, agregar este tipo de contenido y luego tendremos nuestras conexiones disponibles para cambiar la fuente de datos de los informes.

![todo:image_alt_text](reporting-services-and-sharepoint-configuration_8.png)

**Image8:**- Integración exitosa de Aspose.PDF para Reporting Services con MS SharePoint
{{% /alert %}}



