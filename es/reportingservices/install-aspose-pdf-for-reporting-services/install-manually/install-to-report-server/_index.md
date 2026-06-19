---
title: Instalar en Report Server
linktitle: Instalar en Report Server
type: docs
weight: 10
url: /es/reportingservices/install-to-report-server/
lastmod: "2026-06-19"
---

{{% alert color="primary" %}}

Solo necesita seguir estos pasos si instala Aspose.PDF for Reporting Services manualmente, sin usar el instalador MSI. El instalador MSI realiza todas las acciones de instalación y registro necesarias automáticamente.

{{% /alert %}}

En los siguientes pasos, necesitará copiar y modificar archivos en el directorio donde Microsoft SQL Server Reporting Services está instalado. El ensamblado SSRS 2016 se encuentra en el directorio \Bin\SSRS2016 del paquete zip; el ensamblado SSRS 2017 se encuentra en el directorio \Bin\SSRS2017; el ensamblado SSRS 2019 se encuentra en el directorio \Bin\SSRS2019; el ensamblado SSRS 2022 se encuentra en el directorio \Bin\SSRS2022; el ensamblado de Power BI Report Server se encuentra en el directorio \Bin\PowerBI. 

{{% alert color="primary" %}}

**Paso 1.** Ubique el directorio de instalación del Report Server. El directorio raíz de Microsoft SQL Server suele ser C:\Program Files\Microsoft SQL Server. El proceso posterior es ligeramente diferente para Reporting Services 2016, Reporting Services 2017 y versiones posteriores, y Power BI Report Server:

- Report Server 2016, por defecto, se instala en el directorio C:\Program Files\Microsoft SQL Server\MSRS13.MSSQLSERVER\Reporting Services\ReportServer. Si está utilizando instancias con nombres personalizados en lugar de la predeterminada, la ruta por defecto será C:\Program Files\Microsoft SQL Server\MSRS13.[SSRSInstanceName]\Reporting Services\ReportServer
- Report Server 2017 y versiones posteriores, por defecto, se instala en el directorio C:\Program Files\Microsoft SQL Server Reporting Services\SSRS\ReportServer.
- Power BI Report Server, por defecto, se instala en el directorio C:\Program Files\Microsoft Power BI Report Server\PBIRS\ReportServer.

En el texto siguiente, el directorio de instalación de Reporting Services (una de las rutas mencionadas) será referenciado como ```<Instance>```.
{{% /alert %}}

{{% alert color="primary" %}}
**Paso 2.** Copie Aspose.Pdf.ReportingServices.dll para la versión correspondiente de SSRS al ```<Instance>```\bin carpeta.
{{% /alert %}}

{{% alert color="primary" %}}
**Paso 3.** Registrar Aspose.Pdf for Reporting Services como una extensión de renderizado. Abra el ```<Instance>```\\rsreportserver.config archivo y agregue las siguientes líneas en el ```<Render>``` elemento:
{{% /alert %}}

**Ejemplo**

{{< highlight csharp >}}

 <Render>
...
<!--Start here.-->

<Extension Name="APPDF" Type="Aspose.Pdf.ReportingServices.Renderer,Aspose.Pdf.ReportingServices"/>

</Render>

{{< /highlight >}}

{{% alert color="primary" %}}
**Paso 4.** Proporcione Aspose.Pdf para Reporting Services con permisos para ejecutar. Abra el archivo ```<Instance>```\rssrvpolicy.config y añada el siguiente texto como el último elemento en el segundo al exterior elemento ```<CodeGroup>``` (que debería ser ```<CodeGroup class="FirstMatchCodeGroup" version="1" PermissionSetName="Execution" Description="This code group grants MyComputer code Execution permission. ">):```
{{% /alert %}}

**Ejemplo**

{{< highlight csharp >}}

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

{{< /highlight >}}

{{% alert color="primary" %}}
**Step 5.** Verifique que Aspose.Pdf for Reporting Services se haya instalado correctamente. Abra el portal web de Reporting Services y compruebe la lista de formatos de exportación disponibles para un informe. Puede iniciar el portal web abriendo un navegador y escribiendo la URL del portal web de Reporting Services en la barra de direcciones (por defecto es http://```<Reporting_Services_server_name>```/reports/). Seleccione uno de los informes disponibles en su portal web y abra la lista desplegable Export. Debería ver la lista de formatos de exportación, incluidos los proporcionados por la extensión Aspose.Pdf for Reporting Services. Seleccione el elemento PDF via Aspose.PDF.

 
{{% /alert %}}

![todo:image_alt_text](install-to-report-server_1.png)

Haga clic en el elemento seleccionado. Generará el informe en el formato seleccionado, lo enviará al cliente y, según la configuración de su navegador web, mostrará el cuadro de diálogo Guardar archivo para elegir dónde guardar el informe exportado, o descargará automáticamente el archivo en su carpeta Descargas.

{{% alert color="primary" %}}
¡Felicidades, ha instalado correctamente Aspose.Pdf para Reporting Services y ha exportado un informe como un documento PDF!
{{% /alert %}}





