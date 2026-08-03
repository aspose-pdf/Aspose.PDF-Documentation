---
title: Configuración de seguridad
linktitle: Configuración de seguridad
type: docs
weight: 30
url: /reportingservices/security-setting/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

La seguridad siempre ha sido el tema más importante en todos los campos, ya sea la protección de una red o un documento PDF. Los documentos se protegen por muchas razones posibles: el autor del documento puede querer mantener seguro el contenido del documento y no quiere permitir que otros lo cambien, etc.

Aspose.PDF para Reporting Services se ha ocupado mucho de estos aspectos de seguridad al proporcionar estas funciones a los desarrolladores que pueden resultarles útiles para proteger sus documentos PDF. Por lo tanto, contiene una serie de parámetros que permiten a los desarrolladores aplicar diferentes medidas de seguridad a los documentos PDF.

Una de estas medidas es proteger con contraseña el documento PDF durante el cifrado. También puede restringir o permitir la modificación de contenidos, copiar el contenido, imprimir documentos o permitir/deshabilitar el llenado de formularios. En este momento, estas funciones no son compatibles con el exportador de PDF predeterminado de SQL Reporting Services, pero puede implementarlas utilizando Aspose.PDF para Reporting Services. Simplemente agregue los parámetros de seguridad correspondientes a un informe o a un archivo de configuración del servidor de informes y podrá crear documentos PDF seguros con privilegios limitados.

Currently, Aspose.PDF for Reporting Services renderer supports following security attributes:

{{% /alert %}}

```text
Parameter Name: User Password  
Date Type: String  
Values supported: Any plain text
```

```text
Parameter Name: Master Password  
Date Type: String  
Values supported: Any plain text 
```

```text
Parameter Name: IsCopyingAllowed  
Date Type: Boolean  
Values supported: True, False (default) 
```

```text
Parameter Name: IsPrintingAllowed  
Date Type: Boolean  
Values supported: True, False (default)  
```

```text
Parameter Name: IsContentsModifyingAllowed  
Date Type: Boolean  
Values supported: True, False (default) 
```

```text
Parameter Name: IsFormFillingAllowed  
Date Type: Boolean  
Values supported: True, False (default)  
```

## Ejemplo

```xml
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
```

