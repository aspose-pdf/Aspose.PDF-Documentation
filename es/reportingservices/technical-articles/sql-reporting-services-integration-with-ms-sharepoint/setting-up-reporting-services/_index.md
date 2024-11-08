---
title: Configurando Servicios de Reportes
type: docs
weight: 20
url: /es/reportingservices/setting-up-reporting-services/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

Nuestra primera parada en el Servidor de Servicios de Reportes es el Administrador de Configuración de Servicios de Reportes.

{{% /alert %}}

## Cuenta de Servicio:

**Asegúrese de entender qué cuenta de servicio está utilizando para los Servicios de Reportes. Si encontramos problemas, puede estar relacionado con la cuenta de servicio que está utilizando. El valor predeterminado es Servicio de Red. Cuando vamos a implementar nuevas compilaciones, siempre usamos Cuentas de Dominio, porque es donde es probable que encontremos problemas. Para esta instancia de servidor, hemos usado una Cuenta de Dominio llamada RSService.**

![todo:image_alt_text](setting-up-reporting-services_1.png)

**Imagen1:- Configuración de la cuenta de servicio**

## URL del Servicio Web:

{{% alert color="primary" %}}

**Necesitaremos configurar la URL del Servicio Web.** **Este es el directorio virtual (vdir) de ReportServer que aloja los Servicios Web que utiliza Reporting Services, y con el que se comunicará SharePoint. A menos que desees personalizar las propiedades del vdir (es decir, SSL, puertos, encabezados de host, etc...), deberías poder simplemente hacer clic en Aplicar aquí y estar listo para continuar.**

![todo:image_alt_text](setting-up-reporting-services_2.png)

**Imagen2:- Configuración de la URL del Servicio Web Una vez que se haya configurado la URL del servicio web, deberías poder ver los siguientes resultados**

![todo:image_alt_text](setting-up-reporting-services_3.png)

**Imagen3:- Configuración exitosa de la URL del servicio web**
{{% /alert %}}

## Base de datos:

**Necesitamos crear la Base de Datos del Catálogo de Reporting Services. Esto se puede colocar en cualquier Motor de Base de Datos SQL 2008 o SQL 2008 R2. SQL11 también funcionaría bien, pero todavía está en BETA. Esta acción creará dos bases de datos, ReportServer y ReportServerTempDB, por defecto.**

{{% alert color="primary" %}}
**El otro paso importante con esto es asegurarse de que elijas SharePoint Integrated para el tipo de base de datos.  Una vez que se toma esta decisión, no se puede cambiar.**

![todo:image_alt_text](setting-up-reporting-services_4.png)

**Imagen4:- Creando la base de datos del servidor de informes**

![todo:image_alt_text](setting-up-reporting-services_5.png)

**Imagen5:- Configurando el servidor de base de datos y el tipo de autenticación**

![todo:image_alt_text](setting-up-reporting-services_6.png)

**Imagen6:- Configurando el nombre de la base de datos y el Modo**
{{% /alert %}}

**Para las credenciales, así es como el Servidor de Informes se comunicará con el Servidor SQL. Cualquier cuenta que seleccione, se le otorgarán ciertos derechos dentro de la base de datos del Catálogo, así como algunas de las bases de datos del sistema a través del RSExecRole. MSDB es una de estas bases de datos para el uso de Suscripción ya que hacemos uso del Agente SQL.**

![todo:image_alt_text](setting-up-reporting-services_7.png)

**Imagen7:- Configurando las credenciales de la base de datos del Servidor de Informes**

{{% alert color="primary" %}}

**Una vez que se especifican las credenciales de la base de datos, deberíamos poder obtener los resultados especificados a continuación.**


![todo:image_alt_text](setting-up-reporting-services_8.png)
**Image8:- Progreso de creación de la base de datos del Servidor de Informes**

![todo:image_alt_text](setting-up-reporting-services_9.png)

**Image9:- Resumen de finalización de la base de datos del Servidor de Informes**
{{% /alert %}}

## URL del Administrador de Informes:

**Podemos omitir la URL del Administrador de Informes ya que no se utiliza cuando estamos en modo Integrado de SharePoint. SharePoint es nuestro frontend. El Administrador de Informes no funciona.**

## Claves de Cifrado:

{{% alert color="primary" %}}
**Haga una copia de seguridad de sus Claves de Cifrado y asegúrese de saber dónde las guarda. Si se encuentra en una situación en la que necesita migrar la base de datos o restaurarla, necesitará estas claves.**

![todo:image_alt_text](setting-up-reporting-services_10.png)

**Image10:- Copia de seguridad de la clave de cifrado del Servidor de Informes**
{{% /alert %}}

{{% alert color="primary" %}}
**¡Felicidades! Hemos configurado con éxito los Servicios de Informes utilizando el Administrador de Configuración. Si navega a la URL en la pestaña de la URL del Servicio Web, debería mostrar algo similar a lo siguiente.**

![todo:image_alt_text](setting-up-reporting-services_11.png)

**Image11:- Acceso al servidor de informes después de la instalación**

**Razón del error: SharePoint está instalado en nuestro WFE y hemos terminado de configurar los Servicios de Informe. En este ejemplo, los Servicios de Informe y SharePoint están en máquinas diferentes. Si estuvieran en la misma máquina, no verías este error. Técnicamente necesitamos instalar SharePoint en la caja de RS. Eso significa que IIS también estará habilitado.**  
{{% /alert %}}