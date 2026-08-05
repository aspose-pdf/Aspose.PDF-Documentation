---
title: Trabajando con JasperReports
linktitle: Trabajando con JasperReports
type: docs
weight: 10
url: /es/jasperreports/working-with-jasperreports/
description: Domine el trabajo con JasperReports usando Aspose.PDF. Cree y exporte informes detallados en formato PDF con funciones avanzadas.
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

Aspose.Words para JasperReports está disponible para una evaluación gratuita y por tiempo ilimitado desde la página de descarga. Las versiones de evaluación y licencia del producto son la misma descarga.

Cuando esté satisfecho con la versión de evaluación, [comprar una licencia](http://www.aspose.com/purchase/default.aspx). Asegúrese de comprender y aceptar los términos de la licencia.

{{% /alert %}}

La licencia está disponible para descargar desde la página de pedido una vez pagado el pedido. La licencia es un archivo XML de texto claro y firmado digitalmente. La licencia contiene información como el nombre del cliente, el producto adquirido y el tipo de licencia. No modifique el contenido del archivo de licencia: invalida la licencia.

Hay varias formas de activar una licencia:

- [Llame a setLicense](/pdf/es/jasperreports/working-with-jasperreports/#call-setlicense).
- [Establecer un parámetro de exportador en el código](/pdf/es/jasperreports/working-with-jasperreports/#set-the-licensefile-exporter-parameter-in-the-code).
- [Establezca un parámetro de exportador en **applicationContext.xml**](/pdf/es/jasperreports/working-with-jasperserver/).

Los dos primeros se utilizan con JasperReports, el último con JasperServer.

## Llame a setLicense

Este método se utiliza con JasperReports.

1. Descargue la licencia a su computadora y cópiela en la carpeta apropiada (por ejemplo, la carpeta de su aplicación o JasperReports\lib).
2. Agregue el siguiente código a su proyecto:

```java
import com.aspose.pdf.jr3_7_0.jasperreports.*;
try
{ 
    // create a stream object containing the license file
   FileInputStream fstream = new FileInputStream("C:\\Aspose.PDF.JasperReports.lic");  

    // Set the license through the stream object
 
   License license = new License();
   license.setLicense(fstream);
}
catch(Exception ex)
{
   System.out.println(ex.toString());
}

```

## Establezca el parámetro del exportador de archivos de licencia en el código

Este método se utiliza con JasperReports.

1. Descargue la licencia a su computadora y cópiela en la carpeta apropiada (por ejemplo, la carpeta de su aplicación o JasperReports\lib).
2. Agregue el siguiente código a su proyecto:

```java

import com.aspose.pdf.jr3_7_0.jasperreports.*;

com.aspose.pdf.jr3_7_0.jasperreports.JrPdfExporter exporter = new com.aspose.pdf.jr3_7_0.jasperreports.JrPdfExporter();
exporter.setParameter(PdfExporterParameter.LICENSE, "Aspose.PDF.JasperReports.lic");
exporter.exportReport();

```


