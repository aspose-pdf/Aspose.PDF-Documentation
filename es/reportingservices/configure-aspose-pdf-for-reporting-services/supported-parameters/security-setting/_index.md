---
title: Configuración de seguridad
linktitle: Configuración de seguridad
type: docs
weight: 30
url: /es/reportingservices/security-setting/
lastmod: "2026-06-19"
---

{{% alert color="primary" %}}

La seguridad siempre ha sido el tema más importante en todos los campos, ya sea la protección de una red o de un documento PDF. Los documentos se aseguran por muchas razones posibles: el autor del documento puede querer mantener seguro el contenido del documento y no desea permitir que otros lo modifiquen, etc.

Aspose.Pdf for Reporting Services se ha tomado especial cuidado de estos aspectos de seguridad al proporcionar estas funciones a los desarrolladores que pueden ser útiles para proteger sus documentos PDF. Por lo tanto, contiene una serie de parámetros que permiten a los desarrolladores aplicar diferentes medidas de seguridad a los documentos PDF.

Una de estas medidas es proteger con contraseña el documento PDF durante la encriptación. También puede restringir o permitir la modificación del contenido, la copia del contenido, la impresión del documento o permitir/desactivar el relleno de formularios. Estas funciones, en este momento, no son compatibles con el Exportador PDF predeterminado de SQL Reporting Services, pero puede implementar estas funciones utilizando Aspose.Pdf for Reporting Services. Simplemente añada los parámetros de seguridad correspondientes a un informe o a un archivo de configuración del servidor de informes, y podrá crear documentos PDF seguros con privilegios limitados.

Actualmente, el renderizador Aspose.Pdf para Reporting Services admite los siguientes atributos de seguridad:

{{% /alert %}}

{{% alert color="primary" %}}

**Nombre del parámetro**: Contraseña de usuario  
**Tipo de dato**: Cadena  
**Valores admitidos**: Cualquier texto sin formato

**Nombre del parámetro**: Contraseña maestra  
**Tipo de dato**: Cadena  
**Valores admitidos**: Cualquier texto sin formato 

**Nombre del Parámetro**: IsCopyingAllowed  
**Tipo de dato**: Boolean  
**Valores compatibles**: True, False (default)  

**Nombre del Parámetro**: IsPrintingAllowed  
**Tipo de dato**: Boolean  
**Valores compatibles**: True, False (default)  

**Nombre del Parámetro**: IsContentsModifyingAllowed  
**Tipo de dato**: Boolean  
**Valores compatibles**: True, False (default)  

**Nombre del Parámetro**: IsFormFillingAllowed  
**Tipo de dato**: Boolean  
**Valores compatibles**: True, False (default)  

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


