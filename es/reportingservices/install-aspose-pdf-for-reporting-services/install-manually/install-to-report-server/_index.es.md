---
title: Instalar en Report Server
type: docs
weight: 10
url: /reportingservices/install-to-report-server/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

Solo necesita seguir estos pasos si instala Aspose.PDF para Reporting Services manualmente, sin usar el instalador MSI. El instalador MSI realiza automáticamente todas las acciones necesarias de instalación y registro.

{{% /alert %}}

En los siguientes pasos, necesitará copiar y modificar archivos en el directorio donde está instalado Microsoft SQL Server Reporting Services. El ensamblado de SSRS 2016 se encuentra en el directorio \Bin\SSRS2016 del paquete zip; el ensamblado de SSRS 2017 se encuentra en el directorio \Bin\SSRS2017; el ensamblado de SSRS 2019 se encuentra en el directorio \Bin\SSRS2019; el ensamblado de SSRS 2022 se encuentra en el directorio \Bin\SSRS2022; el ensamblado de Power BI Report Server se encuentra en el directorio \Bin\PowerBI. 

{{% alert color="primary" %}}

**Paso 1.** Localice el directorio de instalación de Report Server. El directorio raíz para Microsoft SQL Server suele ser C:\Program Files\Microsoft SQL Server. El proceso posterior es ligeramente diferente para Reporting Services 2016, Reporting Services 2017 y posteriores, y Power BI Report Server:

- Report Server 2016 por defecto se instala en el directorio C:\Program Files\Microsoft SQL Server\MSRS13.MSSQLSERVER\Reporting Services\ReportServer. Si estás utilizando instancias nombradas personalizadas en lugar de la predeterminada, la ruta predeterminada será C:\Program Files\Microsoft SQL Server\MSRS13.[SSRSInstanceName]\Reporting Services\ReportServer
- Report Server 2017 y posteriores por defecto se instala en el directorio C:\Program Files\Microsoft SQL Server Reporting Services\SSRS\ReportServer.
- Power BI Report Server por defecto se instala en el directorio C:\Program Files\Microsoft Power BI Report Server\PBIRS\ReportServer.

En el siguiente texto, el directorio de instalación de los Reporting Services (una de las rutas mencionadas anteriormente) se referirá como ```<Instance>```.
{{% /alert %}}


{{% alert color="primary" %}}**Paso 2.** Copia Aspose.Pdf.ReportingServices.dll para la versión correspondiente de SSRS en la carpeta ```<Instance>```\bin.
{{% /alert %}}

{{% alert color="primary" %}}
**Paso 3.** Registra Aspose.Pdf para Reporting Services como una extensión de renderizado. Abre el archivo ```<Instance>```\rsreportserver.config y añade las siguientes líneas en el elemento ```<Render>```:
{{% /alert %}}

**Ejemplo**

{{< highlight csharp >}}

 <Render>
...
<!--Empieza aquí.-->

<Extension Name="APPDF" Type="Aspose.Pdf.ReportingServices.Renderer,Aspose.Pdf.ReportingServices"/>

</Render>

{{< /highlight >}}

{{% alert color="primary" %}}
**Paso 4.** Proporciona a Aspose.Pdf para Reporting Services permisos para ejecutar. Abre el archivo ```<Instance>```\rssrvpolicy.config y añade el siguiente texto como el último elemento en el segundo al exterior elemento ```<CodeGroup>``` (que debería ser ```<CodeGroup class="FirstMatchCodeGroup" version="1" PermissionSetName="Execution" Description="This code group grants MyComputer code Execution permission. ">):```

{{% /alert %}}

**Example**

{{< highlight csharp >}}

 <CodeGroup>
...

<CodeGroup>
...

<!--Comience aquí.-->

<CodeGroup class="UnionCodeGroup" version="1" PermissionSetName="FullTrust"

Name="Aspose.Pdf_for_Reporting_Services" Description="Este grupo de código otorga plena confianza a la asamblea AP4SSRS.">

<IMembershipCondition class="StrongNameMembershipCondition" version="1" PublicKeyBlob="00240000048000009400000006020000002400005253413100040000010001005542e99cecd28842dad186257b2c7b6ae9b5947e51e0b17b4ac6d8cecd3e01c4d20658c5e4ea1b9a6c8f854b2d796c4fde740dac65e834167758cff283eed1be5c9a812022b015a902e0b97d4e95569eb8c0971834744e633d9cb4c4a6d8eda03c12f486e13a1a0cb1aa101ad94943236384cbbf5c679944b994de9546e493bf " />

</CodeGroup>

<!--Termine aquí. -->

</CodeGroup>

</CodeGroup>

{{< /highlight >}}

{{% alert color="primary" %}}
**Paso 5.** Verifique que Aspose.Pdf para Servicios de Reportes se haya instalado correctamente. Abre el portal web de Reporting Services y verifica la lista de formatos de exportación disponibles para un informe. Puedes lanzar el portal web iniciando un navegador web y escribiendo la URL del portal web de Reporting Services en la barra de direcciones (por defecto es http://```<Reporting_Services_server_name>```/reports/). Selecciona uno de los informes disponibles en tu portal web y despliega la lista de exportación. Deberías ver la lista de formatos de exportación incluyendo los proporcionados por la extensión Aspose.Pdf para Reporting Services. Selecciona el elemento PDF vía Aspose.PDF.
{{% /alert %}}

Haz clic en el elemento seleccionado. Generará el informe en el formato seleccionado, lo enviará al cliente y, dependiendo de la configuración de tu navegador web, ya sea que te muestre el cuadro de diálogo Guardar archivo para elegir dónde guardar el informe exportado, o descargue automáticamente el archivo en tu carpeta de Descargas.

¡Felicidades, has instalado con éxito Aspose.Pdf para Reporting Services y exportado un informe como documento PDF!Lo siento, no puedo ayudar con eso.