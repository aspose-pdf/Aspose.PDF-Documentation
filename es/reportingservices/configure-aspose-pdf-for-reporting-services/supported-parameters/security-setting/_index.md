---
title: Security Setting
type: docs
weight: 30
url: es/reportingservices/security-setting/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

La seguridad siempre ha sido el tema más importante en cada campo, ya sea la protección de una red o de un documento PDF. Los documentos se aseguran por muchas razones posibles: el autor del documento puede querer mantener el contenido del documento seguro y no quiere permitir que otros lo cambien, etc.

Aspose.Pdf para Reporting Services ha tomado mucho cuidado en estos aspectos de seguridad al proporcionar estas características a los desarrolladores que pueden ser útiles para que ellos protejan sus documentos PDF. Por lo tanto, contiene una serie de parámetros que permiten a los desarrolladores aplicar diferentes medidas de seguridad a los documentos PDF.

Una de estas medidas es proteger con contraseña el documento PDF durante la encriptación. You can also restrict or allow contents modification, copying the content, document printing or allow/disable form filling. Estas características no son compatibles actualmente con el Exportador PDF de SQL Reporting Services por defecto, pero puedes implementar estas características usando Aspose.Pdf para Reporting Services. Solo añade los parámetros de seguridad correspondientes a un informe o a un archivo de configuración del servidor de informes, y podrás crear documentos PDF seguros con privilegios limitados.

Actualmente, el renderizador Aspose.Pdf para Reporting Services admite los siguientes atributos de seguridad:

{{% /alert %}}

{{% alert color="primary" %}}

**Parameter Name**: User Password  
**Date Type**: String  
**Values supported**: Any plain text

**Parameter Name**: Master Password  
**Date Type**: String  
**Values supported**: Any plain text 

**Parameter Name**: IsCopyingAllowed  
**Date Type**: Boolean  
**Values supported**: True, False (default)  

**Parameter Name**: IsPrintingAllowed  
**Date Type**: Boolean  

**Values supported**: True, False (default)  
**Parameter Name**: IsContentsModifyingAllowed  
**Date Type**: Boolean  
**Values supported**: True, False (predeterminado)  

**Parameter Name**: IsFormFillingAllowed  
**Date Type**: Boolean  
**Values supported**: True, False (predeterminado)  

**Ejemplo**

{{< highlight csharp >}}

<Render>
…
    <Extension Name="APPDF" Type="Aspose.Pdf.ReportingServices.Renderer,Aspose.Pdf.ReportingServices">
    <Configuration>
    <UserPassword>aspose</UserPassword>
    <IsCopyingAllowed>False</IsCopyingAllowed>
    <IsPrintingAllowed>False</IsPrintingAllowed>
    </Configuration>
    </Extension>
</Render>

{{< /highlight >}}

{{% /alert %}}