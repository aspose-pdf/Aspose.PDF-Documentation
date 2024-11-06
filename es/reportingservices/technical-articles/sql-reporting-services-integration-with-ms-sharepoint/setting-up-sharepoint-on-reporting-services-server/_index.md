---
title: Configuración de SharePoint en el Servidor de Servicios de Reportes
type: docs
weight: 30
url: es/reportingservices/setting-up-sharepoint-on-reporting-services-server/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

Ahora necesitamos realizar pasos similares a los que hicimos para el WFE de SharePoint. Lo primero es pasar por la instalación de los requisitos previos y una vez que esté hecho, iniciar la configuración de SharePoint.

{{% /alert %}}

Para la configuración elijo Granja de Servidores y una instalación completa para que coincida con mi Caja de SharePoint, ya que no quiero una instalación independiente para SharePoint.

## Configuración de SharePoint

{{% alert color="primary" %}}

**En el Asistente de Configuración de SharePoint, queremos conectar a una granja existente.**

![todo:image_alt_text](setting-up-sharepoint-on-reporting-services-server_1.png)

**Imagen1:- asistente de configuración de SharePoint**
{{% /alert %}}

{{% alert color="primary" %}}

**Luego lo dirigiremos a la base de datos SharePoint_Config que nuestra granja está utilizando.  Si no sabes dónde está, puedes averiguarlo a través del Administrador Central a través de Configuración del Sistema -> Administrar Servidores en esta granja.**

![todo:image_alt_text](setting-up-sharepoint-on-reporting-services-server_2.png)

**Imagen2:- Especificar configuración de la base de datos**

![todo:image_alt_text](setting-up-sharepoint-on-reporting-services-server_3.png)

**Imagen3:- Asistente de configuración de SharePoint**
{{% /alert %}}

{{% alert color="primary" %}}

**Una vez que el asistente haya terminado, eso es todo lo que necesitamos hacer en el Servidor de Reportes por ahora. Volviendo a la URL de ReportServer, veremos otro error, pero eso es porque no lo hemos configurado a través del Administrador Central.**

![todo:image_alt_text](setting-up-sharepoint-on-reporting-services-server_4.png)

**Imagen4:- Error del servidor de reportes**
{{% /alert %}}