---
title: Reporting Services y configuración de SharePoint
type: docs
weight: 40
url: /reportingservices/reporting-services-and-sharepoint-configuration/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

Ahora que SharePoint está instalado y configurado en el servidor RS y RS está configurado a través del Administrador de Configuración de Reporting Services, podemos pasar a la configuración dentro de la Administración Central. RS 2008 R2 ha simplificado mucho este proceso. Solíamos tener un proceso de 3 pasos que tenías que realizar para que esto funcionara. Ahora solo tenemos un paso.

{{% /alert %}}

{{% alert color="primary" %}}

Queremos ir al sitio web del Administrador Central y luego a Configuración General de la Aplicación. Hacia la parte inferior veremos Reporting Services.

![todo:image_alt_text](reporting-services-and-sharepoint-configuration_1.png)
**Image1**:- Diálogo de configuración de SharePoint

Seleccione el enlace "Integración de Reporting Services". Se mostrará la siguiente pantalla.

![todo:image_alt_text](reporting-services-and-sharepoint-configuration_2.png)
**Image2**:- Especificar credenciales de integración de Reporting Services

{{% /alert %}}

## URL del Servicio Web:

**Proporcionaremos la URL para el Servidor de Informes que encontramos en el Administrador de Configuración de Reporting Services.**

## Modo de Autenticación:

**También seleccionaremos un Modo de Autenticación. El siguiente enlace de MSDN detalla qué son.
Visión general de seguridad para Reporting Services en Modo Integrado de SharePoint**

{{% alert color="primary" %}}

**En resumen, si su sitio está utilizando Autenticación de Reclamaciones, siempre estará utilizando Autenticación Confiable sin importar lo que elija aquí. Si desea pasar credenciales de Windows, querrá elegir Autenticación de Windows. Para la Autenticación Confiable, pasaremos el token SPUser y no dependeremos de la credencial de Windows. También querrá usar Autenticación Confiable si ha configurado sus sitios en Modo Clásico para NTLM y RS está configurado para NTLM. Se necesitaría Kerberos para usar Autenticación de Windows y para pasar eso a su fuente de datos.**

{{% /alert %}}

## Activar característica:

{{% alert color="primary" %}}

**Esto le da la opción de activar los Servicios de Generación de Informes en todas las colecciones de sitios, o puede elegir en cuáles desea activarlo. Esto significa realmente en qué sitios podrán utilizar los Servicios de Generación de Informes. Cuando se haya hecho, debería ver los siguientes resultados**

![todo:image_alt_text](reporting-services-and-sharepoint-configuration_3.png)

**Imagen3:**- Integración exitosa de los Servicios de Generación de Informes con el entorno de SharePoint
{{% /alert %}}

{{% alert color="primary" %}}

Volviendo a la URL de ReportServer, deberíamos ver algo similar a lo siguiente

![todo:image_alt_text](reporting-services-and-sharepoint-configuration_4.png)

**Imagen4:**- Los Servicios de Generación de Informes están conectados exitosamente con el entorno de SharePoint

**NOTA:** ***Si su sitio de SharePoint está configurado para SSL, no aparecerá en esta lista. Es un problema conocido y no significa que haya un problema. Sus informes deberían seguir funcionando.***
{{% /alert %}}
{{% alert color="primary" %}}

Ahora que hemos integrado con éxito ambos productos, estamos listos para usar Servicios de Reportes en SharePoint 2010. Al igual que la versión anterior, tenemos una característica (activada cuando configuramos la Integración de Servicios de Reportes) en la “Funcionalidad de la Colección de Sitios”. Además, la instalación agregó 3 tipos de contenido para agregar a nuestro sitio. En la Imagen 7 podemos ver 2 de esos tipos de contenido agregados en una biblioteca de documentos para crear un informe personalizado, como podemos ver en la Imagen 5 a continuación.

![todo:image_alt_text](reporting-services-and-sharepoint-configuration_5.png)

**Imagen 5:**- Generador de Informes

El “Generador de Informes” es un control ActiveX, por lo que necesitamos descargarlo en el servidor, como podemos ver en la Imagen 6 a continuación.

![todo:image_alt_text](reporting-services-and-sharepoint-configuration_6.png)

**Imagen 6:**- Descargar e instalar Generador de Informes
{{% /alert %}}

{{% alert color="primary" %}}

Una vez que el proceso de descarga se haya completado, cargue el control “Generador de Informes”. Ahora estamos listos para diseñar nuestro primer informe, como se muestra en la Imagen 7 a continuación.

![todo:image_alt_text](reporting-services-and-sharepoint-configuration_7.png)

**Image7:**- Report Builder – Asistente de generación de nuevos informes  
{{% /alert %}}  

{{% alert color="primary" %}}  

Después de crear nuestro informe, podríamos guardarlo en la biblioteca de documentos creada para colocar los informes en nuestro SharePoint 2010. El otro tipo de contenido debe usarse para crear una conexión compartida como fuente de datos y guardarla en una biblioteca de documentos en SharePoint. Podemos crear una biblioteca de documentos, agregar este tipo de contenido y después podremos tener nuestras conexiones disponibles para cambiar la fuente de datos de los informes.

![todo:image_alt_text](reporting-services-and-sharepoint-configuration_8.png)

**Image8:**- Integración exitosa de Aspose.PDF para Reporting Services con MS SharePoint  
{{% /alert %}}