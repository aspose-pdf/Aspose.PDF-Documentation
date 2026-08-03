---
title: Configurar SharePoint en el servidor de Reporting Services
linktitle: Configurar SharePoint en el servidor de Reporting Services
type: docs
weight: 30
url: /reportingservices/setting-up-sharepoint-on-reporting-services-server/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

Ahora debemos realizar pasos similares a los que hicimos para SharePoint WFE. Lo primero es realizar la instalación de requisitos previos y, una vez hecho esto, iniciar la configuración de SharePoint.

{{% /alert %}}

Para la configuración, elijo Server Farm y una instalación completa que coincida con mi SharePoint Box, ya que no quiero una instalación independiente para SharePoint.

## Configuración de SharePoint

{{% alert color="primary" %}}

**In the SharePoint Configuration Wizard, we want to connect to an existing farm.**

![SharePoint Configuration Wizard](setting-up-sharepoint-on-reporting-services-server_1.png)

**Imagen 1: Asistente de configuración de SharePoint**
{{% /alert %}}

{{% alert color="primary" %}}

**Luego lo apuntaremos a la base de datos SharePoint_Config que utiliza nuestra granja. Si no sabe dónde está, puede averiguarlo a través del Administrador central en Configuración del sistema -> Administrador de servidores en esta granja.**

![SharePoint Configuration Database](setting-up-sharepoint-on-reporting-services-server_2.png)

**Imagen2: - Especificar los ajustes de configuración de la base de datos**

![SharePoint Configuration Wizard](setting-up-sharepoint-on-reporting-services-server_3.png)

**Imagen 3: Asistente de configuración de SharePoint**
{{% /alert %}}

{{% alert color="primary" %}}

**Una vez finalizado el asistente, eso es todo lo que necesitamos hacer en el cuadro del servidor de informes por ahora. Volviendo a la URL de ReportServer, veremos otro error, pero eso se debe a que no lo hemos configurado a través del Administrador Central.**

![SharePoint Configuration Error](setting-up-sharepoint-on-reporting-services-server_4.png)

**Imagen 4: - Error del servidor de informes**
{{% /alert %}}
