---
title: Instalar en el servidor de informes
linktitle: Instalar en el servidor de informes
type: docs
weight: 10
url: /reportingservices/install-to-report-server/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

Solo necesita seguir estos pasos si instala Aspose.PDF para Reporting Services manualmente, sin utilizar el instalador MSI. El instalador MSI realiza todas las acciones necesarias de instalación y registro automáticamente.

{{% /alert %}}

En los siguientes pasos, deberá copiar y modificar archivos en el directorio donde está instalado Microsoft SQL Server Reporting Services. El ensamblado SSRS 2016 se encuentra en el directorio \Bin\SSRS2016 del paquete zip; el ensamblado SSRS 2017 se encuentra en el directorio \Bin\SSRS2017; el ensamblado SSRS 2019 se encuentra en el directorio \Bin\SSRS2019; el ensamblaje SSRS 2022 se encuentra en el directorio \Bin\SSRS2022; el ensamblado del servidor de informes de Power BI se encuentra en el directorio \Bin\PowerBI.

**Paso 1.** Localice el directorio de instalación del servidor de informes. El directorio raíz de Microsoft SQL Server suele ser C:\Program Files\Microsoft SQL Server. El proceso adicional es ligeramente diferente para Reporting Services 2016, Reporting Services 2017 y versiones posteriores, y Power BI Report Server:

- Report Server 2016 se instala de forma predeterminada en el directorio C:\Program Files\Microsoft SQL Server\MSRS13.MSSQLSERVER\Reporting Services\ReportServer. Si utiliza instancias con nombres personalizados en lugar de la predeterminada, la ruta predeterminada será C:\Program Files\Microsoft SQL Server\MSRS13.[SSRSInstanceName]\Reporting Services\ReportServer
- Report Server 2017 y versiones posteriores se instalan de forma predeterminada en el directorio C:\Program Files\Microsoft SQL Server Reporting Services\SSRS\ReportServer.
- Power BI Report Server se instala de forma predeterminada en el directorio C:\Program Files\Microsoft Power BI Report Server\PBIRS\ReportServer.

En el siguiente texto, se hará referencia al directorio de instalación de Reporting Services (una de las rutas antes mencionadas) como `<Instance>`.

**Paso 2.** Copie Aspose.Pdf.ReportingServices.dll para la versión SSRS correspondiente a la carpeta `<Instance>\bin`.

**Paso 3.** Registre Aspose.PDF para Reporting Services como una extensión de renderizado. Abra el archivo `<Instance>\rsreportserver.config` y agregue las siguientes líneas en el elemento `<Render>`:

## Ejemplo

```xml
<Render>
...
<Extension Name="APPDF" Type="Aspose.Pdf.ReportingServices.Renderer,Aspose.Pdf.ReportingServices"/>
</Render>
```

**Paso 4.** Proporcione permisos de ejecución a Aspose.PDF para Reporting Services. Abra el archivo `<Instance>\rssrvpolicy.config` y agregue el siguiente texto como último elemento en el segundo elemento `<CodeGroup>` externo, que debe ser `<CodeGroup class="FirstMatchCodeGroup" version="1" PermissionSetName="Execution" Description="This code group grants MyComputer code Execution permission. ">):`.

## Ejemplo

```xml

 <CodeGroup>
...

<CodeGroup>
...

<!--Start here.-->

<CodeGroup class="UnionCodeGroup" version="1" PermissionSetName="FullTrust"

Name="Aspose.Pdf_for_Reporting_Services" Description="This code group grants full trust to the AP4SSRS assembly.">

<IMembershipCondition class="StrongNameMembershipCondition" version="1" PublicKeyBlob="00240000048000009400000006020000002400005253413100040000010001005542e99cecd28842dad186257b2c7b6ae9b5947e51e0b17b4ac6d8cecd3e01c4d20658c5e4ea1b9a6c8f854b2d796c4fde740dac65e834167758cff283eed1be5c9a812022b015a902e0b97d4e95569eb8c0971834744e633d9cb4c4a6d8eda03c12f486e13a1a0cb1aa101ad94943236384cbbf5c679944b994de9546e493bf " />

</CodeGroup>

<!--End here. -->

</CodeGroup>

</CodeGroup>
```

**Paso 5.** Verifique que Aspose.PDF para Reporting Services se haya instalado correctamente. Abra el portal web de Reporting Services y consulte la lista de formatos de exportación disponibles para un informe. Puede iniciar el portal web iniciando un navegador web y escribiendo la URL del portal web de Reporting Services en la barra de direcciones (de forma predeterminada es `http://<Reporting_Services_server_name>/reports/`). Seleccione uno de los informes disponibles en su portal web y abra la lista desplegable Exportar. Debería ver la lista de formatos de exportación, incluidos los proporcionados por la extensión Aspose.PDF para Reporting Services. Seleccione PDF a través del elemento Aspose.PDF.

![Install to report server](install-to-report-server_1.png)

Haga clic en el elemento seleccionado. Generará el informe en el formato seleccionado, lo enviará al cliente y, dependiendo de la configuración de su navegador web, le mostrará el cuadro de diálogo Guardar archivo para elegir dónde guardar el informe exportado o descargará automáticamente el archivo a su carpeta de Descargas.

¡Felicitaciones, instaló Aspose.PDF para Reporting Services con éxito y exportó un informe como documento PDF!


