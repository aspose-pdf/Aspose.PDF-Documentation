---
title: Configurando Reporting Services
linktitle: Configurando Reporting Services
type: docs
weight: 20
url: /es/reportingservices/setting-up-reporting-services/
lastmod: "2026-06-19"
---

{{% alert color="primary" %}}

Nuestro primer destino en el servidor Reporting Services es el Administrador de Configuración de Reporting Services.

{{% /alert %}}

## Cuenta de servicio:

**Asegúrese de comprender qué cuenta de servicio está utilizando para Reporting Services. Si encontramos problemas, pueden estar relacionados con la cuenta de servicio que está usando. El valor predeterminado es Network Service. Cuando vamos a desplegar nuevas compilaciones, siempre usamos cuentas de dominio, porque es allí donde probablemente surjan problemas. Para esta instancia del servidor, hemos utilizado una cuenta de dominio llamada RSService.**

![todo:image_alt_text](setting-up-reporting-services_1.png)

**Image1:- Configuración de la cuenta de servicio**

## URL del Servicio Web:

{{% alert color="primary" %}}

**Necesitaremos configurar la URL del Servicio Web. Este es el directorio virtual (vdir) de ReportServer que aloja los Servicios Web que usa Reporting Services, y con lo que SharePoint se comunicará. A menos que desees personalizar las propiedades del vdir (p. ej., SSL, puertos, encabezados de host, etc…) deberías poder simplemente hacer clic en Aplicar aquí y estar listo para usar.**
![todo:image_alt_text](setting-up-reporting-services_2.png)

**Image2:- Configuración de la URL del Servicio Web Una vez que la URL del Servicio Web esté configurada, deberías poder ver los siguientes resultados**

![todo:image_alt_text](setting-up-reporting-services_3.png)

**Image3:- Configuración exitosa de la URL del Servicio Web**
{{% /alert %}}

## Base de datos:

**Necesitamos crear la base de datos del catálogo de Reporting Services. Esto puede ubicarse en cualquier motor de base de datos SQL 2008 o SQL 2008 R2. SQL11 también funcionaría bien, pero todavía está en BETA. Esta acción creará dos bases de datos, ReportServer y ReportServerTempDB, por defecto.**

{{% alert color="primary" %}}
**El otro paso importante con esto es asegurarse de que elija SharePoint Integrated para el tipo de base de datos. Una vez que se ha hecho esta elección, no se puede cambiar.**

![todo:image_alt_text](setting-up-reporting-services_4.png)

**Image4:- Creando base de datos del servidor de informes**

![todo:image_alt_text](setting-up-reporting-services_5.png)

**Image5:- Configuración del servidor de bases de datos y tipo de autenticación**

![todo:image_alt_text](setting-up-reporting-services_6.png)

**Image6:- Configuración del nombre de la base de datos y modo**
{{% /alert %}}

**Para las credenciales, así es como el Report Server se comunicará con el SQL Server. La cuenta que seleccione recibirá ciertos derechos dentro de la base de datos Catalog así como en algunas de las bases de datos del sistema a través del RSExecRole. MSDB es una de estas bases de datos para el uso de suscripciones ya que utilizamos SQL Agent.**

![todo:image_alt_text](setting-up-reporting-services_7.png)

**Image7:- Configuración de las credenciales de la base de datos del Report Server**

{{% alert color="primary" %}}

**Una vez que se especifican las credenciales de la base de datos, deberíamos poder obtener los resultados como se indica a continuación.**

![todo:image_alt_text](setting-up-reporting-services_8.png)

**Image8:- Progreso de creación de la base de datos del servidor de informes**

![todo:image_alt_text](setting-up-reporting-services_9.png)

**Image9:- Resumen de finalización de la base de datos del servidor de informes**
{{% /alert %}}

## URL del Administrador de Informes:

**Podemos omitir la URL de Report Manager ya que no se usa cuando estamos en modo integrado de SharePoint. SharePoint es nuestra interfaz frontal. Report Manager no funciona.**

## Claves de cifrado:

{{% alert color="primary" %}}
**Realice una copia de seguridad de sus claves de cifrado y asegúrese de saber dónde las guarda. Si se encuentra en una situación en la que necesita migrar la base de datos o restaurarla, las necesitará.**

![todo:image_alt_text](setting-up-reporting-services_10.png)

**Image10:- Copia de seguridad de la clave de cifrado del servidor de informes**
{{% /alert %}}

{{% alert color="primary" %}}
**¡Felicidades! Hemos configurado con éxito Reporting Services usando Configuration Manager. Si navegas a la URL en la pestaña Web Service URL, debería mostrar algo similar a lo siguiente.**

![todo:image_alt_text](setting-up-reporting-services_11.png)

**Image11:- Acceso al Report Server después de la instalación**

**Razón del error: SharePoint está instalado en nuestro WFE y hemos terminado de configurar Reporting Services. En este ejemplo, Reporting Services y SharePoint están en máquinas diferentes. Si estuvieran en la misma máquina, no habrías visto este error. Técnicamente necesitamos instalar SharePoint en la caja RS. Eso significa que IIS también se habilitará.**
{{% /alert %}}



