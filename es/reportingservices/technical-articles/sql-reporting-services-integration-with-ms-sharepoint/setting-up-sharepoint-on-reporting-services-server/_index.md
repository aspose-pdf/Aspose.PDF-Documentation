---
title: Configuración de SharePoint en el servidor de Reporting Services
linktitle: Configuración de SharePoint en el servidor de Reporting Services
type: docs
weight: 30
url: /es/reportingservices/setting-up-sharepoint-on-reporting-services-server/
lastmod: "2026-06-19"
---

{{% alert color="primary" %}}

Ahora necesitamos ejecutar pasos similares a los que hicimos para el SharePoint WFE. Lo primero es pasar por la instalación de los requisitos previos de uisites y, una vez completada, iniciar la configuración de SharePoint.

{{% /alert %}}

Para la configuración elijo Server Farm y una instalación completa para que coincida con mi SharePoint Box, ya que no quiero una instalación independiente para SharePoint.

## Configuración de SharePoint

{{% alert color="primary" %}}

**En el Asistente de Configuración de SharePoint, queremos conectarnos a una granja existente.**

![todo:image_alt_text](setting-up-sharepoint-on-reporting-services-server_1.png)

**Imagen1:- Asistente de configuración de SharePoint**
{{% /alert %}}

{{% alert color="primary" %}}

**Luego lo apuntaremos a la base de datos SharePoint_Config que está usando nuestra granja. Si no sabes dónde está, puedes averiguarlo a través de Central Admin, en Configuración del sistema -> Manager Servers en esta granja.**

![todo:image_alt_text](setting-up-sharepoint-on-reporting-services-server_2.png)

**Imagen2:- Especificar configuración de la base de datos**

![todo:image_alt_text](setting-up-sharepoint-on-reporting-services-server_3.png)

**Imagen3:- Asistente de configuración de SharePoint**
{{% /alert %}}

{{% alert color="primary" %}}

**Una vez que el asistente haya terminado, eso es todo lo que necesitamos hacer en el servidor de informes por ahora. Volviendo a la URL del ReportServer, veremos otro error, pero eso se debe a que no lo hemos configurado a través del Administrador Central.**

![todo:image_alt_text](setting-up-sharepoint-on-reporting-services-server_4.png)

**Image4:- Error del servidor de informes**
{{% /alert %}}


